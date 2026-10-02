#!/usr/bin/env python3
"""Exact bounded support-carrier detector for the Enterprise Math CFD hybrid task.

Scope: finite Fourier-Galerkin retained cube B_K = [-K,K]^3 with exact integer
wavevector labels.  The detector never prunes amplitudes.  It computes the least
negation-symmetric carrier C containing the seed and closed under p+q whenever
p,q in C and p+q remains in B_K.  If C stays within `limit`, it is an exact
support-level invariant carrier for convolution followed by diagonal Fourier
multipliers and linear combinations.  If the monotone construction exceeds
`limit`, sparse mode is rejected immediately; no claim about the final closure
cardinality is needed.

This is a routing certificate, not a continuous PDE theorem and not a claim that
all coefficients in C are nonzero.  Complex amplitudes, multiplicity and phase
remain in the nonlinear evaluator.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import argparse
import json
import random
import statistics
import time
from typing import Iterable, Optional

Vec = tuple[int, int, int]


def neg(v: Vec) -> Vec:
    return (-v[0], -v[1], -v[2])


def add(p: Vec, q: Vec) -> Vec:
    return (p[0] + q[0], p[1] + q[1], p[2] + q[2])


def in_box(v: Vec, K: int) -> bool:
    return -K <= v[0] <= K and -K <= v[1] <= K and -K <= v[2] <= K


def symmetrize(seed: Iterable[Vec]) -> set[Vec]:
    C = set(seed)
    C |= {neg(v) for v in tuple(C)}
    return C


@dataclass(frozen=True)
class ClosureResult:
    status: str
    carrier_size: Optional[int]
    lower_bound: int
    rounds: int
    pair_tests: int
    carrier: Optional[tuple[Vec, ...]]


def truncated_additive_carrier(seed: Iterable[Vec], K: int, limit: int = 384) -> ClosureResult:
    """Compute the least in-box additive carrier, or soundly reject above limit.

    Exactness invariant: after every completed round, C is a subset of the least
    fixed point C*. Therefore observing |C| > limit proves |C*| > limit.  A
    fixed point is exactly closed under all retained pair sums.
    """
    if K < 0 or limit < 0:
        raise ValueError("K and limit must be nonnegative")
    C = symmetrize(seed)
    if any(not in_box(v, K) for v in C):
        raise ValueError("seed outside retained cube")
    if len(C) > limit:
        return ClosureResult("FALLBACK_DENSE", None, len(C), 0, 0, None)

    rounds = 0
    pair_tests = 0
    while True:
        rounds += 1
        L = sorted(C)
        new: set[Vec] = set()
        for i, p in enumerate(L):
            for q in L[i:]:
                pair_tests += 1
                r = add(p, q)
                if in_box(r, K) and r not in C and r not in new:
                    new.add(r)
                    rn = neg(r)
                    if rn not in C and rn not in new:
                        new.add(rn)
                    if len(C) + len(new) > limit:
                        return ClosureResult(
                            "FALLBACK_DENSE", None, limit + 1, rounds, pair_tests, None
                        )
        if not new:
            carrier = tuple(sorted(C))
            return ClosureResult("CERTIFIED_STATIC_CARRIER", len(C), len(C), rounds, pair_tests, carrier)
        C |= new


def verify_closed(carrier: Iterable[Vec], K: int) -> bool:
    C = set(carrier)
    if any(neg(v) not in C for v in C):
        return False
    L = list(C)
    for p in L:
        for q in L:
            r = add(p, q)
            if in_box(r, K) and r not in C:
                return False
    return True


def lattice_hyperplane(K: int, normal: Vec = (1, -7, 6)) -> set[Vec]:
    a, b, c = normal
    return {
        (x, y, z)
        for x in range(-K, K + 1)
        for y in range(-K, K + 1)
        for z in range(-K, K + 1)
        if a * x + b * y + c * z == 0
    }


def lambda_seed() -> set[Vec]:
    p = (7, 1, 0)
    q = (-6, 0, 1)
    return symmetrize({p, q})


def taylor_green_seed() -> set[Vec]:
    return {(sx, sy, sz) for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)}


def random_symmetric_seed(K: int, pairs: int, seed: int) -> set[Vec]:
    rng = random.Random(seed)
    base: set[Vec] = set()
    while len(base) < pairs:
        v = (rng.randint(-K, K), rng.randint(-K, K), rng.randint(-K, K))
        if v != (0, 0, 0):
            base.add(v)
    return symmetrize(base)


def run_case(name: str, seed: set[Vec], K: int, limit: int, repeats: int) -> dict:
    timings = []
    last = None
    for _ in range(repeats):
        t0 = time.perf_counter()
        last = truncated_additive_carrier(seed, K, limit)
        timings.append(time.perf_counter() - t0)
    assert last is not None
    d = asdict(last)
    d.pop("carrier")
    d.update(
        {
            "name": name,
            "K": K,
            "seed_size_full_signed": len(seed),
            "limit_full_signed": limit,
            "median_seconds": statistics.median(timings),
            "min_seconds": min(timings),
            "max_seconds": max(timings),
        }
    )
    if last.carrier is not None:
        assert verify_closed(last.carrier, K)
    return d


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=384)
    ap.add_argument("--repeats", type=int, default=25)
    args = ap.parse_args()

    cases = []
    for K in (7, 15):
        cases.append(run_case("shear-line", {(0, 1, 0), (0, -1, 0)}, K, args.limit, args.repeats))
        cases.append(run_case("lambda-two-generator", lambda_seed(), K, args.limit, args.repeats))
        cases.append(run_case("taylor-green-support", taylor_green_seed(), K, args.limit, args.repeats))
        cases.append(run_case("heldout-random-16-pairs", random_symmetric_seed(K, 16, 1000 + K), K, args.limit, args.repeats))
        cases.append(run_case("heldout-random-128-pairs", random_symmetric_seed(K, 128, 2000 + K), K, args.limit, args.repeats))

    for K, expected in ((7, 33), (15, 139)):
        got = truncated_additive_carrier(lambda_seed(), K, args.limit)
        assert got.status == "CERTIFIED_STATIC_CARRIER"
        assert got.carrier_size == expected
        exact = lattice_hyperplane(K)
        assert set(got.carrier or ()) == exact

    for K in (7, 15):
        got = truncated_additive_carrier({(0, 1, 0), (0, -1, 0)}, K, args.limit)
        assert got.carrier_size == 2 * K + 1
        assert set(got.carrier or ()) == {(0, y, 0) for y in range(-K, K + 1)}

    for K in (7, 15):
        assert truncated_additive_carrier(taylor_green_seed(), K, args.limit).status == "FALLBACK_DENSE"
        assert truncated_additive_carrier(random_symmetric_seed(K, 16, 1000 + K), K, args.limit).status == "FALLBACK_DENSE"

    print(json.dumps({"schema": "EM_CFD_CLOSED_SUPPORT_DETECTOR_CHECK_V1", "limit": args.limit, "cases": cases}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
