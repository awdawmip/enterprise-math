#!/usr/bin/env python3
"""Deterministic checker for P000 Q18 hidden-carrier bridge canonicality.

Standard-library only.  The F_3^2-style names below are certificate labels for
Q15's already accepted 8-point presentation; no coordinate or group label is
used as primitive ontology.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from math import ceil, log2

def ident(n):
    return tuple(range(n))

def compose(p, q):
    """p after q."""
    return tuple(p[q[i]] for i in range(len(p)))

def inverse(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)

def power(p, n):
    out = ident(len(p))
    for _ in range(n):
        out = compose(p, out)
    return out

def perm_order(p):
    out = ident(len(p))
    for n in range(1, 100):
        out = compose(p, out)
        if out == ident(len(p)):
            return n
    raise AssertionError("order search bound exceeded")

def generated_subgroup(gens):
    I = ident(len(gens[0]))
    seen = {I}
    todo = deque([I])
    while todo:
        x = todo.popleft()
        for g in gens:
            y = compose(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen

POINTS = ("u+", "u-", "v+", "v-", "p+", "p-", "q+", "q-")
POINT_INDEX = {x: i for i, x in enumerate(POINTS)}
TRIPLE_NAMES = (
    ("v+", "u+", "p-"),
    ("v+", "p+", "q-"),
    ("v+", "q+", "u-"),
    ("v-", "u+", "q-"),
    ("v-", "p+", "u-"),
    ("v-", "q+", "p-"),
    ("u+", "p+", "q+"),
    ("u-", "q-", "p-"),
)
TRIPLES = {frozenset(POINT_INDEX[x] for x in t) for t in TRIPLE_NAMES}

# 1. Derive the hidden fibres internally from pair codegree.
pair_codegrees = {}
for a, b in combinations(range(8), 2):
    pair_codegrees[(a, b)] = sum(1 for T in TRIPLES if a in T and b in T)
codegree_histogram = Counter(pair_codegrees.values())
assert codegree_histogram == Counter({1: 24, 0: 4})
zero_pairs = [pair for pair, d in pair_codegrees.items() if d == 0]
FIBRES = [frozenset(pair) for pair in zero_pairs]
assert len(FIBRES) == 4
assert set().union(*FIBRES) == set(range(8))
assert sum(len(F) for F in FIBRES) == 8
FIBRE_INDEX = {F: i for i, F in enumerate(FIBRES)}

# 2. Enumerate primitive hidden automorphisms and their four-fibre action.
def image_set(S, p):
    return frozenset(p[i] for i in S)

AUT_H = []
for p in permutations(range(8)):
    if {image_set(T, p) for T in TRIPLES} == TRIPLES:
        AUT_H.append(p)
assert len(AUT_H) == 48

def quotient_perm(p):
    return tuple(
        FIBRE_INDEX[frozenset(p[x] for x in F)]
        for F in FIBRES
    )

S4 = list(permutations(range(4)))
I4 = ident(4)
I8 = ident(8)
quotient_image = {quotient_perm(g) for g in AUT_H}
assert quotient_image == set(S4)
quotient_kernel = [g for g in AUT_H if quotient_perm(g) == I4]
assert len(quotient_kernel) == 2
Z = next(g for g in quotient_kernel if g != I8)
for F in FIBRES:
    assert image_set(F, Z) == F
    assert all(Z[x] != x for x in F)

# 3. Full bridge space and the bridge-free product action.
# A bridge is a bijection f: hidden fibre index -> carrier-star index.
BRIDGES = S4[:]

def act_bridge(f, qg, h):
    # (g,h).f = h o f o q(g)^(-1)
    iq = inverse(qg)
    return tuple(h[f[iq[i]]] for i in range(4))

f0 = I4
bridge_orbit = {
    act_bridge(f0, quotient_perm(g), h)
    for g in AUT_H
    for h in S4
}
assert len(bridge_orbit) == 24
assert bridge_orbit == set(BRIDGES)

full_product_fixed = [
    f for f in BRIDGES
    if all(
        act_bridge(f, quotient_perm(g), h) == f
        for g in AUT_H
        for h in S4
    )
]
assert full_product_fixed == []

# Postcomposition by carrier S4 is free and transitive: the bridge set is a torsor.
for f in BRIDGES:
    images = {compose(h, f) for h in S4}
    assert images == set(BRIDGES)
    assert sum(1 for h in S4 if compose(h, f) == f) == 1

# The stabilizer of a chosen relative frame is exactly the Q15 48-element coupling.
def stabilizer_of_bridge(f):
    return [
        (g, h) for g in AUT_H for h in S4
        if act_bridge(f, quotient_perm(g), h) == f
    ]

for f in BRIDGES:
    stab = stabilizer_of_bridge(f)
    assert len(stab) == 48
    carrier_projection = {h for _, h in stab}
    kernel_to_carrier = [(g, h) for g, h in stab if h == I4]
    assert carrier_projection == set(S4)
    assert len(kernel_to_carrier) == 2

# 4. Recheck the Q15 nonsplit lift law for one bridge.
lift_by_q = defaultdict(list)
for g in AUT_H:
    lift_by_q[quotient_perm(g)].append(g)
assert all(len(lift_by_q[q]) == 2 for q in S4)

generator_pairs = []
for a in S4:
    if perm_order(a) != 3:
        continue
    for b in S4:
        if perm_order(b) != 2:
            continue
        if perm_order(compose(a, b)) != 4:
            continue
        if len(generated_subgroup([a, b])) != 24:
            continue
        generator_pairs.append((a, b))
assert len(generator_pairs) == 24

lift_checks = 0
for a, b in generator_pairs:
    for A in lift_by_q[a]:
        for B in lift_by_q[b]:
            lift_checks += 1
            assert power(compose(A, B), 4) == Z
assert lift_checks == 96

# 5. Exhaust the 4x4 binary cross-sort relation grammar modulo independent relabeling.
PAIR_ACTIONS = [(p, q) for p in S4 for q in S4]

def relation_mask(edges):
    mask = 0
    for i, j in edges:
        mask |= 1 << (4 * i + j)
    return mask

def transform_mask(mask, p, q):
    out = 0
    for i in range(4):
        for j in range(4):
            if (mask >> (4 * i + j)) & 1:
                out |= 1 << (4 * p[i] + q[j])
    return out

def relation_aut_stats(mask):
    L = [(p, q) for p, q in PAIR_ACTIONS if transform_mask(mask, p, q) == mask]
    hidden_proj = {p for p, _ in L}
    carrier_proj = {q for _, q in L}
    ker_to_carrier = sum(1 for p, q in L if q == I4)
    ker_to_hidden = sum(1 for p, q in L if p == I4)
    return {
        "order": len(L),
        "hidden_projection": len(hidden_proj),
        "carrier_projection": len(carrier_proj),
        "kernel_to_carrier": ker_to_carrier,
        "kernel_to_hidden": ker_to_hidden,
    }

visited = set()
orbit_representatives = []
for mask in range(1 << 16):
    if mask in visited:
        continue
    orbit = {transform_mask(mask, p, q) for p, q in PAIR_ACTIONS}
    visited.update(orbit)
    orbit_representatives.append(
        (mask, len(orbit), mask.bit_count(), relation_aut_stats(mask))
    )
assert len(visited) == 65536
assert len(orbit_representatives) == 317

full_projection_orbits = [
    row for row in orbit_representatives
    if row[3]["hidden_projection"] == 24
    and row[3]["carrier_projection"] == 24
]
assert len(full_projection_orbits) == 4
assert sorted(row[2] for row in full_projection_orbits) == [0, 4, 12, 16]

MATCH = relation_mask((i, i) for i in range(4))
ANTI_MATCH = ((1 << 16) - 1) ^ MATCH
assert relation_aut_stats(MATCH) == {
    "order": 24,
    "hidden_projection": 24,
    "carrier_projection": 24,
    "kernel_to_carrier": 1,
    "kernel_to_hidden": 1,
}
assert relation_aut_stats(ANTI_MATCH) == relation_aut_stats(MATCH)
# Complement is definitionally interrecoverable with matching.
assert (((1 << 16) - 1) ^ ANTI_MATCH) == MATCH

# Two genuinely weaker probes.
ONE_INCIDENCE = relation_mask([(0, 0)])
TWO_BLOCK = relation_mask(
    [(i, j) for i in (0, 1) for j in (0, 1)]
    + [(i, j) for i in (2, 3) for j in (2, 3)]
)
one_stats = relation_aut_stats(ONE_INCIDENCE)
block_stats = relation_aut_stats(TWO_BLOCK)
assert one_stats["carrier_projection"] == 6
assert one_stats["hidden_projection"] == 6
assert block_stats["carrier_projection"] == 8
assert block_stats["hidden_projection"] == 8
assert one_stats["carrier_projection"] < 24
assert block_stats["carrier_projection"] < 24

# Pulling a fibre-constant binary relation back through the 48->24 hidden action
# multiplies its quotient stabilizer and carrier-kernel by the hidden kernel size 2.
assert 2 * one_stats["order"] == 72
assert 2 * block_stats["order"] == 64
assert 2 * block_stats["kernel_to_carrier"] == 8

# 6. Exact information accounting.
relative_frame_choices = len(BRIDGES)
assert relative_frame_choices == 24
fixed_binary_bits = ceil(log2(relative_frame_choices))
assert fixed_binary_bits == 5

print("PASS / NO_NATURAL_HIDDEN_CARRIER_BRIDGE_WITH_EXACT_TORSOR_CERTIFICATE")
print(f"hidden_aut={len(AUT_H)} quotient_image={len(quotient_image)} quotient_kernel={len(quotient_kernel)}")
print(f"bridge_orbit={len(bridge_orbit)} full_product_fixed={len(full_product_fixed)} stabilizer={len(stabilizer_of_bridge(f0))}")
print(f"q15_324_pairs={len(generator_pairs)} lifted_nonsplit_checks={lift_checks}")
print(f"binary_relations=65536 independent_relabel_orbits={len(orbit_representatives)} full_projection_orbits={len(full_projection_orbits)} edge_counts={[x[2] for x in full_projection_orbits]}")
print(f"one_incidence_carrier_image={one_stats['carrier_projection']} two_block_carrier_image={block_stats['carrier_projection']}")
print(f"relative_frame_choices={relative_frame_choices} shannon_bits={log2(relative_frame_choices):.12f} fixed_binary_bits={fixed_binary_bits}")
