# Examples: local ranking recovery

Both businesses are fictional. The names, addresses, figures and events are made up to show the skill and its script working. Neither business exists.

| Folder | The case | What the skill found |
|---|---|---|
| `category-change/` | Calder Heating & Plumbing, Leeds. Calls fell by about 40% in August. | A primary category change from "Plumber" to "Heating contractor", five days before the drop. Local only; organic held. |
| `suspension/` | Larchmont Dental Studio, Croydon. Gone from Google Maps in September. | A hard suspension, most likely for a keyword-stuffed name added by a previous agency in March. An hours edit two days before probably prompted the review. A duplicate profile made afterwards needs removing before the appeal. |

Each folder has:

- `local-seo-brief.md`: the brief the skill wrote while orienting (from what it found, plus the user's answers to what was missing).
- `recovery.json`: the series and events (the script's input).
- `change-points.md`: the script's output.
- `recovery-report.md`: the report the skill wrote from it.

The sectors here (a plumbing and heating firm, a dental practice) are illustration only. The skill itself carries no sector rules: it reads each business through the lens in `references/loop.md`, which is why the first case leans on the category signature and the second on what a regulated practice can show as evidence.

Run the script yourself:

```
S=../../plugins/local-seo/skills/local-ranking-recovery/scripts
python $S/change_points.py category-change/recovery.json
python $S/change_points.py suspension/recovery.json
```
