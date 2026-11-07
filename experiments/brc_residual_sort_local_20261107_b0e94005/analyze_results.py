#!/usr/bin/env python3
"""Summarize the completed, inclusive local-residual benchmark.

Ratios are ratios of seven-round medians, not confidence estimates.
The 'best' comparison columns are retrospective minima among named candidates;
they do not describe an implemented dispatch algorithm.
"""
import csv
import json
import statistics
from collections import OrderedDict
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    rows = list(csv.DictReader((root / "local_results.csv").open()))
    groups = OrderedDict()
    for row in rows:
        key = (row["family"], int(row["n"]))
        group = groups.setdefault(key, {})
        assert row["algorithm"] not in group
        group[row["algorithm"]] = row
    assert len(rows) == 288 and len(groups) == 24
    ordinary = ["std_sort", "offset_radix", "range_count_or_radix",
                "frequency_sort", "affine_range_local", "affine_square_local"]
    previous = ["brc_old_onecorrect", "brc_residual_div"]
    new = ["brc_local_floor", "brc_local_center",
           "brc_local_center_recompute", "brc_local_adaptive"]
    results = []
    lines = [
        "| Family | n | Previous BRC division, µs | Center local, µs | Adaptive, µs | Fastest ordinary candidate, µs |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for (family, n), group in groups.items():
        assert set(group) == set(ordinary + previous + new)
        time_of = lambda name: float(group[name]["median_us"])
        best_ordinary = min(ordinary, key=time_of)
        best_previous = min(previous, key=time_of)
        best_new = min(new, key=time_of)
        base = group["brc_residual_div"]
        center = group["brc_local_center"]
        round_ratios = [float(base[f"round{i}_us"]) / float(center[f"round{i}_us"])
                        for i in range(1, 8)]
        result = {"family": family, "n": n,
                  "times_us": {name: time_of(name) for name in group},
                  "best_ordinary": best_ordinary, "best_previous_brc": best_previous,
                  "best_new_brc": best_new,
                  "global_div_over_center": time_of("brc_residual_div") / time_of("brc_local_center"),
                  "best_previous_over_best_new": time_of(best_previous) / time_of(best_new),
                  "center_winning_rounds_over_global_div": sum(r > 1 for r in round_ratios),
                  "median_matched_round_global_over_center": statistics.median(round_ratios),
                  "shape": {key: base[key] for key in ["mean_distinct", "mean_min", "mean_max",
                            "mean_numeric_span", "floor_bucket_span", "center_bucket_span",
                            "floor_global_cells", "center_global_cells", "floor_local_cells",
                            "center_local_cells"]},
                  "new_paths": {name: group[name]["path"] for name in new},
                  "new_counter_cells": {name: group[name]["counter_cells"] for name in new},
                  "new_auxiliary_vector_bytes": {name: group[name]["auxiliary_vector_bytes"] for name in new}}
        results.append(result)
        lines.append(f"| {family} | {n:,} | {time_of('brc_residual_div'):.3f} | "
                     f"{time_of('brc_local_center'):.3f} | {time_of('brc_local_adaptive'):.3f} | "
                     f"{best_ordinary}: {time_of(best_ordinary):.3f} |")
    paired_fields = ["mean_distinct", "mean_min", "mean_max", "mean_numeric_span", "center_local_cells"]
    for n in (10000, 100000, 1000000):
        a = groups[("square1e6_s0", n)]["std_sort"]
        b = groups[("jitter1e6_B20_D8", n)]["std_sort"]
        assert all(a[key] == b[key] for key in paired_fields)
    for family in ("heldout_jitter_K8", "heldout_jitter_K2", "heldout_jitter_3K4"):
        a = groups[("square1e6_s0", 100000)]["std_sort"]
        b = groups[(family, 100000)]["std_sort"]
        assert all(a[key] == b[key] for key in paired_fields)
    payload = {"rows": len(rows), "conditions": len(groups),
               "ratios": "ratio of medians unless explicitly named matched-round median",
               "best_columns": "retrospective minima, not an implemented dispatcher",
               "paired_shape_summary_checks": "PASS", "results": results}
    (root / "analysis_summary.json").write_text(json.dumps(payload, indent=2) + "\n")
    (root / "results_table.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
