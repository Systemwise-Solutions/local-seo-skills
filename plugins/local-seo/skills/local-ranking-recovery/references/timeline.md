# Building the timeline

One dated list of everything that changed, from 90 days before the drop to today. Most recoveries are solved here. Collect first, judge later: an event that looks irrelevant (new opening hours, a new staff member with access) is often the one that matters.

Mark each date `confirmed` (from a log, an email, an edit history, a published notice) or not. A remembered "sometime in August" is still useful; record it as the first of the month with `"confirmed": false`.

## Event types and where to find the dates

| Type (for the script) | What to look for | Where the date comes from |
|---|---|---|
| `profile_edit` | Name, primary or secondary category, address, service area, hours, phone, website link, services, description. Also edits Google made itself ("Google updated your profile") and edits suggested by the public that went live. | The profile's own notices and edit prompts, emails from Google to the profile owners, the person or agency who made the change, screenshots. Ask who has access: managers, former staff and old agencies all can edit. |
| `suspension` | Profile removed from Maps (hard), or still visible but the owner can't manage it, or edits stop going live (soft). Google's wording for these states changes; record what the notice says. | The email from Google, the notice in the profile manager. |
| `verification` | Google asking for re-verification, video verification, or a verification that failed. | Emails, the profile manager. A request often follows an edit to name, address or category. |
| `merge` | Duplicate listings merged or removed, a practitioner listing merged into the business, two businesses combined. Reviews or the name may have moved. | Emails, support case history, review count jumping or falling on one date. |
| `website` | Redesign, new platform, URL changes, pages removed or merged (especially location and service pages), noindex or robots changes, new domain, changed name, address or phone on the site, the profile's website link now redirecting or 404ing. | Developer or CMS deploy logs, the launch date, Search Console's page indexing report, the Wayback Machine (web.archive.org) for what the page said before. |
| `google_update` | Confirmed Google algorithm or core updates. | Google's Search Status Dashboard and Google's own announcements, checked with web search. Never from memory. Local ranking changes are often not announced at all; don't fill the gap with a guess. |
| `reviews` | Reviews removed (count drops on a date), a sudden run of negative or fake reviews, a review request routine started or stopped. | Review dates from the profile or a review tool; the user's records of total count over time. |
| `competitor` | A new competitor opens nearby, a competitor moves closer, a competitor adds keywords to its name, a competitor adds your category. | Grid results over time (who took over at the points you lost), the competitor's profile, the user's local knowledge. |
| `filtering` | Another business at the same address or very close in the same category (a co-located practice, a franchisee, a former tenant's listing, a duplicate). Google tends to show one and hide the others. | Search the main money search from the business's own location and zoom the map in and out; check for listings at the same address. |
| `measurement` | Call tracking number changed or broken, profile disconnected from a reporting tool, Analytics or Search Console changes, a new website without tracking. | The tool's settings history, the call tracking provider. Rule this out first: it is the cheapest cause to find. |
| `other` | Moved premises, rebrand, seasonal closure, staff change, opening hours cut, a phone line fault. | The user. |

## The series

For the script, collect dated values for as many of these as you can, from at least 8 weeks before the drop to now. Weekly is the best grain; monthly will do but hides cliffs.

| Series | Surface | Free source | With tools |
|---|---|---|---|
| Profile calls, website clicks, direction requests | `profile` | Business Profile performance screens (the user exports or screenshots them) | SearchOps `get_location_profile_performance` with `granularity: week` |
| Maps top-3 coverage per money search | `maps` | Not available free unless old grid scans exist | SearchOps `get_keyword_grid_history` (engine `google_maps`), `list_scans` |
| Local pack coverage | `local_pack` | Not available free | `get_keyword_grid_history` engine `google_search` |
| AI Mode named at N of M points | `ai_mode` | Not available free | `get_keyword_grid_history` engine `ai_mode` |
| Search Console clicks, non-branded and branded separately | `organic` | Search Console export by date (the user exports it) | `query_search_console` with `dimensions: ["date"]` and `queryNotContains` set to the brand |
| Calls from a call tracking number | `profile` | The call tracking provider's report | Same |

Average grid rank is accepted (set `higher_is_better: false`) but coverage is the better series: "average position 4.2" can mean first at the door and gone a mile away.

## Gaps

A week Google didn't report is a gap, not zero. Record it as `null`. A suspended profile often stops reporting entirely, so use call tracking and grid scans for the weeks after a suspension.
