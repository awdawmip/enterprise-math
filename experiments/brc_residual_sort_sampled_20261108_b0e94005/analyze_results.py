#!/usr/bin/env python3
"""Summarize the frozen benchmark without choosing a new algorithm policy."""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

ORDINARY = (
    "std_sort", "offset_radix", "range_count_or_radix", "frequency_sort",
    "affine_range_local", "affine_square_local", "flat_frequency", "full_shift_local",
)
NEW = ("sampled_shift_1024", "sampled_shift_4096", "sampled_recursive_1024")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=Path)
    args = parser.parse_args()
    root = args.csv.resolve().parent
    rows = list(csv.DictReader(args.csv.open()))
    groups = defaultdict(dict)
    for row in rows:
        key = (row["stage"], row["family"], int(row["n"]))
        if row["algorithm"] in groups[key]:
            raise ValueError(f"Duplicate algorithm/condition: {key}/{row['algorithm']}")
        groups[key][row["algorithm"]] = row
    conditions = []
    stage_stats = defaultdict(lambda: {a: {"conditions": 0, "median_wins": 0,
                                           "at_least_10pct_speedup": 0,
                                           "speedup_ratios": []} for a in NEW})
    for key, algorithms in groups.items():
        if set(ORDINARY + NEW) - algorithms.keys():
            raise ValueError(f"Missing candidates at {key}")
        best = min(ORDINARY, key=lambda name: float(algorithms[name]["median_us"]))
        ordinary_time = float(algorithms[best]["median_us"])
        entry = dict(stage=key[0], family=key[1], n=key[2],
                     best_ordinary=best, best_ordinary_us=ordinary_time,
                     median_us={a: float(r["median_us"]) for a, r in algorithms.items()},
                     speedup_vs_best_ordinary={}, diagnostics={})
        for name in NEW:
            r = algorithms[name]
            ratio = ordinary_time / float(r["median_us"])
            entry["speedup_vs_best_ordinary"][name] = ratio
            entry["diagnostics"][name] = {k: v for k, v in r.items()
                if k not in {"stage", "family", "n", "algorithm", "seed_regime"}}
            labels = [key[0]]
            if key[0] in ("regression", "heldout"):
                labels.append("evaluation")
            for label in labels:
                item = stage_stats[label][name]
                item["conditions"] += 1
                item["median_wins"] += ratio > 1
                item["at_least_10pct_speedup"] += ratio >= 1.1
                item["speedup_ratios"].append(ratio)
        conditions.append(entry)
    summary = {
        "input_csv": args.csv.name, "rows": len(rows), "conditions": len(groups),
        "algorithms": sorted({r["algorithm"] for r in rows}),
        "ordinary_baselines": ORDINARY, "fixed_sampled_candidates": NEW,
        "comparison_rule": "Per-condition minimum of 8 ordinary medians; a conservative retrospective reference, not an implemented selector.",
        "uncertainty": "Seven within-process randomized rounds; p10/p90 are empirical quantiles, not confidence intervals. A 10% margin is descriptive, not a significance test.",
        "stage_summary": dict(stage_stats), "condition_results": conditions,
    }
    (root / "analysis_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = ["# Frozen benchmark results", "",
             "Times are microseconds per full sort, including copy, setup, allocation, output and destruction.",
             "The ordinary reference is the fastest measured median among the eight declared ordinary candidates for each condition. It is not a deployable selector.", "",
             "| Stage | Condition | n | Best ordinary | Ordinary µs | S1024 µs | S4096 µs | Recursive1024 µs | Recursive speedup |",
             "|---|---|---:|---|---:|---:|---:|---:|---:|"]
    for c in conditions:
        t = c["median_us"]
        lines.append(f"| {c['stage']} | {c['family']} | {c['n']:,} | {c['best_ordinary']} | {c['best_ordinary_us']:.3f} | {t[NEW[0]]:.3f} | {t[NEW[1]]:.3f} | {t[NEW[2]]:.3f} | {c['speedup_vs_best_ordinary'][NEW[2]]:.3f}× |")
    (root / "results_table.md").write_text("\n".join(lines) + "\n")
    # A standalone plot, built exclusively from the measured table.
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    evaluation = [c for c in conditions if c['stage'] in ('regression', 'heldout')]
    fig, ax = plt.subplots(figsize=(13, max(6, .33 * len(evaluation) + 1.6)))
    y = np.arange(len(evaluation))
    colors = ('#8a96a6', '#268c7e', '#8b4b9b')
    for offset, name, color in zip((-.19, 0, .19), NEW, colors):
        ax.scatter([c['speedup_vs_best_ordinary'][name] for c in evaluation],
                   y + offset, s=30, label=name, color=color, zorder=3)
    ax.axvline(1, color='#444444', linewidth=1.2)
    ax.set_xscale('log', base=2)
    ax.set_yticks(y, [f"{c['family']}  (n={c['n']:,})" for c in evaluation], fontsize=9)
    ax.invert_yaxis()
    ax.grid(axis='x', alpha=.2)
    ax.set_xlabel('Speedup = best ordinary median / candidate median; greater than 1 is faster')
    ax.set_title('Frozen regression and held-out evaluation\n8 input banks · 7 randomized rounds · complete uint64 output')
    ax.legend(loc='upper center', bbox_to_anchor=(.5, -.075), ncol=3, frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(root / 'evaluation_speedup.svg', bbox_inches='tight')
    fig.savefig(root / 'evaluation_speedup.png', dpi=150, bbox_inches='tight')
    print(json.dumps({"rows": len(rows), "conditions": len(conditions),
                      "stages": {k: {a: {x: y for x, y in v.items() if x != 'speedup_ratios'}
                                      for a, v in d.items()} for k, d in stage_stats.items()}}, indent=2))


if __name__ == '__main__':
    main()
