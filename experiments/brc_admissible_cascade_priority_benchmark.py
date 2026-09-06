"""Round-6 finite benchmark for BRC admissible multiplier scan and priority.

Reproduces safe m==2 mod 4 deletion, the mod-20160 + mod-46189 cascade,
and experimental first-hit rank comparisons. No asymptotic factorization
conclusion follows from these finite populations.
"""

from __future__ import annotations

import csv
import random
from math import isqrt
from pathlib import Path
from statistics import mean, median

from enterprise_math.brc_multiplier_factor_scan import (
    admissible_multipliers,
    heuristic_priority_multipliers,
    strong_cascade_passes_squarehood,
)
from enterprise_math.brc_square_gap_prefilter import passes_square_residue_filter
from enterprise_math.legendre import primes_up_to


def ceiling_gap(n: int, m: int) -> int:
    target = n * m
    root = isqrt(target)
    if root * root == target:
        return 0
    return (root + 1) * (root + 1) - target


def is_square(value: int) -> bool:
    root = isqrt(value)
    return root * root == value


def structured_filter_summary() -> dict[str, int]:
    primes = [p for p in primes_up_to(997) if p >= 101]
    candidates = squares = excluded = survive20 = survive2 = false_neg = 0
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            n = p * q
            for m in range(1, 101):
                gap = ceiling_gap(n, m)
                square = is_square(gap)
                candidates += 1
                squares += int(square)
                excluded += int(square and m % 4 == 2)
                survive20 += int(passes_square_residue_filter(gap, 20160))
                cascade = strong_cascade_passes_squarehood(gap)
                survive2 += int(cascade)
                false_neg += int(square and not cascade)
    return {
        "semiprimes": len(primes) * (len(primes) - 1) // 2,
        "candidates": candidates,
        "actual_square_gaps": squares,
        "excluded_m2mod4_square_gaps": excluded,
        "survive_20160": survive20,
        "survive_cascade": survive2,
        "cascade_false_negatives": false_neg,
    }


def _sample_pairs(primes: list[int], count: int, seed: int) -> list[tuple[int, int]]:
    rng = random.Random(seed)
    result = []
    seen = set()
    while len(result) < count:
        p, q = rng.sample(primes, 2)
        if p > q:
            p, q = q, p
        if (p, q) in seen:
            continue
        seen.add((p, q))
        result.append((p, q))
    return result


def _first_rank(order: tuple[int, ...], successes: set[int]) -> int | None:
    for rank, m in enumerate(order, 1):
        if m in successes:
            return rank
    return None


def priority_summary(lo: int, hi: int, sample_count: int | None, seed: int) -> dict[str, object]:
    primes = [p for p in primes_up_to(hi) if p >= lo]
    pairs = (
        [(p, q) for i, p in enumerate(primes) for q in primes[i + 1 :]]
        if sample_count is None
        else _sample_pairs(primes, sample_count, seed)
    )
    ascending = admissible_multipliers()
    priority = heuristic_priority_multipliers()
    ranks_a = []
    ranks_p = []
    for p, q in pairs:
        n = p * q
        successes = {m for m in ascending if is_square(ceiling_gap(n, m))}
        if not successes:
            continue
        ranks_a.append(_first_rank(ascending, successes))
        ranks_p.append(_first_rank(priority, successes))
    return {
        "prime_range": f"{lo}-{hi}",
        "sample_semiprimes": len(pairs),
        "hittable": len(ranks_a),
        "hit_rate": len(ranks_a) / len(pairs),
        "ascending_mean_rank": mean(ranks_a),
        "ascending_median_rank": median(ranks_a),
        "ascending_max_rank": max(ranks_a),
        "heuristic_mean_rank": mean(ranks_p),
        "heuristic_median_rank": median(ranks_p),
        "heuristic_max_rank": max(ranks_p),
        "mean_rank_improvement": mean(ranks_a) / mean(ranks_p),
        "median_rank_improvement": median(ranks_a) / median(ranks_p),
    }


def write_outputs(root: Path) -> None:
    artifacts = root / "research_artifacts"
    artifacts.mkdir(parents=True, exist_ok=True)
    filt = structured_filter_summary()
    with (artifacts / "brc_admissible_cascade_filter_20260906.csv").open("w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=filt.keys()); w.writeheader(); w.writerow(filt)
    rows = [
        priority_summary(101, 997, None, 1),
        priority_summary(1009, 9999, 20_000, 426),
        priority_summary(10007, 99999, 20_000, 427),
        priority_summary(100003, 999999, 20_000, 428),
    ]
    with (artifacts / "brc_multiplier_priority_benchmark_20260906.csv").open("w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)


if __name__ == "__main__":
    write_outputs(Path(__file__).resolve().parents[1])
