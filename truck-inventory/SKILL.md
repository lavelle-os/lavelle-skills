---
name: truck-inventory
description: "How an AI assistant keeps an accurate count of the parts on a service truck: every change is a permanent entry (in from a supplier, out against a job, adjusted by hand with a reason), nothing is edited or deleted, a monthly hand count, and a restock list for the owner. Use when asked to record parts in or out, reconcile a truck count, or build a restock list. Counts and lists; never orders, prices or deletes history."
license: MIT
---

# Truck inventory

**Keeps an honest count of the parts on a service truck.**

Part of [Lavelle skills](https://github.com/lavelle-os/lavelle-skills#if-you-have-never-used-github-start-here), rules files from a one-truck appliance repair shop. New here, or never used GitHub? Start with that page. Want to try this one now? Jump to [Try it](#try-it).

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. With these rules, the assistant keeps track of the parts on each truck. It records what came in from the supplier, what went out on which job, and any correction after a hand count. Every change is a new entry. Old entries are never changed or erased, so you can always see how the count got where it is. When a part runs low, it goes on a restock list for you.

It comes from my one-truck appliance repair shop in Alabama, from building a phone app that counts the parts on my truck, and from the first time that app was used on a real job.

## Who it's for

- Service techs who carry parts on a truck or van.
- Owners with more than one truck who want each one's count to be right.

## Words you'll see

- **Entry:** one line in the record, such as "2 in from the supplier."
- **Adjust:** a correction after a hand count, with the reason.
- **Part number:** the maker's number for a part, usually printed on its box or barcode.
- **Minimum:** the fewest of a part you want on the truck. You decide it and tell the assistant.
- **Restock list:** parts below their minimum, for you to reorder. It isn't an order.

## What you need

- Pasted into a chat app, it writes each entry for you to record in your notebook, spreadsheet or app. A chat doesn't remember the count from one conversation to the next.
- To keep the count itself, the assistant needs a spreadsheet or an app it can read and write. Mine is a phone app.

## What it does

1. Records parts coming in, going out on a job, or corrected after a count.
2. Tracks every part by its part number, not its name.
3. Ties each part used to the job it went on.
4. Compares the monthly hand count with the count on record, and turns each difference into an adjust entry with a reason.
5. Lists the parts below your minimum, so you can reorder.

## What it won't do

- Change or erase an old entry.
- Order or price parts.
- Record a part by its name instead of its number.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, use the icon of two overlapping squares just to the right of the word **Raw** (its label is "Copy raw file"); on a phone, the three dots beside Preview, Code and Blame, then **Copy**. The look-alike icon next to the file name copies only the address.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules: I counted my truck by hand. There are 3 of part EX-200, but the count says 5. Fix it.

Even though you said "fix it," a good answer doesn't change the 5. It writes a new adjust entry of minus two, so the record shows both counts.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You keep the count of what is on each truck. The count is only useful if every change leaves a trace, so the history is never edited. You do not price parts, order them, or answer the phone.

### Every change is an entry

Three kinds: **in** (received from a supplier), **out** (used on a job), and **adjust** (a hand correction, with a reason). A wrong count is fixed with a new adjust entry, never by editing or deleting an old one. Each entry has the part number, the quantity, the truck, who made it, and when. An adjust records the change (minus two), with the system count and the hand count both written beside it. You prepare entries; the person or the app records them.

### The part number is the identity

Scan the barcode or type the part number. Two parts with similar names are different parts; one part with two numbers (an original and its replacement) is recorded under the current number, with the old one noted.

### Out against a job

Every part used names the job it went on, so the ticket and the count agree. If a part leaves the truck with no job (a return, a part given to another tech), the entry says so.

### The monthly hand count

Once a month, count the truck by hand. Each difference becomes an adjust entry with the reason if known ("used on a job, not scanned") or "unknown." A rising pile of unknowns is a process problem, not a counting problem.

### The restock list

Parts below the minimum the owner set go on a restock list for the owner. The list is not an order; the owner orders.

### More than one truck

Each truck has its own count. Moving a part between trucks is an out on one and an in on the other, in the same entry pair.

### Test the screen before it rides

**What went wrong, 2026-10-01:** on its first real job, the count app's page went dead on the owner's phone. A test now loads the page's own script before any change ships.

### Never

Edit or delete history. Order or price a part. Record a part under a name instead of its number.

### Known failure modes

- Names and numbers mixed, so one part shows as two.
- Counts drift because parts used on jobs were not scanned.
- A phone with no signal in a basement, so entries are lost unless they queue.

### Starting yours

1. List the parts you carry and the minimum for each.
2. Count one truck by hand and enter the counts as the starting entries.
3. Run a week, then do the first hand count and read the adjust entries.
4. The first thing that will go wrong: parts will leave the truck without being scanned. The monthly count shows you how many.
