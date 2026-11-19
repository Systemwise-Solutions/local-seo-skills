# Orient: what the page plan needs, and where to find it

Find each piece yourself first. Ask the user only for what you can't find, in one message, and say why you need it. If you can't get something, say what the plan will do without it rather than stalling.

| The plan needs | Look here first | Why it matters |
|---|---|---|
| The exact business name, as on the profile and signage | The profile, the site header and footer, the brief | Schema, headers and the profile must match character for character. |
| What it sells, and roughly what share of revenue each service or product line brings | Site navigation, service or product pages, price lists, the brief; then the user | A service gets a page when it brings money the business wants. Rough shares are enough. |
| The searches that bring revenue | The profile's search terms, Search Console queries, competitors' page titles, the brief | Each page targets one of these. Searches only existing customers use don't justify a page. |
| Customers come to the business, or it goes to them | Address shown or hidden on the profile, site copy, "areas we cover" sections | Decides whether area pages can exist at all, and whether they may carry an address. |
| How far customers travel, or the business travels | Site copy, the profile's service area, delivery or booking radius, the user | Sets the outer edge of the candidate list for `town_score.py`. |
| Where the work or customers actually are | Job software, booking system, order or delivery data, invoices, CRM; then the user | Decides location pages. Without it, plan service pages only and hold location pages. Counts by town or postcode are enough. |
| What proof exists, per service and per place | Gallery, case studies, reviews (which name places?), price pages, credentials on the site; then the user | Proof is what lets a page earn its place. Mark each item supplied or needed. |
| Rules on what it can say | Any regulator, professional body or platform named on the site; the brief | Shapes service names and claims. Find the rule before writing copy. |
| One location or many | Location pages, store finder, profiles | Each staffed location gets its own page; area pages are worked out per location. |
| What pages exist now | In a coding project: the routes, page files, CMS collections, templates and redirect config. Otherwise the sitemap, the navigation and a `site:` search | Generated or templated location pages often hide outside the navigation. Find them all before deciding. |
| Which page the profile links to | The profile's website link | That page carries the profile, so it is decided first. |
| Whether the site is existing, being rebuilt or new, and the domain | The repo, the live site, the user | A new site or rebuild means coordinating with SEO for AI Agents (see SKILL.md). An exact-match domain means checking the profile name first. |
| Who the plan is for | The conversation, the brief | Owner, in-house team or agency client changes the wording and the owners named, not the method. |
| What's already been tried | `local-seo-log.md`, the user | So you don't recreate a page that was removed for a reason, or remove one that works. |

## When you're working in the site's code

Read before you write. Work out how pages are made (static files, a framework's routes, a CMS collection, a template fed by a data file), where redirects live, and where schema is output. A location page template driven by a list of place names is the most common source of town-swap pages; if you find one, count how many pages it makes and how much of each page differs.

## Writing the brief

Write what you learned to `local-seo-brief.md` in plain lines, under 40 lines: the business, the shape from the lens, money searches, area, competitors, audience, data available, constraints. Add a short "Pages" note: existing, rebuild or new (and the domain), rough revenue by service, where the work is, the page the profile links to. Other skills read it, so use plain labels rather than a fixed form. If a brief exists, update it rather than replacing it.
