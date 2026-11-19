# Example: a fictional skin clinic

Example Skin Clinic, Brixton, does not exist. The data here is made up to show the scripts working.

```
S=../../plugins/local-seo/skills/local-seo-audit/scripts
python $S/grid.py summary grid.json --business "Example Skin Clinic"
python $S/review_velocity.py reviews.json
python $S/nap_check.py listings.json
python $S/prioritise.py findings.json
```

`local-seo-brief.md` is the brief the intake produces. `sample-report.md` is a full audit report written by the skill from this data.
