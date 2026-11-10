#!/usr/bin/env python3
"""Summarize the fixed certified selector against all26 same-run controls."""
import argparse
from collections import Counter, defaultdict
import csv
import json
import math
from pathlib import Path
import statistics

NEW = "certified_combined_1024"
PREVIOUS = "selection_combined_1024"


def ratios_summary(values):
    return dict(conditions=len(values), median_wins=sum(x > 1 for x in values),
                at_least_10pct_speedup=sum(x >= 1.1 for x in values),
                at_least_10pct_slower=sum(x <= 1 / 1.1 for x in values),
                median_ratio=statistics.median(values),
                geometric_mean_ratio=math.exp(statistics.mean(map(math.log, values))),
                minimum_ratio=min(values), maximum_ratio=max(values))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv", type=Path)
    p.add_argument("--prefix", default="analysis")
    p.add_argument("--no-plot", action="store_true")
    args = p.parse_args()
    root = args.csv.resolve().parent
    rows = list(csv.DictReader(args.csv.open()))
    names = {r["algorithm"] for r in rows}
    if len(names) != 27 or {NEW, PREVIOUS, "pdqsort"} - names:
        raise ValueError(f"Unexpected candidate set: {sorted(names)}")
    controls = sorted(names - {NEW})
    groups = defaultdict(dict)
    for r in rows:
        key = (r["stage"], r["family"], int(r["n"]))
        if r["algorithm"] in groups[key]:
            raise ValueError(f"Duplicate row: {key}")
        groups[key][r["algorithm"]] = r
    conditions = []
    ratios = defaultdict(lambda: defaultdict(list))
    for key, algorithms in groups.items():
        if set(algorithms) != names:
            raise ValueError(f"Missing candidate: {key}")
        if {int(r["banks"]) for r in algorithms.values()} != {8} or \
                {int(r["rounds"]) for r in algorithms.values()} != {7}:
            raise ValueError("Expected8banks and7rounds")
        times = {name: float(r["median_us"]) for name, r in algorithms.items()}
        if not all(math.isfinite(x) and x > 0 for x in times.values()):
            raise ValueError("Nonpositive or nonfinite timing")
        best = min(controls, key=times.get)
        record = dict(stage=key[0], family=key[1], n=key[2], median_us=times,
                      best_control=best, best_control_us=times[best],
                      speedup_vs_best_control=times[best] / times[NEW],
                      speedup_vs_previous=times[PREVIOUS] / times[NEW],
                      diagnostics={name: {k: v for k, v in algorithms[name].items()
                            if k not in {"stage", "family", "algorithm", "n"}
                            and not k.startswith("round")}
                                   for name in (PREVIOUS, NEW)})
        conditions.append(record)
        ratios[key[0]]["best_control"].append(record["speedup_vs_best_control"])
        ratios[key[0]]["previous"].append(record["speedup_vs_previous"])
    stages = {stage: {ref: ratios_summary(values) for ref, values in refs.items()}
              for stage, refs in ratios.items()}
    nodes = list(csv.DictReader(Path(str(args.csv) + ".certified_nodes.csv").open()))
    attempts = list(csv.DictReader(Path(str(args.csv) + ".certified_attempts.csv").open()))
    own = [r for r in nodes if r["algorithm"] == NEW]
    roots = [r for r in own if int(r["depth"]) == 0]
    trials = [r for r in attempts if r["algorithm"] == NEW]
    trace = dict(nodes=len(own), root_banks=len(roots), attempts=len(trials),
                 root_paths=dict(Counter(r["path"] for r in roots)),
                 node_paths=dict(Counter(r["path"] for r in own)))
    if trials and "method" in trials[0]:
        trace["repair_method_counts"] = dict(Counter(r["method"] for r in trials))
    summary = dict(
        input_csv=args.csv.name, rows=len(rows), conditions=len(groups),
        algorithms=sorted(names), new_candidate=NEW, controls=controls,
        comparison_rule="Compare the fixed new candidate with the previous combined selector and the fastest median of all26 frozen preceding candidates in this same binary/run. The per-condition fastest reference is retrospective, not an implemented selector.",
        stage_policy="Ten exact phase-three conditions are known calibration, including its density witness. Six fresh targeted seed-bank conditions are frozen before generation and use natural samples of shuffled populations. Four prescribed-sample mechanisms are separate. This is a targeted family study, not a deployment-population estimate.",
        uncertainty="Eight fixed banks and seven randomized-order within-process rounds. Quantiles and10% margins are descriptive, not confidence intervals or significance tests. Conditions have equal weight in geometric means regardless of n or real-world prevalence.",
        stage_summary=stages, trace_summary=trace, condition_results=conditions)
    (root / f"{args.prefix}_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = ["# Certified whole-bin selection: full measured table", "",
             "Microseconds per complete sort, including copy, setup, allocations, selection, full output and destruction.",
             "All26 preceding candidates are measured in the same binary. Speedup is control/candidate.", "",
             "| Stage | Condition | n | Best control | Best µs | Previous combined µs | Certified µs | Previous/certified | Best/certified |",
             "|---|---|---:|---|---:|---:|---:|---:|---:|"]
    for c in conditions:
        t = c["median_us"]
        lines.append(f"| {c['stage']} | {c['family']} | {c['n']:,} | {c['best_control']} | "
                     f"{c['best_control_us']:.3f} | {t[PREVIOUS]:.3f} | {t[NEW]:.3f} | "
                     f"{c['speedup_vs_previous']:.3f}× | {c['speedup_vs_best_control']:.3f}× |")
    (root / f"{args.prefix}_table.md").write_text("\n".join(lines) + "\n")
    heldout = [c for c in conditions if c["stage"] == "heldout"]
    if heldout and not args.no_plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize=(11, 6))
        y = np.arange(len(heldout))
        for offset, candidate, label, color in [
                (-.10, PREVIOUS, "Previous density + gap + fused", "#8e99a5"),
                (.10, NEW, "Certified half-mass repair", "#146b75")]:
            ax.scatter([c["best_control_us"] / c["median_us"][candidate] for c in heldout],
                       y + offset, s=44, label=label, color=color, zorder=3)
        ax.axvline(1, color="#303640", lw=1)
        ax.set_xscale("log", base=2)
        ax.set_yticks(y, [f"{c['family']}  (n={c['n']:,})" for c in heldout], fontsize=8.5)
        ax.invert_yaxis()
        ax.grid(axis="x", alpha=.2)
        ax.set_xlabel("Speedup = fastest prior-control median / candidate median")
        ax.set_title("Fixed-grid exact repair: fresh natural samples\n"
                     "26 controls · fixed policy · 8 banks · 7 rounds · complete uint64 output")
        ax.legend(loc="upper center", bbox_to_anchor=(.5, -.12), frameon=False)
        fig.tight_layout()
        for ext in ("png", "svg"):
            fig.savefig(root / f"{args.prefix}_heldout_speedup.{ext}", dpi=160, bbox_inches="tight")
        plt.close(fig)
    print(json.dumps({"rows": len(rows), "conditions": len(groups),
                      "stages": stages, "trace_summary": trace}, indent=2))


if __name__ == "__main__":
    main()
