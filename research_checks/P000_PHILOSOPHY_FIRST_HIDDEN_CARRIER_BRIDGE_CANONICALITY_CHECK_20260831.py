#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
from collections import Counter, deque

HPTS = tuple((a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0))
HI = {v: i for i, v in enumerate(HPTS)}
ID8 = tuple(range(8))
ID4 = tuple(range(4))

def add3(x, y, z):
    return ((x[0] + y[0] + z[0]) % 3, (x[1] + y[1] + z[1]) % 3)

def comp(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def inv(p):
    r = [0] * len(p)
    for i, j in enumerate(p):
        r[j] = i
    return tuple(r)

def power(p, n):
    r = tuple(range(len(p)))
    for _ in range(n):
        r = comp(r, p)
    return r

def order(p):
    one = tuple(range(len(p)))
    r = one
    for n in range(1, 100):
        r = comp(r, p)
        if r == one:
            return n
    raise AssertionError("order bound")

def generated(gens):
    if not gens:
        return {tuple()}
    one = tuple(range(len(gens[0])))
    seen = {one}
    q = deque([one])
    while q:
        x = q.popleft()
        for g in gens:
            y = comp(x, g)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen

def image_tri(p, t):
    return tuple(sorted(p[i] for i in t))

def preserves_tri(p, rel):
    return frozenset(image_tri(p, t) for t in rel) == rel

BAL = frozenset(
    tuple(sorted((HI[x], HI[y], HI[z])))
    for x, y, z in itertools.combinations(HPTS, 3)
    if add3(x, y, z) == (0, 0)
)
assert len(BAL) == 8

codeg = {
    (i, j): sum(i in t and j in t for t in BAL)
    for i, j in itertools.combinations(range(8), 2)
}
assert Counter(codeg.values()) == Counter({1: 24, 0: 4})
FIBRES = tuple(sorted((tuple(sorted(pair)) for pair, d in codeg.items() if d == 0), key=lambda x: x))
assert len(FIBRES) == 4 and all(len(f) == 2 for f in FIBRES)
FIBRE_OF = {}
for s, f in enumerate(FIBRES):
    for x in f:
        FIBRE_OF[x] = s

AUT_H = tuple(p for p in itertools.permutations(range(8)) if preserves_tri(p, BAL))
assert len(AUT_H) == 48

def fibre_action(p):
    out = []
    for f in FIBRES:
        image = {FIBRE_OF[p[x]] for x in f}
        assert len(image) == 1
        out.append(next(iter(image)))
    return tuple(out)

S4 = tuple(itertools.permutations(range(4)))
S4SET = set(S4)
H_IMAGE = {fibre_action(h) for h in AUT_H}
assert H_IMAGE == S4SET
H_KERNEL = tuple(h for h in AUT_H if fibre_action(h) == ID4)
assert len(H_KERNEL) == 2

AXES = tuple(itertools.combinations(range(4), 2))
AI = {e: i for i, e in enumerate(AXES)}
CARRIER_STARS = frozenset(frozenset(AI[e] for e in AXES if v in e) for v in range(4))
assert len(CARRIER_STARS) == 4

def image_set(p, s):
    return frozenset(p[i] for i in s)

AUT_AXIS = tuple(
    p for p in itertools.permutations(range(6))
    if frozenset(image_set(p, s) for s in CARRIER_STARS) == CARRIER_STARS
)
assert len(AUT_AXIS) == 24
STAR_LIST = tuple(sorted(CARRIER_STARS, key=lambda x: tuple(sorted(x))))
STAR_INDEX = {s: i for i, s in enumerate(STAR_LIST)}

def carrier_star_action(p):
    return tuple(STAR_INDEX[image_set(p, STAR_LIST[i])] for i in range(4))

assert {carrier_star_action(p) for p in AUT_AXIS} == S4SET
G0_ORDER = len(AUT_H) * len(S4)
assert G0_ORDER == 1152

BRIDGES = S4

def bridge_act(hq, c, b):
    return comp(c, comp(b, inv(hq)))

bridge_orbit = {bridge_act(fibre_action(h), c, ID4) for h in AUT_H for c in S4}
assert bridge_orbit == set(BRIDGES)
full_bridge_stab = [
    (h, c) for h in AUT_H for c in S4
    if bridge_act(fibre_action(h), c, ID4) == ID4
]
assert len(full_bridge_stab) == 48
assert G0_ORDER // len(full_bridge_stab) == 24
assert all(any(bridge_act(fibre_action(h), c, b) != b for h in AUT_H for c in S4) for b in BRIDGES)

def gen4(gs):
    seen = {ID4}
    q = deque([ID4])
    while q:
        x = q.popleft()
        for g in gs:
            y = comp(x, g)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen

qpairs = [
    (a, b) for a in S4 for b in S4
    if order(a) == 3 and order(b) == 2 and order(comp(a, b)) == 4 and len(gen4((a, b))) == 24
]
assert len(qpairs) == 24
lifts = {q: tuple(h for h in AUT_H if fibre_action(h) == q) for q in S4}
assert all(len(v) == 2 for v in lifts.values())
z = next(h for h in H_KERNEL if h != ID8)
residue = Counter()
for a, b in qpairs:
    for A in lifts[a]:
        for B in lifts[b]:
            residue[power(comp(A, B), 4)] += 1
assert residue == Counter({z: 96})

def parity(p):
    n = 0
    for i in range(4):
        for j in range(i + 1, 4):
            n += p[i] > p[j]
    return n % 2

def canon_partition(block):
    block = frozenset(block)
    other = frozenset(set(range(4)) - set(block))
    return frozenset((block, other))

PARTITIONS = tuple(sorted(
    {canon_partition(b) for b in itertools.combinations(range(4), 2)},
    key=lambda P: sorted(tuple(sorted(B)) for B in P)
))
assert len(PARTITIONS) == 3
PI = {P: i for i, P in enumerate(PARTITIONS)}

def partition_action(p):
    out = []
    for P in PARTITIONS:
        imageP = frozenset(frozenset(p[i] for i in B) for B in P)
        out.append(PI[imageP])
    return tuple(out)

assert len({partition_action(p) for p in S4}) == 6
A_PP = [
    (h, c) for h in AUT_H for c in S4
    if partition_action(fibre_action(h)) == partition_action(c)
]
assert len(A_PP) == 192
assert len({c for _, c in A_PP}) == 24
assert len({h for h, c in A_PP if c == ID4}) == 8
assert G0_ORDER // len(A_PP) == 6

def all_subgroups(group, one):
    group = tuple(group)
    subs = {frozenset((one,))}
    queue = deque([frozenset((one,))])
    while queue:
        K = queue.popleft()
        for g in group:
            if g in K:
                continue
            L = frozenset(generated(tuple(K) + (g,)))
            if L not in subs:
                subs.add(L)
                queue.append(L)
    return subs

H_SUBGROUPS = all_subgroups(AUT_H, ID8)
assert len(H_SUBGROUPS) == 55
S3_SECTIONS = [
    K for K in H_SUBGROUPS
    if len(K) == 6 and len({partition_action(fibre_action(h)) for h in K}) == 6
]
assert S3_SECTIONS
J = next(iter(S3_SECTIONS))
J_BY_PART = {partition_action(fibre_action(h)): h for h in J}
section_pp = {c: J_BY_PART[partition_action(c)] for c in S4}
for c1 in S4:
    for c2 in S4:
        assert section_pp[comp(c1, c2)] == comp(section_pp[c1], section_pp[c2])
assert all((section_pp[c], c) in A_PP for c in S4)

A_OR = [
    (h, c) for h in AUT_H for c in S4
    if parity(fibre_action(h)) == parity(c)
]
assert len(A_OR) == 576
assert len({c for _, c in A_OR}) == 24
assert len({h for h, c in A_OR if c == ID4}) == 24
assert G0_ORDER // len(A_OR) == 2
odd_involutions = [h for h in AUT_H if order(h) == 2 and parity(fibre_action(h)) == 1]
assert odd_involutions
r = odd_involutions[0]
section_or = {c: (r if parity(c) else ID8) for c in S4}
for c1 in S4:
    for c2 in S4:
        assert section_or[comp(c1, c2)] == comp(section_or[c1], section_or[c2])
assert all((section_or[c], c) in A_OR for c in S4)

BLOCK0 = frozenset((0, 1))
BLOCK1 = frozenset((2, 3))
UPART = frozenset((BLOCK0, BLOCK1))

def preserves_upart(p):
    return frozenset((frozenset(p[i] for i in BLOCK0), frozenset(p[i] for i in BLOCK1))) == UPART

def block_swap(p):
    im0 = frozenset(p[i] for i in BLOCK0)
    if im0 == BLOCK0:
        return 0
    if im0 == BLOCK1:
        return 1
    raise AssertionError("not in partition stabilizer")

A_BO = [
    (h, c) for h in AUT_H for c in S4
    if preserves_upart(fibre_action(h)) and block_swap(fibre_action(h)) == parity(c)
]
assert len(A_BO) == 192
assert len({c for _, c in A_BO}) == 24
BO_KERNEL = {h for h, c in A_BO if c == ID4}
assert len(BO_KERNEL) == 8
BO_CHOICE_STATES = G0_ORDER // len(A_BO)
assert BO_CHOICE_STATES == 6
BO_BRIDGE_ORBIT = {bridge_act(fibre_action(h), c, ID4) for h, c in A_BO}
assert BO_BRIDGE_ORBIT == set(BRIDGES)
BO_ODD_H = {
    h for h in AUT_H
    if preserves_upart(fibre_action(h)) and block_swap(fibre_action(h)) == 1
}
BO_ODD_ORDERS = Counter(order(h) for h in BO_ODD_H)
assert BO_ODD_ORDERS == Counter({4: 4, 8: 4})
carrier_transpositions = [c for c in S4 if order(c) == 2 and parity(c) == 1]
assert len(carrier_transpositions) == 6
assert all(not any((h, c) in A_BO and order(h) <= 2 for h in AUT_H) for c in carrier_transpositions)
BO_SECTION_EXISTS = False

A_PART_ONLY = [
    (h, c) for h in AUT_H for c in S4
    if preserves_upart(fibre_action(h))
]
assert len(A_PART_ONLY) == 384
assert len({c for _, c in A_PART_ONLY}) == 24
assert all((ID8, c) in A_PART_ONLY for c in S4)
A_ONE_TUPLE = [
    (h, c) for h in AUT_H for c in S4
    if preserves_upart(fibre_action(h)) and block_swap(fibre_action(h)) == 0 and parity(c) == 0
]
assert len(A_ONE_TUPLE) == 96
assert len({c for _, c in A_ONE_TUPLE}) == 12

def normal_in(K, L):
    for l in L:
        li = inv(l)
        for k in K:
            if comp(comp(l, k), li) not in K:
                return False
    return True

index2_pairs = []
for L in H_SUBGROUPS:
    for K in H_SUBGROUPS:
        if K.issubset(L) and len(L) == 2 * len(K) and normal_in(K, L):
            split = any(order(x) == 2 for x in L if x not in K)
            index2_pairs.append((len(L), len(K), split))

nonsplit_c2 = Counter((lenL, lenK) for lenL, lenK, split in index2_pairs if not split)
assert nonsplit_c2 == Counter({(4, 2): 3, (8, 4): 6, (16, 8): 3})
assert not any((not split and lenK > 8) for _, lenK, split in index2_pairs)
MIN_NONSPLIT_CHOICE_INDEX = min(48 // lenK for _, lenK, split in index2_pairs if not split)
assert MIN_NONSPLIT_CHOICE_INDEX == 6
assert BO_CHOICE_STATES == MIN_NONSPLIT_CHOICE_INDEX

report = {
    "schema": "P000_Q18_HIDDEN_CARRIER_BRIDGE_CANONICALITY_CHECK_V1",
    "status": "PASS",
    "hard_target": "P000_HIDDEN_CARRIER_BRIDGE_CANONICALITY_AND_INFORMATION_COST_CLASSIFIED",
    "terminal_class": "WEAKER_CROSS_SORT_RELATION_SUFFICES_FOR_NONSPLIT_INTERNALIZATION",
    "derived_bridge_free": {
        "hidden_points": 8,
        "balance_triples": 8,
        "hidden_fibres": 4,
        "hidden_aut_order": 48,
        "hidden_fibre_image_order": 24,
        "hidden_fibre_kernel_order": 2,
        "carrier_axis_types": 6,
        "carrier_stars": 4,
        "carrier_aut_order": 24,
        "decoupled_aut_order": 1152,
    },
    "full_hidden_axis_bridge": {
        "bijection_choices": 24,
        "single_orbit": True,
        "fixed_choice_exists": False,
        "stabilizer_order": 48,
        "kernel_order": 2,
        "carrier_image_order": 24,
        "section_exists": False,
        "residue_census": "(AB)^4=z on all 96 lifted (3,2,4) pairs",
        "hartley_bits": math.log2(24),
        "fixed_length_binary_bits": 5,
    },
    "forgetful_candidates": {
        "pair_partition_bridge": {
            "choice_states": 6, "aut_order": 192, "kernel_order": 8,
            "carrier_image_order": 24, "section_exists": True,
        },
        "orientation_bridge": {
            "choice_states": 2, "aut_order": 576, "kernel_order": 24,
            "carrier_image_order": 24, "section_exists": True,
        },
    },
    "block_orientation_bridge": {
        "choice_states": 6,
        "hartley_bits": math.log2(6),
        "fixed_length_binary_bits": 3,
        "aut_order": 192,
        "kernel_order": 8,
        "carrier_image_order": 24,
        "section_exists": BO_SECTION_EXISTS,
        "block_swap_hidden_orders": dict(sorted(BO_ODD_ORDERS.items())),
        "full_bridge_orbit_under_stabilizer": 24,
        "encodes_full_bijection": False,
    },
    "block_orientation_deletions": {
        "delete_relation": {"aut_order": 1152, "carrier_image_order": 24, "section_exists": True},
        "forget_orientation_pairing_keep_hidden_partition": {"aut_order": 384, "carrier_image_order": 24, "section_exists": True},
        "delete_one_of_two_paired_tuples": {"aut_order": 96, "carrier_image_order": 12, "section_exists": False},
    },
    "information_lower_bound": {
        "hidden_subgroup_count": len(H_SUBGROUPS),
        "nonsplit_C2_extension_pairs_by_(L,K)": {f"{a}/{b}": n for (a, b), n in sorted(nonsplit_c2.items())},
        "minimum_choice_orbit_for_full_carrier_nonsplit": MIN_NONSPLIT_CHOICE_INDEX,
        "attained_by_block_orientation_bridge": True,
        "no_nonsplit_with_choice_orbit_below_6": True,
    },
    "interpretation": {
        "q15_full_bridge_canonical": False,
        "q15_exact_C2_extension_survives_pair_partition_forgetting": False,
        "raw_choice_cardinality_alone_determines_splitness": False,
        "weaker_alternative_is_canonical": False,
        "weaker_alternative_is_new_cross_sort_choice": True,
    },
    "method_reuse": [
        "T7_FINITE_SYMMETRY_EQUIVARIANCE",
        "T2_BLOCK_FINITE_CERTIFICATE",
        "Q15 exact HiddenBalance3 automorphism census",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
