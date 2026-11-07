#!/usr/bin/env python3
"""Summarize the measured CSVs without combining unlike sorting interfaces."""
import csv
import json
from pathlib import Path


def summarize(path):
    conditions = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            key = (row["family"], int(row["n"]))
            conditions.setdefault(key, {})[row["algorithm"]] = row
    out = []
    for (family, n), rows in conditions.items():
        eligible = {name: row for name, row in rows.items()
                    if row.get("median_us", "") not in ("", "NA", "nan")}
        brc = [name for name in eligible if name.startswith("brc")]
        baselines = [name for name in eligible if not name.startswith("brc")]
        if not brc or not baselines:
            continue
        best_brc = min(brc, key=lambda name: float(eligible[name]["median_us"]))
        best_baseline = min(baselines, key=lambda name: float(eligible[name]["median_us"]))
        btime = float(eligible[best_brc]["median_us"])
        ctime = float(eligible[best_baseline]["median_us"])
        out.append({
            "family": family,
            "n": n,
            "best_measured_brc": best_brc,
            "best_measured_baseline": best_baseline,
            "best_brc_us": btime,
            "best_baseline_us": ctime,
            "baseline_over_brc": ctime / btime,
            "median_us": {name: float(row["median_us"]) for name, row in eligible.items()},
            "raw_rows": rows,
        })
    return out


def main():
    root = Path(__file__).resolve().parent
    result = {}
    for interface in ("record", "pure"):
        path = root / f"{interface}_results.csv"
        if path.exists():
            result[interface] = summarize(path)
    (root / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    for interface, conditions in result.items():
        print(f"{interface}: {len(conditions)} conditions")
        for item in conditions:
            print(f"{item['family']:28s} n={item['n']:7d} "
                  f"BRC={item['best_brc_us']:10.3f} us "
                  f"baseline={item['best_baseline_us']:10.3f} us "
                  f"ratio={item['baseline_over_brc']:.3f} "
                  f"({item['best_measured_baseline']})")


if __name__ == "__main__":
    main()
