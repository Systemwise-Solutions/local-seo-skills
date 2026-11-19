# Google data: Business Profile, Search Console, Analytics

All three are free from Google. Getting them into Claude is the hard part: Google publishes an official MCP for Analytics, not for Search Console or Business Profile (as of November 2026). Fetch the linked pages before giving steps.

For anything beyond connecting (choosing the right property, reading and interpreting the data, site-wide search problems, installing GA4 or verifying the site), SEO for AI Agents covers it: `seo-demand-search-data` reads whatever Search Console or GA4 source is connected, with setup recipes in its orchestrator's data references, and `seo-operations-measurement` sets up GA4 and Search Console on the site. Hand over if installed.

## Contents
- Business Profile performance
- Google Analytics 4
- Search Console
- The no-setup option: exports

---

## Business Profile performance

- **Free**: calls, website clicks, direction requests and the searches that showed the profile are in the profile's own performance view, for owners and managers.
- **Into Claude**: no official Google MCP for Business Profile that this skill knows of. Routes: SearchOps reads it (`get_location_profile_performance`, `get_location_profile_search_terms`) once the profile is linked inside SearchOps; or the user screenshots or exports the performance view each month and shares it.
- **Access check**: the user must be an owner or manager on the profile. If an agency or old web designer is the only owner, getting ownership back comes first.

## Google Analytics 4

- **Official server**: Google's Analytics MCP, https://github.com/googleanalytics/google-analytics-mcp. Free. Local Python server, so Claude Code, Cursor or the Claude desktop app, not the web app.
- **What it needs** (from the README): pipx installed; the Google Analytics Admin API and Data API enabled in a Google Cloud project; Application Default Credentials for a Google user with access to the property, with the `analytics.readonly` scope (`gcloud auth application-default login --scopes ... --client-id-file=...`). The README walks through it; send the user there for the credential steps rather than retyping them.
- **Claude Code** (README's command):
  ```bash
  claude mcp add analytics-mcp --scope user \
    -e "GOOGLE_APPLICATION_CREDENTIALS=<path to credentials json>" \
    -e "GOOGLE_CLOUD_PROJECT=<project id>" \
    -- pipx run analytics-mcp
  ```
- **Read-only by default**: write tools (`create_property_annotation`, `create_custom_dimension`, `create_key_event`) need a start flag and the edit scope. Leave them off.
- **Cheap read to verify**: `get_account_summaries`, then confirm the property for this website is in the list.
- **Easier route if they use SearchOps**: link GA4 inside SearchOps and use `list_analytics_properties` and `query_google_analytics`. No Google Cloud project needed.
- Honest effort note: the Google Cloud setup takes a non-technical owner a while. If the goal only needs a monthly number, an export (below) is fine.

## Search Console

- **No official Google MCP.** Community servers exist; they're open source, free, unofficial, and vary in maintenance. Examples found in November 2026 (check each repo's README, last commit and auth method before recommending):
  - `search-console-mcp` on npm (runs with `npx`, uses Google credentials)
  - `mcp-google-search-console` on PyPI (one-time interactive sign-in, then runs with `uvx`)
  - `@infinitnet/google-search-console-gsc-mcp-server` on npm (browser sign-in on first use)
- Most need a Google Cloud OAuth client or service account the user creates; the README for the chosen server has the steps. Prefer one that's read-only. Don't recommend a server you haven't looked at in this session.
- **Cheap read to verify**: the server's list-sites tool, then confirm the site is listed and the property type (domain or URL prefix) is the one with data.
- **Easier route if they use SearchOps**: link Search Console inside SearchOps and use `list_search_console_sites` and `query_search_console`.

## The no-setup option: exports

For one location and a monthly check, an export beats an afternoon of Google Cloud setup:
- Search Console: Performance > Export, last 3 or 16 months, by query and by page.
- GA4: a landing page report filtered to organic search, and the key events report.
- Business Profile: a screenshot of the performance view.

Mark data from exports as "reported" in the brief, with the date range.
