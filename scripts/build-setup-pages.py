#!/usr/bin/env python3
"""Build the per-app versions of set-up-your-ai from its one source.

    python3 scripts/build-setup-pages.py

Reads set-up-your-ai/SKILL.md and writes five pages next to it:
for-chatgpt.md, for-claude.md, for-claude-code.md, for-grok.md and
for-perplexity.md. SKILL.md is the only page anyone edits; these five are
thrown away and made again every run.

How it picks the text. It keeps whole sections by their H2 and H3 headings,
then drops the lines, bullets and sentences that belong to other apps. The
tables below hold only the first words of what it picks (the selectors),
never the page's text. Every selector has to find its target in SKILL.md,
and the headings have to be exactly the ones listed. If a later edit to
SKILL.md moves or renames something, the script stops with a plain message
and writes nothing, so it can't quietly make a broken page.

Python 3.9, standard library only. Same input, same output.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "set-up-your-ai")
SOURCE = os.path.join(FOLDER, "SKILL.md")

G, C, K, X, P = "chatgpt", "claude", "claude-code", "grok", "perplexity"
ALL = frozenset([G, C, K, X, P])
NONE = frozenset()
# Chat apps where the person can pick a model (from the dated app cards:
# ChatGPT Plus and up, Claude on every plan, Perplexity Pro and Max; Grok's
# chat model picker is UNVERIFIED, so its page leaves models out).
PICKER = frozenset([G, C, P])
MODELS = PICKER | {K}

# key, the app's name, the file it writes, the one line on what this
# version leaves out (navigation only; no app facts live here).
PAGES = [
    (G, "ChatGPT", "for-chatgpt.md",
     "For a code session with Codex, OpenAI's coding agent, use the full page"),
    (C, "Claude", "for-claude.md",
     "Claude Code has its own version, and the full page has every approval setting of Cowork, Claude's agent"),
    (K, "Claude Code", "for-claude-code.md",
     "The Claude app's own instructions box is in the Claude version, and Codex and Grok Build are on the full page"),
    (X, "Grok", "for-grok.md",
     "For Grok Build, xAI's coding agent, use the full page"),
    (P, "Perplexity", "for-perplexity.md",
     "For Perplexity's desktop app working in folders on your computer, use the full page"),
]

# Every H2 and H3 in SKILL.md, in order. Anything else and the script stops.
EXPECTED = [
    (2, "What this is"),
    (2, "Who it's for"),
    (2, "Words you'll see"),
    (2, "What you need"),
    (2, "What it does"),
    (2, "What it won't do"),
    (2, "Try it"),
    (2, "The rules the assistant follows"),
    (3, "The interview, one question at a time"),
    (3, "What you write, and what only they click"),
    (3, "The app-level instructions"),
    (3, "ChatGPT"),
    (3, "Claude"),
    (3, "Claude Code"),
    (3, "Grok"),
    (3, "Perplexity"),
    (3, "Gemini"),
    (3, "Code sessions: permission modes"),
    (3, "Models and effort"),
    (3, "My rule for tokens"),
    (3, "Hand-off to ai-project-setup"),
    (3, "Prove the instructions took"),
    (3, "Known failure modes"),
    (3, "Starting yours"),
]

# Which pages keep each section. Sections not named here go on every page.
SECTIONS = {
    "ChatGPT": {G},
    "Claude": {C},
    "Claude Code": {K},
    "Grok": {X},
    "Perplexity": {P},
    "Gemini": NONE,
    "Code sessions: permission modes": {K},
    "Models and effort": MODELS,
    "My rule for tokens": MODELS,
}

# Bullets, numbered items, paragraphs or code blocks kept only on some
# pages, found by how they start. Each must match exactly one.
UNITS = {
    "Who it's for": [
        ("Anyone about to let an AI work on files", {K}),
    ],
    "Words you'll see": [
        ("**Permission mode:**", {K}),
        ("**Effort:**", MODELS),
        ("**Thinking:**", MODELS),
        ("**Tokens:**", MODELS),
        ("**Terminal:**", {K}),
        ("**Home folder:**", {K}),
        ("**API key:**", {K}),
        ("**Usage credits (Claude):**", {C, K}),
        ("**Cowork:**", {C}),
    ],
    "What you need": [
        ("For a code session, a computer.", {K}),
    ],
    "What it does": [
        ("For a code session,", {K}),
    ],
    "What it won't do": [
        ("Recommend a never-ask permission mode", {K}),
    ],
    "The app-level instructions": [
        ("Where the plan lets them pick a model", MODELS),
        ("For Grok, keep the who-I-am line", {X}),
        ("For a code session, the same text goes", {K}),
        ("```\nWork only inside the folder", {K}),
    ],
    "ChatGPT": [
        ("**Codex, OpenAI's coding agent:**", NONE),
    ],
    "Grok": [
        ("**Grok Build, xAI's coding agent", NONE),
    ],
    "Hand-off to ai-project-setup": [
        ("When the app-level instructions are in and proven", PICKER | {X}),
        ("Give the create steps for their app", PICKER | {X}),
        ("Tell them to open a new chat outside the project", PICKER | {X}),
        ("> Using these rules, set up a project", PICKER | {X}),
        ("Fill each bracket or delete it", PICKER | {X}),
        ("Don't write the project's instructions here", PICKER | {X}),
        ("For a code session, the folder's instruction file", {K}),
    ],
    "Prove the instructions took": [
        ("**Code session:**", {K}),
    ],
    "Known failure modes": [
        ("The text goes in the right box with the switch off", {G}),
        ("A newer Claude Code starts in auto", {K}),
        ("The default model stays on the strongest one", MODELS),
    ],
}

# Sections whose sentences are sorted by which app they are about.
SENTENCE_SECTIONS = {
    "What this is",
    "Words you'll see",
    "What you write, and what only they click",
    "Try it",
    "The interview, one question at a time",
    "The app-level instructions",
    "Perplexity",
    "Code sessions: permission modes",
    "Models and effort",
    "My rule for tokens",
    "Hand-off to ai-project-setup",
    "Prove the instructions took",
}

# A sentence that starts like this belongs to these pages. The first
# match wins, so the longer names come first. A bullet whose bold label
# matches goes or stays whole.
TAGS = [
    ("full page only", r"(A free plan should work, but this page is long"
                       r"|If it still won't take it"
                       r"|On a computer you can also send this page)", NONE),
    ("code session", r"(If you want a code session"
                     r"|In a code session"
                     r"|A code session takes four parts"
                     r"|Ask Mac, Windows or Linux only for a code session"
                     r"|The cap is for an app's box"
                     r"|The desktop app can also work in folders you pick"
                     r"|The instruction file inside the work folder)", {K}),
    ("Claude Code", r"(Claude Code[,:]|In Claude Code)", {K}),
    ("Codex", r"(Codex[,:]|For Codex|In Codex)", NONE),
    ("Grok Build", r"(Grok Build[,:]|In Grok Build)", NONE),
    ("Cowork", r"(Cowork[,:]|Every Cowork)", {C}),
    ("Perplexity", r"(Perplexity[,:]|Perplexity's desktop|On Perplexity)", {P}),
    ("Claude app", r"(In the Claude app|In Claude,)", {C}),
    ("Anthropic", r"(Anthropic's list for stretching|On Claude's newest models)", {C, K}),
    ("not ChatGPT", r"(For Claude, Grok or Perplexity, give the opt-out switch)", ALL - {G}),
    ("ChatGPT", r"(In ChatGPT|ChatGPT's temporary chat)", {G}),
    ("Grok", r"(For Grok,|In Grok,)", {X}),
    ("chat apps", r"(For the Claude and ChatGPT chat apps)", {G, C}),
]
# A sentence that starts like this stays with the sentence before it.
CONTINUES = re.compile(r"(Its |To take its|A model picked with|To hold every helper|Anthropic's docs agree|They suggest)")

# Sentences that list one clause per app, split at "; ".
CLAUSE_LISTS = [
    "If someone pays but they can't name the plan, they can read it in the app: ",
    "The meters: ",
    "None of these should get switched on by accident: ",
]
CLAUSE_LEADS = [
    ("Claude Code", {K}),
    ("a Claude Code", {K}),
    ("Fable on Claude", {C, K}),
    ("Claude and Grok", {C, K, X}),
    ("Claude", {C}),
    ("ChatGPT", {G}),
    ("Codex", NONE),
    ("Grok Build", NONE),
    ("Grok", {X}),
    ("Perplexity", {P}),
]

# Small fixes where kept text points at a part this version leaves out.
# Each "old" must appear exactly once in its section.
EVERY = ALL
REPLACE = [
    ("Try it", " (in Perplexity, the search box on its home page)", "", ALL - {P}),
    ("Try it", "help me set up my AI app.", "help me set up {app}.", EVERY),
    ("What you write, and what only they click",
     ", a code session's home instruction file (the app-level text plus the four code-session lines) and its settings line",
     "", ALL - {K}),
    ("The app-level instructions", "every line in both blocks", "every line in the block", ALL - {K}),
    ("The app-level instructions", "(see Claude Code below, and Codex and Grok Build under their apps)",
     "(see Claude Code below)", {K}),
    ("Claude", "Claude Code has its own card below.",
     "Claude Code has [its own version](for-claude-code.md).", {C}),
    ("Claude", "(see the Claude Code card)",
     "(see [the Claude Code version](for-claude-code.md))", {C}),
    ("Claude", "has its own approval setting: Code sessions, below.",
     "has its own approval setting.", {C}),
]

# Phrases in the frontmatter description, changed per page.
DESCRIPTION = [
    ("gets a person's AI app ready", "gets a person's {app} ready", ALL),
    ("steps for ChatGPT, Claude, Claude Code, Grok or Perplexity", "steps for {app}", ALL),
    (" (most of Grok's)", " (most of them)", {X}),
    (" (most of Grok's)", "", ALL - {X}),
    (", plain answers on code-session permissions, models and token use", "", {X}),
    ("plain answers on code-session permissions, models and token use",
     "plain answers on models and token use", PICKER),
    ("not set up for projects or code sessions yet", "not set up for projects yet", ALL - {K}),
    ("not set up for projects or code sessions yet", "not set up for code sessions yet", {K}),
]

STAMP = ("# Generated from SKILL.md by scripts/build-setup-pages.py. "
         "Edit SKILL.md, not this file, then run the script again.")

# Sentence breaks: a . ! or ? outside quotes and code, then any closing
# quotes or brackets, then a space before a capital, quote, backtick,
# bracket or digit.
NEXT_START = re.compile(r"[A-Z\"`(0-9~*]")


def split_sentences(prose):
    out = []
    start = 0
    quote = code = False
    i = 0
    while i < len(prose):
        ch = prose[i]
        if ch == "`":
            code = not code
        elif ch == '"' and not code:
            quote = not quote
        elif ch in ".!?" and not quote and not code:
            j = i + 1
            while j < len(prose) and prose[j] in "\")]":
                j += 1
            if j < len(prose) and prose[j] == " " and NEXT_START.match(prose, j + 1):
                out.append(prose[start:j])
                start = j + 1
                i = j
        i += 1
    out.append(prose[start:])
    return out


class Stop(Exception):
    pass


def stop(msg):
    raise Stop(msg)


def read_source():
    with open(SOURCE, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        stop("SKILL.md does not start with its frontmatter (a line of three dashes).")
    end = text.find("\n---\n", 4)
    if end < 0:
        stop("SKILL.md's frontmatter has no closing line of three dashes.")
    front = text[4:end].split("\n")
    body = text[end + 5:]
    fields = {}
    for line in front:
        m = re.match(r"^([a-z]+): (.*)$", line)
        if not m:
            stop("SKILL.md frontmatter line not understood: %r" % line)
        fields[m.group(1)] = m.group(2)
    if list(fields) != ["name", "description", "license"]:
        stop("SKILL.md frontmatter should be name, description, license; found %s." % ", ".join(fields))
    return fields, body


def split_units(lines):
    """One unit per paragraph, list item, quote line, rule or fenced block.
    Each unit remembers whether a blank line came before it."""
    units = []
    blank = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "":
            blank = True
            i += 1
            continue
        if line.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            if j >= len(lines):
                stop("SKILL.md has a code block that never closes.")
            units.append({"text": "\n".join(lines[i:j + 1]), "blank": blank})
            i = j + 1
        else:
            units.append({"text": line, "blank": blank})
            i += 1
        blank = False
    return units


def parse(body):
    lines = body.split("\n")
    heads = [(i, len(m.group(1)), m.group(2)) for i, m in
             ((i, re.match(r"^(#{1,6}) (.*)$", l)) for i, l in enumerate(lines)) if m]
    h1 = [h for h in heads if h[1] == 1]
    if len(h1) != 1:
        stop("SKILL.md should have exactly one H1; found %d." % len(h1))
    found = [(lvl, title) for _, lvl, title in heads if lvl > 1]
    if found != EXPECTED:
        want = ["%s %s" % ("#" * l, t) for l, t in EXPECTED]
        got = ["%s %s" % ("#" * l, t) for l, t in found]
        extra = [g for g in got if g not in want]
        missing = [w for w in want if w not in got]
        msg = ["SKILL.md's section headings are not the ones this script expects."]
        if missing:
            msg.append("Missing: " + "; ".join(missing))
        if extra:
            msg.append("New or renamed: " + "; ".join(extra))
        if not missing and not extra:
            msg.append("Same headings, different order.")
        msg.append("Update EXPECTED and the tables in scripts/build-setup-pages.py to match, then run it again.")
        stop("\n".join(msg))
    first = heads[1][0]
    pre = split_units(lines[h1[0][0] + 1:first])
    texts = [u["text"] for u in pre]
    if (len(texts) != 3 or not texts[0].startswith("**") or not texts[1].startswith("Part of [")
            or not all("(%s)" % f in texts[2] for _, _, f, _ in PAGES)):
        stop("Under the H1, SKILL.md should have the bold one-liner, the \"Part of\" line, "
             "then the paragraph linking the five versions, and nothing else.")
    sections = []
    for n, (i, lvl, title) in enumerate(heads[1:], start=1):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        sections.append({"level": lvl, "title": title, "units": split_units(lines[i + 1:end])})
    return {"h1": lines[h1[0][0]], "oneliner": texts[0], "partof": texts[1], "sections": sections}


class Tracker:
    """Counts how often each selector is used, so an unused one stops the run."""

    def __init__(self):
        self.hits = {}

    def hit(self, key):
        self.hits[key] = self.hits.get(key, 0) + 1

    def unused(self, keys):
        return [k for k in keys if not self.hits.get(k)]


def tag_of(sentence):
    s = sentence[2:] if sentence.startswith("**") else sentence
    for name, rx, pages in TAGS:
        if re.match(rx, s):
            return name, pages
    return None, None


def filter_clauses(sentence, page, track):
    for lead in CLAUSE_LISTS:
        at = sentence.find(lead)
        if at < 0:
            continue
        track.hit(("clause list", lead))
        head = sentence[:at + len(lead)]
        rest = sentence[at + len(lead):]
        if not rest.endswith("."):
            stop("The list after %r in SKILL.md should end with a full stop." % lead)
        kept = []
        for clause in rest[:-1].split("; "):
            for name, pages in CLAUSE_LEADS:
                if clause.startswith(name) and not clause[len(name):len(name) + 1].isalpha():
                    track.hit(("clause lead", name))
                    if page in pages:
                        kept.append(clause)
                    break
            else:
                stop("SKILL.md has a clause the script can't place by app, after %r: %r. "
                     "Add its first words to CLAUSE_LEADS." % (lead, clause[:60]))
        if not kept:
            return ""
        return head + "; ".join(kept) + "."
    return sentence


def filter_sentences(text, page, track):
    marker = re.match(r"^(- |\d+\. )", text)
    lead = marker.group(1) if marker else ""
    prose = text[len(lead):]
    sentences = split_sentences(prose)
    first_tag, first_pages = tag_of(sentences[0])
    if first_tag and sentences[0].startswith("**"):
        track.hit(("tag", first_tag))
        return text if page in first_pages else ""
    kept = []
    current = None  # pages of the sentence before, for continuations
    for s in sentences:
        name, pages = tag_of(s)
        if name:
            track.hit(("tag", name))
            current = pages
        elif CONTINUES.match(s) and current is not None:
            track.hit(("continues", CONTINUES.match(s).group(1)))
            pages = current
        else:
            current = None
            pages = None
        if pages is not None and page not in pages:
            continue
        s = filter_clauses(s, page, track)
        if s:
            kept.append(s)
    if not kept:
        return ""
    out = " ".join(kept)
    if out.startswith("**") and out.endswith("**") and out.count("**") == 2 and lead:
        return ""  # only a bold label was left
    return lead + out


def unit_key(text):
    m = re.match(r"^(- |\d+\. )", text)
    return text[len(m.group(1)):] if m else text


def build_section(sec, page, app, track):
    title = sec["title"]
    rules = UNITS.get(title, [])
    out = []
    carry_blank = False
    dropped = 0  # numbered items dropped so far in this list; a "1." starts a new list
    for u in sec["units"]:
        text = u["text"]
        key = unit_key(text)
        num = re.match(r"^(\d+)\. ", text)
        if num and num.group(1) == "1":
            dropped = 0
        keep = True
        matches = [(p, pages) for p, pages in rules if key.startswith(p)]
        if len(matches) > 1:
            stop("Two selectors match one line in %r: %s" % (title, ", ".join(repr(m[0]) for m in matches)))
        if matches:
            track.hit(("unit", title, matches[0][0]))
            keep = page in matches[0][1]
        if keep and title in SENTENCE_SECTIONS and not text.startswith(("```", ">", "---")):
            text = filter_sentences(text, page, track)
            keep = bool(text)
        if not keep:
            carry_blank = carry_blank or u["blank"]
            if num:
                dropped += 1
            continue
        if num and dropped:
            text = "%d. %s" % (int(num.group(1)) - dropped, text[len(num.group(0)):])
        out.append({"text": text, "blank": u["blank"] or carry_blank})
        carry_blank = False
    body = ""
    for i, u in enumerate(out):
        if i > 0:
            body += "\n\n" if u["blank"] else "\n"
        body += u["text"]
    for sec_title, old, new, pages in REPLACE:
        if sec_title != title or page not in pages:
            continue
        count = body.count(old)
        if count != 1:
            stop("In SKILL.md's section %r, the script expected %r exactly once and found it %d times."
                 % (title, old, count))
        track.hit(("replace", sec_title, old))
        body = body.replace(old, new.replace("{app}", app))
    return body


def words(text):
    return len(text.split())


def build_page(src, fields, page, app, fname, leaves_out, full_words, track):
    desc = fields["description"]
    for old, new, pages in DESCRIPTION:
        if page not in pages:
            continue
        if desc.count(old) != 1:
            stop("SKILL.md's description should contain %r exactly once." % old)
        track.hit(("description", old, new))
        desc = desc.replace(old, new.replace("{app}", app))
    others = [(a, f) for k, a, f, _ in PAGES if k != page]
    links = ", ".join("[%s](%s)" % o for o in others[:-1]) + " and [%s](%s)" % others[-1]
    scope = ("This is the %s version of [Set up your AI first](SKILL.md), about WORDCOUNT words; "
             "the full page is about %s. I keep one page, and a script makes each version from it, "
             "so they say the same thing. This one keeps only what %s needs. %s. "
             "The other versions: %s." % (app, "{:,}".format(full_words), app, leaves_out, links))
    parts = [
        "---\nname: %s-for-%s\ndescription: %s\nlicense: %s\n%s\n---\n"
        % (fields["name"], page, desc, fields["license"], STAMP),
        "%s (%s)" % (src["h1"], app),
        src["oneliner"],
        src["partof"],
        scope,
    ]
    for sec in src["sections"]:
        if page not in SECTIONS.get(sec["title"], ALL):
            continue
        body = build_section(sec, page, app, track)
        parts.append("%s %s" % ("#" * sec["level"], sec["title"]))
        if body:
            parts.append(body)
    text = "\n\n".join(parts[1:])
    text = parts[0] + "\n" + text + "\n"
    n = words(text)
    rounded = int(round(n / 100.0)) * 100
    return text.replace("WORDCOUNT", "{:,}".format(rounded)), n


def all_selectors():
    keys = []
    for title, rules in UNITS.items():
        keys += [("unit", title, p) for p, _ in rules]
    keys += [("tag", name) for name, _, _ in TAGS]
    keys += [("clause list", lead) for lead in CLAUSE_LISTS]
    keys += [("clause lead", name) for name, _ in CLAUSE_LEADS]
    keys += [("replace", t, o) for t, o, _, _ in REPLACE]
    keys += [("description", o, n) for o, n, _ in DESCRIPTION]
    return keys


def main():
    try:
        fields, body = read_source()
        src = parse(body)
        titles = [s["title"] for s in src["sections"]]
        for t in list(SECTIONS) + list(UNITS) + list(SENTENCE_SECTIONS):
            if t not in titles:
                stop("The script names a section SKILL.md doesn't have: %r." % t)
        full_words = int(round(words(open(SOURCE, encoding="utf-8").read()) / 100.0)) * 100
        track = Tracker()
        built = []
        for page, app, fname, leaves_out in PAGES:
            text, n = build_page(src, fields, page, app, fname, leaves_out, full_words, track)
            built.append((fname, text, n))
        unused = track.unused(all_selectors())
        if unused:
            stop("These selectors found nothing in SKILL.md, so it changed under them:\n  "
                 + "\n  ".join(repr(u) for u in unused)
                 + "\nFix the selector or SKILL.md, then run it again.")
    except Stop as e:
        sys.stderr.write("build-setup-pages: stopped, nothing written.\n%s\n" % e)
        return 1
    for fname, text, n in built:
        path = os.path.join(FOLDER, fname)
        old = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                old = f.read()
        if old != text:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
        print("%-20s %5d words%s" % (fname, n, "" if old != text else " (unchanged)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
