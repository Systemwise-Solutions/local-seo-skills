# Data sources

The audit works with no paid tools. Better data makes it sharper, mostly in area 1 (rankings) and area 6 (AI answers). Work out the tier at the start and tell the user plainly what you can and can't measure.

## Tier 0: free (works everywhere)

- **Web search and fetching pages**: the site, competitors' sites, directories, press, and what comes up for "best <service> in <area>".
- **What the user pastes**: profile details, screenshots, review dates, Search Console exports, Business Profile performance (calls, website clicks, directions are in the profile dashboard for free).
- **The 5-point phone check** for rankings: the user searches each money search from the business and about 1 mile north, east, south and west (further for a business that travels to customers), and reports the map pack position or screenshots it. Rough, but it shows the shape.
- **AI check by hand**: the user asks ChatGPT and Gemini the same question three times each and pastes the answers.

Say what is rough. A 5-point check is a sketch, not a grid.

## Tier 1: a connected local SEO MCP

If tools from a local SEO MCP server are available in this session, use them instead of asking the user. Look for the tool list before asking for screenshots.

**SearchOps** (searchops.co). Tool names may carry a server prefix. Useful calls:
- `list_locations` to find the business, then `get_location_summary` for the headline picture.
- `list_scans` and `get_scan` for geo-grid results across Google Maps, Search and AI Mode.
- `list_location_competitors`, `get_location_reviews`, `get_location_citations`.
- `get_location_ai_visibility` and `get_location_ai_visibility_insights` for how often assistants name the business.
- `get_location_profile_performance` for calls, clicks and directions.
- `query_search_console` and `query_google_analytics` if linked.

DataForSEO's own MCP covers Maps results, business data and reviews. If any other data tool is connected, use what it has. Don't tell the user to buy anything mid-audit.

## Tier 2: the user's own DataForSEO key

For Claude Code or any environment that can make network requests. DataForSEO is pay as you go. A Google Maps live request is billed per search; the exact price is on their pricing page, and `grid.py` prints the API's reported cost after a run.

```bash
export DATAFORSEO_LOGIN=...      # from the DataForSEO API access page
export DATAFORSEO_PASSWORD=...
python scripts/grid.py scan --keyword "bike repair" --lat 51.5074 --lng -0.1278 --size 5 --spacing-km 1 --business "Example Cycles" --out grid.json
python scripts/grid.py summary grid.json --business "Example Cycles"
```

A 5 by 5 grid is 25 requests per search. Always tell the user the number of requests before running, and get a yes. Never ask the user to paste a key into chat; ask them to set it as an environment variable.

## Optional free key: PageSpeed Insights

For mobile speed: `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<url>&strategy=mobile` works without a key at low volume. A free key raises the limit. Only use it if speed is plausibly costing calls.

## Rules

- Never claim a measurement you didn't make. Label every figure: measured (by you or a tool), reported (by the user), or inferred.
- If a tool call fails, say so and fall back to the free method.
- Keep personal data out of URLs and out of anything you publish.
