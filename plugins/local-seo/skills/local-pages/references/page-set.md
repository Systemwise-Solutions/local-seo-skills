# Deciding the page set

## Contents
1. The principle
2. Service pages
3. Location pages
4. Keep, create, merge, remove, hold
5. Which page the profile links to
6. Several locations

---

## 1. The principle

A page earns its place with three things: a search people make, money behind it, and something to say that a competitor couldn't copy. loop.md explains why near-identical pages fail. The practical result is usually fewer pages than the owner expects, each one deeper.

## 2. Service pages

A service, product line or treatment gets its own page when all three are true:

| Test | How to check | Why |
|---|---|---|
| People search for it by name | Profile search terms, Search Console, a keyword tool, or competitors ranking pages for it | A page for a search nobody makes has nothing to win. |
| It brings revenue the business wants | The owner's rough revenue split, and what they want more of | Demand for work they'd rather not do is a cost, not an opportunity. |
| There is enough to say | What it involves, who does it, how long it takes, price guidance, examples, questions customers ask | If it's two sentences, it is a section on another page, and a stronger page for it. |

Principles:
- **Split by intent, not by synonym.** Two searches that describe different customers with different needs get different pages; two wordings of the same need share one page, because separate pages would compete with each other.
- **Urgent or out-of-hours pages only if the service is real.** If the business genuinely serves people at those times, a page with the actual hours and price can work. If not, don't create it and don't claim it anywhere, because a promise the phone can't keep loses the customer and the review.
- **Name services within the rules.** Where a regulator or platform limits what can be named or claimed, name what the customer is looking for in permitted terms. Find the rule first.
- **Merge thin services** into the closest page as sections with a jump link, so the main page gets stronger.
- **Brand or product names** only get pages if people search for them with intent to buy locally and the business genuinely supplies or is approved for them.

## 3. Location pages

A location page is for a place where the business can compete and has something specific to say. Run `scripts/town_score.py` on the candidate list. Whether the page can exist at all depends on the lens:

- **Customers come to the business.** Rankings are anchored to the address, and a page for a town 20 minutes away won't move the map pack there. An area page earns a place only where people from that area genuinely make the trip and the page helps them do it: travel and parking from there, why it's worth coming, what people from there typically come for, reviews from people who made the trip. Often the honest answer is no area pages, and stronger service pages instead.
- **The business goes to customers.** Area pages can earn a place where the work is. They describe the area served and the work done there, never a premises.
- **Both.** Treat the premises' own town as the base, and apply the service-area test to the rest.

**Can compete** (the script scores these)
- Within the distance customers or the business actually travel, and ideally inside or near the strong radius from a grid. Far beyond it, the page has to win in organic results; the map pack is unlikely.
- Real work or customers there recently.
- Competition known where possible: who ranks for the service plus the place.

**Something specific to say** (the script counts these as local proof)
- Several real examples there: what was done or bought, roughly where, the result, with photos where the work is visible.
- Reviews that name the place.
- Facts specific to the place that change what the customer needs or how they're served: travel time, access and parking, local rules, the kind of buildings or customers there, landmarks for directions.
- Staff or a premises there (a bonus, not required).

The script's thresholds (3 examples, 2 reviews, 2 facts, score 60) are Mani's working rule of thumb for when a page has enough to stand on. Adjust for the business: a place with fewer but richer examples can pass; one with many examples that all say the same thing may not.

**Never**
- A page per place on a list with the name swapped in. It gets filtered, dilutes the pages that sell, gives AI assistants nothing to quote, and at scale can pull the whole site down.
- A page that implies a premises where there isn't one.
- A page for the base town. The homepage and service pages already target it.

**Big city, one domain.** A city name in the search is usually best served by the homepage or the main service page, not a separate city page competing with them. Location pages are for neighbourhoods and towns where the work is.

**Service and place combined** only for the top service in a strong location with enough examples of that service there to show. Otherwise one location page covering the services done there, linking to each service page.

## 4. Keep, create, merge, remove, hold

| Action | When |
|---|---|
| **Keep** | The page targets a real search, says what and where, and has proof. Note improvements. |
| **Create** | A service or location passes the tests above and has no page. |
| **Merge** | Two pages target the same search, or a thin page has a natural home. Move anything useful into the stronger page, 301 the old URL. |
| **Remove** | Town-swap pages and pages for places the business doesn't serve, with no enquiries and nothing worth moving. 301 to the closest relevant page (or 410 if nothing is relevant and it has no links). |
| **Hold** | Worth a page once proof exists. Name exactly what to collect, and when to revisit (after a few more examples there, or at the next quarterly review). |

Before removing a page, check it hasn't been bringing enquiries (Search Console clicks, analytics key events by landing page, or the owner's own records). A weak page that brings work gets rebuilt with real detail.

Removing many thin pages at once is normal and usually good for the pages that stay. Say so, so the owner isn't alarmed by the page count dropping.

## 5. Which page the profile links to

The profile link should land people on the page that matches the profile's main money search, because that is what they just searched for.

- One location, one dominant service: that service's page, or the homepage if the homepage leads with it.
- One location, several money searches: the homepage, but only if it clearly says what and where and links prominently to each service page. Otherwise the top revenue service.
- Exact-match domain: usually the homepage, which targets the main service in the city.
- Several locations: each profile links to its own location page, never the brand homepage, because the visitor wants that branch's hours, address and team.
- Add UTM tags to the profile link (`?utm_source=google&utm_medium=organic&utm_campaign=gbp`) so profile visits show up separately in analytics.

## 6. Several locations

- One page per staffed location, each with facts only that location has: team, hours, parking, directions, services offered there, reviews mentioning it.
- A template is fine for structure. The content inside it must differ. If two branch pages could swap names and nobody would notice, they're not done.
- Area pages around each location, if any, follow the same scoring with that location as the centre.
- Group findings by cause: "14 branches share one generic page" is one fix.
