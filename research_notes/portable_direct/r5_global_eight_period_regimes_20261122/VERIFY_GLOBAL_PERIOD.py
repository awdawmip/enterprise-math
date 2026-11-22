#!/usr/bin/env python3
"""Arithmetic/CRT validator for the R5 eight-regime conditional theorem.

This validates pole inventories, lcm, congruence intersections and counts.
It does not re-prove the prior cyclotomic characteristic-zero certificates.
"""
from collections import Counter
from math import lcm

PRICES = tuple(range(214, 315))
L = 229746052653717600
K = 92119507880400
P = 79808
D_LOWER = (7, 11, 13, 17, 19, 23, 25, 27, 31, 37)
D_LOWER_16 = D_LOWER + (16,)
A29 = {0, 54, 55, 56, 57}
A32 = {0, 60, 61, 62, 63}
A43 = {0, 37, 38, 39, 40, 41, 42}

pole_orders = tuple(d for d in range(1, max(PRICES)+1)
                    if sum(p % d == 0 for p in PRICES) >= 3)
assert len(pole_orders) == 40
assert lcm(*pole_orders) == L
assert lcm(*D_LOWER_16) == K
assert L == K * 29 * 2 * 43
assert lcm(58, 64, 43) == P
for d in D_LOWER:
    assert sum(p % d == 0 for p in PRICES) >= (3 if d == 37 else 4)
assert sum(p % 16 == 0 for p in PRICES) >= 4
for d in (29, 32, 43):
    assert sum(p % d == 0 for p in PRICES) == 3
    assert all((q == d or sum(p % q == 0 for p in PRICES) <= 2)
               for q in pole_orders if q % d == 0)

def flags(m):
    assert m > 0
    return (m % 58 in A29, m % 64 in A32, m % 43 in A43)

def period(m):
    z29, z32, z43 = flags(m)
    return K * (1 if z29 else 29) * (1 if z32 else 2) * (1 if z43 else 43)

counts = Counter(flags(m) for m in range(1, P+1))
expected = {
    (False, False, False): 56304,
    (False, False, True): 10948,
    (False, True, False): 4752,
    (False, True, True): 924,
    (True, False, False): 5292,
    (True, False, True): 1029,
    (True, True, False): 468,
    (True, True, True): 91,
}
assert counts == expected
assert sum(counts.values()) == P
assert set(period(m) for m in range(1, P+1)) == {
    L, L//43, L//2, L//86, L//29, L//(29*43), L//(29*2), K
}
for m, ratio in [(1,1), (37,43), (54,29), (60,2), (124,86),
                 (170,29*43), (576,29*2), (2492,29*2*43)]:
    assert period(m) == L//ratio

print("PASS denominator_pole_orders=40 L=%d K=%d modulus=%d" % (L,K,P))
print("PASS complete_8_regime_residue_count=79808")
for f in sorted(counts):
    m = next(x for x in range(1,P+1) if flags(x)==f)
    print("flags=%s count=%d period=%d earliest=%d" % (f,counts[f],period(m),m))
print("DEPENDENCY: prior characteristic-zero 29/32/43 cancellation theorems")
print("DEPENDENCY: prior all-m lower cyclotomic jet certificates (including conditional order16)")
