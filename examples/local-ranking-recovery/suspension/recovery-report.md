# Local ranking recovery: Larchmont Dental Studio (fictional)

19 November 2026 · 1 location · Data: SearchOps grid scans and Search Console (measured), Business Profile performance up to the suspension (measured), your call tracking report, the suspension email and the profile's edit history (reported)

## The short version
Your profile was suspended on 10 September and has been off Google Maps since: calls to the profile's tracking number fell from about 40 a week to 3, and you went from the top 3 at 68% of points for "emergency dentist" to none. The most likely cause (high confidence) is the business name: since March the profile has read "Larchmont Dental Studio - Emergency Dentist Croydon, Invisalign & Implants", which isn't the name on your sign, and the Saturday hours edit on 8 September probably prompted the review that found it. Fix the name, remove the second profile made on 12 September, gather the evidence below, and then file one well-evidenced reinstatement request.

## What dropped

| Series | Before | After | From | Shape |
|---|---|---|---|---|
| Calls to the profile's tracking number, per week | 40 | 3 (-93%) | week of 14 Sep | cliff |
| Maps top-3 coverage, "emergency dentist" | 68% of points | 0% | scan of 21 Sep | cliff |
| Profile calls reported by Google | 46 a week | no data | after 7 Sep | stops reporting |

Measured (SearchOps and your call tracking, reported), run through `change_points.py`. Google stopped reporting profile data after the suspension; those weeks are gaps, not zeros.

What didn't drop: Search Console non-branded clicks held (+1%), and branded clicks rose 13%. People who know your name are searching for you and finding the website instead of the profile. The website is not the problem.

## What changed around then

- **10 March**, confirmed (edit history): the previous agency changed the profile name to "Larchmont Dental Studio - Emergency Dentist Croydon, Invisalign & Implants".
- **8 September**, confirmed: Saturday hours changed.
- **10 September**, confirmed: suspension email; the listing disappeared from Maps and from searches for your name.
- **12 September**, reported: a second profile, "Larchmont Dental", created to get back on Maps.

## Most likely cause
**Keywords added to the business name.** Confidence: high.
- Evidence: the name on the profile isn't the name on your signage, website or registration. Keyword-stuffed names are one of the most common reasons profiles get suspended. The hours edit two days before is the kind of change that prompts Google to look at a profile again; it isn't a problem itself. Nothing else on the profile breaks the rules: the address is your surgery, staffed in the hours shown, and the category is "Dentist".
- What would rule it out: a rejected request after the name and duplicate are fixed and the evidence is clean. Then look at ownership (the agency's account may still have access) next.
- Other causes considered: the address (a real surgery with signage, so unlikely); a duplicate (the second profile came after the suspension, but it will count against the request if it stays); the agency's account (it still has manager access; if it manages other suspended profiles, that can count against you).

## What to do, in order

### Before the reinstatement request
1. **Remove the second profile, "Larchmont Dental".** Two profiles for one practice makes reinstatement harder and can affect both. Steps: in your Business Profile account, open "Larchmont Dental" and remove it. Don't create any other. Owner: practice manager. Effort: low.
2. **Change the name on the suspended profile to "Larchmont Dental Studio".** Exactly as on the sign and your registration, nothing added. If the profile won't accept the edit while suspended, note that in the request. Owner: practice manager. Effort: low.
3. **Remove the old agency's access.** Check the profile's managers; remove anyone who shouldn't be there. Owner: practice owner. Effort: low.
4. **Make the name match everywhere.** Website title, footer and contact page; NHS website listing, Yell and any dental directories. Search for "Emergency Dentist Croydon" with your phone number to find copies of the stuffed name. Owner: your web person and practice manager. Effort: medium.

### Evidence to gather
- Companies House record (or CQC registration) in the name "Larchmont Dental Studio".
- A utility bill or lease for the surgery address in the practice's name.
- Photos: the sign over the door, the entrance with the street number, reception, a treatment room.
- Your website showing the same name, address and phone.
- Your GDC registration details for the principal dentist.
- Someone ready to do a video if Google asks: from the street, past the sign, through the door, into a surgery, in one take.

Get everything together before you start. Reports say the upload step can be time-limited.

### The request
Follow the steps on Google's help page, [Fix suspended or disabled profiles](https://support.google.com/business/answer/4569145). Use this explanation, edited if anything differs:

> We are Larchmont Dental Studio, a dental practice at our surgery in Croydon, trading under this name since 2014. In March 2026 a previous agency changed our profile name to include extra keywords. We have corrected it to our registered and signed name, removed a duplicate profile created in error after the suspension, and removed the agency's access. Attached are our Companies House record, a utility bill for the surgery, and photos of our signage, entrance and premises.

Owner: practice owner. Effort: medium.

## Don't do these now
- **Don't create another profile**, and don't file a second request while the first is open.
- **Don't edit anything else on the profile** until there's a decision.
- **Don't copy competitors who use keywords in their names.** It's what got you here.

## Not checked
- Whether the old agency's account manages other suspended profiles. Ask them, or check the account's profile list if you can see it.
- Your rankings for "dentist croydon" and "invisalign croydon": not scanned before the suspension, so there's no baseline. Scan them as soon as you're back.

## How to confirm recovery
- First sign: search "Larchmont Dental Studio" on Google Maps. The profile shows again with its reviews.
- Baseline: about 40 calls a week to the tracking number; "emergency dentist" top 3 at 68% of points.
- Re-run the same "emergency dentist" grid at the first scan after reinstatement, then fortnightly for 8 weeks. Track tracking-number calls weekly.
- Add the reinstatement date to `recovery.json` as an event and re-run `change_points.py`: the recovery shows as a rise starting after that date.
- Recovered means: calls back near 40 a week and "emergency dentist" coverage back above 60%. Google's decision time varies from days to weeks, and rankings can take a little longer to settle after that. No timeframe is guaranteed.
- To stop it happening again: one owner for the profile, a change log, and no edits to name, address or category without a reason.

- If the request is rejected: the next hypothesis is ownership. Check whether the old agency's account manages other suspended profiles before anything else is filed.

## Log lines added
```
2026-11-19 | Suspended 10 Sep; tracking calls 40/week to 3, "emergency dentist" top 3 68% to 0% | Cause: keyword-stuffed name added 10 Mar by previous agency (high); hours edit 8 Sep likely prompted the review | Re-check: n/a
2026-11-19 | Planned in order: remove duplicate "Larchmont Dental", restore name to "Larchmont Dental Studio", remove old agency access, fix name on site and directories, then one reinstatement request | Re-check: profile visible for name search weekly after request
```

## Next steps
If you'd rather have it done with you: localseoconsultant.net/consulting/google-business-profile-suspension/
