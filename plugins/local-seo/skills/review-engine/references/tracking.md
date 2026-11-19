# Monthly tracking

30 minutes, the first week of each month. One person owns it.

## The routine

1. **Export or copy the month's reviews** into `reviews-log.json`: date, rating, text, reply date, reply text. Add the number of requests sent that month from the sending system.
2. **Run the tracker:**
   ```bash
   python scripts/review_tracker.py reviews-log.json --months 6
   ```
   Add `--confidential` and the business's `avoid_in_replies` phrases if there are rules on what replies may say.
3. **Check against the target** from review_velocity.py (the monthly number to match the competitor median).
4. **Find the step that slipped**, using the table in request-flow.md:
   - Requests sent fell: the trigger or the habit broke. Check the automation is on and staff are using the template.
   - Requests held, reviews per 100 requests fell: timing or the link. Check the send delay and tap the link on a phone.
   - Reviews arriving but short: add or restore the "what and where" line.
   - Reply rate or speed slipped: name who replies and when (for example "office manager, Tuesday and Friday mornings").
5. **Answer everything unanswered**, lowest rating first.
6. **Check removals**: status of anything reported, appeal if rejected and the evidence is strong.
7. **Every quarter**, re-run review_velocity.py with fresh competitor dates. Competitors' pace changes; so does the target.

## What to record each month

| Month | Requests sent | New reviews | Reviews per 100 requests | Avg rating | Replied | Median days to reply | Mention a service | Mention a place | Changes made |
|---|---|---|---|---|---|---|---|---|---|

The tracker prints every column except "Changes made". Write one line there, and the same line in `local-seo-log.md`: what you changed and why. It's how you'll know what worked.

## What good looks like

Mani's working rules of thumb, not platform rules:

- New reviews every month, close to the target, without bursts.
- Every review replied to, most within 2 working days.
- A growing share of reviews that mention the service and the area.
- Fewer than one month in six with nothing new.

Don't promise a number of reviews or a ranking change. The routine is in the business's control; the customers' choices and Google's filters aren't.

## With SearchOps

Pull reviews with `get_location_reviews` instead of copying. With a yes, add a monthly task with `create_task` ("Review check: run tracker, reply to all, fix the slipped step"), after checking `list_tasks` so it isn't added twice.
