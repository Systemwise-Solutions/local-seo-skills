# Page plan: Holt Heating (fictional)

19 November 2026 · new site on boilerrepairleeds.co.uk · Data: free checks, plus your job counts, prices and proof list

*Holt Heating, its jobs, reviews and prices are fictional. This is the output the local-pages skill produced from the files in this folder.*

## The short version
You need seven pages to start, not thirty: a homepage that sells boiler repair in Leeds, three service pages for the work that pays, two area pages for Headingley and Rawdon and Yeadon where you already have the jobs and reviews to prove it, and a contact page. Keep your Google profile as "Holt Heating": the domain doesn't need to match it, and renaming the profile to "Boiler Repair Leeds" when that isn't your registered or signed name is a common way trade profiles get suspended. Five more areas are on hold with a short list of what to collect, so each page has something real on it when it goes live.

## Do these three first
1. **Write the homepage as "Boiler repair in Leeds" with your real name in the header.** It's the page your profile will link to and the one that matches the domain, and repairs are 45% of your revenue (reported). Owner: you and your web person. Effort: medium.
2. **Build the landlord gas safety certificate page before the installs page.** You have 14 jobs and 3 reviews from Headingley, mostly landlords, and a September rush every year. It's the fastest route to repeat, bookable work. Owner: you. Effort: low.
3. **Leave the profile name as "Holt Heating" and point its website link at the homepage with tracking.** Use `https://boilerrepairleeds.co.uk/?utm_source=google&utm_medium=organic&utm_campaign=gbp` so profile visits show up separately once analytics is in. Owner: you. Effort: low.

## The domain and the name

The domain is an address, not a ranking plan. In my view an exact-match domain gives no map pack advantage: where you show in Maps still depends on your verified address in Horsforth, your category, your reviews and what your pages prove. It does no harm, and the homepage can target "boiler repair leeds" naturally.

What would do harm is a mismatch. Your van, invoices and registration say Holt Heating, so the site's header, footer, contact page and schema all say Holt Heating too, with "Boiler repair in Leeds" as the headline, not the name.

The site isn't built yet. If you have SEO for AI Agents installed, run its `new-site` job for the build (stack, rendering, analytics) and `seo-demand-keyword-research` to firm up demand; the pages below are the local page set it should build. If not: make sure every page is in the served HTML (not drawn by JavaScript after the page loads), and add GA4 and Search Console before launch.

## Page plan

| Page | URL | Action | Target search | Why |
|---|---|---|---|---|
| Homepage: boiler repair | / | create | boiler repair leeds | Profile links here. Repairs are 45% of revenue. Matches the domain. Includes evening callouts and powerflush as sections. |
| Boiler servicing | /boiler-service/ | create | boiler service leeds | 20% of revenue, repeat yearly, feeds repairs. Published price (£85). |
| Landlord gas safety certificates | /landlord-gas-safety-certificate/ | create | landlord gas safety certificate leeds | 15% of revenue, repeat yearly, strong proof in Headingley. |
| Combi boiler installation | /boiler-installation/ | create | combi boiler installation leeds | 15% now, highest value per job, and the work you want more of. "From £2,100" price and free survey. |
| Headingley | /areas/headingley/ | create | boiler repair headingley, gas safety certificate headingley | 14 jobs, 6 with photos, 3 reviews naming it, clear local specifics. |
| Rawdon and Yeadon | /areas/rawdon-yeadon/ | create | boiler repair rawdon, boiler service yeadon | 9 jobs, 4 with photos, 2 reviews, low competition, 3.6 km away. |
| Contact and areas covered | /contact/ | create | (supports all) | Name, phone, hours, areas covered, links to the two area pages. No street address: you're a service-area business. |
| Emergency boiler repair | none | don't create | | You work until 9pm weekdays, not 24/7. An emergency page would promise something you don't offer. Evening callouts go on the homepage with the real hours and price. |
| Powerflush, radiators | none | merge | | Under 5% of revenue, rarely searched on their own. A section on the homepage and the installs page. |
| Kirkstall, Bramley, Guiseley, Otley | none | hold | | Work there, not enough proof yet. See below. |
| Leeds city centre | none | don't create | | See "Changes" below. |

Profile links to: `https://boilerrepairleeds.co.uk/?utm_source=google&utm_medium=organic&utm_campaign=gbp`
Redirects: none (new site).

## Location pages: how they were decided

From `town_score.py` on your job counts (reported) and distances from Horsforth (measured):

| Town | km | Jobs | Local proof | Decision |
|---|---|---|---|---|
| Rawdon and Yeadon | 3.6 | 9 | 3/4 | create |
| Headingley | 4.5 | 14 | 3/4 | create |
| Kirkstall | 3.7 | 6 | 0/4 | hold |
| Bramley | 3.9 | 3 | 0/4 | hold |
| Guiseley | 6.2 | 2 | 0/4 | hold |
| Otley | 7.9 | 1 | 0/4 | hold |
| Leeds city centre | 7.7 | 2 | 0/4 | hold, changed to don't create |
| Horsforth | 0 | 19 | 4/4 | no page: base town |
| Roundhay | 9.0 | 0 | 0/4 | don't create |
| Harrogate | 18.0 | 1 | 0/4 | don't create |
| Wetherby | 19.1 | 0 | 0/4 | don't create |

Changes to the script's decisions:
- **Leeds city centre: hold to don't create.** The homepage already targets "boiler repair leeds". A city centre page would compete with it, and you've done 2 jobs there.
- **Horsforth: no page.** You're based there. The homepage says so in its opening lines and the contact page covers it.

What to collect for the holds:
- **Kirkstall** (closest to a page): 1 more job with photos, 1 more review that mentions Kirkstall, and one more local fact beyond the new-build flats (parking, boiler types you find there). Revisit after your next 3 jobs there.
- **Bramley and Guiseley**: photos of every job there from now on, and ask those customers to mention the area in their review. Revisit in the spring.
- **Otley**: 1 job so far. Don't plan for it yet.

To collect proof without scripting anyone: photograph every job (before, during, after) and note the street; when you send the review link, ask "if you're happy to, say what I did and where".

## Briefs

### Homepage: boiler repair in Leeds

- URL: `/`
- Target search: boiler repair leeds; also boiler repair near me, boiler engineer leeds, gas engineer horsforth
- Searcher: a homeowner or tenant in north-west Leeds with no heating or hot water, on a phone, who wants someone today or tomorrow at a known price.
- Title: Boiler Repair in Leeds | Holt Heating, Horsforth (46 characters)
- Meta description: Gas Safe boiler repairs across north-west Leeds. £75 callout including the first hour, evenings until 9pm. Call Sam at Holt Heating.
- H1: Boiler repair in Leeds
- Opening lines: what (boiler repairs, all makes), where (Horsforth and north-west Leeds), the safe-choice point (Gas Safe, published price, parts in the van).
- Above the fold on mobile: Call button (`tel:`), "Book a repair" button, "£75 callout including the first hour", "5.0 from 11 Google reviews" (update the count as it grows).
- Sections: common faults and what a repair involves; prices; evening callouts (until 9pm weekdays, £95); powerflush (when it helps, when it doesn't); who you are; areas covered (link to Headingley and Rawdon and Yeadon); other services (link to the three service pages); questions.
- Proof to gather: van photo with the Holt Heating name (needed), a photo of you at work (needed), Gas Safe number (needed), 2 reviews (supplied).
- Internal links out: /boiler-service/, /landlord-gas-safety-certificate/, /boiler-installation/, /areas/headingley/, /areas/rawdon-yeadon/, /contact/
- Schema: `HVACBusiness` with `@id` `https://boilerrepairleeds.co.uk/#business`, no street address, `areaServed` the six areas.
- Facts needed from owner: Gas Safe number, boiler makes you're happiest working on, typical repair time.

### Landlord gas safety certificates

- URL: `/landlord-gas-safety-certificate/`
- Target search: landlord gas safety certificate leeds; also gas safety certificate leeds, CP12 leeds
- Searcher: a landlord or letting agent with a deadline, often with several properties.
- Title: Landlord Gas Safety Certificate Leeds | Holt Heating (51 characters)
- Meta description: CP12 gas safety certificates for Leeds landlords. £70 for one appliance, £15 each extra. Certificates emailed the same day.
- H1: Landlord gas safety certificates in Leeds
- Opening lines: £70, same-day certificate, several houses in one visit, Headingley student lets.
- Above the fold on mobile: Call, "Book certificates", price, rating.
- Sections: what the check covers; price, including multi-property; how booking works with tenants (you arrange access, permit parking); the September rush and booking ahead; reminders each year (only if you'll actually send them); questions (what if an appliance fails, how long it takes).
- Proof: Tom's review (supplied), number of certificates done since August (needed).
- Internal links out: /areas/headingley/, /boiler-service/, /
- Schema: `Service`, `provider` the business `@id`, `offers` £70.
- Facts needed: do you send annual reminders? Do you work with letting agents directly?

### Boiler servicing

- URL: `/boiler-service/`
- Target search: boiler service leeds; also annual boiler service, boiler service horsforth
- Title: Boiler Service in Leeds, £85 | Holt Heating (43 characters)
- H1: Boiler servicing in Leeds
- Opening lines: £85, what's checked, why a service keeps the warranty valid.
- Sections: what a service includes; price; warranty (manufacturers usually require a yearly service; check yours); how long it takes; booking; areas; questions.
- Internal links: /, /boiler-installation/, area pages.
- Facts needed: time per service, whether you service all makes.

### Combi boiler installation

- URL: `/boiler-installation/`
- Target search: combi boiler installation leeds; also new boiler leeds, back boiler replacement leeds
- Title: Combi Boiler Installation Leeds, from £2,100 | Holt Heating (58 characters)
- H1: Combi boiler installation in Leeds
- Opening lines: from £2,100 fitted, free survey, back boiler removals in terraces.
- Sections: what's included; what changes the price (flue, pipework, moving the boiler); back boiler replacements (Headingley terraces: your two jobs, with photos); the boilers you fit and their warranties; how long it takes; survey and quote; finance (only if you offer it); questions.
- Proof to gather: before and after photos of both back boiler jobs (supplied), manufacturer installer accreditation if you have one (needed).
- Facts needed: boiler brands and warranty lengths, whether you're an accredited installer for any of them.

### Headingley

- URL: `/areas/headingley/`
- Target search: boiler repair headingley; gas safety certificate headingley; also gas engineer headingley
- Title: Boiler Repair and Gas Certificates in Headingley | Holt Heating (59 characters)
- H1: Boiler repairs and gas certificates in Headingley
- Opening lines: the work done there since August, response time from Horsforth, the terraces and student lets.
- Local detail: back boilers and cupboard boilers in terraces; September certificate rush; permit parking.
- Proof: 6 jobs with photos (supplied), Priya's and Tom's reviews (supplied).
- No address. Links to the landlord certificate page, installs page and homepage.

### Rawdon and Yeadon

- URL: `/areas/rawdon-yeadon/`
- Target search: boiler repair rawdon; boiler service yeadon
- Title: Boiler Repair in Rawdon and Yeadon | Holt Heating (48 characters)
- H1: Boiler repairs and servicing in Rawdon and Yeadon
- Local detail: long flue runs on hillside stone houses; loft boilers in bungalows near the airport (access, ladders, what the service involves).
- Proof: 4 jobs with photos (supplied), 2 reviews naming the area (supplied; owner to confirm which can be quoted).
- Facts needed: travel time from Horsforth at peak, any recurring faults you see there.

## Written pages

### Homepage

```markdown
# Boiler repair in Leeds

Boiler not firing, no hot water, or a fault code you don't recognise? I'm Sam, a Gas Safe engineer based in Horsforth, and I repair all makes of boiler across north-west Leeds. Callouts are £75 including the first hour, and I carry the common parts in the van so most repairs are done on the first visit.

[Call 0113 000 0000] [Book a repair]
£75 callout including the first hour · Evenings until 9pm · 5.0 from 11 Google reviews

## What a repair involves
I find the fault first and tell you what it'll cost before I fit anything. The most common jobs are failed fans, diverter valves, pressure problems and printed circuit boards. If a repair costs more than the boiler is worth, I'll say so.

## Prices
- Callout and first hour, weekdays 8am to 6pm: £75
- Evening callout until 9pm, Monday to Friday: £95
- Parts: quoted before fitting

## Evening callouts
I take repair calls until 9pm on weekdays. I don't offer a 24-hour service. If you call after 9pm, leave a message and I'll call back from 8am.

## Powerflush
If your radiators are cold at the bottom or the boiler is noisy, a powerflush can help. I'll tell you on the visit whether it's worth it.

## About Holt Heating
Holt Heating is me, Sam Holt. Gas Safe registered (number [Gas Safe number: owner to supply]). Six years as an engineer with a national heating company before going independent in 2026. Fully insured.

> "Boiler died on a Sunday night in our terrace off Cardigan Road. Sam came Monday morning, had the part in the van, sorted by 10." Priya, Headingley

## Where I work
Horsforth, Headingley, Kirkstall, Rawdon, Yeadon, Bramley and the rest of north-west Leeds, up to about 10 miles from Horsforth.
- [Boiler repairs and gas certificates in Headingley](/areas/headingley/)
- [Boiler repairs and servicing in Rawdon and Yeadon](/areas/rawdon-yeadon/)

## Other services
- [Boiler servicing, £85](/boiler-service/)
- [Landlord gas safety certificates, from £70](/landlord-gas-safety-certificate/)
- [Combi boiler installation, from £2,100](/boiler-installation/)

## Questions
**How quickly can you come out?** Usually the same or next working day. Call and I'll give you a time.

**Do you repair all makes?** Yes. [Owner to confirm any makes you don't work on.]

**Do you charge for a visit if you can't fix it?** The £75 covers the visit and first hour, including finding the fault. You won't pay for parts you didn't agree to.
```

Placeholders to fill: phone number, Gas Safe number, makes you don't work on.

### Headingley

```markdown
# Boiler repairs and gas certificates in Headingley

Since August 2026 I've done 14 jobs in Headingley: boiler repairs, two back boiler replacements in Victorian terraces, and gas safety certificates for landlords with student houses. I'm based in Horsforth, about 15 minutes away, and charge £75 for a repair callout including the first hour.

[Call 0113 000 0000] [Book a visit]
£75 repair callout · Landlord certificates from £70 · 5.0 from 11 Google reviews

## Terraces and back boilers
Many Headingley terraces still have old back boilers behind the fireplace, or a boiler squeezed into a kitchen cupboard. I've replaced two back boilers with combis this year [photos: before and after]. If yours is still going, it's worth a service; when it goes, I'll quote a replacement on the same visit. [See combi boiler installation](/boiler-installation/).

## Gas certificates for student lets
Most of the gas certificates I do in Headingley are for landlords getting houses ready before tenants arrive in September. I can do several houses in one morning and email the certificates the same day. £70 for one appliance, £15 for each extra. [Landlord gas safety certificates](/landlord-gas-safety-certificate/).

> "Did gas certificates for all four of our student houses in one morning and sent the certificates the same day." Tom, landlord, Headingley

## Parking
Most Headingley streets are permit parking. When you book, I'll ask you for a visitor permit so I can park outside.

## Recent jobs
- [Job 1: street, what was wrong, what I did, photo]
- [Job 2]
- [Job 3]

> "Boiler died on a Sunday night in our terrace off Cardigan Road. Sam came Monday morning, had the part in the van, sorted by 10." Priya, Headingley

## Also nearby
I work across north-west Leeds from Horsforth. [Rawdon and Yeadon](/areas/rawdon-yeadon/) · [All services](/)
```

Placeholders to fill: phone number, three recent jobs with street and photo, back boiler photos.

### Schema for the homepage

```json
{
  "@context": "https://schema.org",
  "@type": "HVACBusiness",
  "@id": "https://boilerrepairleeds.co.uk/#business",
  "name": "Holt Heating",
  "url": "https://boilerrepairleeds.co.uk/",
  "telephone": "[main number exactly as on the profile]",
  "priceRange": "££",
  "areaServed": [
    {"@type": "Place", "name": "Horsforth"}, {"@type": "Place", "name": "Headingley"},
    {"@type": "Place", "name": "Kirkstall"}, {"@type": "Place", "name": "Rawdon"},
    {"@type": "Place", "name": "Yeadon"}, {"@type": "Place", "name": "Bramley"}
  ],
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "08:00", "closes": "18:00"}
  ],
  "sameAs": ["[Maps URL of the Holt Heating profile]"]
}
```

No street address, because the profile hides it. Name matches the profile exactly.

## Internal links
- Homepage links to every service page, both area pages and contact.
- Each service page links back to the homepage and to the area pages where that service has jobs (certificates and installs to Headingley; servicing to Rawdon and Yeadon).
- Each area page links to the services done there and to the other area page.
- Contact links to both area pages.

## Not checked
- Search demand by town: only one Keyword Planner range was available (reported, and it covers the whole city). The area decisions rest on your jobs and proof, which is enough at this size.
- Competitors' pages: not reviewed for this plan. Before writing, search each target search and note what the top three pages prove that yours don't.
- Rankings: the profile is two months old. Do a 5-point check from Horsforth, Headingley, Kirkstall, Rawdon and Bramley before the site goes live so you have a baseline.

## How to measure
- Before the site goes live: the 5-point check above for "boiler repair" and "gas safety certificate", and the profile's calls and website clicks for October and November.
- Six weeks after launch: the same five points, the same searches, and calls, website clicks and enquiries by landing page.
- Every quarter: re-run `town_score.py` with the new job counts. Kirkstall is likely to move to create first.

## Log lines added
- 2026-11-19: page plan agreed, 7 pages for launch (homepage, 3 services, Headingley, Rawdon and Yeadon, contact). Re-check rankings and enquiries by landing page 6 weeks after launch.
- 2026-11-19: profile name kept as Holt Heating; website link set to homepage with UTM. Re-check profile clicks monthly.
- 2026-11-19: Kirkstall, Bramley, Guiseley, Otley on hold for proof. Re-run town_score.py at the next quarterly review.

If you'd rather have it done with you: localseoconsultant.net/consulting/local-landing-pages/
