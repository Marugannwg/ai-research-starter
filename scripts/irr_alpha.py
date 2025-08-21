# Compute Krippendorff's alpha (nominal) for pilot labels.
# Input: data/pilot_labels.csv with columns: unit, rater, label
# Example rows:
# unit,rater,label
# 1,human1,POS
# 1,human2,NEG
# 1,llm,POS
#
# Usage: python scripts/irr_alpha.py

import csv
from pathlib import Path
from collections import defaultdict, Counter
import math

INPUT = Path("data/pilot_labels.csv")

def krippendorff_alpha_nominal(data):
    """
    data: list of lists, rows are units, columns are raters' labels (strings or None)
    Missing values should be None.
    Implementation adapted from Krippendorff (2004) nominal metric.
    """
    values = set(v for row in data for v in row if v is not None)
    if not values:
        return float("nan")

    coincidence = {v: {w: 0 for w in values} for v in values}
    for row in data:
        vals = [v for v in row if v is not None]
        n = len(vals)
        if n < 2:
            continue
        counts = Counter(vals)
        for v in values:
            for w in values:
                if v == w:
                    coincidence[v][w] += counts[v] * (counts[w] - 1)
                else:
                    coincidence[v][w] += counts[v] * counts[w]

    n_tot = sum(coincidence[v][w] for v in values for w in values)
    if n_tot == 0:
        return float("nan")

    Do = sum(coincidence[v][w] for v in values for w in values if v != w)
    Do /= (n_tot - sum(coincidence[v][v] for v in values))

    marginals = {v: sum(coincidence[v][w] for w in values) for v in values}
    De = sum(marginals[v] * marginals[w] for v in values for w in values if v != w)
    De /= (n_tot * (n_tot - 1))

    if De == 0:
        return 1.0
    return 1.0 - Do / De

def load_pilot(path: Path):
    by_unit = defaultdict(dict)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            unit = row["unit"]
            rater = row["rater"]
            label = row["label"].strip() if row["label"].strip() else None
            by_unit[unit][rater] = label
    raters = sorted({r for d in by_unit.values() for r in d.keys()})
    data = []
    def _key(u):
        try:
            return (0, int(u))
        except ValueError:
            return (1, str(u))
    for unit in sorted(by_unit.keys(), key=_key):
        row = [by_unit[unit].get(r, None) for r in raters]
        data.append(row)
    return data, raters

def main():
    data, raters = load_pilot(INPUT)
    alpha = krippendorff_alpha_nominal(data)
    print(f"Raters: {raters}")
    print(f"Units: {len(data)}")
    if isinstance(alpha, float) and not math.isnan(alpha):
        print(f"Krippendorff's alpha (nominal): {alpha:.3f}")
        if alpha >= 0.80:
            print("Reliability: STRONG (>= 0.80)")
        elif alpha >= 0.667:
            print("Reliability: TENTATIVE (>= 0.667 and < 0.80)")
        else:
            print("Reliability: INSUFFICIENT (< 0.667)")
    else:
        print("Alpha could not be computed (insufficient data).")

if __name__ == "__main__":
    main()
