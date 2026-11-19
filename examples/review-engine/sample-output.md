# Review engine: Example Physiotherapy

19 November 2026 · 1 location · Data: free checks, your reviews tab screenshots and competitor review dates from Maps · Compared with: Didsbury Physio Studio, Withington Sports Injury Clinic, Chorlton Physio & Pilates

*Example Physiotherapy, its competitors and every reviewer here are fictional.*

## The short version
You've had 5 reviews in the last 90 days against a competitor median of 8, and Didsbury Physio Studio gets one about every week; 8 of your last 16 arrived in one week of June after a team meeting, then the flow stopped. The failing step is simple: nobody asks unless they remember, so the fix is an automatic text from your booking software as patients leave, one email, and a QR code at reception. Separately, four of your replies confirm the reviewer was a patient, and the two lowest reviews have no reply at all, so those get fixed this week.

## Start these three this week
1. **Turn on an automatic review text from your booking software.** It already sends appointment reminders, so it can send a text within the hour after a patient's second appointment of a course, once per patient every 6 months. This replaces "reception asks sometimes", which produced the June burst and little since. Owner: practice manager. Effort: low.
2. **Rewrite the four replies that confirm a patient, and answer the three open reviews.** The replies of 28 September, 15 August, 19 July and 25 June mention sessions, a named physio, a knee and a neck. Confirming someone was a patient can breach confidentiality; the safe rewrites are below. Owner: practice manager. Effort: low.
3. **Report the one-star of 9 October.** No booking under that name in 2026 (reported, from your booking software), and the reviewer's only other review is five stars for a clinic in Chorlton left the same day. Owner: you. Effort: low.

## Where you stand

| Business | Total | Rating | Last 90 days | Per month | Newest (days ago) | Typical gap (days) |
|---|---|---|---|---|---|---|
| **Example Physiotherapy** | 47 | 4.7 | 5 | 1.7 | 15 | 11 |
| Didsbury Physio Studio | 132 | 4.9 | 14 | 4.7 | 2 | 7 |
| Withington Sports Injury Clinic | 88 | 4.8 | 8 | 2.7 | 9 | 13 |
| Chorlton Physio & Pilates | 61 | 4.6 | 7 | 2.3 | 14 | 30 |

**Findings**

- Velocity: 5 new reviews in 90 days against a competitor median of 8. To match it, aim for about 3 a month.
- Recency: newest review is 15 days old; Didsbury Physio Studio typically gets one every 7 days.
- Bursts: half or more of the recent reviews arrived within two weeks, then slowed. A routine (SMS within the hour, one email follow-up) flattens this.

Measured with review_velocity.py from the dates you shared. Chorlton Physio & Pilates' dates are Google's relative dates, so its figures are rough.

**Target:** at least 3 new reviews a month to match the competitor median, every month. Didsbury Physio Studio, the clinic you most often lose to, gets about 4 or 5.

From review_tracker.py on your last 6 months (measured, from your screenshots):

| Month | New reviews | Avg rating | Requests sent | Reviews per 100 requests | Replied | Median days to reply | Mention a service | Mention a place |
|---|---|---|---|---|---|---|---|---|
| 2026-06 | 8 | 5 | - | - | 8 of 8 | 7 | 25% | 0% |
| 2026-07 | 1 | 5 | - | - | 1 of 1 | 11 | 100% | 100% |
| 2026-08 | 1 | 4 | - | - | 1 of 1 | 10 | 100% | 0% |
| 2026-09 | 2 | 5 | - | - | 2 of 2 | 8 | 50% | 50% |
| 2026-10 | 2 | 1.5 | - | - | 0 of 2 | - | 0% | 0% |
| 2026-11 | 1 | 5 | - | - | 0 of 1 | - | 100% | 0% |

- **Replies:** 40% of reviews in the last 90 days have one; the median wait is 8 days. Aim for every review within 2 working days, negative ones the same day.
- **What reviews say:** 40% mention a service, 20% a place. The June burst was mostly one-line ("Excellent.", "Great team."), which helps people choose less than "sorted my lower back pain in four sessions".
- **Unanswered:** the 1-star (41 days), the 2-star (29 days) and a 5-star (15 days).
- **Regulated check:** 4 replies flagged (below).

## The request flow

| Touch | Trigger | Delay | Owner |
|---|---|---|---|
| SMS | Booking software: appointment marked complete, patient's 2nd appointment of a course, not asked in the last 180 days | 30 minutes | Automatic; practice manager sets it up |
| Email | Same patients, if the software can send email | 3 days after the SMS | Automatic |
| QR code | Card on the reception desk and by the card reader | At payment | Reception |
| Staff prompt | When a patient says something positive, and at payment for course patients | In person | Reception and physios |

Why the second appointment: your patients come for 3 to 6 sessions, so asking after every one would annoy them, and after the first they haven't felt a difference yet. The software's "not asked in the last 180 days" filter stops repeats; if it doesn't have one, add a "review asked" date column to the patient list.

**Your direct review link:** in your Business Profile on Google, choose the option to ask for reviews and copy the link (it starts g.page/r/). Test it on a phone that isn't signed in to the clinic's Google account: it should open the star-rating box in one tap. Use the same link in the SMS, the email and the QR code.

## Messages

**SMS** (148 characters with a typical g.page link, so one text)
> Thanks for visiting Example Physiotherapy today. If you'd like to share your experience, please leave us a Google review: {link}

Set the software to send from the clinic's name, so the text doesn't need a sign-off.

**Email** (3 days later, once)

Subject: **A quick favour?**

> Hi {first name},
>
> Thank you for choosing Example Physiotherapy. If you haven't had a chance yet, we'd really appreciate a Google review. It takes about a minute:
>
> [Leave a review]({link})
>
> If you'd like to share your experience, it helps others in Didsbury choosing a clinic. And if anything wasn't right, reply to this email and our practice manager will be in touch.
>
> Thank you,
> The Example Physiotherapy team
>
> *Don't want emails like this? Reply "stop" and we'll take you off.*

**QR card** (reception desk, A6)
> **Thank you for visiting**
> Leave us a Google review. Point your phone camera here.
> [QR code]
> It helps other people in Didsbury find us.

**Receipt footer**
> Thank you for choosing Example Physiotherapy. A Google review helps other people in Didsbury find us: scan the code at reception or use the link in your text.

**Staff script**
- Reception, at payment for a course patient: "You'll get a text from us shortly with a link, if you'd like to leave a review. Thank you for coming in."
- Anyone, when a patient says something positive: "Thank you, that's lovely to hear. If you'd be happy to put that in a Google review, the link's in the text we'll send you."
- Don't: ask only patients who seem pleased, hand over the clinic iPad to review on the spot, or suggest what to write.

Prompting for the service and place: the email asks them to share their experience "for others in Didsbury choosing a clinic". That's as far as a clinic should go. Patients often name their treatment and area anyway; let them.

## Reply templates

All replies: thank the person, say nothing about whether they were a patient, what they came for, who saw them or how it went. Sign off "The Example Physio team".

**Positive**
> Thank you for taking the time to leave a review. We're glad you found the team helpful.

> Thank you for your kind words. We'll share them with everyone here.

> Thank you for this lovely review. It means a lot to the whole team.

**Neutral**
> Thank you for your feedback. We take every comment seriously and use it to improve. If you'd like to talk about anything, please contact our practice manager on 0161 496 0000.

**Negative**
> We're sorry to read this. We can't discuss individual circumstances here, but we'd welcome the chance to talk. Please contact our practice manager on 0161 496 0000 or hello@example-physio.co.uk.

> Thank you for raising this. Confidentiality means we can't respond to specifics publicly, but we'd like to hear from you directly. Please call 0161 496 0000 and ask for our practice manager.

## Replies to post now

**2 stars, 21 October** ("waited 25 minutes... invoice was different to what I was quoted")
> We're sorry to read this, and thank you for raising it. We can't discuss individual circumstances here, but we'd like to put this right. Please contact our practice manager on 0161 496 0000 or hello@example-physio.co.uk.

Then fix the cause: if running late is common, reception texts patients when a physio is more than 10 minutes behind; and every price is confirmed in writing at booking.

**1 star, 9 October** ("Terrible. Avoid.")
> We're sorry to see this. We'd like to understand what happened, so please contact our practice manager on 0161 496 0000.

Calm and short: readers judge the reply. Report it as well (below).

**5 stars, 4 November** (shoulder)
> Thank you for taking the time to leave such a kind review. We'll share it with the team.

**Rewrites of the flagged replies** (edit each existing reply on the profile)

| Review | Current reply says | Replace with |
|---|---|---|
| 28 Sep, 5 stars | "Glad your back pain is sorted after your sessions with Tom." | Thank you so much for this review. We'll pass it on to the team. |
| 15 Aug, 4 stars | "we're glad you enjoyed your sports massage." | Thank you for the review, and for the feedback. It's always useful to hear. |
| 19 Jul, 5 stars | "Great to hear your knee is doing well!" | Thank you for taking the time to write this. It means a lot to everyone here. |
| 25 Jun, 5 stars | "Glad we could help your neck!" | Thank you for your kind words. |

## Fake or competitor reviews

**1 star, 9 October, "Terrible. Avoid."**
- Policy reason: conflict of interest (the reviewer appears connected to a competitor) or fake (no record of the person).
- Evidence to keep: a screenshot of the review and the reviewer's profile showing their only other review, five stars for a Chorlton clinic on the same day; the review link; a private note that no booking matches the name in 2026. Don't send patient records to anyone.
- Report: on Maps, open the review's menu, report it under conflict of interest. Check the status in Google's Reviews Management Tool after a few days. If it's rejected, appeal once with the two lines of evidence above.
- Log: date reported, category, status, appeal date, outcome. Check it in the monthly routine.

## Monthly routine

First Tuesday of each month, 30 minutes, practice manager:
1. Copy the month's reviews and replies into reviews-log.json, plus the number of review texts the booking software sent.
2. Run `python scripts/review_tracker.py reviews-log.json --months 6 --regulated`.
3. Check new reviews against the target of 3 a month. If requests held but reviews fell, check the send delay and tap the link; if requests fell, check the automation is still on.
4. Reply to anything unanswered, lowest rating first. Replies twice a week anyway: Tuesday and Friday mornings.
5. Fix any reply the regulated check flags.
6. Check the removal report's status.
7. Every quarter, refresh the competitor dates and re-run review_velocity.py.

## Not checked
- **Request-to-review rate.** There are no requests yet to measure against. From December, the tracker shows reviews per 100 requests; that's the number to watch.
- **Whether reviews are being filtered.** If patients say they left a review that never appeared, note the dates; filtering of the June burst is possible but not visible from outside.
- **Doctify or other platforms.** Not looked at. Keep the request to the one Google link.

If you'd rather have it done with you: localseoconsultant.net/consulting/local-seo-audit/
