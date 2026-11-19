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

## A business type the examples don't cover

"I run a mobile dog grooming van covering villages around Thame. People keep telling me they asked ChatGPT for a groomer and got the salons in town. Can you check?"

Good output: reads the shape through the lens (goes to customers, no premises, a spread of villages rather than one neighbourhood), so the prompts name the villages and "mobile" or "comes to you" needs, not a street or landmark; checks the profile is set up as a service-area business before blaming the assistants; looks for the directories and review sites that actually rank for these prompts rather than assuming any; writes site copy that says where the van goes and how booking works, with prices and any qualifications left as gaps for the user to confirm; and doesn't suggest a fake address in town to get named alongside the salons.

## What good output looks like

- Says once, plainly, that this is the newest and least certain area and nobody can guarantee a mention.
- Orients from context first (brief, log, site, profile, connected tools) and asks only what's missing, in one message. No fixed questionnaire.
- Builds a prompt set from the money searches, the area as customers say it, and the reasons people choose, shaped by the lens (a place people visit or a business that travels), and lets the user edit it.
- On the free tier: does its own web search for the sources, clearly labelled as not assistant output, and gives the copy-paste block for 3 runs per prompt per assistant.
- With SearchOps: calls `get_location_ai_visibility_insights` once per engine (ChatGPT, Gemini), never adds engines together, never describes a rank or position; uses `get_analytics_ai_referrals` as a floor, not a total.
- Runs `mention_rate.py` on the pasted runs (or counts by hand with the same rules if scripts can't run), and reports per assistant, per prompt and per competitor.
- Doesn't read anything into fewer than 3 runs or a one-in-three difference.
- Source gap analysis with each source's listed status marked as checked or unknown, a consistency check, and why the most-named competitor wins.
- Writes quotable site copy with gaps marked for the user to fill, never inventing prices, credentials or years, and checks it against any rules on what the business can say.
- Saves the prompt set and assistants in the brief and logs the baseline with a re-run date.
- Sends the user back to the lower rungs (local-seo-audit) if the profile or site basics are broken.
- No fake reviews, planted forum posts or paid placements presented as editorial. No em dashes. One plain next-steps line; none in agency client-facing output.
