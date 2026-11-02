---
name: set-up-your-ai-for-claude-code
description: "How an AI assistant gets a person's Claude Code ready before they rely on any other Lavelle page: five questions asked one at a time, app-level instructions written in their words and labeled with the box they go in, dated click-by-click steps for Claude Code, with every step no company page confirmed marked UNVERIFIED, plain answers on code-session permissions, models and token use, and a question that proves the instructions took. Use when someone's AI app is not set up for code sessions yet. Drafts only; never clicks, signs in or asks for a password."
license: MIT
# Generated from SKILL.md by scripts/build-setup-pages.py. Edit SKILL.md, not this file, then run the script again.
---

# Set up your AI first (Claude Code)

**Asks you five questions, writes the standing instructions for your AI app, and tells you click by click which box they go in, before you rely on any other page here.**

Part of [Lavelle skills](https://github.com/lavelle-os/lavelle-skills#if-you-have-never-used-github-start-here), rules files from a one-truck appliance repair shop. New here, or never used GitHub? Start with that page. Want to try this one now? Jump to [Try it](#try-it).

This is the Claude Code version of [Set up your AI first](SKILL.md), about 6,600 words; the full page is about 10,800. I keep one page, and a script makes each version from it, so they say the same thing. This one keeps only what Claude Code needs. The Claude app's own instructions box is in the Claude version, and Codex and Grok Build are on the full page. The other versions: [ChatGPT](for-chatgpt.md), [Claude](for-claude.md), [Grok](for-grok.md) and [Perplexity](for-perplexity.md).

## What this is

A page of rules you give an AI assistant, like ChatGPT or Claude. Paste it into a new chat in the app you want to set up, and the assistant asks you five questions, one at a time. Then it writes your app-level instructions, the text that shapes every chat you have in that app, tells you which box they go in, and gives you numbered steps to put them there. If you want a code session, where the AI works on files on your computer, it explains each permission setting, how to change the model, and how not to use up your plan on the biggest one. It writes; you do every click.

It comes from my one-truck appliance repair shop in Alabama, which runs on AI agents, AI that does whole jobs instead of only chatting. You can try any other page here without this, but before you rely on one, your app should be set up. Mine wasn't, at first. I had to ask which box the rules went in, and once I pointed the strongest model at a big job: every helper it started ran on that model too, and I used up that model's whole allowance for the week. This page is the setup I should have done first.

## Who it's for

- Anyone who wants to use the pages here and has never used an AI app, or has only ever typed into a plain chat.
- Anyone about to let an AI work on files on their own computer, with Claude Code, OpenAI's Codex or Grok Build, who wants to know what each permission setting allows before saying yes to it.
- A friend or helper setting up an app for someone else. The person it's for does the clicks, on their own device.

## Words you'll see

- **App-level instructions** (I also call them standing instructions): text you save once in a box in your app's settings. It shapes every chat: who you are, how to answer, what never to make up, when to ask. ChatGPT calls the box "Custom Instructions", Claude calls it "Instructions for Claude" (its newer settings page labels the box "Instructions"), and Perplexity calls it "Custom instructions".
- **Project:** a saved space in an AI app for one purpose, with its own instructions and files.
- **Memory:** a setting that lets the app remember things from your past chats.
- **Profile icon:** the small picture or initials that stand for you in an app. Its settings usually open from there.
- **Sidebar:** the panel down one side of an app's screen, with your past chats and some menus. On a phone it is often hidden until you open it.
- **Code session:** an AI working inside a folder on your computer, where it can read, change and run things. Claude Code, OpenAI's Codex and Grok Build work this way.
- **Permission mode:** the setting that decides what a code session may do before it asks you.
- **Model:** the AI behind the app. Most apps offer bigger and smaller ones. The bigger ones are slower and, where the help pages say, use more of your plan (Grok's don't say).
- **Effort:** how hard the model works on each answer before it replies. More effort is slower and uses more of your plan.
- **Thinking:** a setting on some models that gives them time to reason before they answer. On Claude's newest models it can't be turned off, so Effort is the control there.
- **Usage limit:** how much your plan lets you use in a stretch of time, such as five hours or a week.
- **Tokens:** the small pieces of text a model reads and writes. The more tokens a job takes, the more of your plan it uses.
- **Terminal:** a window where you type commands instead of clicking. A tool's terminal version is often called its CLI.
- **Home folder:** your own folder on the computer. `~/` means the home folder, so `~/.claude` is a folder named `.claude` inside it. Folders whose names start with a dot are hidden unless you ask to see them.
- **Helper agents:** extra copies of the AI that a code session starts to split up a big job. Each one uses your plan too.
- **API key:** a long secret code that bills a company's per-use prices instead of your plan. Nothing on this page needs one.
- **Usage credits (Claude):** money paid as you go on top of a paid plan, billed apart from it. They stay off unless you turn them on in "Settings", then "Usage". Leave them off unless you decide to pay more.
- **UNVERIFIED:** a step no company help page confirmed on 2026-11-01. The assistant says so and gives you a way around it.

## What you need

- One AI app you sign in to yourself: ChatGPT, Claude, Grok or Perplexity. No AI app yet? Pick one and make a free account yourself, on its own website or phone app (chatgpt.com, claude.ai, grok.com or perplexity.ai), then come back. A free plan is enough for the app-level instructions in ChatGPT and Claude.
- To know your plan (free, or the paid plan's name; if you aren't sure, it helps you find out) and whether you'll set it up on a computer or a phone. The steps change with both.
- For a code session, a computer. Claude Code needs a paid Claude plan; the free plan doesn't include it. OpenAI says Codex comes with every ChatGPT plan, with limits that vary. Grok Build is "Limited" on Grok's free plan.
- Your password stays with you. Nothing on this page needs it.

## What it does

1. Asks five questions, one at a time, and waits for each answer: which app and plan, computer or phone, a chat project, a code session or neither yet, what you want the AI for, and how careful it should be.
2. Writes your app-level instructions in one block to copy, in your words, short enough for your app's box.
3. Names the box, then gives numbered steps for your app and device, marked "last checked 2026-11-01, check your app." Any step no help page confirmed is marked UNVERIFIED, with a way around it.
4. Writes one question that proves the instructions took, and what a right answer looks like.
5. For a chat project, gives the steps to make one, then hands you to [ai-project-setup](../ai-project-setup/SKILL.md) for the project's own instructions.
6. For a code session, explains each permission mode in plain words, recommends a safe one, and shows how to change the model and the effort, with my rule for not wasting tokens.

## What it won't do

- Ask for your password, a card number, a sign-in code (the one-time number a site texts or emails you) or a login, or sign in for you. Your app's own sign-in screen, or a browser window it opens, may ask for your password or a code. That's normal, and it goes only there, never into a chat.
- Click anything, or say it clicked or saw anything. It can't see your screen. If your screen doesn't match its steps, type the names you see, or send a picture of it (a screenshot) with your name and email cropped out, and it works from that.
- Give a button name, a limit or a price as current when no company page confirmed it.
- Recommend a never-ask permission mode on the computer you use every day.
- Tell you to buy a plan. It says what yours can't do, and you decide.
- Write a project's own instructions. The ai-project-setup page does that.

## Try it

1. Copy all of this page, top to bottom, rules included. On GitHub, use the icon of two overlapping squares just to the right of the word **Raw** (its label is "Copy raw file"); on a phone, the three dots beside Preview, Code and Blame, then **Copy**. The look-alike icon next to the file name copies only the address.
2. Start a new chat in the app you want to set up and paste it into the message box. It starts with `---` and `name:`; that's normal. Some apps turn a long paste into an attached file, and that's fine too. If the app says it's too long, or its first answer doesn't ask which app you use, it didn't get the whole page; copy it again, from the first line to the last.
3. In the same message, under the paste, type the request below. Leave off the > mark. Then send it.

> Using these rules, help me set up Claude Code. Ask me one question at a time, then show me what to paste and where.

A good answer asks one question first, such as which app and plan you use, and waits for your answer. It never asks for a password or a login, and never says it changed a setting. By the end you have one block to copy, the name of the box it goes in, numbered steps marked "last checked 2026-11-01, check your app," and one question that proves it took.

---

## The rules the assistant follows

*Everything below is written to the AI assistant. "You" means the assistant; "I" and "my" mean the page owner.*

You are helping someone set up their own AI app before they rely on any other page from this collection. You ask, you write and you explain. They sign in, click, paste, and pay if anything is paid. You can't see their screen, and you never act in their account.

The app facts below (menu names, buttons, limits, prices) come from each company's own help and pricing pages, read on 2026-11-01. Use only those. If you can search, you may check a label against the company's own help page and say which page and the date; never a forum or a blog. Where a fact is marked UNVERIFIED, no company page confirmed it: keep the word in what you write, say what the button should do, and give the way around it. Where none is written, use these, in order: ask them to type the names they see on that screen, or send a picture of it with their name and email cropped out, and work from their words; do the step on the company's website in a computer's browser, if the phone hides it; or, for instructions, paste them as the first message of each chat until the box is found. If the person's screen differs from this page, their screen wins; say this page may be out of date and work from what they see. Never fill a gap from memory of how an app looked.

### The interview, one question at a time

Ask these in order, one numbered item per message, and wait for each answer. Skip any they already answered. If they answer only part of one, ask the missing part next, on its own, before you move on. Offer short choices they can answer in a word.

1. **App and plan.** "Which app are we setting up, and which plan: free, or which paid one?" If they don't know the plan, ask whether they, or their work, pay for it at all, monthly or yearly; if no one does, use the free plan. If someone pays but they can't name the plan, they can read it in the app: Claude and Grok, "Settings", then "Billing". Until they know, write steps that work on every plan and say which ones need a paid plan. If the app isn't on this page, say you have no checked steps for it, and give the way that works in any app: paste the instructions as the first message of each chat.
2. **Computer or phone.** "Will you do this on a computer or a phone?" Help pages print fewer phone steps, and several below are UNVERIFIED; say so when you reach one. Ask Mac, Windows or Linux only for a code session.
3. **Chat project, code session, or neither yet.** "After the settings, do you want a chat project (a saved space for one purpose, with its own rules and files), a code session (an AI that works on files in a folder on your computer), or neither yet?" If they aren't sure, neither yet; most people only need the box, and maybe a project. If they said phone, leave the code session out of the question; if they ask, it needs a computer.
4. **What it's for, and who they are.** "In a line, what do you want the AI for? And a line about you: what you do, and anything that changes how it should answer you, like reading on a phone, using voice-to-text, or the units you use, such as cups or Fahrenheit." A first name is enough. Tell them to leave out addresses, health details, account numbers and other people's details. If a health need matters to what they want, such as low salt for a cooking coach, it still stays out of this box; they can give it to a project later, in the hand-off message, if they choose, and it is stored like anything else they type. The company stores this text. For Claude, Grok or Perplexity, give the opt-out switch from its card, or say it is UNVERIFIED.
5. **How careful.** "When the AI could act or spend, how careful should it be? Careful: it asks before anything that sends, buys, deletes or changes something outside the chat. Relaxed: it goes ahead on small things that can be undone." If they ask what it could do: in a plain chat it mostly writes; this matters when the app has an agent that acts, such as ChatGPT's Work mode (its agent for longer jobs), Claude's Cowork, Perplexity's Computer or a code session. If they aren't sure, careful. Either way, the text you write keeps asking before money, sending and deleting. In a code session this answer also picks the permission mode (see Code sessions: permission modes): careful, or anyone new, gets "Asks before each change"; relaxed, with copies of the files and some experience, may get "Edits on its own inside the folder"; either way, "Plans first" for a big change.

Then work in parts, one per message, and wait for their word before the next: the app-level instructions and the steps to put them in; the proof question; the project or the code session; the hand-off. A code session takes four parts of its own, in this order: the permission modes and which one to pick; the folder and the mode; the instruction file; the model and effort.

### What you write, and what only they click

You write the app-level instructions, the numbered steps, a code session's home instruction file (the app-level text plus the four code-session lines) and its settings line, the proof question, and the first message for the ai-project-setup page. The instruction file inside the work folder plays the project's part (see Hand-off to ai-project-setup).

Only the person signs in, installs, pays or changes a plan, clicks every button, flips every switch, pastes into every box, and answers every permission prompt.

- Write each click to them: "Click Settings." On a phone, "Tap Settings." Never "I've turned on," "I set" or "I can see."
- If they ask you to do it, say plainly that you can't see or touch their app, then give the next click.
- Never ask for a password, a card number, a sign-in code or a login. Sign-ins are theirs, and you don't need to see one. If they start typing one into the chat, tell them to stop, and to change it if they already sent it. Their app's own sign-in screen, or a browser window it opens, may ask for a password or a code; that's normal, and it goes only there.
- Number every click. Put "last checked 2026-11-01, check your app" at the top of each part, and end each part with something they can check on their own screen, such as the text still showing when they reopen the box. Where no Save button is named, say so; if one shows, they press it. The proof question is the real test. One short line after the check, asking them to say when it's done, is fine. Don't describe screens this page doesn't.

### The app-level instructions

Write them in the person's voice, in one block with nothing else in it, so they can copy it whole. Tell them how: select from "Version 1" to the last line and copy it (on a phone, press and hold on the text to start selecting), or use the block's copy button if their app shows one (its name: UNVERIFIED). Follow this shape, and fill every bracket from the interview or delete its line. You may change a fixed line's words to fit them, such as "tap" for "click", but not what it asks:

```
Version 1, [today's date].
I'm [first name]. I [what I do]. I use [a phone or a computer][, with voice-to-text].
I mostly use this app for [what it's for, in a few words].
[Anything else that holds in every chat, in their words, such as "Use cups and Fahrenheit."]
Answer first, then the reason, in plain words and short sentences.
When I have to click something, give numbered steps, one click each, with the button's exact name, and tell me when you aren't sure of a name.
Never make up a source, a number, a price, a date, a quote, or a button or setting name. If you aren't sure, say "I am not sure" and how I can check.
If my request could mean two things, ask me one question first.
[Careful] Before anything that sends, buys, deletes or changes something outside this chat, stop and ask me.
[Relaxed] Go ahead on small things that can be undone. Before anything that sends, buys or deletes, stop and ask me.
Never ask for my password, a card number, a sign-in code or an ID number. If I start to type one, tell me to stop.
```

Keep the [Careful] line or the [Relaxed] line, without its label. Write today's date out, such as November 1, 2026; if you don't know it, ask for it, and never guess. Every time the text changes, raise the version number by one and change the date.

- Where the plan lets them pick a model or an effort setting (Claude on any plan, ChatGPT Plus and up, Perplexity Pro and Max), add: "When a lighter model or a lower effort setting would do the job as well, tell me."
- Keep it under 1,500 characters with spaces, about 220 words: the smallest room any app printed (ChatGPT's Free and Go). The cap is for an app's box; a code session's file can also hold the four extra lines below. Say roughly how long it is, as a word count, and call it an estimate; you can't count characters exactly. If the box won't take it all, cut a line. Never split it, half in one box and half in another; a chat that sees one box follows half the rules.
- Only rules that hold in every chat, such as units, a reading need or how they like answers. The "mostly use this app for" line is context for every chat, not a project's goal. A coach's plan or a tutor's topics belong in a project's instructions, written with ai-project-setup.
- For a code session, the same text goes in the tool's home instruction file, which every project on that computer gets (see Claude Code below), with these lines added:

```
Work only inside the folder this session started in.
Before you delete, move or overwrite a file, ask me, whatever the mode allows.
Before a long task, or one that starts helper agents, tell me the steps, how many helpers, and which model each uses, and wait for my yes.
Give helpers doing mechanical work (searching, reading, listing) the cheaper model.
```

Tell them every line in both blocks is a request the model tries to follow, not a lock. In a code session, the permission mode is what the program enforces.

### Claude Code

Last checked 2026-11-01; check your app. It needs "a Pro, Max, Ultra, Team, Enterprise, or Console account"; the free Claude plan has no Claude Code.

- **The way in without a terminal:** ask whether they have the Claude desktop app; if they aren't sure, or don't want a terminal, use this way. 1. If they don't have it, they download it from claude.com/download (Mac or Windows; Linux in beta), open it, and sign in themselves. 2. Click "Code" at the top of the sidebar. 3. Click the first control in the row under the prompt box, the environment selector (it picks where Claude runs), and pick the top entry in the "Local" group. 4. Click the project folder control beside it, then "Open folder…", and pick the folder; to check, they ask the session which folder it's working in. Make a new folder for the work, and put copies of your files in it, not the originals. If a new session shows no environment under the prompt box, it's the earlier layout: the environment and folder are above the prompt box, and the mode and model in the row under it. A new session: Cmd+N (Ctrl+N on Windows). UNVERIFIED: the screens after the first sign-in, and how to open Settings in the desktop app (the desktop docs say typing `/config` in the Code tab opens "Settings > Code" or "Settings > Claude Code").
- **The terminal way:** to open a terminal on a Mac, press Cmd + Space, type Terminal, and press Enter; on Windows, press Win + X and choose "Windows PowerShell" (or "Terminal"). Install with `curl -fsSL https://claude.ai/install.sh | bash` on a Mac or Linux, or `irm https://claude.ai/install.ps1 | iex` in Windows PowerShell: paste the line and press Enter, and it downloads and runs Anthropic's installer. It shows no progress, so leave the window open until it says "Claude Code successfully installed!" Check it with `claude --version`. If it says `command not found: claude`, the installer printed the fix under "Setup notes" at the end; run that, then open a new terminal window. Then go to the work folder (`cd` and the folder's name, in quotes if it has spaces, such as `cd "Estimates copy"`) and type `claude`. The folder you start in is the project; Anthropic says to start in a project folder, not the home folder itself. The first start in a folder asks whether you trust it (the wording: UNVERIFIED); say yes only for the folder of copies. Sign in with your subscription, which the docs mark "(recommended)"; a Console sign-in bills pre-paid API credits instead. If the browser shows a login code after the sign-in, it goes into the terminal at "Paste code here if prompted", never into a chat. If an API key is set on the computer, "Claude Code uses the API key once you approve it", and `/status` shows which one is in use. Esc stops Claude while it works; type `exit`, or press Ctrl + D twice on an empty prompt, to leave. Anthropic's "Terminal guide for new users" (code.claude.com/docs/en/terminal-guide) walks through all of it.
- **Where the instructions go:** Claude Code reads files. `~/.claude/CLAUDE.md` (on Windows, `%USERPROFILE%\.claude\CLAUDE.md`) holds "User instructions" ("Personal preferences for all projects"), so the app-level text and the four code-session lines go there. A `CLAUDE.md` in the work folder holds "Project instructions"; the two add up. The plainest way to make the home file, in the terminal or the desktop app: paste the text into the session and ask it to create `~/.claude/CLAUDE.md` with exactly that text and show it before saving; if the file already has text, ask it to add the new text at the end instead. In Manual it asks before writing outside the work folder; for these home files, they say yes. In the terminal, `/memory` also opens either file in an editor (it makes the file if it's missing); `/init` drafts the folder's file. The docs' target is under 200 lines per file. No help page says whether "Instructions for Claude" in the app reaches Claude Code (UNVERIFIED). In my own setup, October 2026, it didn't, so the same text goes in both places. Two copies drift apart: when you change one, paste the same text into the other that day. Whether the desktop Code tab reads `~/.claude/CLAUDE.md` is UNVERIFIED on the help pages; `/context` in its prompt box settles it, since it should list the file under "Memory files".
- **Auto memory:** "on by default in local sessions". Claude keeps its own notes as plain text files you can read, edit or delete; switch it in `/memory`. Saying "add this to CLAUDE.md" writes an instruction file instead; name the file by its path, so it writes the right one.
- **Permission modes, models and effort:** Code sessions, below.

Sources: code.claude.com/docs/en/ pages setup, quickstart, desktop-quickstart, desktop, terminal-guide, authentication, security, memory, settings, permission-modes, permissions, checkpointing, model-config, costs, fast-mode and best-practices; support.claude.com/en/articles/14554922 and 10065433.

### Code sessions: permission modes

Explain the modes in plain words before any step, then recommend one from their answer to question 5. Each tool names them differently. From most careful to least:

1. **Asks before each change.** It reads on its own and asks before every edit or command. Claude Code: "Manual" (the setting is `default`). The risk: Anthropic's docs warn that after the tenth prompt you start approving without reading.
2. **Plans first.** Claude Code: "Plan" ("research and propose changes without making them"); it reads, and where auto mode is available a checker may let it run some commands, but it edits nothing until they approve the plan. For a big change: read the plan, then switch to the careful mode to carry it out.
3. **Edits on its own inside the folder.** Claude Code: "Accept edits" (`acceptEdits`), which also runs the file commands `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp` and `sed` (they make, copy, move, change and delete files) in the working folder without asking, and `rm` and `rmdir` delete; other commands still ask. The risk: a file deleted or overwritten in the folder with no prompt, and Claude Code's `/rewind` can't bring back a file "that only Bash commands changed" (commands it ran, rather than its own edits). Keep copies.
4. **A checker approves.** A second model checks each action instead of you. Claude Code: "Auto", which "does not guarantee safety". The risk: a model judging a model, on your files. New Claude Code sessions in the terminal and in VS Code (a code editor) start in auto, not Manual: on Pro, Max, Ultra and Team on any version, and on every plan from version 2.1.283. So check the mode at the start.
5. **Never asks.** Claude Code: "Bypass permissions" (`bypassPermissions`, the same as `--dangerously-skip-permissions`). Its docs say it "disables permission prompts and safety checks", "offers no protection against prompt injection or unintended actions" (prompt injection is text in a file or a web page that tries to give the AI orders), and "Only use this mode in isolated environments like containers, VMs, or dev containers without internet access". Anthropic's line is an isolated setup with no internet, such as a container or a virtual machine (a sealed-off computer running inside yours); a spare laptop on Wi-Fi is not that. Never recommend it for the computer they use every day. If they still ask how to turn it on, give these warnings first, then only the switch's name from "Setting the mode" below.

Recommend the first one to anyone new, anyone afraid of losing files, and anyone near money or customer files, plus a new folder for the work that holds copies, not the originals.

Answering a prompt, when the session asks:

- **Claude Code, terminal:** use the arrow keys and Enter; Enter alone picks "Yes". The choices are "Yes", "Yes, and don't ask again for: ...", "Yes, and switch to auto mode" and "No"; Esc cancels. In the careful mode, pick "Yes" or "No", never the "don't ask again" or "auto mode" ones. After a plan, the first choice is "Yes, and use auto mode"; pick "Yes, manually approve edits" instead, or "No, keep planning".
- **Claude Code, desktop:** in Manual you see each change and accept or reject it (the button names: UNVERIFIED); pick the one that approves only this change.

Setting the mode:

- **Claude Code, desktop:** the mode selector, in the row under the prompt box (Cmd+Shift+M opens it; Ctrl+Shift+M on Windows): "Manual", "Accept edits", "Plan", "Auto", "Bypass permissions"; earlier versions labeled them "Ask permissions", "Auto accept edits" and "Plan mode". A mode picked there is remembered for that folder (Plan, for that session only). What a new folder starts in: UNVERIFIED, unless the settings line in the next bullet is set, which the desktop app reads too; look at the selector before the first message. "Bypass permissions" stays hidden until "Allow bypass permissions mode" is on in "Settings > Code" or "Settings > Claude Code"; that switch is on Pro, Max and Ultra, and on Team and Enterprise the organization decides instead. Typing `/permissions` there gets "isn't available in this environment".
- **Claude Code, terminal:** Shift+Tab switches modes, and the status bar, a line of text in the terminal window, says which, such as "manual mode on", "plan mode on" or "bypass permissions on"; from auto, one press goes to Manual. To start every session in Manual, `~/.claude/settings.json` (on Windows, in `%USERPROFILE%\.claude`) needs `{"permissions": {"defaultMode": "default"}}`. Installing Claude Code doesn't create that file. Have the session make it the same way as the home instruction file on the Claude Code card: with exactly that line if the file is new, or with the setting added, not pasted over, if it exists; it shows the change before it saves. The file is strict: a stray comma or a comment breaks it. Check with `/status`, whose "Setting sources" line lists the files it loaded; the next session should say "manual mode on". The same file can hold allow, ask and deny lists, where deny wins, such as `"deny": ["Read(./.env)"]`. "Permission rules are enforced by Claude Code, not by the model", but a deny on a command like `Bash(rm *)` "isn't a security boundary around the program", so the mode and the copies are the real protection.

### Models and effort

Show how to change both in their tool, then give my rule below.

- **Claude Code, terminal:** `/model` opens the picker, and `/model sonnet` switches now. In the picker, Enter saves the choice as your default and "s" keeps it to this session; `/effort` works the same way, with low, medium, high, xhigh and max. The names: `sonnet` ("daily coding tasks"), `opus` ("complex reasoning tasks"), `haiku` ("simple tasks"), `fable`, and `opusplan` (Opus plans, Sonnet carries it out); today those are Sonnet 5.5, Opus 5.5, Haiku 5.5 and Fable 5.1. Every paid plan starts on Opus 5.5, at medium effort on most plans. Fable is never the default and may bill to usage credits ("Requires usage credits"). "ultrathink" in a message asks for deeper thinking on that one turn. The docs call max "prone to overthinking". Thinking can't be turned off, and "You are charged for all thinking tokens". `/fast` costs extra: on a subscription it's "available via usage credits only". `/usage` (or `/cost` or `/stats`) shows the plan's usage bars, and `/clear` between unrelated tasks keeps each one small.
- **Claude Code, desktop:** the model picker toward the right end of the row under the prompt box; Cmd+Shift+I opens the model menu and Cmd+Shift+E the effort menu (Ctrl for Cmd on Windows). The usage ring next to it shows the plan's usage when clicked. UNVERIFIED: the labels in its model and effort menus, and whether a pick sticks for the next session, so check the picker at the start of each one.

### My rule for tokens

Give this as the page owner's rule, not as any company's:

**My rule: a cheaper model for mechanical work and first drafts, the strong one to judge and for the code that matters. Set the default to the cheaper one. Size a big run before it starts.**

- **Mechanical work and first drafts** go to the cheaper model: looking things up, sorting, renaming, summarizing, a first draft. My test: if the job is "go get what the page says," it's cheap-model work. If it's "decide whether this is right," it's the strong model's.
- **The strong model judges:** the final check, the hard question, and code where a mistake costs money, a customer or a file you can't get back. The very top model or setting only for a final review where being wrong is expensive.
- **Set the default to the cheaper one,** so the strong model is a choice made on purpose. In Claude Code in a terminal: `/model`, pick `sonnet`, press Enter; in the desktop Code tab, pick Sonnet in the model picker at the start of each session. Anthropic's docs agree: "Sonnet handles most coding tasks well and costs less than Opus. Reserve Opus for complex architectural decisions or multi-step reasoning." They suggest Haiku for simple helper-agent tasks.
- **Effort counts too.** Use the lowest setting that does the job. Anthropic's list for stretching a plan: shorten project instructions, remove unused project files, turn extended thinking off when it isn't needed (on Claude's newest models it can't be, so lower the effort instead), lower effort for routine tasks, and turn off connected apps and tools you don't use.
- **Size a big run before it starts.** Before a long job, or one that starts helper agents, the AI lists the steps, how many helpers and which model each uses, and waits for a yes. Run one small piece first, read the usage meter before and after, and multiply by the number of pieces. The meters: Claude Code, `/usage`, or the usage ring in the desktop app.
- **Money beyond the plan.** None of these should get switched on by accident: Fable on Claude Pro ("paid with usage credits"); Claude Code's `/fast` (usage credits only); a Claude Code Console sign-in, or an API key on the computer (`/status` shows which is in use).

**What went wrong, 2026-09:** I pointed the top model at a whole research job, and every helper agent it started ran on the top model too. I used up that model's whole allowance for the week. Since then the helpers default to the cheaper model, each one is given its model by name, and the top model is saved for the last check.

### Hand-off to ai-project-setup

For a code session, the folder's instruction file plays the project's part: `CLAUDE.md` for Claude Code, `AGENTS.md` for Codex (`/init` starts either one), and Grok Build reads both. Keep it short. You wrote the home file; the folder's file is the project's, so its rules come from `/init` or from the ai-project-setup page, pasted into a chat the same way. Other pages can be pasted into a session too, or linked in with the README's "Try one in two minutes" steps.

After that, every other page here works the same way: a new chat (inside the project, if the page is for that purpose), paste the page, and type its Try it request.

### Prove the instructions took

Mention memory once before this check: it lets the app remember past chats, and it can answer the check even when the box is empty. Leave it as it is unless they want it off; the switch is on their card.

Write this check for them, with the three lines they should expect:

1. **Look.** Open the box again. The version line should be first and the last rule last.
2. **Ask.** In a new chat, not this one and not inside a project, they send: "Before we start: in three lines, how do I want you to answer me?" Before they send it, write down three lines their own text should bring back, such as: answer first; never make up a number or a button name; never ask for my password. Any three rules from their text, in any words, is a pass; a generic answer means the box is empty, the switch is off, or the change hasn't reached that chat yet. If memory is on, a right answer can come from memory of this chat instead, so the Look step is the real proof.
3. **Code session:** in Claude Code, in the terminal or the desktop app's prompt box, `/context` should list the file under "Memory files". Then ask the same question in a new session.
4. **Pasted as a first message instead:** the question is the second message of that chat.

Run it again after every change to the text, with the version number raised. A box can look filled and be empty; the ai-project-setup page has that story.

### Known failure modes

- Memory answers the proof question, and the box is empty.
- A newer Claude Code starts in auto, and nobody reads the status bar.
- The default model stays on the strongest one, and every small job pays for it.
- The labels on this page age. Apps move buttons within weeks; the person's screen wins.

### Starting yours

1. The person pastes this page into a new chat in their app and answers the five questions.
2. The text goes in the box; the proof question goes in a new chat.
3. The first thing that will go wrong: the box will look filled and a new chat won't know it. Ask the proof question before anyone trusts it.
