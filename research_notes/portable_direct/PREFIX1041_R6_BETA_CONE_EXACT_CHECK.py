#!/usr/bin/env python3
"""Exact rational checks for PREFIX-1041.

Analytic Bessel bounds, density representation and the Hoeffding bound
are proof premises stated in the companion note, not computed by this file.
"""
from fractions import Fraction as Q
from math import factorial

A = 2 * (2 * 36**3) + 36**2 * 521
assert A == 861840
term_A = Q(A, 5) * Q(5, 2)
term_B = (Q(69984, 3) + 16 * 34992) / 5
term_CD = Q(564 * 180 * 2, 5)
term_CE = Q(564 * 72, 5) * (Q(9, 4) + Q(2, 3))
M = term_A + term_B + term_CD + term_CE
assert (term_A, term_B, term_CD, term_CE) == (430920, 116640, 40608, 23688)
assert M == 611856
assert sum(Q(3**i, factorial(i)) for i in range(5)) > 16  # e^3>16

cases = [
    (4, 10**6, Q(7, 4), Q(5, 3)),
    (16, 10**9, Q(49, 50), Q(9, 10)),
]
for center, inverse_delta, gamma, margin in cases:
    delta = Q(1, inverse_delta)
    h = delta / 72
    n0 = 9 * (72 * inverse_delta)**2
    assert 2 * n0 * h**2 == 18
    assert gamma - (gamma + M) / 2**23 > margin
    assert n0 % 9 == 0
    j = n0 * center // 36
    assert Q(j, n0) == Q(center, 36)
    assert 1 <= j <= n0
    m, k = j - 1, n0 - j
    assert m + k + 1 == n0
    print(f'center={center}, delta={delta}, n0={n0}, '
          f'sample (m,k)=({m},{k}), guaranteed D>{margin}')
print(f'GLOBAL_SCALAR_BOUND={M}; EXACT_RATIONAL_IMPLICATIONS_PASSED')
