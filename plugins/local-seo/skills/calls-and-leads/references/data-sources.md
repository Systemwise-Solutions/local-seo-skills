# Data sources

The diagnosis works with no paid tools: the Business Profile dashboard, the phone system and the booking diary hold most of what's needed. Tools make it faster and give longer history. Say at the start which tier you're on.

## Free

- **Business Profile performance** (in the profile, Performance): views split by Search and Maps, calls, website clicks, direction requests, and bookings where a booking partner is connected. Ask for the same months in two periods. The data runs a few days behind. Business Profile chat ended in 2024, so there are no message counts.
- **Phone system or call tracking log**: calls answered and missed, by hour and day if possible. Most VoIP systems and mobile networks can export this. Ask for counts, not recordings.
- **Form inbox and booking system**: enquiries received and bookings made, by week.
- **Job diary or CRM**: booked jobs, and where possible the source each customer gave.
- **Phone tests the user can do**: ring the number on the profile at 8am, lunchtime and 5.30pm on a weekday and once on Saturday; tap the call button on the profile and the website from a mobile; submit the website form with "TEST" in the name and time how long until it arrives.
- **What you can check yourself**: fetch the landing page; check the call link is a `tel:` link and the number matches; look at the profile's hours, phone, booking link, photos, reviews and services against the 3 businesses beside it.

## SearchOps (if connected)

Tool names may carry a server prefix. Start with `list_locations` to find the location.
- `get_location_profile_performance`: calls, website clicks, direction requests, bookings and views by month, week or day (day only up to 3 months), for 1 to 18 months, against the same period before. It ends at the last day Google reported. When it says a comparison isn't comparable, don't quote the change. Days Google never reported are null, not zero.
- `get_location_profile_roi`: action rate (actions divided by views) now against a baseline before SearchOps was connected. Action rate is the best single number for "is the profile converting", because it doesn't rise just because more people searched. Under 60 days of data the percentages are suppressed: report counts only.
- `get_location_week`: the last 7 reported days against the 7 before, beside the tasks done that week. Use it for the weekly check during the 30-day plan. It shows the two side by side; never claim the work caused the change.
- `query_google_analytics` (after `list_analytics_properties`): sessions and key events grouped by `landingPage`, `sessionSourceMedium` or `sessionCampaignName`, filtered by `deviceCategory` or `sourceContains`. For profile traffic, group by `sessionCampaignName` and look for the UTM campaign (for example `gbp`). Key events by landing page show which page converts.
- `get_location_profile_search_terms`: what people searched when the profile showed. Useful when views are steady but actions fell: the profile may be showing for searches that don't fit the business.
- `query_search_console`: impressions and clicks by page and query, for the Seen stage.
- `create_task`: add each fix as a task if the user wants it tracked.

## Other tools

Call tracking platforms (CallRail, Mediahawk and others) export calls by source, answered and missed, and many push call events into GA4. Booking platforms often have a GA4 integration. Use what the business already has; don't push the user to buy anything mid-task. Setup steps change: link the vendor's own docs.

## Rules

- Label every figure: measured (by you or a tool), reported (by the user), inferred.
- If a tool says the profile isn't connected or has no data, say so. Never report it as zero.
- Ask for counts, not personal data. No call recordings, names or phone numbers of customers in chat.
- If a tool call fails, say so and fall back to the free method.
