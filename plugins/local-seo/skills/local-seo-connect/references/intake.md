# Intake for connecting data

This skill needs less than the audit. Ask only what's missing, in one message, with options. If the user has already answered in their request, don't ask again.

## Questions (only if there is no brief)

1. **Business name and website.** Plus the Google Business Profile name as it shows on Maps.
2. **Who is this for?** a. My own business / b. A brand with several locations / c. An agency, for clients
3. **How many locations?** 1 / 2 to 5 / 6 to 20 / 21 or more
4. **What do you want the data for?** a. Rank higher in Google Maps / b. More calls and bookings / c. Recover rankings that dropped / d. Get named by AI assistants / e. New website launching / f. Reviews / g. Just see where I stand
5. **The searches that make money.** Up to 5, as customers type them. Optional here; the audit will ask.

Then the environment questions from step 3 of SKILL.md.

## Brief template

Write the brief in this exact shape (shared by every skill in the pack) and keep it under 40 lines. Leave fields this skill didn't ask about as "to confirm" so the next skill fills them.

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

This skill expands **Data available** into the fuller shape in verify.md. Other skills read the first line ("Tier") and the connection list, so keep both.
