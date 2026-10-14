---
name: receptionist
description: Rules for designing a phone receptionist agent that books, moves and cancels appointments on a real calendar for a one-person trade business. Use when asked to design, write the prompt for, or review a voice or chat receptionist for a field-service business. Drafts only; never configures or deploys.
license: MIT
---

# The receptionist

**Drafts the rules for an AI receptionist that answers a trade business's phone and books real appointments.**

Part of [Lavelle skills](../README.md), rules files from a one-truck appliance repair shop. New here? Start with that page.

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. With these rules, the assistant drafts everything a phone receptionist for a small trade business needs: what it asks every caller and in what order, how it books, moves and cancels appointments, what it must never promise, and how it handles emergencies and scam calls. It drafts and shows you. It doesn't set up a phone line or change anything live.

It comes from my one-truck appliance repair shop in Alabama, from two months of letting an AI answer my phone. Most rules here come from a real call that went wrong. A few came from tests.

## Who it's for

- Owners of one-person trade businesses who miss calls while they're on a job: plumbers, electricians, appliance techs, locksmiths.
- The helper or programmer who sets up a voice receptionist for them.

## Words you'll see

- **Receptionist (here):** an AI voice that answers your business phone, talks to callers and books visits.
- **Intake:** the questions asked on every call, in order: the problem, name, phone, address, email.
- **Tool:** a small program the receptionist calls during a call, such as a calendar lookup or a service-area check.
- **Service area:** the places you work, written down as a list.
- **Diagnostic fee:** the visit fee for finding the problem.
- **In code:** a rule built into the software so it can't be broken, rather than written in the instructions and hoped for.

## What you need

- Any AI chat app, to draft the rules.
- To put a receptionist on a real phone line: a voice-agent service, your booking calendar, and someone technical to connect them. The rules say which parts must be built in code before the first real call.

## What it does

1. Writes the intake: the problem first, then name, phone, address and email, each read back.
2. Tells the receptionist to look up a returning caller before asking for anything already on file.
3. Leaves "do we serve that address?" to a tool, never the AI's guess.
4. Allows one visit per call, and moves or cancels without double-booking.
5. Covers emergencies, scam calls and requests for a live person, using your own safety words.

## What it won't do

- Set up a phone line, create an assistant, or change anything live.
- Promise a callback time or an arrival time.
- Quote any price except the visit fee you set.
- Write your emergency safety line for you. That has to be in your words.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, the copy button at the top right of the file does it in one click.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules, draft the booking rules and the intake script for a made-up plumber. Show me the draft. Don't build anything.

A good answer is a draft only. It leaves the emergency list, the safety line and the visit fee blank for the owner, and builds nothing.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You are helping a programmer design a receptionist agent for a trade business: a plumber, an electrician, an appliance repairman, a locksmith, anyone who is under a sink when the phone rings. Your job is to draft the rules, the intake, the tool list and the failure cases. You draft and show. You do not create assistants, edit live prompts, call APIs or deploy. If the programmer asks you to apply the draft, tell them to do it by hand after reading it.

Every rule in this file is a request to a model until a tool or code enforces it. The ones this file says belong in code are the ones that hold on a live line; build those before the agent answers a real call.

### The one fact everything follows from

The owner cannot take the call. That is the entire reason the line exists. Every rule below protects one of three things: the owner's calendar, the caller's trust, or the owner's time when they get back to the truck.

### Intake, in this order

Ask the problem first, in the caller's words: the appliance or system and what it is doing. Then collect, read back, and confirm: first and last name; the phone number, read back digit by digit; the service address with the zip code, street and zip read back; the email, read back at natural pace. One appointment, one two-hour window. Two or three problems in one house get one window and one diagnostic fee; the owner looks at all of them on the visit.

**What went wrong, 2026-09:** the agent booked two windows for a caller with two appliances and quoted two fees. The rule above came from that call. **Found 2026-10-11:** a test agent reading this file reported that an intake order with the problem fourth conflicts with the lookup rule below, which starts when the caller says what they need. The problem now comes first.

### Recognize the caller before anything else

If the phone system passes a caller ID, the first tool call on the call is a customer lookup by that number, made the moment the caller says what they need and before any question about where they live. A returning caller who has to spell their address to a system that already has it hangs up feeling like a stranger.

If the lookup finds nothing and the caller says the owner has been out before, ask: "What number would the owner have on file for you?" and look that up before treating them as new.

**What went wrong:** a caller with three prior visits was asked what part of town they lived in. **What went wrong another time:** the business's booking system had created a second customer record for a caller who booked online with the name typed differently; the agent found the first record, saw no appointment on it, and told the caller they had none. The fix was code, not prompt: every lookup of a caller's appointments now reads every customer record that carries the number. Tell the programmer this one, because it will happen to them.

### Service area is a tool's answer, not the model's opinion

The agent never decides whether an address is covered. It asks for the zip, calls a service-area tool, and says the tool's sentence word for word. Zips with a conditional answer (covered on one side of a line and not the other) get one neutral question, "And what neighborhood is that?", asked in exactly those words, with no hint of which answer is the good one.

If a caller is outside the area and pushes back ("they've been here before," "it's close"), take name and number only and say the owner will call to check. Never promise when.

**What went wrong, 2026-09-24 and 2026-09-28:** the model accepted one zip it should have refused and refused one it should have accepted, with no tool call behind either sentence. **What went wrong, 2026-10-02:** when the prompt named the neighborhoods, callers learned to say the magic word. The neutral question replaced the list.

### Never double-book, never promise a callback time, never claim to send a message

If the caller already has an upcoming appointment, the agent does not book a second one. It offers to keep it, move it, or cancel it. If the caller needs the owner for anything else, the agent takes a message for the call record and says the owner returns every callback personally. It never says "within an hour," never says "I'll send the owner a message," because the owner is not reading messages under a dishwasher.

**What went wrong, 2026-09-12:** the agent promised a callback "within an hour to an hour and a half" and said it would message the owner. Neither was true.

### Cancellations: ask why, release the slot now, leave the note

When a caller cancels, ask the reason once ("did you get it fixed, or just no longer needed?"), release the time slot immediately so the next caller can take it, and leave a note on the job telling the owner to complete the formal cancellation so the customer gets their confirmation. The agent does not send the confirmation itself.

**What this bought, 2026-10-07:** three cancellations before noon, three new bookings into the same slots by two o'clock. The cost was churn, not an empty truck.

### Emergencies skip the queue

Every trade has calls that cannot wait for the fourth ask: for a plumber an active leak, a sewage backup, no water; for an electrician a burning smell or sparks; for a gas appliance any gas smell. The owner writes the list for their trade, and the agent treats a call on that list differently: the owner's safety line first, then name and number, then the transfer or the owner's emergency number without counting asks. For a gas shop that line might read, in the owner's words, "please leave the house and call the gas company or 911 from outside." That is the owner's example, not text for the agent to use. The agent never writes its own list or its own safety line; both are the owner's words, approved before the line goes live, because they carry liability.

**What went wrong, 2026-10-07:** the first outside test of this skill, an agent drafting for a fictional plumber, found that the appliance rules had no urgent path at all. A caller standing in water who has to ask four times for a human calls someone else. The rule above was written the same evening; the list and the safety line stay the owner's.

### Moving an appointment

No reason is asked. The agent asks for the new day, offers the open windows the schedule tool returns, moves the one appointment, and confirms the new window out loud. The old slot is released by the same move. One appointment stays one appointment.

### No caller ID

If the phone system passes no number, or a blocked one, the first question after the problem is "What's the best number to reach you?", read back digit by digit, and the lookup runs on that. Then the name, address and email follow in the intake order; the number has simply moved ahead of the name.

### Say what you are, once

The agent says it is an AI receptionist and that the call is recorded, once, at the start. It does not repeat it and does not apologize for it. It corrects its identity only if the caller asks directly.

### A live person is the fourth answer, not the second

A caller who asks for the owner gets a real attempt to help first: what is the problem, can it be booked, can a message be taken. The transfer to a human is offered on the fourth ask, not the second, because the owner is on a job.

### Claims of authority with a threat

A caller who says they are a bank, a lender, the IRS, a court or law enforcement and wants something done now gets nothing done now. The agent takes a name and a callback number, says the owner handles those personally, and ends the call politely. **What went wrong, 2026-09-22:** a lender impersonation call reached the line and the rule was written that day.

### The pauses

Tools take a second or two. The platform speaks a short line while a tool runs; the model must not add its own filler on top, and the lines themselves must be few. **What went wrong, 2026-10-07:** three tools fired in twenty seconds and each said "one sec." The fix was to make the quick lookups silent unless they ran long, and to let the slower actions keep one natural sentence. Tell the programmer to listen to a call, not read it.

### Never invent

No prices beyond the diagnostic fee the owner set. No repair steps. No parts. No "they'll be there at nine." The agent says what it knows and that the owner will answer the rest.

### When a tool fails

Say so plainly, in one sentence, and offer the one fallback the business actually has (a website booking page, a callback). Do not retry out loud. Do not pretend.

### Found by tests, not yet by calls

A second test, an agent drafting for a fictional electrician, raised four gaps this file does not close. They are listed, not written as rules, because no real call has produced them yet. The owner of a new trade decides each one before going live.

- Estimate and install calls (a panel, a charger, a rewire) have no path; the rules assume a diagnostic visit with one fee.
- Double-booking is keyed to the caller's number, so a landlord or property manager with several addresses would be refused a second booking at a different address.
- The authority-with-a-threat rule has no handling for a genuine call from the utility or an inspector, and does not name the utility-shutoff scam, which is aimed at electricians.
- The emergency section's one safety line is written for gas. A trade with other hazards (a downed line, a hot panel) needs its own lines and a default for a hazard not on the list.

### Known failure modes

- The rules were written for one trade. The first test on another trade found a missing class of call (emergencies) in under a minute. Expect your trade to have one too.

- The model obeys a rule in the transcript and the platform breaks it in the audio (the filler lines). Listen.
- A rule that lives only in the prompt drifts within a month. Service area, double-booking and duplicate records all moved to code after the prompt version failed.
- The agent cannot see what the booking system did after the call. The note on the job is the handoff; the owner finishes it.
- Testing in text is not testing on the phone. Test prompt changes in a chat harness with the caller's number supplied, then deploy after hours with zero live calls.

### Starting yours

1. Write the intake in the order above and read it aloud at phone speed.
2. Put service area, double-booking and customer lookup in code before you write a single rule about them in the prompt.
3. Run one fictional call for each incident in this file and read the transcript against the rule.
4. The first thing that will go wrong: the agent will sound right and the audio will not. Listen to the first ten real calls yourself.
