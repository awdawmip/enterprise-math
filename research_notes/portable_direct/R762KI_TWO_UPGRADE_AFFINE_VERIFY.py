#!/usr/bin/env python3
"""Exact R762KI proof checker: 28 two-upgrade four-point affine obstructions.
Unsigned six-axis Port--Euler observer; standard-library integer arithmetic.
"""
from itertools import combinations, permutations
from collections import Counter
import json

missing_ports = {(0, 1), (2, 3), (4, 5)}
ports = [p for p in combinations(range(6), 2) if p not in missing_ports]
positions = {p: i for i, p in enumerate(ports)}
supports = list(combinations(range(6), 3))
edges = {s: list(combinations([positions[p] for p in combinations(s, 2)
                               if p in positions], 2)) for s in supports}
forced = [s for s in supports if len(edges[s]) == 1]
flexible = [s for s in supports if len(edges[s]) == 3]
assert len(ports) == 12 and len(forced) == 12 and len(flexible) == 8

parent = list(range(12))
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i
for s in forced:
    u, v = edges[s][0]
    a, b = find(u), find(v)
    parent[a] = b
roots = sorted({find(i) for i in range(12)})
component = {i: roots.index(find(i)) for i in range(12)}
assert Counter(component.values()) == Counter({0: 4, 1: 4, 2: 4})

def boundary(e):
    return (1 << e[0]) ^ (1 << e[1])

def type_bit(e):
    pair = frozenset((component[e[0]], component[e[1]]))
    return {frozenset((0, 1)): 1,
            frozenset((0, 2)): 2,
            frozenset((1, 2)): 4}[pair]

def choices(s, count):
    inds = ((i,) for i in range(3)) if count == 1 else (
        (i, j) for i in range(3) for j in range(i, 3))
    out = set()
    for row in inds:
        b, t = 0, 0
        for i in row:
            e = edges[s][i]
            b ^= boundary(e)
            t |= type_bit(e)
        out.add((b, t))
    assert len(out) == (3 if count == 1 else 6)
    return out

opt = {(s, count): choices(s, count)
       for s in flexible for count in (1, 2)}
force_targets = {0}
for s in forced:
    e = boundary(edges[s][0])
    force_targets |= {x ^ e for x in tuple(force_targets)}
assert len(force_targets) == 512

def reachable(upgraded):
    states = {(0, 0)}
    for j, s in enumerate(flexible):
        loc = opt[s, 2 if j in upgraded else 1]
        states = {(x ^ y, u | v) for x, u in states for y, v in loc}
    connected = {x for x, t in states if t.bit_count() >= 2}
    parity_only = {x for x, _ in states}
    assert (parity_only & force_targets) == (connected & force_targets)
    return connected & force_targets

base_holes = force_targets - reachable(set())
assert len(base_holes) == 47
single_holes = [force_targets - reachable({i}) for i in range(8)]
assert all(len(x) == 17 and x <= base_holes for x in single_holes)

def hamming_distance(a, b):
    return sum((set(a) & set(p)) != (set(b) & set(p))
               for p in sorted(missing_ports))

def name(s):
    return ''.join(map(str, s))

pairs = {}
for i, j in combinations(range(8), 2):
    holes = sorted(force_targets - reachable({i, j}))
    assert len(holes) == 4
    assert holes[0] ^ holes[1] ^ holes[2] ^ holes[3] == 0
    assert set(holes) <= base_holes
    pairs[(i, j)] = holes
assert len(pairs) == 28
assert len(set(x for row in pairs.values() for x in row)) == 47

H = [p for p in permutations(range(6))
     if {tuple(sorted((p[i], p[j]))) for i, j in missing_ports} == missing_ports]
assert len(H) == 48
flex_idx = {s: i for i, s in enumerate(flexible)}

def transform_index(j, perm):
    return flex_idx[tuple(sorted(perm[i] for i in flexible[j]))]

def transform_boundary(b, perm):
    result = 0
    for k, port in enumerate(ports):
        if b & (1 << k):
            new_port = tuple(sorted((perm[port[0]], perm[port[1]])))
            result ^= 1 << positions[new_port]
    return result

representative = {}
for (i, j), holes in pairs.items():
    representative.setdefault(hamming_distance(flexible[i], flexible[j]),
                              ((i, j), holes))
assert set(representative) == {1, 2, 3}
for (i, j), holes in pairs.items():
    d = hamming_distance(flexible[i], flexible[j])
    (a, b), base = representative[d]
    assert any({transform_index(a, perm), transform_index(b, perm)} == {i, j}
               and {transform_boundary(x, perm) for x in base} == set(holes)
               for perm in H)

sizes = Counter(hamming_distance(flexible[i], flexible[j]) for i, j in pairs)
assert sizes == Counter({1: 12, 2: 12, 3: 4})
report = {
    "schema": "R762KI_TWO_UPGRADE_AFFINE_EXCEPTIONS_V1",
    "model": "auxiliary unsigned Port-Euler, inactive 01,23,45",
    "ports": [name(p) for p in ports],
    "flexible": [name(s) for s in flexible],
    "forced_boundary_targets": len(force_targets),
    "no_upgrades_unreachable": len(base_holes),
    "one_upgrade_unreachable_each": 17,
    "two_upgrades_unreachable_each": 4,
    "two_upgrade_pairs": len(pairs),
    "all_28_exceptions_are_affine_2_flats": True,
    "union_all_two_upgrade_exceptions_equals_no_upgrade_exceptions": True,
    "symmetry_group_order": len(H),
    "cube_distance_pair_orbit_sizes": {str(k): v for k, v in sorted(sizes.items())},
    "three_templates": {str(d): {"upgraded": [name(flexible[i]) for i in pair],
                                "four_missing_boundaries": holes}
                        for d, (pair, holes) in sorted(representative.items())},
    "all_28_exact_missing_sets": {name(flexible[i])+"+"+name(flexible[j]): holes
                                  for (i, j), holes in pairs.items()},
    "proof_scope": "exact finite parity-and-connectivity in minimum 1/2 flexible palette",
    "independent_review": "NOT_REVIEWED"
}
print(json.dumps(report, indent=2))
