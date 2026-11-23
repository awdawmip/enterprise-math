#!/usr/bin/env python3
"""Finite exact p=17 valuation-one T6 profile injection up to four atoms.

Domain: per-side sum(e)<=2331, denominator d=e+1, 17||d.
The test uses only exact integer arithmetic, with no floating point.
"""
from collections import Counter
from itertools import combinations_with_replacement

CAP = 2331
P = 17
MODS = tuple(P**k for k in range(1, 5))
UNITS = tuple(u for u in range(1, (CAP + 1)//P + 1) if u % P)
ATOM_SIG = {
    u: tuple(pow(u, -k, modulus) for k, modulus in enumerate(MODS, 1))
    for u in UNITS
}

def signature(profile):
    return tuple(
        sum(ATOM_SIG[u][i] for u in profile) % modulus
        for i, modulus in enumerate(MODS)
    )

seen = {}
count_by_size = Counter()
collisions = []

# Every admissible multiset of 0,...,4 exact-v17(d)=1 denominators.
for n in range(5):
    for profile in combinations_with_replacement(UNITS, n):
        if P * sum(profile) - n > CAP:
            continue
        count_by_size[n] += 1
        sig = signature(profile)
        if sig in seen and seen[sig] != profile:
            collisions.append((seen[sig], profile))
        else:
            seen[sig] = profile

expected = {0: 1, 1: 129, 2: 4220, 3: 62225, 4: 531399}
assert dict(count_by_size) == expected, (count_by_size, expected)
assert len(seen) == sum(expected.values()) == 597974, len(seen)
assert not collisions, collisions[:5]
print("p17 exact-valuation-one profiles by size:", dict(count_by_size))
print("four-moment signatures:", len(seen))
print("collisions:", len(collisions))
print("PASS: profiles of up to four atoms are uniquely determined by k=1..4")
