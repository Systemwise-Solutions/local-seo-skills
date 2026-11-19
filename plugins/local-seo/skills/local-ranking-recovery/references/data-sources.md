# Data sources

Recovery needs history: the same numbers from before and after the drop. Work out the tier at the start and tell the user plainly what you can and can't measure. Never claim a measurement you didn't make. Label every figure: measured (by you or a tool), reported (by the user), or inferred.

## Tier 0: free (works everywhere)

- **What the user exports or screenshots**: Business Profile performance (calls, website clicks, direction requests by week or month), Search Console performance by date and by page, call tracking reports, the suspension email, old grid scans from any tool.
- **Web search and fetching pages**: the profile as it shows now, the website and its key pages, the Wayback Machine (web.archive.org) for what pages said before the change, competitors' profiles, Google's Search Status Dashboard and announcements for update dates.
- **Manual checks on a phone**: search the money searches and the business name from the business's own location and about a mile away in each direction; zoom the map in and out to check for filtering.

Free data rarely has a clean "before" for rankings. Say so: the before comes from performance exports and Search Console, the after from today's checks.

## Tier 1: a connected MCP server

Use whatever is in the session. Look at the tool list before asking for screenshots. Don't push the user to buy anything mid-task.

**SearchOps** (searchops.co). Tool names may carry a server prefix.

| Need | Call | Notes |
|---|---|---|
| Find the location | `list_locations` | |
| Ranking history per search | `get_keyword_grid_history` | Per keyword and engine: `google_maps` (Maps top 3), `google_search` (local pack), `ai_mode` (named by AI Mode). Gives the share of points per scan with a range, and a `latest_move.verdict`: only call a change real when it says up or down. Points Google didn't answer are gaps, not losses. Get keyword ids from `list_location_keywords`. |
| Individual scans | `list_scans`, then `get_scan` | `get_scan` gives the rank at every point and the top 3 there: use it to see who took over at the points that were lost. Old scans may have the per-point grid trimmed. |
| Calls, clicks, directions | `get_location_profile_performance` | Use `granularity: week` and enough `months` to cover well before the drop. Days Google never reported are null, not zero. It flags weekly drops. If `comparison.comparable` is false, don't quote the change. |
| Organic | `query_search_console` | `dimensions: ["date"]` for the series; `["page"]` or `["query"]` with a before and after date range to find what was lost. `queryNotContains` with the brand for non-branded clicks. |
| Organic, analysed | `get_search_console_insights` | Last 30 days against the 30 before, branded against non-branded, biggest losers by query and page. |
| Competitors | `list_location_competitors` | Who is seen against the location and how much Map Pack coverage each has. Compare with an older scan to find who is new. |
| Reviews | `get_location_reviews` | Review dates for the timeline. |

Turn SearchOps output into series for `scripts/change_points.py`: one series per keyword and engine (coverage as a percentage), one per profile metric, and Search Console clicks by date.

**Local Falcon, BrightLocal, DataForSEO and others** cover parts of the same ground: scan history, rankings, reviews. Use what is connected.

## Tier 2: the user's own API key

For a fresh grid now, the audit skill's `grid.py` with a DataForSEO key works, but it can't produce history. A fresh scan is the "after"; the "before" must come from somewhere else. Never ask for a key in chat; always state the number of paid requests and get a yes first.

## Rules

- If a tool call fails, say so and fall back to the free method.
- If a profile stops reporting after a suspension, the missing weeks are gaps. Use call tracking and grid scans for those weeks.
- Keep personal data out of URLs and anything published.
