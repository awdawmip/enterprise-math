#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
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

def preserves_tri(p, rel):
    return frozenset(tuple(sorted(p[i] for i in t)) for t in rel) == rel

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
FIBRES = tuple(sorted(
    (tuple(sorted(pair)) for pair, d in codeg.items() if d == 0),
    key=lambda x: x
))
assert len(FIBRES) == 4
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
assert {fibre_action(h) for h in AUT_H} == set(S4)
H_KERNEL = tuple(h for h in AUT_H if fibre_action(h) == ID4)
assert len(H_KERNEL) == 2
z = next(h for h in H_KERNEL if h != ID8)

def parity(p):
    n = 0
    for i in range(4):
        for j in range(i + 1, 4):
            n += p[i] > p[j]
    return n % 2

def bridge_act(hq, c, b):
    return comp(c, comp(b, inv(hq)))

def canon_partition(block):
    block = frozenset(block)
    other = frozenset(set(range(4)) - set(block))
    return frozenset((block, other))

PARTITIONS = tuple(sorted(
    {canon_partition(b) for b in itertools.combinations(range(4), 2)},
    key=lambda P: sorted(tuple(sorted(B)) for B in P)
))
PI = {P: i for i, P in enumerate(PARTITIONS)}
assert len(PARTITIONS) == 3

def block_order(P):
    return tuple(sorted(tuple(sorted(B)) for B in P))

def part_image(p, P):
    return frozenset(frozenset(p[i] for i in B) for B in P)

def partition_delta(p, P):
    B0, _ = block_order(P)
    P2 = part_image(p, P)
    C0, _ = block_order(P2)
    imB0 = tuple(sorted(p[i] for i in B0))
    return 0 if imB0 == C0 else 1

def bo_act(hq, c, state):
    pidx, eps = state
    P = PARTITIONS[pidx]
    P2 = part_image(hq, P)
    return (PI[P2], eps ^ partition_delta(hq, P) ^ parity(c))

G0 = tuple((h, c) for h in AUT_H for c in S4)
assert len(G0) == 1152

def gmul(g1, g2):
    return (comp(g1[0], g2[0]), comp(g1[1], g2[1]))

def ginv(g):
    return (inv(g[0]), inv(g[1]))

X24 = S4
X6 = tuple((i, e) for i in range(3) for e in (0, 1))
x24 = ID4
x6 = (PI[canon_partition((0, 1))], 0)

def act24(g, x):
    return bridge_act(fibre_action(g[0]), g[1], x)

def act6(g, x):
    return bo_act(fibre_action(g[0]), g[1], x)

def perm_on(space, act, g):
    ix = {x: i for i, x in enumerate(space)}
    return tuple(ix[act(g, x)] for x in space)

def analyze(space, x0, act):
    orbit = {act(g, x0) for g in G0}
    assert orbit == set(space)
    stab = tuple(g for g in G0 if act(g, x0) == x0)
    kernel = tuple(g for g in G0 if all(act(g, x) == x for x in space))
    image = {perm_on(space, act, g) for g in G0}
    iso_image = {perm_on(space, act, g) for g in stab}
    assert len(image) == len(G0) // len(kernel)
    assert len(iso_image) == len(stab) // len(kernel)

    one = (ID8, ID4)
    assert all(act(one, x) == x for x in space)
    for g in G0[::31]:
        gi = ginv(g)
        for x in space:
            assert act(gi, act(g, x)) == x
    for g1 in G0[::37]:
        for g2 in G0[::41]:
            gg = gmul(g1, g2)
            for x in space:
                assert act(gg, x) == act(g1, act(g2, x))

    loops = {g for g in G0 if act(g, x0) == x0}
    assert loops == set(stab)

    g_out = next(g for g in G0 if act(g, x0) != x0)
    x1 = act(g_out, x0)
    assert x1 != x0
    for a in stab:
        k = gmul(a, ginv(g_out))
        assert act(k, x1) == x0
        assert gmul(k, g_out) == a

    reps = {}
    for r in G0:
        reps.setdefault(act(r, x0), r)
    for y, r in reps.items():
        stab_y = {g for g in G0 if act(g, y) == y}
        conj = {gmul(gmul(r, a), ginv(r)) for a in stab}
        assert stab_y == conj

    return {
        "choice_states": len(space),
        "orbit_size": len(orbit),
        "stabilizer_order": len(stab),
        "global_action_kernel_order": len(kernel),
        "effective_action_order": len(image),
        "effective_loop_transport_order": len(iso_image),
        "effective_loop_transport_order_histogram": dict(sorted(Counter(order(p) for p in iso_image).items())),
        "minimum_nonidentity_automorphism_loop_length": 1,
        "minimum_distinct_intermediate_state_loop_length": 2,
        "every_two_step_loop_residue_exhausts_static_stabilizer": True,
        "basepoint_gauge_is_stabilizer_conjugacy": True,
    }

A24 = analyze(X24, x24, act24)
A6 = analyze(X6, x6, act6)

assert A24["choice_states"] == 24
assert A24["stabilizer_order"] == 48
assert A24["global_action_kernel_order"] == 2
assert A24["effective_action_order"] == 576
assert A24["effective_loop_transport_order"] == 24
assert A24["effective_loop_transport_order_histogram"] == {1: 1, 2: 9, 3: 8, 4: 6}

assert A6["choice_states"] == 6
assert A6["stabilizer_order"] == 192
assert A6["global_action_kernel_order"] == 24
assert A6["effective_action_order"] == 48
assert A6["effective_loop_transport_order"] == 8
assert A6["effective_loop_transport_order_histogram"] == {1: 1, 2: 5, 4: 2}

def generated4(gs):
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
    if order(a) == 3 and order(b) == 2
    and order(comp(a, b)) == 4
    and len(generated4((a, b))) == 24
]
assert len(qpairs) == 24

full_stab = tuple(g for g in G0 if act24(g, x24) == x24)
full_lifts = {c: [h for h in AUT_H if (h, c) in full_stab] for c in S4}
assert all(len(v) == 2 for v in full_lifts.values())
full_residue = Counter()
for a, b in qpairs:
    for A in full_lifts[a]:
        for B in full_lifts[b]:
            full_residue[power(comp(A, B), 4)] += 1
assert full_residue == Counter({z: 96})

bo_stab = tuple(g for g in G0 if act6(g, x6) == x6)
bo_lifts = {c: [h for h in AUT_H if (h, c) in bo_stab] for c in S4}
assert all(len(v) == 8 for v in bo_lifts.values())
bo_residue = Counter()
for a, b in qpairs:
    for A in bo_lifts[a]:
        for B in bo_lifts[b]:
            bo_residue[power(comp(A, B), 4)] += 1
assert bo_residue == Counter({ID8: 768, z: 768})

report = {
    "schema": "P000_Q21_HIDDEN_COUPLING_TORSOR_TRANSPORT_CHECK_V1",
    "status": "PASS",
    "hard_target": "P000_HIDDEN_COUPLING_TORSOR_TRANSPORT_OR_NO_NEW_INVARIANT_CLASSIFIED",
    "terminal_class": "TORSOR_TRANSPORT_REDUCES_TO_STATIC_Q18_DATA",
    "primitive_change_group_order": len(G0),
    "full_bridge_24_state_action_groupoid": A24,
    "block_orientation_6_state_action_groupoid": A6,
    "reduction_theorem": {
        "transitive_action_groupoid_equivalent_to_static_isotropy": True,
        "path_difference_with_same_endpoints_is_stabilizer_element": True,
        "basepoint_change_conjugates_stabilizer": True,
        "new_gauge_invariant_loop_datum_beyond_Q18_static_action": False,
        "continuation_killed_by_minimum_sufficient_abstraction_gate": True,
    },
    "carrier_relation_loop_residue": {
        "word": "(A B)^4 for carrier (3,2,4) generating pairs",
        "generating_pairs": len(qpairs),
        "full_bridge_lifts_per_carrier_element": 2,
        "full_bridge_total_lift_pairs": 96,
        "full_bridge_residue": {"z": 96},
        "block_orientation_lifts_per_carrier_element": 8,
        "block_orientation_total_lift_pairs": 1536,
        "block_orientation_residue": {"identity": 768, "z": 768},
        "interpretation": "STATIC_EXTENSION_RESIDUE_ONLY_NOT_CHOICE_HOLONOMY",
    },
    "q12_comparison_gate": {
        "triggered": False,
        "reason": "No new gauge-invariant coupling-choice holonomy survives reduction; the only nontrivial loop residues are already internal to Q18 stabilizer/kernel extension data.",
    },
    "ontology_boundary": {
        "no_bare_P000_group_name_promotion": True,
        "no_bundle_sheaf_stack_connection_promotion": True,
        "certificate_groups_are_finite_presentations_only": True,
    },
}
print("PASS P000_Q21_HIDDEN_COUPLING_TORSOR_TRANSPORT")
print(json.dumps(report, sort_keys=True))
