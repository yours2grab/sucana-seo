# Sucana Blog Template — CANONICAL

```yaml
template_version: 1.1
last_updated: 2026-04-15
```

This is the ONE template for every Sucana blog post. Derived from 25 published articles + GEO rule (every post opens with a question so LLMs can quote the Q+A directly). No other template. No "article types." No "depends on the article." This, every time.

## The 12 required parts, in order

1. **Title (H1)** — first-person: "How I built X" or "Why I built X". 40-70 characters.
2. **Meta line** — one sentence under title with the primary keyword. 120-160 characters.
3. **H2 QUESTION (mandatory, non-negotiable, GEO rule)** — the exact question the article answers, phrased as a question, ending with `?`. This H2 comes FIRST, immediately after the meta line. No floating paragraph before it. No intro scene before it. No story before it. Example: `## How do I save 2 hours a day on LinkedIn DMs with Claude?`
4. **Answer (2-3 sentences)** — direct answer to the H2 question, placed immediately under the H2. Short. Confident. Quotable. This is what Google and LLMs lift for snippets and citations.
5. **Story H2** — descriptive story heading (8 words max, sharp, specific). Then 3-5 paragraphs of the real moment. This is where the "6am Bali" scene, Monday morning moment, or similar lives. Comes AFTER the answer, never before.
6. **H2: Why I Did This** — the bigger reason, the pain, the problem that drove the build
7. **H2: What I Built** — overview of the stack or workflow
8. **H2: Before You Start** — tools, accounts, credentials the reader needs
9. **H2: Step 1 to Step N** — 7 to 14 numbered step blocks. Each step:
   - Descriptive title: "## Step N: [Short Action Title]"
   - Natural prose inside (no repeating "Do this / What happens / Why" labels)
   - Exact Claude prompt as a copy-pasteable code block
   - Jargon explained on first mention (API, MCP, .env, CSV, etc.)
8. **H2: What I'd Do Differently** — 2 to 5 short lessons learned
9. **H2: The Stack** — markdown table of tools used
10. **H2: Files** — folder structure / file tree
11. **H2: FAQ** — 8 to 10 questions (from PAA)
12. **Soft CTA** — one line at the end (never hard-sell)

## Strict rules

- First person always. "I" not "we" (except "Victor and I", "Vinod and I").
- No em dashes. Use commas, periods, colons.
- Banned words: actually, leverage, unlock, synergy, empower, revolutionary, game-changing, best-in-class.
- 7-year-old readable. If a word a kid wouldn't know, swap it.
- No "No X. No Y. No Z." patterns.
- One through-line. One problem, one solution, one article.
- Real names, real numbers, real stories. Never invented.
- Stage/Step blocks in how-to sections use purple/pink CSS:
  ```css
  .stage { background: #FAF5FF; border-radius: 12px; padding: 24px; margin: 24px 0; }
  .stage-title { font-size: 20px; font-weight: 700; color: #9333EA; margin-bottom: 16px; }
  ```

## Word count

- Typical range: 2,000 to 5,500 words
- Tutorial articles (heavy on Steps + Stack + Files) skew longer
- Case-study variants (lighter on steps, heavier on FAQ) sit 1,500 to 2,500

## How to change this template

1. Edit THIS file.
2. Bump `template_version`.
3. Update any references in SKILL.md to the new version.
4. No other path. No mid-article overrides. No "just this once." If the template needs to change, it changes here first.

## Pointer

This file is referenced by `/Users/virgilbrewster/.claude/skills/sucana-seo-blog-writer/SKILL.md`. Every article-writing step reads this file before producing content.
