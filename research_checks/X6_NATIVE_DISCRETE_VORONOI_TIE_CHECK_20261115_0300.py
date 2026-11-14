#!/usr/bin/env python3
"""Exact integer check for the typed X6 native Cell Voronoi comparator.
Checks 3 site pairs on all 5^6 signed lattice points [-2,2]^6.
Separate theorem (unbounded) is proved in the accompanying note.
"""
from itertools import product
from math import gcd

ZERO = (0,) * 6
PAIRS = (
    ("adjacent", ZERO, (1, 0, 0, 0, 0, 0), (9375, 6250, 0)),
    ("double_axis", ZERO, (2, 0, 0, 0, 0, 0), (9375, 3125, 3125)),
    ("two_axis", ZERO, (1, 1, 0, 0, 0, 0), (9375, 3750, 2500)),
)

def dist2(x, a):
    return sum((u - v) ** 2 for u, v in zip(x, a))

def norm2(a):
    return sum(u * u for u in a)

def main():
    for name, a, b, expected in PAIRS:
        g = 0
        for delta in (v-u for u, v in zip(a, b)):
            g = gcd(g, abs(delta))
        assert g > 0
        possible_integer_tie = (norm2(b)-norm2(a)) % (2*g) == 0
        counts = [0, 0, 0]
        for x in product(range(-2, 3), repeat=6):
            da, db = dist2(x, a), dist2(x, b)
            assert da-db == 2*sum(xx*(bb-aa) for xx, aa, bb in zip(x, a, b)) + norm2(a)-norm2(b)
            counts[0 if da < db else 1 if db < da else 2] += 1
        assert tuple(counts) == expected, (name, counts, expected)
        assert possible_integer_tie == (counts[2] > 0), name
        print(f"{name} gcd={g} integer_tie={possible_integer_tie} cube_counts={tuple(counts)}")
    print("PASS_X6_NATIVE_DISCRETE_VORONOI_INTEGER_TIE_20261115_0300")

if __name__ == "__main__":
    main()
