# What was checked (fictional)

Example Roofing does not exist. These are the checks the skill asked for and what came back, made up for the example.

## Reported by the owner

**Missed calls by time, Aug to Oct 2026** (phone provider's log, 95 missed in total)
| When | Missed |
|---|---|
| Weekdays 7:00 to 8:30 | 36 |
| Weekdays 12:00 to 14:00 | 19 |
| Weekdays 8:30 to 12:00 and 14:00 to 17:00 | 14 |
| Weekdays after 17:00 | 6 |
| Saturdays | 20 |

Missed calls called back the same day: "maybe half" (reported, not logged).

**Phone test** (owner rang his own number from his wife's phone)
- 7:45 Tuesday: rang 8 times, then a generic network voicemail ("the person you are calling is not available").
- 12:30 Tuesday: answered.
- 10:00 Saturday: rang out to the same generic voicemail.

**Form test** (owner submitted both forms with "TEST" in the name)
- "Get a free quote" form on the homepage and every service page: success message shown, nothing arrived after 30 minutes. The web designer confirmed it sends to office@, the office manager's mailbox, which was closed when she left in June.
- "Request a call back" form on the contact page: arrived in 2 minutes at the owner's address.

**Quotes**: since June, quotes are sent by the owner in the evening and not chased.

## Checked by the skill (free tier)

**Business Profile** (viewed on Maps)
- Hours: Monday to Friday 8:00 to 17:00, Saturday closed. Owner says he works most Saturday mornings from April to October.
- Phone: the office landline (diverts to mobile). Matches the website footer.
- Website link: homepage, no UTM.
- Reviews: 4.8 from 63 (reported). Newest 5 weeks old; two nearest competitors both have reviews from the last week.
- Photos: newest owner photo from 2024.
- Services listed: roof repairs, flat roofs, guttering, chimney repairs.

**Homepage at phone width (390px)**
- First screen: a full-height slider of three stock roof photos with the line "Quality Roofing Solutions".
- Phone number: only inside the menu. Not a `tel:` link in the footer.
- "Get a free quote" button: below the slider, after one scroll.
- Quote form: 9 fields including address, budget and "how did you hear about us", all required.
- PageSpeed Insights mobile: not run. Slider images are about 2 MB each (measured from the page source), so the first screen loads late on a slow connection.

**GA4**: installed (tag found in the page source). Owner has no key events set up, per the web designer.
