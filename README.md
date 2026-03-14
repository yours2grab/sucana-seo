# Sucana SEO Article Pipeline

A Claude Code skill that manages the full SEO article production pipeline for [sucana.ai/blog](https://sucana.ai/blog). Takes an article from brief to live deployment in a single session.

## What It Does

Writes long-form SEO articles (2,000+ words) dual-optimized for Google ranking AND LLM citation (AI Overviews, ChatGPT, Perplexity). Each article goes through a 14-step pipeline with 7 human approval gates before anything goes live.

## The Pipeline

| Step | What Happens | Human Approval? |
|------|-------------|----------------|
| 1 | Load SEO strategy, find next article from production tracker (XLSX) | Yes - confirm brief |
| 2 | Keyword research + SERP analysis + competitor gap analysis + Reddit pain validation | Yes - confirm keywords & angle |
| 3 | Load Virgil's voice profile (Virgil_Voice_MASTER.md) | No |
| 4 | Find a real story from content-ideas.md + Fireflies transcripts | No |
| 5a | Write opening H2 question + direct answer | Yes - confirm opening |
| 5b | Write full article body with image placeholders | No |
| 5c | Write FAQ section (10 questions minimum from PAA data) | No |
| 5.5 | Structure checkpoint (H1, first H2, angle review) | Yes |
| 5.6 | Voice check (first-person, not IKEA manual) | Yes |
| 6 | Generate 2 Plotly charts with Sucana brand colors | Yes - approve charts |
| 7 | Automated self-check (11 bash checks on the actual file) | No - auto-fix |
| 8 | Show full article in chat for review | Yes - approve article |
| 9 | Save article + update production XLSX + tag used story | No |
| 10 | Generate hero cover image via Nanobanana (3 variants) | Yes - pick variant |
| 11 | Final deploy confirmation | Yes |
| 12 | Convert to MDX + push to GitHub (Vercel auto-deploys) | No |
| 13 | Verify live URL + mark Published in tracker | No |
| 14 | Generate distribution assets (LinkedIn teaser + email snippet) | No |

## Content Strategy

80 planned articles across 4 pillars:

| Pillar | Focus | Example Topics |
|--------|-------|---------------|
| P1 - AI for Performance Marketing | How AI changes running paid ads | AI Google Ads, ChatGPT for ads, AI Meta ads |
| P2 - AI Workflows for Marketers | Real tool reviews, automations tested | AI marketing workflow, marketing automation |
| P3 - AI-Powered Marketing Org | How AI reshapes teams and roles | AI agency automation, AI-native teams |
| P4 - Experiments and Results | We tried something, here's what happened | Real test data, actual outcomes |

## Automated Quality Checks (Step 7)

The skill runs 11 bash checks on every article before it's shown for review:

1. **Em dashes** - Must be 0. Uses commas or colons instead.
2. **Banned phrases** - "Here's the thing", "You need to", etc.
3. **Complex vocabulary** - Flags words a 7-year-old wouldn't understand.
4. **Long sentences** - Hard fail on any sentence over 20 words.
5. **Question-first structure** - No floating paragraphs before the first H2.
6. **FAQ count** - Minimum 10 questions inside the FAQ section.
7. **Horizontal dashes** - No `---` dividers in article body.
8. **Blob detection** - No paragraphs with 4+ sentences.
9. **Repeated phrases** - Catches duplicate distinctive phrases.
10. **Near-duplicate sentences** - Stemmed word overlap detection.
11. **Bold label spacing** - Blank line required after every bold label.
12. **Consecutive sentence starts** - Never start 2+ sentences with the same word.

All checks must pass before proceeding. Failures are auto-fixed and re-checked.

## Image Generation

Each article gets exactly 3 images:

**In-article (2 Plotly charts):**
- Sucana brand colors: purple `#8b5cf6` + pink `#ec4899`
- Background: `#f1f5f9`, text: `#0f172a`
- Output: 1200x675 at 2x scale
- Templates included for simple bar and grouped bar charts

**Hero cover (1 Nanobanana image):**
- Photorealistic, shot on Canon EOS R5
- Never literal (metaphor over screenshot)
- 3 variants generated, user picks one
- Resized to 1200x675 (true 16:9)

## Deployment

Articles deploy to `sucana.ai/blog` via:
1. Convert approved article to MDX with frontmatter
2. Push to `vinodsharma10x/www.sucana.ai` GitHub repo (main branch)
3. Vercel auto-deploys on push
4. Verify live URL loads with all images
5. Update production tracker to "Published"

## Voice Rules

All articles written in Virgil Brewster's voice:
- First-person narrative ("I", not "we")
- Real stories, real names (Victor, Vinod), real numbers
- Plain language a 7-year-old can read
- Say it once, move on
- Steps sound like a friend explaining, not an IKEA manual
- 2-3 sentence blocks, blank line between each

## Story Sourcing

Stories are never invented. Every article sources from:
- `content-ideas.md` - tagged with `<!-- USED IN: article-XX-slug -->` after use
- Fireflies meeting transcripts (via MCP tools)
- Reddit pain points (optional, from automated scrape)

The tagging system prevents story reuse across sessions since Claude has no memory between conversations.

## Key Files

| File | Purpose |
|------|---------|
| `SKILL.md` | The full skill definition (this repo) |
| `Marketing/SEO/Article_Production_System.xlsx` | 80-article tracker |
| `Marketing/SEO/SEO_GEO_Playbook.md` | Content pillar strategy |
| `Marketing/SEO/keyword-research.md` | 40 validated keywords |
| `Soul/Virgil_Voice/Virgil_Voice_MASTER.md` | Voice profile |
| `Marketing/Research/content-ideas.md` | Story source with usage tracking |
| `Marketing/SEO/article-formatting-guide.md` | Formatting rules |

## Install

Drop `SKILL.md` into your `.claude/skills/seo/` directory.

## Requirements

- Claude Code CLI
- Python 3 with `plotly`, `kaleido`, `openpyxl`, `Pillow`
- Nanobanana MCP (for hero cover images)
- Fireflies MCP (for meeting transcript search)
- GitHub access to the deployment repo
- Vercel connected to the repo for auto-deploy

## Credits

Built by Virgil Brewster at [Sucana](https://sucana.ai) — AI-powered content and analytics for B2B SaaS.
