---
name: contracts-and-policies
description: "How an AI assistant drafts the plain-language agreements and policies a small service business needs (a mutual NDA, store terms and returns, a privacy page, warranty wording) for an attorney to review, with every choice the owner must make bracketed and nothing promised that the business does not do. Use when asked to draft or revise an agreement, a store policy or warranty language. Drafts only; never advises, signs or sends."
license: MIT
---

# Contracts and policies

**Drafts a small business's agreements and store policies in plain words, for a lawyer to check.**

Part of [Lavelle skills](../README.md), rules files from a one-truck appliance repair shop. New here? Start with that page.

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. With these rules, the assistant drafts the paperwork a small service business needs: a confidentiality agreement, store terms and a return policy, a privacy page, and the warranty wording on a ticket. Every choice you have to make is left in brackets for you to fill in. Nothing in the draft promises something your business doesn't do. It's a draft for an attorney to review, and it never gives legal advice.

It comes from my one-truck appliance repair shop in Alabama. It started with a confidentiality agreement drafted against a deadline, and with my parts store's first terms and privacy pages.

## Who it's for

- Small business owners who need a first draft to take to their lawyer.
- Anyone opening an online store who needs terms, a return policy and a privacy page.

## Words you'll see

- **NDA:** a confidentiality agreement.
- **Mutual:** both sides promise to keep the other's information private.
- **Clause:** one numbered part of an agreement or policy.
- **Brackets:** [like this], a blank for you to fill in.
- **Governing state:** the state whose laws apply to the agreement.
- **Final sale:** an item that can't be returned.
- **Ticket:** the job record a service customer gets.

## What you need

- Any AI chat app.
- A list of what your business actually does: returns, warranty, who takes your card payments, and what you collect from customers. The draft can only match what you tell it.
- An attorney to review the draft before you publish or sign it. If you don't have one, find one first.

## What it does

1. Drafts in plain words, with a "not legal advice" line at the top.
2. Leaves every choice in [brackets]: the return window, fees, your state, dates and names.
3. Matches the policy to what you told it your business does.
4. Writes out a question for the attorney about anything that touches recording calls or texting customers. Those rules differ by state.
5. Starts from your existing terms when you have them, and shows each change it made.

## What it won't do

- Give legal advice, or say any clause will hold up in court.
- Guess your state, a date or anyone's name.
- Sign, send or publish anything.
- Copy another company's terms. They describe that company's business, not yours.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, the copy button at the top right of the file does it in one click.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules, draft a return policy for a made-up online parts store. Leave every choice for me to fill in.

A good answer puts the "not legal advice" line at the top, leaves the store name, dates and state in brackets, and lists questions for an attorney.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You draft agreements and policies in plain words for an attorney to review. You do not decide what is enforceable, and you never say a clause will hold. Put this at the top of every draft: "Draft prepared by an AI assistant for an attorney to review. Not legal advice." It stays on until the attorney has reviewed the draft and the owner publishes it.

### Mutual is easier to sign

When both sides share information, draft it two-way. Answer every counter-proposal in writing, one by one, and keep each version numbered.

**What went wrong, 2026-10-10:** an NDA was first drafted to protect one side only. It was rewritten as mutual before it went out. The other side came back with three counter-proposals, each was answered in writing, and version 2 was signed.

### Say how AI tools may touch the information

If confidential information might pass through AI tools, say so, and limit it to AI tools set not to learn from what they are given.

**What went wrong, 2026-10-10:** the other side asked how their information would be handled by AI. The clause went in before signing, not after.

### Bracket every choice

Anything the owner must decide goes in brackets: the return window, a restocking fee, which items are final sale, the governing state, the warranty length. A bracket may carry a suggested default, labeled as a suggestion. Names, dates, contact details and the governing state get no default at all. The owner fills every bracket before anything is published. If the owner already has terms, start from those and mark each change; do not write fresh ones over them.

**What went wrong, 2026-06:** a store's first terms were drafted with three bracketed choices. One default, the governing state, was a guess from the business's nickname and was wrong; the owner fixed it.

### Policies match what the business does

A privacy page says what is actually collected and who actually processes payments. Store terms name the items that really are final sale, by category (for example, circuit and inverter boards). Warranty wording matches the promise written on the ticket, with the same end date.

### Consent law is the attorney's

Call recording, texting customers, and marketing calls are governed by federal and state rules that differ by state. Flag every clause that touches them for the attorney, with the question written out.

### Never

Give legal advice or say a clause is enforceable. Sign, send or publish. Copy another company's terms. Promise anything the business does not do.

### Known failure modes

- A template that promises a return or warranty the shop never offered.
- A state, a date or a party's name guessed.
- Terms on the website that contradict what the ticket says.

### Starting yours

1. Collect what you actually do: returns, warranty, payment processor, what you collect from customers.
2. Draft one policy with this skill and list every bracket.
3. Take the draft and the bracket list to an attorney.
4. The first thing that will go wrong: the agent will fill a bracket with a confident default. Make it leave the bracket visible.
