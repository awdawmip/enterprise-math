#!/usr/bin/env python3
"""Exact checker for RS-P000-SIX-AXIS-P11-SIMULTANEOUS-C1-C2-AP-PAIRABILITY.

The checker uses only exact integer arithmetic.  It never filters primes,
composites, even roots, negative roots, or zero roots.

Load-bearing checks:
  * exact pairability of two primitive witnesses;
  * exact equal-area Pythagorean normal-form identities;
  * primitive common-root gcd;
  * full-integer root-height regression B=20 and precommitted control B=64;
  * exploratory falsification census B=256.

A larger exploratory bound may be requested with --extra-bound B.
Finite census results are regression/falsification evidence only.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from functools import reduce
from math import gcd, isqrt
from typing import Dict, List, Optional, Sequence, Set, Tuple

Pair = Tuple[int, int]
Datum = Tuple[int, int, int, int, int, int]


def pairable_roots(h: int, t: int) -> Optional[Pair]:
    disc = h * h - 4 * t
    if disc < 0:
        return None
    d = isqrt(disc)
    if d * d != disc:
        return None
    if (h - d) % 2:
        return None
    r = (h - d) // 2
    s = (h + d) // 2
    assert r <= s and r + s == h and r * s == t
    return (r, s)


def is_strict_ap3(v: Sequence[int]) -> bool:
    return len(v) == 3 and v[0] < v[1] < v[2] and v[0] + v[2] == 2 * v[1]


def outer_root_table(datum: Datum) -> Dict[Tuple[int, int], Pair]:
    H = datum[:3]
    T = datum[3:]
    assert is_strict_ap3(H), H
    assert is_strict_ap3(T), T
    out: Dict[Tuple[int, int], Pair] = {}
    for i, h in enumerate(H):
        for j, t in enumerate(T):
            if (i, j) == (1, 1):
                continue
            roots = pairable_roots(h, t)
            if roots is None:
                raise AssertionError(f"outer cell {(i,j)} not pairable: h={h}, t={t}")
            out[(i, j)] = roots
    assert len(out) == 8
    return out


def common_root_gcd(datum: Datum) -> int:
    vals: List[int] = []
    for r, s in outer_root_table(datum).values():
        vals.extend((abs(r), abs(s)))
    g = reduce(gcd, vals)
    assert g > 0
    return g


def scale_datum(datum: Datum, m: int) -> Datum:
    assert m > 0
    return (
        datum[0] * m,
        datum[1] * m,
        datum[2] * m,
        datum[3] * m * m,
        datum[4] * m * m,
        datum[5] * m * m,
    )


def primitive_normalization(datum: Datum) -> Tuple[Datum, int]:
    g = common_root_gcd(datum)
    H = tuple(h // g for h in datum[:3])
    T = tuple(t // (g * g) for t in datum[3:])
    prim = H + T
    assert scale_datum(prim, g) == datum
    assert common_root_gcd(prim) == 1
    return prim, g


def discriminant_root(h: int, t: int) -> int:
    roots = pairable_roots(h, t)
    if roots is None:
        raise AssertionError((h, t))
    return roots[1] - roots[0]


def equal_area_normal_form(datum: Datum) -> dict:
    """Recover and exactly verify the equal-area Pythagorean normal form."""
    H = datum[:3]
    T = datum[3:]
    outer_root_table(datum)

    h = H[1]
    d = H[1] - H[0]
    t = T[1]
    e = T[1] - T[0]
    assert d > 0 and e > 0 and H == (h - d, h, h + d)
    assert T == (t - e, t, t + e)

    a = discriminant_root(H[0], T[0])
    b = discriminant_root(H[0], T[1])
    c = discriminant_root(H[0], T[2])
    mu = discriminant_root(H[1], T[0])
    nu = discriminant_root(H[1], T[2])
    f = discriminant_root(H[2], T[0])
    g = discriminant_root(H[2], T[1])
    k = discriminant_root(H[2], T[2])

    assert a > b > c >= 0
    assert f > g > k >= 0
    assert (a + c) % 2 == 0 and (a - c) % 2 == 0
    assert (f + k) % 2 == 0 and (f - k) % 2 == 0

    x = (a + c) // 2
    y = (a - c) // 2
    X = (f + k) // 2
    Y = (f - k) // 2

    # Pythagorean + equal-area core.
    assert x > y > 0 and X > Y > 0
    assert x * x + y * y == b * b
    assert X * X + Y * Y == g * g
    assert x * y == X * Y == 2 * e

    # Row-coupling and middle-row square cuts.
    K = g * g - b * b
    assert K == f * f - a * a == k * k - c * c
    assert K == 4 * h * d
    assert 2 * mu * mu == a * a + f * f - 2 * d * d
    assert 2 * nu * nu == c * c + k * k - 2 * d * d

    # Parity is preserved exactly; no square-only shortcut.
    assert (a - (h - d)) % 2 == 0
    assert (b - (h - d)) % 2 == 0
    assert (c - (h - d)) % 2 == 0
    assert (mu - h) % 2 == 0 and (nu - h) % 2 == 0
    assert (f - (h + d)) % 2 == 0
    assert (g - (h + d)) % 2 == 0
    assert (k - (h + d)) % 2 == 0

    # Exact reconstruction of T.
    assert e == (x * y) // 2
    assert 4 * t == (h - d) * (h - d) - b * b
    assert (t - e, t, t + e) == T

    return {
        "h": h, "d": d, "t": t, "e": e,
        "top_discriminants": [a, b, c],
        "middle_discriminants": [mu, nu],
        "bottom_discriminants": [f, g, k],
        "top_triangle": [x, y, b],
        "bottom_triangle": [X, Y, g],
        "equal_leg_product": x * y,
        "K": K,
        "primitive_root_gcd": common_root_gcd(datum),
    }


def root_catalog(B: int) -> Tuple[Dict[int, Set[int]], Dict[Tuple[int, int], Pair]]:
    assert B >= 0
    S: Dict[int, Set[int]] = defaultdict(set)
    roots: Dict[Tuple[int, int], Pair] = {}
    for r in range(-B, B + 1):
        for s in range(r, B + 1):
            h, t = r + s, r * s
            S[h].add(t)
            roots[(h, t)] = (r, s)
    return S, roots


def enumerate_root_height(B: int) -> Tuple[List[Datum], Dict[Tuple[int, int], Pair]]:
    """Enumerate every AP outer-grid datum whose eight recovered root pairs lie in [-B,B]."""
    S, roots = root_catalog(B)
    Hvals = sorted(S)
    sols: List[Datum] = []

    for h0 in Hvals:
        for h2 in Hvals:
            if h2 <= h0 or (h0 + h2) % 2:
                continue
            h1 = (h0 + h2) // 2
            if h1 not in S:
                continue

            top_bottom = S[h0] & S[h2]
            if len(top_bottom) < 3:
                continue

            # Middle row needs only the two outer T columns.
            ends = sorted(top_bottom & S[h1])
            for i, t0 in enumerate(ends):
                for t2 in ends[i + 1:]:
                    if (t0 + t2) % 2:
                        continue
                    t1 = (t0 + t2) // 2
                    if t0 < t1 < t2 and t1 in top_bottom:
                        datum: Datum = (h0, h1, h2, t0, t1, t2)
                        # Recheck all 8 cells by the direct predicate.
                        outer_root_table(datum)
                        # Every recovered root must be inside the declared full-integer box.
                        assert max(abs(z) for pair in outer_root_table(datum).values()
                                   for z in pair) <= B
                        sols.append(datum)

    return sorted(set(sols)), roots


def census(B: int) -> dict:
    sols, _ = enumerate_root_height(B)
    primitive = [s for s in sols if common_root_gcd(s) == 1]
    normalized = sorted({primitive_normalization(s)[0] for s in sols})
    return {
        "B": B,
        "raw_solution_count": len(sols),
        "primitive_solution_count": len(primitive),
        "primitive_normalized_count": len(normalized),
        "primitive_solutions": [list(s) for s in primitive],
        "primitive_normalized": [list(s) for s in normalized],
    }


WITNESS_A: Datum = (41, 44, 47, 0, 210, 420)
WITNESS_A_INV: Datum = (-47, -44, -41, 0, 210, 420)
WITNESS_B: Datum = (-105, 0, 105, -10816, -5800, -784)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extra-bound", type=int, default=None)
    args = parser.parse_args()

    A = equal_area_normal_form(WITNESS_A)
    Ainv = equal_area_normal_form(WITNESS_A_INV)
    B = equal_area_normal_form(WITNESS_B)

    assert A["top_triangle"] == [21, 20, 29]
    assert A["bottom_triangle"] == [35, 12, 37]
    assert A["equal_leg_product"] == 420 and A["e"] == 210
    assert A["K"] == 528 == 4 * 44 * 3
    assert A["middle_discriminants"] == [44, 16]
    assert A["primitive_root_gcd"] == 1

    assert Ainv["top_triangle"] == [35, 12, 37]
    assert Ainv["bottom_triangle"] == [21, 20, 29]
    assert Ainv["h"] == -44 and Ainv["K"] == -528
    assert Ainv["primitive_root_gcd"] == 1

    assert B["top_triangle"] == [176, 57, 185]
    assert B["bottom_triangle"] == [176, 57, 185]
    assert B["equal_leg_product"] == 10032 and B["e"] == 5016
    assert B["K"] == 0 and B["h"] == 0
    assert B["middle_discriminants"] == [208, 56]
    assert B["primitive_root_gcd"] == 1

    # Scaling is exactly common-root scaling.
    assert common_root_gcd(scale_datum(WITNESS_A, 2)) == 2
    assert primitive_normalization(scale_datum(WITNESS_A, 2))[0] == WITNESS_A
    assert common_root_gcd(scale_datum(WITNESS_B, 3)) == 3
    assert primitive_normalization(scale_datum(WITNESS_B, 3))[0] == WITNESS_B

    # Parent regression and precommitted control.
    c20 = census(20)
    c64 = census(64)
    c256 = census(256)

    assert c20["raw_solution_count"] == 0
    assert c64["raw_solution_count"] == 2
    assert c64["primitive_solutions"] == [list(WITNESS_A_INV), list(WITNESS_A)]
    assert c256["raw_solution_count"] == 11
    assert c256["primitive_solution_count"] == 3
    assert c256["primitive_solutions"] == [
        list(WITNESS_B), list(WITNESS_A_INV), list(WITNESS_A)
    ]

    payload = {
        "schema": "P000_P11_SIMULTANEOUS_C1_C2_AP_PAIRABILITY_CHECK_V1",
        "witness_A": A,
        "witness_A_involution": Ainv,
        "witness_B": B,
        "census": [c20, c64, c256],
        "finite_census_is_proof": False,
        "normal_form_checked_by_exact_integer_identities": True,
    }

    if args.extra_bound is not None:
        payload["extra_census"] = census(args.extra_bound)

    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
