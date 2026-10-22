---
name: second-model-brief
description: How to write a research brief for a second AI model, read its memo back, and reconcile it before anyone acts on it. Use when asked to draft a research brief, verify another model's findings, or decide whether a memo can be trusted. Never acts on an unreconciled memo.
license: MIT
---

# The second-model brief

**Writes the request for a second AI to check the first one's research, and reads the answer back before anyone acts on it.**

Part of [Lavelle skills](https://github.com/lavelle-os/lavelle-skills#if-you-have-never-used-github-start-here), rules files from a one-truck appliance repair shop. New here, or never used GitHub? Start with that page. Want to try this one now? Jump to [Try it](#try-it).

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. One AI agrees with itself. A second AI from a different company is a cheap second witness. With these rules, the assistant writes the request you send to that second AI. It states what you already believe, so the second AI has something to correct, and always asks for the case against you. When the answer comes back, the assistant reads it against the sources and writes down what holds up before you act on any of it.

It comes from my one-truck appliance repair shop in Alabama. We've sent about forty of these to a second AI and read every answer back against the sources. This is the shape that survived.

## Who it's for

- Anyone who uses AI for research and wants an independent check before acting on it.
- Owners checking a legal, tax or license finding before spending money on it.

## Words you'll see

- **Brief:** the written request you send to the second AI.
- **Memo:** the second AI's written answer.
- **Reconcile:** read the memo against the original sources and write down what holds up, what it corrected, and what stays open.
- **CONFIRMED:** the second AI says it opened the page, and gives its address and the date. **UNVERIFIED:** everything else.
- **Different family:** an AI made by a different company. A second copy of the same company's AI isn't an independent check.

## What you need

- Two AI chat apps from different companies.
- The claims you want checked, written down.
- About ten minutes to re-open the two or three sources that would change your decision.

## What it does

1. Writes the brief: a title, the rules of evidence, who is asking with nothing private in it, what you already believe, and numbered questions.
2. Always includes an "argue against" question.
3. Reads the memo back and re-opens the sources behind the claims that matter most. Without web access, it tells you which ones to open.
4. Separates what the second AI checked from what it simply repeated from your brief.
5. Writes the reconciliation, and sends legal, tax and license findings to a third reader, a person or another AI, before anyone acts.

## What it won't do

- Send the brief or run the check itself. You send it to an AI from a different company.
- Act on a memo before the reconciliation is written.
- Treat "not found" as "doesn't exist."
- Put a customer's name or private details in a brief.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, use the icon of two overlapping squares just to the right of the word **Raw** (its label is "Copy raw file"); on a phone, the three dots beside Preview, Code and Blame, then **Copy**. The look-alike icon next to the file name copies only the address.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules, draft a brief asking a second AI to check this made-up claim: the town of Example Falls requires a permit to sell firewood from a truck. Don't send it.

A good answer has a title line, the evidence rules, your claim stated for the second AI to confirm or correct, and an "argue against" question. It doesn't run the check itself.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You are helping someone get research from a second model they do not control, and then decide how much of it to believe. Your job is to draft the brief, or to reconcile a memo that came back. You never act on a memo that has not been reconciled, and you say so when asked to. You do not send the brief or run it yourself, and you never stand in for the second model with another copy of yourself or a model from your own family; the owner sends it to a model from a different family.

**What went wrong, 2026-10-12:** told to "check that with another model", an agent under these rules ran the brief on a second model of its own family and reported back. It reconciled honestly and said not to act, but the read it got was not the independent one the brief exists for.

### Why a second model at all

A single model agrees with itself. The second one is cheap, has different training, and will open pages the first one guessed about. It is not a judge; it is a second witness whose testimony gets checked.

### The brief, in this order

1. **A conversation title**, one line, the same as the filename the memo will be saved under. The memo comes back by share link and has to land somewhere findable.
2. **The rules of evidence, up front:** public information only; answer in the chat; every finding labeled CONFIRMED with the URL and the date opened, or UNVERIFIED; sources at the end; research date; no praise.
3. **Who is asking**, in one paragraph, with nothing private: the asker appears as "the author," customers carry no names, no health detail, no money figures, no credentials. If the brief needs a customer's situation, it describes the situation and not the person.
4. **What the author already found**, as claims for the second model to confirm or correct. Give it something to disagree with. A brief that only asks questions gets a survey; a brief that states findings gets corrections.
5. **The questions, numbered, in the order the answer should come**, each one specific enough that "not found" is a possible answer.
6. **The crew.** Before writing the questions, name the three to five fields that would sit at the table if the answer had to be right: an examiner, a short seller, a forensic accountant, a repair technician, a roboticist, whoever the question actually needs. Then write at least one question that asks for what each of those people would do: the records a short seller would pull, the test an examiner would run. Do not ask the second model to play the part. Role play changes the voice and leaves the method behind. Ask for the method. **What it looks like done right, 2026-10-15:** five research lanes on one question, each briefed on what one field would check (the cabinet's own records, vendor pricing pages, statutes and headcount evidence, regulator rules, the robot makers' own tests), came back as five different lists of checks rather than five opinions.
7. **Argue against.** One question always asks for the strongest case against the author's own position, then the strongest case for, then which is stronger in five sentences. Memos that skip this flatter.
8. **The memo format:** the ten sentences you would say in ten minutes; findings ranked by how much they change the decision; the corrected version of whatever the author drafted; what could not be verified; sources with dates opened.

**What went wrong, 2026-10-07:** a brief went out with "[PASTE BLOCK HERE]" still in it. The second model designed a replacement from scratch instead of correcting the draft, in trade jargon, with the author's scope dropped. Paste the draft before sending. Read the brief once as the recipient before sending.

### Reading the memo back

A memo is not a result. It is read against the sources before it is used, and the reading is written down beside it.

1. **Re-open the two or three claims that would change the decision.** Not all of them. The ones that, if wrong, flip the verdict. Open the primary page, quote it, mark the claim CONSISTENT or CORRECTED.
2. **Separate what the memo verified from what it was told.** A memo repeats the brief's own claims back as findings. Those are not findings.
3. **"Not found" is not "does not exist."** A second model that cannot open a page reports absence. Say "none found," never "none exist," and say which pages were blocked.
4. **Blocked fetches are a tooling problem, not a research result.** A 403 or a timeout means try another route: a browser, a different mirror, a cached copy. **What went wrong, 2026-08 to 2026-09:** a court-records site and a government statistics site blocked automated fetches for thirty-five days; both rendered in an ordinary browser the day someone tried.
5. **Where the memo corrects the author, write it down as a correction**, with the author's original words next to it. **What went wrong, 2026-10-07:** the author remembered a public figure saying they found "room in the kernel." The memo found the actual quote: "started much lower in the stack, so far more room." Different layer, different conclusion. The memory had driven the question.
6. **Where the memo is wrong for this reader, say why.** A memo written for a programmer is not wrong when it uses trade words; it is wrong for a reader who asked for plain words. Rewrite; do not discard.
7. **Legal, tax and licensing findings get a second pass by a third reader before anyone acts.** **What went wrong, 2026-09:** three legal findings in one week were caught on the second pass, including a reading of a copyright opinion that the first pass had reversed.

### The reconciliation file

Beside every memo, a file with: what was re-opened and what it showed; where the memo corrects the author; where the memo is wrong for this reader; the verdict in one paragraph; what stays open. Nothing moves until that file exists. The memo folder is history, not an inbox.

### Known failure modes

- The second model answers the brief it received, not the one meant. Every ambiguity in the brief comes back as a confident answer to the wrong question.
- Share links may not render outside a signed-in session. Save the memo text, not the link.
- The author's own claims, pasted into the brief, come back labeled CONFIRMED because the model found the author's source. Check whether the source is independent of the author.
- A memo that is mostly right is more dangerous than one that is mostly wrong, because the wrong line gets read in the same voice as the right ones.

### Starting yours

1. Write the title line and the rules of evidence before the questions.
2. State what you already believe, so the model has something to correct.
3. Put "argue against" in every brief, no exceptions.
4. The first thing that will go wrong: you will act on the memo's ten sentences before reading the reconciliation, because the ten sentences are good. Set up the reconciliation file and its checklist before the memo arrives, and fill it in as you re-open the sources.
