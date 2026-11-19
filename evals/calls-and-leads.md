# Evals: calls-and-leads

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline.

## Should trigger

1. "We're not getting calls any more. We still rank on Google. What's going on?"
2. "Our profile gets 4,000 views a month but hardly anyone rings."
3. "Bookings at the clinic are down 30% since we changed our website in March."
4. "How do I track calls from our Google Business Profile without messing up our listings?"
5. "Here are our profile stats for this October and last October. Where are we losing enquiries?"
6. "Is our local SEO actually bringing in customers? I can't tell."

## Should not trigger

1. "Set up Google Ads conversion tracking for our shop." (paid search)
2. "Why don't we show in Google Maps in the next town?" (local-seo-audit)
3. "Install GA4 on our new Next.js site." (SEO for AI Agents: `seo-operations-measurement`)
4. "Write a reply to this one-star review."

## Borderline (trigger is acceptable, should stay focused)

1. "Our rankings dropped and the phone's gone quiet." Should check views first, hand rankings to `local-seo-audit`, and still check the stages below.
2. "Should we use a call tracking number on Google?" Answer directly (tracking number as primary, main number as additional, main number everywhere else) and may offer the full diagnosis.
3. "Our receptionist misses calls at lunch, what should we do?" Answer the Reached stage directly; doesn't need a full intake.

## What good output looks like

- Reads or writes the shared brief; asks when the drop started, what changed, how calls are answered and what counts as a booking.
- States the data tier. Never treats missing data as zero. Labels figures measured, reported or inferred.
- Gets two comparable periods (same months last year for seasonal businesses) and runs `funnel.py`.
- Tests the path where it can: profile on a phone, `tel:` link, a marked test form submission, the user ringing their own number at set times.
- Names one primary leak with evidence and an inferred count of enquiries lost, and orders fixes nearest the money first, with tracking from day one.
- Writes the copy it recommends: voicemail, missed-call text, above-the-fold block, follow-up text.
- Tracking advice is right: tracking number primary, main number additional; main number kept in schema and directories; UTM on the profile link; GA4 key events on successful form submission, not button click.
- 30-day plan with a baseline table, daily and weekly checks, and a day-30 comparison with `funnel.py`, judged on rates.
- Hands rankings to `local-seo-audit` and GA4 setup to `seo-operations-measurement` rather than doing them.
- Never suggests review gating, fake reviews or keyword-stuffed names. No promised call volumes.
- No em dashes; one plain next-steps line at the end (not in agency client output).
