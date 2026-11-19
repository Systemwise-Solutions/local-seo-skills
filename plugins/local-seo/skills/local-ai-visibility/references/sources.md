# Sources, consistency and quotable facts

## Contents
1. The source map
2. Consistency
3. Why the winner wins
4. Quotable facts on the site
5. Turning gaps into actions

---

## 1. The source map

Start from two lists: the domains the script counted from the answers, and the sites your own web search found for the prompts. Group them:

| Type | Examples to look for | Check |
|---|---|---|
| The business's own site | Home, service pages, about, prices | Does it state the facts in section 4? Is the page the answers would need indexed? |
| Directories | Yell, Thomson Local, sector directories (Doctify and Top Doctors for health, Checkatrade and TrustATrader for trades, the Law Society for solicitors), Apple Maps, Bing Places | Listed? Same name, address, phone? Services and description current? |
| Review sites | Google, Trustpilot, sector review sites | Present? Review count and recency against the competitor named most. Does review text name the service and the place? |
| Comparison articles | "Best <service> in <area>" lists on local blogs, guides and magazines | Listed? If not, who wrote it, when, and is it updated? |
| Local press and community | Local news sites, council and community pages, sponsors, associations | Any mention at all? |
| Forums and video | Reddit threads for the city, local Facebook groups, YouTube | Who do people recommend, in their own words? |
| Competitors' sites | | What they say that the business doesn't. |

For each source record: listed (yes / no / unknown), how it describes the business, and which competitors it lists. "Unknown" means you couldn't load it; ask the user to check, don't guess.

A source cited in several runs that doesn't list the business is a gap. A source that lists it but ranks it below the competitors, or describes it vaguely, is a weaker gap.

## 2. Consistency

Assistants seem to name businesses that several sources describe the same way. Check across the profile, site and the top sources:

- **Name**: the same everywhere, matching the signage. No keyword versions.
- **Address and area**: current address everywhere; old addresses after a move are the most common fault.
- **Phone**: one main number.
- **What it does**: the same core services and specialisms. A site saying "sports injury specialists" while every directory says "general physiotherapy" splits the picture.
- **Who it's for**: the same audience.
- **Credentials and facts**: the same years trading, qualifications, memberships, team size.

If `local-seo-audit`'s `nap_check.py` is available in this environment, use it for name, address and phone. This skill doesn't ship it; do it by hand otherwise.

## 3. Why the winner wins

For the competitor named in most runs, put the two side by side:
- Which cited sources list them and not this business.
- What the sources say about them: specialism, awards, years, review themes.
- What their site states plainly that this business's site doesn't.
- Their review count and recency (reported or read from Maps).

The gaps become actions. Don't copy their claims; find the true equivalent for this business.

## 4. Quotable facts on the site

An assistant can only repeat what it can find stated clearly. Check the homepage and each money-search service page for plain sentences covering:

- **What**: the service, in the words customers use.
- **Where**: the town, neighbourhoods, and where they travel to (service-area businesses).
- **For whom**: the people it suits ("runners and people with desk-job back pain").
- **Prices**: a price or a "from" price, and what's included.
- **Credentials**: qualifications, registrations and memberships that can be checked (for example HCPC registration for physios), years trading, team.
- **Proof**: a number of reviews and rating, named awards, the kind of jobs done there.
- **How to book**: hours, booking link, phone.

Write the missing copy, ready to paste: short factual sentences near the top of the page, not buried in a long story. One fact per sentence. Use the same wording the profile and directories should use.

Rules:
- Only facts the user confirms. Never invent prices, credentials, years or awards; leave a marked gap for them to fill.
- Regulated sectors: no prescription-only medicines advertised to the public in the UK, no claims of outcomes. Flag wording for their compliance lead.
- A short facts block ("At a glance") is fine. A page written only for assistants isn't.
- Add or correct LocalBusiness schema so it matches the copy, if it's missing or wrong.

## 5. Turning gaps into actions

| Gap | Action | Owner | Effort |
|---|---|---|---|
| A cited directory doesn't list the business | Create or claim the listing with the same name, address, phone, services and description. | you | low |
| A cited directory has old details | Correct it; ask for duplicates to be merged. | you | low |
| A comparison article lists competitors, not the business | Email the author with a short, factual case and one thing their readers would care about. Accept no. Never pay for an editorial-looking placement without it being labelled. | you | medium |
| No local press or community mentions | One realistic local story (a sponsorship, a community project, expert comment on something local). | you | medium |
| Reviews don't mention the service or place | Ask customers to say what was done and where, without scripting their words. SMS with a one-tap link within the hour, one follow-up. | you | low, routine |
| Site doesn't state the facts | Paste the copy from section 4 onto the homepage and service pages. | web person | low |
| Forum threads recommend competitors | Nothing planted. If the business has a genuine account and can answer a question helpfully and openly, fine. Mostly, this follows from reviews and reputation. | you | low |
| Described wrongly by an assistant | Fix the sources it leans on. Most assistants also have a feedback button on answers; worth using, but don't rely on it. | you | low |
