---
name: truck-inventory
description: "How an agent keeps an accurate count of the parts on a service truck: every change is a permanent entry (in from a supplier, out against a job, adjusted by hand with a reason), nothing is edited or deleted, a monthly hand count, and a restock list for the owner. Use when asked to record parts in or out, reconcile a truck count, or build a restock list. Counts and lists; never orders, prices or deletes history."
license: MIT
---

# Truck inventory

*Written from building a phone app that counts the parts on a service truck, and from its first real job.*

You keep the count of what is on each truck. The count is only useful if every change leaves a trace, so the history is never edited. You do not price parts, order them, or answer the phone.

## Every change is an entry

Three kinds: **in** (received from a supplier), **out** (used on a job), and **adjust** (a hand correction, with a reason). A wrong count is fixed with a new adjust entry, never by editing or deleting an old one. Each entry has the part number, the quantity, the truck, who made it, and when. An adjust records the change (minus two), with the system count and the hand count both written beside it. You prepare entries; the person or the app records them.

## The part number is the identity

Scan the barcode or type the part number. Two parts with similar names are different parts; one part with two numbers (an original and its replacement) is recorded under the current number, with the old one noted.

## Out against a job

Every part used names the job it went on, so the ticket and the count agree. If a part leaves the truck with no job (a return, a part given to another tech), the entry says so.

## The monthly hand count

Once a month, count the truck by hand. Each difference becomes an adjust entry with the reason if known ("used on a job, not scanned") or "unknown." A rising pile of unknowns is a process problem, not a counting problem.

## The restock list

Parts below the minimum the owner set go on a restock list for the owner. The list is not an order; the owner orders.

## More than one truck

Each truck has its own count. Moving a part between trucks is an out on one and an in on the other, in the same entry pair.

## Test the screen before it rides

**What went wrong, 2026-10-01:** on its first real job, the count app's page went dead on the owner's phone. A test now loads the page's own script before any change ships.

## Never

Edit or delete history. Order or price a part. Record a part under a name instead of its number.

## Known failure modes

- Names and numbers mixed, so one part shows as two.
- Counts drift because parts used on jobs were not scanned.
- A phone with no signal in a basement, so entries are lost unless they queue.

## Starting yours

1. List the parts you carry and the minimum for each.
2. Count one truck by hand and enter the counts as the starting entries.
3. Run a week, then do the first hand count and read the adjust entries.
4. The first thing that will go wrong: parts will leave the truck without being scanned. The monthly count shows you how many.
