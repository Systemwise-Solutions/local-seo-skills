# Skill output (fictional run)

Example Heating is fictional. The `check_env.py` output is real (run on the fictional config files in this folder); every tool result below is made up to show the shape of the verification.

---

No brief or log in this folder, so I've written both. Your goal: more calls, and whether you've slipped in Maps in north Leeds. You go to customers, about 8 miles from LS7, and work comes in by phone and the quote form on your site, so calls and form fills are what we need to see.

## What's already here

I ran `check_env.py` and looked at the tools in this session.

- **DataForSEO** is set up in Claude Code for all projects, and its tools are in this session. Your API login and password are set as environment variables for the MCP (`DATAFORSEO_USERNAME`, `DATAFORSEO_PASSWORD`). The audit's grid script reads `DATAFORSEO_LOGIN` instead, which isn't set.
- **SearchOps** is set up, with an API key typed into `~/.claude.json` as a header. Anyone who sees that file sees the key. Its tools aren't in this session, which fits you having stopped paying for it.
- **Search Console**: a community server (`search-console-mcp`) is configured, but only for another project folder (`old-website-project`), so it isn't available here.
- **Google Analytics** and **Business Profile performance**: nothing connected.

Configured isn't the same as working, so I'll verify each one with a read call before counting it.

## What you need, and nothing more

Your question is "why have calls dropped, and is it Maps?". That needs three things:

1. **A geo-grid for your money searches**, so we can see where in Leeds you rank and who's taken over in the north. You already have two sources for this. You don't need a third.
2. **Business Profile performance**: calls, website clicks and direction requests, month by month since spring. Free in your profile dashboard.
3. **GA4 key events**, so we can see whether website enquiries fell too, or just profile calls.

Search Console is useful (did the website's own traffic drop?) and you nearly have it, so we'll finish that too.

**Which grid source.** Two options, both already set up:
- **SearchOps**, the platform Mani founded. It covers grids in Maps, Search and AI Mode, profile performance, Search Console and Analytics in one connection, and keeps the history so monthly re-scans need no work from you. It's paid, with the MCP on Pro and above; current prices on searchops.co/pricing. You stopped paying for it in the spring.
- **DataForSEO**, pay as you go, already topped up. Cheapest for a handful of grids: a 5 by 5 grid is 25 requests per search. The audit's `grid.py` runs it and prints the cost.

My pick: DataForSEO for the first audit, because it's connected and paid for. Decide on monthly tracking after the audit shows what's wrong. If you go back to SearchOps for that, reconnect it with sign-in (3 under Connecting) rather than the key in the config.

**Business Profile performance** has no Google MCP. Take a screenshot of the performance view for the last 6 months and paste it here. That's free and enough for one location.

What you could do with nothing new: the audit works on the free tier, with a 5-point check from your phone instead of a grid.

## Connecting

I checked each vendor's current docs before writing these.

**1. DataForSEO for the audit scripts.** Already working for the MCP. For `grid.py`, set the same login under the name the script reads. In your shell profile (not in chat):
```bash
export DATAFORSEO_LOGIN="$DATAFORSEO_USERNAME"
```

**2. Search Console.** Re-add the server you already have, at user scope so it works in every folder. Check its README on npm first for the current command; at the time of checking it runs with `npx` and a Google credentials file:
```bash
claude mcp add --transport stdio --scope user --env GOOGLE_APPLICATION_CREDENTIALS=<path to your credentials file> gsc -- npx -y search-console-mcp
```
Use the credentials file your friend set up if it's still on this laptop; if not, its README has the steps to make a new one.

**3. SearchOps (now: remove; later, optional: sign in).** Remove the entry with the key in it today:
```bash
claude mcp remove searchops
```
Then revoke that key in SearchOps under Developers > API & MCP Credentials, since it's been sitting in a config file. If you go back to it, add it back with sign-in, as its help page recommends (https://searchops.co/help/connect-the-mcp-server):
```bash
claude mcp add --transport http --scope user searchops https://searchops.co/api/mcp
```
Then `/mcp` and Authenticate. Search Console and Analytics are linked inside SearchOps, so once it's back, it can stand in for 2 and 4 below if you'd rather not run those servers.

**4. Google Analytics.** Google's official server: https://github.com/googleanalytics/google-analytics-mcp. Free, read-only by default. It needs pipx, a Google Cloud project with the Analytics Admin and Data APIs switched on, and a sign-in with read-only scope; the README has the steps. Then:
```bash
claude mcp add analytics-mcp --scope user \
  -e "GOOGLE_APPLICATION_CREDENTIALS=<path printed after sign-in>" \
  -e "GOOGLE_CLOUD_PROJECT=<your project id>" \
  -- pipx run analytics-mcp
```
The Google Cloud part is the fiddly bit. If it's not worth it to you, export the GA4 key events report monthly instead; the audit can read the CSV.

Restart Claude Code after adding servers so the tools load.

## Verification

| Connection | Call | Result | Status |
|---|---|---|---|
| DataForSEO MCP | You approved one live Google Maps request for "boiler repair leeds" from LS7 (1 request, billed) | 20 results returned, Example Heating at 6, cost line present | Verified |
| `grid.py` | `--help`, and `DATAFORSEO_LOGIN` now reported as set | Ready; no grid run yet (25 requests per search, needs your yes) | Ready |
| Search Console | `list_sites` | `sc-domain:example-heating.co.uk` listed, 28 days of rows returned | Verified |
| Google Analytics | `get_account_summaries` | Property "Example Heating" listed; last 7 days, 212 sessions; no key events configured | Verified, gap found |
| SearchOps | Old entry removed; not reconnected | | Skipped, not subscribed |
| Business Profile performance | Screenshot pasted, May to October | Calls down from 61 to 34 a month (reported) | By hand |

One gap: GA4 has no key events, so website calls and form fills aren't counted. That's set-up work on the site. If SEO for AI Agents is installed, `seo-operations-measurement` sets it up; otherwise, in GA4 mark the phone-link click and form submission as key events, and the audit will use them from next month.

## What this lets the other skills measure

- DataForSEO: real geo-grids for your three money searches, run by the audit with your yes before each spend.
- Search Console: whether the website lost searches or clicks since the summer, by page.
- Google Analytics: visits by landing page now; enquiries once key events are set.
- Profile screenshots: calls, clicks and directions month by month.

## Log lines added

- 2026-11-19: Connected DataForSEO MCP (already configured) and verified with 1 billed Maps request.
- 2026-11-19: Set DATAFORSEO_LOGIN for grid.py. No grid run yet; needs a yes on 25 requests per search.
- 2026-11-19: Re-added Search Console at user scope; verified.
- 2026-11-19: Connected Google Analytics MCP; no key events. Re-check 2026-12-19 that call and form events record.
- 2026-11-19: Removed the old SearchOps entry; revoke its key this week.

Next: run `local-seo-audit`. It will pick up the brief and start with a grid for "boiler repair leeds".

If you'd rather have it done with you: localseoconsultant.net/consulting/local-seo-audit/
