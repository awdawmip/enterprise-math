"""Finite benchmark for priority scheduling over the BRC multiplier x vertical wheel.

The benchmark separates:
1. exact factor-pair rank geometry (cheap, large samples);
2. actual vertical-wheel runtime after one shared horizontal BRC state build;
3. a diagnostic runtime showing that the proved arbitrary one-correction jump
   should not replace CPython isqrt in the default priority path.

No asymptotic factorization conclusion follows from these finite samples.
"""

from __future__ import annotations

import csv
import random
import statistics
import time
from math import isqrt
from pathlib import Path

from enterprise_math.brc_multiplier_factor_scan import (
    AdmissibleMultiplierRootState,
    admissible_multipliers,
    admissible_root_state_sequence,
    heuristic_priority_multipliers,
    nontrivial_same_parity_factor_pairs,
)
from enterprise_math.brc_multiplier_priority_vertical import (
    ordered_vertical_factor_witness_from_states,
    remainder_aware_multiplier_jump,
)
from enterprise_math.legendre import primes_up_to


def _ceil_sqrt(value: int) -> int:
    root = isqrt(value)
    return root if root * root == value else root + 1


def _all_same_parity_pairs(multiplier: int) -> tuple[tuple[int, int], ...]:
    pairs = list(nontrivial_same_parity_factor_pairs(multiplier))
    root = isqrt(multiplier)
    if root * root == multiplier:
        pairs.append((root, root))
    return tuple(pairs)


def minimum_vertical_offset(p: int, q: int, multiplier: int) -> int | None:
    """Exact least t from any same-parity multiplier split for N=p*q."""
    base = _ceil_sqrt(multiplier * p * q)
    best: int | None = None
    pairs = _all_same_parity_pairs(multiplier)
    if multiplier == 1:
        pairs = ((1, 1),)
    for u, v in pairs:
        for left, right in ((u * p, v * q), (v * p, u * q)):
            if (left - right) & 1:
                continue
            x = (left + right) // 2
            t = x - base
            if t >= 0 and (best is None or t < best):
                best = t
    return best


def _sample_pairs(lo: int, hi: int, count: int, seed: int) -> list[tuple[int, int]]:
    primes = [p for p in primes_up_to(hi) if p >= lo]
    rng = random.Random(seed)
    result: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    while len(result) < count:
        p, q = rng.sample(primes, 2)
        if p > q:
            p, q = q, p
        if (p, q) in seen:
            continue
        seen.add((p, q))
        result.append((p, q))
    return result


def _first_rank(order: tuple[int, ...], success: set[int]) -> int:
    return next(rank for rank, multiplier in enumerate(order, 1) if multiplier in success)


def rank_summary(lo: int, hi: int, t_limit: int, count: int, seed: int) -> dict[str, object]:
    pairs = _sample_pairs(lo, hi, count, seed)
    ascending = admissible_multipliers()
    priority = heuristic_priority_multipliers()
    ranks_a: list[int] = []
    ranks_p: list[int] = []
    for p, q in pairs:
        success = {
            m
            for m in ascending
            if (t := minimum_vertical_offset(p, q, m)) is not None and t <= t_limit
        }
        if not success:
            continue
        ranks_a.append(_first_rank(ascending, success))
        ranks_p.append(_first_rank(priority, success))
    hit = len(ranks_a)
    return {
        "section": "rank",
        "prime_range": f"{lo}-{hi}",
        "t_limit": t_limit,
        "sample_count": count,
        "hittable": hit,
        "hit_rate": hit / count,
        "ascending_mean_rank": statistics.mean(ranks_a),
        "ascending_median_rank": statistics.median(ranks_a),
        "priority_mean_rank": statistics.mean(ranks_p),
        "priority_median_rank": statistics.median(ranks_p),
        "priority_top5_rate": sum(rank <= 5 for rank in ranks_p) / hit,
        "priority_top10_rate": sum(rank <= 10 for rank in ranks_p) / hit,
        "rank_improvement": statistics.mean(ranks_a) / statistics.mean(ranks_p),
        "ascending_all_population_mean": (sum(ranks_a) + 75 * (count - hit)) / count,
        "priority_all_population_mean": (sum(ranks_p) + 75 * (count - hit)) / count,
    }


def runtime_summary(t_limit: int, count: int = 300, seed: int = 881) -> dict[str, object]:
    pairs = _sample_pairs(10007, 99999, count, seed + t_limit)
    ascending = admissible_multipliers()
    priority = heuristic_priority_multipliers()
    families = [admissible_root_state_sequence(p * q) for p, q in pairs]

    start = time.perf_counter()
    results_a = [
        ordered_vertical_factor_witness_from_states(states, t_limit, ascending)
        for states in families
    ]
    ascending_seconds = time.perf_counter() - start

    start = time.perf_counter()
    results_p = [
        ordered_vertical_factor_witness_from_states(states, t_limit, priority)
        for states in families
    ]
    priority_seconds = time.perf_counter() - start

    if [value is None for value in results_a] != [value is None for value in results_p]:
        raise AssertionError("priority order changed vertical rectangle existence")
    ranks_a = [value.priority_rank for value in results_a if value is not None]
    ranks_p = [value.priority_rank for value in results_p if value is not None]
    return {
        "section": "runtime",
        "prime_range": "10007-99999",
        "t_limit": t_limit,
        "sample_count": count,
        "hittable": len(ranks_a),
        "hit_rate": len(ranks_a) / count,
        "ascending_mean_rank": statistics.mean(ranks_a),
        "priority_mean_rank": statistics.mean(ranks_p),
        "runtime_speedup": ascending_seconds / priority_seconds,
        "ascending_seconds": ascending_seconds,
        "priority_seconds": priority_seconds,
    }


def direct_priority_state(n: int, multiplier: int) -> AdmissibleMultiplierRootState:
    root = isqrt(n * multiplier)
    return AdmissibleMultiplierRootState(
        n=n,
        multiplier=multiplier,
        root=root,
        remainder=n * multiplier - root * root,
        correction_steps=0,
    )


def arbitrary_jump_runtime_summary(bits: int, count: int, prefix: int = 10) -> dict[str, object]:
    rng = random.Random(992_000 + bits)
    ns = [rng.getrandbits(bits - 1) | (1 << (bits - 1)) | 1 for _ in range(count)]
    order = heuristic_priority_multipliers()[:prefix]

    # Warm the coefficient cache so this comparison measures transition cost,
    # not one-time coefficient construction.
    state = direct_priority_state(ns[0], order[0])
    for target in order[1:]:
        cert = remainder_aware_multiplier_jump(state, target)
        state = AdmissibleMultiplierRootState(
            n=state.n,
            multiplier=target,
            root=cert.target_root,
            remainder=cert.target_remainder,
            correction_steps=cert.correction_steps,
        )

    direct_times: list[float] = []
    jump_times: list[float] = []
    for _ in range(5):
        start = time.perf_counter()
        for n in ns:
            for multiplier in order:
                direct_priority_state(n, multiplier)
        direct_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        for n in ns:
            state = direct_priority_state(n, order[0])
            for target in order[1:]:
                cert = remainder_aware_multiplier_jump(state, target)
                state = AdmissibleMultiplierRootState(
                    n=n,
                    multiplier=target,
                    root=cert.target_root,
                    remainder=cert.target_remainder,
                    correction_steps=cert.correction_steps,
                )
        jump_times.append(time.perf_counter() - start)

    direct = statistics.median(direct_times)
    jump = statistics.median(jump_times)
    return {
        "section": "arbitrary_jump_runtime_negative",
        "prime_range": f"{bits}-bit random odd N",
        "t_limit": f"priority_prefix_{prefix}",
        "sample_count": count,
        "direct_seconds": direct,
        "jump_seconds": jump,
        "direct_priority_over_jump": jump / direct,
    }


def write_csv(path: str | Path) -> None:
    rows: list[dict[str, object]] = [
        rank_summary(1009, 9999, 10, 20_000, 526),
        rank_summary(10007, 99999, 100, 20_000, 527),
        rank_summary(100003, 999999, 1000, 20_000, 528),
        runtime_summary(30),
        runtime_summary(100),
        runtime_summary(300),
        arbitrary_jump_runtime_summary(512, 100),
        arbitrary_jump_runtime_summary(1024, 100),
        arbitrary_jump_runtime_summary(2048, 40),
        arbitrary_jump_runtime_summary(4096, 40),
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
        / "brc_priority_vertical_scheduler_20260906.csv"
    )
