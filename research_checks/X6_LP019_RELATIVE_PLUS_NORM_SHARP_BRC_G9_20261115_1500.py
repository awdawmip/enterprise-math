#!/usr/bin/env python3
"""Exact LP019 sharp norm and common-depth BRC observer test; stdlib only."""
from collections import defaultdict
from itertools import product
from math import factorial

def native_brc(z):
    a = tuple(abs(x) for x in z)
    v = factorial(sum(a))
    for x in a:
        v //= factorial(x)
    return v

def relative(z):
    h = min(z)
    return tuple(x - h for x in z)

# All G<=9 signed triples are in [-3,3]^3. Keep both cells and counts.
fibers = defaultdict(list)
for z in product(range(-3, 4), repeat=3):
    G = sum(x*x for x in z)
    if G <= 9:
        fibers[(relative(z), G)].append((z, native_brc(z)))
bad = {k: v for k,v in fibers.items() if len({b for _,b in v}) > 1}
assert len(fibers) == 110
assert len(bad) == 6
assert {k[1] for k in bad} == {9}
assert all(sorted({b for _,b in v}) == [1, 30] for v in bad.values())
assert bad[((0,0,3),9)] == [((-2,-2,1),30),((0,0,3),1)]

# All relative triples with max<=2 have a BRC value fixed by (r,G)
# even when the common depth ranges beyond the finite native cube.
small = [r for r in product(range(3),repeat=3) if min(r)==0]
for r in small:
    seen = {}
    for h in range(-20, 21):
        z = tuple(x+h for x in r)
        G = sum(x*x for x in z)
        b = native_brc(z)
        assert G not in seen or seen[G] == b, (r,h,G,seen.get(G),b)
        seen[G] = b

print("PASS_X6_LP019_SHARP_RELATIVE_PLUS_NORM_BRC_LOSS_G9")
print(f"exact_fibers={len(fibers)} differing_fibers={len(bad)}")
print("earliest_G=9; differing_BRC_values=1,30; spread_threshold=3")
