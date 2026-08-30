#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, deque
from itertools import combinations, permutations
from math import ceil

TASK_ID = "RS-GEO6-KISSING-CONTACT-CAPACITY-BRIDGE"

G = (
    (2, 0, -1, 0, 0, 0),
    (0, 2, 0, -1, 0, 0),
    (-1, 0, 2, -1, 0, 0),
    (0, -1, -1, 2, -1, 0),
    (0, 0, 0, -1, 2, -1),
    (0, 0, 0, 0, -1, 2),
)

def mat_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M)))

def dot(u, v):
    Gv = mat_vec(G, v)
    return sum(u[i] * Gv[i] for i in range(6))

def reflect(v, i):
    gv = mat_vec(G, v)
    out = list(v)
    out[i] -= gv[i]
    return tuple(out)

def generate_e6_roots():
    start = (1, 0, 0, 0, 0, 0)
    roots = {start}
    q = deque([start])
    while q:
        v = q.popleft()
        for i in range(6):
            w = reflect(v, i)
            if w not in roots:
                roots.add(w)
                q.append(w)
    return tuple(sorted(roots))

S4 = tuple(permutations(range(4)))
CELLS = tuple(range(4))
AXES = tuple(combinations(range(4), 2))

def cell_pair_action(pair, p):
    return tuple(sorted((p[pair[0]], p[pair[1]])))

def axis_action(axis, p):
    return tuple(sorted((p[axis[0]], p[axis[1]])))

def axis_pair_action(pair, p):
    a, b = pair
    return tuple(sorted((axis_action(a, p), axis_action(b, p))))

def degree_spectrum(points, edges):
    return tuple(sorted(sum(x in e for e in edges) for x in points))

def invariant_under(edges, pair_action):
    edges = {tuple(sorted(e)) for e in edges}
    return all({pair_action(e, p) for e in edges} == edges for p in S4)

def check():
    roots = generate_e6_roots()
    assert len(roots) == 72
    assert all(dot(r, r) == 2 for r in roots)
    rootset = set(roots)
    for r in roots:
        for i in range(6):
            assert reflect(r, i) in rootset
    for i in range(6):
        for a in roots:
            for b in roots:
                assert dot(reflect(a, i), reflect(b, i)) == dot(a, b)

    expected = Counter({2: 1, 1: 20, 0: 30, -1: 20, -2: 1})
    for a in roots:
        assert Counter(dot(a, b) for b in roots) == expected

    external_edges = {
        (i, j)
        for i, j in combinations(range(len(roots)), 2)
        if dot(roots[i], roots[j]) == 1
    }
    assert {sum(i in e for e in external_edges) for i in range(len(roots))} == {20}
    assert len(external_edges) == 720

    cell_pairs = set(combinations(CELLS, 2))
    cell_orbit = {cell_pair_action(next(iter(cell_pairs)), p) for p in S4}
    assert cell_orbit == cell_pairs
    invariant_cell_graphs = []
    ordered_cell_pairs = tuple(sorted(cell_pairs))
    for mask in range(1 << len(ordered_cell_pairs)):
        edges = {
            ordered_cell_pairs[k]
            for k in range(len(ordered_cell_pairs))
            if (mask >> k) & 1
        }
        if invariant_under(edges, cell_pair_action):
            invariant_cell_graphs.append(edges)
    assert {frozenset(e) for e in invariant_cell_graphs} == {
        frozenset(),
        frozenset(cell_pairs),
    }
    assert sorted(max(degree_spectrum(CELLS, e)) for e in invariant_cell_graphs) == [0, 3]

    axis_pairs = set(combinations(AXES, 2))
    axis_orbits = []
    remaining = set(axis_pairs)
    while remaining:
        seed = next(iter(remaining))
        orb = {axis_pair_action(seed, p) for p in S4}
        axis_orbits.append(orb)
        remaining -= orb
    assert sorted(map(len, axis_orbits)) == [3, 12]

    def incident(pair):
        a, b = pair
        return len(set(a) & set(b)) == 1

    incident_orbit = next(o for o in axis_orbits if all(incident(e) for e in o))
    disjoint_orbit = next(o for o in axis_orbits if all(not incident(e) for e in o))
    assert (len(disjoint_orbit), len(incident_orbit)) == (3, 12)

    axis_graphs = [
        set(),
        set(disjoint_orbit),
        set(incident_orbit),
        set(axis_pairs),
    ]
    assert [degree_spectrum(AXES, e) for e in axis_graphs] == [
        (0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1),
        (4, 4, 4, 4, 4, 4),
        (5, 5, 5, 5, 5, 5),
    ]
    assert all(invariant_under(e, axis_pair_action) for e in axis_graphs)

    center = ("center",)
    star_cells = (center,) + tuple(("axis", a) for a in AXES)
    star_edges = {frozenset((center, ("axis", a))) for a in AXES}

    def star_action(x, p):
        return center if x == center else ("axis", axis_action(x[1], p))

    def star_edge_action(e, p):
        return frozenset(star_action(x, p) for x in e)

    assert all({star_edge_action(e, p) for e in star_edges} == star_edges for p in S4)
    star_degrees = tuple(sorted(sum(x in e for e in star_edges) for x in star_cells))
    assert star_degrees == (1, 1, 1, 1, 1, 1, 6)
    star_edge = next(iter(star_edges))
    assert {star_edge_action(star_edge, p) for p in S4} == star_edges

    residual = ceil(len(roots) / len(AXES))
    assert residual == 12
    assert 72 > 7 and 72 > 6 and 72 > 4
    assert 20 > 6 and 20 > 5 and 20 > 3

    return {
        "task_id": TASK_ID,
        "e6_root_count": 72,
        "e6_contact_degree": 20,
        "e6_contact_edges": 720,
        "e6_pairing_distribution_per_root": dict(sorted(expected.items())),
        "native_four_cell_rotation_invariant_capacities": [0, 3],
        "six_axis_pair_orbit_sizes": [3, 12],
        "six_axis_rotation_invariant_capacities": [0, 1, 4, 5],
        "declared_native_axis_star_capacity": 6,
        "declared_native_axis_star_contact_orbit_size": 6,
        "minimum_extra_states_per_axis_for_72_injective_labels": 12,
        "terminal_class": "CONTACT_ATLAS_CONSTRUCTED_WITH_CANONICALITY_AND_CURRENT_READOUT_TRANSFER_OBSTRUCTION",
    }

if __name__ == "__main__":
    import json
    print(json.dumps(check(), indent=2, sort_keys=True))
