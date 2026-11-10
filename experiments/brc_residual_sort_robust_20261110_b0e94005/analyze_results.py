#!/usr/bin/env python3
"""Analyze the fixed benchmark matrix without selecting or tuning a new policy."""
import argparse
import csv
from collections import Counter, defaultdict
import json
import math
from pathlib import Path
import statistics


ROBUST = ("robust_dense_1024", "robust_trim_1024", "robust_combined_1024", "robust_compact_1024")
PREVIOUS = "sampled_recursive_1024"
ORDINARY = ("std_sort", "offset_radix", "range_count_or_radix", "frequency_sort",
            "affine_range_local", "affine_square_local", "flat_frequency", "full_shift_local",
            "pdqsort")
DIAGNOSTICS = {
    "p10_us", "p90_us", "path_mix", "terminal_path_mix", "sample_count", "learning_visits",
    "processed", "covered", "spills", "full_data_visits", "counter_cells_demanded",
    "counter_cells_allocated", "spill_vector_bytes", "recursive_nodes", "recursive_max_depth",
    "recursive_input_total", "recursive_processed_total", "recursive_counter_cells_total",
    "recursive_emitted_total", "recursive_merge_writes_total", "recursive_radix_leaves",
    "dense_probes", "dense_accepts", "dense_probe_visits_total", "trim_attempts",
    "trim_layout_accepts", "compact_attempts", "compact_accepts", "compact_trim_accepts",
    "compact_counter_cells_total",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--prefix", default="analysis")
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()
    root = args.csv.resolve().parent
    rows = list(csv.DictReader(args.csv.open()))
    grouped = defaultdict(dict)
    for row in rows:
        key = (row["stage"], row["original_stage"], row["family"], int(row["n"]))
        if row["algorithm"] in grouped[key]:
            raise ValueError(f"Duplicate condition/candidate: {key}/{row['algorithm']}")
        grouped[key][row["algorithm"]] = row
    all_names = {r["algorithm"] for r in rows}
    if len(all_names) != 20 or set(ROBUST + ORDINARY + (PREVIOUS,)) - all_names:
        raise ValueError(f"Unexpected candidate set: {sorted(all_names)}")
    controls = sorted(all_names - set(ROBUST))
    results = []
    stage_data = defaultdict(lambda: defaultdict(list))
    for key, algorithms in grouped.items():
        if set(algorithms) != all_names:
            raise ValueError(f"Missing candidates in {key}")
        if {int(r["banks"]) for r in algorithms.values()} != {8} or \
           {int(r["rounds"]) for r in algorithms.values()} != {7}:
            raise ValueError("Expected exactly eight banks and seven rounds")
        times = {a: float(r["median_us"]) for a, r in algorithms.items()}
        if not all(math.isfinite(x) and x > 0 for x in times.values()):
            raise ValueError("Nonpositive/nonfinite timing")
        ordinary = min(ORDINARY, key=times.get)
        control = min(controls, key=times.get)
        condition = dict(stage=key[0], original_stage=key[1], family=key[2], n=key[3],
                         best_ordinary=ordinary, best_ordinary_us=times[ordinary],
                         best_control=control, best_control_us=times[control],
                         median_us=times, speedup_vs_best_ordinary={},
                         speedup_vs_best_control={}, speedup_vs_previous_recursive={}, diagnostics={})
        labels = [key[0]]
        if key[0] in ("regression", "heldout"):
            labels.append("evaluation_all_including_old_mechanisms")
            if key[1] != "mechanism":
                labels.append("evaluation_excluding_old_mechanisms")
        if key[0] == "regression" and key[1] == "mechanism":
            labels.append("old_mechanisms_regression")
        elif key[0] == "regression":
            labels.append("regression_excluding_old_mechanisms")
        for candidate in ROBUST:
            ratios = {
                "ordinary": times[ordinary] / times[candidate],
                "control": times[control] / times[candidate],
                "previous": times[PREVIOUS] / times[candidate],
            }
            condition["speedup_vs_best_ordinary"][candidate] = ratios["ordinary"]
            condition["speedup_vs_best_control"][candidate] = ratios["control"]
            condition["speedup_vs_previous_recursive"][candidate] = ratios["previous"]
            condition["diagnostics"][candidate] = {k: v for k, v in algorithms[candidate].items()
                if k in DIAGNOSTICS}
            for label in labels:
                stage_data[label][candidate].append(ratios)
        results.append(condition)
    stages = {}
    for stage, candidates in stage_data.items():
        stages[stage] = {}
        for name, measured in candidates.items():
            item = {"conditions": len(measured)}
            for reference in ("ordinary", "control", "previous"):
                values = [r[reference] for r in measured]
                item[reference] = {
                    "median_wins": sum(x > 1 for x in values),
                    "at_least_10pct_speedup": sum(x >= 1.1 for x in values),
                    "at_least_10pct_slower": sum(x <= 1 / 1.1 for x in values),
                    "median_ratio": statistics.median(values),
                    "geometric_mean_ratio": math.exp(statistics.mean(map(math.log, values))),
                    "minimum_ratio": min(values), "maximum_ratio": max(values),
                }
            stages[stage][name] = item
    trace_path = Path(str(args.csv) + ".robust_nodes.csv")
    trace_rows = list(csv.DictReader(trace_path.open()))
    roots = [r for r in trace_rows if int(r["depth"]) == 0]
    trace_summary = {}
    for name in (PREVIOUS,) + ROBUST:
        own = [r for r in trace_rows if r["algorithm"] == name]
        own_roots = [r for r in roots if r["algorithm"] == name]
        trace_summary[name] = dict(nodes=len(own), root_banks=len(own_roots),
                                  node_paths=dict(Counter(r["path"] for r in own)),
                                  root_paths=dict(Counter(r["path"] for r in own_roots)),
                                  max_depth=max((int(r["depth"]) for r in own), default=0))
    summary = {
        "input_csv": args.csv.name, "rows": len(rows), "conditions": len(grouped),
        "algorithms": sorted(all_names), "robust_candidates": ROBUST,
        "ordinary_baselines": ORDINARY, "all_controls": controls,
        "comparison_rule": "The ordinary reference is the per-condition minimum of nine declared ordinary medians. The stronger control reference is the minimum of all fifteen preceding candidates plus pdqsort. These are retrospective comparison references, not implemented selectors.",
        "uncertainty": "Seven within-process randomized rounds over eight fixed input banks. p10/p90 are empirical quantiles, not confidence intervals. A 10% margin is descriptive, not a significance test. Median wins among shared small-array fallbacks do not identify a distinct algorithmic improvement.",
        "stage_policy": "Fourteen newly frozen input-bank conditions are heldout. All thirty-nine prior conditions are calibration or regression; the five old deterministic mechanism conditions retain original_stage=mechanism and are also summarized separately.",
        "stage_summary": stages, "trace_summary": trace_summary, "condition_results": results,
    }
    (root / f"{args.prefix}_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = ["# Measured robust residual sorting results", "",
             "Microseconds per complete sort, including input copy, model construction, allocation, output and destruction.",
             "The strongest control is the fastest median among all 15 preceding candidates plus official pdqsort; it is a retrospective reference, not an executable selector.", "",
             "| Stage / origin | Condition | n | Strongest control | Control µs | Previous recursive µs | Dense µs | Trim µs | Combined µs | Compact µs | Compact/control speedup |",
             "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for c in results:
        t = c["median_us"]
        values = " | ".join(f"{t[a]:.3f}" for a in (PREVIOUS,) + ROBUST)
        lines.append(f"| {c['stage']} / {c['original_stage']} | {c['family']} | {c['n']:,} | "
                     f"{c['best_control']} | {c['best_control_us']:.3f} | {values} | "
                     f"{c['speedup_vs_best_control'][ROBUST[-1]]:.3f}× |")
    (root / f"{args.prefix}_table.md").write_text("\n".join(lines) + "\n")
    if not args.no_plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
        heldout = [c for c in results if c["stage"] == "heldout"]
        if heldout:
            fig, ax = plt.subplots(figsize=(12, 8))
            y = np.arange(len(heldout))
            names = (PREVIOUS, ROBUST[2], ROBUST[3])
            labels = ("Previous recursive", "Dense gate + global trim", "Compact interval + global trim")
            for offset, name, label, color in zip((-.2, 0, .2), names, labels,
                                                 ("#8c98a7", "#c27430", "#176b87")):
                ratios = [c["best_control_us"] / c["median_us"][name] for c in heldout]
                ax.scatter(ratios, y + offset, s=35, color=color, label=label, zorder=3)
            ax.axvline(1, color="#303640", lw=1)
            ax.set_xscale("log", base=2)
            ax.set_yticks(y, [f"{c['family']}  (n={c['n']:,})" for c in heldout], fontsize=9)
            ax.invert_yaxis()
            ax.grid(axis="x", alpha=.2)
            ax.set_xlabel("Speedup = fastest control median / candidate median; above 1 is faster")
            ax.set_title("Fresh held-out input banks, fixed policies\n"
                         "16 control implementations · 8 banks · 7 randomized rounds · full uint64 output")
            ax.legend(loc="upper center", bbox_to_anchor=(.5, -.09), ncol=1, frameon=False)
            fig.tight_layout()
            for ext in ("png", "svg"):
                fig.savefig(root / f"{args.prefix}_heldout_speedup.{ext}", dpi=160, bbox_inches="tight")
            plt.close(fig)
    print(json.dumps({"rows": len(rows), "conditions": len(grouped), "stages": stages,
                      "trace_summary": trace_summary}, indent=2))


if __name__ == "__main__":
    main()
