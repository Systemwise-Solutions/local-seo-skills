# Evals: local-ai-visibility

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline.

## Should trigger

1. "ChatGPT keeps recommending our competitor instead of us when people ask for a physio in Bristol. Why?"
2. "Does Gemini mention my restaurant? How would I even check?"
3. "How do I get my plumbing business into Google's AI Overviews for 'emergency plumber Leeds'?"
4. "Can you do GEO for my dental practice?"
5. "Here are six ChatGPT answers I saved. Are we being recommended?" (with pasted answers)
6. "Our agency wants to report AI visibility for 8 client clinics. Where do we start?"

## Should not trigger

1. "Write a blog post about how AI is changing search."
2. "Use ChatGPT's API to summarise my reviews."
3. "Why don't we show in the Google map pack outside our street?" (local-seo-audit)
4. "Optimise our SaaS documentation for AI crawlers." (SEO for AI Agents territory, not local)

## Borderline (trigger is acceptable, should stay honest)

1. "Can you guarantee we'll be recommended by ChatGPT?" (should say nobody can, then offer to measure)
2. "Should I add an llms.txt file to get named by AI?" (should say there's no good evidence it gets a local business named, and point at sources and on-site facts)
3. "I asked ChatGPT once and we weren't named. Is our SEO broken?" (should explain one run proves nothing and offer the prompt set)

## What good output looks like

- Says once, plainly, that this is the newest and least certain area and nobody can guarantee a mention.
- Builds a prompt set from the money searches, area and reasons people choose, and lets the user edit it.
- On the free tier: does its own web search for the sources, clearly labelled as not assistant output, and gives the copy-paste block for 3 runs per prompt per assistant.
- With SearchOps: calls `get_location_ai_visibility_insights` once per engine (ChatGPT, Gemini), never adds engines together, never describes a rank or position; uses `get_analytics_ai_referrals` as a floor, not a total.
- Runs `mention_rate.py` on the pasted runs (or counts by hand with the same rules if scripts can't run), and reports per assistant, per prompt and per competitor.
- Doesn't read anything into fewer than 3 runs or a one-in-three difference.
- Source gap analysis with each source's listed status marked as checked or unknown, a consistency check, and why the most-named competitor wins.
- Writes quotable site copy with gaps marked for the user to fill, never inventing prices, credentials or years.
- Sends the user back to the lower rungs (local-seo-audit) if the profile or site basics are broken.
- No fake reviews, planted forum posts or paid placements presented as editorial. No em dashes. One plain next-steps line; none in agency client-facing output.
