# Schema

LocalBusiness schema tells search engines and AI systems which business the page is about. Its job here is consistency: name, address and phone exactly as on the Business Profile, character for character.

## Rules

- Use the most specific subtype that fits: `Plumber`, `HVACBusiness`, `Electrician`, `RoofingContractor`, `Dentist`, `MedicalClinic`, `LegalService`, `AccountingService`. Otherwise `LocalBusiness`.
- One LocalBusiness block per real location, with the same `@id` on every page that refers to it (for example `https://example.co.uk/#business`). Location pages for areas served don't get their own LocalBusiness; they reference the main one and describe the area in `areaServed`.
- `name`: exactly the profile name. Not the domain, not a tagline.
- `address`: exactly as on the profile. Service-area business with a hidden address: leave `streetAddress` out and keep `addressLocality`, `addressRegion` and `postalCode` only if you're comfortable showing them; otherwise use `areaServed` alone.
- `telephone`: the main number, as on the profile. If call tracking puts a different number on the website, the schema still carries the main number, so the business stays consistent across the web.
- `openingHoursSpecification`: same as the profile.
- `aggregateRating`: don't add it for the business's own reviews on its own site. Google doesn't show self-serving review stars for LocalBusiness, and invented or copied ratings are a risk.
- `sameAs`: the profile's Maps URL and the main directory and social profiles.
- Validate with Google's Rich Results Test and the Schema.org validator.

## Template: business (homepage or main location page)

```json
{
  "@context": "https://schema.org",
  "@type": "Plumber",
  "@id": "https://example.co.uk/#business",
  "name": "<exact profile name>",
  "url": "https://example.co.uk/",
  "telephone": "<main number as on profile>",
  "image": "https://example.co.uk/images/van.jpg",
  "priceRange": "££",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "<town>",
    "addressRegion": "<county>",
    "postalCode": "<postcode>",
    "addressCountry": "GB"
  },
  "areaServed": [{"@type": "Place", "name": "<area 1>"}, {"@type": "Place", "name": "<area 2>"}],
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "18:00"}
  ],
  "sameAs": ["<Maps URL>", "<main directory profile>"]
}
```

## Template: service page

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Boiler installation",
  "serviceType": "Boiler installation",
  "provider": {"@id": "https://example.co.uk/#business"},
  "areaServed": [{"@type": "Place", "name": "<area>"}],
  "offers": {"@type": "Offer", "priceCurrency": "GBP", "price": "<from price, only if published on the page>"}
}
```

Leave `offers` out if the page has no published price. Every value in the schema must also be visible on the page.

## Template: area page

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "<page title>",
  "about": {"@id": "https://example.co.uk/#business"},
  "mainEntity": {"@type": "Service", "name": "<services done in the area>", "provider": {"@id": "https://example.co.uk/#business"},
                 "areaServed": {"@type": "Place", "name": "<area>"}}
}
```
