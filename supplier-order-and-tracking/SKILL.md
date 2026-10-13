---
name: supplier-order-and-tracking
description: "How an agent turns a paid online parts order into a distributor order the owner places, shipped blind to the buyer, and then gets the tracking number back to the customer and the owner: the part number in the product's SKU field, the ship-to read back, the store order number as the purchase order, tracking matched from the distributor's email, and an alert that leaves the full number out of shared channels. Use when a store order comes in or a shipment email arrives. Prepares and applies; never places or pays for an order."
license: MIT
---

# Supplier order and tracking

*Written from an online parts store that ships straight from a distributor to the buyer, and from the orders it could not route.*

You prepare the distributor order for each paid store order, and you get the tracking back to the customer when it ships. The owner places and pays for every order himself.

## The part number lives in the SKU field

Each product in the store carries the distributor's part number in its SKU field, not only in its title. Without it an order cannot be matched to a part or a price. A number in the product's title is a hint, not a part number, until someone confirms it and copies it into the SKU.

**What went wrong, 2026-07-24:** the store's first real order could not be routed. Seventeen of its twenty-one products had a blank SKU field; the part number lived only in the product title. Every SKU was filled the same day.

## The order packet

For each order: ship blind (the customer's address, no distributor branding or invoice in the box, the store's name as the return address); the store's order number as the purchase order number; and each ship-to field written in the order the distributor's form asks for, so the owner can copy them top to bottom. Read the ship-to back against the store order before the owner places it. The owner's margin (retail collected, cost, shipping) is shown to the owner only.

## When it ships

The distributor's shipment email is matched to the open order by the ship-to zip code and confirmed by the last name. The tracking number is applied once: the order is marked shipped, the customer is emailed, and the store order is completed. An empty tracking number is refused, and the same number with spaces or different case counts as the same number.

**What went wrong, 2026-10-12:** the first fully automatic run applied a tracking number within a minute of the distributor's email. It also showed that nothing told the owner. A shipped alert was added that day.

## Tell the owner, carefully

The shipped alert says the part, the carrier, the city and state, whether the customer email went out, and whether the store order completed. If the alert goes to a shared or public channel, it carries only the last four digits of the tracking number, never the street or the customer's name.

## Never

Place or pay for an order. Enter card or account details. Put the distributor's branding or price in the customer's box. Post a full tracking number or address to a shared channel.

## Known failure modes

- A new product added without its SKU, so its first order cannot route.
- A ship-to typo that is copied faithfully.
- A shipment email that arrives before anything is watching for it.
- An alert sent to a channel nobody is subscribed to.

## Starting yours

1. Check every product in your store for a filled SKU.
2. Write your distributor's ship-to form fields, in order.
3. Run one fictional order through the packet and read it back.
4. The first thing that will go wrong: an order will arrive for a product with no SKU. Make the packet say "needs manual sourcing" in its first line.
