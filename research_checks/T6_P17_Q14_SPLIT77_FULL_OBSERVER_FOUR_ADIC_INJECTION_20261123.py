#!/usr/bin/env python3
"""Exact proof checker: 17-adic four-moment signatures injective for p17 q14(7,7) one-power sides.

One side has vertical atoms d=17(17q+r), sum(q)=7, and arbitrary q0
atoms d=17j, 1<=j<=16, with total exponent mass sum(d-1)<=2331.
17-free lower-prime terms need not be enumerated: their reciprocal sums
are 17-adic integers and hence do not affect the necessary signatures.
"""
from collections import Counter, defaultdict
from bisect import bisect_right
from itertools import combinations_with_replacement, product
import json

P, MAX_MASS = 17, 2331
MOD = tuple(P**k for k in range(1, 5))

def smooth(n):
    for p in (2, 3, 5, 7, 11, 13, 17):
        while n % p == 0:
            n //= p
    return n == 1

def sig_atom(cofactor):
    assert cofactor % P
    out = tuple(pow(cofactor, -k, mod) for k, mod in enumerate(MOD, 1))
    assert out == tuple(pow(pow(cofactor, -1, mod), k, mod)
                        for k, mod in enumerate(MOD, 1))
    return out

def add(a, b, coeff=1):
    return tuple((x + coeff*y) % mod for x, y, mod in zip(a, b, MOD))

atoms = tuple((q, r, 289*q + 17*r - 1, sig_atom(17*q+r))
              for q in range(1, 8) for r in range(1, 17)
              if smooth(17*q+r))
assert len(atoms) == 60
zero = (0,)*len(MOD)
vertical = []

def build_vertical(first, q_left, mass, ids, sig):
    if q_left == 0:
        vertical.append((tuple(ids), mass, sig))
        return
    for idx in range(first, len(atoms)):
        q, r, cost, a_sig = atoms[idx]
        if q <= q_left and mass + cost <= MAX_MASS:
            build_vertical(idx, q_left - q, mass + cost,
                           ids+[idx], add(sig, a_sig))
build_vertical(0, 7, 0, [], zero)
assert len(vertical) == 1907

# Independent partition/combinations enumeration of the exact roster domain.
def partitions(n, low=1):
    if n == 0:
        yield ()
    for q in range(low, n+1):
        for tail in partitions(n-q, q):
            yield (q,) + tail
by_q = {q: tuple(i for i, atom in enumerate(atoms) if atom[0]==q)
        for q in range(1, 8)}
independent = set()
for part in partitions(7):
    runs = Counter(part)
    blocks = [combinations_with_replacement(by_q[q], repeats)
              for q, repeats in sorted(runs.items())]
    for choices in product(*blocks):
        ids = tuple(sorted(i for group in choices for i in group))
        if sum(atoms[i][2] for i in ids) <= MAX_MASS:
            independent.add(ids)
assert independent == {v[0] for v in vertical}

q0 = []
def build_q0(j, mass, num, sig, counts):
    if j == 17:
        q0.append((tuple(counts), mass, num, sig))
        return
    cost, unit_sig = 17*j-1, sig_atom(j)
    for multiplicity in range((292-mass)//cost+1):
        build_q0(j+1, mass + multiplicity*cost, num+multiplicity,
                 add(sig, unit_sig, multiplicity), counts+[multiplicity])
build_q0(1, 0, 0, zero, [])
assert len(q0) == 1223

# Independent combinatorial count using only the q0 mass distribution.
q0_mass_sorted = sorted(x[1] for x in q0)
independent_total = sum(bisect_right(q0_mass_sorted, MAX_MASS-v[1])
                        for v in vertical)

seen = {}
collisions = []
count = 0
for ids, vmass, vsig in vertical:
    for counts, qmass, qnum, qsig in q0:
        if vmass + qmass > MAX_MASS:
            continue
        key = add(vsig, qsig)
        entry = (ids, counts)
        if key in seen and seen[key] != entry:
            collisions.append((seen[key], entry, key))
        else:
            seen[key] = entry
        count += 1
assert count == independent_total == 55347
assert len(seen) == count and collisions == []

# Three moments leave opposite-support-disjoint modular ambiguities.
prefix = defaultdict(list)
for key, (ids, counts) in seen.items():
    vmask = sum(1 << i for i in set(ids))
    qmask = sum(1 << j for j, c in enumerate(counts) if c)
    prefix[key[:3]].append((vmask, qmask))
prefix_collisions = prefix_disjoint = 0
for options in prefix.values():
    for i, a in enumerate(options):
        for b in options[i+1:]:
            prefix_collisions += 1
            if not ((a[0] & b[0]) or (a[1] & b[1])):
                prefix_disjoint += 1
assert prefix_collisions == 1850 and prefix_disjoint == 27

certificate = {
    "scope": "maximal-p17 one-power q14 split(7,7), each U-side mass<=2331",
    "observer": "H0..H4 equality implies S1..S4 equality on the full sides",
    "necessary_condition": "R_k(U+) == R_k(U-) mod 17**k for k=1..4",
    "vertical_atoms": len(atoms),
    "vertical_rosters": len(vertical),
    "q0_side_multisets_mass_le_292": len(q0),
    "all_U_side_states_under_actual_budget": count,
    "distinct_four_component_signatures": len(seen),
    "colliding_distinct_U_sides": len(collisions),
    "three_component_colliding_pairs": prefix_collisions,
    "three_component_disjoint_colliding_pairs": prefix_disjoint,
    "lower_prime_completion": "arbitrary 17-free denominators only; no 17**2 denominator",
    "claim_status": "EXACT_FINITE_CHECKED; NOT_NATIVE_REVIEWED_OR_ADMITTED"
}
print(json.dumps(certificate, indent=2))
