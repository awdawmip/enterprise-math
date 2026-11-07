#!/usr/bin/env python3
"""Exact rational certificate for S23/AV future-sign capacity, h=81..90."""
from bisect import bisect_left
from fractions import Fraction
from math import comb

EXPECTED = {81: 443, 82: 448, 83: 453, 84: 459, 85: 464,
            86: 470, 87: 475, 88: 481, 89: 486, 90: 492}


def thresholds(h):
    entries = sorted((Fraction(10**i, 7**(i + j)), i, j)
                     for i in range(h + 1) for j in range(h - i + 1))
    values = [a for a, _, _ in entries]
    assert len(values) == comb(h + 2, 2) == len(set(values))
    return entries, values


def occupied_intervals(n, values):
    """All prefixes of length <= n; label 3 pads to exact length n."""
    seen = bytearray(len(values) + 1)
    for k in range(n + 1):
        ten = 10**k
        for ell in range(n - k + 1):
            if k == ell == 0:
                continue  # equality class at Lambda=1; never an open interval
            lam = Fraction(7**(k + ell), ten)
            p = bisect_left(values, lam)
            assert p == len(values) or values[p] != lam
            seen[p] = 1
    return [j for j, seen_j in enumerate(seen) if not seen_j]


def tail_length(h):
    n = 0
    while 7**(n + h) >= 10**n:
        n += 1
    assert 7**(n + h) < 10**n
    assert n == 0 or 7**(n - 1 + h) >= 10**(n - 1)
    return n


def run():
    print('S23/AV exact finite-future threshold occupancy')
    for h, actual in EXPECTED.items():
        entries, values = thresholds(h)
        n_tail = tail_length(h)
        assert actual >= n_tail
        empty = occupied_intervals(actual, values)
        assert empty == [], (h, actual, empty)
        if h == 81:
            shorter = occupied_intervals(actual - 1, values)
            assert shorter, (h, actual)
            first = shorter[0]
            boundaries = (entries[first - 1][1:] if first else None,
                          entries[first][1:] if first < len(entries) else None)
            print(f'h={h} N={actual} tail={n_tail} lower_gap={first}, bounds={boundaries}, '
                  f'intervals={len(values) + 1} PASS')
        else:
            # Even the least prefix ratio at length n_tail-1 misses (0,7^-h).
            assert 7**(actual - 1 + h) >= 10**(actual - 1)
            print(f'h={h} N={actual} tail={n_tail} tail_lower_bound=EXACT '
                  f'intervals={len(values) + 1} PASS')
    print('PASS_S23_AV_N81_90_EXACT_HORIZON_SATURATION_20261107')


if __name__ == '__main__':
    run()
