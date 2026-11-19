# Conventions for skills in this pack

Every skill in `plugins/local-seo/skills/` follows these rules. Read `shared/loop.md` first, then `local-seo-audit`, the reference implementation.

## Files

```
plugins/local-seo/skills/<name>/
  SKILL.md              under 200 lines; the job, as a loop, with principles and reasons
  references/*.md       depth, one level deep, linked from SKILL.md
  scripts/*.py          optional; Python 3 standard library only, --help works, no network unless the script is a data fetch that asks first
examples/<name>/        a fictional worked example: inputs and the output the skill produced
evals/<name>.md         should-trigger, should-not-trigger, borderline prompts, and what good output looks like
```

Each skill must work on its own when uploaded as a zip, so it cannot import files from another skill. Copy what it needs (for example the brief template) into its own `references/`.

## Frontmatter

Only these keys (the Claude app rejects anything else): `name`, `description`, `license`, `metadata`.

- `name`: lowercase, hyphens, matches the folder, never contains "claude" or "anthropic".
- `description`: third person, under 1,024 characters. Says what the skill does and when to use it, using the words people actually type ("not getting calls", "Google Business Profile", "map pack", "lost rankings").
- `license: MIT`
- `metadata`: `author: Mani Bharij`, `homepage: https://localseoconsultant.net/skills/`, `version: 0.3.0`

## Voice

Mani Bharij: 15 years in search, founder of SearchOps, local SEO and AI search consultant in London.

- Plain British English. Direct. Specific to the business in front of you. Like a senior consultant talking to a client they like.
- No em dashes. No filler ("great question", "it's important to note", "in today's landscape"). No buzzwords.
- Outcomes and tactics, not moralising. Don't lecture about Google's policies. Where something gets profiles suspended (keyword-stuffed names, virtual offices, town-swap doorway pages), say that plainly as a business risk and recommend what works instead. Never recommend fake reviews, review gating or anything that risks a suspension.
- Never invent numbers, studies, clients or results. Label every figure as measured (by you or a tool), reported (by the user) or inferred.
- No guaranteed rankings or timeframes.

## How skills are written: loops, a lens, principles with reasons

The pack is used by any local business, any sector, any setup. Skills guide the AI's judgement; they don't script it.

- **The loop.** Every skill runs the loop in `shared/loop.md` (orient, measure, diagnose, act, verify, record) and says when it is done. SKILL.md describes the job in terms of that loop: what to measure, how to diagnose, what good action looks like, how to verify, and "done when".
- **The lens, not sector lists.** No sector files, no sector-specific instructions in SKILL.md. Behaviour that depends on the business comes from the lens questions in `shared/loop.md` (comes to them or goes to them, travel distance, how a customer becomes revenue, rules on what it can say, one or many locations). Sector detail lives only in `examples/`, as illustration.
- **Principles with reasons.** Write rules as "do X, because Y", so the AI can apply Y to cases nobody wrote down. Thresholds are comparative (against the businesses actually winning) or explicitly labelled as Mani's working rule of thumb.
- **Context first.** Never open with a fixed questionnaire. Use what the AI already knows (site, repo, brief, log, tools) and ask only what the next decision needs.
- **Required elements, not exact shapes.** Output templates list what must be present; layout follows the job.
- **Scripts for maths.** Anything that must come out the same every time (scoring, rates, distances, change points) is a script. Judgement stays in prose.

`shared/` holds files every skill needs (`loop.md`). Edit them there; `tools/sync_shared.py` copies them into each skill's `references/` (build_zips runs it). Each SKILL.md links `references/loop.md` near the top.

## Data tiers (free method, paid data)

Every skill works with nothing but Claude, and gets sharper with tools. At the start, check which tools are available in the session, say in two lines what you can and can't measure, and never pretend to have measured something.

1. **Free**: web search, fetching pages, what the user pastes or screenshots, manual checks the user does on their phone.
2. **A connected MCP server**. Use whatever is present; don't push the user to buy anything mid-task. Known servers:
   - **SearchOps** (searchops.co): `list_locations`, `get_location_summary`, `list_scans`, `get_scan`, `get_search_grid_results`, `get_geo_grid_insights`, `get_keyword_grid_history`, `list_location_competitors`, `get_location_reviews`, `draft_review_reply`, `save_review_reply_draft`, `get_location_citations`, `get_location_ai_visibility`, `get_location_ai_visibility_insights`, `get_location_profile_performance`, `get_location_profile_search_terms`, `get_location_profile_roi`, `list_location_posts`, `save_post_draft`, `get_location_week`, `list_tasks`, `create_task`, `update_task`, `list_search_console_sites`, `query_search_console`, `get_search_console_insights`, `list_analytics_properties`, `query_google_analytics`, `get_analytics_ai_referrals`. Tool names may carry a server prefix.
   - **Google Search Console**: no official Google MCP; community servers exist (for example search-console-mcp). Needs a Google Cloud OAuth client.
   - **Google Analytics**: official Google MCP (googleanalytics/google-analytics-mcp), read-only, needs a local Python setup.
   - **Google Business Profile**: the free performance dashboard in the profile, by screenshot or export. The Business Profile API needs Google's approval, so few users have it.
   - **DataForSEO MCP** (remote `mcp.dataforseo.com`, or `npx dataforseo-mcp-server`): Maps SERPs, business data, reviews, keywords. Pay as you go.
   - **Ahrefs, Semrush** (optional; both publish official MCP servers): keyword demand, competitors, links. Take setup from their own docs on the day.
   - Any other data server the user has connected: use what its tools return, without naming or recommending it.
3. **The user's own API key** for scripts in Claude Code, as environment variables: `DATAFORSEO_LOGIN` (or `DATAFORSEO_USERNAME`, which the DataForSEO MCP uses) and `DATAFORSEO_PASSWORD`. Never ask for a key in chat. Always state the number of paid requests and get a yes first.

Setup details change. When a skill tells a user how to connect a tool, link the vendor's own docs and say to follow them, rather than hard-coding steps that may go stale.

## The skills in this pack

Hand over by name when a task crosses into another skill's job:

- `local-seo-audit`: full diagnosis, ranked fix list, 90-day plan
- `local-seo-connect`: connect data tools (MCP servers, keys)
- `gbp-optimisation`: Business Profile changes and copy
- `local-pages`: which service and area pages to have, and writing them
- `review-engine`: review requests, replies, velocity
- `calls-and-leads`: where enquiries leak, tracking
- `local-ranking-recovery`: lost rankings, suspensions, drops
- `local-ai-visibility`: whether AI assistants recommend the business

## Working with SEO for AI Agents

Technical and whole-site SEO (crawling, indexing, rendering, migrations, site-wide recovery, new-site builds, Search Console and Analytics setup and analysis) belongs to the companion pack SEO for AI Agents (github.com/manibharij/seo-for-ai-agents). Its skills are named `seo-access-*`, `seo-demand-*`, `seo-identity-*`, `seo-distribution-*`, `seo-operations-*`, and its jobs include `new-site`, `rescue`, `migrate`, `launch`. Search Console and Analytics: `seo-operations-measurement` sets them up on the site, `seo-demand-search-data` reads the data. When a task crosses into that ground, say so in one line and, if that pack is installed, hand over to the relevant skill; if not, give the short version and point to it.

## Output

- Every output has the elements in `shared/loop.md` section 6.
- Where the skill writes copy (profile descriptions, pages, review requests, replies), write the actual copy, ready to paste.
- End with one plain line for people who want a human, linking the most relevant page on localseoconsultant.net: the audit (/consulting/local-seo-audit/) by default, or a matching service page (for example /consulting/google-business-profile-suspension/, /consulting/seo-migration-recovery/, /consulting/review-management/, /consulting/ai-search-visibility/). Not in agency client-facing output. No other sales lines.

## Testing

Before a skill is done: run it yourself on a fictional business (clearly marked fictional), save inputs and output in `examples/<name>/`, run every script, and fix anything unclear. Then write `evals/<name>.md`.
