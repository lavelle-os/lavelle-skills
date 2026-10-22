---
name: warranty-and-callbacks
description: "How an AI assistant handles the promises a service business makes after a visit: a no-charge return window written with its exact end date, repeat failures that start from the last visit's notes, recalls inside the shop's window, and never promising a follow-up that no tool will deliver. Use when drafting a return-visit ticket, a warranty line, or a reply to a customer whose repair failed again. Drafts; the owner decides what is free."
license: MIT
---

# Warranty and callbacks

**Keeps the promises a repair business makes after the visit.**

Part of [Lavelle skills](https://github.com/lavelle-os/lavelle-skills#if-you-have-never-used-github-start-here), rules files from a one-truck appliance repair shop. New here, or never used GitHub? Start with that page. Want to try this one now? Jump to [Try it](#try-it).

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. With these rules, the assistant handles what happens after a repair: the free-return promise written on the ticket, the call when the problem comes back, and the trip back out. Many shops make two promises. One is a short free return trip. The other is a longer guarantee on the same repair. The assistant keeps the two apart, writes every promise with an exact end date, and reads the last visit's notes before anything else. What's free is always the owner's call.

It comes from my one-truck appliance repair shop in Alabama. Some of my promises were harder to keep than to make, and these rules came out of those.

## Who it's for

- Service businesses that offer a free return trip or a repair guarantee.
- Anyone answering the "it's broken again" call.

## Words you'll see

- **Ticket:** the job record the customer gets.
- **Write-up:** the description on the ticket of what was found and done.
- **Callback:** in the repair trade, a customer calling because the problem came back.
- **Return window:** how long a free return trip is promised.
- **Guarantee:** the longer promise on the same repair. Ours is no charge for the same problem on the same machine within one year.
- **Diagnostic:** the visit fee for finding the problem.

## What you need

- Any AI chat app.
- Your shop's return window and guarantee, written down.
- The last visit's write-up, pasted in, when a customer calls back.

## What it does

1. Writes a return promise that says what it covers and its exact last day.
2. When a customer calls back, reads the last visit's write-up first.
3. Notices when the same part keeps failing, which often means the real cause is something else.
4. Points out, for the owner to decide, when the same repair has failed again inside the guarantee.
5. Says only what's true about follow-up. "The owner reviews every call" is fine only if the owner does.

## What it won't do

- Promise an arrival time.
- Promise free work beyond the shop's written rule.
- Blame the customer in writing.
- Charge a second visit fee on a return the shop promised.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, use the icon of two overlapping squares just to the right of the word **Raw** (its label is "Copy raw file"); on a phone, the three dots beside Preview, Code and Blame, then **Copy**. The look-alike icon next to the file name copies only the address.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules: we fixed a made-up washer on March 3, 2027 and promised a free return for 90 days. Write the promise line for the ticket, with its end date.

A good answer gives June 1, 2027. Day one is the day after the visit, and the last day counts.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You are handling what happens after the first visit: the promise written on the ticket, the call when the problem returns, and the return trip. A promise the business cannot find later is worse than none. What is free is the owner's call, written down; you apply it.

### Write the promise with its end date

A return promise names what it covers and the exact last day, counted from the visit. "No charge to come back and look at any of the three for the next 90 days, through January 10, 2027" can be checked by anyone. "90 days" alone cannot. Count days, not months: day one is the day after the visit, and the last day counts.

**What went wrong, 2026-10-12:** one visit looked at a dryer, a washer and a refrigerator, and the owner offered one no-charge return covering all three. The line was written with its end date counted out, so nobody has to recount it later.

### A repeat failure starts from the last visit

When a customer calls back about the same machine, read the last visit's write-up first. It may already name the next step and what it costs.

**What went wrong, 2026-10-12:** an ice maker's fill tube froze solid again a week after it was thawed. The first write-up had said the water inlet valve was next, with no added labor. The return ticket charged the valve only, as promised, and named the earlier visit.

### A part that keeps failing may not be the part

A bulb that keeps blowing or a fuse that keeps opening often points at something upstream (the socket, a wiring short, poor airflow). Say so to the technician; do not quote the same part a third time without the technician's word.

**What went wrong, 2026-10-13:** an oven's upper light blew a second bulb within two weeks. The technician called it the socket, and both the socket and a heat-rated bulb went on the order.

### Recalls inside the window

The same machine and the same complaint inside the shop's recall window is a recall, handled under the shop's rule (ours: no charge inside one year for the same repair). Flag it for the owner with the earlier visit named. A different complaint on the same machine is a new visit. The two windows are separate: a return promise covers any complaint it names for its short window; the recall window covers only the same repair, for longer.

### Never promise a follow-up no tool will deliver

"I'll flag that for the owner" is only true if something actually sends the flag: a note on the job, a message log, an alert. If nothing does, say what is true instead, such as "the owner reviews every call."

**What went wrong, 2026-10-11:** a phone agent told a caller it would flag a problem for the owner: a map pin on the wrong street. No tool sent anything; a review of the calls caught it hours later.

### Never

Promise a time. Promise free work beyond the shop's written rule. Blame the customer in writing. Charge a second diagnostic on a return the shop promised.

### Known failure modes

- An end date counted wrong across a month boundary.
- A promise made out loud and never written on the ticket.
- A return visit booked as a new job with a new diagnostic fee.

### Starting yours

1. Write your return window and recall window, with what each covers.
2. Find one repeat failure in your last month and write it up under these rules.
3. Run the skill on a fictional callback inside the window.
4. The first thing that will go wrong: the agent will count 90 days as three months. Give it the end date to check against.
