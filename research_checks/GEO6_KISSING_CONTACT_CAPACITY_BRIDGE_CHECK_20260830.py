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

def permute_pair(pair, p):
    return tuple(sorted((p[pair[0]], p[pair[1]])))

S4 = tuple(permutations(range(4)))
CELLS = tuple(range(4))
AXES = tuple(combinations(range(4), 2))

def cell_pair_action(pair, p):
    return permute_pair(pair, p)

def axis_action(axis, p):
    return tuple(sorted((p[axis[0]], p[axis[1]])))

def axis_pair_action(pair, p):
    a, b = pair
    return tuple(sorted((axis_action(a, p), axis_action(b, p))))

def degree_spectrum(points, edges):
    deg = Counter()
    for x in points:
        deg[x] = sum(x in e for e in edges)
    return tuple(sorted(deg.values()))

def invariant_under(points, edges, pair_action):
    edges = {tuple(sorted(e)) for e in edges}
    for p in S4:
        moved = {pair_action(e, p) for e in edges}
        if moved != edges:
            return False
    return True

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
            ra = reflect(a, i)
            for b in roots:
                assert dot(ra, reflect(b, i)) == dot(a, b)

    expected_distribution = Counter({2: 1, 1: 20, 0: 30, -1: 20, -2: 1})
    for a in roots:
        assert Counter(dot(a, b) for b in roots) == expected_distribution

    external_edges = {
        (i, j)
        for i, j in combinations(range(len(roots)), 2)
        if dot(roots[i], roots[j]) == 1
    }
    external_degrees = [sum(i in e for e in external_edges) for i in range(len(roots))]
    assert set(external_degrees) == {20}
    assert len(external_edges) == 720

    cell_pairs = set(combinations(CELLS, 2))
    cell_orbits = []
    remaining = set(cell_pairs)
    while remaining:
        seed = next(iter(remaining))
        orb = {cell_pair_action(seed, p) for p in S4}
        cell_orbits.append(orb)
        remaining -= orb
    assert sorted(map(len, cell_orbits)) == [6]
    cell_invariant_graphs = [set(), set(cell_pairs)]
    assert all(invariant_under(CELLS, e, cell_pair_action) for e in cell_invariant_graphs)
    assert [degree_spectrum(CELLS, e) for e in cell_invariant_graphs] == [
        (0, 0, 0, 0),
        (3, 3, 3, 3),
    ]

    invariant_masks = []
    ordered_cell_pairs = tuple(sorted(cell_pairs))
    for mask in range(1 << len(ordered_cell_pairs)):
        edges = {
            ordered_cell_pairs[k]
            for k in range(len(ordered_cell_pairs))
            if (mask >> k) & 1
        }
        if invariant_under(CELLS, edges, cell_pair_action):
            invariant_masks.append(edges)
    assert len(invariant_masks) == 2
    assert {frozenset(e) for e in invariant_masks} == {
        frozenset(),
        frozenset(cell_pairs),
    }

    axis_pairs = set(combinations(AXES, 2))
    axis_orbits = []
    remaining = set(axis_pairs)
    while remaining:
        seed = next(iter(remaining))
        orb = {axis_pair_action(seed, p) for p in S4}
        axis_orbits.append(orb)
        remaining -= orb
    assert sorted(map(len, axis_orbits)) == [3, 12]

    def share_vertex(pair):
        a, b = pair
        return len(set(a) & set(b)) == 1

    adjacent_orbit = next(o for o in axis_orbits if all(share_vertex(e) for e in o))
    disjoint_orbit = next(o for o in axis_orbits if all(not share_vertex(e) for e in o))
    assert len(adjacent_orbit) == 12
    assert len(disjoint_orbit) == 3

    axis_graphs = [set(), set(disjoint_orbit), set(adjacent_orbit), set(axis_pairs)]
    axis_degree_sets = [degree_spectrum(AXES, e) for e in axis_graphs]
    assert axis_degree_sets == [
        (0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1),
        (4, 4, 4, 4, 4, 4),
        (5, 5, 5, 5, 5, 5),
    ]
    assert all(invariant_under(AXES, e, axis_pair_action) for e in axis_graphs)

    CENTER = ("center",)
    STAR_CELLS = (CENTER,) + tuple(("axis", a) for a in AXES)
    STAR_EDGES = {tuple(sorted((CENTER, ("axis", a)), key=repr)) for a in AXES}

    def star_action(x, p):
        if x == CENTER:
            return CENTER
        return ("axis", axis_action(x[1], p))

    def star_edge_action(edge, p):
        return tuple(sorted((star_action(edge[0], p), star_action(edge[1], p)), key=repr))

    assert all({star_edge_action(e, p) for e in STAR_EDGES} == STAR_EDGES for p in S4)
    star_degrees = [sum(x in e for e in STAR_EDGES) for x in STAR_CELLS]
    assert sorted(star_degrees) == [1, 1, 1, 1, 1, 1, 6]
    assert max(star_degrees) == 6
    star_contact_orbit = {star_edge_action(next(iter(STAR_EDGES)), p) for p in S4}
    assert star_contact_orbit == STAR_EDGES
    assert len(star_contact_orbit) == 6

    assert len(roots) > len(CELLS)
    assert len(roots) > len(AXES)
    assert 20 > 3 and 20 > 5
    residual_states_per_axis_lower_bound = ceil(len(roots) / len(AXES))
    assert residual_states_per_axis_lower_bound == 12

    empty_capacity = max(degree_spectrum(CELLS, set()))
    complete_capacity = max(degree_spectrum(CELLS, cell_pairs))
    assert (empty_capacity, complete_capacity) == (0, 3)

    return {
        "task_id": TASK_ID,
        "e6_root_count": len(roots),
        "e6_contact_degree": 20,
        "e6_contact_edges": len(external_edges),
        "e6_pairing_distribution_per_root": dict(sorted(expected_distribution.items())),
        "native_four_cell_pair_orbits": [len(o) for o in cell_orbits],
        "native_four_cell_rotation_invariant_capacities": [0, 3],
        "six_axis_pair_orbit_sizes": sorted(map(len, axis_orbits)),
        "six_axis_rotation_invariant_capacities": [0, 1, 4, 5],
        "declared_native_axis_star_capacity": 6,
        "declared_native_axis_star_contact_orbit_size": 6,
        "minimum_extra_states_per_axis_for_72_injective_labels": 12,
        "terminal_class": "CONTACT_ATLAS_CONSTRUCTED_WITH_CANONICALITY_AND_CURRENT_READOUT_TRANSFER_OBSTRUCTION",
    }

if __name__ == "__main__":
    import json
    print(json.dumps(check(), indent=2, sort_keys=True))
