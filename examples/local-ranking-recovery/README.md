# Examples: local ranking recovery

Both businesses are fictional. The names, addresses, figures and events are made up to show the skill and its script working. Neither business exists.

| Folder | The case | What the skill found |
|---|---|---|
| `category-change/` | Calder Heating & Plumbing, Leeds. Calls fell by about 40% in August. | A primary category change from "Plumber" to "Heating contractor", five days before the drop. Local only; organic held. |
| `suspension/` | Larchmont Dental Studio, Croydon. Gone from Google Maps in September. | A hard suspension, most likely for a keyword-stuffed name added by a previous agency in March. An hours edit two days before probably prompted the review. A duplicate profile made afterwards needs removing before the appeal. |

Each folder has:

- `local-seo-brief.md`: the brief the intake produces.
- `recovery.json`: the series and events (the script's input).
- `change-points.md`: the script's output.
- `recovery-report.md`: the report the skill wrote from it.

Run the script yourself:

```
S=../../plugins/local-seo/skills/local-ranking-recovery/scripts
python $S/change_points.py category-change/recovery.json
python $S/change_points.py suspension/recovery.json
```
