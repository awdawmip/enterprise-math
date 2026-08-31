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
FIBRES = tuple(
    sorted(
        (tuple(sorted(pair)) for pair, d in codeg.items() if d == 0),
        key=lambda x: x,
    )
)
assert len(FIBRES) == 4
FIBRE_OF = {}
for s, f in enumerate(FIBRES):
    for x in f:
        FIBRE_OF[x] = s

AUT_H = tuple(
    p for p in itertools.permutations(range(8))
    if preserves_tri(p, BAL)
)
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

def parity(p):
    n = 0
    for i in range(4):
        for j in range(i + 1, 4):
            n += p[i] > p[j]
    return n % 2

def bridge_act(hq, c, b):
    return comp(c, comp(b, inv(hq)))

BLOCK0 = frozenset((0, 1))
BLOCK1 = frozenset((2, 3))
UPART = frozenset((BLOCK0, BLOCK1))

def preserves_upart(p):
    return frozenset(
        (frozenset(p[i] for i in BLOCK0), frozenset(p[i] for i in BLOCK1))
    ) == UPART

def block_swap(p):
    im0 = frozenset(p[i] for i in BLOCK0)
    if im0 == BLOCK0:
        return 0
    if im0 == BLOCK1:
        return 1
    raise AssertionError("not in partition stabilizer")

G = tuple((h, c) for h in AUT_H for c in S4)
E = (ID8, ID4)
assert len(G) == 1152

def gcomp(x, y):
    return (comp(x[0], y[0]), comp(x[1], y[1]))

def ginv(x):
    return (inv(x[0]), inv(x[1]))

def gorder(x):
    r = E
    for n in range(1, 100):
        r = gcomp(r, x)
        if r == E:
            return n
    raise AssertionError("group order bound")

A24 = frozenset(
    (h, c) for h, c in G
    if bridge_act(fibre_action(h), c, ID4) == ID4
)
assert len(A24) == 48
assert len({c for _, c in A24}) == 24
assert len({h for h, c in A24 if c == ID4}) == 2

A6 = frozenset(
    (h, c) for h, c in G
    if preserves_upart(fibre_action(h))
    and block_swap(fibre_action(h)) == parity(c)
)
assert len(A6) == 192
assert len({c for _, c in A6}) == 24
assert len({h for h, c in A6 if c == ID4}) == 8

def left_coset(g, A):
    return frozenset(gcomp(g, a) for a in A)

def cosets(A):
    remaining = set(G)
    rows = []
    while remaining:
        rep = min(remaining)
        C = left_coset(rep, A)
        rows.append((rep, C))
        remaining.difference_update(C)
    return tuple(rows)

def coset_index(rows):
    out = {}
    for i, (_, C) in enumerate(rows):
        for x in C:
            assert x not in out
            out[x] = i
    assert len(out) == len(G)
    return out

def conjugate_subgroup(g, A):
    gi = ginv(g)
    return frozenset(gcomp(gcomp(g, a), gi) for a in A)

def analyze(A, expected_states, expected_stabilizer, expected_kernel):
    rows = cosets(A)
    index = coset_index(rows)
    assert len(rows) == expected_states
    assert all(len(C) == expected_stabilizer for _, C in rows)

    ref_index = index[E]
    assert ref_index == 0
    ref_rep = rows[ref_index][0]

    # Exact action-groupoid stabilizer law at every object.  The action of k
    # on the coset represented by r lands in the coset containing k*r.
    for i, (rep, _) in enumerate(rows):
        Stab = frozenset(k for k in G if index[gcomp(k, rep)] == i)
        assert len(Stab) == expected_stabilizer
        assert Stab == conjugate_subgroup(rep, A)

    # Every ordered object pair has |A| primitive-preserving arrows.
    hom_counts = []
    for i, (rx, _) in enumerate(rows):
        counts = Counter(index[gcomp(k, rx)] for k in G)
        assert set(counts) == set(range(len(rows)))
        assert set(counts.values()) == {expected_stabilizer}
        hom_counts.extend(counts.values())
    assert set(hom_counts) == {expected_stabilizer}

    # Choose one genuine state-changing primitive arrow from the reference.
    g = next(g for g in G if index[gcomp(g, ref_rep)] != ref_index)
    y_index = index[gcomp(g, ref_rep)]
    assert y_index != ref_index

    # Every static isotropy element is realized by a two-edge excursion:
    # ref --g--> y --(a*g^-1)--> ref.  Thus loops select no proper
    # path-dependent subset beyond the already-known stabilizer.
    gi = ginv(g)
    composites = set()
    for a in A:
        second = gcomp(a, gi)
        assert index[gcomp(second, gcomp(g, ref_rep))] == ref_index
        assert gcomp(second, g) == a
        composites.add(gcomp(second, g))
    assert composites == set(A)

    # Nontrivial explicit length-2 loop.
    a = next(a for a in sorted(A) if a != E and gorder(a) == 2)
    second = gcomp(a, gi)
    assert index[gcomp(second, gcomp(g, ref_rep))] == ref_index
    assert gcomp(second, g) == a != E

    # Loop acts trivially on choice object; gauge move only conjugates isotropy.
    assert index[gcomp(a, ref_rep)] == ref_index

    return {
        "choice_states": len(rows),
        "group_order": len(G),
        "stabilizer_order": len(A),
        "kernel_order": expected_kernel,
        "groupoid_arrow_count": len(G) * len(rows),
        "loop_arrow_count": len(rows) * len(A),
        "hom_count_between_each_ordered_pair": expected_stabilizer,
        "all_static_isotropy_realizable_by_two_edge_excursion": True,
        "closed_path_product_exactly_stabilizer": True,
        "gauge_change_is_stabilizer_conjugacy": True,
        "choice_object_loop_action": "IDENTITY_ON_BASE_CHOICE",
        "reference_state_index": ref_index,
        "excursion_state_index": y_index,
        "minimal_state_changing_loop_length": 2,
        "example_excursion": {
            "first_arrow": {
                "hidden_perm8": list(g[0]),
                "hidden_fibre_perm4": list(fibre_action(g[0])),
                "carrier_perm4": list(g[1]),
                "order": gorder(g),
            },
            "second_arrow": {
                "hidden_perm8": list(second[0]),
                "hidden_fibre_perm4": list(fibre_action(second[0])),
                "carrier_perm4": list(second[1]),
                "order": gorder(second),
            },
            "composite_isotropy": {
                "hidden_perm8": list(a[0]),
                "hidden_fibre_perm4": list(fibre_action(a[0])),
                "carrier_perm4": list(a[1]),
                "order": gorder(a),
            },
        },
    }

R24 = analyze(A24, 24, 48, 2)
R6 = analyze(A6, 6, 192, 8)

# Exact reduction theorem instantiated twice.
assert R24["loop_arrow_count"] == len(G)
assert R6["loop_arrow_count"] == len(G)
assert R24["all_static_isotropy_realizable_by_two_edge_excursion"]
assert R6["all_static_isotropy_realizable_by_two_edge_excursion"]

report = {
    "schema": "P000_Q21_HIDDEN_COUPLING_TORSOR_TRANSPORT_CHECK_V1",
    "status": "PASS",
    "hard_target": "P000_HIDDEN_COUPLING_TORSOR_TRANSPORT_OR_NO_NEW_INVARIANT_CLASSIFIED",
    "terminal_class": "TORSOR_TRANSPORT_REDUCES_TO_STATIC_Q18_DATA",
    "primitive_change_group": {
        "description": "Aut(HiddenBalance3) x induced carrier S4, using the exact Q18 bridge-free primitive automorphisms",
        "order": len(G),
        "hidden_order": len(AUT_H),
        "carrier_order": len(S4),
    },
    "full_bridge_24_state_groupoid": R24,
    "block_orientation_6_state_groupoid": R6,
    "reduction_theorem": {
        "path_composition": "Every legal path composes to one element g of the same primitive change group G.",
        "closed_loop_criterion": "A path at object x is closed iff its composite lies in Stab_G(x).",
        "two_edge_surjectivity": "For any a in Stab_G(x) and any state-changing g, the loop g then a*g^-1 has composite a.",
        "gauge_rule": "Changing base object by k conjugates Stab_G(x) to k Stab_G(x) k^-1.",
        "consequence": "The action groupoid is a transitive presentation of the already-known stabilizer; no proper holonomy subset, cocycle, or path residue is selected without adding extra non-primitive path/connection data.",
    },
    "comparison": {
        "same_transport_pattern": True,
        "24_state_difference": "static stabilizer order 48, carrier kernel 2",
        "6_state_difference": "static stabilizer order 192, carrier kernel 8",
        "choice_cardinality_creates_new_path_invariant": False,
    },
    "continuation_gate": {
        "new_loop_invariant_found": False,
        "extra_legal_model_change_generators_supplied_by_Q18": False,
        "inventing_extra_arrows_allowed": False,
        "kill_transport_upgrade": True,
    },
    "method_reuse": [
        "Q18 exact HiddenBalance3 automorphism census",
        "Q18 full bridge stabilizer",
        "Q18 BlockOrientationBridge stabilizer",
        "T7_FINITE_SYMMETRY_EQUIVARIANCE",
        "T2_BLOCK_FINITE_CERTIFICATE",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
