---
name: sucana-seo
description: "Sucana SEO — SEO article production pipeline for Sucana. MANDATORY triggers on: SEO, seo, write article, next article, SEO article, seo article, start article, article pipeline. Reads SEO strategy research, finds the next unwritten article from the Production System CSV, runs keyword research to validate and enrich targeting before writing, loads Virgil's voice via the Writer skill, searches Fireflies transcripts for real stories, writes the full article dual-optimized for Google AND LLM citation, generates 2 Plotly charts (brand colors) per article, generates a photorealistic hero cover image via Nanobanana (3 variants, Virgil picks one), shows for review, and on approval converts to MDX, pushes to GitHub, and Vercel auto-deploys to sucana.ai/blog. Complete end-to-end SEO content production system."
---

# SEO Article Production Pipeline

Write SEO articles for Sucana in Virgil's voice, dual-optimized for Google ranking AND LLM citation. Full pipeline from brief to live on sucana.ai/blog.

This skill manages the full pipeline from brief to published article, tracking progress across 100 planned articles.

---

## Step 1: Load SEO Strategy Context

**Content Strategy (no file read — pillars are here):**

- **Pillar 1 — AI tools and workflows for marketers:** Real tool reviews, automations built, workflows tested. Always first-person: "I used this to do X, here's what happened."
- **Pillar 2 — Performance marketing meets AI:** How AI changes running ads, building audiences, optimizing spend. Real campaign data, real before-and-afters.
- **Pillar 3 — Building an AI-powered business:** The Sucana story. Decisions, mistakes, wins. For the founder/agency-owner types who want to understand how AI products are made.
- **Pillar 4 — The future of marketing work:** How AI reshapes teams, roles, hiring, and economics. What does the marketing team of 2027 look like?
- **Pillar 5 — Experiments and results from Sucana Lab:** Documentary content. We tried something, here's what happened. No theory — just results.

90% education and value across pillars. 10% Sucana-specific (and even that is story, not pitch).

**Read this file:**

1. **Production System:** `Marketing/SEO/Article_Production_System.xlsx`
   - Find the NEXT article to write: filter for Status = "Not Started", pick row #1 (lowest # = highest priority)
   - Extract the full brief: Topic/Question, Primary Keyword, Pillar, Source, Demand, Difficulty, Opportunity, Format

2. **Detect how-to articles (automatic, no user input needed):**

   Check if this article should use the how-to-draft format instead of the standard article flow:

   **Signal 1 — Format column:** If the Format field from the CSV matches any of these, flag as how-to: `How-to guide`, `Tutorial`, `Step-by-step`, `Workflow walkthrough`, `SOP-style workflow`, `Step-by-step guide`, `Step-by-step tutorial`, `Step-by-step with examples`, `Workflow article`

   **Signal 2 — Title:** If the title contains "How to", "How I", "How We", "Guide to", "Steps to", or "Build a" AND the topic involves a tool, skill, or workflow being built, flag as how-to.

   If flagged as how-to, scan for an existing how-to-draft source file:
   - Search `Marketing/Newsletter/Content/how-we-built-*.md` for a file matching the article topic
   - Search `Virgil Second Brain/Content/Blog Content/how-we-built-*.md` for a file matching the article topic
   - If found, store the path as `HOW_TO_SOURCE_DRAFT`

   Set the article path:
   - If how-to + draft found: `Article Path: How-To (source draft at [path])`
   - If how-to + no draft: `Article Path: How-To (from scratch)`
   - If not how-to: `Article Path: Standard`

3. **Show the brief to Virgil** before writing:
   ```
   NEXT ARTICLE: #[number]
   Title: [title]
   Type: [article type] | Pillar: [pillar]
   Article Path: [How-To (source draft at path) / How-To (from scratch) / Standard]
   Google Keyword: [keyword]
   LLM Query Target: [query]
   Word Count: [target]
   Google Intent: [intent type]
   LLM Citation Goal: [citation goal]
   Schema: [schema type]

   Ready to write?
   ```

🛑 **HUMAN LOOP #1:** Wait for Virgil's confirmation before proceeding.

---

## Step 2: Keyword Research & Validation

**Before writing a single word, validate and enrich the keywords for the article.**

The CSV has a keyword assigned, but real data is needed to confirm it's the right target. This step answers three questions: What exactly are we targeting? Why this keyword? How do we expect to rank?

### 2-FIRST: Check Existing Keyword Research

**BEFORE doing any live research, check if keyword research already exists:**

- Read `Marketing/SEO/keyword-research.md` — 40 keywords across 4 pillars, top 15 priority targets with demand/difficulty signals

If the article already has validated keyword research in these files:
- Extract the findings (volume, difficulty, supporting keywords, questions, ranking strategy)
- Show the keyword brief to Virgil (skip to Step 2d)
- Only do live research if Virgil wants to re-validate or update

If no existing research found, proceed with live research below.

### 2a: Research the Primary Keyword

Use web search to gather real data on the CSV's assigned keyword:

1. **Search volume** — How many people search this monthly? Use keyword research tools and searches like `[keyword] search volume 2026` to find estimates.
2. **Keyword difficulty** — How hard is it to rank? Check who currently owns page 1 — are they huge sites with massive authority, or smaller players we can beat?
3. **SERP analysis** — What type of content currently ranks? (listicles, guides, tool pages, forums, thin content?) This tells us what Google thinks searchers want.
4. **Content gap** — What are the top results missing? This is our angle in. If everyone writes generic overviews and nobody shares real data or founder experience, that's the gap we fill.

Search queries to run:
- `[keyword]` — see what actually ranks on page 1
- `[keyword] search volume keyword difficulty` — find volume estimates
- `[keyword] site:reddit.com` or `site:quora.com` — find real questions people ask about this topic
- Related searches and "People Also Ask" — find the long-tail variations

### 2b: Find Supporting Keywords

Every article needs a primary keyword plus 3-5 supporting long-tail keywords. These go naturally into H2s, body text, and FAQ answers. Search for:

- **Long-tail variations** — longer, more specific versions of the primary keyword
- **Related questions** — "People Also Ask" style queries that real people type into Google
- **LSI keywords** — semantically related terms Google expects to see in comprehensive content about this topic

### 2c: Validate or Adjust

Based on the research, make a call:

- **KEEP** the CSV keyword if search volume exists and the competition is beatable
- **ADJUST** if a better variation has more volume or lower competition — update the CSV with the better keyword
- **ADD** supporting keywords that should appear naturally throughout the article

### 2d: Show the Keyword Brief to Virgil

Present findings before proceeding:

```
KEYWORD RESEARCH: Article #[number]

PRIMARY KEYWORD: [keyword]
Search Volume: [monthly estimate]
Difficulty: [Low/Medium/High] — [one sentence on why]
Current Page 1: [2-3 bullet summary of who ranks and what they wrote]
Our Edge: [one sentence — why we beat them]

SUPPORTING KEYWORDS (weave naturally into article):
1. [long-tail keyword] — [volume estimate if available]
2. [long-tail keyword] — [volume estimate if available]
3. [long-tail keyword] — [volume estimate if available]

QUESTIONS PEOPLE ASK (use in FAQ section):
1. [question from PAA or Reddit/Quora]
2. [question]
3. [question]
4. [question]
5. [question]

RANKING STRATEGY: [2-3 sentences explaining HOW we rank]

Proceed with writing?
```

🛑 **HUMAN LOOP #2:** Wait for Virgil's confirmation. If he wants keyword changes, adjust before moving on.

### 2e: Update the CSV

After keyword validation is confirmed, update the article's row in `Marketing/SEO/Article_Production_System.xlsx`:
- Update the primary keyword if it changed
- Add validated supporting keywords to the "Supporting Keywords" column
- Add a one-line ranking strategy note to the "Ranking Strategy" column

### 2f: Research Competing Articles + Reddit Angle Validation

**This step is mandatory and happens BEFORE choosing the article angle or writing a single word.**

**Step 1: Research what's already ranking**

Search the primary keyword and read the top 5-7 results. For each one, note:
- What angle did they take?
- What problem did they claim to solve?
- What did they miss or get wrong?
- Is there a gap nobody has filled?

**Step 2: Go to Reddit and find real pain**

Search Reddit for the topic and keyword. Look for:
- Real frustration people are expressing
- Real questions they cannot find answers to
- Real mistakes they are making repeatedly

**Step 3: Pick ONE real problem**

From the Reddit research, identify the single most common, most urgent, most specific real problem. That problem becomes the article's one through-line.

**Show Virgil the angle before writing:**

```
ARTICLE ANGLE: Article #[number]

Competing articles cover: [1-2 sentences]
Gap identified: [what nobody has answered yet]

Reddit problem found: [quote or paraphrase]
Source: [reddit thread URL or search terms used]

ONE THROUGH-LINE: This article solves the problem of [one sentence].

Proceed with writing?
```

🛑 **HUMAN LOOP #2b:** Wait for Virgil to confirm the angle before writing.

---

## Step 2.5: Load How-To Source Draft (CONDITIONAL)

**Only run this step if the article was flagged as how-to in Step 1.** If Article Path = "Standard", skip to Step 3.

### If a source draft exists (Article Path = "How-To (source draft at [path])"):

1. Read the how-to-draft .md file from the path detected in Step 1
2. Extract every stage: count them, list the stage titles
3. For each stage, extract:
   - The prompt (what the user typed into Claude)
   - The result (what came back)
   - The test (what was checked and what was found)
   - The "why" (one sentence)
   - Any direction changes
4. If a PRODUCT.md exists in the same skill folder, read it and cross-reference: every feature in the PRODUCT.md should map to a stage in the draft
5. Show in chat:
   ```
   HOW-TO SOURCE DRAFT LOADED
   File: [path]
   Stages found: X
   PRODUCT.md: [found at path / not found]
   Features covered: Y/Z (if PRODUCT.md exists)
   ```

### If no source draft exists (Article Path = "How-To (from scratch)"):

1. Show in chat: "No existing how-to draft found. Will write the how-to sections from scratch using the how-to-draft format."
2. The how-to format rules from Step 5b (Pattern 8: How-To) will guide the writing. No source material needed.

---

## Step 3: Load Virgil's Voice

**Read the voice profile:**

- **Virgil_Voice_MASTER.md** at `Soul/Virgil_Voice/Virgil_Voice_MASTER.md` — read in full. This is the single authoritative voice file (596 lines). Contains complete voice context, Long-Form Voice Rules, People rules, and fresh story requirement. Do NOT read FINAL or COMPLETE.
- **Virgil_Writing_Examples.md** at `Soul/Virgil_Voice/Blog Writing Examples.md` — read in full. Real writing samples from Virgil showing the voice in practice. Study the rhythm, the one-line punches, the cultural references, the vulnerability, and the concrete details. The MASTER file tells you the rules. This file shows you what the voice sounds like.

**Key voice rules for long-form SEO articles:**
- First-person narrative throughout — "I" not "we" (except "Victor and I", "Vinod and I")
- Real stories, real names, real numbers — never invent
- Plain language a 7-year-old can read
- Say it once, move on — no repetition
- Conversational tone, not textbook
- Compression over long-winded explanations

**BANNED PHRASES (from Writer skill):**
- "Here's the thing"
- "Here's why/how/what"
- "This is where [X] gets made"
- "That's the edge"
- "You need to" / "You should"
- "Most people don't realize"
- Complex words a 7-year-old wouldn't understand
- Repeating the same idea multiple times

---

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

## Step 5: Write the Article

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

### Step 5a: Write ONLY the Opening — Stop Here

**This sub-step is its own moment. Do not write anything else until this is shown.**

Write exactly this sequence:

1. The H2 question (the exact question the article answers) — SEO anchor, comes first
2. Result sentence — 1 line, a real number or outcome from Sucana, Victor's agency, or our work. No generic claims. No invented stats.
3. Story bridge — 2-3 sentences from our perspective (Sucana, Victor, Vinod, or a real client situation). The before. What was broken or hard. How the thing we're about to explain changed it.
4. Transition line — "Here's exactly what we did." or equivalent. One sentence. Leads into the steps.

Then **stop**. Show just this to confirm the opening is right before writing the full article.

**CORRECT:**
```
## What Are the Best ChatGPT Prompts for PPC Managers?

Victor's team cut campaign review time from 3 hours to 20 minutes with one prompt change.

They were asking ChatGPT generic questions and getting generic answers back. The fix was feeding it actual client data first — spend, ROAS, campaign history, what the client keeps complaining about. Once the context was in, the answers became useful.

Here's exactly what changed.
```

**WRONG:**
```
To get useful answers from ChatGPT as a PPC manager...  ← floating paragraph before any H2

## Why Most Prompts Don't Work  ← question buried, came second
```

**ALSO WRONG:**
```
## What Are the Best ChatGPT Prompts for PPC Managers?

The best ones start with your client's actual data, not a generic question.  ← generic advice, no proof
```

Rules:
- H2 question comes first. Before any paragraph. Before anything.
- Result sentence is always from our world — Sucana, Victor, Vinod, a real campaign, a real number.
- Story bridge is always first-person, always from our perspective. Never generic "many agencies find..."
- Transition line leads into the steps. Short. One sentence.
- All other H2s in the body can be statements or questions — does not matter.
- Only this first H2 must be the question that matches the article's intent.

🛑 **Show the opening H2 + result + story + transition. Wait for confirmation before proceeding to Step 5b.**

---

### Step 5b: Write the Full Article Body

After opening is confirmed, write the full article hitting the word count target from the CSV.

**Start with** the confirmed opening H2 + answer from Step 5a, then add the story, then the full body.

**Do NOT write the "in practice" section or FAQ in this step — those are Steps 5c and 5d.**

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

1. **Question H2 first**: The very first H2 is a question that directly matches the article's topic. Directly below it: result sentence (real number/outcome from our world), story bridge (2-3 sentences from Sucana/Victor/Vinod perspective), transition line. This IS the answer — just delivered through proof and story, not generic advice. The story is part of the opening, not a section that comes after it.

2. **Question-based H2 headings**: Use headings that mirror natural language queries.
   - Good: `## How Much Does a PPC Dashboard Cost?`
   - Bad: `## Pricing Information`

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

Structure depends on article type:

**Founder Story articles:** Personal narrative, origin stories, real moments, vulnerability + insight
**Pillar Page articles:** Comprehensive guides, definitive resource, heavy on value, structured with clear H2/H3 sections
**Problem Articles:** Pain point → real examples → why it happens → what to do about it
**Data Articles:** Research-backed, statistics, benchmarks, tables, with Sucana's perspective woven in
**Comparison articles:** Fair analysis, pros/cons, clear recommendation, honest about where Sucana fits
**Tutorial articles:** Walk them through it like a friend, not an IKEA manual. Steps sound like "The first thing I look for is X" — not "Step 1: Do X." Practical and actionable, but always in Virgil's first-person voice. Every step ends with proof it worked: a real number, a real outcome, a one-line result from Sucana or Victor's agency. No step is advice-only.
**Trend Articles:** Current data, what's changing, what it means for agencies, Sucana's take
**How-To articles (uses how-to-draft format):** Only applies when Article Path = "How-To" from Step 1. Uses the rigorous stage format from the how-to-draft skill. Each section of the article maps from a how-to-draft stage:

| How-to-draft stage element | SEO article translation |
|---|---|
| **Do this:** Type: "[prompt]" | Conversational intro + prompt in a code block. "Open Claude Code and tell it..." or "I typed this into Claude:" followed by the prompt in a copyable code block. |
| **What happens:** | Woven into the narrative after the code block: "Claude came back with..." or "What I got back was..." Max 2 sentences. |
| **We tested this by:** | Becomes the proof paragraph. Real numbers, real outcomes, real fixes. "I checked the output and found 7 story angles. Two taught the same lesson so I told Claude to keep the stronger one." This is what makes the article credible. |
| **Why we did this:** | One-line punch that closes the section. Standalone line. |
| Direction changes ("Then we said:") | The most valuable content. "That didn't work. The action items were pulling priorities as tasks. So I told Claude to add a filter: can someone check this off by end of week? If no, it's not an action item." |

**How-To additional rules:**

1. **Every prompt is copyable.** The reader copies the exact text from the code block into Claude Code and gets the same result.

2. **"Before You Start" section is mandatory.** List everything the reader needs: Claude account, API keys, tools, files. Keep it short.

3. **Jargon gets explained on first mention.** Use this list (explain each term the FIRST time it appears, never repeat):

   - **.env file** — "A file that stores your passwords and API keys. It stays on your computer and never gets shared."
   - **PRODUCT.md** — "Your project's memory. Documents what you built, what decisions you made, and where everything lives."
   - **SKILL.md** — "The instruction file that tells Claude what to do. Think of it as a recipe card."
   - **GitHub** — "Where we store finished code so anyone can download it. A public folder on the internet."
   - **API** — "How two tools talk to each other. When we say 'Beehiiv API,' it means Claude can look up subscribers without you logging in."
   - **Next.js** — "The tool that builds the website. The engine behind the page."
   - **Vercel** — "The service that puts the website on the internet. Push a file, Vercel updates the site automatically."
   - **MCP** — "How Claude connects to external tools. Like plugging in a cable between Claude and another app."
   - **CTA** — "Call to Action. The line that tells people what to do next."
   - **Funnel** — "Shows how people move through stages. Each stage has fewer people than the one before."
   - **CSV** — "A spreadsheet file. When you export data from a tool, it downloads as a CSV."
   - **API route** — "A small piece of code on the website that runs when someone clicks a button."
   - **Guardrails** — "Writing rules. Banned words and patterns that make content sound like AI wrote it."
   - **PRD** — "The plan. What we're building, why, and in what order."

   This list grows. When the checker flags an unexplained term, add it here permanently.

4. **Two mandatory sections in every how-to article:**
   - Early: a section about creating the PRODUCT.md ("Before we kept building, we saved what we had so far")
   - Last section before "What We'd Do Differently": updating the PRODUCT.md ("When we come back to this project, this file tells us everything")

5. **If a source draft exists (from Step 2.5):** Use every stage from the draft. Do not skip stages. Do not summarize. Every stage in the draft becomes a section in the article. If the draft has 14 stages, the article has 14 how-to sections.

6. **If no source draft:** Write the how-to sections from scratch using the same format. Each section still needs: conversational prompt intro, code block, result narrative, proof paragraph, one-line punch.

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

### Step 5c: Write the "What This Looks Like in Practice" Section — MANDATORY

**This section is mandatory in every article. It comes immediately before the FAQ.**

Write a before/after story using a real person from our world: Victor, Vinod, a Sucana beta tester, or a real client situation. Never invent. Source the story from content-ideas.md (Step 4 rules apply).

Structure:
- Before: What their situation looked like before. Specific. Named. Real hours, real cost, real frustration.
- After: What changed. Same specificity — hours saved, cost cut, results improved.
- One punch line at the end that connects back to the article's main point.

Format as flowing prose, not a comparison table. 150-250 words. First-person ("Victor runs a lead gen agency. Before we built this...").

**CORRECT:**
```
## What This Looks Like in Practice

Victor runs a lead gen agency. His Monday used to end at noon before he'd touched a single campaign.

Seven to eleven every week: pulling Meta data, Google data, CRM exports, building the deck, writing the summary email. Same work, same format, same four hours. Every Monday.

We built the reporting workflow in one afternoon. It runs automatically now. Victor spends 20 minutes reviewing it instead of building it.

That's the difference between a workflow that exists and one that doesn't.
```

🛑 **Write this section, then move to FAQ.**

---

### Step 5d: Write the FAQ — Dedicated Sub-Step

**This is its own moment. Treat it like generating images — a separate, deliberate action, not a footnote.**

**The "in practice" section (Step 5c) must be written before starting this.**

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

## Step 5b: Structure Checkpoint

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

## Step 5c: Voice Check — Before Images

**This is a mandatory stop. Do not generate images until this clears.**

Read two body sections (not the intro, not the FAQ — two sections from the middle of the article). Ask yourself:

1. Does every section contain at least one sentence starting with "I" or a direct Virgil experience? If two consecutive sections have no "I" — stop. Rewrite before continuing.
2. Do the steps read like a friend walking someone through it, or like an IKEA manual? If IKEA manual — stop. Rewrite.
3. Does any section declare things as universal rules ("The right tool is X", "The best approach is Y") instead of Virgil's personal take ("I use X", "What worked for me is Y")? If yes — stop. Rewrite.

Show Virgil:

```
VOICE CHECK: Article #[number]

Section sampled: [H2 heading]
First-person present: [Yes / No — if No, quote the offending passage]
Tone: [Friend talking / IKEA manual]
Universal declarations: [None / Quote any found]

Passes voice check? Or need rewrite?
```

🛑 **HUMAN LOOP #3b:** Wait for Virgil's confirmation. If voice fails, rewrite the flagged sections and show again before generating images.

---

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
fig.write_image('/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/articles/images/{slug}-image-1.png', scale=2)
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
fig.write_image('/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/articles/images/{slug}-image-2.png', scale=2)
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
open "/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/articles/images/{slug}-image-1.png"
open "/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/articles/images/{slug}-image-2.png"
```

Also use the Read tool on each PNG so the image displays inline in chat:

```
Read: /Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/articles/images/{slug}-image-1.png
Read: /Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/articles/images/{slug}-image-2.png
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
COMPLEX_WORDS=$(grep -in "regardless\|commentary\|leverage\|synergy\|unlock\|empower\|revolutionary\|game-changing\|best-in-class\|comprehensive\|furthermore\|additionally\|nevertheless\|consequently\|utilize\|utilise\|facilitate\|demonstrate\|attribution\|methodology\|framework\|ecosystem\|paradigm\|scalable\|robust\|seamless\|actionable\|impactful\|holistic\|streamline\|benchmark\|bandwidth\|granular\|alignment\|landscape\|trajectory\|narrative\|optimiz" "$ARTICLE_PATH" || true)
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
  echo "❌ FAIL: Only $FAQ_COUNT FAQ questions found. Need 10 minimum. Go back to Step 5d and add more questions from the PAA list before proceeding."
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

**If CHECK 5 outputs ❌ FAIL:** Go back to Step 5d and add more questions from the PAA list. Do not proceed until the check outputs ✅ PASS with 10+.

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
□ H2 headings are question-based (natural language queries)?

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

### 7c: How-To Article Checker (CONDITIONAL — only run if Article Path = "How-To")

**Skip this entire section if the article is not a how-to.** Only runs for articles flagged in Step 1.

Go through the article section by section. For each how-to section, run these 7 checks:

| # | Check | Question | If FAIL |
|---|-------|----------|---------|
| 1 | Action clear | Does the section tell the reader exactly what to type or do? | Add the missing action |
| 2 | Prompt copyable | Is there a code block with the exact Claude prompt the reader can copy? | Add the code block |
| 3 | Result verifiable | Does the section tell the reader what they should see after running the prompt? | Add what to expect |
| 4 | No gap | Would a reader be lost between this section and the next? | Add a bridge |
| 5 | No jargon | Is there a technical term that isn't explained? | Use the jargon list from Pattern 8 (How-To) |
| 6 | Proof included | Does the section have a real test result with real numbers woven into the narrative? | Add proof |
| 7 | Prerequisites | Does "Before You Start" list everything needed? | Add the missing item |

**Show the checker results:**

```
HOW-TO CHECKER:
Section 1: ✅ ✅ ✅ ✅ ✅ ✅ ✅
Section 2: ✅ ✅ ✅ ❌ ✅ ✅ ✅ — Gap: reader doesn't know how to open Claude Code yet
Section 3: ✅ ✅ ✅ ✅ ❌ ✅ ✅ — "MCP" not explained
...
```

Fix all failures. Re-run. Only proceed when all sections pass all 7 checks.

**PRODUCT.md cross-check (if PRODUCT.md was loaded in Step 2.5):**

Compare every feature in the PRODUCT.md against sections in the article. If a feature has no section, ADD IT. If a section covers something not in the PRODUCT.md, flag it for the user.

---

## Step 8: Show Article for Review

**MANDATORY: ALWAYS show the full article text directly in chat. Do NOT use the Read tool (output collapses in VSCode). Instead, output the article text as plain markdown in your response message. If the article is long, split it across TWO messages to prevent truncation. Virgil must see every word in chat without clicking anything.**

**TRUNCATION SAFEGUARD:** Before showing, run `wc -w` on the file and note the count. After showing, verify the displayed text matches by checking that the FAQ section (last major section) is visible at the bottom of your display. If the FAQ is not visible, the display was truncated — split the article into two messages and show both.

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

[Image 1 — [description]](computer:///sessions/intelligent-zen-mccarthy/mnt/Sucana/Marketing/SEO/articles/images/[article-slug]-image-1.png)
[Image 2 — [description]](computer:///sessions/intelligent-zen-mccarthy/mnt/Sucana/Marketing/SEO/articles/images/[article-slug]-image-2.png)

RULE: Always show image links here. Never skip. Never describe. Just the clickable links.

Ready to approve? Or need edits?
```

🛑 **HUMAN LOOP #5:** DO NOT save yet. Wait for Virgil's approval. If edits needed, revise and show again.

---

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
python3 << 'EOF'
import openpyxl
wb = openpyxl.load_workbook('/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/Article_Production_System.xlsx')
ws = wb['Article Production System']
for row in ws.iter_rows(min_row=2):
    if row[0].value == ARTICLE_NUMBER:
        row[10].value = 'In Progress'   # Status column (K)
        row[11].value = '/blog/SLUG'    # URL Slug column (L)
        break
wb.save('/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/Article_Production_System.xlsx')
print('Production System updated: In Progress')
EOF
```

Replace `ARTICLE_NUMBER` with the article's # and `SLUG` with the actual slug.

### Tag the used story in content-ideas.md

Go to `Marketing/Research/content-ideas.md`. Find the story used in this article. Add this tag on the line immediately after the story:

```
<!-- USED IN: article-XX-slug -->
```

This is mandatory. No memory between sessions — the file is the only record. If you skip this, the same story will appear in the next article.

---

## Step 10: Generate Hero Cover Image (Nanobanana)

**Every article gets a photorealistic hero cover image. Nanobanana generates 3 variants — Virgil picks the best one.**

### 10a: Load the Schema

Read this file before building the prompt:
`/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/skills/nano_banana_image.md`

Use the Blog Hero Image JSON structure from that file.

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
`/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/prompts/blog/{slug}-cover.json`

### 10d: Generate 3 Variants

```bash
cd "/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator" && python3 scripts/generate.py --count 3 "prompts/blog/{slug}-cover.json"
```

Output saves to: `images/blog/{slug}-cover_v1.png`, `_v2.png`, `_v3.png`

### 10e: Show All 3 Variants to Virgil

**MANDATORY: OPEN THE IMAGES SO VIRGIL CAN SEE THEM. Every single time. No exceptions. Do not describe them. Do not link them. OPEN THEM.**

Run `open` on each image file so it opens in macOS Preview:

```bash
open "/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/images/blog/{slug}-cover_v1.png"
open "/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/images/blog/{slug}-cover_v2.png"
open "/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/images/blog/{slug}-cover_v3.png"
```

Also use the Read tool on each PNG so the image displays inline in chat:

```
Read: /Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/images/blog/{slug}-cover_v1.png
Read: /Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/images/blog/{slug}-cover_v2.png
Read: /Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/images/blog/{slug}-cover_v3.png
```

Then output:

```
HERO COVER VARIANTS: Article #[number]

Variant 1: [image displayed above]
Variant 2: [image displayed above]
Variant 3: [image displayed above]

Which one? (1, 2, or 3 — or say regenerate for new variants)
```

🛑 **HUMAN LOOP #7:** Wait for Virgil to select a variant.

### 10e: Resize and Save

After Virgil selects a variant, resize to **1200 x 675 pixels** (true 16:9 — pure scale down, no crop):

```python
from PIL import Image

src = "/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Sucana Agents/Ad Image Generator/images/blog/{slug}-cover_v{N}.png"
dest = "/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/articles/images/{slug}-cover.png"

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

## Step 12: Convert to MDX + Deploy to GitHub

**Only after Virgil confirms deploy in Step 11.**

### 12a: Generate the MDX file

```yaml
---
title: "Your Post Title Here"
excerpt: "A 1-2 sentence summary (120-160 chars). Factual, not marketing copy."
date: "YYYY-MM-DD"
tags: ["tag1", "tag2", "tag3"]
category: "category-slug"
coverImage: "/images/blog/{slug}-cover.png"
readingTime: "X min read"
author: "Sucana"
featured: false
---
```

**For How-To articles:** Add `schema: "HowTo"` to the frontmatter. This enables HowTo structured data markup which helps Google display the article as a step-by-step result in search.

**MDX body rules:**
- Strip the SEO Frontmatter block — stays in local .md file only
- Strip the SEO Notes section — stays in local .md file only
- Keep all H2/H3 headings, body content, FAQ section
- Keep all image references — update paths to deployed format

### 12b: Clone repo and deploy

Read `Marketing/SEO/BLOG-INSTRUCTIONS.md` at runtime for the GitHub PAT and exact git commands.

```bash
git clone https://[PAT]@github.com/vinodsharma10x/www.sucana.ai.git
cd www.sucana.ai
git config user.name "vinodsharma10x"
git config user.email "vinod@vinodsharma.co"

git add content/blog/{slug}.mdx
git add public/images/blog/{slug}-cover.png
git add public/images/blog/{slug}-image-1.png
git add public/images/blog/{slug}-image-2.png
git add public/images/blog/{slug}-image-3.png

git commit -m "Add blog post: {Post Title}"
git push origin main
```

**Rules:** Push directly to `main`. Do NOT create branches. Do NOT modify existing files.

---

## Step 13: Verify Deployment + Update Production System

1. Wait ~60 seconds for Vercel to deploy
2. Check the live URL: `https://www.sucana.ai/blog/{slug}`
3. Confirm cover image loads
4. Confirm in-article images load

Once confirmed live, update the Production System to "Published":

```bash
python3 << 'EOF'
import openpyxl
from datetime import date
wb = openpyxl.load_workbook('/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/Article_Production_System.xlsx')
ws = wb['Article Production System']
for row in ws.iter_rows(min_row=2):
    if row[0].value == ARTICLE_NUMBER:
        row[10].value = 'Published'                  # Status column (K)
        row[12].value = str(date.today())            # Publish Date column (M)
        break
wb.save('/Users/virgilbrewster/My Drive/Drive-sandbox/Sucana/Marketing/SEO/Article_Production_System.xlsx')
print('Production System updated: Published', date.today())
EOF
```

Replace `ARTICLE_NUMBER` with the article's #.

```
✅ DEPLOYED: https://www.sucana.ai/blog/{slug}
Article #[number] is live. Production System updated.

Live article: [Article Title](https://www.sucana.ai/blog/{slug})
```

---

## Step 14: Distribution Assets

1. **LinkedIn teaser post** — 100-150 words, hook from article's most compelling insight
2. **Email snippet** — 2-3 sentences for newsletter inclusion

Show both in chat for review. Do NOT auto-save.

---

## Pipeline Summary

```
Step 1:  Load context + find next article            → 🛑 HUMAN LOOP #1
Step 2:  Keyword research + show brief               → 🛑 HUMAN LOOP #2
Step 3:  Load voice
Step 4:  Find story from content-ideas.md
Step 5:  Write article (with image placeholders)
Step 5b: Structure checkpoint — H1, first H2, angle → 🛑 HUMAN LOOP #3
Step 6:  Generate 2 Plotly charts                   → 🛑 HUMAN LOOP #4
Step 7:  Self-check — BASH COMMANDS ON FILE, show output, fix failures before Step 8
Step 8:  Show FULL article for review                → 🛑 HUMAN LOOP #5
Step 9:  Save article + mark In Progress in XLSX + tag used story in content-ideas.md
Step 10: Generate hero cover image (Nanobanana, 3 variants) → 🛑 HUMAN LOOP #6
Step 11: Final deploy confirmation                   → 🛑 HUMAN LOOP #7
Step 12: Convert to MDX + push to GitHub
Step 13: Verify deployment + mark Published in XLSX
Step 14: Distribution assets (LinkedIn + email)
```

---

## Important Rules

1. **One article at a time.** Complete the full pipeline before moving to the next.
2. **Never skip the CSV check.** Always verify which article is next by Priority Rank.
3. **Never skip keyword research.** Every article gets validated keywords before writing.
4. **Never save without approval.** Always show in chat first.
5. **Never invent stories.** Source every story from content-ideas.md. Check USED IN tags. Stay close to the raw notes — do not expand into invented scenes or dialogue.
6. **Voice comes from the Writer skill.** The approved posts database defines the style.
7. **Dual optimize everything.** Every article serves both Google AND LLMs.
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
18. **FAQ is 10 questions minimum.** The bash check counts `### ` headers inside the `## Frequently Asked Questions` section only — must be 10+. If CHECK 5 outputs ❌ FAIL, go back to Step 5d and add more questions before proceeding.
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
