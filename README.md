# Lavelle skills

*Rules one small business learned by running agents in front of real customers, packaged as files any coding agent can read. Private until each skill passes the gate. Last verified 2026-10-07.*

**Read this first:** a skill is prose. It instructs an agent; it does not run anything. Every skill here tells the agent to draft and show, never to apply. If your agent applies a draft anyway, that is your harness's permission setting, and this repository cannot fix it.

## What this is

A skill is one folder with a `SKILL.md` inside. The file has a short header the agent reads to decide when the skill applies, then the rules. Claude Code, Codex, Hermes, Pi and Omarchy's agent launcher all read skills from the same kind of folder, so one file works wherever the agent runs. These are the rules behind the agents described in the Lavelle notes, rewritten so a programmer can hand them to their own agent and build the same thing for a different business.

Every rule carries the incident that produced it, dated when the date is known, with the customer taken out. A rule with no incident under it is suspect, and the file says so.

## Skills in the box

| Skill | What it is for |
|---|---|
| [receptionist](receptionist/SKILL.md) | A phone receptionist that books on a real calendar for a trade business: intake, recognition, service area, cancellations, what it may never say. |
| [honest-tutor](honest-tutor/SKILL.md) | A tutor for a subject where sources matter and the student will go on to teach others: one idea at a time, say it back, never invent, say what the model cannot compute. |
| [second-model-brief](second-model-brief/SKILL.md) | How to brief a second AI model, read its memo back against the sources, and reconcile it before anyone acts. |
| [resale-identification](resale-identification/SKILL.md) | Identify used furniture and household goods from phone photos, say what they tend to sell for, draft the listing; photo versus in hand; never a value as fact. |

## Install

Clone the folder of the skill you want into your agent's skills directory. Claude Code reads `~/.claude/skills/<name>/SKILL.md`; the shared location most harnesses now read is `~/.agents/skills/<name>/SKILL.md`. Omarchy symlinks both.

```
git clone <this repository> ~/lavelle-skills
mkdir -p ~/.agents/skills
ln -s ~/lavelle-skills/receptionist ~/.agents/skills/receptionist
ln -s ~/lavelle-skills/honest-tutor ~/.agents/skills/honest-tutor
```

## The one test

Open your agent. Ask it: "Using the receptionist skill, draft the booking rules and the intake script for a fictional plumber in a fictional town. Show me the draft. Do not create, configure or deploy anything." Read what comes back against the skill. Then do the same on a second machine, or in the Claude app, where the skill is pasted into the conversation instead of installed.

Stop if the skill only works in one place, or if the agent builds instead of drafting.

## What is not here

No customer data, no phone numbers, no addresses, no system prompts of a live agent, no credentials. The scanner in `scripts/gate.sh` runs before every commit and blocks on any of those. A grep is not anonymity; a person reads every file before it goes public.

## Starting yours

1. Copy a skill folder and rename it.
2. Replace every rule with one you have an incident for. Delete the rest.
3. Run the one test above with a fictional customer.
4. The first thing that will go wrong: the agent will follow the rules in the draft and ignore them in the build. That is the harness, not the skill. Put the rule in code the moment it costs money.
