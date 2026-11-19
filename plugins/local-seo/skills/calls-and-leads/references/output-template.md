# Output template

Use these headings in this order. Plain English. No em dashes. Every finding has evidence and an exact action. Mark each figure as measured, reported or inferred where it isn't obvious.

```markdown
# Calls and leads: <business name>

<Date> · <locations> · Data: <tier in plain words, e.g. "your profile screenshots, phone log and diary">

## Where the leak is
<Two or three sentences. The stage losing the most enquiries, the evidence, and roughly how many enquiries a month it costs (inferred, from funnel.py). Name any secondary leak.>

## Do these three first
1. **<Action>.** <Why, tied to the evidence.> Owner: <who>. Effort: <low/medium/high>.
2. ...
3. ...

## The funnel
<funnel.py tables: monthly counts and rates for both periods. One line under them on what changed and what didn't.>

## Findings by stage
<Only stages with findings, in path order. Each: title, evidence, fix (exact steps or copy), owner, effort.>

## Fixes in order
<Numbered. Leaks nearest the money first, then conversion, then visibility. Tracking alongside from day one.>

## 30-day measurement plan
<See below.>

## Hand-offs
<Only if needed: rankings to local-seo-audit or local-ranking-recovery; profile copy to gbp-optimisation; reviews to review-engine; pages to local-pages; GA4 and Search Console setup to seo-operations-measurement.>

## Not checked
<What you couldn't measure and how to check it.>

If you'd rather have it done with you: localseoconsultant.net/consulting/local-seo-audit/
```

For agency clients, drop the last line from the client document and add "For the account team": what the client must change themselves, and what the agency can do without them.

## The 30-day measurement plan

```markdown
### Baseline (before any change)
| Measure | Baseline | Source |
|---|---|---|
| Profile views a month | | Profile performance |
| Profile action rate | | Profile performance |
| Calls answered / missed a month | | Phone log |
| Form enquiries a month | | Form inbox / GA4 |
| Bookings a month | | Diary |

### Days 1 to 7: fixes
- Day 1: <fix>, <owner>
- Day 1: tracking (call tracking number, UTM, GA4 key events), tested
- ...

### Every day
- Missed calls, and whether each was called back the same day.

### Every week
- Profile calls, website clicks, directions and views for the last 7 days (SearchOps: get_location_week).
- Form enquiries and bookings.
- Anything else that changed: prices, ads, staff, weather, holidays.

### Day 30: compare
- Same counts for days 1 to 30, into funnel.json as the second period, run funnel.py.
- If the business is seasonal, also compare with the same 30 days last year.
- Judge on rates at the stage you fixed, not on total calls. Total calls can fall in a quiet month while the leak is fixed.
```

Profile data runs a few days behind, so read day 30 on day 34 or later.
