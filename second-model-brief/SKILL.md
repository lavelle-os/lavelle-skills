---
name: second-model-brief
description: How to write a research brief for a second AI model, read its memo back, and reconcile it before anyone acts on it. Use when asked to draft a research brief, verify another model's findings, or decide whether a memo can be trusted. Never acts on an unreconciled memo.
---

# The second-model brief

*One small business has sent about forty of these to a second model and read every answer back against the sources. This is the shape that survived.*

You are helping someone get research from a second model they do not control, and then decide how much of it to believe. Your job is to draft the brief, or to reconcile a memo that came back. You never act on a memo that has not been reconciled, and you say so when asked to.

## Why a second model at all

A single model agrees with itself. The second one is cheap, has different training, and will open pages the first one guessed about. It is not a judge; it is a second witness whose testimony gets checked.

## The brief, in this order

1. **A conversation title**, one line, the same as the filename the memo will be saved under. The memo comes back by share link and has to land somewhere findable.
2. **The rules of evidence, up front:** public information only; answer in the chat; every finding labeled CONFIRMED with the URL and the date opened, or UNVERIFIED; sources at the end; research date; no praise.
3. **Who is asking**, in one paragraph, with nothing private: the asker appears as "the author," customers carry no names, no health detail, no money figures, no credentials. If the brief needs a customer's situation, it describes the situation and not the person.
4. **What the author already found**, as claims for the second model to confirm or correct. Give it something to disagree with. A brief that only asks questions gets a survey; a brief that states findings gets corrections.
5. **The questions, numbered, in the order the answer should come**, each one specific enough that "not found" is a possible answer.
6. **Argue against.** One question always asks for the strongest case against the author's own position, then the strongest case for, then which is stronger in five sentences. Memos that skip this flatter.
7. **The memo format:** the ten sentences you would say in ten minutes; findings ranked by how much they change the decision; the corrected version of whatever the author drafted; what could not be verified; sources with dates opened.

**What went wrong, 2026-10-07:** a brief went out with "[PASTE BLOCK HERE]" still in it. The second model designed a replacement from scratch instead of correcting the draft, in trade jargon, with the author's scope dropped. Paste the draft before sending. Read the brief once as the recipient before sending.

## Reading the memo back

A memo is not a result. It is read against the sources before it is used, and the reading is written down beside it.

1. **Re-open the two or three claims that would change the decision.** Not all of them. The ones that, if wrong, flip the verdict. Open the primary page, quote it, mark the claim CONSISTENT or CORRECTED.
2. **Separate what the memo verified from what it was told.** A memo repeats the brief's own claims back as findings. Those are not findings.
3. **"Not found" is not "does not exist."** A second model that cannot open a page reports absence. Say "none found," never "none exist," and say which pages were blocked.
4. **Blocked fetches are a tooling problem, not a research result.** A 403 or a timeout means try another route: a browser, a different mirror, a cached copy. **What went wrong, 2026-08 to 2026-09:** a court-records site and a government statistics site blocked automated fetches for thirty-five days; both rendered in an ordinary browser the day someone tried.
5. **Where the memo corrects the author, write it down as a correction**, with the author's original words next to it. **What went wrong, 2026-10-07:** the author remembered a public figure saying he found "room in the kernel." The memo found the actual quote: "started much lower in the stack, so far more room." Different layer, different conclusion. The memory had driven the question.
6. **Where the memo is wrong for this reader, say why.** A memo written for a programmer is not wrong when it uses trade words; it is wrong for a reader who asked for plain words. Rewrite; do not discard.
7. **Legal, tax and licensing findings get a second pass by a third reader before anyone acts.** **What went wrong, 2026-09:** three legal findings in one week were caught on the second pass, including a reading of a copyright opinion that the first pass had reversed.

## The reconciliation file

Beside every memo, a file with: what was re-opened and what it showed; where the memo corrects the author; where the memo is wrong for this reader; the verdict in one paragraph; what stays open. Nothing moves until that file exists. The memo folder is history, not an inbox.

## Known failure modes

- The second model answers the brief it received, not the one meant. Every ambiguity in the brief comes back as a confident answer to the wrong question.
- Share links may not render outside a signed-in session. Save the memo text, not the link.
- The author's own claims, pasted into the brief, come back labeled CONFIRMED because the model found the author's source. Check whether the source is independent of the author.
- A memo that is mostly right is more dangerous than one that is mostly wrong, because the wrong line gets read in the same voice as the right ones.

## Starting yours

1. Write the title line and the rules of evidence before the questions.
2. State what you already believe, so the model has something to correct.
3. Put "argue against" in every brief, no exceptions.
4. The first thing that will go wrong: you will act on the memo's ten sentences before reading the reconciliation, because the ten sentences are good. Write the reconciliation first.
