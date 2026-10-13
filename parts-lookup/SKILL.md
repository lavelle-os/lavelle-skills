---
name: parts-lookup
description: "How an AI assistant finds the right replacement part for a specific appliance and says where it can be bought today: the model from the tag, the model's own parts diagram, discontinued parts and their replacements, parts sold only inside an assembly, and how to read a supplier's stock. Use when asked to find a part number, check stock, or confirm a part fits a model. Finds and reports; never orders, pays or prices for the customer."
license: MIT
---

# Parts lookup

**Finds the right replacement part for an appliance, and where you can buy it today.**

Part of [Lavelle skills](../README.md), rules files from a one-truck appliance repair shop. New here? Start with that page.

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. With these rules, the assistant looks up appliance parts the way my repair shop does. You give it the model number from the machine's tag and say what broke. It finds the part, where to buy it, and whether it's in stock. It tells you anything it isn't sure about, and it never buys anything.

It comes from my one-truck appliance repair shop in Alabama. Most of these rules are here because a lookup came back wrong without them.

## Who it's for

- Appliance repair techs looking up parts from a phone between jobs.
- A homeowner fixing their own machine who wants the right part the first time.

## Words you'll see

- **Tag:** the sticker or plate on the machine with its model and serial numbers.
- **Parts diagram:** the maker's drawing of the machine, with every part numbered, split into sections such as the door or the pump.
- **Supplier:** the parts house you buy from.
- **Discontinued:** the maker stopped selling that part. Usually a newer part replaces it.
- **Backorder:** the supplier is out, and will ship when more arrive.
- **Bake element:** the heating coil in the bottom of an oven.

## What you need

- An AI assistant that can browse the web, so it can read supplier pages and stock. Without that, it can only tell you what to look for.
- One that accepts photos, if you want it to read the tag for you.

## What it does

1. Reads the model number off a photo of the tag, one character at a time.
2. Finds the part on that model's own parts diagram, in the right section.
3. If the part is discontinued, looks for the part that replaced it.
4. Checks whether the supplier has it, and how soon you can get it.
5. Reports back in plain words, with each doubt in its own sentence.

## What it won't do

- Buy anything, pay, or type in card details.
- Give a part number from memory.
- Say a part fits when no parts list confirms it.
- Get past a website's "prove you're human" check. That one is for a person to clear.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, the copy button at the top right of the file does it in one click.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules, find the bake element for a made-up oven, model EX-100. Show me what you find. Don't order anything.

A made-up model won't match any real parts list. A good answer says so, asks for a photo of the tag, and doesn't guess a part number.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You are finding the part a technician needs for one machine, and saying where it can be bought and how soon. The technician is often in the customer's kitchen. You report the part, the supplier, the stock and anything you are unsure of. You never order, never pay, and never set the customer's price (the part-pricing skill does that). If you cannot reach any supplier or parts list, say so and ask for the tag photo and which piece; never fill the gap from memory. The incidents below are lessons, not answers: confirm every part on the list each time, even for a model that looks familiar.

### Start from the tag, not the description

The model and serial come from a photo of the tag. Read every character: a zero and the letter O look alike, and the letters at the end of a model number mark a version and matter. If the tag is blurry, say what you could not read. If the supplier lists the model under a slightly different number, say which one you matched and why.

**What went wrong, 2026-10-13:** a wall oven's tag seemed to show a zero after one letter of the model. The supplier listed the same series without it. The lookup matched the listed model and said so, instead of reporting "model not found."

### Use the model's own parts list

Find the part on that model's diagram, in the right section (upper oven, lower oven, a dishwasher's pump area, the door). The technician's words ("the light up top", "the hose out of the pump") point to a section. Confirm which piece they mean before naming a number: inlet or outlet, upper or lower.

**What went wrong, 2026-10-12:** a technician said a dishwasher was leaking at "the hose between the sump and the pump." The first lookup named the inlet sleeve. The technician meant the outlet elbow, which is not sold on its own: it comes only inside the whole wash pump. The technician remembered that before the parts list confirmed it.

### Discontinued is not the end

When a part shows "no longer available," look for what replaced it before saying it is gone. The supplier's page may list no replacement while the manufacturer's own parts list does. Name the current number and what it replaces.

**What went wrong, 2026-10-13:** an oven's original bulb read "no longer available" at the supplier, with no replacement listed. The manufacturer's parts list named a standard 40-watt appliance bulb as its replacement, and the supplier stocked a heat-rated one.

### A kit with no model list is not confirmed

Some kits and universal parts list no models on their page. Name the part, and tell the technician the fit is not confirmed for this model.

**What went wrong, 2026-10-12:** a dryer's drum roller support showed as discontinued on the model's list. The current roller kit's page listed no models. The quote named the kit and flagged the fit for the technician to check.

### Read the stock line that matters

A supplier's page can show its own shelf as out of stock while a second stock line further down the page, from other warehouses, still has units. A missing delivery-date line usually means an open-ended backorder, not a date. The manufacturer's own store is separate inventory and can disagree by days. Check both before saying a part cannot be had. Give the branch count when a branch is near enough for same-day pickup.

**What went wrong, 2026-08:** a control board read out of stock at the distributor while the manufacturer's store could ship it the same day. Another part looked dead for two weeks because that second stock line further down the page was missed.

### When a site asks if you are human

A "verify you are human" page is the owner's to clear. Never solve it. Say the site is walled and try the other supplier. These pages often clear on their own within the hour.

### What you report

The model as matched; the part's plain name; the part number and what it replaces; where you found it; that supplier's retail price; stock (branch counts if shown); and every doubt, in a sentence each. Supplier prices go to the technician, never onto the customer's invoice.

### Never

Order, pay, or enter card or account details. Solve a human check. Give a part number from memory. Set the customer's price. Say a part fits when no list confirms it.

### Known failure modes

- The right part for a model whose number differs by one character.
- The upper-oven part when the technician meant the lower oven.
- A confident part number from memory that was right last year.
- "Out of stock" on the supplier's own shelf read as "cannot be had."

### Starting yours

1. Write down the two suppliers you buy from and how each one's page shows stock.
2. Look up one part you already know, end to end, and time it.
3. Run the skill on a fictional machine with a discontinued part.
4. The first thing that will go wrong: the agent will report the first part number it finds. Make it name the diagram section it came from.
