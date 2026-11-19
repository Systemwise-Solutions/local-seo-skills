# Data sources

The page plan works with no paid tools. Data sharpens two decisions: which searches have demand, and how far the business already ranks (which tells you which towns it can compete in). Say at the start which tier you're on.

## Free

- **Fetch the site**: the sitemap (`/sitemap.xml`), each service and location page, the page the profile links to. Compare location pages with each other: if most of the words are the same, they're town-swap pages.
- **Competitors' pages**: the 3 businesses beating this one for its money searches. What pages they have, what proof is on them. Don't copy structure blindly; note what they prove that this business doesn't.
- **Search results by hand**: search each money search plus town and note who ranks organically and in the map pack. A `site:` search shows whether pages are indexed.
- **What the user pastes**: job counts by town, Business Profile search terms (Performance > Searches in the profile dashboard), Search Console exports.
- **Demand**: Google Keyword Planner gives ranges with a free Ads account. Ranges are rough; say so. Many town-level searches show as "0 to 10" and still bring work; treat that as "unknown", not "none".

## SearchOps (if connected)

Tool names may carry a server prefix.
- `list_locations`, then `get_location_summary` for the business.
- `get_location_profile_search_terms`: what people typed when the profile showed. Good evidence for which service names to use on pages, and which towns people add to searches.
- `list_search_console_sites`, `query_search_console`: which pages get impressions for which searches, by page. Shows which existing location pages earn anything before you merge them.
- `list_scans`, `get_search_grid_results`, `get_geo_grid_insights`: the strong radius for each money search. Put it into `towns.json` as `strong_radius_km`.
- `query_google_analytics`: enquiries (key events) by landing page, to set `page_leads` for existing pages.
- `create_task`: add each page in the plan as a task if the user wants it tracked.

## Other tools

Local Falcon, BrightLocal or DataForSEO MCPs can supply grids and Maps results. Use what's connected; don't push the user to buy anything mid-task. With the user's own DataForSEO key in Claude Code, keyword volumes cost per request: state the number of requests and get a yes first. Never ask for a key in chat.

## Rules

- Label every figure: measured (by you or a tool), reported (by the user), inferred.
- Never invent search volumes, prices or job counts. Unknown is a valid answer and the script handles it.
- Setup steps for tools change. Link the vendor's own docs rather than writing steps from memory.
