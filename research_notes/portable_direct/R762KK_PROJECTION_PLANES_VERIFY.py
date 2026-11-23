#!/usr/bin/env python3
"""R762KK: closed projection-pair formula and adaptive M3 upgrade theorem.
Pure exact integer mathematics for the frozen unsigned Port-Euler observer.
"""
from itertools import combinations, product
from collections import Counter

cube = list(product((0, 1), repeat=3))
missing = {(0, 1), (2, 3), (4, 5)}
ports = [p for p in combinations(range(6), 2) if p not in missing]
port_index = {p: i for i, p in enumerate(ports)}
W = (1 << len(ports)) - 1

def port_A(t): return (t[0], 2 + t[1])
def port_B(t): return (t[0], 4 + t[2])
def port_C(t): return (2 + t[1], 4 + t[2])
projections = (port_A, port_B, port_C)

def plane_formula(u, v):
    masks = [(1 << port_index[g(u)]) ^ (1 << port_index[g(v)])
             for g in projections]
    d = sum(x != y for x, y in zip(u, v))
    if d == 1:
        assert masks.count(0) == 1
        x, y = (m for m in masks if m)
        return {W, W ^ x, W ^ y, W ^ x ^ y}
    assert d in (2, 3) and all(masks)
    x, y, z = masks
    return {W ^ x, W ^ y, W ^ z, W ^ x ^ y ^ z}

def edge_mask(a, b):
    return (1 << port_index[a]) ^ (1 << port_index[b])

# The three edges of each legal triangle: AB, AC, BC.
edge_choice = {
    t: tuple(edge_mask(*e)
             for e in combinations([f(t) for f in projections], 2))
    for t in cube
}

def connected_reachable(upgraded):
    # Exact local two-event types: repeated edge gives 0 XOR,
    # two distinct edges give the remaining triangle edge's XOR.
    states = {(0, 0)}
    for t in cube:
        es = edge_choice[t]
        if t in upgraded:
            opts = {(es[i] ^ es[j], (1 << i) | (1 << j))
                    for i in range(3) for j in range(i, 3)}
        else:
            opts = {(es[i], 1 << i) for i in range(3)}
        states = {(a ^ b, types | new_types)
                  for a, types in states for b, new_types in opts}
    return {b for b, types in states if types.bit_count() >= 2}

def parity_reachable(upgraded):
    reached = {0}
    for t in cube:
        choices = set(edge_choice[t])
        if t in upgraded:
            choices.add(0)
        reached = {a ^ b for a in reached for b in choices}
    return reached

forced = []
for triple in combinations(range(6), 3):
    ps = [p for p in combinations(triple, 2) if p not in missing]
    if len(ps) == 2:
        forced.append(edge_mask(*ps))
assert len(forced) == 12

F = {0}
for delta in forced:
    F |= {x ^ delta for x in tuple(F)}
assert len(F) == 512 and W in F

planes = {}
for u, v in combinations(cube, 2):
    predicted = plane_formula(u, v)
    assert len(predicted) == 4
    assert F - parity_reachable({u, v}) == predicted
    assert F - connected_reachable({u, v}) == predicted
    planes[u, v] = predicted
assert len(planes) == 28

# Independently enumerate all 3^8 single-flex choices.
zero_reached = set()
for picks in product(range(3), repeat=8):
    if len(set(picks)) < 2:
        continue
    b = 0
    for t, choice in zip(cube, picks):
        b ^= edge_choice[t][choice]
    if b in F:
        zero_reached.add(b)
zero_holes = F - zero_reached
assert zero_holes == set().union(*planes.values())
assert len(zero_holes) == 47
assert len(zero_reached) == 465

distance_counts = Counter(
    sum(a != b for a, b in zip(u, v)) for u, v in planes)
assert distance_counts == {1: 12, 2: 12, 3: 4}

pair_membership = Counter(b for plane in planes.values() for b in plane)
assert Counter(pair_membership.values()) == {1: 28, 4: 18, 12: 1}

single_holes = {}
for u in cube:
    holes = F - parity_reachable({u})
    assert holes == F - connected_reachable({u})
    assert len(holes) == 17
    adjoining_union = set().union(
        *(plane for pair, plane in planes.items() if u in pair))
    assert holes == adjoining_union
    single_holes[u] = holes

adaptive_two = set.intersection(*single_holes.values())
assert adaptive_two == {W}
single_failures = Counter(
    sum(b in holes for holes in single_holes.values())
    for b in zero_holes)
assert single_failures == {2: 28, 4: 18, 8: 1}

print("PASS 512 exact forced boundaries, 28 projection-formula affine planes")
print("PASS 47 zero-upgrade holes, pair-incidence classes 1/4/12")
print("PASS all 28 pairs and 8 singles: parity/connected states agree")
print("PASS adaptive minima: 465 need 0, 46 need 1, one needs 2")
print("P000: unsigned auxiliary observer; review NOT_REVIEWED")
