#!/usr/bin/env python3
"""Exact verifier for the O13 ordered-port orbit theorem, horizons 5..20.

Pure Python integer arithmetic; no external dependencies.
"""
from itertools import product
from math import comb, prod
import json

F5 = range(5)
F5_STAR = (1, 2, 3, 4)
V = tuple((a, s) for a in F5_STAR for s in F5)
INDEX = {p: i for i, p in enumerate(V)}
G = tuple(product(F5_STAR, F5_STAR, F5))
assert len(V) == 20 and len(G) == 80

def permutation(u, v, t):
    return tuple(INDEX[((u * a) % 5, (v * s + t) % 5)] for a, s in V)

def cycle_count(perm):
    seen = set()
    cycles = 0
    for i in range(len(perm)):
        if i in seen:
            continue
        cycles += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = perm[j]
    return cycles

group_rows = []
for u, v, t in G:
    perm = permutation(u, v, t)
    fixed = sum(perm[i] == i for i in range(20))
    cycles = cycle_count(perm)
    identity = (u, v, t) == (1, 1, 0)
    assert fixed == 20 if identity else fixed <= 4
    group_rows.append({"u": u, "v": v, "t": t, "fixed_points": fixed,
                       "cycles": cycles, "identity": identity})

horizons = []
for m in range(5, 21):
    falling = prod(range(20 - m + 1, 21))
    assert falling % 80 == 0
    factor = falling // 80
    by_initial_size = [factor * comb(20 - m, k) for k in range(21 - m)]
    total = sum(by_initial_size)
    assert total == factor * (2 ** (20 - m))
    horizons.append({"m": m, "falling_factorial": falling,
                     "orbit_factor": factor, "by_initial_support_size": by_initial_size,
                     "total_orbits": total})

assert horizons[0]["orbit_factor"] == 23256
assert horizons[0]["total_orbits"] == 762052608
assert horizons[0]["by_initial_support_size"] == [
    23256, 348840, 2441880, 10581480, 31744440, 69837768,
    116396280, 149652360, 149652360, 116396280, 69837768,
    31744440, 10581480, 2441880, 348840, 23256
]

print(json.dumps({
    "model": "O13 finite Boolean-support BRC auxiliary model",
    "ports": 20,
    "group_order": 80,
    "nonidentity_max_fixed_points": max(r["fixed_points"] for r in group_rows if not r["identity"]),
    "group_elements_checked": len(group_rows),
    "horizons": horizons,
    "theorem": "For m>=5 distinct ordered ports, the diagonal G-action on (S,p1,...,pm), S disjoint from the tuple, is free; orbit count by |S|=k is (20)_m/80 * binom(20-m,k)."
}, indent=2))
