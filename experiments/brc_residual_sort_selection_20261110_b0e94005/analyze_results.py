#!/usr/bin/env python3
"""Summarize selection/output policies, fixed-control comparisons and retained losses."""
import argparse
import csv
from collections import Counter, defaultdict
import json
import math
from pathlib import Path
import statistics

NEW = ("selection_fused_1024", "selection_density_gap_1024", "selection_combined_1024")
PREVIOUS = "adaptive_combined_1024"
DIAGNOSTICS = {
    "p10_us", "p90_us", "path_mix", "terminal_path_mix", "sample_count", "learning_visits",
    "processed", "covered", "spills", "counter_cells_demanded", "counter_cells_allocated",
    "recursive_nodes", "recursive_max_depth", "recursive_input_total", "recursive_processed_total",
    "recursive_counter_cells_total", "recursive_emitted_total", "recursive_merge_writes_total",
    "recursive_radix_leaves", "trim_attempts", "compact_accepts", "compact_trim_accepts",
    "ladder_attempts", "prune_attempts", "prune_accepts", "prune_mass_rejects",
    "actual_spill_failures", "selected_omitted_bins_total", "selected_omitted_samples_total",
    "selected_omitted_cells_total", "prune_order_entries_total", "prune_order_vector_bytes_peak",
}


def ratio_summary(values):
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
    groups = defaultdict(dict)
    for row in rows:
        key = (row["stage"], row["family"], int(row["n"]))
        if row["algorithm"] in groups[key]:
            raise ValueError(f"Duplicate candidate row at {key}")
        groups[key][row["algorithm"]] = row
    names = {r["algorithm"] for r in rows}
    if len(names) != 26 or set(NEW + (PREVIOUS, "pdqsort")) - names:
        raise ValueError(f"Unexpected candidate set: {sorted(names)}")
    controls = sorted(names - set(NEW))
    conditions = []
    ratios = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for key, algorithms in groups.items():
        if set(algorithms) != names:
            raise ValueError(f"Missing candidates at {key}")
        if {int(r["banks"]) for r in algorithms.values()} != {8} or \
           {int(r["rounds"]) for r in algorithms.values()} != {7}:
            raise ValueError("Expected eight banks and seven rounds")
        times = {a: float(r["median_us"]) for a, r in algorithms.items()}
        if not all(math.isfinite(v) and v > 0 for v in times.values()):
            raise ValueError("Nonpositive or nonfinite timing")
        best = min(controls, key=times.get)
        c = dict(stage=key[0], family=key[1], n=key[2], best_control=best,
                 best_control_us=times[best], median_us=times,
                 speedup_vs_best_control={}, speedup_vs_previous_adaptive={}, diagnostics={})
        for candidate in NEW:
            control_ratio = times[best] / times[candidate]
            previous_ratio = times[PREVIOUS] / times[candidate]
            c["speedup_vs_best_control"][candidate] = control_ratio
            c["speedup_vs_previous_adaptive"][candidate] = previous_ratio
            c["diagnostics"][candidate] = {k: v for k, v in algorithms[candidate].items()
                                           if k in DIAGNOSTICS or any(tag in k for tag in ("density", "gap", "output_writes", "boundary_search", "selected_sample"))}
            ratios[key[0]][candidate]["control"].append(control_ratio)
            ratios[key[0]][candidate]["previous"].append(previous_ratio)
        conditions.append(c)
    stages = {stage: {name: {ref: ratio_summary(v) for ref, v in refs.items()}
                      for name, refs in candidates.items()}
              for stage, candidates in ratios.items()}
    nodes = list(csv.DictReader(Path(str(args.csv) + ".selection_nodes.csv").open()))
    attempts = list(csv.DictReader(Path(str(args.csv) + ".selection_attempts.csv").open()))
    traces = {}
    for name in NEW:
        own = [r for r in nodes if r["algorithm"] == name]
        roots = [r for r in own if int(r["depth"]) == 0]
        trials = [r for r in attempts if r["algorithm"] == name]
        traces[name] = dict(nodes=len(own), root_banks=len(roots), attempts=len(trials),
                            root_paths=dict(Counter(r["path"] for r in roots)),
                            node_paths=dict(Counter(r["path"] for r in own)))
    summary = {
        "input_csv": args.csv.name, "rows": len(rows), "conditions": len(groups),
        "algorithms": sorted(names), "new_candidates": NEW, "controls": controls,
        "comparison_rule": "For each condition, compare each fixed new candidate with the fastest median among all twenty-three frozen prior candidates (including pdqsort). This is a retrospective reference, not an implemented selector. Also report comparison with the previous adaptive combined candidate measured in the same run.",
        "stage_policy": "Eight exact phase-two input-bank conditions are known calibration. Twelve fresh targeted seed-bank conditions were chosen after phase-two feedback. High/low mirror pairs share seeds and are related evaluations. Four deterministic mechanisms are separate. This is a targeted family study, not an unbiased workload population.",
        "uncertainty": "Eight fixed banks, seven within-process randomized-order rounds. Quantiles and a10% margin are descriptive, not confidence intervals or significance tests. Per-condition geometric means weight conditions equally, not by array size or deployment prevalence.",
        "stage_summary": stages, "trace_summary": traces, "condition_results": conditions,
    }
    (root / f"{args.prefix}_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = ["# Residual sorting selection and fused output: full measured table", "",
             "Microseconds per complete sort, including copy, setup, allocation, full output and destruction.",
             "The reference is the fastest median among all twenty-three frozen controls measured in this same run.", "",
             "| Stage | Condition | n | Best control | Control µs | Previous adaptive µs | Fused-only µs | Selection-only µs | Combined µs | Combined/control speedup |",
             "|---|---|---:|---|---:|---:|---:|---:|---:|---:|"]
    for c in conditions:
        t = c["median_us"]
        values = " | ".join(f"{t[a]:.3f}" for a in (PREVIOUS,) + NEW)
        lines.append(f"| {c['stage']} | {c['family']} | {c['n']:,} | {c['best_control']} | "
                     f"{c['best_control_us']:.3f} | {values} | "
                     f"{c['speedup_vs_best_control'][NEW[-1]]:.3f}× |")
    (root / f"{args.prefix}_table.md").write_text("\n".join(lines) + "\n")
    heldout = [c for c in conditions if c["stage"] == "heldout"]
    if heldout and not args.no_plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize=(12, 8))
        y = np.arange(len(heldout))
        candidates = (PREVIOUS,) + NEW
        labels = ("Previous adaptive", "Fused output only", "Density + gap selection", "Selection + fused output")
        for offset, candidate, label, color in zip((-.24, -.08, .08, .24), candidates, labels,
                ("#96a1ad", "#a97028", "#6f56a5", "#146b75")):
            ax.scatter([c["best_control_us"] / c["median_us"][candidate] for c in heldout],
                       y + offset, s=32, label=label, color=color, zorder=3)
        ax.axvline(1, color="#303640", lw=1)
        ax.set_xscale("log", base=2)
        ax.set_yticks(y, [f"{c['family']}  (n={c['n']:,})" for c in heldout], fontsize=8.5)
        ax.invert_yaxis()
        ax.grid(axis="x", alpha=.2)
        ax.set_xlabel("Speedup = fastest control median / candidate median; above 1 is faster")
        ax.set_title("Selection and output: fresh seed banks after phase-two feedback\n"
                     "23 controls · fixed policies · 8 banks · 7 rounds · complete uint64 output")
        ax.legend(loc="upper center", bbox_to_anchor=(.5, -.09), ncol=2, frameon=False)
        fig.tight_layout()
        for ext in ("png", "svg"):
            fig.savefig(root / f"{args.prefix}_heldout_speedup.{ext}", dpi=160, bbox_inches="tight")
        plt.close(fig)
    print(json.dumps({"rows": len(rows), "conditions": len(groups), "stages": stages,
                      "trace_summary": traces}, indent=2))


if __name__ == "__main__":
    main()
