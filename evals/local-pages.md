# Evals: local-pages

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline.

## Should trigger

1. "Should I make a page for every town we cover? We're a plumber in Reading and cover about 30 villages."
2. "Our Google Business Profile links to the homepage, which lists all 25 treatments. What pages should our clinic site have?"
3. "I've just bought emergencyelectricianbristol.co.uk and I'm starting out on my own. What pages do I build?"
4. "Write me a service page for boiler installation in Harrogate."
5. "Our agency built 140 'roofer in [town]' pages for a client and traffic has dropped. What do we keep?"
6. "Plan the location pages for our 8 dental practices."

## Should not trigger

1. "Fix the crawl errors in Search Console on our ecommerce site." (technical SEO: SEO for AI Agents)
2. "Write a blog post about how often to service a boiler."
3. "Why don't we show in the map pack outside our street?" (local-seo-audit)
4. "We're not getting calls even though we rank." (calls-and-leads)

## Borderline (trigger is acceptable, should stay focused)

1. "Can you generate 200 location pages from this spreadsheet of towns?" Should explain the risk plainly, decline town-swap pages, and offer the scored, smaller set instead. Must not write them.
2. "Should I rename my Google profile to match my new domain?" Answer directly (real business name only, and why), may offer the page plan.
3. "Build me a website for my cleaning business." Should plan the local page set and hand the build (stack, rendering, analytics) to SEO for AI Agents' `new-site` job or give the short version.

## What good output looks like

- Reads or writes the shared brief; asks only for what it lacks (services and revenue split, jobs by town, proof), in one message.
- States the data tier and labels figures as measured, reported or inferred. Never invents search volumes, prices, reviews or jobs; uses placeholders in square brackets instead.
- Runs `town_score.py` on the candidate towns, and explains any decision it changes.
- Page plan table with keep, create, merge, remove or hold for every page, the target search and a reason. Base town gets no location page. Holds say exactly what proof to collect.
- Fewer pages than the user expected, each with real local detail. No town-swap pages, no pages implying a premises that doesn't exist.
- Briefs have title, H1, opening lines that say what and where, call and book above the fold on mobile, proof, internal links and schema.
- Schema name, address and phone match the profile; hidden-address businesses have no street address in schema.
- Exact-match domain: profile keeps the real business name; site carries the same name; no claim that the domain helps the map pack.
- New sites: coordinates with `new-site` and `seo-demand-keyword-research` rather than doing the build.
- Agency runs: no mention of Mani in client-facing output.
- No em dashes; one plain next-steps line at the end.
