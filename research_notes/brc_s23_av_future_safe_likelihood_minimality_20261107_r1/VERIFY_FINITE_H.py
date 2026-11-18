#!/usr/bin/env python3
"""Exact bounded-future likelihood-sign quotient verification (Fraction only)."""
from fractions import Fraction
from math import comb


def states(n):
    return [Fraction(7 ** (k + ell), 10 ** k)
            for k in range(n + 1) for ell in range(n - k + 1)]


def count_signatures(n, h):
    suffix = states(h)
    return len({tuple((x * y > 1) - (x * y < 1) for y in suffix)
                for x in states(n)})


assert count_signatures(0, 1) == 1
for n in range(1, 31):
    expected = 3 if n <= 5 else 5
    assert count_signatures(n, 1) == expected, n
print("ONE_STEP_EXACT n=0:1 n=1..5:3 n=6..30:5")

saturation = {}
for n in range(1, 8):
    target = comb(n + 2, 2)
    hits = [h for h in range(0, 40) if count_signatures(n, h) == target]
    assert hits and all(count_signatures(n, h) == target for h in range(hits[0], 40))
    if hits[0] > 0:
        assert count_signatures(n, hits[0] - 1) < target
    saturation[n] = hits[0]
assert saturation == {1: 0, 2: 6, 3: 11, 4: 17, 5: 22, 6: 28, 7: 33}
print("SATURATION_H n=1..7: " + ", ".join(f"{n}:{h}" for n, h in saturation.items()))

# Once n is large enough each of M+1 possible open intervals is occupied,
# plus the exact L=1 class. Check the small h cases over a growing n grid.
for h in range(0, 5):
    maximum = comb(h + 2, 2) + 2
    witness_n = next(n for n in range(1, 61)
                     if count_signatures(n, h) == maximum)
    assert all(count_signatures(n, h) == maximum
               for n in range(witness_n, min(witness_n + 4, 61)))
    print(f"INTERVAL_SATURATION h={h}: states={maximum}, witness_prefix_n={witness_n}")

# Exact finite evidence for the proposed sharp saturation threshold at h=1..10.
expected_n = [6, 11, 17, 22, 28, 33, 39, 44, 50, 55]
for h, n0 in enumerate(expected_n, start=1):
    maximum = comb(h + 2, 2) + 2
    assert count_signatures(n0 - 1, h) < maximum
    assert count_signatures(n0, h) == maximum
print("EXACT_N_H h=1..10: " + ",".join(map(str, expected_n)))

print("PASS_S23_AV_BOUNDED_FUTURE_SIGN_QUOTIENT_20261107")
