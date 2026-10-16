---
name: part-pricing
description: "How an AI assistant turns a supplier's retail price into the price on a customer's part line, the same way every time: one written formula, retail from the suppliers the shop buys from, every line rounded, quoted prices never repriced, and no tax stacked on a price that already covers it. Use when asked to price a part line, check a ticket's part prices, or explain how a price was set. Prices draft lines; the technician approves."
license: MIT
---

# Part pricing

**Turns a supplier's price into the price your customer pays for a part, the same way every time.**

Part of [Lavelle skills](../README.md), rules files from a one-truck appliance repair shop. New here? Start with that page.

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. With these rules, the assistant prices the parts on a repair ticket the way my shop does. You tell it the part's retail price at your supplier. It runs your shop's written formula, rounds each line, and shows you the math. The customer sees only the final price.

It comes from my one-truck appliance repair shop in Alabama. The rules are here because a price came out wrong three times without them.

## Who it's for

- Repair shops that want every tech, and every AI, to price a part the same way.
- Anyone writing tickets who has been asked why a part cost more last time.

## Words you'll see

- **Ticket:** the job record the customer gets, with the work described and the prices listed.
- **Line:** one item on a ticket, such as one part or the labor.
- **Retail price:** the supplier's listed price, before any discount the shop gets.
- **Formula:** your shop's written rule for turning retail into the customer's price.
- **Quoted:** a price the customer has already been given.

## What you need

- Any AI chat app. It doesn't need the web, because you give it the prices.
- Your own formula. Ours is in the rules below, under "One written rule." Before you paste the page, change those numbers to yours.

## What it does

1. Takes the retail price from the supplier you actually buy from.
2. Runs your formula. Ours is the retail price times 1.10, plus $15 for shipping on every part number. Several of the same part share one $15. In our books the extra 10% covers the sales tax.
3. Rounds each line to the nearest $5. Labor is your number, rounded the same way.
4. Shows you the math, and keeps the math out of what the customer sees.
5. Leaves alone any price a customer was already quoted.

## What it won't do

- Make up a price, or use one from memory.
- Use the manufacturer's own website price, which runs higher.
- Change a price a customer was already quoted.
- Add "plus tax" when your formula already covers the tax.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, the copy button at the top right of the file does it in one click.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules, price two made-up parts for a ticket. Part one is $20.00 retail at our supplier. Part two is $85.00. Labor is $150. Show me the math.

A good answer prices part one at $35 and part two at $110, leaves the labor at $150, and adds the lines to $295.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You are setting the price a customer pays for a part. Two people pricing the same part on the same day should get the same number. The math goes to the technician; the customer sees only the price.

### One written rule

Ours: the supplier's retail price, times 1.10, plus $15 for shipping, rounded to the nearest five dollars. In this shop's books the 1.10 covers the sales tax, so the ticket never says "plus tax" on top of it. The $15 is added on every part line, even a cheap part, because each part is priced as if it ships on its own. Several of the same part number ship together, so they share one $15: one line with the quantity, and each piece priced at retail times 1.10 plus $15 divided by the quantity, rounded to five. Three knobs at $43.89 retail come to $55 each, not $65. Labor is not run through the formula: it is the technician's number, rounded to five. Whatever your rule is, write it down with its numbers, and apply it per line.

Worked examples with made-up retail prices: $100.00 becomes 125.00, so $125. $56.40 becomes 77.04, so $75. $44.70 becomes 64.17, so $65. Round each line, never the total.

### Retail comes from where you buy

Read retail from the suppliers the shop actually buys from, on that supplier's own page for the part. Never from a manufacturer's store or a parts website, which run higher. Use a big parts retailer only when neither supplier carries the part, and say so in the message to the technician. Use retail, not the shop's own discounted cost.

**What went wrong, 2026-10-09:** tickets were priced from a manufacturer's retail and came out higher than the shop's own suppliers would have set them. They were repriced from the supplier the same day.

### A quoted price stays quoted

Once a price has gone to a customer, a new rule does not change it. New lines follow the new rule; old quotes keep their number.

**What went wrong, 2026-10-09:** a ticket already quoted to a customer was repriced under a rule made that morning. The owner had it put back.

### Don't stack tax

If the rule's multiplier covers tax, the write-up does not add "plus sales tax." Whether parts and labor are taxable, and how, is a question for the shop's accountant (CPA), not the agent; the agent keeps the shop's rule consistent and flags any line that looks inconsistent.

**What went wrong, 2026-10-13:** two tickets said "plus sales tax" on top of prices whose 1.10 already covered it. Both customers paid the stated totals, and the words came off.

### The math goes to the technician

Show the retail, the supplier, the formula and the rounding in the message to the technician. The customer's part line says only the part's name and number (see the field-ticket skill).

### Never

Invent a retail price. Price from memory. Reprice a quoted job. Add tax wording the shop's rule does not use. Put the math, the supplier or the shop's cost on the customer's invoice.

### Known failure modes

- Rounding the total instead of each line.
- Using the shop's discounted cost instead of retail.
- A retail price read last month, used today.
- A part bought from a third supplier priced as if it came from one of the two.

### Starting yours

1. Write your formula with its numbers at the top of this file.
2. Price five parts you already sold, and check the results against what you charged.
3. Decide, with your CPA, how tax is handled, and write that sentence down.
4. The first thing that will go wrong: the agent will round the total. Give it an example with three lines.
