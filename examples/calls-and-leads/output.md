# Calls and leads: Example Roofing (fictional)

19 November 2026 · 1 location · Data: your profile screenshots, phone log, quote inbox and diary for Aug to Oct 2025 and 2026, plus checks of the profile and homepage

*Example Roofing and every figure here are fictional. This is the output the calls-and-leads skill produced from the files in this folder.*

## Where the leak is
People are still finding you: profile views are down only 4% on the same months last year, and website clicks from the profile are up 14% (reported). The enquiries are being lost after that. Your quote form has sent every request since June to a mailbox that no longer exists, and almost a third of calls now go unanswered, mostly before 8:30am and on Saturdays. At last year's rates that is about 29 quote requests and 21 answered calls a month you aren't getting (inferred), which goes a long way to explaining why bookings fell from 47 to 29 a month.

## Do these three first
1. **Point the quote form at your own inbox today, and test it.** Since the office manager's mailbox closed in June, the "Get a free quote" form shows a success message and sends nothing. Form enquiries fell from 32 to 7 a month, and the 7 all came through the contact page's call-back form. Owner: your web designer. Effort: low.
2. **Stop losing early and Saturday calls.** 56 of the 95 missed calls were weekdays before 8:30am or Saturdays (reported), and the voicemail is the network's generic message. Set a missed-call text, record your own voicemail, and either answer from 7:30 and on Saturday mornings or pay an answering service for those hours. Owner: you. Effort: low.
3. **Put a call button and a quote button on the first screen of the homepage on a phone.** Right now the first screen is a stock photo slider and the number is hidden in the menu, while more people than last year are clicking through from the profile. Owner: your web designer. Effort: low.

## The funnel

Monthly averages, from `funnel.py` (all counts reported):

| | Aug-Oct 2025 | Aug-Oct 2026 | Change |
|---|---|---|---|
| Profile views | 3,800 | 3,633 | -4% |
| Calls from profile | 114 | 100 | -12% |
| Website clicks | 155 | 176 | +14% |
| Direction requests | 17 | 16 | -8% |
| Form fills | 32 | 7 | -77% |
| Bookings | 47 | 29 | -38% |
| Calls answered | 106 | 73 | -31% |
| Calls missed | 12 | 32 | +164% |

| Rate | Aug-Oct 2025 | Aug-Oct 2026 | Change |
|---|---|---|---|
| Profile action rate | 7.5% | 8.0% | +7% |
| Call rate | 3.0% | 2.8% | -8% |
| Website click rate | 4.1% | 4.8% | +19% |
| Form rate | 20.6% | 4.2% | -80% |
| Answer rate | 89.8% | 69.7% | -22% |
| Booking rate | 32.2% | 27.2% | -15% |

The profile is doing its job: the share of viewers who act went up. The leaks are the website form and the phone. Form fills are now under 30 a month, so read that rate as rough, but a fall from 32 to 7 with a confirmed broken form isn't noise. Profile calls count taps on the call button; your phone log counts every call to the office line, so the two won't match exactly.

## Findings by stage

### Seen: no leak
Views are down 4% against the same three months last year. That's within normal variation for a seasonal trade. No ranking work is needed to explain this drop. If you want to know how far you rank across Cheam, Carshalton and Banstead, that's a separate job for `local-seo-audit`.

### Profile converts

**Hours say closed on Saturday, when you work most Saturday mornings**
- Evidence: 20 missed calls on Saturdays in three months (reported); profile shows Saturday closed.
- Fix: if you'll answer, set Saturday 8:00 to 12:00 from April to October and back to closed for winter, with special hours for bank holidays. If you won't answer, leave it closed and let the missed-call text do the work.
- Owner: you. Effort: low.

**Newest photo is from 2024, and the newest review is 5 weeks old**
- Evidence: two nearest competitors both have reviews from the last week (checked on Maps).
- Fix: photograph every job (before, during, after, with the street). Add 5 recent ones now and a couple a month. Text the review link when the job is signed off, asking customers to say what you did and where.
- Owner: you. Effort: low. This helps you get chosen; it isn't why the phone went quiet.

### Page converts

**The quote form sends to a closed mailbox**
- Evidence: test submission showed the success message and never arrived; web designer confirmed it sends to office@, closed in June. The contact page form works (arrived in 2 minutes).
- Fix: change the recipient to your own address and add a second recipient (an office or shared address you'll keep). Submit a test from a phone and from a laptop and check both arrive. Ask the designer to also check what happened to submissions since June: some form tools keep a copy you can still reply to.
- Owner: web designer. Effort: low.

**The first screen on a phone is a slider, with no call or quote button**
- Evidence: at 390px the first screen is three stock photos and "Quality Roofing Solutions"; the number is only in the menu; slider images are about 2 MB each (measured).
- Fix: replace the slider with one real photo of your work, compressed, and put this above it:

```
Roof repairs in Sutton, Cheam and Carshalton

Leaks, slipped tiles, flat roofs and chimneys. Free quotes, usually within 48 hours.

[Call 020 0000 0000]  [Get a free quote]
4.8 from 63 Google reviews
```

Make the call button a `tel:` link with the same number as the profile. Put the number as a `tel:` link in the footer too.
- Owner: web designer. Effort: low.

**The quote form asks for nine things before anyone can send it**
- Evidence: address, budget and "how did you hear about us" are all required.
- Fix: cut it to name, phone, postcode, and "what's the problem?" with an optional photo upload. Ask the rest when you call back.
- Owner: web designer. Effort: low.

### Reached

**Almost a third of calls go unanswered**
- Evidence: answer rate fell from 90% to 70% (reported, phone log). 36 missed weekdays 7:00 to 8:30, 20 on Saturdays, 19 at lunchtime. The office manager used to answer from 7:30; since June the line diverts to your mobile on a roof. Only "maybe half" are called back the same day.
- Fix, in this order:
  1. Record your own voicemail today:
     > "You've reached Example Roofing. Sorry we missed you, we're probably up a roof. Leave your name, number and postcode and we'll call you back today. Or text this number a photo of the problem."
  2. Turn on a missed-call text if your phone provider offers it (most VoIP systems do; ask yours):
     > "Sorry we missed your call, this is Example Roofing. We'll call you back today. If it's a leak, text us a photo and your postcode."
  3. Block 12:30 and 16:30 every working day to return every missed call. Keep a tally of missed calls and call-backs on paper or a spreadsheet for 30 days.
  4. If the tally shows you still can't get back to them the same day, price an answering service for 7:00 to 8:30 and Saturdays only.
- Owner: you. Effort: low.

### Booked

**Quotes go out and nobody chases them**
- Evidence: booking rate fell from 32% to 27% (reported). Since June, quotes go out in the evening and aren't followed up.
- Fix: a two-line follow-up text three days after each quote, and one call at seven days:
  > "Hi [name], it's [owner] from Example Roofing. Just checking you got the quote for [job]. Happy to answer any questions or book a date."
- Owner: you. Effort: low.

### Counted

**You can't see which stage moved**
- Evidence: no call tracking, no UTM on the profile link, GA4 has no key events (reported).
- Fix, on day one:
  - Add UTM to the profile's website link: `https://example-roofing-sutton.co.uk/?utm_source=google&utm_medium=organic&utm_campaign=gbp`
  - In GA4, mark three key events: a click on a `tel:` link, a successful quote form submission (on the success message or thank-you page, not the button click), and a successful call-back form submission. Test each in GA4's Realtime view.
  - Optional but useful: a call tracking number as the primary phone on the profile, with the office landline as the additional phone. Keep the landline on the website, in the schema and on every directory.
- Owner: web designer (GA4), you (profile). Effort: low.

## Fixes in order
1. Quote form recipient fixed and tested. Day 1.
2. Your own voicemail and the missed-call text. Day 1.
3. Tracking: UTM, GA4 key events, tested. Day 1 to 2.
4. Call-back blocks at 12:30 and 16:30, with a tally. From day 1.
5. Homepage first screen: call and quote buttons, slider out. Days 2 to 5.
6. Quote form cut to four fields. Days 2 to 5.
7. Quote follow-up texts. From day 1.
8. Saturday hours on the profile, if you'll answer. Day 1.
9. Photos and the review text after each job. From week 2, ongoing.

## 30-day measurement plan

### Baseline (Aug to Oct 2026, monthly averages, reported)
| Measure | Baseline | Source |
|---|---|---|
| Profile views a month | 3,633 | Profile performance |
| Profile action rate | 8.0% | Profile performance |
| Calls answered / missed a month | 73 / 32 | Phone provider log |
| Answer rate | 70% | Phone provider log |
| Form enquiries a month | 7 | Quote inbox |
| Bookings a month | 29 | Job diary |

### Days 1 to 7 (24 to 30 November 2026)
- Day 1: quote form fixed and tested (web designer); voicemail and missed-call text (you); Saturday hours decided (you); UTM on the profile link (you).
- Day 2: GA4 key events in and tested (web designer).
- Days 2 to 5: homepage first screen and shorter form (web designer).

### Every day
- Tally: missed calls, and whether each was called back the same day.

### Every week
- Profile calls, website clicks, directions and views for the last 7 days, from the profile's Performance screen.
- Quote form and call-back form enquiries; bookings in the diary.
- Anything else that changed: storms, prices, ads, time off.

### Day 30 (23 December 2026, read on 27 December or later because profile data lags)
- Put the 30 days into `funnel.json` as the second period, with the baseline as the first, and run `funnel.py`.
- Judge on the form rate and the answer rate, not on total calls. December is often quieter for roofing outside storm weeks, so also compare with December 2025 if you have it.
- What would show it worked: form rate back towards 20% of website clicks, answer rate back towards 90%. If the answer rate hasn't moved, the answering service goes in.

## Not checked
- Mobile speed: PageSpeed Insights not run. Run it on the homepage (mobile) after the slider comes out.
- Rankings beyond your own area: views held, so not needed for this drop. Run `local-seo-audit` if you want to win more of Banstead and Worcester Park.
- Enquiries lost since June: ask the web designer whether the form tool kept copies of submissions. If it did, ring those people this week.
- Lead quality: not checked. If the calls that do come in are for jobs you don't want, note the job type on the tally for the 30 days.

If you'd rather have it done with you: localseoconsultant.net/consulting/local-seo-audit/
