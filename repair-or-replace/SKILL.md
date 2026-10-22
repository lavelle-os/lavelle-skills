---
name: repair-or-replace
description: "How an AI assistant lays out a costly repair next to replacement options so the customer can decide: the repair quote, the technician's recommendation if the technician gave one, good, better and best replacements of a similar size with where to buy them, and an invoice that carries only the diagnostic until the customer chooses. Use when a repair costs a large share of a new machine, or when asked to compare repairing and replacing. Drafts the write-up; the customer decides."
license: MIT
---

# Repair or replace

**Lays out an expensive repair next to new machines, so the customer can decide.**

Part of [Lavelle skills](https://github.com/lavelle-os/lavelle-skills#if-you-have-never-used-github-start-here), rules files from a one-truck appliance repair shop. New here, or never used GitHub? Start with that page. Want to try this one now? Jump to [Try it](#try-it).

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. Sometimes a repair costs close to the price of a new machine. With these rules, the assistant writes the page the customer reads to decide. It says what's wrong and what the repair would cost. It shows three new machines that fit the same space, and where to buy them. The customer chooses. The assistant doesn't push either way. If the technician has an opinion, it's written down as the technician's.

It comes from my one-truck appliance repair shop in Alabama, after a week when three customers had repairs that cost close to a new machine.

## Who it's for

- Repair techs who have to tell a customer "it's fixable, but it's expensive."
- Service businesses that want the repair quote on paper without billing for it.

## Words you'll see

- **Ticket:** the job record the customer gets.
- **Invoice:** the part of the ticket the customer pays. While they decide, it shows only the visit fee.
- **Write-up:** the description on the ticket. The repair quote goes here, on record but not billed.
- **Diagnostic:** the visit fee for finding the problem.
- **Compressor:** the pump that runs a refrigerator's cooling. Replacing one is among the most expensive repairs.
- **Good, better, best:** three replacement choices at rising prices.

## What you need

- Any AI chat app. It writes the write-up and the bill. You put them into whatever you use for tickets, even paper.
- For replacement prices, an assistant that can browse store websites. Without that, those slots stay blank for you to fill in.
- The old machine's measurements, if the technician took them. The assistant won't guess them.

## What it does

1. Writes the bill for the diagnostic visit only, while the customer decides.
2. Writes the repair quote into the write-up, part by part.
3. Adds the technician's recommendation, only if the technician gave one.
4. Finds good, better and best replacements of a similar size, with prices read from a store that day.
5. Rewrites the ticket once the customer chooses.

## What it won't do

- Recommend replacing when the technician didn't.
- Guess a machine's size, a price or a model number.
- Promise that a store has one in stock.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, use the icon of two overlapping squares just to the right of the word **Raw** (its label is "Copy raw file"); on a phone, the three dots beside Preview, Code and Blame, then **Copy**. The look-alike icon next to the file name copies only the address.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules, write up a made-up 12-year-old refrigerator that needs a $650 compressor repair. The technician didn't give a recommendation.

A good answer bills only the visit fee and gives no recommendation. If it can't look up store prices, it leaves those slots blank and says so.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You are writing the page a customer uses to decide whether to fix an old machine or buy a new one. The technician found the problem and priced the repair. You lay out both paths plainly, and the customer chooses. You never push either one.

### When this applies

A sealed-system repair (the refrigerant side of a fridge or freezer), a compressor, several parts on an older machine, or any repair the technician says is close to the cost of replacing. The threshold is the shop's, written down. Replacement is never recommended for the shop's convenience.

### The invoice is the diagnostic; the quote is in the write-up

While the customer decides, the invoice carries only the diagnostic visit. The full repair quote goes in the write-up, so it is on record without being billed.

**What went wrong, 2026-10-12:** a rental fridge needed a compressor, and the tenant and landlord had to decide together. The invoice had to show only the diagnostic, with the full quote, the technician's recommendation, and replacements that fit the space in the write-up. The first draft was one long paragraph; the owner had it rewritten in sections, and that became the rule for every write-up.

### The sections, in order

WHAT I FOUND. WHAT THE REPAIR WOULD COST (labor, each part with its price, the total, and whether today's diagnostic counts toward it under the shop's rule). MY RECOMMENDATION, only if the technician gave one, in the technician's words. REPLACEMENTS (good, better and best, a similar size). WHERE TO BUY (the store, the date the prices were seen, and that sale prices change). NEXT STEP.

### Sizes are measured, never guessed

Start the replacements with the old machine's own measurements if the technician measured it. If its capacity is not published, do not supply one. Give each new model's height, width, depth and capacity from the store's own listing, and tell the customer to measure the space.

**What went wrong, 2026-10-13:** a freezer's capacity was not published for its model. A draft said "about 20 cubic feet" for the customer's freezer; it was a guess and came back out. The heading described the new ones instead and told the customer to measure.

### Real models, real prices, dated

Each replacement is a real model number with the price and size read from a store's page that day. Name the store and the date. Never invent a price or a model; if you cannot read a store's page, leave the slot blank and say so. Leave the MY RECOMMENDATION heading out entirely when the technician gave none.

### When the customer decides

If they choose replacement, the ticket becomes the diagnostic with a short line recording their decision, and the repair quote stays for their records. If they choose the repair, the ticket becomes the repair.

**What went wrong, 2026-10-12:** a customer chose to replace a dryer after the repair was quoted. The ticket was reset to the diagnostic, with the quote kept and a line saying the customer chose to replace it.

### Never

Recommend replacement the technician did not recommend. Invent a size, a price or a model. Promise a store has it in stock. Steer the customer to a store for any reason but price and fit.

### Known failure modes

- A replacement that does not fit the space (depth with the door open, the door swing).
- Prices read once and quoted a week later.
- A rental where it is unclear who pays.

### Starting yours

1. Write your threshold for raising replacement, as a share of the new price.
2. Pick the two or three stores your customers actually use.
3. Run the skill on a fictional ten-year-old machine with a failed compressor.
4. The first thing that will go wrong: the agent will fill in the old machine's size from memory. Make it say "not measured."
