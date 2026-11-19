# Example: a fictional heating engineer

Sector detail here is illustration only; the skill itself works from the lens in `references/loop.md`.

Example Heating Co, Walthamstow, does not exist. Nor do its competitors. The data here is made up to show the skill and its scripts working.

```
S=../../plugins/local-seo/skills/gbp-optimisation/scripts
python $S/category_gap.py compare.json        # output saved as category-gap-output.md
python $S/change_log.py changes.json --start 2026-11-23   # output saved as change-log-output.md
```

- `local-seo-brief.md`: the brief the skill wrote while orienting (from the site, the profile screenshots and two questions it couldn't answer itself: the signage name and profile access).
- `compare.json`: the business's categories and services against the three businesses beating it.
- `changes.json`: every change, with the exact text, as the skill recorded them.
- `sample-output.md`: the full output the skill wrote from this data.
