#!/usr/bin/env python3
"""Exact N=25 two-axis root-fiber distinction within the P000 signed X6 substrate.

Counts are for the union of fixed *two-axis* charts; not the entire X6 N=25
sphere or a new native PathSqrt operator. Root descriptions retain ordered
axis labels, unlike their native endpoint image.
"""
from collections import Counter
from itertools import combinations, product
from math import factorial

D = 6
R2 = 25
ROOTS = tuple((a, b) for a in range(6) for b in range(6) if a*a+b*b == R2)
assert ROOTS == ((0, 5), (3, 4), (4, 3), (5, 0))

def endpoint(i, j, a, b, si=1, sj=1):
    z = [0] * D
    z[i] += si*a
    z[j] += sj*b
    return tuple(z)

def brc(z):
    n = sum(abs(v) for v in z)
    out = factorial(n)
    for v in z:
        out //= factorial(abs(v))
    return out

description_fibers = Counter()
for i in range(D):
    for j in range(D):
        if i != j:
            for a, b in ROOTS:
                description_fibers[endpoint(i, j, a, b)] += 1

positive = set(description_fibers)
assert sum(description_fibers.values()) == 120
assert len(positive) == 36
assert Counter(description_fibers.values()) == Counter({10:6, 2:30})
assert sum(brc(z) for z in positive) == 1056
assert sum(sum(v != 0 for v in z) == 1 for z in positive) == 6

signed = set()
for i, j in combinations(range(D), 2):
    for a, b in ROOTS:
        for si, sj in product((-1, 1), repeat=2):
            signed.add(endpoint(i, j, a, b, si, sj))
assert len(signed) == 132
assert sum(sum(v != 0 for v in z) == 1 for z in signed) == 12
assert sum(sum(v != 0 for v in z) == 2 for z in signed) == 120
assert sum(brc(z) for z in signed) == 4212
assert endpoint(0, 1, 3, 4) != endpoint(0, 2, 3, 4)
assert brc(endpoint(0, 1, 3, 4)) == brc(endpoint(0, 2, 3, 4)) == 35
print("PASS_X6_LP028_R25_ORDERED_TWO_AXIS_CHART_FIBERS")
print("ordered_positive_descriptions=120; unique_positive_endpoints=36; positive_brc_mass=1056")
print("positive_description_preimage_size_histogram={2:30,10:6}")
print("signed_two_axis_unique_endpoints=132; signed_two_axis_brc_mass=4212")
print("status=EXACT_FINITE_TWO_AXIS_CHART_ONLY_NOT_FULL_X6_SHELL")
