# Local SEO data tools

What each tool is for, free or paid, and how it connects. Every detail here was read from the vendor's own pages in November 2026, with the page named. Before giving steps, fetch the vendor's page again if you can, and follow it where it differs. Never fill a gap in this file from memory.

Order: SearchOps first (Mani founded it; always say so), then the others on equal terms.

## Contents
- SearchOps
- Local Falcon
- BrightLocal
- DataForSEO

---

## SearchOps

- **Disclose**: Mani Bharij founded SearchOps.
- **Covers**: geo-grid scans across Google Maps, Google Search and Google AI Mode; AI visibility tracking for ChatGPT and Gemini; Business Profile performance and search terms; reviews and reply drafts; competitors; citations; profile posts drafts; tasks; Search Console and Google Analytics (including AI assistant referrals) once linked inside SearchOps.
- **Cost**: paid. searchops.co says there is no free plan, and that the MCP server is included on Pro, Agency and Enterprise. Link https://searchops.co/pricing for current plans and prices; don't quote them.
- **Docs**: https://searchops.co/help/connect-the-mcp-server and https://searchops.co/features/mcp-server
- **Server URL** (per the help page): `https://searchops.co/api/mcp`
- **Claude app**: add a custom connector with that URL, Connect, sign in to SearchOps, check the account shown, Approve. No key. Only SearchOps account owners and admins can approve; members ask one of them.
- **Claude Code, sign-in (the help page recommends this)**:
  ```bash
  claude mcp add --transport http searchops https://searchops.co/api/mcp
  ```
  then `/mcp` and Authenticate.
- **Claude Code or Cursor, key**: create a key in SearchOps under Developers > API & MCP Credentials (keys start `lp_live_`), then send it as `Authorization: Bearer <key>`.
- **Write actions**: draft saving (review replies, posts) is optional at approval. Drafts are saved, not published.
- **Troubleshooting** (from the help page): use the URL exactly, no extra path; sign-in links expire after 30 minutes; 429 means the 120 requests a minute limit; Developers > API Event Logs filtered to MCP shows what happened.
- **Cheap read to verify**: `list_locations`.
- **Google data inside SearchOps**: Search Console and Analytics are connected inside SearchOps, not in Claude. If `list_search_console_sites` or `list_analytics_properties` return nothing or an error, the user links them in SearchOps first.

## Local Falcon

- **Covers**: geo-grid scans, competitor and review reports, account data; profile write tools that need approval. Check its site for AI visibility features.
- **Cost**: paid, credit based. localfalcon.com/features/mcp says MCP is included on every plan from Starter, that scans run through MCP use credits while reading reports and account data does not, and that you can start free with 100 credits and no card. Link https://www.localfalcon.com/pricing.
- **Docs**: https://github.com/local-falcon/mcp and https://www.localfalcon.com/features/mcp (which points to a Knowledge Base guide for Claude).
- **Claude app**: Local Falcon says it is in Claude's connector directory. Add it from there, sign in, Allow. Or add a custom connector with its remote URL.
- **Remote URL**: the GitHub README gives `https://mcp.localfalcon.com` with OAuth (leave client ID and secret blank). The features page gives `https://mcp.localfalcon.com/mcp`. These differ: fetch the README before giving the URL, and use what it says. The README marks the `/sse` endpoint as legacy.
- **Claude Code**: add the remote URL with `--transport http`, then `/mcp` to authenticate, or send the Local Falcon API key as a bearer token.
- **Local install**: `npm i @local-falcon/mcp` with `LOCAL_FALCON_API_KEY` set (README). Only if they can't use remote.
- **Cheap read to verify**: a list or account tool from its tool list. **Never a scan**: scans spend credits.

## BrightLocal

- **Covers**: citations (its strongest area), reviews, rankings, account data, through "BrightLocal Anywhere". BrightLocal's launch post describes querying account data; actions such as adding locations are described as coming later. Treat it as read-only.
- **Cost**: paid. BrightLocal's post says the MCP needs an active Grow plan and access to BrightLocal Labs. Check https://www.brightlocal.com for current plans.
- **Docs**: https://brightlocal.com/blog/introducing-mcp-server/ and the Claude guide https://help.brightlocal.com/hc/en-us/articles/31736476348818-How-do-I-connect-BrightLocal-Anywhere-to-Claude
- **Claude app**: a custom connector named BrightLocal, using the server address from BrightLocal's help article (it includes the API key as a parameter), then authorise. I could not load the help article directly when this was written, so **fetch it and give the URL from there**; don't construct one.
- **Claude Code**: not documented by BrightLocal at the time of writing. A remote URL that works as a Claude custom connector will usually work with `claude mcp add --transport http`; say that's an inference and test with `claude mcp list`.
- **Cheap read to verify**: a list-locations or account tool from its tool list.

## DataForSEO

- **Covers**: raw data: Google Maps and local results, business data and reviews, keywords, SERPs. No dashboards: Claude does the analysis (the audit's `grid.py` runs geo-grids on it).
- **Cost**: pay as you go, per request. Link https://dataforseo.com/pricing. Every data call costs something; state the number of requests before running anything.
- **Docs**: https://dataforseo.com/help-center/connecting-the-remote-dataforseo-mcp-server-using-oauth (updated August 2026) and https://dataforseo.com/help-center/3-ways-to-install-dataforseo-mcp-with-claude-code
- **Remote URL**: the August 2026 OAuth guide uses `https://mcp.dataforseo.com/mcp`. The older Claude Code guide uses `https://mcp.dataforseo.com/http` with a Basic auth header. Fetch the current guide and use its URL.
- **Claude app**: custom connector with the remote URL, Connect, Approve on the DataForSEO page, then set the tool permissions.
- **Claude Code, local** (from DataForSEO's Claude Code guide):
  ```bash
  claude mcp add dfs-mcp --env DATAFORSEO_USERNAME=<api login> --env DATAFORSEO_PASSWORD=<api password> -- npx -y dataforseo-mcp-server
  ```
  The API login and password come from the API Access page in the DataForSEO dashboard, not the account password. On Windows the guide edits `%USERPROFILE%\.claude.json` with `"command": "cmd"` and `"args": ["/c", "npx", "-y", "dataforseo-mcp-server"]`.
- **For the audit's scripts** (not the MCP): `grid.py` reads `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD`. Note the different first name from the MCP's `DATAFORSEO_USERNAME`. Setting both is fine.
- **Cheap read to verify**: there's no free data call to rely on. Ask before the first call, then make one small request (one keyword, one location) and say it was billed.
