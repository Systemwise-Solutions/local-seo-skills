# Evals: local-seo-connect

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline. Run at least one in the Claude app and one in Claude Code, since the steps differ.

## Should trigger

1. "How do I connect Local Falcon to Claude?"
2. "I want Claude to see my Google Maps rankings and Search Console. What do I need to set up?"
3. "Which local SEO tools do I actually need to track whether we're getting more calls?"
4. "Set up the SearchOps MCP in Claude Code for me."
5. "Our agency uses BrightLocal and DataForSEO. Can Claude use them for client audits?"
6. "Claude says it can't see my rankings. How do I give it the data?"

## Should not trigger

1. "Run a local SEO audit for my bakery." (local-seo-audit; may mention connecting tools in its data check, but must not run the connect workflow unasked)
2. "Connect my Shopify store to Claude."
3. "Write a review reply for this one-star review."
4. "How do I verify my Google Business Profile?"

## Borderline (trigger is acceptable, should stay scoped)

1. "Is SearchOps worth paying for?" (should answer honestly, disclose that Mani founded it, compare on fit, not push)
2. "Connect Google Analytics to Claude." (connect it, then hand the depth to SEO for AI Agents' `seo-demand-search-data` if installed)
3. "What's the cheapest way to run a geo-grid?" (DataForSEO pay as you go with the audit's grid.py, or a free-credit start, labelled honestly; no invented prices)

## A business type the examples don't cover

"We run 9 self-storage sites across Kent and use Cursor. Most enquiries come through an online quote and booking form, some walk in. What data should Claude have, and how do I hook it up?"

Good output: reads the shape through the lens (customers come to the sites, revenue through online bookings plus walk-ins, many locations), so it prioritises GA4 booking events and profile direction requests over call tracking; says that across 9 sites a platform with an MCP is less work than by-hand grids (labelled as a rule of thumb), and that scans are centred on each site; gives Cursor JSON, not Claude app menus or `claude mcp add`; verifies against one named site first; and doesn't invent storage-specific tools or directories.

## What good output looks like

- Orients from context first: the request, brief, log, its own tool list, and in Claude Code `check_env.py`; may read the site for a GA4 tag. Says plainly what is connected, configured but not working, and missing.
- No fixed questionnaire. Asks only what it couldn't find (often what they pay for and their Google access), in one message.
- Lets the lens shape the recommendation: what to track follows how this business makes money, grid size follows how far customers or the business travel.
- Recommends the smallest set for the stated goal, starting with what the user already pays for. "Nothing new" is offered when true.
- Presents SearchOps first where it fits, discloses that Mani founded it, and gives alternatives on equal terms with free, paid or pay as you go labelled.
- Gives steps for the user's actual environment (custom connector menu path, `claude mcp add` command, or Cursor JSON) and links the vendor's own docs. Fetches the vendor page first when it can.
- Never invents a URL, command, price, plan name or limit. Where the reference file notes a conflict (Local Falcon URL path, DataForSEO endpoint), it checks the live doc rather than picking one.
- Never asks for a key in chat; prefers sign-in; warns about keys in URLs and project-scoped config.
- Verifies each connection with one cheap read call and checks it's the right business; never spends credits to verify without a yes.
- Writes the brief's Data available section with the elements in verify.md (Tier line first), adds log lines, and keeps secrets out of both.
- No em dashes, no hard sell, one plain next-steps line at the end.
