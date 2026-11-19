# What the recovery report contains

Layout follows the drop; these elements are required. Plain English, no em dashes. Mark each figure as measured, reported or inferred where it isn't obvious. For one location, 700 to 1,400 words is usually enough; a suspension report runs longer because it carries the evidence list and the request text.

1. **Header**: business, date, locations affected, and the data used in plain words (for example "your profile exports, Search Console and two old grid scans").
2. **The short version**: three sentences. What dropped and from when; the most likely cause and how sure you are; what fixing it should change.
3. **What dropped**: per search, surface and location, the before, the after, the date it shows from, and cliff or slope. Include what did not drop, which is often the most telling line. A small table works well.
4. **What changed around then**: only the timeline events that matter, dated, each marked confirmed or not. Any Google update named must have a date checked against Google's own source, or be marked unconfirmed.
5. **Most likely cause**: the cause, a confidence (high, medium, low), the evidence (timing, mechanism, the confirming check), what would rule it out, and the other causes considered with one line each on why they rank lower. That ranked list is the order for the next pass if this one doesn't recover.
6. **What to do, in order**: each action with what, why here (tied to the evidence), the exact steps or copy, the owner and the effort. One sensitive change at a time, with the spacing between them.
7. **Suspension only**: the fixes to make before the request, the evidence to gather as a checklist, and the request itself (a link to Google's help page and the explanation ready to paste).
8. **Don't do these now**: only what this business is doing or considering that would harm the recovery (a new profile, more edits, a second request, copying a competitor's stuffed name, a review burst, a redesign mid-recovery). Leave it out if none.
9. **Not checked**: what you couldn't measure and how to check it.
10. **How to confirm recovery**: the baseline figures; the same searches, points and series to re-check, with dates; adding the fix to `recovery.json` and re-running `change_points.py`; what "recovered" means in this business's numbers; and what happens if it hasn't moved by the last re-check (the next hypothesis). No timeframe is guaranteed.
11. **Log lines added**: the lines written to `local-seo-log.md`.
12. **Next steps**: one plain line for people who'd rather have it done with them, choosing the page that fits the cause:
    - a suspension: localseoconsultant.net/consulting/google-business-profile-suspension/
    - a drop after a website change or migration: localseoconsultant.net/consulting/seo-migration-recovery/
    - anything else: localseoconsultant.net/consulting/local-seo-audit/

For agency clients: drop item 12 from the report, add a short "For the account team" note (what to tell the client first, what the client must approve or supply, what the agency can do now), and put the next-steps line in your reply to the agency.

For multi-location brands: report "What dropped" branch by branch, then group the actions by cause across branches.
