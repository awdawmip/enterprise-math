#!/usr/bin/env python3
"""Exact finite G<=18 test for native BRC loss after (relative,G,L) compression."""
from collections import defaultdict
from itertools import product
from math import factorial

def brc(z):
    a = [abs(t) for t in z]
    return factorial(sum(a)) // (factorial(a[0])*factorial(a[1])*factorial(a[2]))

groups = defaultdict(list)
for z in product(range(-5, 6), repeat=3):
    G = sum(t*t for t in z)
    if G > 18:
        continue
    h = min(z)
    r = tuple(t-h for t in z)
    L = sum(abs(t) for t in z)
    groups[(r,G,L)].append((z, brc(z)))
different = {k:v for k,v in groups.items() if len({b for _,b in v}) > 1}
assert len(groups) == 315
assert len(different) == 6
assert {k[1] for k in different} == {18}
assert {k[2] for k in different} == {6}
assert all(sorted({b for _,b in v}) == [20,30] for v in different.values())
assert different[((0,0,3),18,6)] == [((-3,-3,0),20),((1,1,4),30)]
assert not any(g<=17 for (_,g,_),v in different.items())
print("PASS_X6_LP019_SHARP_RELATIVE_NORM_LENGTH_BRC_LOSS_G18")
print(f"exact_fibers={len(groups)} differing_fibers={len(different)}")
print("earliest_G=18; common_L=6; differing_BRC_values=20,30")
