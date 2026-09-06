"""Finite benchmark for the BRC multi-strip smooth-relation facade.

This experiment compares, at equal raw point budgets:
- one classical m=1 vertical strip;
- shallow round-robin sampling over all admissible BRC multiplier strips;
- a 75-way minimum-gap merge of those same strips.

Smooth relations and GF(2) dependencies are classical Dixon/QS/MPQS ideas.
The benchmark tests only the finite BRC sampling geometry and exact cross-strip
carrier implementation. It is not a production sieve and makes no factoring
complexity or novelty claim.
"""

from __future__ import annotations

import csv
import random
from pathlib import Path
from statistics import mean, median
from typing import Iterable

from enterprise_math.brc_multiplier_factor_scan import (
    AdmissibleMultiplierRootState,
    admissible_root_state_sequence,
)
from enterprise_math.brc_smooth_relation_scheduler import minimum_gap_relation_points
from enterprise_math.brc_smooth_relations import (
    GF2RelationAccumulator,
    congruence_from_dependency,
    factor_base,
    layered_relation_points,
    relation_from_multiplier_state,
)
from enterprise_math.legendre import is_prime


def _random_prime(lo: int, hi: int, rng: random.Random) -> int:
    while True:
        candidate = rng.randrange(lo | 1, hi, 2)
        if is_prime(candidate):
            return candidate


def semiprime_sample(lo: int, hi: int, count: int, seed: int) -> list[int]:
    rng = random.Random(seed)
    result: list[int] = []
    seen: set[tuple[int, int]] = set()
    while len(result) < count:
        p = _random_prime(lo, hi, rng)
        q = _random_prime(lo, hi, rng)
        if p == q:
            continue
        if p > q:
            p, q = q, p
        if (p, q) in seen:
            continue
        seen.add((p, q))
        result.append(p * q)
    return result


def _source(
    states: tuple[AdmissibleMultiplierRootState, ...],
    point_limit: int,
    mode: str,
) -> Iterable[tuple[AdmissibleMultiplierRootState, int]]:
    if mode == "single":
        return ((states[0], t) for t in range(point_limit))
    if mode == "layered":
        return layered_relation_points(states, point_limit)
    if mode == "minimum_gap":
        return (
            (point.state, point.vertical_offset)
            for point in minimum_gap_relation_points(states, point_limit)
        )
    raise ValueError("unknown scan mode")


def _smooth_count(n: int, smooth_bound: int, point_limit: int, mode: str) -> int:
    """Count all smooth relations in the full declared point budget."""
    base = factor_base(smooth_bound)
    states = admissible_root_state_sequence(n)
    count = 0
    for state, offset in _source(states, point_limit, mode):
        count += int(relation_from_multiplier_state(state, offset, base) is not None)
    return count


def _scan(
    n: int,
    smooth_bound: int,
    point_limit: int,
    mode: str,
) -> dict[str, int | None]:
    base = factor_base(smooth_bound)
    states = admissible_root_state_sequence(n)
    accumulator = GF2RelationAccumulator(base)
    dependencies = 0

    for points_examined, (state, offset) in enumerate(
        _source(states, point_limit, mode), 1
    ):
        relation = relation_from_multiplier_state(state, offset, base)
        if relation is None:
            continue
        dependency = accumulator.add(relation)
        if dependency is None:
            continue
        dependencies += 1
        congruence = congruence_from_dependency(tuple(accumulator.relations), dependency)
        factor = congruence.nontrivial_factor
        if factor is not None:
            return {
                "factor": factor,
                "points": points_examined,
                "smooth": len(accumulator.relations),
                "dependencies": dependencies,
            }
    return {
        "factor": None,
        "points": point_limit,
        "smooth": len(accumulator.relations),
        "dependencies": dependencies,
    }


def smooth_yield_summary() -> dict[str, object]:
    sample = semiprime_sample(100_000, 1_000_000, 20, 610)
    bound = 200
    point_limit = 3000
    single = [_smooth_count(n, bound, point_limit, "single") for n in sample]
    layered = [_smooth_count(n, bound, point_limit, "layered") for n in sample]
    return {
        "section": "smooth_yield",
        "prime_range": "100000-1000000",
        "sample_count": len(sample),
        "smooth_bound": bound,
        "point_limit": point_limit,
        "factor_base_count": len(factor_base(bound)),
        "single_mean_smooth": mean(single),
        "single_median_smooth": median(single),
        "layered_mean_smooth": mean(layered),
        "layered_median_smooth": median(layered),
        "mean_relation_yield_ratio": mean(layered) / mean(single),
    }


def factor_summary(lo: int, hi: int, count: int, seed: int, bound: int, point_limit: int) -> dict[str, object]:
    sample = semiprime_sample(lo, hi, count, seed)
    single = [_scan(n, bound, point_limit, "single") for n in sample]
    layered = [_scan(n, bound, point_limit, "layered") for n in sample]
    return {
        "section": "factor_budget",
        "prime_range": f"{lo}-{hi}",
        "sample_count": count,
        "smooth_bound": bound,
        "point_limit": point_limit,
        "factor_base_count": len(factor_base(bound)),
        "single_success": sum(row["factor"] is not None for row in single),
        "layered_success": sum(row["factor"] is not None for row in layered),
        "single_mean_points_miss_charged": mean(row["points"] for row in single),
        "layered_mean_points_miss_charged": mean(row["points"] for row in layered),
        "mean_point_ratio": mean(row["points"] for row in single) / mean(row["points"] for row in layered),
        "single_median_success_points": median(row["points"] for row in single if row["factor"] is not None),
        "layered_median_success_points": median(row["points"] for row in layered if row["factor"] is not None),
    }


def scheduler_summary(lo: int, hi: int, count: int, seed: int, bound: int, point_limit: int) -> dict[str, object]:
    sample = semiprime_sample(lo, hi, count, seed)
    layered = [_scan(n, bound, point_limit, "layered") for n in sample]
    minimum = [_scan(n, bound, point_limit, "minimum_gap") for n in sample]
    return {
        "section": "minimum_gap_scheduler",
        "prime_range": f"{lo}-{hi}",
        "sample_count": count,
        "smooth_bound": bound,
        "point_limit": point_limit,
        "layered_success": sum(row["factor"] is not None for row in layered),
        "minimum_gap_success": sum(row["factor"] is not None for row in minimum),
        "layered_mean_points": mean(row["points"] for row in layered),
        "minimum_gap_mean_points": mean(row["points"] for row in minimum),
        "extra_scheduler_ratio": mean(row["points"] for row in layered) / mean(row["points"] for row in minimum),
    }


def write_csv(path: str | Path) -> None:
    rows = [
        smooth_yield_summary(),
        factor_summary(100_000, 1_000_000, 50, 610, 200, 10_000),
        factor_summary(1_000_000, 10_000_000, 50, 611, 300, 20_000),
        factor_summary(10_000_000, 100_000_000, 30, 612, 500, 50_000),
        scheduler_summary(100_000, 1_000_000, 30, 610, 200, 10_000),
        scheduler_summary(1_000_000, 10_000_000, 30, 611, 300, 20_000),
        scheduler_summary(10_000_000, 100_000_000, 20, 612, 500, 50_000),
    ]
    keys = sorted({key for row in rows for key in row})
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    write_csv(
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_smooth_relation_lattice_benchmark_20260906.csv"
    )
