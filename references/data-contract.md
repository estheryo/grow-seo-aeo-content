# Opportunity scoring data contract

Prepare a UTF-8 CSV with one row per page-query pair or aggregated page. Required columns:

| Column | Meaning |
|---|---|
| `url` | Canonical URL |
| `query` | Search query; may be blank for page aggregates |
| `clicks_current` | Clicks in the current 28-day window |
| `clicks_previous` | Clicks in the preceding 28-day window |
| `impressions_current` | Current-window impressions |
| `position_current` | Current average position |

Optional columns:

| Column | Meaning |
|---|---|
| `expected_ctr` | Site-specific CTR benchmark as a decimal; preferred |
| `target_position` | Expected attainable position; defaults to 10 for page-two rows |
| `conversion_value` | Relative business weight; defaults to 1 |

The scorer calculates:

- `recover = max(clicks_previous - clicks_current, 0)` only when the loss is at least 10 clicks and 20%.
- `ctr_headroom = impressions_current * max(expected_ctr - actual_ctr, 0)`.
- `rank_headroom = impressions_current * max(expected_ctr(target_position) - actual_ctr, 0)` for positions 5–20.
- `primary_score = max(recover, ctr_headroom, rank_headroom) * conversion_value`.

Default CTR values are deliberately conservative heuristics. Replace them with the site's own non-branded curve whenever possible. Scores prioritize review; they are not forecasts.

Run:

```bash
python3 scripts/score_opportunities.py input.csv output.csv
```
