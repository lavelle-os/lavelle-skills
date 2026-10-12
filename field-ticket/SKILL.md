---
name: field-ticket
description: "How an agent writes a service ticket for a trade business from the technician's spoken findings: the customer-visible write-up, the parts lines, the pricing rules, and what never goes on an invoice. Use when asked to draft or update a job ticket, invoice line, or repair write-up from a tech's notes. Drafts the lines; the technician approves the price."
license: MIT
---

# The field ticket

*Written after a technician dictated some sixty tickets to an agent from the driveway, and the agent learned what a customer should read, what a parts line may say, and what a price is allowed to look like.*

You are turning a technician's spoken findings into a ticket the customer will read. The technician is standing at the truck, often on a phone, between jobs. Your job is to write the lines; the technician sets or confirms the price. You never invent a finding, a part number, a price or a model number.

## The write-up goes where the customer reads it

Findings belong on the customer-visible service line, in plain words, in this order: the machine (make, model, serial if given); the complaint in the customer's words; what was found and why it causes the complaint; what was done or what is needed; what was verified at the end. A private note on the job is for the technician's eyes only and is used only when the technician says so.

**What went wrong, 2026-09:** findings written as private notes left the customer with an invoice that said "Dishwasher" and a number. The customer could not see what they paid for. Every finding moved to the visible line.

## The write-up is sections, never a paragraph

The customer-visible write-up is broken into short labeled sections with line breaks, in this order, each heading in capitals and each point a one-line bullet: the machine line (make, model, serial, year), WHAT I FOUND, WHAT THE REPAIR WOULD COST, MY RECOMMENDATION, and, when replacement is the recommendation, REPLACEMENTS THAT FIT THIS SPACE (the unit's own measurements first, then numbered models with their color suffixes, a size note where one differs, and a listed price range) and WHERE TO BUY (stores, delivery, haul-away at checkout). Drop a section that does not apply. Never collapse the rest into prose.

**What went wrong, 2026-10-12:** a quote for a landlord was written as one long paragraph with everything in it. The owner had it rewritten into sections and said it was much easier for people to read. The paragraph had the same facts; nobody could find them.

## One line per thing, and a parts line says only what the part is

The labor line carries the write-up and the labor price, and says whether the diagnostic fee is included. Each part gets its own line: the part's plain name and its part number, nothing else. A part line's description shows no price math: no retail price, no shipping arithmetic, no supplier name. Sales tax goes on the invoice as the state requires.

**What went wrong, 2026-09-12 and 2026-09-30:** a parts line that showed the math behind the price invited the customer to redo the math. The rule became "name and number only," ruled twice.

## Prices are the technician's, rounded

The technician gives the labor price, or the convention the shop uses. Part prices follow the shop's rule (ours: the supplier's retail price times 1.10, plus $15 for shipping, rounded to the nearest five dollars; retail is read from the two suppliers the shop actually buys from, never from a manufacturer's site). Every line is rounded to the nearest five. If the technician did not give a price, the line keeps the price it had and the agent says so; it does not guess. A new line that has no price yet stays blank, with the words "price not given by the technician", until the technician gives one.

**What went wrong, 2026-10-07:** a ticket was written at the diagnostic price because the technician forgot to say the labor; he had already changed it himself by the time the agent asked. The agent's write-up survived underneath his price because the agent changed only the fields it was told to.

## Look the part up, and say where

When a part is needed, go to the supplier the shop actually buys from, find the part on the model's own parts list there, confirm it fits that model, and name that supplier and its price in the message to the technician, not on the invoice. A manufacturer's diagram can help you find the number; its retail price never sets the price. When the exact model cannot be found, say which sibling model the number was confirmed on. When two part numbers exist (an original and a replacement), use the current one and say what it replaces.

## Verification is a sentence, not a word

"Ran a cycle; filled, washed, drained, spun; no leak" is a verification. "Works" is not. If the technician did not say what was tested, ask once; if no answer, write what was done and leave verification out rather than invent it.

## What never goes on the ticket

The technician's private opinions of the customer or the house. Other customers' names. Supplier prices. Guesses dressed as findings. A model number read off a blurry tag without saying it was read off a blurry tag.

**What went wrong:** a note about the condition of a home was needed for the technician's own safety on a return visit. It went in a private note, on his word, and nowhere a customer reads.

## Warranty and referrals

When the repair is covered by a manufacturer program, the ticket says so in the customer's words: the program's name or number, what it covers and until when, the number to call, and exactly what to say on the call. The visit is priced at what the technician says, including zero.

## Known failure modes

- The agent rewrites the whole line set and drops a line the technician added by hand. Read the lines first; change only what you were told to.
- The technician dictates the complaint and the finding in one breath. Separate them on the ticket.
- A parts site lists six suffixes of the same number. Pick by the model's own list, not by price.
- Prices arrive late. Write the words first; the number can follow.

## Starting yours

1. Write your shop's price rule in one sentence and put it at the top of this file.
2. Write the three lines every ticket must have: machine, finding, verification.
3. Decide what a private note is for, and write it down.
4. The first thing that will go wrong: the agent will put the parts math on the invoice because it was in the technician's sentence. Strip it.
