#!/usr/bin/env python3
"""Exact checks for the fixed-fiber future-sign minimality theorem.

The infinite-horizon density lemma is proved in PROOF.md, not inferred
from these finite tests. Uses only Python standard-library Fraction.
"""
from bisect import bisect_right
from fractions import Fraction
from math import comb


def likelihood(k: int, ell: int) -> Fraction:
    return Fraction(7 ** (k + ell), 10 ** k)


def counts(n: int):
    return [(k, ell) for k in range(n + 1)
            for ell in range(n - k + 1)]


for n in range(1, 13):
    signatures = {likelihood(k, ell) for k, ell in counts(n)}
    assert len(signatures) == comb(n + 2, 2)
print("INJECTIVE_COUNTS_VERIFIED n=1..12")

# Explicit n=6 indistinguishable-prefix / one-step sign split.
w = likelihood(5, 1)  # 111114
v = likelihood(0, 1)  # 433333
one = likelihood(1, 0)
assert w == Fraction(117649, 100000) and v == 7
assert w > 1 and v > 1
assert w * one == Fraction(823543, 1000000) < 1
assert v * one == Fraction(49, 10) > 1
print("ANY4_PREFIX_COLLISION n=6: 117649/100000 and 7")
print("AFTER_COMMON_SUFFIX_1: 823543/1000000 < 1 < 49/10")

# Independent finite coverage check of every pair of inequivalent count
# states up to length n=7, using suffix counts in the box [0,40]^2.
# This is a finite regression, not the infinite-density proof.
suffixes = sorted((likelihood(k, ell), k, ell)
                  for k in range(41) for ell in range(41))
values = [s[0] for s in suffixes]
checked = 0
max_used_length = 0
for n in range(1, 8):
    states = [(k, ell, likelihood(k, ell)) for k, ell in counts(n)]
    for idx, (_, _, x) in enumerate(states):
        for _, _, y in states[idx + 1:]:
            low, high = sorted((x, y))
            j = bisect_right(values, 1 / high)
            assert j < len(values) and values[j] < 1 / low, (n, low, high)
            _, k, ell = suffixes[j]
            assert low * likelihood(k, ell) < 1 < high * likelihood(k, ell)
            max_used_length = max(max_used_length, k + ell)
            checked += 1
print(f"PAIRWISE_SUFFIX_WITNESSES n=1..7: {checked}, max_suffix_length={max_used_length}")
print(f"MINIMAL_FUTURE_SAFE_STATES n=6:{comb(8, 2)} n=7:{comb(9, 2)} n=1000:{comb(1002, 2)}")
print("PASS_S23_AV_FUTURE_SAFE_OBSERVER_MINIMALITY_20261107")
