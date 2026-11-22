#!/usr/bin/env python3
"""Exact finite census for R762IO, independent of the R762IM active-set filter.
Six axes, 15 pair-Ports, 20 triple supports; integer arithmetic only.
Counts local feasibility and potential-edge connectivity, NOT Euler realizations.
"""
from collections import Counter
from itertools import combinations
from math import factorial

AXES = range(6)
PORTS = tuple(combinations(AXES, 2))
SUPPORTS = tuple(combinations(AXES, 3))
PORT_INDEX = {p: i for i, p in enumerate(PORTS)}
TRI = tuple(tuple(PORT_INDEX[p] for p in combinations(s, 2)) for s in SUPPORTS)
ALL_PORTS = (1 << len(PORTS)) - 1


def forced_absent(inactive):
    mask = 0
    for i, triangle in enumerate(TRI):
        if sum((inactive >> v) & 1 for v in triangle) >= 2:
            mask |= 1 << i
    return mask


def wedge_formula(inactive):
    degrees = [0] * 6
    for i, (a, b) in enumerate(PORTS):
        if inactive >> i & 1:
            degrees[a] += 1
            degrees[b] += 1
    triangles = sum(all(inactive >> v & 1 for v in triple) for triple in TRI)
    return sum(d * (d - 1) // 2 for d in degrees) - 2 * triangles


def potential_connected(inactive, zero_supports):
    active = ALL_PORTS & ~inactive
    start = (active & -active).bit_length() - 1
    graph = [0] * 15
    for i, triple in enumerate(TRI):
        if zero_supports >> i & 1:
            continue
        allowed = [v for v in triple if active >> v & 1]
        for u, v in combinations(allowed, 2):
            graph[u] |= 1 << v
            graph[v] |= 1 << u
    visited = 1 << start
    stack = [start]
    while stack:
        u = stack.pop()
        neighbors = graph[u] & ~visited
        while neighbors:
            bit = neighbors & -neighbors
            v = bit.bit_length() - 1
            visited |= bit
            stack.append(v)
            neighbors ^= bit
    return visited == active


def kind_of_pair(a, b):
    intersection = len(set(SUPPORTS[a]) & set(SUPPORTS[b]))
    return {0: "disjoint", 1: "intersect_one", 2: "intersect_two"}[intersection]


ZERO_SETS = {0: [()], 1: list(combinations(range(20), 1)),
             2: list(combinations(range(20), 2))}
BY_KIND = {"zero_none": Counter(), "zero_one": Counter(),
           "disjoint": Counter(), "intersect_one": Counter(),
           "intersect_two": Counter()}
PAIR_KINDS = Counter()
CONNECTED = Counter()
REJECTED_CONNECTIVITY = []
FORMULA_FAILURE = []

FORCED = [forced_absent(inactive) for inactive in range(1 << 15)]
assert all(f.bit_count() == wedge_formula(i) for i, f in enumerate(FORCED))

for z_count, choices in ZERO_SETS.items():
    for missing in choices:
        support_mask = sum(1 << i for i in missing)
        if z_count == 0:
            label = "zero_none"
        elif z_count == 1:
            label = "zero_one"
        else:
            label = kind_of_pair(*missing)
            PAIR_KINDS[label] += 1
        for inactive in range(1 << 15):
            forced = FORCED[inactive]
            if forced & ~support_mask:
                continue
            BY_KIND[label][inactive.bit_count()] += 1
            if not potential_connected(inactive, support_mask):
                REJECTED_CONNECTIVITY.append((missing, inactive))
            else:
                CONNECTED[label] += 1


EXPECTED = {
    "zero_none": {0: 1, 1: 15, 2: 45, 3: 15},
    "zero_one": {0: 20, 1: 300, 2: 960, 3: 500, 4: 60},
    "disjoint": {0: 10, 1: 150, 2: 510, 3: 350, 4: 150, 5: 60, 6: 10},
    "intersect_one": {0: 90, 1: 1350, 2: 4590, 3: 3150, 4: 540},
    "intersect_two": {0: 90, 1: 1350, 2: 4590, 3: 3330, 4: 720},
}
assert {k: dict(v) for k, v in BY_KIND.items()} == EXPECTED
assert dict(PAIR_KINDS) == {"disjoint": 10, "intersect_one": 90,
                             "intersect_two": 90}
assert not REJECTED_CONNECTIVITY, REJECTED_CONNECTIVITY[:5]
assert not FORMULA_FAILURE, FORMULA_FAILURE[:5]

# Independent multinomial enumeration of every D=60-|n| in {0,2,4,6}.
HIST = Counter()
for m in range(3):  # zero-count support types
    for u in range(4):  # one-count support types
        for e in range(7):  # two-count support types
            three = 20 - m - u - e
            if three < 0 or 2*u + e + 3*m not in {0, 2, 4, 6}:
                continue
            n = factorial(20) // (factorial(m)*factorial(u)*factorial(e)*factorial(three))
            HIST[m] += n
assert dict(HIST) == {0: 155156, 1: 26600, 2: 190}

per_zero = {
    0: sum(BY_KIND["zero_none"].values()),
    1: sum(BY_KIND["zero_one"].values()) // 20,
    2: (sum(BY_KIND["disjoint"].values()) +
        sum(BY_KIND["intersect_one"].values()) +
        sum(BY_KIND["intersect_two"].values())),
}
assert per_zero == {0: 76, 1: 92, 2: 21040}
weighted = {0: HIST[0]*per_zero[0], 1: HIST[1]*per_zero[1], 2: per_zero[2]}
assert weighted == {0: 11791856, 1: 2447200, 2: 21040}
assert sum(weighted.values()) == 14260096
assert sum(CONNECTED.values()) == 22956

# Explicit 60-event T20 realization with 14 active Ports and inactive Port 01.
# Each triple support uses the specified pair-Port edge three times.
WITNESS = (
    ("02", "12"), ("03", "13"), ("04", "14"), ("05", "15"),
    ("02", "03"), ("02", "04"), ("02", "05"), ("03", "04"),
    ("03", "35"), ("04", "45"), ("12", "13"), ("12", "14"),
    ("12", "25"), ("14", "34"), ("15", "35"), ("14", "45"),
    ("23", "24"), ("23", "25"), ("24", "45"), ("34", "45"),
)
assert len(WITNESS) == len(SUPPORTS)
port_by_str = {"".join(map(str, p)): i for i, p in enumerate(PORTS)}
used_edges = []
for i, names in enumerate(WITNESS):
    u, v = (port_by_str[name] for name in names)
    assert u in TRI[i] and v in TRI[i] and u != v
    used_edges.extend([(u,v)]*3)
assert len(used_edges) == 60

def euler_check(edge_list):
    degrees = [0]*15
    graph = [set() for _ in range(15)]
    for u,v in edge_list:
        degrees[u] += 1
        degrees[v] += 1
        graph[u].add(v)
        graph[v].add(u)
    live = {i for i, d in enumerate(degrees) if d}
    seen = {next(iter(live))}
    stack = list(seen)
    while stack:
        for v in graph[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    assert live == seen
    assert all(degrees[i] % 2 == 0 for i in live)
    assert live == set(range(15))-{port_by_str["01"]}
    return degrees

degrees60 = euler_check(used_edges)
# Remove 2 of the 3 parallel edges at each of the first four support types.
kept = []
for i in range(20):
    kept.extend(used_edges[3*i:3*(i+1)][:(1 if i < 4 else 3)])
assert len(kept) == 52
assert euler_check(kept)

print("PASS R762IO_CORRECTED_INACTIVE_CENSUS")
print("candidate mask distribution by missing-support type:")
for label in EXPECTED:
    print(label, dict(sorted(BY_KIND[label].items())))
print("support histogram count by zero support number:", dict(HIST))
print("candidate (histogram, inactive-mask) total:", sum(weighted.values()))
print("all local-admissible potential-edge graphs connected:", sum(CONNECTED.values()))
print("wedge identity checked for every locally admissible pair:", sum(CONNECTED.values()))
print("T20 60-event / 14 active Port witness: PASS; 52-event parity/connectedness witness: PASS")
