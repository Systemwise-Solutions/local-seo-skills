# Data sources

The skill works with nothing but Claude. Better data shortens the asking and sharpens the competitor comparison. Work out the tier at the start and say in two lines what you can and can't see.

## Tier 0: free

- **The user's own profile.** Ask for screenshots of the edit screens: business information (name, categories, description, opening date), contact (phone, website), location and areas, hours (regular, holiday, more hours), more (attributes), services, products. This is the only reliable free source for the business's own secondary categories and services.
- **Competitors on Maps.** Search each money search on Maps from the business's area (or ask the user to, on their phone, and screenshot). The primary category is shown under the business name. Services, products, photos, review count and recent posts are visible on the profile.
- **Competitors' secondary categories.** Not shown on Maps. Free category-viewer browser extensions read them from the page; if the user has one, ask them to screenshot it, following that extension's own instructions. If not, compare primaries and services only, and say so under "Not checked".
- **What people search.** The profile's performance tab shows the searches that found it (free for the owner). Google's autocomplete and "people also search for" show how customers phrase services.
- **The website.** Fetch it: which service pages exist, what the page the profile links to says.

## Tier 1: a connected MCP

Use whatever is connected before asking for screenshots.

**SearchOps** (searchops.co). Tool names may carry a server prefix.
- `list_locations`, then `get_location_summary` for the headline picture.
- `list_location_competitors`: rivals seen across grid scans, Google Search and ChatGPT, with `map_pack_coverage`. Use it to choose the three to beat. It doesn't give their categories.
- `get_location_profile_search_terms`: what people typed when the profile showed, by month. Use non-branded terms to name services. Small counts come back as below threshold: never treat them as zero.
- `get_location_profile_performance`: calls, website clicks, directions, bookings and views, by month or week. The baseline before the first edit.
- `list_location_posts`: post cadence, including posts made outside SearchOps. A null cadence means unknown, not none.
- `save_post_draft`: saves a post as a draft for a person to add a photo and publish. It strips phone numbers, emails and links from the text because Google rejects posts with them. Only when the user asks, after showing the text.
- `get_location_week`, `list_tasks`, `create_task`: this week's numbers beside the work, and the change log as tasks with due dates (only with a yes; check `list_tasks` first).

**Local Falcon** (official MCP) and **BrightLocal** cover competitor and ranking data; Local Falcon also has profile write tools with approval. Never make a live profile edit through a tool without the user approving that specific edit.

**DataForSEO MCP** or **Google Maps results from any business-data tool** often return each business's primary and additional categories. That fills the secondary-category gap.

## Tier 2: the user's own DataForSEO key

In Claude Code, a Google Maps live search returns category and additional categories for each result in the map pack. One request per search per location. Tell the user the number of requests first and get a yes. Keys go in environment variables, never in chat. Follow DataForSEO's own docs for setup.

## Rules

- Never claim to have seen a field you didn't see. If a screenshot cuts off, say what's missing.
- If a tool call fails, say so and fall back to the free method.
- Keep personal data out of URLs and anything published.
