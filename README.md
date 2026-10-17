# Lavelle skills

Eighteen rules files from a one-truck appliance repair shop in Alabama that runs on AI agents. Each one tells an agent how to do one job the way my shop does it, and most rules are there because something went wrong without them. I'm the owner, I don't write code, and these are what I learned.

A skill is plain text. It doesn't run anything. Every one tells the agent to draft and show you, never to act on its own.

## Try one in two minutes

**No terminal:** open any skill's `SKILL.md` below, copy all of it into your chat app, and ask for a draft.

**With a coding agent:** this copies the repository once and links every skill into the folder Claude Code reads (`~/.claude/skills`) and the one OpenCode reads (`~/.agents/skills`). For any other agent, check where its documentation says skills go.

```
git clone https://github.com/lavelle-os/lavelle-skills ~/lavelle-skills
mkdir -p ~/.claude/skills ~/.agents/skills
for name in receptionist honest-tutor ai-project-setup second-model-brief resale-identification field-ticket starting-a-home-service-business business-license-research legal-research-memo parts-lookup part-pricing repair-or-replace warranty-and-callbacks bookkeeper contracts-and-policies truck-inventory supplier-order-and-tracking review-replies; do
  ln -s ~/lavelle-skills/$name ~/.claude/skills/$name
  ln -s ~/lavelle-skills/$name ~/.agents/skills/$name
done
```

Then ask: "Using the receptionist skill, draft the booking rules and the intake script for a fictional plumber. Show me the draft. Don't build anything."

## The skills

Every skill's page starts with a plain explanation: what it is, who it's for, the trade words it uses, what you need, what it does and won't do, and a request to try with what a good answer looks like. The rules the AI follows come after that.

| Skill | What it does |
|---|---|
| [receptionist](receptionist/SKILL.md) | Answers a trade business's phone and books on a real calendar. |
| [field-ticket](field-ticket/SKILL.md) | Turns what the tech says in the driveway into the ticket the customer reads. |
| [honest-tutor](honest-tutor/SKILL.md) | Teaches one idea at a time and never makes up a number or a source. |
| [ai-project-setup](ai-project-setup/SKILL.md) | Turns a one-line goal into the pieces of an AI chat project, says which box each goes in, and writes the setup steps. |
| [second-model-brief](second-model-brief/SKILL.md) | Writes the brief for a second AI to check the first, and reconciles the answer. |
| [resale-identification](resale-identification/SKILL.md) | Works out what a used piece of furniture is from photos, without guessing a price. |
| [starting-a-home-service-business](starting-a-home-service-business/SKILL.md) | The eleven steps to open a one-person service business, in order. |
| [business-license-research](business-license-research/SKILL.md) | Finds every license and tax account a business needs, from official pages only. |
| [legal-research-memo](legal-research-memo/SKILL.md) | First-pass legal research a lawyer can check in a minute. Never advice. |
| [parts-lookup](parts-lookup/SKILL.md) | Finds the right part for one machine from its tag, follows discontinued parts to their replacements, and reads supplier stock. |
| [part-pricing](part-pricing/SKILL.md) | Turns a supplier's retail price into the customer's price, one written rule, every line rounded. |
| [repair-or-replace](repair-or-replace/SKILL.md) | Puts a costly repair next to good, better and best replacements, and lets the customer decide. |
| [warranty-and-callbacks](warranty-and-callbacks/SKILL.md) | Return promises with an exact end date, repeat failures, recalls, and no promise no tool keeps. |
| [bookkeeper](bookkeeper/SKILL.md) | Monthly books for one truck and a clean packet for the CPA. Never files, never advises. |
| [contracts-and-policies](contracts-and-policies/SKILL.md) | Drafts NDAs, store terms and warranty wording for an attorney to review. |
| [truck-inventory](truck-inventory/SKILL.md) | Counts the parts on each truck; a wrong count is fixed with a new entry, never an edit. |
| [supplier-order-and-tracking](supplier-order-and-tracking/SKILL.md) | Turns a store order into a blind-ship distributor order and gets the tracking back to the customer. |
| [review-replies](review-replies/SKILL.md) | Drafts review replies in the owner's voice, with no invented details and no sales pitch. |

## How they were tested

- The first eight ran under Claude Code on a Mac, an Ubuntu server and a fresh Omarchy 4.0.4 install, and under OpenCode with NVIDIA's free Nemotron model.
- Each of those eight loaded on both agents. Under Claude all eight held their rules; asked plainly, without the rule in the question, two broke and I fixed them. Under Nemotron three broke and I fixed those too.
- The nine I added on October 13 have had one run each, under Claude on the Mac, with no web. All nine held. Every run found lines that weren't clear, and I fixed them that day. They haven't run on the other machines or under OpenCode yet.
- My own AI graded the runs. [TEST-LOG.md](TEST-LOG.md) has every prompt and every miss.

## Before you rely on one

- Read every draft. A rule in a prompt is a request; put it in code the moment it costs money.
- The skills folder is a git clone. Read a change before you pull it (`git -C ~/lavelle-skills fetch && git -C ~/lavelle-skills log -p HEAD..origin/main`), and don't let your agent write inside it. OpenCode's default agent does, without asking.
- The legal and license skills do first-pass research and say so on every page. They are not legal or tax advice.
- Nobody has tried this on Windows. Copying the folders in should work.

## Make your own

1. Copy a skill folder and rename it.
2. Keep only the rules you have a story for.
3. Run the test above with a made-up customer.

No customer data lives here; `scripts/gate.sh` checks every commit for it before I push. MIT licensed, copyright The Morriss Group LLC.
