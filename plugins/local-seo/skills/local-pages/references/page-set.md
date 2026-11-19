# Deciding the page set

## Contents
1. The principle
2. Service pages
3. Location pages
4. Keep, create, merge, remove, hold
5. Which page the profile links to
6. Multi-location brands

---

## 1. The principle

Every page has to earn its place: a search people make, money behind it, and something to say that a competitor couldn't copy. Fewer, deeper pages beat many thin ones. One strong page per core service, and location pages only where the business genuinely works and can show it. Often that's fewer pages than the owner expects.

## 2. Service pages

A service gets its own page when all three are true:

| Test | How to check |
|---|---|
| People search for it by name | It appears in the profile's search terms, Search Console, a keyword tool, or competitors rank pages for it. "Boiler installation" yes; "magnetic filter fitting" usually no. |
| It brings in revenue the business wants | From the owner's revenue split. A service they'd rather not do doesn't get a page, however much demand. |
| There is enough to say | What it involves, who does it, how long it takes, price guidance, photos, questions customers ask. If it's two sentences, it's a section on another page. |

Rules of thumb:
- **Split by intent, not by synonym.** "Boiler repair" and "boiler installation" are different customers and get different pages. "Boiler repair" and "boiler fix" are the same page.
- **Emergency is a page only if it's real.** If the business genuinely answers out of hours, an emergency page with the actual hours and call-out price can work. If not, don't create it, and don't put "24/7" anywhere.
- **Regulated work.** UK clinics: pages name the concern or the consultation ("frown lines", "anti-wrinkle consultation"), not prescription-only medicines.
- **Merge thin services** as sections on the closest page, with a jump link, so the main page gets stronger.
- **Brand names and products** (a boiler brand, a filler brand) only get pages if people search for them with intent to buy locally and the business is an approved installer or provider.

## 3. Location pages

A location page is for a town or area where the business can compete and has something specific to say. Run `scripts/town_score.py` on the candidate list.

**Can compete**
- Close enough: within the distance the business travels, and ideally inside or near the strong radius from a grid. Far beyond it, the page has to win in organic results; the map pack is unlikely there.
- Real work there: jobs or customers in the last 12 months (or since launch).
- Competition known where possible: who ranks for the service plus town.

**Something specific to say** (local proof, the script counts these)
- 3+ jobs there with photos: what was done, the street or area, the problem, the result.
- 2+ reviews that name the town.
- 2+ facts specific to the place: housing stock ("Victorian terraces with back boilers"), parking and access, local rules (conservation areas, HMO licensing), travel time, landmarks for directions.
- A team member or depot there (a bonus, not required).

**Never**
- A page per town on a list with the name swapped in. That is a doorway page. It gets filtered, it dilutes the pages that sell, it gives AI assistants nothing to quote, and on a large scale it can pull the whole site down.
- A page that implies a premises where there isn't one.
- A page for the base town. The homepage and service pages already target it.

**Big city, one domain.** A city name in the search ("boiler repair leeds") is usually best served by the homepage or the main service page, not a separate city page competing with it. Location pages are for neighbourhoods and towns where the work is.

**Service and location combined** ("boiler installation Headingley") only for the top service in a strong location with enough jobs of that type to show. Otherwise one location page covering the services done there, linking to each service page.

## 4. Keep, create, merge, remove, hold

| Action | When |
|---|---|
| **Keep** | The page targets a real search, says what and where, and has proof. Note improvements. |
| **Create** | A service or location passes the tests above and has no page. |
| **Merge** | Two pages target the same search, or a thin page has a natural home. Move anything useful into the stronger page, 301 the old URL. |
| **Remove** | Town-swap pages and pages for places the business doesn't serve, with no leads and nothing worth moving. 301 to the closest service page (or 410 if nothing is relevant and it has no links). |
| **Hold** | Worth a page once proof exists. Name exactly what to collect, and when to revisit (usually after 3 more jobs there, or at the next quarterly review). |

Before removing a page, check it hasn't been bringing leads (Search Console clicks, analytics key events by landing page, or the owner's own records). A town-swap page that brings enquiries is rebuilt with real detail, not deleted.

Removing dozens of thin pages at once is normal and usually good for the pages that stay. Say so, so the owner isn't alarmed by the page count dropping.

## 5. Which page the profile links to

- One location, one dominant service: the profile links to that service's page, or the homepage if the homepage leads with it.
- One location, several money searches: the homepage, but only if it clearly says what and where and links prominently to each service page. Otherwise the top revenue service.
- Exact-match domain: usually the homepage, which targets the main service in the city.
- Multi-location: each profile links to its own location page, never the brand homepage.
- Add UTM tags to the profile link (`?utm_source=google&utm_medium=organic&utm_campaign=gbp`) so profile visits show up separately in analytics.

## 6. Multi-location brands

- One page per staffed location, each with facts only that branch has: team, hours, parking, directions from the station, services offered there, reviews mentioning it.
- A template is fine for structure. The content inside it must differ. If two branch pages could swap names and nobody would notice, they're not done.
- Area pages around each branch follow the same scoring, run per branch with that branch as the centre.
- Group findings by cause: "14 branches share one generic page" is one fix.
