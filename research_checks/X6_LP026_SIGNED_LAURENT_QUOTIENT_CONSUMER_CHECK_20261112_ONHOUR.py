#!/usr/bin/env python3
"""Exact signed-relative X6 BRC Laurent adapter and typed legacy-consumer regression.

P000's signed X6 primitive-axis words only. The quotient is an observer of
native endpoints, never a native Cell address. All arithmetic is exact.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
import importlib.util

D = 6
ZERO5 = (0,) * 5
POS = [tuple(int(j == i) for j in range(5)) for i in range(5)] + [(-1,) * 5]
NEG = [tuple(-x for x in q) for q in POS]


def chart(z):
    assert len(z) == D
    return tuple(z[i] - z[-1] for i in range(5))


def can6(z):
    h = min(z)
    return tuple(x - h for x in z)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def quotient_walks(max_length, wp, wm):
    """Exact Laurent coefficients of F_weighted(y)**N."""
    steps = POS + NEG
    weights = list(map(Fraction, wp)) + list(map(Fraction, wm))
    states = {ZERO5: Fraction(1)}
    for n in range(max_length + 1):
        yield n, states
        if n == max_length:
            return
        nxt = defaultdict(Fraction)
        for q, mass in states.items():
            for step, weight in zip(steps, weights):
                if weight:
                    nxt[add(q, step)] += mass * weight
        states = dict(nxt)


def native_endpoint_weight(n, z, wp, wm):
    """Independent signed 12-letter histogram formula at one true endpoint."""
    positive = [max(x, 0) for x in z]
    negative = [max(-x, 0) for x in z]
    length = sum(positive) + sum(negative)
    if n < length or (n - length) % 2:
        return Fraction(0)
    thickness = (n - length) // 2
    total = Fraction(0)
    for allocation in product(range(thickness + 1), repeat=6):
        if sum(allocation) != thickness:
            continue
        term = Fraction(factorial(n))
        for i in range(6):
            p = positive[i] + allocation[i]
            m = negative[i] + allocation[i]
            term *= Fraction(wp[i]) ** p * Fraction(wm[i]) ** m
            term /= factorial(p) * factorial(m)
        total += term
    return total


def independent_depth_fiber(n, q, wp, wm):
    """Every true endpoint over q has z6=h, and |h|<=N."""
    return sum(
        (native_endpoint_weight(n, tuple(x + h for x in q) + (h,), wp, wm)
         for h in range(-n, n + 1)), Fraction(0))


def fixed_positive_legacy(n, a):
    """Restricted six-positive-letter relative formula, not signed BRC."""
    gap = n - sum(a)
    if gap < 0 or gap % 6:
        return 0
    counts = [x + gap // 6 for x in a]
    value = factorial(n)
    for count in counts:
        value //= factorial(count)
    return value


def current_source_positive_consumer(n, a):
    """Optional actual current consumer check, only if full repo exists."""
    path = (Path(__file__).resolve().parents[1] / "experiments" /
            "x6_signed_native_spatial_v16_20260905" / "x6_signed.py")
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location("current_x6_signed", path)
    assert spec is not None and spec.loader is not None
    import sys
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod.relative_endpoint_multiplicity(n, a)


def main():
    ones = (1,) * 6
    all_states = {}
    compared = 0
    for n, counts in quotient_walks(8, ones, ones):
        assert sum(counts.values()) == 12 ** n
        assert len(counts) == (1,12,73,284,835,2036,4347,8408,15069)[n]
        for q, mass in counts.items():
            assert mass == counts.get(tuple(-x for x in q), 0)
            assert chart(can6(q + (0,))) == q
        compared += len(counts)
        all_states[n] = counts

    a = (0, 1, 1, 2, 3, 5)
    assert all_states[2][ZERO5] == 12
    assert all_states[6][ZERO5] == 21360
    assert all_states[8][chart(a)] == 4200

    positive = dict(quotient_walks(8, ones, (0,) * 6))
    assert positive[6][ZERO5] == 720
    actual_consumer = False
    for n, a0 in [(2, (0,)*6), (6, (0,)*6),
                  (8, a), (1, (0,0,0,0,0,1))]:
        expected = fixed_positive_legacy(n, a0)
        observed = current_source_positive_consumer(n, a0)
        if observed is not None:
            assert observed == expected
            actual_consumer = True
        assert positive[n].get(chart(a0), 0) == expected
    assert fixed_positive_legacy(8, a) == 0

    wp = (Fraction(1), Fraction(1,2), Fraction(2),
          Fraction(1), Fraction(3,2), Fraction(2))
    wm = (Fraction(1), Fraction(3,2), Fraction(1,3),
          Fraction(2), Fraction(1), Fraction(3))
    weighted_compared = 0
    weighted = {}
    for n, counts in quotient_walks(4, wp, wm):
        assert sum(counts.values()) == sum(wp + wm) ** n
        for q, mass in counts.items():
            assert mass == independent_depth_fiber(n, q, wp, wm), (n, q)
            weighted_compared += 1
        weighted[n] = counts
    assert weighted[2][ZERO5] == 2 * sum(
        (p * m for p, m in zip(wp, wm)), Fraction(0))

    print("PASS X6_LP026_SIGNED_LAURENT_QUOTIENT_CONSUMER")
    print("unweighted_state_length_cases", compared)
    print("weighted_depth_multinomial_cases", weighted_compared)
    print("signed_relative_n6_zero", all_states[6][ZERO5])
    print("signed_relative_n8_011235", all_states[8][chart(a)])
    print("legacy_positive_n6_zero", positive[6][ZERO5])
    print("weighted_n2_zero", weighted[2][ZERO5])
    print("current_repo_positive_consumer", "PASS" if actual_consumer else "NOT_RUN_NO_CHECKOUT")


if __name__ == "__main__":
    main()
