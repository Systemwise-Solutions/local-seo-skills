# Tracking: the minimum to see which stage moved

Track the routes this business actually makes money through, and nothing more, because unused tracking is noise. For most businesses that means some of: calls, website visits from the profile, the main website action (form, booking, reservation, order), and where customers came from. Setup screens change; link the vendor's own docs and say to follow them.

## 1. Call tracking number on the profile (if calls matter)


- Get a local-looking tracking number (same area code as the main number) from a call tracking provider or the phone system.
- On the Business Profile, put the **tracking number as the primary phone** and the **main number as an additional phone**. Google can still match the main number to the business across the web.
- Keep the **main number** in the website's schema, the footer of record, and every directory listing. Changing the main number everywhere breaks consistency, which caps rankings.
- The tracking number forwards to the same phone as the main number, so nothing changes for whoever answers.
- On the website, a second tracking number (or dynamic number insertion from the provider) can separate website calls from profile calls. Optional; the profile number matters most.
- Check the provider records answered and missed calls by hour. That is the Reached stage.

If call tracking isn't possible, Business Profile calls (taps on the call button) are the fallback. They're not connected calls, so compare them with the phone log rather than treating them as enquiries.

## 2. UTM on the profile website link

Add UTM parameters to the website link on the profile so profile visits show up as their own campaign in GA4:

```
https://example.co.uk/?utm_source=google&utm_medium=organic&utm_campaign=gbp
```

Use a different `utm_content` for the booking or appointment link if it goes to the same site, for example `utm_content=booking`. Multi-location: one campaign value per location, or `utm_content=<location>`.

In GA4, filter by session campaign `gbp` to see profile visits, their landing page and their key events.

## 3. GA4 key events

Mark the events for this business's main actions as key events in GA4 (Admin > Events, or Admin > Key events). Fire each on the completed action, never the start, because a started booking or a clicked button counts failures too:

| What | Event | Fire it on |
|---|---|---|
| Calls from the website | `click_to_call` (or the provider's event) | A click on any `tel:` link. Tracked call events from the provider are better, because they count connected calls. |
| Form enquiries | `generate_lead` | A successful submission: the thank-you page or the form's success callback. Never on the button click, which counts failed sends too. |
| Bookings or reservations | `booking_complete` (or the booking tool's own event) | A confirmed booking, from the booking tool's GA4 integration or its confirmation page. |
| Online orders | `purchase` (or the ordering platform's own event) | A completed order. Many ordering platforms run on their own domain; check whether they pass events back, and if not, use their own reports by source. |
| Directions | a click on the directions or map link | Only a signal of intent; the visit itself happens offline. |

Then check each one fires: tap the call link on a phone, submit a test form, make and cancel a test booking, and watch GA4's Realtime or DebugView.

## 4. Customers who walk in

Visits can't be tracked from the website. Use what the business can count: a till or booking system that records "how did you find us", a weekly tally at the door or counter, a profile-only offer or code, and profile direction requests as the leading signal. Read these as trends, not exact counts, and keep the method the same across both periods.

Installing GA4 itself, verifying Search Console, consent mode and tag managers are setup work beyond this skill. If SEO for AI Agents is installed, hand over to `seo-operations-measurement`. If not: install GA4 with one tag (not two), confirm in Realtime that page views arrive, then add the three key events above.

## What the business can then see

| Question | Where |
|---|---|
| Did more people see the profile? | Profile performance: views |
| Did more of them act? | Profile performance: calls, website clicks, directions, divided by views |
| Did profile visitors convert on the site? | GA4: campaign `gbp`, key events by landing page |
| Were calls answered? | Call tracking: answered vs missed, by hour |
| Did enquiries become revenue? | Booking, order or job system, with source recorded |
| Did people who looked up directions come in? | Profile direction requests against the business's own visit count |
