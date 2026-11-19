# Intake

The intake makes the audit about this business. Ask everything in one message. Show options so the user can answer fast ("1b, 3a and 3c"). If they have already given an answer in their request, don't ask it again.

## Questions

1. **Business name and website.** Plus the Google Business Profile link or the exact name as it shows on Google Maps.
2. **Who is the audit for?**
   a. My own business (one location)
   b. A brand with several locations
   c. An agency client (the report goes to the client under the agency's brand)
3. **How many locations?** 1 / 2 to 5 / 6 to 20 / 21 or more. For more than one, ask for the list or a sample of 3: the strongest, the weakest, and a typical one.
4. **What kind of business?** Clinic or healthcare / trade or home services / hospitality or leisure / professional services / retail or automotive / something else (say what).
5. **What's going wrong?** Pick all that apply:
   a. We rank near the door, then vanish
   b. We rank for our name, not our services
   c. AI assistants name competitors, not us
   d. Competitors have more recent reviews
   e. Some branches rank, others don't
   f. We pay for SEO and can't see what changed
   g. Our profile is suspended
   h. New business or new location, starting from nothing
6. **The searches that make money.** Up to 5, as customers type them (for example "emergency plumber", "lip filler", "family solicitor"). Not the business name.
7. **Where customers come from.** A town, postcodes, or "about X miles from us". For service-area businesses, where the jobs actually are.
8. **Who you lose to.** 1 to 3 competitors, if known. If not, you'll find them.
9. **What you can share.** Any of: Google Business Profile performance screenshots, Search Console access or exports, review counts, call tracking. Optional.

If the profile is suspended (5g), the audit still runs, but the first section of the report is reinstatement, and every other fix waits until the profile is live.

If they have 21 or more locations, audit a sample of 3 locations in full, then group the rest by likely cause. Say that a full estate audit needs a scanning tool.

## Brief template

Write the brief in this exact shape and keep it under 40 lines.

```markdown
# Local SEO brief: <business name>

Updated: <date>
Audit for: <owner | brand | agency client (agency: <name>)>
Website: <url>
Profile: <Maps link or exact name>
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
- <anything that changes the audit: suspension, rebrand, recent move, regulated sector>
```

## How the brief changes the audit

| Answer | What changes |
|---|---|
| Agency client | Report written for the end client, white-label, no mention of Mani in the body. Effort owners named as "your team" and "client". |
| Several locations | Check the sample in depth, then look for the same fault across the rest: same category, same landing page pattern, same review gap. Group fixes by cause, not by branch. |
| Rank near door, then vanish (a) | Grid and radius first. Most often a proof problem (category, services, page) rather than a distance one. |
| Name, not services (b) | Category, services list and landing page first. |
| AI names competitors (c) | AI answers area first, then consistency across the web. |
| Reviews behind (d) | Run review_velocity.py against the named competitors. |
| Can't see what changed (f) | Set up measurement in the plan: the baseline grid, calls and bookings by source. |
| Suspended (g) | Reinstatement section first. Check name, address and category against what is on the signage. |
| New (h) | Eligibility rung first: verification, NAP, the first page per service, first 10 reviews. |
