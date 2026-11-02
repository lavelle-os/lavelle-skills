# Lavelle skills

Nineteen rules files from a one-truck appliance repair shop in Alabama that runs on AI agents. Each one tells an agent how to do one job the way my shop does it, and most rules are there because something went wrong without them. I'm the owner, I don't write code, and these are what I learned.

A skill is plain text. It doesn't run anything. Every one tells the agent to draft and show you, never to act on its own.

## If you have never used GitHub, start here

GitHub is a website that stores files. The text you are reading is one of them, called README. You don't need an account to read or copy anything here, and clicking can't break anything. You can ignore every button I don't name below.

### Try a skill in a chat app (no account, about two minutes)

1. Scroll down to the table called [The skills](#the-skills) and click a skill's name, for example **receptionist**. Its page opens. The grey table at the top of that page (name, description, license) is a label for AI apps. That's normal.
2. Copy the whole page.
   - **On a computer:** at the top right of the box that holds the text, find the word **Raw**. Click the icon of two overlapping squares just to its right (its label is "Copy raw file"). Nothing on the page changes when it works. Don't use the same-looking icon next to the file name **SKILL.md** near the top. That one copies only the page's address.
   - **On a phone:** tap the three dots (**...**) on the same line as **Preview**, **Code** and **Blame**, then tap **Copy** under "Raw file content". Don't use the three dots at the very top of the page.
   - **If that doesn't work:** click **Raw**. A plain page of text opens. Select all and copy it (Ctrl+A, then Ctrl+C. On a Mac, Cmd+A, then Cmd+C).
3. Open ChatGPT, Claude or whatever chat app you use, start a new chat, and paste into the message box. It's long, and it starts with `---` and `name:`. That's normal. Some apps turn a long paste into an attached file, and that's fine too.
4. Go back to the skill's page and scroll down to **Try it**. After your paste, type the request shown there (leave off the > mark) and send. For the receptionist the request is: "Using these rules, draft the booking rules and the intake script for a made-up plumber. Show me the draft. Don't build anything."
5. Right under that request, the skill's page says what a good answer looks like.

To come back here, click **lavelle-skills** at the top left of any page (not **lavelle-os**), or use your browser's back button.

### Get every skill onto your computer (optional, not for phones)

You don't need this to use a skill in a chat app.

1. Go to the first page of this repository: https://github.com/lavelle-os/lavelle-skills
2. Above the list of folders, on the right, click the green **Code** button. Not the **Code** tab at the top left.
3. A box headed **Clone** opens. Ignore everything in it except the last line, **Download ZIP**, and click that.
4. A file named `lavelle-skills-main.zip` goes into your Downloads folder. On a Mac, double-click it. On Windows, right-click it, then click **Extract All**.
5. Each skill is a folder with one file inside, `SKILL.md`. It opens in Notepad or TextEdit as plain text with # and * marks. The folder named `scripts` is not a skill.

### Tell me what broke (needs a free GitHub account)

1. Click **Issues** at the top of the page, next to **Code**.
2. The page will say "No results matched your search." That only means nobody has written one yet.
3. Click the green **New issue** button on the right.
4. If you aren't signed in, GitHub shows "Sign in to GitHub" instead of a form. Click **Create an account** (under "New to GitHub?") and follow GitHub's steps. Then come back to **Issues** and click **New issue** again.
5. Type a short title, write what you did and what happened in the big box, and click the green button to post it.

Everything you post there is public, with your GitHub name on it. Leave out customer names, phone numbers and addresses.

## Set up your AI app first (if you have not)

Trying a page needs no setup. Before you use the pages for real, set up your AI app once. If you have never used an AI app, or have only ever typed into a plain chat, [set-up-your-ai](set-up-your-ai/SKILL.md) walks you through it: it asks five questions, writes the standing instructions that shape every chat, and tells you which box they go in. You do every click.

No AI app yet? Pick one and make a free account yourself, on its own website or phone app (chatgpt.com, claude.ai, grok.com or perplexity.ai), then come back.

1. Copy the whole [set-up-your-ai](set-up-your-ai/SKILL.md) page and paste it into a new chat in the app you want to set up (in Perplexity, the search box on its home page), the same way as in [Try a skill in a chat app](#try-a-skill-in-a-chat-app-no-account-about-two-minutes). A free plan should work, but the page is long, and nobody has tried it in a free ChatGPT, where OpenAI lists the input maximum as about 12 pages of text. Each app below has a shorter version of the page, with only that app's steps; paste that one instead if your app refuses the long one, or doesn't start by asking which app you use.
2. In the same message, under the paste, type this and send it: "Using these rules, help me set up my AI app. Ask me one question at a time, then show me what to paste and where."
3. It asks one question at a time, starting with your app and plan, and waits for each answer. That's normal. It never needs your password. If it asks for one, don't give it. Your app's own sign-in screen may ask for your password or a code; that goes only there, never into a chat.
4. At the end you have one block of text to copy, the name of the box it goes in, numbered steps for your app, and one question that proves it took.

If you only need the box, here is where each app keeps it, with a link to that app's shorter page, from each company's own help pages, last checked 2026-11-01. Buttons move, so check your app. If your screen is different, your screen wins.

- **ChatGPT** ([its page](set-up-your-ai/for-chatgpt.md)), every plan, on a computer: 1. Click your profile icon. 2. Click **Personalization** (if you see **Settings** instead, click **Settings**, then **Personalization**). 3. Turn on **Enable customization**. 4. Paste into **Custom Instructions**. 5. If a **Save** button shows, click it. On a phone, your profile icon is in the sidebar (how to open the sidebar: UNVERIFIED); it opens Settings, then **Personalization** or **Customize ChatGPT**, with the same switch and box.
- **Claude** ([its page](set-up-your-ai/for-claude.md)), every plan, on a computer: 1. Click your initials, lower left. 2. Click **Settings**. 3. Click **Your Claude**. 4. Paste under **Instructions**. In an older layout, step 3 is **Account** and the box is **Instructions for Claude**. On a phone, Settings opens from your initials or name in the left sidebar; the rest of the phone path is UNVERIFIED, so claude.ai in a computer's browser is surer.
- **Grok** ([its page](set-up-your-ai/for-grok.md)): the product page of xAI, the company that makes Grok, lists "Custom instructions", but no help page says where the box is (UNVERIFIED). Look in Settings (on grok.com: **Profile**, then **Settings**, per xAI's FAQ). If you find a box with that name, paste there. If not, paste your text as the first message of each chat. Keep it to your first name and what you do: the help pages of X, the social network that also offers Grok, ask you not to share personal data with Grok.
- **Perplexity** ([its page](set-up-your-ai/for-perplexity.md)), on the web: 1. Go to perplexity.ai/account/details, or click your avatar, the small picture or initial (bottom right corner; an older help page says bottom left), then **All Settings**. 2. Find the **Personalization** section. 3. Paste into **Custom instructions**. An older help page calls it **Introduce yourself**.
- **Gemini:** not checked for this page, so paste your text as the first message of each chat. For a Gemini project, use the Gemini entry on [ai-project-setup](ai-project-setup/SKILL.md).

After the box, set-up-your-ai hands you to [ai-project-setup](ai-project-setup/SKILL.md) for a project with its own rules, like a coach or a tutor. Most people only need the box, and maybe a project. A code session lets the AI change files on your computer; skip it unless you know you want that. For one, with Claude Code ([its page](set-up-your-ai/for-claude-code.md)), OpenAI's Codex or Grok Build (both on the [full page](set-up-your-ai/SKILL.md)), it explains each permission setting before you say yes to one, how to change the model, and how not to use up your plan on the biggest one.

Sources: chatgpt.com/pricing and help.openai.com/en/articles/8096356, 11899719 and 20001038; claude.com/pricing and support.claude.com/en/articles/8114491, 10185728 and 12111783; x.ai/grok, docs.x.ai/grok/faq and help.x.com/en/using-x/about-grok; perplexity.ai/pro and perplexity.ai/help-center/en/articles/10352993, 10352990 and 10354769. The set-up-your-ai page lists the rest.

## Try one in two minutes

**No terminal:** see [If you have never used GitHub, start here](#if-you-have-never-used-github-start-here) above. It walks through copying one skill into a chat app, click by click.

**For people who use Claude Code or OpenCode in a terminal. Everyone else can skip this.**

**With a coding agent:** this copies the repository once and links every skill into the folder Claude Code reads (`~/.claude/skills`) and the one OpenCode reads (`~/.agents/skills`). For any other agent, check where its documentation says skills go.

```
git clone https://github.com/lavelle-os/lavelle-skills ~/lavelle-skills
mkdir -p ~/.claude/skills ~/.agents/skills
for name in set-up-your-ai receptionist honest-tutor ai-project-setup second-model-brief resale-identification field-ticket starting-a-home-service-business business-license-research legal-research-memo parts-lookup part-pricing repair-or-replace warranty-and-callbacks bookkeeper contracts-and-policies truck-inventory supplier-order-and-tracking review-replies; do
  ln -s ~/lavelle-skills/$name ~/.claude/skills/$name
  ln -s ~/lavelle-skills/$name ~/.agents/skills/$name
done
```

Then ask: "Using the receptionist skill, draft the booking rules and the intake script for a fictional plumber. Show me the draft. Don't build anything."

## The skills

Every skill's page starts with a plain explanation: what it is, who it's for, the trade words it uses, what you need, what it does and won't do, and a request to try with what a good answer looks like. The rules the AI follows come after that.

| Skill | What it does |
|---|---|
| [set-up-your-ai](set-up-your-ai/SKILL.md) | Gets your AI app ready before any other page: writes its standing instructions, says which box they go in, and explains permissions and models for code sessions. |
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
- ai-project-setup, added October 16, had two runs on the Mac that night, then one run each on the Omarchy machine, under Claude Code and under OpenCode with a free model. All held.
- set-up-your-ai, added November 1, has had two runs under Claude with made-up people, plus a read by an AI reviewer playing someone who has never used an AI app. Both runs held. Nobody has pasted it into a real ChatGPT, Grok or Perplexity app yet.
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
