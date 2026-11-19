# Local SEO audit: Example Skin Clinic

19 November 2026 · 1 location · Data: one DataForSEO geo-grid for "acne scar treatment", plus the profile details, review dates, listings and AI answers you shared

## The short version
Google can find you: you rank first for "acne scar treatment" at the clinic door and show for your own name, but Yell still has your old Coldharbour Lane address and Treatwell uses a different name, so that is the first thing to tidy. The real break is the next rung up: your profile calls you a "Medical clinic", lists no acne scar or microneedling service, and links to a homepage covering 31 treatments, so Google isn't sure that's what you do, and you drop out of the top 3 about 1 km from the clinic. Fixing the categories, services and treatment pages, and restarting reviews, should widen the area where you win and give AI assistants something to name you for.

## Do these three first
1. **Correct Yell and Treatwell.** Yell shows your old address (4 Coldharbour Lane, SW9 8PR) and an old phone number, and Treatwell calls you "Example Skin & Laser Clinic Brixton". Treatwell is one of the two sources ChatGPT and Gemini cited. Owner: you. Effort: low.
2. **Change your primary category to "Skin care clinic".** You use "Medical clinic"; two of the three competitors beating you use "Skin care clinic" and the third "Dermatologist". The primary category is the strongest signal you control for what you treat. Owner: you. Effort: low.
3. **Add "Acne scar treatment" and "Microneedling" to your profile services.** Right now the profile lists only "Facials", "Laser" and "Consultation", so two of your three money searches aren't on it at all. Owner: you. Effort: low.

## Where you rank

| Search | Strong radius | Top 3 | Top 10 | Who takes over |
|---|---|---|---|---|
| acne scar treatment | 1.0 km | 4 of 25 points (16%) | 9 of 25 (36%) | Skin Clinic Clapham, Brixton Dermatology (top 3 at all 25 points), Stockwell Skin (west side), Herne Hill Skin (east side) |
| microneedling | Not scanned | | | |
| skin clinic brixton | Not scanned | | | |

Measured: 5 by 5 grid, points about 1 km apart, centred on the clinic. Your rank at each point:

```
  -   -  14   -   -
  -   9   4   8   -
 12   3   1   2  11
  -   6   2   7   -
  -   -  13   -   -
```
(- = not in the results; centre is the clinic; north at the top)

You are first at the door and top 3 one point away to the west, east and south. North, toward Stockwell, you are already fourth at 1 km. By 2 km you are 11th to 14th, and at the corners you aren't in the results at all. Your patients come from about 2 miles (3 km) away, so you are winning roughly a third of the area you serve. Herne Hill Skin isn't on your brief's competitor list but holds the top 3 on the east side; worth watching.

## Findings

Order from prioritise.py, with three changes: the patient-confirming review replies move to month 1 because they are a regulatory risk and take ten minutes; the review routine moves to month 1 because reviews dried up and need months to build; the local mentions move to month 3 because they work best once the category, services and pages are fixed.

### Month 1

**Yell and Treatwell describe a different business**
- Evidence: from the 4 listings you found (reported, checked with nap_check.py), Yell has 4 Coldharbour Lane, SW9 8PR and 020 7946 0999; Treatwell has the name "Example Skin & Laser Clinic Brixton". Your website footer and Facebook match.
- Fix: log in to both. On Yell, change the address to 12 Acre Lane, London SW2 5SG and the phone to 020 7946 0123. On Treatwell, change the name to "Example Skin Clinic", exactly as on your profile and signage.
- Owner: you. Effort: low.

**Primary category is "Medical clinic"; two of three competitors use "Skin care clinic"**
- Evidence (reported): your primary is "Medical clinic", secondary "Beauty salon". Skin Clinic Clapham and Stockwell Skin use "Skin care clinic"; Brixton Dermatology uses "Dermatologist". These three hold the top 3 wherever you drop out of it.
- Fix: change the primary category to "Skin care clinic". Remove "Beauty salon" unless you offer salon services such as nails or hair. Add "Dermatologist" as a secondary only if a dermatologist sees patients at the clinic.
- Owner: you. Effort: low.

**Profile services don't include acne scar treatment or microneedling**
- Evidence (reported): services listed are "Facials", "Laser" and "Consultation".
- Fix: add "Acne scar treatment" and "Microneedling", each with two lines on what it is and that it is done at the Brixton clinic. Rename "Laser" to the laser treatments you actually do, for example "Laser skin resurfacing".
- Owner: you. Effort: low.

**Homepage title says "Home" instead of what you do and where**
- Evidence (reported): the title is "Example Skin Clinic | Home", and this is the page your profile links to.
- Fix: change the title to "Skin Clinic in Brixton | Acne Scar Treatment & Microneedling | Example Skin Clinic" and the main heading to "Skin clinic in Brixton". The opening lines should say what you treat and where, in the words patients use.
- Owner: your web person. Effort: low.

**No page for acne scar treatment or microneedling**
- Evidence (reported): the homepage lists 31 treatments with one paragraph each. Neither money-search treatment has its own page.
- Fix: build one page for each: what it is, who it suits, who carries it out and their qualifications, how many sessions and how long each takes, price guidance, real photos of the room and team, and the address with directions from Brixton station. Put a book button at the top. Then point the profile's website link at the acne scar treatment page. Ask your compliance lead to check any claims about results.
- Owner: your web person. Effort: medium.

**Two review replies confirm the reviewer was a patient**
- Evidence (reported): about a third of reviews have replies. Two say "thanks for choosing us for your acne treatment", which confirms the person was a patient and names their condition.
- Fix: edit those two replies today. Then reply to every review with a warm line that says nothing about the person or their care. For example: "Thank you for taking the time to leave a review. We're glad you found the team helpful." Or: "Thank you for your feedback. If you'd like to talk about anything, please call us on 020 7946 0123."
- Owner: you. Effort: low.

**2 new reviews in 90 days against a competitor median of 9**
- Evidence (measured with review_velocity.py from the dates you shared): 2 reviews in 90 days (0.7 a month), newest 50 days old. Brixton Dermatology got 11 in the same period (newest 4 days ago) and Skin Clinic Clapham 7. 8 of your last 12 reviews came between 8 and 14 July, then stopped. Your 4.9 rating is the best of the three, so this is about flow, not quality.
- Fix: send an SMS with a one-tap review link as the patient leaves, one email follow-up two or three days later, and keep a QR code at reception. Aim for about 3 a month, every month. Ask patients to mention which treatment they had and that it was in Brixton, without scripting their words.
- Owner: you. Effort: medium.

### Month 2

**No booking link on the profile**
- Evidence (reported): hours and phone are set; the booking link is empty.
- Fix: add your online booking page as the booking link, or the consultation booking form if every treatment starts with a consultation.
- Owner: you. Effort: low.

**No prices, and the book button is only in the footer**
- Evidence (reported): no prices or price guidance anywhere on the site. On a phone, a patient has to scroll past 31 treatments to find the book button.
- Fix: put a book button and the phone number at the top of every page, visible on a phone without scrolling. Add "from" prices or a price range for each treatment, and the consultation fee.
- Owner: your web person. Effort: low.

**22 photos, mostly stock**
- Evidence (reported): 22 profile photos, most of them stock images.
- Fix: replace them with real photos: the entrance on Acre Lane, reception, each treatment room and the team. Add a few each month. Before-and-after photos only with the patient's written consent and your compliance lead's sign-off.
- Owner: you. Effort: low.

### Month 3

**Named in 0 of 6 AI answers; Brixton Dermatology in 5 of 6**
- Evidence (reported): you asked ChatGPT and Gemini "best clinic for acne scar treatment in Brixton" three times each. Brixton Dermatology was named 5 times, Skin Clinic Clapham 3, Example Skin Clinic 0. The answers cited a Time Out "best skin clinics in south London" article and a Treatwell listing page.
- Fix: once Treatwell has your correct name, complete it: acne scar treatment and microneedling listed by name, prices, real photos, and the same description as your profile. Contact the Time Out writer when the article is next updated, with the new treatment pages and your practitioners' credentials. Make sure the treatment pages say plainly what you do, where, for whom and at what price, so an assistant has something to quote.
- Owner: you. Effort: medium.

**Top 3 only within 1 km; patients come from about 3 km away**
- Evidence (measured): see the grid above. Strong radius 1.0 km; top 3 at 16% of points, top 10 at 36%.
- Fix: most of this should move with the month 1 fixes. Re-run the same grid first. Where you still drop out, earn three local mentions that link to the acne scar treatment page: a feature in Brixton or Lambeth local press, a listing with the local business association, and a page from a nearby partner such as a GP, pharmacy or gym.
- Owner: you. Effort: medium.

**Facebook page has no phone number**
- Evidence (reported): right name and address, no phone.
- Fix: add 020 7946 0123.
- Owner: you. Effort: low.

**No LocalBusiness schema on the site**
- Evidence (reported): no LocalBusiness structured data on the homepage.
- Fix: add LocalBusiness schema with the name, address and phone exactly as on the profile: Example Skin Clinic, 12 Acre Lane, London SW2 5SG, 020 7946 0123. Drop "Ltd" from the footer name so the two match.
- Owner: your web person. Effort: low.

## Don't spend time on

- **A redesign with video backgrounds.** Patients searching on a phone want to see the treatment, the price and a book button in a few taps. Video backgrounds slow the page and push those down. The two treatment pages and a book button at the top will do more for bookings.
- **40 "acne treatment in <town>" pages.** Pages that only swap the town name rarely rank for long, dilute the pages that sell, and give AI assistants nothing to quote. You are one clinic in Brixton; the grid shows where you can win, and that is the area to build for. One strong acne scar treatment page beats 40 thin ones.

## Not checked

- **Rankings for "microneedling" and "skin clinic brixton"**: only acne scar treatment was scanned. Run the same 5 by 5 grid for each.
- **Maps against the local pack and AI Mode**: the grid covers Google Maps only. A scanning tool that covers all three would show which surface you lose on.
- **Other profiles at 12 Acre Lane**: search Maps for the address and each practitioner's name. Extra practitioner or old Coldharbour Lane profiles split reviews and compete with the clinic.
- **Competitors' services, photos and pages**: only their primary categories were checked. Look at their profile services and the page each links to for acne scar treatment.
- **Stockwell Skin's reviews**: not in the review data. Add its count and recent dates to compare against all three.
- **What your reviews say**: check how many mention a treatment or Brixton.
- **Other directories and local links**: only 4 listings were checked. Search your name with the old phone number (020 7946 0999) and the old address to find others still carrying them, and look at which local sites link to your competitors.
- **Indexing and mobile speed**: search `site:example-skin-clinic.co.uk` to confirm your pages are in Google, and test the homepage in PageSpeed Insights on mobile.

## How to measure progress
- Re-run the same rankings check in 30, 60 and 90 days, from the same points.
- Track calls, website clicks and direction requests from the Business Profile dashboard monthly.
- Track new reviews per month against Brixton Dermatology.

## Next steps
Work through month 1, then run this audit again with your brief to see what moved.

If you want it done with you, Mani Bharij runs this audit personally, with full geo-grid scans, a recorded walkthrough and 90 days of follow-up: localseoconsultant.net/consulting/local-seo-audit/
