# The six areas

Each check says how to do it on each data tier (see data-sources.md) and what makes it a finding. Thresholds are comparative wherever possible: the business against the 3 competitors actually beating it for its money searches. Find those competitors first (area 1).

## Contents
1. Where you actually rank
2. Business Profile
3. Website
4. Reviews
5. Consistency across the web
6. AI answers

---

## 1. Where you actually rank

Question: where in the area does the business show up, and where does it disappear?

| Check | Free | With a scanning tool | Finding when |
|---|---|---|---|
| Map pack for each money search | Ask the user to search on their phone from 5 points: the business, and roughly 1 mile north, east, south and west (further for a business that travels to customers). Screenshot the map pack. Run grid.py on the results. | Run a grid per money search (SearchOps, other geo-grid MCP, or grid.py with DataForSEO). Size it to how far customers travel. | Not top 3 at the business's own location (eligibility or relevance problem). Top 3 at the door but out of the top 10 within the area customers come from. |
| Maps vs local pack vs AI Mode | Not checkable free. List under "Not checked". | Compare the same search across surfaces where the tool supports it. | Big gaps between surfaces: note which surface the business loses on. |
| Strong radius | From the 5-point check: rough only. | grid.py summary. | Strong radius smaller than the area customers come from. |
| Edge competitors | Note who appears where the business drops out. | From the grid results. | The same 1 to 3 businesses take over. These become the competitors for every comparison below. |
| Branded search | Search the business name. | Same. | Profile doesn't show for its own name, or shows a duplicate. This is an eligibility break. |

---

## 2. Business Profile

Question: is Google sure what the business is?

Get the profile details by fetching the Maps listing if possible, otherwise ask the user to paste: name, primary and secondary categories, services, description, hours, attributes, website link, number of photos. Do the same for the 3 competitors (their categories are visible in Maps; the primary is the one shown under the name).

| Check | Finding when |
|---|---|
| Primary category | Different from what most of the 3 competitors use for the money search, or broader than the service (a general category where the winners use a specific one). High impact, low effort. |
| Secondary categories | Missing categories competitors use that match services the business really offers. |
| Services | Money-search services not listed, or listed with vague names that don't match how people search. |
| Business name | Contains keywords, locations or taglines that aren't on the signage. Suspension risk: fix before anything else. If competitors do it, don't copy; it gets profiles suspended. |
| Address and service area | Address is a virtual office or somewhere the business doesn't operate. Suspension risk. Service area settings don't widen rankings, so don't treat them as a fix. |
| Website link | Points to a page that doesn't match the money searches. One location with one dominant service: link to that service's page. Several money searches: link to the homepage only if it clearly leads with them and links to each service page; otherwise link to the top revenue service. Multi-location: each profile links to its own location page, never the brand homepage. |
| Hours, phone, booking link | Missing, wrong, or a call tracking number not set up as primary with the main number as additional. |
| Photos | Few or only stock images compared with competitors. Impact is on being chosen, not ranking. |
| Duplicates and practitioners | More than one listing at the address for the same business, or practitioner listings splitting reviews. |

---

## 3. Website

Question: does the page the profile links to deserve to rank?

Fetch the site. Check the landing page and each money-search service.

| Check | Finding when |
|---|---|
| One page per core service | A money-search service has no dedicated page, or shares one page with many others. |
| The page says what and where | The page doesn't state the service and the town or area in the title, main heading and opening lines, written for the person searching. |
| Proof on the page | No prices or price guidance, no photos of real work or the team, no reviews, no clear call or book button above the fold on a phone. |
| Location pages | Pages that only swap the town name. Thin pages get filtered and drag the site down. Recommend fewer pages with real local detail: jobs done there, team, directions, local reviews. |
| Internal links | Blog or area pages not linking to the service pages that sell. |
| LocalBusiness schema | Missing, or name, address and phone don't match the profile exactly. |
| Indexing | Key pages blocked by robots or noindex, or not found with a `site:` search. |
| Mobile speed | Slow on mobile (PageSpeed Insights). Only a priority if it's clearly hurting calls or bookings. |

---

## 4. Reviews

Question: do the reviews help the business rank and get chosen?

Get review count, rating and the dates of the most recent 20 to 30 reviews for the business and the 3 competitors (2 if that's all the user can get; say so). Free: ask the user, or read from Maps if fetchable. Then run:

```bash
python scripts/review_velocity.py reviews.json
```

| Check | Finding when |
|---|---|
| Velocity | Fewer new reviews in the last 90 days than the competitor median. |
| Recency | Newest review older than the competitors' typical gap between reviews. |
| Bursts | Most reviews arrived in one short burst, then stopped. |
| Review text | Reviews rarely mention the service or the place. Fix: ask customers to say what was done and where, without scripting their words. |
| Replies | Under most reviews have replies, or replies are generic. Where the business has rules on what it can say, replies break them (for example confirming someone was a client when that's confidential). |
| Request process | No routine. Recommend: SMS with a one-tap review link within the hour the job ends, one email follow-up two or three days later, QR code at the counter or on the invoice, and staff who know when to mention it. |
| Fake or competitor reviews | Clear spam reviews present. Report them through the profile and keep the evidence. |

---

## 5. Consistency across the web

Question: does the rest of the internet describe the same business?

Search the business name plus phone number, the old address if any, and the main directories for the country and sector. Collect name, address and phone from each, then run:

```bash
python scripts/nap_check.py listings.json
```

| Check | Finding when |
|---|---|
| NAP matches | Any listing differs from the profile in name, address or phone. Rate it: wrong details on the website or a duplicate profile is eligible, impact 3. Wrong details on a main directory or data aggregator is eligible, impact 2. One minor directory, or a small wording difference, is impact 1 (polish). |
| Old details | Old addresses or numbers still live. |
| Duplicates | Duplicate or merged listings on the main directories. |
| Local mentions and links | Competitors have local press, associations, suppliers or sponsorship links and the business has none. Suggest the 3 most realistic local sources. |

---

## 6. AI answers

Question: when someone asks an assistant for a business like this, is it named?

Free: use web search to see which businesses and sources come up for the money searches with "best" or "recommended" plus the area. Ask the user to put the same question to ChatGPT and Gemini three times each and paste the answers. With a tool: use its AI visibility data.

| Check | Finding when |
|---|---|
| Named or not | Business named in fewer than half the runs, while a competitor is named in most. |
| Who is named and why | List the sources the answers cite or lean on: directories, comparison articles, press, review sites. Gaps where competitors appear and the business doesn't are findings. |
| How it is described | Sources describe the business differently (old name, different services). |
| Quotable site content | The site has no plain statements an assistant could quote: what it does, where, for whom, prices, credentials. |

Treat AI results as a pattern across runs, never a single answer.
