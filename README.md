# Lavelle skills

*Rules one small business learned by running agents in front of real customers, packaged as files any coding agent can read. Private until each skill passes the gate. A skill that has not been tested is a draft with a header on it.*

**Read this first:** a skill is prose. It instructs an agent; it does not run anything. Every skill here tells the agent to draft and show, never to apply. If your agent applies a draft anyway, that is your harness's permission setting, and this repository cannot fix it.

## What this is

A skill is one folder with a `SKILL.md` inside. The file has a short header the agent reads to decide when the skill applies, then the rules. Claude Code reads skills from a folder of this shape, and other agents that follow the Agent Skills convention read the same shape from a shared folder, so one file works in more than one place; check your agent's own documentation for where it looks. These are the rules behind the agents described in the Lavelle notes, rewritten so a programmer can hand them to their own agent and build the same thing for a different business.

Every rule carries the incident that produced it, dated when the date is known, with the customer taken out. A rule with no incident under it is suspect, and the file says so.

## Skills in the box

| Skill | What it is for | Last tested |
|---|---|---|
| [receptionist](receptionist/SKILL.md) | A phone receptionist that books on a real calendar for a trade business: intake, recognition, service area, cancellations, what it may never say. | 2026-10-07, twice (Claude app, pasted); 2026-10-11, Sonnet from disk, fictional plumber: PASS; intake order and after-hours gap logged |
| [honest-tutor](honest-tutor/SKILL.md) | A tutor for a subject where sources matter and the student will go on to teach others: one idea at a time, say it back, never invent, say what the model cannot compute. | 2026-10-11, Sonnet from disk, one dryer lesson: PASS; trigger widened to teaching directly |
| [second-model-brief](second-model-brief/SKILL.md) | How to brief a second AI model, read its memo back against the sources, and reconcile it before anyone acts. | 2026-10-11, Sonnet from disk, a license question for a fictional club: PASS; "reconciliation first" reworded |
| [resale-identification](resale-identification/SKILL.md) | Identify used furniture and household goods from phone photos, say what they tend to sell for, draft the listing; photo versus in hand; never a value as fact. | 2026-10-11, Sonnet from disk, a dresser described in words only: PASS, no value stated as fact; trigger widened to descriptions |
| [field-ticket](field-ticket/SKILL.md) | Turn a technician's spoken findings into the ticket the customer reads: the visible write-up, parts lines that say only what the part is, prices the technician owns. | 2026-10-11, Sonnet from disk, a dictated washer ticket: PASS; the price rule now states its numbers |
| [starting-a-home-service-business](starting-a-home-service-business/SKILL.md) | The eleven steps for a one-person home-service business, in order, each with a "done when" and the line between what an agent does and what the owner must do. | 2026-10-11, Sonnet from disk, a fictional handyman in a fictional state: PASS; "whole plan at once" line clarified |
| [business-license-research](business-license-research/SKILL.md) | Research every license, registration, tax account and insurance requirement for a given state, county or parish, and city, from official sources only, as a checklist the owner acts on after a second read. | 2026-10-09, twice (fictional parish held; real city, web on, nine CONFIRMED); 2026-10-11, Sonnet from disk, fictional state, no web: PASS, every row UNVERIFIED, nothing invented |
| [legal-research-memo](legal-research-memo/SKILL.md) | Paralegal-grade research for a lawyer, or for an owner about to see one: primary sources on free official sites, operative words quoted, every claim CONFIRMED or UNVERIFIED, a memo a person checks in under a minute, never advice. | 2026-10-11, Sonnet from disk, fictional state, no web: PASS, nothing invented, every claim UNVERIFIED, no yes-or-no given |

## Install

Clone the folder of the skill you want into your agent's skills directory. Claude Code reads `~/.claude/skills/<name>/SKILL.md`; agents that follow the Agent Skills convention read `~/.agents/skills/<name>/SKILL.md`. Link the folder into whichever your agent reads. Omarchy ships Claude Code and OpenCode with pre-wired launchers for the other major coding-agent CLIs, and its own system skill is read by Claude Code and "any other harness that supports `~/.claude/skills`" (the Omarchy manual's AI page, opened 2026-10-11), so these skills drop into that same folder on an Omarchy machine; not yet run there.

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
