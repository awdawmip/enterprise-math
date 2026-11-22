#!/usr/bin/env python3
"""Exact bounded one-power p17 q13(6,7) zero-q0 moment audit.

No external dependencies; source Task model uses denominator 17*(17*q+r),
full named atom multiplicity, real signed side mass, and cancellation.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
import json

PRIMES = (2, 3, 5, 7, 11, 13, 17)
BUDGET = 2331


def smooth17(n):
    for p in PRIMES:
        while n % p == 0:
            n //= p
    return n == 1


def atoms(order):
    return tuple((q, r, 17*q+r, 289*q+17*r-1)
                 for q in range(1, order+1)
                 for r in range(1, 17) if smooth17(17*q+r))


def dfs_rosters(order):
    catalog = atoms(order)
    out = []
    def rec(start, rem, mass, indices, reciprocal, second, mask):
        if rem == 0:
            out.append((tuple(indices), mass, len(indices), reciprocal, second, mask))
            return
        for i in range(start, len(catalog)):
            q, r, a, cost = catalog[i]
            if q <= rem and mass+cost <= BUDGET:
                indices.append(i)
                rec(i, rem-q, mass+cost, indices, reciprocal+F(1,a),
                    second+F(1,a*a), mask | (1 << i))
                indices.pop()
    rec(0, order, 0, [], F(0), F(0), 0)
    return catalog, out


def partitions(n, smallest=1):
    if n == 0:
        yield ()
    else:
        for q in range(smallest, n+1):
            for tail in partitions(n-q, q):
                yield (q,)+tail


def independent_roster_keys(order):
    by_q = {q: tuple((q,r,17*q+r,289*q+17*r-1)
                      for r in range(1,17) if smooth17(17*q+r))
            for q in range(1,order+1)}
    keys = set()
    for part in partitions(order):
        by_count = Counter(part)
        groups = [combinations_with_replacement(by_q[q], n)
                  for q,n in sorted(by_count.items())]
        for choice in product(*groups):
            flat = tuple(item for group in choice for item in group)
            if sum(a[3] for a in flat) <= BUDGET:
                key = tuple(sorted(a[2] for a in flat))
                assert key not in keys
                keys.add(key)
    return keys


c6, r6 = dfs_rosters(6)
c7, r7 = dfs_rosters(7)
assert (len(c6), len(c7), len(r6), len(r7)) == (52, 60, 11105, 1907)
assert {tuple(sorted(c6[i][2] for i in row[0])) for row in r6} == independent_roster_keys(6)
assert {tuple(sorted(c7[i][2] for i in row[0])) for row in r7} == independent_roster_keys(7)

lookup = defaultdict(list)
for row in r6:
    lookup[(row[2], row[3])].append(row)

index7 = {atom: i for i,atom in enumerate(c7)}
matched_h01 = 0
support_disjoint_h01 = 0
matched_h012 = []
for minus in r7:
    for plus in lookup[(minus[2], minus[3])]:
        matched_h01 += 1
        plus_mask = 0
        for i in plus[0]:
            plus_mask |= 1 << index7[c6[i]]
        if plus_mask & minus[5]:
            continue
        support_disjoint_h01 += 1
        if plus[4] == minus[4]:
            matched_h012.append((plus, minus))

assert (matched_h01, support_disjoint_h01, len(matched_h012)) == (2425, 375, 1)
plus, minus = matched_h012[0]
A = tuple(sorted(c6[i][2] for i in plus[0]))
B = tuple(sorted(c7[i][2] for i in minus[0]))
assert A == (21, 30, 84) and B == (20, 35, 70)
assert (plus[1], minus[1]) == (2292, 2122)
assert (plus[2], minus[2]) == (3, 3)
assert plus[3] == minus[3] == F(13, 140)
assert plus[4] == minus[4] == F(69, 19600)

# Original observer H_k = sum((e/(e+1))**k), e+1 = 17*cofactor.
def H(k, coeffs):
    return sum((F(17*a-1,17*a)**k for a in coeffs), F(0))
delta = [H(k,A)-H(k,B) for k in range(7)]
assert delta[:3] == [0, 0, 0]
assert delta[3] == F(1,1083316500)
assert delta[3] != 0

certificate = {
    'schema': 'T6_P17_Q13_SPLIT6_7_ZERO_Q0_H012_CERT_V1',
    'task_id': 'RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND',
    'scope': 'ONE_POWER_MAXIMAL_P17_Q13_SPLIT6_7_ZERO_Q0_NAMED_SUPPORT',
    'max_side_exponent_mass': BUDGET,
    'catalog_atoms_q6_q7': [len(c6), len(c7)],
    'side_rosters_q6_q7': [len(r6), len(r7)],
    'matching_H0_H1_pairs_before_cancellation': matched_h01,
    'support_disjoint_matching_H0_H1_pairs': support_disjoint_h01,
    'support_disjoint_matching_H0_H1_H2_pairs': len(matched_h012),
    'unique_witness': {
        'q6_cofactors': A, 'q7_cofactors': B,
        'q6_denominators': [17*x for x in A],
        'q7_denominators': [17*x for x in B],
        'vertical_orders': [6,7],
        'side_exponent_masses': [plus[1],minus[1]],
        'H0_both': 3,
        'scaled_first_reciprocal_both': str(plus[3]),
        'scaled_second_reciprocal_both': str(plus[4]),
        'observer_differences_H0_through_H6': [str(x) for x in delta],
    },
    'methods': ['monotone_atom_index_DFS','independent_integer_partition_and_multiset_enumeration'],
    'status': 'AUTHOR_EXACT_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED',
    'global_T6_status': 'OPEN',
}
print(json.dumps(certificate,ensure_ascii=False,indent=2))
