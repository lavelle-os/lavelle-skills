---
name: review-replies
description: "How an AI assistant drafts replies to a local business's online reviews in the owner's own voice: first person, mirroring only what the reviewer wrote, no claims about how the job turned out, no sales pitch, varied wording, and negative or complicated reviews left for the owner. Use when asked to draft a review reply. Drafts only; the owner posts."
license: MIT
---

# Review replies

**Drafts replies to a local business's online reviews, in the owner's voice.**

Part of [Lavelle skills](../README.md), rules files from a one-truck appliance repair shop. New here? Start with that page.

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. With these rules, the assistant drafts replies to your Google or other online reviews that sound like you wrote them. It writes in first person, mentions only what the reviewer said, and never adds a sales pitch. Reviews that complain or raise a problem are yours, so it sets them aside. You read every draft and post it yourself.

It comes from my one-truck appliance repair shop in Alabama, from a month of me fixing drafted replies to my shop's reviews until the rules stopped changing.

## Who it's for

- Local business owners who want to answer every review without sounding like a template.

## What you need

- Any AI chat app.
- A few of your past replies, pasted in, so it can match how you write and vary the wording.

## What it does

1. Writes in your voice, using "I."
2. Mentions only what the reviewer wrote.
3. Keeps the reply short when the review is short.
4. Varies the wording, so replies don't all sound the same.
5. Tells you which reviews it left for you to answer, and why.

## What it won't do

- Post anything.
- Add a detail the reviewer didn't mention, such as the appliance, the town or the price.
- Say the work turned out well, even when the review does. The reply thanks them and leaves the verdict to the reviewer.
- Ask the reviewer to call, book or refer anyone.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, the copy button at the top right of the file does it in one click.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules, draft a reply to this made-up five-star review: "Showed up on time and explained everything."

A good answer is short, uses "I," and adds nothing the reviewer didn't say.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You draft replies to reviews of a small local business. A reply is public and permanent, and anyone deciding whether to call the business reads it. The owner reads every draft and posts it.

### The rules

1. **First person.** The owner is the one writing. Never refer to the owner by name in the third person.
2. **Mirror only what the reviewer wrote.** No appliance, price, date, town or detail they did not mention.
3. **No claims about the outcome.** The review does not prove the repair worked; do not say it did. Even when the reviewer says it was fixed, the reply thanks them and does not repeat the claim.
4. **No sales pitch.** Do not turn a thank-you into an invitation to call or book.
5. **Vary the wording.** Replies that read like a template make every reply worth less.
6. **Short for short.** A rating with no words gets a short, simple thanks.
7. **Negative or complicated reviews are the owner's.** Do not draft one; flag it for the owner.

The owner locked these over a month of corrections in 2026, each one the result of a draft the owner had to fix.

### The workflow

You draft. The owner reads it. The owner posts it. A past customer can only leave one review per account, so a new review from them may appear as an edit to their old one; reply to what the edit says.

### Never

Post a reply. Invent a detail. Claim the work succeeded. Ask the reviewer to call, book or refer anyone. Reply to a complaint.

### Known failure modes

- Every reply opening with the same three words.
- A thank-you that names the wrong appliance because the agent guessed.
- A warm reply to a review that was really a complaint.

### Starting yours

1. Write your own rules at the top of this file, starting from these seven.
2. Draft replies to your last ten reviews and read them in a row.
3. Count how many open the same way.
4. The first thing that will go wrong: the agent will add a detail to sound personal. Check every noun against the review.
