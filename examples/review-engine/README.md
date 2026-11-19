# Example: a fictional physiotherapy clinic

Example Physiotherapy, Didsbury, does not exist. Nor do its competitors or any reviewer. The data here is made up to show the skill and its scripts working.

```
S=../../plugins/local-seo/skills/review-engine/scripts
python $S/review_velocity.py reviews.json                                  # saved as velocity-output.md
python $S/review_tracker.py reviews-log.json --months 6 --regulated        # saved as tracker-output.md
```

- `local-seo-brief.md`: the brief the intake produced.
- `reviews.json`: review counts and recent dates for the clinic and three competitors.
- `reviews-log.json`: the clinic's own reviews for six months, with text and replies.
- `sample-output.md`: the full output the skill wrote from this data.
