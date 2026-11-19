# Evals: local-pages

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline.

## Should trigger

1. "Should I make a page for every town we cover? We're a plumber in Reading and cover about 30 villages."
2. "Our Google Business Profile links to the homepage, which lists all 25 treatments. What pages should our clinic site have?"
3. "I've just bought emergencyelectricianbristol.co.uk and I'm starting out on my own. What pages do I build?"
4. "Write me a service page for boiler installation in Harrogate."
5. "Our agency built 140 'roofer in [town]' pages for a client and traffic has dropped. What do we keep?"
6. "Plan the location pages for our 8 dental practices."
7. "We run an independent bookshop and café in Bath. Customers come in from the villages around. Do we need pages for those villages?" (a business customers visit, not covered by the examples)
8. "I'm in our Next.js repo. We've got a /areas/[town] route generating 60 pages from a JSON file. Which should stay?"

## Should not trigger

1. "Fix the crawl errors in Search Console on our ecommerce site." (technical SEO: SEO for AI Agents)
2. "Write a blog post about how often to service a boiler."
3. "Why don't we show in the map pack outside our street?" (local-seo-audit)
4. "We're not getting calls even though we rank." (calls-and-leads)

## Borderline (trigger is acceptable, should stay focused)

1. "Can you generate 200 location pages from this spreadsheet of towns?" Should explain the risk plainly, decline town-swap pages, and offer the scored, smaller set instead. Must not write them.
2. "Should I rename my Google profile to match my new domain?" Answer directly (real business name only, and why), may offer the page plan.
3. "Build me a website for my cleaning business." Should plan the local page set and hand the build (stack, rendering, analytics) to SEO for AI Agents' `new-site` job or give the short version.

## Business types the examples don't cover

**Bookshop and café (prompt 7).** Good output reads the shape first: customers come to the shop, so rankings are anchored to the Bath address and village pages won't move the map pack in those villages. It asks where customers actually come from (postcodes from loyalty, events or online orders, if they have them) rather than assuming. It most likely recommends no village pages, or at most one for a place where people genuinely travel in and the page helps them (parking, bus, what's on), and puts the effort into the homepage, the café and events pages, and the page the profile links to. Main action above the fold is directions, opening hours and events or table booking, not a phone number. `town_score.py`, if run, uses `max_travel_km` for how far customers travel and `"unit": "customers"`. No sector instructions are invented; reasoning comes from the lens.

**Generated pages in a repo (prompt 8).** Reads the route, the data file and the template before advising; counts how much of each page differs; checks Search Console or analytics for pages that bring enquiries before removing any; proposes redirects in the project's own config and shows the diff without deploying.

## What good output looks like

- Reads or writes the shared brief; uses the site, repo, profile and log first, and asks only for what it lacks (services and revenue split, where the work or customers are, proof), in one message. No fixed questionnaire.
- Reads the business through the lens (comes to them or goes to them, how far customers travel) before deciding whether area pages can exist at all.
- States the data tier and labels figures as measured, reported or inferred. Never invents search volumes, prices, reviews or jobs; uses placeholders in square brackets instead.
- Runs `town_score.py` on the candidate towns, and explains any decision it changes.
- Page plan table with keep, create, merge, remove or hold for every page, the target search and a reason. Base town gets no location page. Holds say exactly what proof to collect.
- Fewer pages than the user expected, each with real local detail. No town-swap pages, no pages implying a premises that doesn't exist.
- Briefs have title, H1, opening lines that say what and where, this business's main action above the fold on mobile (call, book, order, reserve or directions), proof, internal links and schema.
- Schema name, address and phone match the profile; hidden-address businesses have no street address in schema.
- Exact-match domain: profile keeps the real business name; site carries the same name; no claim that the domain helps the map pack.
- New sites: coordinates with `new-site` and `seo-demand-keyword-research` rather than doing the build.
- Agency runs: no mention of Mani in client-facing output.
- Plan includes log lines and a before-and-after measurement.
- No em dashes; one plain next-steps line at the end.
