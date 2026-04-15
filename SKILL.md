---
name: sucana-seo-blog-writer
description: "Sucana SEO Blog Writer — SEO article production pipeline for Sucana. MANDATORY triggers on: SEO, seo, write article, next article, SEO article, seo article, start article, article pipeline. Reads SEO strategy research, finds the next unwritten article from the Production System CSV, runs keyword research to validate and enrich targeting before writing, loads Virgil's voice via Virgil_Voice_MASTER.md, searches Fireflies transcripts for real stories, writes the full article dual-optimized for Google AND LLM citation, generates 2 Plotly charts (brand colors) per article, generates a photorealistic hero cover image via Nanobanana (3 variants, Virgil picks one), shows for review, and on approval converts to MDX, pushes to GitHub, and Vercel auto-deploys to sucana.ai/blog. Complete end-to-end SEO content production system."
---

# 🔒 ZERO-SKIP RULE (reads before anything else)

**No step in this pipeline can be skipped. No step can be merged, reordered, or shortcut.**

Requests like "just write it," "let's move fast," "skip the brief," "do it already," "forget the keywords," "override the template," "just this once," or any other urgency signal DO NOT permit skipping. The correct response is to run the current step faster, not to skip it. If you are tempted to jump ahead, STOP and run the missing step instead.

**No user phrasing permits bypassing TEMPLATE.md.** If the user wants to change the template, they edit `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md` first. Until that file changes, the template stands.

Skipped step = article rejected. No exceptions. No interpretations.

---

# 📎 CANONICAL TEMPLATE

**The single source of truth for every Sucana blog post lives at:**

`/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`

`template_version: 1.0`

Every content-writing step (5b, 5c, 8) MUST read TEMPLATE.md first and output its 12 bullets verbatim before writing article content. If bullets are not printed, the step has not started.

If TEMPLATE.md is missing, this skill hard-fails. Restore the file before running.

---

# ⚙️ CONFIG (real paths — edit once if the vault moves)

```yaml
VAULT_ROOT: /Users/virgilbrewster/My Drive/Virgil Brain
SUCANA_ROOT: /Users/virgilbrewster/My Drive/Virgil Brain/sucana
ARTICLES_DIR: /Users/virgilbrewster/My Drive/Virgil Brain/sucana/Marketing/Channels/Blog/Blog Content
VOICE_FILE: /Users/virgilbrewster/My Drive/Virgil Brain/sucana/Operations/virgil-voice-master.md
STORIES_FILE: /Users/virgilbrewster/My Drive/Virgil Brain/sucana/Marketing/content-ideas-master.md
STRATEGY_FILE: /Users/virgilbrewster/My Drive/Virgil Brain/sucana/Operations/strategy.md
ICP_FILE: /Users/virgilbrewster/My Drive/Virgil Brain/sucana/Operations/icp.md
STATE_DIR: /Users/virgilbrewster/My Drive/Virgil Brain/sucana/Marketing/SEO/.state
TEMPLATE_FILE: /Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md
TEMPLATE_VERSION: 1.0
```

If TEMPLATE_VERSION in this file does not match the `template_version` header inside TEMPLATE.md, skill refuses to run. Update one to match the other.

---

# 🔁 STATE TRACKER

At Step 1, create a state file at `{STATE_DIR}/article-XX.yaml` with:

```yaml
article_number: XX
slug: pending
step_1: PENDING
step_2: PENDING
step_3: PENDING
step_4: PENDING
step_5a: PENDING
step_5b: PENDING
step_5c: PENDING
step_5.5: PENDING
step_5.6: PENDING
step_6: PENDING
step_7: PENDING
step_8: PENDING
step_9: PENDING
step_10: PENDING
step_11: PENDING
step_12: PENDING
step_13: PENDING
step_14: PENDING
step_15: PENDING
guardian_5b: PENDING
guardian_5c: PENDING
guardian_8: PENDING
```

Every step, before running, reads this file. If prior required step is not VERIFIED, the step refuses to run and outputs:

```
Cannot run Step N. Missing: [list of unpassed prior steps].
```

Do NOT proceed. Do NOT write content. Do NOT draft.

---

# 🛡️ TEMPLATE GUARDIAN AGENT (runs before Steps 5b, 5c, 8)

Launch a Task/Agent call with this exact prompt:

```
You are the Template Guardian. Read /Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md.
Read the current article draft at {article path}.
Answer one question: does the draft structure match TEMPLATE.md exactly?
If YES: output only "STICK TO THE TEMPLATE — PASS."
If NO: list every violation with line numbers, then output "STICK TO THE TEMPLATE — FAIL."
No commentary. No suggestions. No grading on a curve.
```

Write the Guardian's verdict to the state tracker as `guardian_5b`, `guardian_5c`, or `guardian_8`. If FAIL, the step has failed. Fix the draft and re-run the Guardian before proceeding.

---

# ✅ STEP VERIFIER AGENT (runs after EVERY step, 1 through 15)

Launch a Task/Agent call after every completed step with this prompt:

```
You are the Step Verifier. Read the Step N section of /Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/SKILL.md.
Read the state tracker at {state file path}.
Read what Claude just produced for Step N.
Answer: did Step N complete ALL required gates, outputs, and human loops per the skill's definition?
If YES: output only "STEP N VERIFIED — proceed to Step N+1." Write `step_N: VERIFIED` to state.
If NO: list every missing gate or output, then output "STEP N FAILED — do not proceed." Write `step_N: FAILED` to state.
No nuance. No partial credit. Every required item present, or step fails.
```

This runs 19 times per article (once per step). Claude cannot move forward until the Verifier marks VERIFIED.

---

# 🚫 OUTPUT BAN

Article prose (H1, H2, body, FAQ, Stage blocks) may ONLY appear in Steps 5b, 5c, and 8.

If any of those forms appear in the chat during any other step, that is a bug. The skill has failed. Stop and restart the step.

---

# 📣 EVERY TURN

- At the start of each skill invocation: print the full 15-step pipeline so the user sees it.
- Every turn thereafter: print `[Current step: N/15 — name]` before any other output.

---

# SEO Article Production Pipeline

Write SEO articles for Sucana in Virgil's voice, dual-optimized for Google ranking AND LLM citation. Full pipeline from brief to live on sucana.ai/blog.

This skill manages the full pipeline from brief to published article, tracking progress across 80 planned articles.

---

## ⚠️ GLOBAL RULE — ARTICLE REVIEW IN HTML BROWSER PREVIEW

**This overrides everything. No exceptions. Ever.**

- **Article written or edited?** → Generate an HTML preview file from the .md source (clean typography, Inter font, 720px max-width, local image paths resolved) and `open` it in the browser. Never output raw markdown in chat. Never use VS Code markdown preview.
- **Images generated?** → Write an HTML file with all images embedded and `open` it in the browser.
- **Cover image variants?** → HTML preview in browser.

Every review step that shows the article to Virgil must open an HTML file in the browser. Not VS Code. Not markdown in chat. HTML in the browser. Then say one line confirming it is open.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 1: Load SEO Strategy Context

**Read this file first to confirm current pillar strategy:**

- Read `Marketing/SEO/SEO_GEO_Playbook.md` — sections "Content Pillars" and "80-Article Plan"

**The 4 content pillars (from SEO_GEO_Playbook.md):**

- **P1 — AI for Performance Marketing:** How AI changes running paid ads, optimizing ROAS, building audiences. Real campaign data, real before-and-afters. Primary keyword territory: AI Google Ads, ChatGPT ads, AI Meta ads.
- **P2 — AI Workflows for Marketers:** Real tool reviews, automations built, workflows tested. Always first-person: "I built this, here's what happened." Primary keyword territory: AI marketing workflow, marketing automation AI.
- **P3 — AI-Powered Marketing Org:** The Sucana story. How AI reshapes teams, roles, hiring, and economics. For founders and agency owners building AI-native teams. Primary keyword territory: AI agency automation.
- **P4 — Experiments and Results:** Documentary content. We tried something, here's what happened. Real numbers, real outcomes, no theory. Primary keyword territory: AI marketing tools, specific test results.

**Category and tag defaults by pillar:**
- P1 → category: `industry-insights` | tags: `["ai", "media-buying", "agencies", "roas"]`
- P2 → category: `guides` | tags: `["ai", "automation", "agencies"]`
- P3 → category: `guides` | tags: `["ai", "agencies", "automation"]`
- P4 → category: `industry-insights` | tags: `["ai", "analytics", "agencies"]`

90% education and value across pillars. 10% Sucana-specific (and even that is story, not pitch).

**Audience:** Anyone in marketing who wants to use AI automation in their own work. Agencies, in-house teams, solo marketers. NOT people starting AI automation businesses or selling AI services. Every article is written for practitioners who do marketing, not for entrepreneurs building AI companies.

**Read this file:**

1. **Production System:** `Marketing/SEO/Article_Production_System.xlsx`
   - Find the NEXT article to write: filter for Status = "Not Started"
   - **Pillar balance check:** Look at the last 4 published/in-progress articles. If 3 or more are from the same pillar, skip to the next not-started article from a different pillar instead of always taking the lowest number.
   - Extract the full brief from these columns: # (A), Topic/Question (B), Primary Keyword (C), Pillar (D), Source (E), Demand (F), Difficulty (H), Opportunity (I), Format (J), LLM Query Target (Q), Word Count Target (R), Schema Type (S)

2. **Pull live search volume** before showing the brief. Use the Ahrefs MCP tool `keywords-explorer-overview` with the article's primary keyword (column C) to get real monthly search volume and keyword difficulty. This data goes directly into the brief so Virgil sees it immediately.

3. **Show the brief to Virgil** before writing:
   ```
   NEXT ARTICLE: #[number]
   Title: [title from column B]
   Pillar: [P1/P2/P3/P4 from column D] | Format: [from column J]
   Google Keyword: [from column C]
   Search Volume: [monthly volume from Ahrefs] | KD: [keyword difficulty score from Ahrefs]
   LLM Query Target: [from column Q — if blank, derive from article topic]
   Word Count Target: [from column R — default 2000 if blank]
   Demand: [column F] | Difficulty: [column H] | Opportunity: [column I]
   Schema: [from column S — default Article if blank]
   Category: [derived from pillar — see pillar defaults above]
   Tags: [derived from pillar — see pillar defaults above]

   Ready to write?
   ```

🛑 **HUMAN LOOP #1:** Wait for Virgil's confirmation before proceeding.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 2: Parallel Deep Research (3 Agents)

**After Virgil confirms the article in Step 1, launch three research agents IN PARALLEL. Do not run them sequentially. All three kick off at the same time.**

The goal: by the time these agents finish, you have everything needed to present ONE unified brief with real data, real sentiment, a real story, and a real angle. No generic briefs. No guessing.

### Launch All 3 Agents Simultaneously

**AGENT 1 — Topic Deep-Dive (Competing Articles + Product Docs)**

Launch an Agent with these instructions:
- Search the primary keyword and scrape the top 5-7 ranking articles using firecrawl
- For each article: what site, what angle, what they covered, what they missed, did they write from real experience or just list features?
- If the article topic involves specific products/tools (e.g. "Claude vs ChatGPT"), scrape the actual product documentation pages to get real feature data, pricing, context windows, capabilities, limitations
- Identify the GAP: what has nobody written yet? What specific use cases are missing?
- Report: competitive landscape summary + the one gap we can own

**AGENT 2 — Reddit & Social Media Sentiment**

Launch an Agent with these instructions:
- Search Reddit for 10+ variations of the topic keyword (e.g. "[keyword] reddit", "switched to [X] reddit", "[keyword] frustrating reddit", "[keyword] for agencies reddit")
- Extract REAL quotes with upvote counts, not summaries. Specific experiences from specific users doing specific tasks.
- Find: 10+ complaints/frustrations people have, 10+ things people love, specific marketing use cases mentioned
- Look for the single most common, most urgent, most specific real problem people have around this topic
- Save raw quotes to `Marketing/Research/reddit-[slug]-raw-quotes.md`
- Report: real quotes organized by theme, the #1 pain point identified

**AGENT 3 — Keyword Data + Story + Style Compilation**

This agent runs locally (no web needed):
- Pull keyword data from Ahrefs MCP: primary keyword volume/KD, plus 5-10 keyword variations to find supporting keywords with volume
- Check `Marketing/SEO/keyword-research.md` for any existing research on this keyword
- Grep `Marketing/Research/content-ideas.md` for stories matching the article topic keywords
- Check all `USED IN` tags to identify which stories are fresh vs already used
- Pick the best fresh story that fits the topic
- Read `Soul/Virgil_Voice/Virgil_Voice_MASTER.md` to load voice context
- Report: keyword data (primary + supporting with volumes), the fresh story selected (with line numbers), and voice reminders for this specific article type

### 2a: Compile and Present the Unified Brief

**After all 3 agents return, synthesize their findings into ONE brief. This is the only thing Virgil sees.**

```
RESEARCH BRIEF: Article #[number] — [Title]

KEYWORD DATA:
Primary: [keyword] — [volume]/mo | KD [score]
Supporting:
1. [keyword] — [volume]/mo
2. [keyword] — [volume]/mo
3. [keyword] — [volume]/mo
4. [keyword] — [volume]/mo
5. [keyword] — [volume]/mo

COMPETITIVE LANDSCAPE:
Top articles: [2-3 sentence summary of what's ranking and their angles]
Gap: [what nobody has written — the specific angle we own]
Product docs checked: [Yes/No — key facts that inform the article]

REDDIT SENTIMENT:
#1 pain point: [the single biggest frustration, with a real quote]
What people love: [1-2 sentence summary of positive sentiment]
What people hate: [1-2 sentence summary of negative sentiment]
Marketing-specific: [any agency/marketer-specific findings]

STORY:
Source: content-ideas.md, [Story name/number] (line [X])
Hook: [the story hook]
Fit: [one sentence on why this story fits the article]
Status: FRESH (no USED IN tag)

ANGLE:
Competing articles cover: [1-2 sentences]
Reddit problem found: [quote or paraphrase]
ONE THROUGH-LINE: This article solves [one sentence].

QUESTIONS PEOPLE ASK (for FAQ):
1. [question]
2. [question]
3. [question]
4. [question]
5. [question]
6. [question]
7. [question]
8. [question]
9. [question]
10. [question]

RANKING STRATEGY: [2-3 sentences]

Ready to write?
```

🛑 **HUMAN LOOP #2:** Wait for Virgil's confirmation. If he wants keyword changes, angle changes, or a different story, adjust before moving on.

### 2b: Update the CSV

After Virgil confirms, update the article's row in `Marketing/SEO/Article_Production_System.xlsx`:
- Update the primary keyword if it changed
- Add validated supporting keywords to the "Supporting Keywords" column
- Add a one-line ranking strategy note to the "Ranking Strategy" column

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 3: Load Virgil's Voice

**Read the voice profile:**

- **Virgil_Voice_MASTER.md** at `Soul/Virgil_Voice/Virgil_Voice_MASTER.md` — read in full. This is the single authoritative voice file (596 lines). Contains complete voice context, Long-Form Voice Rules, People rules, and fresh story requirement. Do NOT read FINAL or COMPLETE.
- **Virgil_Writing_Examples.md** at `Soul/Virgil_Voice/Virgil_Writing_Examples.md` — read in full. Real writing samples from Virgil showing the voice in practice. Study the rhythm, the one-line punches, the cultural references, the vulnerability, and the concrete details. The MASTER file tells you the rules. This file shows you what the voice sounds like.

**Key voice rules for long-form SEO articles:**
- First-person narrative throughout — "I" not "we" (except "Victor and I", "Vinod and I")
- Real stories, real names, real numbers — never invent
- Plain language a 7-year-old can read
- Say it once, move on — no repetition
- Conversational tone, not textbook
- Compression over long-winded explanations

**BANNED PHRASES:**
- "Here's the thing"
- "Here's why/how/what"
- "This is where [X] gets made"
- "That's the edge"
- "You need to" / "You should"
- "Most people don't realize"
- Complex words a 7-year-old wouldn't understand
- Repeating the same idea multiple times

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 4: Find a Real Story from content-ideas.md

**CRITICAL RULE: Never write a story from memory. Never invent story details. Always source from content-ideas.md. The file tracks what has been used.**

### Why this rule exists

Claude has no memory between sessions. Without this rule, the same 3-4 stories appear in every article. The fix: source stories from the file every time, tag used stories in the file, and never touch a tagged story again.

### 4a: Search Fireflies

Use the Fireflies MCP tools to search for keywords from the article brief. Pull real quotes and numbers if found.

### 4b: MANDATORY — Grep content-ideas.md for a relevant story

No matter what Fireflies returned, grep `Marketing/Research/content-ideas.md` for stories related to the article topic. Search for the article's main keywords and themes.

### 4c: Check for USED IN tags — skip any tagged story

Search content-ideas.md for `USED IN:` to see which stories are already used. **Any story with a `<!-- USED IN: -->` tag is off-limits. Do not use it.**

Pick only stories with no tag.

### 4d: Pick the most relevant fresh story

From the untagged stories, pick the one that best fits the article's theme. Stay as close to the raw notes as possible. Do not embellish. Do not add dialogue that isn't in the notes. If the notes contain a direct quote, use it exactly. If the notes say "X happened," write "X happened" — do not expand it into a scene you are inventing.

If no untagged stories fit the topic: use the most recent untagged story and adapt to the article angle. Do not invent. Do not borrow from other articles.

### 4e: After saving (Step 9) — tag the used story

Go to content-ideas.md and add this tag on the line immediately after the story you used:
```
<!-- USED IN: article-XX-slug -->
```

This is how future sessions know which stories are fresh. No memory between sessions — the file tracks it.

---


### Pattern 1: Punch line standing alone

A short sentence that lands the point. It gets its own block. Nothing attached to it.

✅ CORRECT:
```
You start with the tasks they already hate.
```

```
That approach failed.
```

```
If I can build it, your agency can build it.
```

❌ WRONG:
```
You start with the tasks they already hate, because that is where the most time gets wasted.
```
(Punch lines die when padded. Cut after the point lands.)

---

### Pattern 2: 2-3 sentence blocks, blank line between

Group connected sentences into a block. Blank line between every block. Never 4+.

✅ CORRECT:
```
I learned this the hard way. When I first tried adding AI to our marketing operations at Sucana, I made the classic mistake. I looked at what AI could do and tried to find places to use it.

That approach failed.

What actually works: look at where your team wastes time, then ask if AI can take that off their plate. The workflow comes from the problem, not from the technology.
```

❌ WRONG:
```
I learned this the hard way. When I first tried adding AI to our marketing operations at Sucana, I made the classic mistake. I looked at what AI could do and tried to find places to use it. That approach failed. What actually works is to look at where your team wastes time and ask if AI can take that off their plate. The workflow comes from the problem, not from the technology.
```
(This is a blob. Six sentences jammed together. Never do this.)

---

### Pattern 3: Bold labels only for genuine callouts

Bold a label when the label belongs on its own line before a prose block. Never bold inline inside a sentence.

Always put a blank line between the bold label and the text below it. Never put the text on the line directly after the label.

✅ CORRECT:
```
**Data layer:**

Where your numbers live, ad platforms, CRM, analytics.

**Connection layer:**

How data moves between systems, Claude Code, n8n, custom scripts.

**AI layer:**

Where the thinking happens, Claude, custom agents.
```

❌ WRONG:
```
**Data layer:**
Where your numbers live, ad platforms, CRM, analytics.
```
(No blank line between label and text. Always add a blank line after the bold label.)

❌ WRONG:
```
The **data layer** is where your numbers live and includes ad platforms, CRM, and analytics, while the **connection layer** handles how data moves between systems.
```
(Inline bold is McKinsey slide. Concepts that flow as prose belong as prose.)

---

### Pattern 4: Lists with blank lines between items

Each list item gets its own line. Blank line between items when items carry inline descriptions.

✅ CORRECT:
```
The criteria for a good AI workflow:

- **Repeatable:** It happens the same way every time

- **Data-driven:** The inputs are structured, not random

- **Time-consuming:** It takes hours, not minutes

- **Low-judgment:** The decisions are routine, not strategic
```

❌ WRONG:
```
The criteria for a good AI workflow:
- Repeatable: same every time
- Data-driven: structured inputs
- Time-consuming: hours not minutes
- Low-judgment: routine decisions
```
(No blank lines between items. Compresses into a wall.)

---

### Pattern 5: FAQ answer blocks

2-3 sentences per block inside a FAQ answer. Blank line between blocks within the same answer.

✅ CORRECT:
```
### How long does it take to see results from AI workflows?

If your workflow is well-scoped, you'll see time savings in the first week.

Most teams report 4-6 hours saved per week within 30 days. Payback period for setup time is usually one to two weeks.
```

❌ WRONG:
```
### How long does it take to see results from AI workflows?
If your workflow is well-scoped, you'll see time savings in the first week. Most teams report 4-6 hours saved per week within 30 days. Payback period is usually one to two weeks.
```
(No blank line before first sentence, no blank line between blocks. Runs together.)

---

### Pattern 6: Steps written as a friend talking, not an IKEA manual

✅ CORRECT (from AI SOPs article):
```
Open Claude Cowork. Tell Claude what the task is.

"I do a weekly client report every Monday. It takes me two hours."

Then say: "Can you ask me questions to refine this?"

Claude will ask things like: What format does the client expect? What tone do they prefer?

You answer. Claude builds the plan.
```

❌ WRONG:
```
Step 1: Open Claude Cowork.
Step 2: Tell Claude what the task is.
Step 3: Input your description of the weekly report.
Step 4: Ask Claude to ask you questions to refine.
```
(IKEA manual. Numbered steps kill the voice.)

---

## STANDING RULE: ALWAYS OPEN ARTICLE IN VS CODE PREVIEW

**This applies everywhere in the pipeline — not just Step 8.**

Every time you edit the article file for any reason — story rewrite, step edit, heading change, FAQ addition, bash fix — you MUST regenerate the HTML preview file and `open` it in the browser immediately after saving.

Do NOT output the article as markdown in chat. Do NOT use VS Code markdown preview. Always generate an HTML file and open it in the browser.

**No exceptions. No "I updated the file" without opening the HTML preview.**

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 5: Write the Article

### WRITING RULES — Read Before Every Sentence

These are corrections from Virgil. Each one is a mistake that was made and corrected. Do not repeat them. This list is updated after every article.

**Last updated:** 2026-03-14

1. **Never use vague category words without the specific modifier.** "Agency" alone is meaningless. "Tool" alone is meaningless. Always specify what kind. "Marketing agency." "Reporting tool." "Analytics platform." The reader should never have to guess.

2. **Opening sentences must be concrete actions, not clever phrases.** Never start an article with something abstract or poetic. Start with what to do. "Start with X" beats "Not with Y, with Z" every time.

3. **H2 headings are 8 words maximum.** Short, punchy, like a hook.

4. **Titles must match what the article actually teaches.** If the article is about improving something that already exists, do not title it as if you are building something new. The title sets the expectation. The content must deliver exactly that.

5. **"Where to Start" and actionable sections must be universally applicable.** Do not assume the reader works in a specific niche. Use general examples that work for any reader in the target audience.

6. **No brand name in title tags.** No SEO value for a new domain with no brand recognition. Drop "| Sucana" or any brand suffix.

7. **All publish dates must be unique.** Never deploy two articles on the same date.

8. **Always show the full article in chat after every change.** Output every word as markdown in the response. Do not use the Read tool (collapses in VSCode). No exceptions.

9. **Pillar pages link to ALL cluster articles in their pillar. Every cluster article links back.** After deploying a pillar page, run retroactive linking immediately.

10. **Do not write steps that assume niche-specific tools or workflows.** If the article is for a broad audience, use examples any reader would recognize. Only use niche-specific references when the article is explicitly about that niche.

11. **Never repeat the heading in the first sentence.** The first sentence after any H2 or H3 must add new information, not echo the heading. If the heading says "Victor Was Staring at Three Monitors" the paragraph must NOT open with "Victor was staring at three monitors." The reader already read the heading. Move the story forward.

12. **Never reference internal tools, agents, or systems without explaining them.** The reader does not know what Nelly, Hermes, Honcho, MCP, or any internal name means. If you mention it, explain what it does in one plain sentence. If it takes more than one sentence to explain, leave it out entirely. Do not pull names from transcripts or internal notes assuming the reader has context. Everything must be crystal clear to a first-time reader.

**How to update this list:** When Virgil corrects something during an article session, add the correction here as a new numbered rule immediately. Do not wait until end of session. Cap at 25-30 rules. Merge similar rules. Only remove a rule when it has been absorbed into an automated bash check.

---

**Structure every article with these sections:**

### SEO Frontmatter (top of the markdown file)
```markdown
# [Article Title]

**Primary Keyword:** [validated keyword from Step 2]
**Supporting Keywords:** [3-5 long-tail keywords from Step 2]
**LLM Query Target:** [llm query from CSV]
**Word Count:** [actual word count]
**Author:** Virgil Brewster
**Status:** Ready for review
```

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

### Step 5a: Write ONLY the Opening H2 + Answer — Then Voice-Check It Before Showing

**This sub-step is its own moment. Do not write anything else until the opening is approved.**

**MANDATORY: Read the last published article first.** Before writing a single word, find the most recently published article in `Marketing/SEO/articles/` (check file dates or the Production System for the latest "Published" entry). Read at least the first 60 lines — the opening H2, the answer, the story section, and the first body section. This is your voice calibration. Match that rhythm, that specificity, that level of concreteness. If the last article names exact tasks ("Monday morning data pulls"), do not write generic labels ("grunt work"). If the last article opens with an action ("Start with the bottleneck"), do not open with a statement. The last published article is the quality bar and the voice bar.

Write:
1. The H2 question (the exact question the article answers)
2. A 2-3 sentence direct answer directly below the H2

**BEFORE showing to Virgil, run a Voice Gate Agent.** Launch an Agent with these instructions:

```
You are Virgil's voice gate. Read Soul/Virgil_Voice/Virgil_Voice_MASTER.md in full.
Then check this opening text against the voice rules:

[paste the opening H2 + answer here]

Check for:
1. AI crap detector: Does any sentence sound like it was written by an AI? Flag specific phrases. "Every marketer works differently" = AI filler. "In my experience" = borderline. "I run my marketing on it" = real.
2. Words Virgil would never say: Check against the banned words list AND the cringe words list in the voice file. Also flag any word a 7-year-old would not understand.
3. Sentence rhythm: Are sentences varied in length? Or do they all follow the same pattern? Virgil's rhythm is short-long-short-punch. Not medium-medium-medium-medium.
4. Virgil's actual phrases: Does it sound like something Virgil would say in a Slack message? If not, rewrite it so it does.
5. Compression test: Can any sentence be said in fewer words? If yes, compress it.
6. "Two tequilas on Ibiza" test: Read it out loud. Does it sound like a guy at a beach bar telling you what he uses? Or does it sound like a blog post?

Return:
- PASS or FAIL
- If FAIL: flag every offending sentence with a rewrite suggestion
- If PASS: confirm it sounds like Virgil, not like AI
```

**Only show the opening to Virgil AFTER the voice gate passes.** If it fails, rewrite the flagged sentences and run the gate again. Do not show AI crap to Virgil.

**CORRECT:**
```
## What Are the Best ChatGPT Prompts for PPC Managers?

The best ones start with your client's actual data, not a generic question.

Feed ChatGPT the spend, ROAS, campaign history, and what the client keeps complaining about. Then ask.

Generic prompts give generic answers.
```

**WRONG:**
```
To get useful answers from ChatGPT as a PPC manager...  ← floating paragraph before any H2

## Why Most Prompts Don't Work  ← question buried, came second
```

Rules:
- H2 question comes first. Before any paragraph. Before any story. Before anything.
- The answer to that question is 2-3 sentences directly below the H2. Short and direct.
- Story comes after the answer — in Step 5b.
- All other H2s in the body can be statements or questions — does not matter.
- Only this first H2 must be the question that matches the article's intent.

🛑 **Show the opening H2 + answer (voice-gate passed). Wait for confirmation before proceeding to Step 5b.**

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

### Step 5b: Write the Full Article Body

After opening is confirmed, write the full article hitting the word count target from the CSV.

**Do NOT write the FAQ section in this step — that's Step 5c.**

---

#### ARTICLE STRUCTURE — read TEMPLATE.md, not this skill

⚠️ **STICK TO THE TEMPLATE.** Article structure is defined in ONE place: `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`.

Do not follow any inline structure rules that used to live in this skill. They are gone. TEMPLATE.md is the only source.

Before writing any article content:
1. Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md` in full.
2. Output its 12 bullets verbatim in the chat.
3. Then write the article following those 12 parts, in order, every time.
4. When finished, call the Template Guardian agent (spec at top of this file) on the draft. If Guardian returns FAIL, fix violations and re-run. Step 5b does not complete until Guardian returns PASS.

No "article types." No "depends on the topic." Twelve parts. In order. Every time.

---

**IMPORTANT — Image Placement Planning:**
While writing the article, identify **2-3 spots** where an image would add real value to the reader. Mark these spots with image placeholders. Good image locations are:

- After a section that explains a concept visually (data flow, process, comparison)
- Next to a data-heavy section (turn numbers into a visual)
- At a key transition point to break up long text and re-engage the reader

Use this placeholder format in the draft:

```markdown
![IMAGE: Brief description of what this image should show](placeholder-image-1.png)
```

Number them sequentially: `placeholder-image-1.png`, `placeholder-image-2.png`, `placeholder-image-3.png`

**Every article MUST have at least 2 image placeholders, ideally 3.** Do NOT cluster them — spread them evenly through the article body.

**Content structure rules (for Google AND LLM citation):**

1. **Question H2 first**: The very first H2 is a question that directly matches the article's topic. The 2-3 sentences below it directly answer that question. Story comes after the answer, never before.

2. **H2 headings are statements, not questions.** Only the FIRST H2 is a question. All other body H2s are short statement hooks. Questions belong in the FAQ section only. **All H2 headings must be 8 words maximum.**
   - Good: `## The Real Cost of AI Automation`
   - Good: `## What Nobody Tells You About Maintenance`
   - Bad: `## Pricing Information` (too generic)
   - Bad: `## How Much Does a PPC Dashboard Cost for Your Agency?` (too long, and question outside FAQ)

3. **Use H2 for main sections, H3 for subsections.** Never skip levels.

4. **Include specific data**: Statistics, percentages, dollar amounts. Quantitative claims get 40% higher citation rates.

5. **Use structured formats — but prose is the default:**
   - Virgil's voice is prose-first. Only use lists when 4+ items genuinely work better as a list than as a sentence.
   - Numbered lists and bullet points work for enumerable items — not for concepts that flow naturally as writing
   - Comparison tables for direct comparisons — yes
   - Code blocks for actual prompts and commands — yes
   - Step-by-step formatting: walk through it conversationally, not as numbered IKEA instructions

6. **Target 2,000+ words** — but hit it through depth of insight, not padding. One sentence that says it fully beats a paragraph that says it three times. Word count comes from covering the topic completely, not repeating it. The voice file ceiling is 2,000 words. Push past it only when the topic genuinely demands it.

7. **Do NOT use**:
   - Vague statements ("many agencies find that...")
   - Filler paragraphs that don't add information
   - Clickbait or exaggerated claims

⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md` now. Before writing ANY article content, output the 12 template bullets from TEMPLATE.md verbatim in the chat. If the bullets are not printed, Step 5b has not started.

**There is ONE template. Every Sucana article is a How-To built from TEMPLATE.md.**

No "article types." No "Founder Story vs Pillar vs Comparison." No "it depends." Every article. One template. Twelve parts. Twelve times, in order.

```
1.  Title (H1) — first-person "How I built X" or "Why I built X"
2.  Meta — one sentence under title, includes primary keyword
3.  Intro — 1 to 3 paragraphs, first-person, problem or moment
4.  H2: Why I Did This (or "The Problem I Was Trying to Solve")
5.  H2: What I Built (or "What I Asked Claude Code to Build")
6.  H2: Before You Start — tools, accounts, credentials
7.  H2: Step 1 to Step N (7 to 14 steps) — prose + exact Claude prompt as code block
8.  H2: What I'd Do Differently — 2 to 5 short lessons
9.  H2: The Stack — table of tools
10. H2: Files — folder structure
11. H2: FAQ — 8 to 10 questions
12. Soft CTA — one line at end
```

**Step block format (purple/pink, mandatory, same in every article):**

```css
.stage {
  background: #FAF5FF;
  border-radius: 12px;
  padding: 24px;
  margin: 24px 0;
}
.stage-title {
  font-size: 20px;
  font-weight: 700;
  color: #9333EA;
  margin-bottom: 16px;
}
```

Inside each Step block: natural prose. Exact Claude prompt as copy-pasteable code block. Jargon explained on first mention. No repeated "Do this / What happens / Why I did this" labels.

**Source-skill read requirement:** If the article documents a workflow powered by another skill (dm, lfg, newsletter, ad-image, etc.), read that skill's SKILL.md in full before writing Step 1. The Steps come from the source skill, not from imagination.

**Before continuing Step 5b, call the Template Guardian agent (see top of this file) on the draft. Step 5b cannot complete until Guardian returns PASS.**

### Dual Optimization (Google + LLM)

**For Google ranking:**
- Primary keyword in H1, first paragraph, and 2-3 H2s naturally
- Supporting keywords woven into H2s, H3s, and body text — never forced
- Title tag (≤60 characters) — compelling, keyword-included
- Meta description (≤155 characters) — includes keyword, drives clicks
- Internal link opportunities noted at the bottom
- Clear heading hierarchy (H1 → H2 → H3)
- FAQ section using the "Questions People Ask" from Step 2
- **Images with keyword-rich alt text** — Google indexes alt text for image search

**For LLM citation:**
- Clear, definitive answers to the LLM Query Target question
- Structured data that LLMs can extract and cite
- FAQ answers written as standalone, quotable paragraphs
- Confident first-person tone on data points — "I found that X works" not "X is the correct approach." Authority comes from the story, not the posture. Cite sources where applicable.
- Entity establishment — make "Sucana" and "Virgil Brewster" clearly defined entities

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

### Step 5c: Write the FAQ — Dedicated Sub-Step

**This is its own moment. Treat it like generating images — a separate, deliberate action, not a footnote.**

**10 questions minimum. No exceptions.**

Source questions from the PAA (People Also Ask) list compiled in Step 2. Use those exact questions — they are what real people search for.

Each answer: 2-4 sentences. Group 2-3 connected sentences into a block. Blank line between blocks. Same rule as the article body — no choppy single-sentence lines, no blobs.

Format:

```markdown
## Frequently Asked Questions

### What is ROAS and why does it matter?

ROAS (Return on Ad Spend) measures revenue generated per dollar of ad spend. Higher ROAS means your ads are working.

Most agencies target 3-4x ROAS as a baseline, but the right number depends on your margins.

### How often should I check campaign metrics?

For active campaigns, daily monitoring of key metrics catches problems before they compound. Weekly deep dives catch trends that daily checks miss.
```

**After writing the FAQ, count the questions before moving on. If under 10, add more from the PAA list before proceeding.**

### SEO Notes (bottom of file)
```markdown
## SEO Notes

**Primary Keyword:** [keyword]
**Supporting Keywords:** [list]
**Ranking Strategy:** [1-2 sentence summary from Step 2]

**Internal Link Opportunities:**
- [list 3-5 internal linking opportunities to other articles in the CSV]

**Schema Markup:**
- [schema types from CSV — Article, FAQ, Person, Dataset, HowTo, etc.]

**Meta Description (155 chars):**
"[meta description]"

**Title Tag (60 chars):**
"[title tag]"

**In-Article Images:**
- placeholder-image-1.png → [description of what it shows]
- placeholder-image-2.png → [description of what it shows]
- placeholder-image-3.png → [description of what it shows]
```

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 5.5: Structure Checkpoint

**Before generating images, show Virgil the FULL article body in chat. Read the article from the file using the Read tool and display every word. Then show the structure summary below it:**

```
STRUCTURE CHECK: Article #[number]

H1: [exact title]

First H2: [the question — must be a natural language question]

Opening answer: [the 2-3 sentences directly under the first H2]

Angle: [one sentence — what makes this article different from everything else ranking]

Right question? Right angle? Say yes to continue or tell me what to change.
```

🛑 **HUMAN LOOP #3:** Wait for approval. If the question or angle is wrong, rewrite those sections before continuing. Do NOT proceed to Step 6 until Virgil says yes.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 5.6: Two-Agent Review Gate — Before Images

**This is a mandatory stop. Do not generate images until this clears. Do NOT show the article to Virgil until BOTH agents pass.**

Launch TWO agents IN PARALLEL. They each review the article independently. Then their findings are cross-checked. Both must pass.

### AGENT A — Content & Quality Reader

```
You are the content quality reader for Sucana. Read the full article draft at [article path].

Then read the last approved article: find the most recently published article in Marketing/SEO/articles/ (check file dates). Read it in full. This is the quality bar.

CHECK:
1. Strong how-to section? Can a beginner follow step by step AND does an advanced reader learn something new? If the how-to is weak, vague, or skippable — FAIL with specifics.
2. Every claim backed by a real example, real number, or real story? Flag any sentence that makes a claim without proof.
3. Anything fake, invented, or embellished? Flag it. Zero tolerance.
4. Clear for beginners AND advanced? If it talks down or bores experts, flag which sections.
5. Article structure matches the template? (H2 question, answer, story H2, story, steps, FAQ)
6. Quality at least as good as the last published article? Compare directly.
7. SEO: primary keyword in H1 and first paragraph? Supporting keywords natural in H2s?

RETURN:
- PASS or FAIL
- If FAIL: list every issue with line numbers and specific fix instructions
- If PASS: one sentence confirming quality
```

### AGENT B — Voice & AI Detector

```
You are Virgil's voice enforcer. Your only job is making sure this article sounds like Virgil wrote it, not an AI.

STEP 1: Read Soul/Virgil_Voice/Virgil_Voice_MASTER.md in full. Study the voice rules, banned words, cringe words, compression principle, and the Virgil Library sentences.

STEP 2: Read the last approved article in Marketing/SEO/articles/ (most recent by file date). Study the rhythm, the sentence lengths, the way Virgil opens sections, how he transitions. This is what "passing" sounds like.

STEP 3: Read the new article draft at [article path].

STEP 4: Check every sentence:
- AI filler detector: Flag any phrase that sounds generated. Examples of AI crap: "In my experience", "Every marketer works differently", "It depends on your needs", "This is where X gets made", "Here's the thing", "At the end of the day", "It's worth noting". If a human would never say it in a Slack message, flag it.
- Banned words: Check against the voice file lists. Flag with line numbers.
- 7-year-old test: Any word a kid would not understand? Flag it with a simpler replacement.
- First-person check: Does every section have at least one "I" sentence? Flag any section that is purely general advice.
- IKEA manual check: Do steps sound like a friend talking or an instruction manual? Flag robotic sentences.
- Universal declarations: "The right tool is X" instead of "I use X"? Flag them.
- Sentence rhythm: Are lengths varied (short-long-short-punch) or monotone (medium-medium-medium)? Flag monotone stretches.
- "Two tequilas on Ibiza" test: Read the whole thing. Does it sound like Virgil at a beach bar or like a content marketing intern?
- Compare rhythm and tone to the last approved article. Flag any drift.

RETURN:
- PASS or FAIL
- If FAIL: list every offending sentence with line number, quote it, explain why it fails, and provide a rewrite suggestion in Virgil's voice
- If PASS: one sentence confirming it sounds like Virgil
```

### Cross-Check and Resolve

After both agents return:

**Both PASS:** Proceed to Step 6. Article is ready for images.

**One or both FAIL:** Fix every flagged issue from both agents. Then run BOTH agents again on the fixed version. Repeat until both return PASS. Do NOT proceed to Step 6 or show anything to Virgil until both pass.

**Conflicting feedback:** If Agent A says a section is good but Agent B flags the voice, fix the voice. Voice always wins over structure. If Agent B says the voice is fine but Agent A flags a quality issue, fix the quality. Both gates must be green.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 6: Generate In-Article Images (2 Plotly Charts)

**Every article gets exactly 2 images: both are Plotly charts with Sucana brand colors. No Nanobanana inside the article.**

Save all images to: `Marketing/SEO/articles/images/{slug}-image-{number}.png`

---

### 6a: Plotly Charts (Images 1 and 2)

**Brand colors (hardcoded — always use these):**
- Background: `#f1f5f9` (light grey)
- Grid lines: `#e2e8f0` (subtle)
- Purple (primary bar): `#8b5cf6`
- Pink (accent bar): `#ec4899`
- Text: `#0f172a` (dark)
- Muted labels: `#64748b`

**Chart layout rules (hardcoded — always apply):**
- `paper_bgcolor` and `plot_bgcolor`: `#f1f5f9`
- `font.family`: `'Inter, Arial, sans-serif'`
- `font.color`: `#0f172a`
- Axes: no border lines (`showline=False`), grid color `#e2e8f0`, tick font color `#64748b`
- Title: centered (`x=0.5`), font size 20, color `#0f172a`
- Margins: `l=60, r=60, t=80, b=60`
- Output size: `width=1200, height=675` (16:9), `scale=2`

**Image 1 — Before/After or key metric comparison (simple bar chart):**

⚠️ COPY THIS TEMPLATE EXACTLY. Do NOT rewrite it. Only replace the placeholder values.

```bash
python3 << 'PYEOF'
import plotly.graph_objects as go

# COLORS — use these exact hex codes, never CSS color names
PINK   = '#ec4899'
PURPLE = '#8b5cf6'
BG     = '#f1f5f9'
GRID   = '#e2e8f0'
TEXT   = '#0f172a'
MUTED  = '#64748b'

fig = go.Figure()
fig.add_trace(go.Bar(
    x=['[Label A]', '[Label B]'],
    y=[VALUE_A, VALUE_B],
    marker_color=[PINK, PURPLE],
    marker_line_width=0,
    width=0.45,
    text=['VALUE_A [unit]', 'VALUE_B [unit]'],
    textposition='outside',
    textfont=dict(color=TEXT, size=18, family='Inter, Arial, sans-serif'),
))
fig.update_layout(
    title=dict(text='[Chart title]', font=dict(color=TEXT, size=20, family='Inter, Arial, sans-serif'), x=0.5, xanchor='center', pad=dict(b=8)),
    plot_bgcolor=BG, paper_bgcolor=BG,
    font=dict(color=TEXT, family='Inter, Arial, sans-serif'),
    xaxis=dict(showgrid=False, showline=False, tickfont=dict(color=TEXT, size=15)),
    yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, showline=False, tickfont=dict(color=MUTED, size=13), ticksuffix=' [unit]', range=[0, MAX_VALUE * 1.2]),
    # l = tick label width (~30px) + padding (40px) = 70px
    # r = padding only (40px) → equal visual breathing room on both sides
    margin=dict(l=70, r=40, t=120, b=60),
    width=1200, height=675, bargap=0.5,
)
fig.write_image('/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-1.png', scale=2)
print('Chart 1 saved.')
PYEOF
```

**Image 2 — Grouped bar chart (multiple categories × 2 metrics):**

⚠️ COPY THIS TEMPLATE EXACTLY. Use when comparing 2 series across multiple categories (e.g. ABO vs CBO across 4 creatives).

```bash
python3 << 'PYEOF'
import plotly.graph_objects as go

PINK   = '#ec4899'
PURPLE = '#8b5cf6'
BG     = '#f1f5f9'
GRID   = '#e2e8f0'
TEXT   = '#0f172a'
MUTED  = '#64748b'

categories = ['[Cat A]', '[Cat B]', '[Cat C]', '[Cat D]']
series1_values = [V1, V2, V3, V4]
series2_values = [V1, V2, V3, V4]

fig = go.Figure()
fig.add_trace(go.Bar(
    name='[Series 1 label]',
    x=categories,
    y=series1_values,
    marker_color=PURPLE,
    marker_line_width=0,
    text=[f'{v}[unit]' for v in series1_values],
    textposition='outside',
    textfont=dict(color=TEXT, size=14, family='Inter, Arial, sans-serif'),
))
fig.add_trace(go.Bar(
    name='[Series 2 label]',
    x=categories,
    y=series2_values,
    marker_color=PINK,
    marker_line_width=0,
    text=[f'{v}[unit]' for v in series2_values],
    textposition='outside',
    textfont=dict(color=TEXT, size=14, family='Inter, Arial, sans-serif'),
))
fig.update_layout(
    barmode='group',
    bargap=0.25,
    bargroupgap=0.05,
    title=dict(text='[Chart title]', font=dict(color=TEXT, size=20, family='Inter, Arial, sans-serif'), x=0.5, xanchor='center', pad=dict(b=8)),
    plot_bgcolor=BG, paper_bgcolor=BG,
    font=dict(color=TEXT, family='Inter, Arial, sans-serif'),
    legend=dict(orientation='h', yanchor='bottom', y=1.0, xanchor='center', x=0.5, font=dict(color=TEXT, size=14)),
    xaxis=dict(showgrid=False, showline=False, tickfont=dict(color=TEXT, size=14)),
    yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, showline=False, tickfont=dict(color=MUTED, size=13), ticksuffix='[unit]', range=[0, MAX_VALUE * 1.3]),
    # l = tick label width (~30px) + padding (40px) = 70px
    # r = padding only (40px) → equal visual breathing room on both sides
    margin=dict(l=70, r=40, t=120, b=60),
    width=1200, height=675,
)
fig.write_image('/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-2.png', scale=2)
print('Chart 2 saved.')
PYEOF
```

Use the simple bar template for Image 1, grouped bar template for Image 2 when 2 series are needed. If Image 2 is a single-series comparison instead, use the simple bar template for both.

---

### 6b: Replace Placeholders in the Article

```markdown
![Description of what the chart shows](/images/blog/{slug}-image-1.png)
```

Alt text stays descriptive (SEO + accessibility). Path points to the blog image directory.

---

### 6c: Show Charts to Virgil

**MANDATORY: OPEN THE IMAGES SO VIRGIL CAN SEE THEM. Every single time. No exceptions. Do not describe them. Do not link them. OPEN THEM.**

Run `open` on each image file so it opens in macOS Preview where Virgil can actually see it:

```bash
open "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-1.png"
open "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-2.png"
```

Also use the Read tool on each PNG so the image displays inline in chat:

```
Read: /Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-1.png
Read: /Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-2.png
```

Then output:

```
IN-ARTICLE CHARTS: Article #[number]

Chart 1: [one sentence — what data it shows]
[image displayed above]

Chart 2: [one sentence — what data it shows]
[image displayed above]

Charts ok? Or need changes?
```

🛑 **HUMAN LOOP #4:** Wait for Virgil's approval. If changes needed, fix the Python code and regenerate. Show again until approved.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 7: Self-Check Before Showing

**THE SELF-CHECK IS NOT MENTAL. RUN BASH COMMANDS ON THE ACTUAL FILE. SHOW THE OUTPUT. DO NOT PROCEED TO STEP 8 UNTIL ALL CHECKS PASS.**

### 7a: MANDATORY Bash Checks — Run These, Show the Output

```bash
ARTICLE_PATH="Marketing/SEO/articles/article-XX-slug.md"

# CHECK 1: Em dashes — must be 0. Use commas or colons instead. Never em dashes.
EM_DASH_COUNT=$(grep -c "—" "$ARTICLE_PATH" 2>/dev/null || echo "0")
if [ "$EM_DASH_COUNT" -gt 0 ]; then
  echo "❌ FAIL: Found $EM_DASH_COUNT em dash(es). Replace every — with a comma or colon. Do not proceed until fixed."
else
  echo "✅ PASS: No em dashes found."
fi

# CHECK 2: Banned phrases
echo "Banned phrases:" && grep -in "here's the thing\|here's why\|here's how\|most people don't\|you need to\|you should\|that's the edge" "$ARTICLE_PATH" || echo "NONE"

# CHECK 2b: Complex vocabulary — words Virgil would never say
COMPLEX_WORDS=$(grep -in "regardless\|commentary\|leverage\|synergy\|unlock\|empower\|revolutionary\|game-changing\|best-in-class\|comprehensive\|furthermore\|additionally\|nevertheless\|consequently\|utilize\|utilise\|facilitate\|demonstrate\|methodology\|ecosystem\|paradigm\|scalable\|robust\|seamless\|actionable\|impactful\|holistic\|streamline\|benchmark\|bandwidth\|granular\|alignment\|landscape\|trajectory\|optimiz" "$ARTICLE_PATH" || true)
if [ -n "$COMPLEX_WORDS" ]; then
  echo "❌ FAIL: Complex words found — replace with plain language a 7-year-old understands:"
  echo "$COMPLEX_WORDS"
  echo "Do not proceed until fixed."
else
  echo "✅ PASS: No complex vocabulary found."
fi

# CHECK 2c: Long sentences — flag any sentence over 20 words (hard fail)
echo "Sentences over 20 words:"
LONG_SENTENCES=$(python3 -c "
import re, sys
text = open('$ARTICLE_PATH').read()
# Skip code blocks and frontmatter
text = re.sub(r'\`\`\`.*?\`\`\`', '', text, flags=re.DOTALL)
sentences = re.split(r'(?<=[.!?])\s+', text)
found = [(i+1, s.strip()) for i, s in enumerate(sentences) if len(s.split()) > 20 and s.strip()]
for num, s in found:
    print(f'  [{len(s.split())} words] {s[:120]}')
print(f'TOTAL: {len(found)}')
" 2>/dev/null)
echo "$LONG_SENTENCES"
LONG_COUNT=$(echo "$LONG_SENTENCES" | grep "TOTAL:" | grep -o "[0-9]*" || echo "0")
if [ "$LONG_COUNT" -gt 0 ] 2>/dev/null; then
  echo "❌ FAIL: $LONG_COUNT sentence(s) over 20 words. Break every one into shorter sentences. Do not proceed until fixed."
else
  echo "✅ PASS: All sentences are 20 words or under."
fi

# CHECK 3: Word count
echo "Word count:" && wc -w < "$ARTICLE_PATH"

# CHECK 3c: H2 WORD COUNT — all H2 headings must be 8 words maximum
echo "H2 word count check:"
H2_LONG=$(python3 -c "
import re
lines = open('$ARTICLE_PATH').readlines()
fails = []
for i, line in enumerate(lines):
    if line.startswith('## '):
        heading = line.strip().lstrip('# ').strip()
        wc = len(heading.split())
        if wc > 8:
            fails.append((i+1, wc, heading))
for f in fails:
    print(f'  Line {f[0]}: [{f[1]} words] {f[2]}')
print(f'LONG H2 COUNT: {len(fails)}')
" 2>/dev/null)
echo "$H2_LONG"
LONG_H2_COUNT=$(echo "$H2_LONG" | grep "LONG H2 COUNT:" | grep -o "[0-9]*" || echo "0")
if [ "$LONG_H2_COUNT" -gt 0 ] 2>/dev/null; then
  echo "❌ FAIL: $LONG_H2_COUNT H2 heading(s) over 8 words. Shorten every H2 to 8 words max. Do not proceed until fixed."
else
  echo "✅ PASS: All H2 headings are 8 words or under."
fi

# CHECK 3b: STORY H2 HEADING — the second H2 must be a specific story heading, not a step and not a generic label
SECOND_H2=$(grep -n "^## " "$ARTICLE_PATH" | sed -n '2p')
SECOND_H2_TEXT=$(echo "$SECOND_H2" | cut -d: -f2-)
echo "Second H2: $SECOND_H2_TEXT"
# Fail if second H2 starts with "Step" or is a generic label
if echo "$SECOND_H2_TEXT" | grep -qiE "^## Step |^## Background|^## The Story|^## My Experience|^## Introduction|^## Overview|^## Context"; then
  echo "❌ FAIL: Second H2 is a step or generic label — '$SECOND_H2_TEXT'. The second H2 MUST be a sharp, specific story heading (e.g. '## What I Saw When I Searched for Sucana in ChatGPT'). Do not proceed until fixed."
elif [ -z "$SECOND_H2_TEXT" ]; then
  echo "❌ FAIL: No second H2 found. Every article needs a story H2 heading immediately after the opening Q&A. Do not proceed until fixed."
else
  echo "✅ PASS: Story H2 present: $SECOND_H2_TEXT"
fi

# CHECK 4: QUESTION FIRST — detect any non-blank paragraph before the first ## heading
FIRST_H2_LINE=$(grep -n "^## " "$ARTICLE_PATH" | head -1 | cut -d: -f1)
echo "First H2 at line: $FIRST_H2_LINE — $(grep -m 1 "^## " "$ARTICLE_PATH")"
FLOATING_PARA=$(awk "NR<$FIRST_H2_LINE && /^[A-Za-z]/{print; exit}" "$ARTICLE_PATH")
if [ -n "$FLOATING_PARA" ]; then
  echo "❌ FAIL: Found floating paragraph before first ## heading:"
  echo "  → $FLOATING_PARA"
  echo "  FIX: Delete this paragraph. The article must start with the H2 question (after frontmatter). Do not proceed until fixed."
else
  echo "✅ PASS: No floating paragraph before first H2."
fi

# CHECK 5: FAQ count — only counts H3s inside the ## Frequently Asked Questions section
FAQ_COUNT=$(awk '/^## Frequently Asked Questions/{found=1; next} found && /^## /{found=0} found && /^### /{count++} END{print count+0}' "$ARTICLE_PATH")
echo "FAQ question count (inside FAQ section only): $FAQ_COUNT"
if [ "$FAQ_COUNT" -lt 10 ]; then
  echo "❌ FAIL: Only $FAQ_COUNT FAQ questions found. Need 10 minimum. Go back to Step 5c and add more questions from the PAA list before proceeding."
else
  echo "✅ PASS: $FAQ_COUNT FAQ questions found."
fi

# CHECK 6: NO HORIZONTAL DASHES — `---` dividers are banned from article body
DASH_COUNT=$(grep -c "^---$" "$ARTICLE_PATH" || echo "0")
if [ "$DASH_COUNT" -gt 0 ]; then
  echo "❌ FAIL: Found $DASH_COUNT horizontal dash divider(s). Remove all --- lines — use H2/H3 headings only. Do not proceed until fixed."
else
  echo "✅ PASS: No horizontal dash dividers found."
fi

# CHECK 7: NO BLOBS — paragraphs must be 2-3 sentences max. 4+ = blob.
echo "Blob check (paragraphs with 4+ sentences):"
BLOB_RESULT=$(python3 -c "
import re, sys
text = open('$ARTICLE_PATH').read()
# Strip frontmatter
text = re.sub(r'^---.*?---\n', '', text, flags=re.DOTALL)
# Strip code blocks
text = re.sub(r'\`\`\`.*?\`\`\`', '', text, flags=re.DOTALL)
# Strip image tags and headings
paragraphs = re.split(r'\n{2,}', text)
blobs = []
for i, p in enumerate(paragraphs):
    p = p.strip()
    if not p or p.startswith('#') or p.startswith('!') or p.startswith('|') or p.startswith('-') or p.startswith('*'):
        continue
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', p) if s.strip()]
    if len(sentences) >= 4:
        blobs.append((len(sentences), p[:120]))
for b in blobs:
    print(f'  [{b[0]} sentences] {b[1]}...')
print(f'BLOB COUNT: {len(blobs)}')
" 2>/dev/null)
echo "$BLOB_RESULT"
BLOB_COUNT=$(echo "$BLOB_RESULT" | grep "BLOB COUNT:" | grep -o "[0-9]*" || echo "0")
if [ "$BLOB_COUNT" -gt 0 ] 2>/dev/null; then
  echo "❌ FAIL: $BLOB_COUNT blob(s) found. Split every paragraph with 4+ sentences into 2-3 sentence blocks with a blank line between them. Do not proceed until fixed."
else
  echo "✅ PASS: No blobs found. All paragraphs are 2-3 sentences."
fi

# CHECK 8: REPETITION — no repeated distinctive phrases within the same paragraph or across paragraphs
echo "Repetition check (repeated phrases across article):"
REPEAT_RESULT=$(python3 -c "
import re, sys
text = open('$ARTICLE_PATH').read()
# Strip frontmatter and code blocks
text = re.sub(r'^---.*?---\n', '', text, flags=re.DOTALL)
text = re.sub(r'\`\`\`.*?\`\`\`', '', text, flags=re.DOTALL)
# Strip headings, images, list markers
lines = [l.strip() for l in text.split('\n') if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('!') and not l.strip().startswith('|')]
text_clean = ' '.join(lines)

# Find repeated phrases (3+ words that appear more than once)
words = text_clean.split()
found = []
seen_phrases = set()
for length in range(3, 8):
    for i in range(len(words) - length + 1):
        phrase = ' '.join(words[i:i+length]).lower()
        # Skip common phrases that naturally repeat
        skip = ['in the', 'of the', 'to the', 'and the', 'for the', 'on the', 'at the', 'is the', 'it is', 'i use', 'i do', 'i have', 'i want', 'i tell', 'i ask', 'that is', 'this is', 'you can', 'does not', 'do not', 'ad copy', 'google ads', 'search terms', 'character limit']
        if any(phrase.startswith(s) or phrase.endswith(s) or phrase == s for s in skip):
            continue
        # Check if this phrase appears more than once
        count = text_clean.lower().count(phrase)
        if count >= 2 and phrase not in seen_phrases:
            # Check it's not a substring of an already-found longer phrase
            is_sub = any(phrase in p for p in seen_phrases if len(p) > len(phrase))
            if not is_sub:
                seen_phrases.add(phrase)
                found.append((count, phrase))

# Sort by length (longer = more significant) then by count
found.sort(key=lambda x: (-len(x[1].split()), -x[0]))
# Show top 10 most significant
for count, phrase in found[:10]:
    print(f'  [{count}x] \"{phrase}\"')
print(f'REPETITION COUNT: {len(found)}')
" 2>/dev/null)
echo "$REPEAT_RESULT"
REPEAT_COUNT=$(echo "$REPEAT_RESULT" | grep "REPETITION COUNT:" | grep -o "[0-9]*" || echo "0")
if [ "$REPEAT_COUNT" -gt 0 ] 2>/dev/null; then
  echo "⚠️  WARNING: $REPEAT_COUNT repeated phrase(s) found. Review each one. If the same distinctive phrase appears twice, rewrite one instance. Common phrases (google ads, ad copy, etc.) are excluded. Do not proceed until reviewed."
else
  echo "✅ PASS: No repeated phrases found."
fi

# CHECK 8b: NEAR-DUPLICATE PHRASES — catch "finding good media buyers" / "find good media buyers" style repeats
echo "Near-duplicate phrase check (stemmed words):"
NEARDUPE_RESULT=$(python3 -c "
import re

def stem(w):
    w = w.lower().strip('.,!?;:\"')
    # Simple suffix stripping to catch ing/ed/s/ly variants
    for suffix in ['ing', 'tion', 'ed', 'ly', 'ment', 'ness', 'able', 'ible']:
        if len(w) > len(suffix) + 3 and w.endswith(suffix):
            return w[:-len(suffix)]
    if w.endswith('s') and len(w) > 4 and not w.endswith('ss'):
        return w[:-1]
    return w

text = open('$ARTICLE_PATH').read()
text = text.split('## SEO Notes')[0] if '## SEO Notes' in text else text
text = re.sub(r'\`\`\`.*?\`\`\`', '', text, flags=re.DOTALL)
lines = [l.strip() for l in text.split('\n') if l.strip() and not l.startswith('#') and not l.startswith('!') and not l.startswith('|') and not l.startswith('**')]
# Get all sentences
all_sents = []
for line in lines:
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', line) if s.strip()]
    all_sents.extend(sents)

# For each pair of sentences, check if they share 3+ stemmed content words in same order
from collections import Counter
stop = {'the','a','an','is','are','was','were','be','been','being','have','has','had','do','does','did','will','would','shall','should','may','might','must','can','could','to','of','in','for','on','with','at','by','from','as','into','through','during','before','after','above','below','between','out','off','over','under','again','further','then','once','not','no','nor','but','or','yet','so','if','when','while','that','this','it','i','you','he','she','we','they','me','him','her','us','them','my','your','his','its','our','their','what','which','who','whom','how','all','each','every','both','few','more','most','other','some','such','than','too','very','just','also','and'}
fails = []
for i in range(len(all_sents)):
    words_i = [stem(w) for w in all_sents[i].split() if w.lower().strip('.,!?;:\"') not in stop and len(w) > 2]
    for j in range(i+1, min(i+8, len(all_sents))):  # check within 8 sentences
        words_j = [stem(w) for w in all_sents[j].split() if w.lower().strip('.,!?;:\"') not in stop and len(w) > 2]
        # Find shared stemmed words
        shared = set(words_i) & set(words_j)
        if len(shared) >= 3 and len(words_i) > 0 and len(words_j) > 0:
            ratio = len(shared) / min(len(words_i), len(words_j))
            if ratio >= 0.6:  # 60%+ overlap = near duplicate
                fails.append((all_sents[i][:80], all_sents[j][:80], shared))
for f in fails:
    print(f'  NEAR-DUPE:')
    print(f'    A: \"{f[0]}\"')
    print(f'    B: \"{f[1]}\"')
    print(f'    Shared stems: {f[2]}')
print(f'NEAR-DUPE COUNT: {len(fails)}')
" 2>/dev/null)
echo "$NEARDUPE_RESULT"
NEARDUPE_COUNT=$(echo "$NEARDUPE_RESULT" | grep "NEAR-DUPE COUNT:" | grep -o "[0-9]*" || echo "0")
if [ "$NEARDUPE_COUNT" -gt 0 ] 2>/dev/null; then
  echo "❌ FAIL: $NEARDUPE_COUNT near-duplicate sentence pair(s) found. These say the same thing in different words. Rewrite one of each pair. Do not proceed until fixed."
else
  echo "✅ PASS: No near-duplicate phrases found."
fi

# CHECK 9: BOLD LABEL SPACING — blank line required after every bold label
echo "Bold label spacing check:"
LABEL_RESULT=$(python3 -c "
import re
lines = open('$ARTICLE_PATH').readlines()
fails = []
for i, line in enumerate(lines):
    stripped = line.strip()
    # Match lines that are just a bold label (e.g. **Something:** or **Something.**)
    if re.match(r'^\*\*[^*]+\*\*$', stripped) or re.match(r'^-\s*\*\*[^*]+\*\*', stripped):
        # Check if next line is NOT blank
        if i + 1 < len(lines) and lines[i + 1].strip() != '':
            fails.append((i + 1, stripped, lines[i + 1].strip()[:80]))
for f in fails:
    print(f'  Line {f[0]}: {f[1]}')
    print(f'    Next line: {f[2]}')
print(f'LABEL SPACING FAILS: {len(fails)}')
" 2>/dev/null)
echo "$LABEL_RESULT"
LABEL_FAIL_COUNT=$(echo "$LABEL_RESULT" | grep "LABEL SPACING FAILS:" | grep -o "[0-9]*" || echo "0")
if [ "$LABEL_FAIL_COUNT" -gt 0 ] 2>/dev/null; then
  echo "❌ FAIL: $LABEL_FAIL_COUNT bold label(s) missing blank line after them. Add a blank line between every bold label and its body text. Do not proceed until fixed."
else
  echo "✅ PASS: All bold labels have blank lines after them."
fi

# CHECK 10: CONSECUTIVE SENTENCE-START REPETITION — never start 2+ sentences with the same word
echo "Consecutive sentence-start repetition check:"
CONSEC_RESULT=$(python3 -c "
import re
text = open('$ARTICLE_PATH').read()
# Strip frontmatter, code blocks, headings, images, SEO notes
text = text.split('## SEO Notes')[0] if '## SEO Notes' in text else text
text = re.sub(r'\`\`\`.*?\`\`\`', '', text, flags=re.DOTALL)
text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
lines = [l.strip() for l in text.split('\n') if l.strip() and not l.startswith('#') and not l.startswith('**') and not l.startswith('!') and not l.startswith('-') and not l.startswith('|')]
# Get all sentences in order
all_sentences = []
for line in lines:
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', line) if s.strip()]
    all_sentences.extend(sents)
# Check consecutive sentences starting with the same word
fails = []
for i in range(1, len(all_sentences)):
    word_a = all_sentences[i-1].split()[0].lower() if all_sentences[i-1].split() else ''
    word_b = all_sentences[i].split()[0].lower() if all_sentences[i].split() else ''
    # Skip common starters that naturally repeat: I, The, It, If, For, But, And
    skip_words = {'i', 'the', 'it', 'if', 'for', 'but', 'and', 'a', 'an', 'this', 'that'}
    if word_a == word_b and word_a not in skip_words and word_a:
        fails.append((word_a, all_sentences[i-1][:60], all_sentences[i][:60]))
for f in fails:
    print(f'  [{f[0].upper()}] \"{f[1]}...\"')
    print(f'         \"{f[2]}...\"')
print(f'CONSECUTIVE START FAILS: {len(fails)}')
" 2>/dev/null)
echo "$CONSEC_RESULT"
CONSEC_COUNT=$(echo "$CONSEC_RESULT" | grep "CONSECUTIVE START FAILS:" | grep -o "[0-9]*" || echo "0")
if [ "$CONSEC_COUNT" -gt 0 ] 2>/dev/null; then
  echo "❌ FAIL: $CONSEC_COUNT consecutive sentence(s) start with the same word. Rewrite one of each pair to start differently. 'Some X. Some Y. Some Z.' = three sentences starting with 'Some' = instant fail. Do not proceed until fixed."
else
  echo "✅ PASS: No consecutive sentence-start repetition found."
fi
```

**If Em dashes > 0:** Replace every `—` with a period, comma, or colon. Do not proceed until 0.

**If Banned phrases found:** Rewrite those sentences. Do not proceed until NONE.

**If CHECK 4 outputs ❌ FAIL:** Delete the floating paragraph. The first H2 IS the answer opener. Answer in 2-3 sentences below the H2, then the story. Do not proceed until the check outputs ✅ PASS.

**If CHECK 5 outputs ❌ FAIL:** Go back to Step 5c and add more questions from the PAA list. Do not proceed until the check outputs ✅ PASS with 10+.

**If CHECK 6 outputs ❌ FAIL:** Find every `---` line in the article and delete it. Sections are separated by H2 headings only. Do not proceed until check outputs ✅ PASS.

**If CHECK 7 outputs ❌ FAIL:** Find every paragraph with 4+ sentences. Split into 2-3 sentence blocks separated by a blank line. Rule: 2-3 sentences, blank line, next block. Never 4+ sentences in one block. Do not proceed until BLOB COUNT is 0.

**If CHECK 9 outputs ❌ FAIL:** Add a blank line after every bold label that's missing one. Bold label, blank line, body text. No exceptions.

**If CHECK 8 outputs ⚠️ WARNING:** Review each repeated phrase. If a distinctive phrase (not a common connector) appears twice, rewrite one instance so the same idea is said differently. Never repeat the same phrase in one paragraph. Never repeat the same distinctive phrase anywhere in the article. Do not proceed until reviewed and fixed.

### 7b: Manual Checks (After Bash Passes)

```
VOICE CHECK:
□ Two tequilas on Ibiza beach party tone?
□ 7-year-old can read every sentence?
□ Every H2 section has at least one "I" sentence or direct Virgil experience — no section is purely general advice?
□ Steps sound like a friend explaining, not an IKEA manual?
□ No section declares universal rules instead of Virgil's personal take?
□ Real names used (Victor, Vinod)?
□ Real numbers used (not vague)?
□ No educator/teacher voice?
□ No banned phrases? (Bash confirmed)
□ No repetition (said once, moved on)?
□ Story sourced from content-ideas.md (not memory)?

SEO CHECK:
□ Primary keyword in H1 and first paragraph?
□ Supporting keywords appear naturally in H2s and body?
□ Title tag ≤60 characters?
□ Meta description ≤155 characters?
□ FAQ section uses real questions from keyword research?
□ Internal link opportunities noted?
□ Schema types specified?
□ Word count hits target (±10%)?
□ QUESTION FIRST: first H2 is a question matching the article topic?
□ Answer to that question is 2-3 sentences directly below the H2 (before any story)?
□ Body H2s are statement hooks (not questions)? Questions only in FAQ section?

IMAGE CHECK:
□ 2 Plotly charts generated (Images 1 and 2)?
□ Charts use Sucana brand colors (purple + pink bars)?
□ No watermarks or logos in any image?
□ Alt text is descriptive and keyword-rich?
□ All placeholder references replaced with real image paths?
□ Charts approved by Virgil (HUMAN LOOP #4 cleared)?
□ Nanobanana cover image generated separately in Step 10 (not an in-article image)?

MANDATORY VISUAL QA — after generating EACH image, read it back using the Read tool and visually inspect:
□ Nothing clipped or cut off at any edge (left, right, top, bottom)?
□ All chart labels and values fully visible?
□ Text is readable — not too small, not overlapping?
□ Layout looks balanced — no large empty space on one side?
□ If any issue found: fix the code and regenerate BEFORE moving on.
DO NOT show a broken image to Virgil. Fix it first.

LLM CITATION CHECK:
□ LLM query target answered clearly?
□ Definitive, quotable paragraphs?
□ Entities clearly defined (Sucana, Virgil)?
□ Data points that LLMs would cite?
□ Structured formats used (lists, tables, steps)?

TRUTH CHECK:
□ Sucana is NOT fully launched yet
□ No invented stories or fake data
□ Only documented facts and real conversations
□ No claims about having thousands of users

IF ANY FAIL → FIX BEFORE SHOWING
```

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 8: Show Article for Review

**MANDATORY: Generate an HTML preview and open it in the browser.**

Generate a clean HTML file from the .md source (Inter font, 720px max-width, local image paths resolved, clean typography) and `open` it in the browser.

Do NOT output article content as markdown in chat. Do NOT use VS Code markdown preview. HTML in the browser is the only way Virgil reviews the article.

Include at the top:

```
ARTICLE #[number]: [Title]
Word Count: [actual] / [target]
Primary Keyword: [keyword] | Volume: [estimate] | Difficulty: [L/M/H]
Supporting Keywords: [list]
LLM Query Target: [query]
Ranking Strategy: [one sentence]
Images: [number] generated (Nanobanana, approved in Step 6)

✅ Em dash check: 0 (bash confirmed)
✅ Horizontal rule check: 0 (bash confirmed)
✅ Banned phrases: NONE (bash confirmed)
✅ Story source: content-ideas.md [story name/date]

[Full article content — every word]

**IMAGES — show as clickable links (computer:// format), one per line:**

[Image 1 — [description]](computer:///Users/virgilbrewster/My%20Drive/Sucana/Marketing/SEO/articles/images/[article-slug]-image-1.png)
[Image 2 — [description]](computer:///Users/virgilbrewster/My%20Drive/Sucana/Marketing/SEO/articles/images/[article-slug]-image-2.png)

RULE: Always show image links here. Never skip. Never describe. Just the clickable links.

Ready to approve? Or need edits?
```

🛑 **HUMAN LOOP #5:** DO NOT save yet. Wait for Virgil's approval. If edits needed, revise and show again.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 9: On Approval — Save Article + Update CSV + Tag Used Story

**Only after Virgil says "approved", "good", "save it", or similar:**

### Save the working article
Save to: `Marketing/SEO/articles/article-[##]-[slug].md`
- Article number padded to 2 digits (01, 02, 03...)
- Slug is lowercase, hyphens, from the title (max 6 words)

### Save the in-article images
Ensure all generated images are saved in: `Marketing/SEO/articles/images/`

### Update the Production System
In `Marketing/SEO/Article_Production_System.xlsx`, mark the article as "In Progress" (it's written but not yet deployed):

```bash
python3 -c "
import openpyxl
# REPLACE THESE VALUES before running:
article_number = 25        # actual article number (integer)
slug = 'my-article-slug'   # actual slug (no leading slash)

wb = openpyxl.load_workbook('/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/Article_Production_System.xlsx')
ws = wb['Article Production System']
for row in ws.iter_rows(min_row=2):
    if row[0].value == article_number:
        row[10].value = 'In Progress'            # Status column (K)
        row[11].value = '/blog/' + slug          # URL Slug column (L)
        break
wb.save('/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/Article_Production_System.xlsx')
print('Production System updated: In Progress')
"
```

### Tag the used story in content-ideas.md

Go to `Marketing/Research/content-ideas.md`. Find the story used in this article. Add this tag on the line immediately after the story:

```
<!-- USED IN: article-XX-slug -->
```

This is mandatory. No memory between sessions — the file is the only record. If you skip this, the same story will appear in the next article.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 10: Generate Hero Cover Image (Nano Banana 2.0)

**Every article gets a photorealistic hero cover image. Nano Banana MCP generates 3 variants — Virgil picks the best one.**

**NEVER SHOW SQUARE IMAGES IN THE PREVIEW. ONLY 16:9 RESIZED VERSIONS. IF THE GENERATION PRODUCES SQUARE IMAGES, CROP AND RESIZE TO 1200x675 BEFORE SHOWING ANYTHING TO VIRGIL. NO EXCEPTIONS.**

### 10a: Load the Schema

Read this file before building the prompt:
`/Users/virgilbrewster/My Drive/Sucana/Sucana Agents/Ad Image Generator/skills/ad-image.md`

This is the Nano Banana 2.0 pipeline. Use `mcp__plugin_creative_nano-banana__generate_image` MCP tool for generation. NEVER use generate.py for generation — generate.py is ONLY for local cropping/resizing. If the Nano Banana MCP tool is not available in the current session, fall back to generate.py with Gemini but ALWAYS resize to 16:9 before showing.

### 10b: Show Prompt Concepts for Approval

Before building the JSON or generating anything, propose **4 different scene concepts** in plain language. Each should be a distinct visual direction — vary the setting, lighting, and mood.

**CRITICAL RULE — Never illustrate the article literally.**
The image should capture the *feeling*, *tension*, or *outcome* of the article — not its subject matter. An article about AI automation is NOT a laptop with code on the screen. An article about finding hidden data could be an explorer in a cave. Think metaphor, not screenshot. The more unexpected the image, the more it stops the scroll. At least one option must be completely unexpected — something you'd never guess was connected to the article topic until you think about it.

```
HERO IMAGE CONCEPTS: Article #[number]

Option 1:
Scene: [2-3 sentences — objects, layout, lighting, mood]
Lighting: [color and direction]
Objects: [specific items or people]
Surface: [what they sit on]

Option 2:
Scene: [2-3 sentences — different setting or angle than Option 1]
Lighting: [color and direction]
Objects: [specific items or people]
Surface: [what they sit on]

Option 3:
Scene: [2-3 sentences — different mood or composition]
Lighting: [color and direction]
Objects: [specific items or people]
Surface: [what they sit on]

Option 4 (most unexpected):
Scene: [2-3 sentences — a completely lateral concept nobody would expect for this article]
Lighting: [color and direction]
Objects: [specific items or people]
Surface: [what they sit on]

Which one? (1, 2, 3, or 4 — or describe a different direction)
```

🛑 **HUMAN LOOP #6:** Wait for Virgil to pick a concept. If he wants changes, revise and show again. Only proceed to 10c after he picks one.

### 10c: Build the Hero Image JSON

Once the concept is approved, build the full JSON using the nano_banana_image.md schema.

**Blog Hero Image rules:**
- **Never literal.** Never show what the article is about — show the *feeling* of it. Metaphor over screenshot. A climber, not a spreadsheet. The more unexpected, the better.
- People-based cinematic scenes preferred — real agency/founder moments, not posed stock photos
- Lens: `35mm`, aperture `f/4.0`, shallow DOF
- Shot on Canon EOS R5. 8K ultra realistic, hyper realistic photorealism.
- Lighting color: derive from the article topic (cool blue for data/tech, warm amber for growth/success, neutral white for clean editorial — NOT always purple)
- `ad_format.platform`: `"Blog / Website"`
- `ad_format.ratio_and_resolution`: `"Landscape (16:9) 1920x1080"`
- `negative_prompt` MUST include: `"text"`, `"words"`, `"letters"`, `"numbers"`, `"writing"`, `"signage"`, `"watermarks"`, `"logos"`, `"bad anatomy"`, `"deformities"`, `"cartoon"`, `"illustration"`, `"3D render"`, `"CGI"`, `"rendered"`

Save JSON to:
`/Users/virgilbrewster/My Drive/Sucana/Sucana Agents/Ad Image Generator/prompts/blog/{slug}-cover.json`

### 10d: Generate 3 Variants Using Imagen 4.0 via generate.py

**Use the existing generate.py script. This is the same pipeline that made all 30+ blog post covers.**

```bash
cd "/Users/virgilbrewster/My Drive/Sucana (1)/Sucana/Sucana Agents/Ad Image Generator"
GEMINI_API_KEY="AIzaSyC1feU9aWztXcNzqy6nVsEigWweNdIE8L0" python3 scripts/generate.py prompts/blog/{slug}-cover.json --count 3 --open
```

This generates 3 variants saved to `images/blog/{slug}-cover_v1.png`, `_v2.png`, `_v3.png`.

**IMPORTANT: Imagen 4.0 generates square (1:1) images.** The aspect ratio map in generate.py does not natively produce 16:9 from a "Landscape (16:9)" JSON value. After generation, ALWAYS resize to 1200x675 (true 16:9):

```python
from PIL import Image
for i in [1,2,3]:
    img = Image.open(f'images/blog/{slug}-cover_v{i}.png')
    target_w, target_h = 1200, 675
    src_w, src_h = img.size
    new_h = int(src_w / (target_w / target_h))
    top = (src_h - new_h) // 2
    img = img.crop((0, top, src_w, top + new_h))
    img = img.resize((target_w, target_h), Image.LANCZOS)
    img.save(f'images/blog/{slug}-cover_v{i}_16x9.png', quality=95)
```

Use the `_16x9.png` versions for the preview and final cover. Never use the square versions as hero images. Never show Virgil the square versions in any preview. Only show 16:9 resized versions.

### 10e: Show All 3 Variants to Virgil

**⚠️ HARD RULE: After all 3 variants are generated, write an HTML preview file and open it in the browser. This is the ONLY reliable way Virgil sees the images. Do NOT skip this. Do NOT describe the images in text. OPEN THE HTML.**

After all 3 generate_image calls, note the 3 saved paths from the MCP outputs. Then run this Python to write and open the preview:

```bash
python3 << 'PYEOF'
slug = "{slug}"
article_number = {N}
path_v1 = "/Users/virgilbrewster/My Drive/Sucana/generated_imgs/{filename_v1}"
path_v2 = "/Users/virgilbrewster/My Drive/Sucana/generated_imgs/{filename_v2}"
path_v3 = "/Users/virgilbrewster/My Drive/Sucana/generated_imgs/{filename_v3}"

html = f"""<!DOCTYPE html>
<html><head><style>
body {{ background: #111; font-family: sans-serif; color: white; padding: 40px; }}
h1 {{ font-size: 18px; margin-bottom: 30px; color: #aaa; }}
.variant {{ margin-bottom: 50px; }}
.variant h2 {{ font-size: 14px; color: #888; margin-bottom: 10px; }}
img {{ width: 100%; max-width: 960px; border-radius: 8px; display: block; }}
</style></head><body>
<h1>Hero Cover Variants — Article #{article_number}</h1>
<div class="variant"><h2>Variant 1</h2><img src="{path_v1}"></div>
<div class="variant"><h2>Variant 2</h2><img src="{path_v2}"></div>
<div class="variant"><h2>Variant 3</h2><img src="{path_v3}"></div>
</body></html>"""

html_path = f"/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/preview-{slug}-covers.html"
with open(html_path, 'w') as f:
    f.write(html)
print(f"HTML written to: {html_path}")
PYEOF

open "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/preview-{slug}-covers.html"
```

Then output:
```
HERO COVER VARIANTS: Article #[number]
Preview opened in your browser — all 3 variants visible.

Which one? (1, 2, or 3 — or say regenerate for new variants)
```

🛑 **HUMAN LOOP #7:** Wait for Virgil to select a variant.

### 10e: Resize and Save

After Virgil selects a variant, resize to **1200 x 675 pixels** (true 16:9 — pure scale down, no crop):

```python
from PIL import Image

src = "/Users/virgilbrewster/My Drive/Sucana/Sucana Agents/Ad Image Generator/images/blog/{slug}-cover_v{N}.png"
dest = "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-cover.png"

img = Image.open(src)
# 1200x675 = true 16:9. Pure scale down, no crop. Never use 1200x630 — wrong ratio, clips heads.
img = img.resize((1200, 675), Image.LANCZOS)
img.save(dest, quality=95)
```

Saved to: `Marketing/SEO/articles/images/{slug}-cover.png`

### 10f: Previous Cover Scenes (never repeat)

- Article #7 (96 Hours): hourglass with purple sand on a clean white desk next to a closed laptop
- Article #8 (Data Silos): disconnected cables and ethernet cords scattered across a white desk with isolated data screens glowing
- Article #9 (Client Churn): messy desk with multiple open laptops showing dashboards, scattered reports, half-empty coffee cups
- Article #10 (Make.com): glowing app icons on a white desk connected with light trails showing automation flow

Each new article gets a DIFFERENT scene. Update this list after each article is deployed.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 11: Final Confirmation Before Deploy

```
READY TO DEPLOY: Article #[number]

Article: [Title]
Cover: {slug}-cover.png (Nanobanana)
Images: {slug}-image-1.png, {slug}-image-2.png[, {slug}-image-3.png]
Slug: sucana.ai/blog/{slug}
Category: [category]
Tags: [tags]

This will convert to MDX, push to GitHub (article + cover + all images), and go live on sucana.ai/blog.

Deploy now?
```

🛑 **HUMAN LOOP #7:** Wait for Virgil's go-ahead. Nothing gets pushed until he confirms.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 12: Convert to MDX + Deploy to GitHub

**Only after Virgil confirms deploy in Step 11.**

### 12a: Generate the MDX file

```yaml
---
title: "Your Post Title Here"
excerpt: "A 1-2 sentence summary (120-160 chars). Factual, not marketing copy."
date: "YYYY-MM-DD"
lastModified: "YYYY-MM-DD"
tags: ["tag1", "tag2", "tag3"]
category: "category-slug"
coverImage: "/images/blog/{slug}-cover.png"
readingTime: "X min read"
author: "Virgil Brewster"
featured: false
---
```

Use the category and tags for the article's pillar (see pillar defaults in Step 1). Set `date` and `lastModified` both to today's date.

**MDX body rules:**
- Strip the SEO Frontmatter block — stays in local .md file only
- Strip the SEO Notes section — stays in local .md file only
- Keep all H2/H3 headings, body content, FAQ section
- Keep all image references — update paths to deployed format

### 12b: Clone repo and deploy

Read `Marketing/SEO/BLOG-INSTRUCTIONS.md` at runtime for the GitHub PAT and exact git commands.

```bash
# Clone only if not already cloned
if [ ! -d "/tmp/www.sucana.ai" ]; then
  git clone https://[PAT]@github.com/vinodsharma10x/www.sucana.ai.git /tmp/www.sucana.ai
fi
cd /tmp/www.sucana.ai
git pull origin main
git config user.name "vinodsharma10x"
git config user.email "vinod@vinodsharma.co"

# Copy MDX file into the repo
cp "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/article-[##]-{slug}.mdx" "content/blog/{slug}.mdx"

# Copy images into the repo
cp "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-cover.png" "public/images/blog/{slug}-cover.png"
cp "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-1.png" "public/images/blog/{slug}-image-1.png"
cp "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-2.png" "public/images/blog/{slug}-image-2.png"
# image-3 is optional — only copy/add if it exists
[ -f "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-3.png" ] && \
  cp "/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/articles/images/{slug}-image-3.png" "public/images/blog/{slug}-image-3.png"

git add content/blog/{slug}.mdx
git add public/images/blog/{slug}-cover.png
git add public/images/blog/{slug}-image-1.png
git add public/images/blog/{slug}-image-2.png
[ -f "public/images/blog/{slug}-image-3.png" ] && git add public/images/blog/{slug}-image-3.png

git commit -m "Add blog post: {Post Title}

- New blog post: content/blog/{slug}.mdx
- Cover image: public/images/blog/{slug}-cover.png

Authored-By: Virgil"
git push origin main
```

**Rules:** Push directly to `main`. Do NOT create branches. Do NOT modify existing files.

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 13: Verify Deployment + Update Production System

1. Wait ~60 seconds for Vercel to deploy
2. Open the live article in Chrome: `open -a "Google Chrome" "https://sucana.ai/blog/{slug}"`
3. Confirm cover image loads
4. Confirm in-article images load

Once confirmed live, update the Production System to "Published":

```bash
python3 -c "
import openpyxl
from datetime import date
# REPLACE THIS VALUE before running:
article_number = 25   # actual article number (integer)

wb = openpyxl.load_workbook('/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/Article_Production_System.xlsx')
ws = wb['Article Production System']
for row in ws.iter_rows(min_row=2):
    if row[0].value == article_number:
        row[10].value = 'Published'           # Status column (K)
        row[12].value = str(date.today())     # Publish Date column (M)
        break
wb.save('/Users/virgilbrewster/My Drive/Sucana/Marketing/SEO/Article_Production_System.xlsx')
print('Production System updated: Published', date.today())
"
```

```
✅ DEPLOYED: https://sucana.ai/blog/{slug}
Article #[number] is live. Production System updated.

Live article: [Article Title](https://sucana.ai/blog/{slug})
```

**AUTO-TRIGGER: Immediately after confirming deployment, launch Step 15 (Internal Linking) as a background agent. Do not wait for Virgil to ask. Internal linking runs automatically after every deploy, no exceptions.**

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 14: Distribution Assets

1. **LinkedIn teaser post** — 100-150 words, hook from article's most compelling insight
2. **Email snippet** — 2-3 sentences for newsletter inclusion

Show both in chat for review. Do NOT auto-save.

---

## Pipeline Summary

```
Step 1:   Load context + read SEO_GEO_Playbook.md + find next article  → 🛑 HUMAN LOOP #1
Step 2:   3 parallel agents (topic research + Reddit sentiment + keyword/story/style)
          → Compile unified brief                                       → 🛑 HUMAN LOOP #2
Step 3:   Load voice (Virgil_Voice_MASTER.md) — already loaded by Agent 3
Step 4:   Story already selected by Agent 3 — confirm fit
Step 5a:  Write opening H2 + answer only — stop and confirm
Step 5b:  Write full article body (with image placeholders)
Step 5c:  Write FAQ (10 questions minimum)
Step 5.5: Structure checkpoint — H1, first H2, angle                   → 🛑 HUMAN LOOP #3
Step 5.6: Full Review Agent (voice + quality + last article comparison) → Must PASS before continuing
Step 6:   Generate 2 Plotly charts                                      → 🛑 HUMAN LOOP #4
Step 7:   Self-check — BASH COMMANDS ON FILE, show output, fix failures before Step 8
Step 8:   Show FULL article for review                                  → 🛑 HUMAN LOOP #5
Step 9:   Save article + mark In Progress in XLSX + tag used story
Step 10:  Generate hero cover image (Nanobanana, 3 variants)            → 🛑 HUMAN LOOP #6
Step 11:  Final deploy confirmation                                     → 🛑 HUMAN LOOP #7
Step 12:  Convert to MDX + copy files + push to GitHub
Step 13:  Verify deployment + mark Published in XLSX
Step 14:  Distribution assets (LinkedIn + email)
Step 15:  Internal linking (outbound + inbound + pillar) — self-test, no approval needed
```

---

> ⚠️ **STICK TO THE TEMPLATE.** Read `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/TEMPLATE.md`. No deviation. No urgency permits skipping. Run the Step Verifier agent after this step completes.

## Step 15: Internal Linking (Post-Publish)

After the article is live on sucana.ai, run internal linking. This is NOT optional. Every article must be cross-linked.

### 15a: Outbound links (new article → existing articles)

Scan the new article body for 3-5 places it should link to existing published articles.

Rules:
- Use descriptive anchor text (never "click here" or "this article")
- Max 1 internal link per paragraph
- Prefer linking in the first 60% of the article body
- Never link inside FAQ answer sections
- Never link to the same target article twice

### 15b: Inbound links (existing articles → new article)

Scan ALL existing published articles at `/tmp/www.sucana.ai/content/blog/`. Find 3-5 articles that should link TO the new article. For each, find a natural sentence where the link adds genuine value.

### 15c: Pillar page linking (MANDATORY)

Identify which pillar the new article belongs to based on its tags and topic:

| Pillar | Slug | Status |
|--------|------|--------|
| P1 — AI for Performance Marketing | /blog/ai-performance-marketing-pillar | Published |
| P2 — AI Workflows for Marketers | TBD | Not yet published |
| P3 — AI-Powered Marketing Org | TBD | Not yet published |
| P4 — Experiments and Results | TBD | Not yet published |

If the pillar page exists:
1. Add a link FROM the new article TO its pillar page (find a natural place in the body)
2. Add a link FROM the pillar page TO the new article (add the new article to the pillar's cluster list)

Pillar links get priority over sibling article links. Every cluster article MUST link to its pillar page.

### 15d: Show suggestions and apply

Present ALL link suggestions using this format:

```
INTERNAL LINKS — New article: "[Title]" (/blog/[slug])

OUTBOUND (this article → others):
Link 1:
  Current sentence: "[exact sentence]"
  Updated sentence: "[sentence with [anchor text](/blog/target)]"
  Links to: /blog/[target] — "[Title]"

INBOUND (others → this article):
Link 1:
  Article: "[Source Title]" (/blog/[source-slug])
  Current sentence: "[exact sentence]"
  Updated sentence: "[sentence with [anchor text](/blog/new-slug)]"

PILLAR LINKS:
  New article → pillar: [sentence with link]
  Pillar → new article: [where in pillar page to add link]
```

**No approval needed for internal links.** Use your own judgment. Apply the links, then self-test:
1. Does each link make sense in context?
2. Is it relevant for SEO?
3. Is the article over-linked? (3-5 links for a 2000-word article is clean. Don't link stuff just to link it.)

After self-test passes:
1. Edit the MDX files at `/tmp/www.sucana.ai/content/blog/`
2. Verify all links render correctly (no broken markdown)
3. Commit with message: "Add internal links for /blog/[slug]"
4. Push to main
5. Report summary: articles updated, links added, total link count

---

## Important Rules

1. **One article at a time.** Complete the full pipeline before moving to the next.
2. **Never skip the CSV check.** Always verify which article is next by Priority Rank.
3. **Never skip keyword research.** Every article gets validated keywords before writing.
4. **Never save without approval.** Always show in chat first.
5. **Never invent stories.** Source every story from content-ideas.md. Check USED IN tags. Stay close to the raw notes — do not expand into invented scenes or dialogue.
6. **Voice comes from Virgil_Voice_MASTER.md.** Read it in full in Step 3. Located at `Soul/Virgil_Voice/Virgil_Voice_MASTER.md`. Do NOT use FINAL or COMPLETE versions.
7. **Subtle dialogue touches (Eddie Shleyner's realism technique).** Use real conversations between Virgil, Victor, and Vinod at about 10% of the article. Not throughout. Subtle. Three rules:
   - **Only facts, actions, and dialogue.** Never write "I felt frustrated." Show the conversation that reveals it.
   - **Strategic sparseness.** Do not over-explain. Let gaps exist so the reader fills them in.
   - **10% rule.** Place dialogue in the opening (to set up the problem), one key moment in the middle (a question that changes direction), and the closing (a reaction to the result). The steps themselves stay clean and action-focused. Do NOT turn every step into a conversation. That overdoes it.
   Example: Victor asked me: "How do we know who signed up from the blog versus LinkedIn?" I had not thought about that.
8. **Dual optimize everything.** Every article serves both Google AND LLMs.
8. **Update the CSV after every article.**
9. **Hero image from Nanobanana.** Generate 3 variants in Step 10, Virgil picks one.
10. **Deploy to GitHub.** Every approved article gets pushed to main.
11. **6 human loops.** Brief, keywords, images, article, cover image, deploy. Never skip any.
12. **Every article gets exactly 2 in-article images + 1 cover.** Image 1 + Image 2 = Plotly charts (Sucana brand colors, purple + pink). Cover = Nanobanana hero image (Step 10, separate from in-article images). No matplotlib. No Nanobanana for in-article charts.
13. **Nanobanana Blog Hero Image JSON schema is sacred.** Use the structure from nano_banana_image.md for cover images.
14. **All images deploy with the article.** One commit, everything together.
15. **Self-check is bash commands, not mental.** Run grep on the file. Show the output. Zero em dashes. Non-negotiable.
16. **Tag used stories.** After every save, add `<!-- USED IN: article-XX-slug -->` to the used story in content-ideas.md. This is the only memory between sessions.
17. **Question H2 comes first. Always.** The very first thing after frontmatter is an H2 question. Answer it in 2-3 sentences. Then story. Then rest of article. Never put a floating paragraph before the first H2. No exceptions.
18. **FAQ is 10 questions minimum.** The bash check counts `### ` headers inside the `## Frequently Asked Questions` section only — must be 10+. If CHECK 5 outputs ❌ FAIL, go back to Step 5c and add more questions before proceeding.
19. **No purple accent bar on charts.** Removed per Virgil's preference (Article #1). Do not add it back.
20. **Section dividers `---` are banned from article body.** Use H2/H3 headings only for section breaks. CHECK 6 hard-fails on any `---` line found.
21. **This file is the source of truth.** Located at `Marketing/SEO/SKILL.md`. After any edit, repackage using the skill-creator to sync the installed version.

---

## 📊 REDDIT PAIN POINTS RESOURCE (Optional — Agency Intelligence)

**This is optional. Only use if Virgil asks, or if the article topic is closely tied to agency pain points and you want extra signal.**

If needed, check the latest Reddit scrape at: `{SUCANA}/automations/Reddit-Monitoring/latest-scrape.csv`

**What it is:** Real posts from r/PPC, r/FacebookAds, r/analytics, r/smallbusiness, r/adops, r/ecommerce, and related subreddits. Updated automatically.

**How to use it (when you do use it):**
- Scan the **Title** and **Content** columns for current agency pain points
- Use the exact language agencies use — not marketing speak
- Look for recurring frustrations, trending problems, and specific vocabulary

**Rules:** Do NOT quote posts verbatim. Do NOT name specific Reddit users. Use as live market research only.
