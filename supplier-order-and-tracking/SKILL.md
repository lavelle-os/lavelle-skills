---
name: supplier-order-and-tracking
description: "How an AI assistant turns a paid online parts order into a distributor order the owner places, shipped blind to the buyer, and then gets the tracking number back to the customer and the owner: the part number in the product's SKU field, the ship-to read back, the store order number as the purchase order, tracking matched from the distributor's email, and an alert that leaves the full number out of shared channels. Use when a store order comes in or a shipment email arrives. Prepares and applies; never places or pays for an order."
license: MIT
---

# Supplier order and tracking

**Gets an online parts order ready for the distributor, then gets the tracking number to the customer.**

Part of [Lavelle skills](../README.md), rules files from a one-truck appliance repair shop. New here? Start with that page.

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. It's for an online parts store that doesn't keep stock, where a distributor ships each part straight to the buyer. When an order is paid, the assistant gets the distributor's order ready for you to place. When the part ships, it reads the distributor's shipping email and puts the tracking number on the order. Then it emails the customer and tells you. You place and pay for every order yourself.

It comes from my one-truck appliance repair shop in Alabama, from its online parts store, and from the orders that store couldn't send on to the distributor.

## Who it's for

- Small online stores that have a distributor ship parts straight to the buyer.
- Repair shops that sell parts online alongside their service work.

## Words you'll see

- **Distributor:** the warehouse that ships the part.
- **SKU field:** the box on each product in your store that holds its part number.
- **Ship blind:** the box shows your store's name, not the distributor's, and has no distributor invoice inside.
- **Purchase order (PO) number:** the number the distributor tracks your order by. Here, it's your store's own order number.

## What you need

- Pasted into a chat app, it writes the distributor order and the customer's email for you to copy and send.
- To read shipping emails and update orders by itself, it has to be connected to your store and your email. That takes setup by someone technical. My store is set up that way.

## What it does

1. Checks that each product has the distributor's part number in its SKU field.
2. Writes out the customer's address in the same sequence as the distributor's order form, so you can copy it top to bottom.
3. Marks the order to ship blind.
4. Matches the distributor's shipping email to the right order by zip code and last name.
5. Puts the tracking number on the order only once, so the customer gets one email, and tells you without posting the full number anywhere shared.

## What it won't do

- Place or pay for an order.
- Type in card or account details.
- Treat a number in a product's title as the part number until someone confirms it.
- Post a full tracking number or a customer's address where other people can see it.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, the copy button at the top right of the file does it in one click.
2. Paste it into a new chat in any AI chat app. A free one works for this test.
3. Type the request below. Leave off the > mark.

> Using these rules: a paid order came in for one made-up water tube, but the product's SKU field is empty. Get the order ready.

A good answer says in its first line that the order needs a part number before it can go ("needs manual sourcing," meaning someone has to find the part number by hand).

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant.*

You prepare the distributor order for each paid store order, and you get the tracking back to the customer when it ships. The owner places and pays for every order.

### The part number lives in the SKU field

Each product in the store carries the distributor's part number in its SKU field, not only in its title. Without it an order cannot be matched to a part or a price. A number in the product's title is a hint, not a part number, until someone confirms it and copies it into the SKU.

**What went wrong, 2026-07-24:** the store's first real order could not be routed. Seventeen of its twenty-one products had a blank SKU field; the part number lived only in the product title. Every SKU was filled the same day.

### The order packet

For each order: ship blind (the customer's address, no distributor branding or invoice in the box, the store's name as the return address); the store's order number as the purchase order number; and each ship-to field written in the order the distributor's form asks for, so the owner can copy them top to bottom. Read the ship-to back against the store order before the owner places it. The owner's margin (retail collected, cost, shipping) is shown to the owner only.

### When it ships

The distributor's shipment email is matched to the open order by the ship-to zip code and confirmed by the last name. The tracking number is applied once: the order is marked shipped, the customer is emailed, and the store order is completed. An empty tracking number is refused, and the same number with spaces or different case counts as the same number.

**What went wrong, 2026-10-12:** the first fully automatic run applied a tracking number within a minute of the distributor's email. It also showed that nothing told the owner. A shipped alert was added that day.

### Tell the owner, carefully

The shipped alert says the part, the carrier, the city and state, whether the customer email went out, and whether the store order completed. If the alert goes to a shared or public channel, it carries only the last four digits of the tracking number, never the street or the customer's name.

### Never

Place or pay for an order. Enter card or account details. Put the distributor's branding or price in the customer's box. Post a full tracking number or address to a shared channel.

### Known failure modes

- A new product added without its SKU, so its first order cannot route.
- A ship-to typo that is copied faithfully.
- A shipment email that arrives before anything is watching for it.
- An alert sent to a channel nobody is subscribed to.

### Starting yours

1. Check every product in your store for a filled SKU.
2. Write your distributor's ship-to form fields, in order.
3. Run one fictional order through the packet and read it back.
4. The first thing that will go wrong: an order will arrive for a product with no SKU. Make the packet say "needs manual sourcing" in its first line.
