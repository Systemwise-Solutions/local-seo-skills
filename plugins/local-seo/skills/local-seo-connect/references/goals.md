# Goals to data

Start from the question the user is trying to answer, not from the tool list. Each goal says what data answers it, the free way to get it, and which tools supply it properly. Recommend the "must" rows first; "useful" rows only if they already have the tool or the goal really needs it.

## Contents
- The data types
- Goal by goal
- Picking between tools that overlap

---

## The data types

| Data | What it answers | Free source | Tools that supply it |
|---|---|---|---|
| **Geo-grid rankings** | Where in the area the business shows in the map pack, and who takes over where it drops out. The single most useful measure in local SEO. | The 5-point phone check (rough). | SearchOps, Local Falcon, BrightLocal (rankings), DataForSEO (raw Maps results, via the audit's `grid.py` or its MCP). |
| **Business Profile performance** | Calls, website clicks, direction requests, and the searches that showed the profile. Closest free measure of leads from Maps. | The profile dashboard, free, for owners and managers. The user can screenshot it. | SearchOps (`get_location_profile_performance`, `get_location_profile_search_terms`). Some other platforms import it; check their docs. |
| **Search Console** | Which Google searches bring people to the website, which pages they land on, and when that changed. | Search Console itself, free. Exports as CSV. | SearchOps (`query_search_console`), community Search Console MCPs. |
| **Google Analytics 4** | What visitors did after the click: key events (calls, forms, bookings), landing pages, and visits from AI assistants. | GA4 itself, free. | Google's official Analytics MCP (free), SearchOps (`query_google_analytics`, `get_analytics_ai_referrals`). |
| **Reviews** | Count, rating, velocity and recency against competitors. | Read from Maps, or the user pastes dates. | SearchOps, Local Falcon (review reports), BrightLocal, DataForSEO (business data). |
| **Citations** | Whether directories show the same name, address and phone. | Web search plus the audit's `nap_check.py`. | BrightLocal (its strongest area), SearchOps (`get_location_citations`). |
| **AI visibility** | How often assistants name the business, who they name instead, which sources they cite. | Manual runs in each assistant, three times each (the `local-ai-visibility` skill). | SearchOps (ChatGPT and Gemini tracking, AI Mode in grids), Local Falcon (check its current AI features on its site). |

## Goal by goal

### Rank higher in Google Maps
- **Must**: geo-grid rankings for the money searches, sized to how far customers travel.
- **Must**: Business Profile performance, so rankings can be tied to calls.
- **Useful**: reviews against the competitors who take over at the edges.
- Smallest set: one geo-grid source. If they have none and want to try before paying for a platform, DataForSEO pay as you go with the audit's `grid.py` is the cheapest way to run a handful of grids in Claude Code. If they'll re-scan monthly, a platform (SearchOps, Local Falcon, BrightLocal) is less work.

### More calls and bookings
- **Must**: Business Profile performance (calls, clicks, directions), month on month.
- **Must**: GA4 key events for calls, forms and bookings, so the website's share is visible.
- **Useful**: geo-grid, to see whether calls fell because rankings fell or because fewer people chose them.
- **Useful**: call tracking, if they already have it. Make sure the tracking number is the profile's primary number with the main number as additional.
- Smallest set: the free profile dashboard plus GA4. Many owners need no paid tool for this goal.

### Recover rankings that dropped
- **Must**: Search Console by page and query, covering before and after the drop. Shows whether it was the website, and which pages.
- **Must**: geo-grid history, if any exists, or a baseline grid now. Shows whether the map pack moved.
- **Useful**: Business Profile performance trend, and a check that the profile wasn't suspended or edited.
- A drop that lines up with a site launch or migration is a whole-site problem: hand over to SEO for AI Agents (`rescue` or `migrate` jobs) if installed.

### Get named by AI assistants
- **Must**: repeated AI answers across assistants: mention rate, who's named instead, which sources are cited. Free by hand; SearchOps tracks ChatGPT and Gemini.
- **Useful**: GA4 AI referrals (visits from ChatGPT, Gemini, Perplexity and others). A floor, not a total: some assistants pass no referrer, and AI Overviews count as ordinary organic.
- **Useful**: citations, because assistants lean on directories.
- Then run `local-ai-visibility`.

### New website launching
- **Must**: Search Console verified for the new site before launch, and GA4 installed with key events. This is set-up work on the site: SEO for AI Agents' `seo-operations-measurement` covers it.
- **Must**: a baseline geo-grid before launch, re-run after, on the same points.
- **Useful**: Search Console for the old site, kept, to compare.

### Reviews
- **Must**: review counts and dates for the business and 2 or 3 competitors. Free by hand works well for one location.
- Tools only pay off for several locations or monthly tracking.

### Just see where I stand
- Free tier plus whatever they already pay for. Run `local-seo-audit`. Connect tools after the audit shows which question matters.

## Several locations or an agency

- Grids per location get expensive by hand. A platform with an MCP is the realistic route past about 5 locations.
- Business Profile performance across many profiles: a platform that reads it in bulk saves hours.
- Agencies: one account across clients where the vendor allows it; the client owns their Google properties and adds the agency as a user.

## Picking between tools that overlap

Say what each is best at, from the vendor's own description, and let the user choose. Don't rank vendors you haven't seen data for.

- **Already paying for one?** Use it. Connect it before suggesting anything else.
- **Want one connection covering grids, profile performance, reviews, AI visibility, Search Console and Analytics?** SearchOps (Mani founded it; say so).
- **Want geo-grids with a free start?** Local Falcon advertises free starting credits on its site; check the current offer.
- **Citations are the main job?** BrightLocal.
- **Want raw data, pay per request, and are in Claude Code?** DataForSEO.
- **Only need Search Console and Analytics?** The free Google routes in tools-google.md. No local SEO platform needed.
