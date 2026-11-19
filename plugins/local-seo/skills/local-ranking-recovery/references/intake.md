# Intake

Ask everything in one message, in plain language, with options so the user can answer fast ("2a, 4b"). Skip anything they've already told you. If a `local-seo-brief.md` exists, only ask questions 4 to 8.

## Questions

1. **Business name, website, and the Google Business Profile link** (or the exact name as it shows on Google Maps).
2. **Who is this for?**
   a. My own business
   b. A brand with several locations
   c. An agency client (output goes to the client under the agency's brand)
3. **Which locations are affected?** One / some (which) / all of them.
4. **What dropped?** Pick all that apply:
   a. We're gone from the map pack or Google Maps for our main searches
   b. We don't show up even when people search our name
   c. Calls or bookings from Google fell
   d. Website traffic from Google fell
   e. Google says the profile is suspended, or we can't manage it any more
   f. AI answers stopped mentioning us
5. **When did you notice, and is it sudden or gradual?** A date or a week if you can. "Overnight" and "over a couple of months" point to different causes.
6. **What changed in the three months before?** Pick any, with dates if you have them:
   a. Business Profile edits: name, category, address, hours, phone, website link
   b. Google asked us to verify again, or sent us an email about the profile
   c. A new website, redesign, new platform, or pages removed or renamed
   d. Moved premises, rebranded, merged, or opened another branch
   e. New agency, new staff with profile access, or a change of owner
   f. Reviews disappeared, or a run of bad reviews
   g. A new competitor nearby, or a competitor changed their name
   h. Nothing we know of
7. **The searches that matter.** Up to 5, as customers type them. Not the business name.
8. **What you can share.** Any of: Business Profile performance (calls, clicks, directions) from before and after, Search Console access or exports, call tracking reports, old grid scans, the suspension email, screenshots of the profile.

If 4e: also ask for the exact wording of Google's email or notice, and whether anyone has already appealed.

## Brief template

The same brief all skills in this pack read and write. Keep it under 40 lines. Put the drop under "Problems reported" and anything that changes the diagnosis under "Notes".

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

## The working file

Alongside the brief, keep the timeline and series as `recovery.json`, the input to `scripts/change_points.py`. It is the record of what was found and when, and the baseline for checking recovery later. In Claude Code save it to the working folder; in the Claude app show it and offer it as a file.
