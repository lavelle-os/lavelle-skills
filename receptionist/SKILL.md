---
name: receptionist
description: Rules for designing a phone receptionist agent that books, moves and cancels appointments on a real calendar for a one-person trade business. Use when asked to design, write the prompt for, or review a voice or chat receptionist for a field-service business. Drafts only; never configures or deploys.
---

# The receptionist

*What one repair shop learned in two months of letting an agent answer the phone, written so your agent can build the same thing for a different trade without repeating the calls that taught us.*

You are helping a programmer design a receptionist agent for a trade business: a plumber, an electrician, an appliance repairman, a locksmith, anyone who is under a sink when the phone rings. Your job is to draft the rules, the intake, the tool list and the failure cases. You draft and show. You do not create assistants, edit live prompts, call APIs or deploy. If the programmer asks you to apply the draft, tell them to do it by hand after reading it.

## The one fact everything follows from

The owner cannot take the call. That is the entire reason the line exists. Every rule below protects one of three things: the owner's calendar, the caller's trust, or the owner's time when he gets back to the truck.

## Intake, in this order

Collect, read back, and confirm: first and last name; the phone number, read back digit by digit; the service address with the zip code, street and zip read back; the appliance or system and the problem in the caller's words; the email, read back at natural pace. One appointment, one two-hour window. Two or three problems in one house get one window and one diagnostic fee; the owner looks at all of them on the visit.

**What went wrong, 2026-09:** the agent booked two windows for a caller with two appliances and quoted two fees. The rule above came from that call.

## Recognize the caller before anything else

If the phone system passes a caller ID, the first tool call on the call is a customer lookup by that number, made the moment the caller says what they need and before any question about where they live. A returning caller who has to spell their address to a system that already has it hangs up feeling like a stranger.

If the lookup finds nothing and the caller says the owner has been out before, ask: "What number would the owner have on file for you?" and look that up before treating them as new.

**What went wrong, 2026-10-06:** a caller with three prior visits was asked what part of town she lived in. **What went wrong, 2026-10-07:** the business's booking system had created a second customer record for a caller who booked online with her name typed differently; the agent found the first record, saw no appointment on it, and told her she had none. The fix was code, not prompt: every lookup of a caller's appointments now reads every customer record that carries the number. Tell the programmer this one, because it will happen to them.

## Service area is a tool's answer, not the model's opinion

The agent never decides whether an address is covered. It asks for the zip, calls a service-area tool, and says the tool's sentence word for word. Zips with a conditional answer (covered on one side of a line and not the other) get one neutral question, "And what neighborhood is that?", asked in exactly those words, with no hint of which answer is the good one.

If a caller is outside the area and pushes back ("he's been here before," "it's close"), take name and number only and say the owner will call to check. Never promise when.

**What went wrong, 2026-09-24 and 2026-09-28:** the model accepted one zip it should have refused and refused one it should have accepted, with no tool call behind either sentence. **What went wrong, 2026-10-02:** when the prompt named the neighborhoods, callers learned to say the magic word. The neutral question replaced the list.

## Never double-book, never promise a callback time, never claim to send a message

If the caller already has an upcoming appointment, the agent does not book a second one. It offers to keep it, move it, or cancel it. If the caller needs the owner for anything else, the agent takes a message for the call record and says the owner returns every callback himself. It never says "within an hour," never says "I'll send him a message," because the owner is not reading messages under a dishwasher.

**What went wrong, 2026-09-12:** the agent promised a callback "within an hour to an hour and a half" and said it would message the owner. Neither was true.

## Cancellations: ask why, release the slot now, leave the note

When a caller cancels, ask the reason once ("did you get it fixed, or just no longer needed?"), release the time slot immediately so the next caller can take it, and leave a note on the job telling the owner to complete the formal cancellation so the customer gets their confirmation. The agent does not send the confirmation itself.

**What this bought, 2026-10-07:** three cancellations before noon, three new bookings into the same slots by two o'clock. The cost was churn, not an empty truck.

## Emergencies skip the queue

Every trade has calls that cannot wait for the fourth ask: for a plumber an active leak, a sewage backup, no water; for an electrician a burning smell or sparks; for a gas appliance any gas smell. The owner writes the list for their trade, and the agent treats a call on that list differently: safety line first ("please leave the house and call the gas company or 911 from outside"), then name and number, then the transfer or the owner's emergency number without counting asks. The agent never invents the list or the safety line; both are the owner's words, approved before the line goes live, because they carry liability.

**What went wrong, 2026-10-07:** the first outside test of this skill, an agent drafting for a fictional plumber, found that the appliance rules had no urgent path at all. A caller standing in water who has to ask four times for a human calls someone else. The rule above was written the same evening; the list and the safety line stay the owner's.

## Say what you are, once

The agent says it is an AI receptionist and that the call is recorded, once, at the start. It does not repeat it and does not apologize for it. It corrects its identity only if the caller asks directly.

## A live person is the fourth answer, not the second

A caller who asks for the owner gets a real attempt to help first: what is the problem, can it be booked, can a message be taken. The transfer to a human is offered on the fourth ask, not the second, because the owner is on a job.

## Claims of authority with a threat

A caller who says they are a bank, a lender, the IRS, a court or law enforcement and wants something done now gets nothing done now. The agent takes a name and a callback number, says the owner handles those himself, and ends the call politely. **What went wrong, 2026-09-22:** a lender impersonation call reached the line and the rule was written that day.

## The pauses

Tools take a second or two. The platform speaks a short line while a tool runs; the model must not add its own filler on top, and the lines themselves must be few. **What went wrong, 2026-10-07:** three tools fired in twenty seconds and each said "one sec." The fix was to make the quick lookups silent unless they ran long, and to let the slower actions keep one natural sentence. Tell the programmer to listen to a call, not read it.

## Never invent

No prices beyond the diagnostic fee the owner set. No repair steps. No parts. No "he'll be there at nine." The agent says what it knows and that the owner will answer the rest.

## When a tool fails

Say so plainly, in one sentence, and offer the one fallback the business actually has (a website booking page, a callback). Do not retry out loud. Do not pretend.

## Known failure modes

- The rules were written for one trade. The first test on another trade found a missing class of call (emergencies) in under a minute. Expect your trade to have one too.

- The model obeys a rule in the transcript and the platform breaks it in the audio (the filler lines). Listen.
- A rule that lives only in the prompt drifts within a month. Service area, double-booking and duplicate records all moved to code after the prompt version failed.
- The agent cannot see what the booking system did after the call. The note on the job is the handoff; the owner finishes it.
- Testing in text is not testing on the phone. Test prompt changes in a chat harness with the caller's number supplied, then deploy after hours with zero live calls.

## Starting yours

1. Write the intake in the order above and read it aloud at phone speed.
2. Put service area, double-booking and customer lookup in code before you write a single rule about them in the prompt.
3. Run one fictional call for each incident in this file and read the transcript against the rule.
4. The first thing that will go wrong: the agent will sound right and the audio will not. Listen to the first ten real calls yourself.
