---
name: starting-a-home-service-business
description: The order of steps for starting a one-person home-service business (appliance repair, plumbing, electrical, HVAC, handyman, cleaning, lawn) and what an agent can do at each step versus what the owner must do. Use when someone says they want to start a trade or home-service business, or asks what to do first. The agent researches, drafts and keeps the list; the owner decides, signs, files and pays.
license: MIT
---

# Starting a home-service business

*The order one owner would have wanted handed to him in January 2018, when he opened a one-truck appliance repair business and found every step by running into it. Written so an agent can walk the next person through it, and so a programmer can set it up for someone else.*

You are helping one person start a home-service business, or helping a programmer set that up for them. Your job is to keep the list, research each step from official sources, draft what can be drafted, and say plainly which steps are the owner's alone. Two humans stay in the loop from day one: the owner, and a tax preparer or attorney for anything with a signature or a fee.

## The one fact everything follows from

The owner's first paying job is the deadline. Every step below either must be done before that job, or can wait. Keep the two lists apart, and keep the "before" list short enough to finish in weeks, not months.

## The steps, in order

1. **Decide what you do and where.** The trade, the brands or systems you will not touch, and the service area as a list of places, with the places you decline named. **What went wrong, 2026-10:** a receptionist agent booked a job in a neighborhood the owner does not serve because the area was a feeling, not a list. The owner ruled it a list, with the declined names written down. Done when the owner can say the area in one breath.

2. **Research the licenses.** Use the `business-license-research` skill: state, county or parish, city, trade. Output is a checklist with sources and dates, labeled CONFIRMED or UNVERIFIED, second-read before anyone acts. Done when the owner has the checklist and knows which office is first.

3. **Choose the entity and the name.** The agent lays out the questions, not the answer: sole proprietor now and an LLC later, or the LLC first; whether the name is available; what a registered agent is. The owner decides with a preparer. The owner in the worked example ran as a sole proprietor for his first years and formed a company later; neither order is wrong. Done when the owner has picked and the preparer has agreed.

4. **Tax number, bank account, and books from the first dollar.** The federal tax number is free from the IRS. A separate bank account before the first deposit. A bookkeeping method, even a spreadsheet, from day one. **What went wrong, 2026-10:** after a bookkeeper change, an owner had to reconstruct his own records, with the prior years' returns as the only map. Books the owner can read himself are not optional. Done when the owner can say what came in and went out last week.

5. **Insurance.** Questions for the owner's insurance agent, not answers. What general liability does the first job call for? Does the auto policy cover a truck used for work? What workers' compensation does the state require at the owner's employee count, according to the state's own page? Done when the agent has answered, the policy numbers exist and the renewal dates are on the calendar.

6. **A phone number, a calendar, and a way to book.** A business number separate from the personal cell. Booking software with online booking, because customers book themselves at night. A receptionist agent can answer when the owner is under a sink; use the `receptionist` skill, which carries the rules learned from real calls. Done when a stranger can book a visit without the owner touching the phone.

7. **Pricing and the ticket.** A diagnostic fee that is the same every time and credited toward the repair, parts priced by one written rule from the owner's own suppliers' prices, and every line on the customer's invoice in plain words. Use the `field-ticket` skill. **What went wrong, 2026-10-09:** part prices were being taken from manufacturer sites until the owner ruled that only his two suppliers' retail counts. One rule, written down, ends that. Done when two different people could price the same job the same way.

8. **Parts and suppliers.** Accounts with two suppliers, one local with a counter and one that ships. The agent can look up parts on the model's own diagram and the supplier's stock before the owner drives. Done when the owner can find a part number and a price without leaving the job.

9. **Being found.** In this order: the free business profile on the map, claimed and complete, with the real address and hours; a one-page site that says what you fix and where; reviews, answered in the owner's own voice with no sales pitch; videos of real repairs once the first three are in place. **What went wrong, 2026:** a listing left with a placeholder name and a made-up street sat in search for months, and a map ranking that had been lost took weeks of daily habits to recover. The profile is the storefront; keep it true. Done when a search for the trade and the town shows the business on the map.

10. **The first hire.** Questions for the owner, not advice. Is the owner turning down work yet? What would a written screen for the first technician ask? What would a good first week look like for the new person? Done when the owner can answer the last one in their own words.

11. **What runs on agents and what stays with the owner.** Agents can answer the phone, book, draft tickets, look up parts, draft replies and posts, and keep the books in order. The owner decides prices, hires, what to decline, and anything that costs money. Promote an agent to a new job one job at a time, after it has done the job in draft for a while without a miss. Done when there is a written list of what the agent may do alone.

## Humans in the loop, named

The owner, on everything with money or a signature. A tax preparer, on the entity and the books. An attorney, if there are partners, investors, a lease, or a trade with licensing exposure. The city clerk, who will tell you in five minutes what a day of searching did not.

## Known failure modes

- Step 9 starts before step 2. Marketing a business that is not licensed yet is the fastest way to a letter from the city.
- The agent writes the whole plan at once and the owner does none of it. Showing the ordered list once, so the owner sees the shape, is fine; working it is one step, a "done when," then the next.
- Entity advice gets given instead of entity questions. The agent asks; the preparer answers.
- The receptionist goes live before the service area is a list.
- Books start "next month." They start with the first dollar.
- "Autonomous" gets read as a switch. It is tiers, earned one job at a time.

## Starting yours

1. Put your trade and your town at the top of this file and strike the steps that do not apply.
2. Run step 2 first and let the checklist set the order of steps 3 to 5.
3. Write the "done when" for each step in your own words.
4. The first thing that will go wrong: you will try to skip to step 9 because it is the fun one. Steps 2 and 4 are the ones that keep the business alive.
