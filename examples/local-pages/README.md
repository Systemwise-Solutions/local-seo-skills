# Example: a fictional gas engineer on an exact-match domain

Holt Heating, Horsforth, does not exist. Neither does its website. The domain, jobs, reviews and prices are made up to show the skill working. The places are real, with approximate coordinates.

The scenario: a sole trader who went independent in August 2026, bought `boilerrepairleeds.co.uk`, and wants to know which pages to build and whether to rename the profile to match the domain.

```
S=../../plugins/local-seo/skills/local-pages/scripts
python $S/town_score.py towns.json > town-scores.md
```

- `local-seo-brief.md`: the brief written while orienting (from the owner's answers to the few questions the site couldn't answer).
- `proof.md`: what the owner supplied (prices, credentials, reviews he can quote, jobs with photos, local facts).
- `towns.json`: candidate towns with job counts and proof, the script's input.
- `town-scores.md`: the script's output.
- `page-plan.md`: the full output: plan table, location decisions, briefs, two written pages and schema.
