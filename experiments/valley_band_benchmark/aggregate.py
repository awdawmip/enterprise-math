"""Aggregate the frozen benchmark table without dropping null/timeout rows."""

from __future__ import annotations

import csv
import hashlib
import json
import statistics
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_PATH = ROOT / "research_output" / "VALLEY_BAND_BENCHMARK_RUNS_20260823.csv"
OUT_PATH = ROOT / "research_output" / "VALLEY_BAND_BENCHMARK_AGGREGATES_20260823.csv"


FIELDS = [
    "algorithm", "band_threshold", "policy_variant", "multiplier_policy", "multiplier",
    "large_prime_mode", "bits", "split", "planned_runs", "completed_runs", "not_run_runs",
    "timeout_runs", "error_runs", "factor_found_runs", "null_factor_runs", "median_wall_seconds",
    "mad_wall_seconds", "min_wall_seconds", "max_wall_seconds", "median_peak_memory_bytes",
    "median_point_candidates", "median_band_candidates", "median_full_relations", "median_rank",
    "median_dependencies", "relation_yield_per_1000_candidates", "rank_yield_per_1000_candidates",
    "status_counts_json", "source_runs_sha256",
]


def number(rows: list[dict[str, str]], field: str) -> list[float]:
    return [float(row[field]) for row in rows if row.get(field, "") != ""]


def median_or_blank(values: list[float]) -> str:
    return "" if not values else f"{statistics.median(values):.9f}"


def main() -> int:
    raw = RUN_PATH.read_bytes()
    source_digest = hashlib.sha256(raw).hexdigest()
    rows = list(csv.DictReader(raw.decode("utf-8").splitlines()))
    groups: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    keys = ("algorithm", "band_threshold", "policy_variant", "multiplier_policy", "multiplier",
            "large_prime_mode", "bits", "split")
    for row in rows:
        groups[tuple(row[key] for key in keys)].append(row)
    out: list[dict[str, object]] = []
    for key, group in sorted(groups.items()):
        completed = [row for row in group if row["completed"] == "true"]
        walls = number(completed, "wall_seconds")
        candidates = sum(float(row["point_candidates"] or 0) + float(row["band_candidates"] or 0)
                         for row in completed)
        full = sum(float(row["full_relations"] or 0) for row in completed)
        rank = sum(float(row["rank"] or 0) for row in completed)
        statuses: dict[str, int] = defaultdict(int)
        for row in group:
            statuses[row["status"]] += 1
        result: dict[str, object] = dict(zip(keys, key))
        result.update({
            "planned_runs": len(group), "completed_runs": len(completed),
            "not_run_runs": len(group) - len(completed), "timeout_runs": statuses.get("TIMEOUT", 0),
            "error_runs": statuses.get("ERROR", 0),
            "factor_found_runs": sum(row["factor_found"] == "true" for row in completed),
            "null_factor_runs": sum(row["factor_found"] == "false" for row in completed),
            "median_wall_seconds": median_or_blank(walls),
            "mad_wall_seconds": "" if not walls else f"{statistics.median(abs(x-statistics.median(walls)) for x in walls):.9f}",
            "min_wall_seconds": "" if not walls else f"{min(walls):.9f}",
            "max_wall_seconds": "" if not walls else f"{max(walls):.9f}",
            "median_peak_memory_bytes": median_or_blank(number(completed, "peak_memory_bytes")),
            "median_point_candidates": median_or_blank(number(completed, "point_candidates")),
            "median_band_candidates": median_or_blank(number(completed, "band_candidates")),
            "median_full_relations": median_or_blank(number(completed, "full_relations")),
            "median_rank": median_or_blank(number(completed, "rank")),
            "median_dependencies": median_or_blank(number(completed, "dependencies")),
            "relation_yield_per_1000_candidates": "" if not candidates else f"{1000*full/candidates:.9f}",
            "rank_yield_per_1000_candidates": "" if not candidates else f"{1000*rank/candidates:.9f}",
            "status_counts_json": json.dumps(dict(sorted(statuses.items())), separators=(",", ":")),
            "source_runs_sha256": source_digest,
        })
        out.append(result)
    with OUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(out)
    print(json.dumps({"groups": len(out), "output": str(OUT_PATH), "source_digest": source_digest}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
