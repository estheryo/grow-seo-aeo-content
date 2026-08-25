#!/usr/bin/env python3
"""Rank SEO opportunities from a GSC-like CSV without external packages."""

import csv
import sys


CTR_CURVE = {1: 0.28, 2: 0.15, 3: 0.10, 4: 0.07, 5: 0.05,
             6: 0.04, 7: 0.035, 8: 0.03, 9: 0.027, 10: 0.025}


def number(row, key, default=0.0):
    value = row.get(key, "")
    return float(value) if value not in (None, "") else default


def expected_ctr(position):
    position = max(1, min(10, round(position)))
    return CTR_CURVE[position]


def score(row):
    clicks = number(row, "clicks_current")
    previous = number(row, "clicks_previous")
    impressions = number(row, "impressions_current")
    position = number(row, "position_current", 100.0)
    weight = number(row, "conversion_value", 1.0)
    actual_ctr = clicks / impressions if impressions else 0.0

    absolute_loss = max(previous - clicks, 0.0)
    proportional_loss = absolute_loss / previous if previous else 0.0
    recover = absolute_loss if absolute_loss >= 10 and proportional_loss >= 0.20 else 0.0

    benchmark = number(row, "expected_ctr", expected_ctr(position))
    ctr_headroom = impressions * max(benchmark - actual_ctr, 0.0)

    target = number(row, "target_position", 10.0)
    rank_headroom = 0.0
    if 5 <= position <= 20:
        rank_headroom = impressions * max(expected_ctr(target) - actual_ctr, 0.0)

    levers = {"recover": recover, "ctr": ctr_headroom, "rank": rank_headroom}
    primary_lever = max(levers, key=levers.get)
    primary_score = levers[primary_lever] * weight
    return {
        **row,
        "actual_ctr": f"{actual_ctr:.6f}",
        "recover": f"{recover:.2f}",
        "ctr_headroom": f"{ctr_headroom:.2f}",
        "rank_headroom": f"{rank_headroom:.2f}",
        "primary_lever": primary_lever,
        "primary_score": f"{primary_score:.2f}",
    }


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: score_opportunities.py INPUT.csv OUTPUT.csv")
    with open(sys.argv[1], newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        required = {"url", "query", "clicks_current", "clicks_previous",
                    "impressions_current", "position_current"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise SystemExit("missing columns: " + ", ".join(sorted(missing)))
        rows = [score(row) for row in reader]
    rows.sort(key=lambda row: float(row["primary_score"]), reverse=True)
    fields = list(reader.fieldnames or []) + [
        "actual_ctr", "recover", "ctr_headroom", "rank_headroom",
        "primary_lever", "primary_score"
    ]
    with open(sys.argv[2], "w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
