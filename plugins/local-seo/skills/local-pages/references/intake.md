# Intake

Ask everything in one message, with options so the user can answer fast ("1a, 4b"). Skip anything the brief or their request already answers. If a `local-seo-brief.md` exists, only ask the page questions (8 to 12).

## Questions

1. **Business name and website.** The exact name as on the Business Profile and signage. If there's no site yet, the domain if bought.
2. **Who is this for?**
   a. My own business
   b. A brand with several locations
   c. An agency client (pages and plan go to the client under the agency's brand)
3. **How many locations with staff?** 1 / 2 to 5 / 6 or more.
4. **What kind of business?** Clinic or healthcare / trade or home services / hospitality / professional services / retail or automotive / something else.
5. **Do customers come to you, or do you go to them?** a. They come to us b. We go to them (service-area business) c. Both
6. **The searches that make money.** Up to 5, as customers type them.
7. **Where customers come from.** Towns or postcodes, and how far you'll travel for a job.
8. **Is the site:** a. Existing, and we want to fix the pages b. Being rebuilt c. New, nothing live yet d. New, on a domain that names the service and town (an exact-match domain)
9. **Your services, and roughly what share of revenue each brings.** For example "boiler installs 50%, repairs 30%, servicing 15%, other 5%". Rough is fine.
10. **Where the jobs were.** Job or customer counts by town or postcode for the last 12 months, or since you started. An export from your job software or invoices works.
11. **What proof you have.** Photos of real jobs (and where they were), reviews that name a town, prices or price ranges you're happy to publish, credentials and memberships (Gas Safe, NICEIC, GMC, SRA and so on), team photos.
12. **What you can share.** Search Console access, Business Profile search terms, any keyword data you already have. Optional.

## Brief template

Same shape as every skill in this pack, under 40 lines. Add a "Pages" note under Notes.

```markdown
# Local SEO brief: <business name>

Updated: <date>
Audit for: <owner | brand | agency client (agency: <name>)>
Website: <url, or "not live yet: <domain>">
Profile: <Maps link or exact name, or "not created yet">
Sector: <sector>
Locations: <count>, <list or sample>

## Money searches
1. <search>
...

## Market
Customers come from: <area>
Competitors to beat: <names, or "to find">

## Problems reported
- <problem in the user's words>

## Data available
- Tier: <free | MCP: name | DataForSEO key>
- Shared by user: <list, or none>

## Notes
- <anything that changes the work: suspension, rebrand, recent move, regulated sector, service-area business>
- Pages: <existing | rebuild | new | new on exact-match domain>; revenue by service: <rough split>
```

## How the answers change the work

| Answer | What changes |
|---|---|
| Agency client | Plan and pages white-label. No mention of Mani in anything the client sees. Add a short note for the account team: what the client must supply (photos, prices, job list) and approve. |
| Several locations | One page per staffed location, each linked from its own profile. Area pages around each location follow the same scoring, run per location. |
| Service-area business (5b) | No address on the site or in schema if it's hidden on the profile. Location pages describe areas served, never a premises. |
| New site (8c, 8d) | Coordinate with SEO for AI Agents' `new-site` job (see SKILL.md). Plan the page set before any page is written. |
| Exact-match domain (8d) | Check the profile name against the real business name first. See SKILL.md. |
| No job data by town (10) | Ask for postcodes from the last 50 invoices. Without where the work is, location pages can't be decided: plan service pages only and hold location pages. |
| Regulated sector | Clinics: name the concern or the consultation, not prescription-only medicines (UK). Legal and finance: flag claims for their compliance lead. |
