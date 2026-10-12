# Lavelle skills

*Rules one small business learned by running agents in front of real customers, packaged as files any coding agent can read. Public since 2026-10-11: each skill passed the gate and a run against a model before the flip, and the table says what was run on each. A skill that has not been tested is a draft with a header on it.*

**Read this first:** a skill is prose. It instructs an agent; it does not run anything. Every skill here tells the agent to draft and show, never to apply. If your agent applies a draft anyway, that is your harness's permission setting, and this repository cannot fix it.

## What this is

A skill is one folder with a `SKILL.md` inside. The file has a short header the agent reads to decide when the skill applies, then the rules. The Agent Skills spec defines the file, not where it lives, so check your agent's own documentation for where it looks; the Install section says where the three agents we know of look. These are the rules behind the agents described in the Lavelle notes, rewritten so a programmer can hand them to their own agent and build the same thing for a different business.

Every rule carries the incident that produced it, dated when the date is known, with the customer taken out. A rule with no incident under it is suspect, and the file says so.

## Skills in the box

| Skill | What it is for | Last tested |
|---|---|---|
| [receptionist](receptionist/SKILL.md) | A phone receptionist that books on a real calendar for a trade business: intake, recognition, service area, cancellations, what it may never say. | 2026-10-07, twice (once pasted into the Claude app, once from disk); 2026-10-11, Sonnet from disk, fictional plumber: PASS; intake order and after-hours gap logged; 2026-10-12, Opus 5.5 from disk on Omarchy in a VM, cloned from this public repository: PASS, loaded from the VM's own skills folder |
| [honest-tutor](honest-tutor/SKILL.md) | A tutor for a subject where sources matter and the student will go on to teach others: one idea at a time, say it back, never invent, say what the model cannot compute. | 2026-10-11, Sonnet from disk, one dryer lesson: PASS; trigger widened to teaching directly |
| [second-model-brief](second-model-brief/SKILL.md) | How to brief a second AI model, read its memo back against the sources, and reconcile it before anyone acts. | 2026-10-11, Sonnet from disk, a license question for a fictional club: PASS; "reconciliation first" reworded |
| [resale-identification](resale-identification/SKILL.md) | Identify used furniture and household goods from phone photos, say what they tend to sell for, draft the listing; photo versus in hand; never a value as fact. | 2026-10-11, Sonnet from disk, a dresser described in words only: PASS, no value stated as fact; trigger widened to descriptions |
| [field-ticket](field-ticket/SKILL.md) | Turn a technician's spoken findings into the ticket the customer reads: the visible write-up, parts lines that say only what the part is, prices the technician owns. | 2026-10-11, Sonnet from disk, a dictated washer ticket: PASS; the price rule now states its numbers |
| [starting-a-home-service-business](starting-a-home-service-business/SKILL.md) | The eleven steps for a one-person home-service business, in order, each with a "done when" and the line between what an agent does and what the owner must do. | 2026-10-11, Sonnet from disk, a fictional handyman in a fictional state: PASS; "whole plan at once" line clarified |
| [business-license-research](business-license-research/SKILL.md) | Research every license, registration, tax account and insurance requirement for a given state, county or parish, and city, from official sources only, as a checklist the owner acts on after a second read. | 2026-10-09, twice (fictional parish held; real city, web on, nine CONFIRMED); 2026-10-11, Sonnet from disk, fictional state, no web: PASS, every row UNVERIFIED, nothing invented |
| [legal-research-memo](legal-research-memo/SKILL.md) | First-pass research for a lawyer, or for an owner about to see one: primary sources on free official sites, operative words quoted, every claim FOUND BY TOOL, NOT YET CHECKED or UNVERIFIED, a memo a person checks in under a minute, never advice. | 2026-10-11, Sonnet from disk, fictional state, no web: PASS, nothing invented, every claim UNVERIFIED, no yes-or-no given; 2026-10-12, Opus 5.5 from disk on Omarchy in a VM, no web: PASS, one row with all seven cells, no claim about the law |

## Install

The Agent Skills spec defines the file, not where it lives. Claude Code reads `~/.claude/skills`; Codex reads `~/.agents/skills`; OpenCode reads both. Omarchy's manual says its skill is configured in OpenCode and Claude Code through `~/.claude/skills` (AI page, opened 2026-10-11). Link these there. Run on Omarchy 4.0.4 in a virtual machine on 2026-10-12: the Claude Code that Omarchy installs (2.1.296) read the box from `~/.claude/skills` and both skills tried held; the entry in TEST-LOG.md has what the machine needed first.

Paste this into a terminal. It copies the repository once and links all eight skill folders into both skills folders, so it works for any of the three agents.

```
git clone https://github.com/lavelle-os/lavelle-skills ~/lavelle-skills
mkdir -p ~/.claude/skills ~/.agents/skills
for name in receptionist honest-tutor second-model-brief resale-identification field-ticket starting-a-home-service-business business-license-research legal-research-memo; do
  ln -s ~/lavelle-skills/$name ~/.claude/skills/$name
  ln -s ~/lavelle-skills/$name ~/.agents/skills/$name
done
```

On Windows the links need Git Bash or WSL, and symlinks need Developer Mode turned on. Copying the folders into the skills folder works everywhere.

## The one test

Open your agent. Ask it: "Using the receptionist skill, draft the booking rules and the intake script for a fictional plumber in a fictional town. Show me the draft. Do not create, configure or deploy anything." Read what comes back against the skill. Then do the same on a second machine, or in the Claude app, where a skill can be pasted into the conversation or added through the app's own skills setting instead of installed from disk. As of 2026-10-12, the receptionist and the legal memo have run from disk on three machines (a Mac, an Ubuntu server, an Omarchy virtual machine), and the receptionist also in the Claude app by paste. The other six have run only from disk on one machine, so their second-machine step is still owed.

Stop if the skill only works in one place, or if the agent builds instead of drafting.

## What is not here

No customer data, no phone numbers, no addresses, no system prompts of a live agent, no credentials. `scripts/gate.sh` is a script the owner runs by hand before each commit. No hook ships with this repository, so cloning it does not run the script for you. It checks the staged files for phone-number shapes, street addresses, key shapes and roadmap words, and for a list of private names that is not published. A grep is not anonymity; a person reads every file before it goes public.

## License

MIT, in `LICENSE`. The copyright holder is The Morriss Group LLC, as the `LICENSE` file says. The license covers these files as documentation. It does not warrant the accuracy of any rule, and it grants no rights in any name.

## Starting yours

1. Copy a skill folder and rename it.
2. Replace every rule with one you have an incident for. Delete the rest.
3. Run the one test above with a fictional customer.
4. The first thing that will go wrong: the agent will follow the rules in the draft and ignore them in the build. That is the harness, not the skill. Put the rule in code the moment it costs money.
