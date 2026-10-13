# Lavelle skills

Eight rules files from a one-truck appliance repair shop in Alabama that runs on AI agents. Each one tells an agent how to do one job the way my shop does it, and most rules are there because something went wrong without them. I'm the owner, I don't write code, and these are what I learned.

A skill is plain text. It doesn't run anything. Every one tells the agent to draft and show you, never to act on its own.

## Try one in two minutes

**No terminal:** open any skill's `SKILL.md` below, copy all of it into your chat app, and ask for a draft.

**With a coding agent:** this copies the repository once and links the eight skills into the folder Claude Code reads (`~/.claude/skills`) and the one OpenCode reads (`~/.agents/skills`). For any other agent, check where its documentation says skills go.

```
git clone https://github.com/lavelle-os/lavelle-skills ~/lavelle-skills
mkdir -p ~/.claude/skills ~/.agents/skills
for name in receptionist honest-tutor second-model-brief resale-identification field-ticket starting-a-home-service-business business-license-research legal-research-memo; do
  ln -s ~/lavelle-skills/$name ~/.claude/skills/$name
  ln -s ~/lavelle-skills/$name ~/.agents/skills/$name
done
```

Then ask: "Using the receptionist skill, draft the booking rules and the intake script for a fictional plumber. Show me the draft. Don't build anything."

## The eight

| Skill | What it does |
|---|---|
| [receptionist](receptionist/SKILL.md) | Answers a trade business's phone and books on a real calendar. |
| [field-ticket](field-ticket/SKILL.md) | Turns what the tech says in the driveway into the ticket the customer reads. |
| [honest-tutor](honest-tutor/SKILL.md) | Teaches one idea at a time and never makes up a number or a source. |
| [second-model-brief](second-model-brief/SKILL.md) | Writes the brief for a second AI to check the first, and reconciles the answer. |
| [resale-identification](resale-identification/SKILL.md) | Works out what a used piece of furniture is from photos, without guessing a price. |
| [starting-a-home-service-business](starting-a-home-service-business/SKILL.md) | The eleven steps to open a one-person service business, in order. |
| [business-license-research](business-license-research/SKILL.md) | Finds every license and tax account a business needs, from official pages only. |
| [legal-research-memo](legal-research-memo/SKILL.md) | First-pass legal research a lawyer can check in a minute. Never advice. |

## How they were tested

- Under Claude Code on a Mac, an Ubuntu server and a fresh Omarchy 4.0.4 install, and under OpenCode with NVIDIA's free Nemotron model.
- Every skill loaded on both agents. Under Claude all eight held their rules; asked plainly, without the rule in the question, two broke and I fixed them. Under Nemotron three broke and I fixed those too.
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
