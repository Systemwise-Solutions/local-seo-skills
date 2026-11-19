# Data sources

Works with nothing but Claude. Tools save the user copying dates by hand.

## Tier 0: free

- **The business's reviews.** The owner sees every review, its date and reply in the Business Profile. Ask for a screenshot of the reviews tab sorted by newest, or for the dates, ratings, text and reply dates pasted in. 6 months is enough.
- **Competitors' reviews.** On Google Maps, open each competitor, Reviews, sort by Newest. The dates show as "2 weeks ago", "a month ago": the scripts accept those. The count and rating show at the top. Get 20 to 30 recent dates each; fewer for a quiet competitor is fine, say so.
- **Request counts.** The SMS tool, booking system or job app usually shows how many messages went out. Without these you can see that reviews fell, but not which step failed.

Relative dates are rough ("a month ago" covers several weeks). Say so when the gap is close.

## Tier 1: a connected MCP

**SearchOps** (searchops.co). Tool names may carry a server prefix.
- `get_location_reviews`: totals, average rating, rating distribution and the most recent reviews (up to 100), with which have no owner reply.
- `list_location_competitors`: rivals seen across grid scans, Search and ChatGPT. Use it to pick the three to compare. Competitor review dates still come from Maps or another tool.
- `draft_review_reply`: SearchOps's own reply agent drafts one reply in the location's saved style. One review per call, only when asked.
- `save_review_reply_draft`: saves a reply you wrote as a draft in the Reply Inbox. Only when asked, after showing the text. It flags staff names and contact details Google tends to reject.
- `list_tasks`, `create_task`, `update_task`: the monthly routine and removal follow-ups as tasks.

**BrightLocal MCP** (read-only) and **Local Falcon** have competitor review reports. **DataForSEO** has a Google reviews endpoint that returns review dates for any business (paid per request: state the number and get a yes first; keys in environment variables, never in chat).

## Rules

- Never claim a measurement you didn't make. Label figures measured, reported or inferred.
- If a tool call fails, say so and fall back to the free method.
- Review text and reviewer names are personal data. Keep them out of URLs and anything published; quote only what's needed.
