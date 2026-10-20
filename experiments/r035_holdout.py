"""Independent holdout validation for R035.

This file deliberately reimplements the lower-index oracle by monotone integer
binary search rather than importing the discriminant/isqrt inversion.  It then
cross-checks the optimized exact oracle and stress-tests structural laws on
parameter ranges largely disjoint from the discovery scans.
"""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Iterable, Tuple

from experiments.r035_polygonal_dynamics import (
    cardinality_components,
    is_integer_interval,
    iterate_support,
    lower_index,
    lower_jump,
    parent_children,
    polygonal,
    r4_children_formula,
)


def p_slow(s: int, k: int) -> int:
    return ((s - 2) * k * k - (s - 4) * k) // 2


def lower_slow(s: int, n: int) -> int:
    lo, hi = 0, 1
    while p_slow(s, hi) <= n:
        lo, hi = hi, 2 * hi
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if p_slow(s, mid) <= n:
            lo = mid
        else:
            hi = mid
    return lo


def children_slow(s: int, r: int, k: int) -> Tuple[int, ...]:
    n = r * p_slow(s, k)
    m = lower_slow(s, n)
    if p_slow(s, m) == n:
        return (m,)
    return (m, m + 1)


def one_step_slow(s: int, r: int, support: Iterable[int]) -> Tuple[int, ...]:
    out = set()
    for k in support:
        out.update(children_slow(s, r, k))
    return tuple(sorted(out))


def run_holdout(seed: int = 35035035) -> dict:
    rng = random.Random(seed)
    counts = {
        "lower_index_independent_crosschecks": 0,
        "parent_children_independent_crosschecks": 0,
        "jump_bound_random_checks": 0,
        "no_recoalescence_adjacent_random_checks": 0,
        "r2_r3_interval_levels_holdout": 0,
        "r4_formula_crosschecks": 0,
        "arbitrary_support_cardinality_checks": 0,
        "one_step_sanity_window_crosschecks": 0,
    }

    # 1. Optimized discriminant inversion vs an independently coded monotone
    # binary-search oracle, outside the original small n/s window.
    for _ in range(20_000):
        s = rng.randint(13, 90)
        n = rng.randint(0, 10**20)
        a = lower_index(s, n)
        b = lower_slow(s, n)
        if a != b:
            raise AssertionError(("lower-index mismatch", s, n, a, b))
        counts["lower_index_independent_crosschecks"] += 1

    # 2. Parent endpoint blocks, using r>40 and large k as a true holdout.
    for _ in range(20_000):
        s = rng.randint(13, 90)
        r = rng.randint(41, 160)
        k = rng.randint(0, 10**7)
        a = parent_children(s, r, k)
        b = children_slow(s, r, k)
        if a != b:
            raise AssertionError(("children mismatch", s, r, k, a, b))
        counts["parent_children_independent_crosschecks"] += 1

    # 3. Random jump bounds at large parameters; r>=4 also checks disjoint
    # adjacent child blocks directly with the independent endpoint oracle.
    for _ in range(50_000):
        s = rng.randint(13, 120)
        r = rng.randint(1, 200)
        k = rng.randint(1, 10**7)
        d = lower_jump(s, r, k)
        if not (1 <= d <= r):
            raise AssertionError(("jump bound", s, r, k, d))
        counts["jump_bound_random_checks"] += 1
        if r >= 4:
            a = children_slow(s, r, k)
            b = children_slow(s, r, k + 1)
            if set(a).intersection(b):
                raise AssertionError(("unexpected recoalescence", s, r, k, a, b))
            counts["no_recoalescence_adjacent_random_checks"] += 1

    # 4. Independent default-orbit generation for r=2,3 at k/depth outside the
    # initial discovery range.  No optimized one_step is used here.
    for s in range(13, 45):
        for r in (2, 3):
            for k0 in range(201, 281):
                current = (k0,)
                if not is_integer_interval(current):
                    raise AssertionError("singleton not interval")
                counts["r2_r3_interval_levels_holdout"] += 1
                for _ in range(11):
                    current = one_step_slow(s, r, current)
                    if not is_integer_interval(current):
                        raise AssertionError(("r2/r3 holdout gap", s, r, k0, current))
                    counts["r2_r3_interval_levels_holdout"] += 1

    # 5. Critical r=4 formula at much larger k and s than the regression suite.
    for _ in range(30_000):
        s = rng.randint(3, 150)
        k = rng.randint(0, 10**8)
        a = children_slow(s, 4, k)
        b = r4_children_formula(s, k)
        if a != b:
            raise AssertionError(("r4 formula", s, k, a, b))
        counts["r4_formula_crosschecks"] += 1

    # 6. Arbitrary finite supports, with widely separated indices, to verify
    # the exact hit/duplicate cardinality accounting on a disjoint random range.
    for _ in range(10_000):
        s = rng.randint(13, 100)
        r = rng.randint(1, 120)
        support = {rng.randint(0, 100_000) for _ in range(rng.randint(0, 20))}
        n, hits, duplicates, nnext = cardinality_components(s, r, support)
        if nnext != 2 * n - hits - duplicates:
            raise AssertionError(("cardinality", s, r, support))
        counts["arbitrary_support_cardinality_checks"] += 1

    # 7. The taskbook's suggested one-step sanity window, checked against the
    # independent oracle for every (s,r,k) triple.
    for s in range(3, 13):
        for r in range(1, 41):
            for k in range(0, 201):
                a = parent_children(s, r, k)
                b = children_slow(s, r, k)
                if a != b:
                    raise AssertionError(("sanity-window mismatch", s, r, k, a, b))
                counts["one_step_sanity_window_crosschecks"] += 1

    # Deterministic sharp-threshold and recoalescence witnesses are replayed
    # through the independent oracle.
    tri_r5_1 = (1,)
    tri_r5_2 = one_step_slow(3, 5, tri_r5_1)
    tri_r5_3 = one_step_slow(3, 5, tri_r5_2)
    if tri_r5_2 != (2, 3) or tri_r5_3 != (5, 7, 8):
        raise AssertionError(("sharp witness", tri_r5_2, tri_r5_3))

    tri_r2_1 = one_step_slow(3, 2, (4,))
    tri_r2_2 = one_step_slow(3, 2, tri_r2_1)
    if tri_r2_1 != (5, 6) or tri_r2_2 != (7, 8, 9):
        raise AssertionError(("recoalescence witness", tri_r2_1, tri_r2_2))

    total = sum(counts.values())
    return {
        "seed": seed,
        "method": "independent monotone integer binary-search oracle; no floating point",
        "status": "PASS",
        "counts": counts,
        "total_counted_checks": total,
        "deterministic_witnesses": {
            "sharp_interval_failure_r5": {
                "s": 3,
                "r": 5,
                "k0": 1,
                "S1": list(tri_r5_2),
                "S2": list(tri_r5_3),
            },
            "recoalescence_r2": {
                "s": 3,
                "r": 2,
                "k0": 4,
                "S1": list(tri_r2_1),
                "S2": list(tri_r2_2),
            },
        },
    }


if __name__ == "__main__":
    result = run_holdout()
    out = Path(__file__).resolve().parents[1] / "holdout_results.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
