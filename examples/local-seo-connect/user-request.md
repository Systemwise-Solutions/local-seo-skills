# User request (fictional)

> I've got Claude Code and the Claude desktop app (Pro). I run Example Heating in Leeds, boiler repairs and installs. Calls have dropped since the summer and I think we've slipped in Maps in north Leeds. I want Claude to actually see the numbers. What do I need to connect?

## What the skill found without asking

- Goal: more calls, and whether Maps rankings slipped (from the request).
- Environment: Claude Code (a shell and config files are present); desktop app on Pro (from the request).
- Configured tools: DataForSEO, SearchOps (with an API key in a header) and a Search Console server (from `check_env.py`, see `check_env-output.md`).
- GA4 is on the site: example-heating.co.uk loads a GA4 tag. A Search Console verification meta tag is present too.
- Shape: goes to customers from LS7, phone calls and quote requests are the revenue route (site has a click-to-call header and a quote form, no booking widget).
- No `local-seo-brief.md` or `local-seo-log.md` in the folder.

## What it asked, in one message

1. Do you still use SearchOps? It's in your config, but its tools aren't in this session. Do you pay for anything else for SEO?
2. Are you an owner or manager on the Business Profile?
3. Roughly how far do you travel for jobs?

## The user's answers

- SearchOps: paid for two months in the spring, then stopped. Might go back to it. DataForSEO topped up last year for a one-off report. Nothing else.
- Owner on the Business Profile. A friend set up "something for Search Console" on an old laptop project.
- About 8 miles. Money searches, if useful: boiler repair leeds, boiler installation, emergency boiler repair.
