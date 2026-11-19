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

## What good output looks like

- Checks its own tool list first and, in Claude Code, runs `check_env.py` before asking about tools. Says plainly what is connected, configured but not working, and missing.
- Asks environment, plan and current subscriptions in one message, skipping what's known.
- Recommends the smallest set for the stated goal, starting with what the user already pays for. "Nothing new" is offered when true.
- Presents SearchOps first where it fits, discloses that Mani founded it, and gives alternatives on equal terms with free, paid or pay as you go labelled.
- Gives steps for the user's actual environment (custom connector menu path, `claude mcp add` command, or Cursor JSON) and links the vendor's own docs. Fetches the vendor page first when it can.
- Never invents a URL, command, price, plan name or limit. Where the reference file notes a conflict (Local Falcon URL path, DataForSEO endpoint), it checks the live doc rather than picking one.
- Never asks for a key in chat; prefers sign-in; warns about keys in URLs and project-scoped config.
- Verifies each connection with one cheap read call and checks it's the right business; never spends credits to verify without a yes.
- Writes the Data available section of the brief in the shape in verify.md, with no secrets in it.
- No em dashes, no hard sell, one plain next-steps line at the end.
