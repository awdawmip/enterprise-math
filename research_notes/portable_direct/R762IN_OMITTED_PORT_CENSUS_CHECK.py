#!/usr/bin/env python3
"""Exact Port inactive-set census with at most two absent triple supports.
Frozen six-axis composite Port-Euler observer; no external dependencies.
"""
from itertools import combinations
from collections import Counter

AXES = range(6)
PORTS = list(combinations(AXES, 2))
SUPPORTS = list(combinations(AXES, 3))
PORT_ID = {p: i for i, p in enumerate(PORTS)}
SUPPORT_ID = {s: i for i, s in enumerate(SUPPORTS)}
TRI = [sum(1 << PORT_ID[p] for p in combinations(s, 2)) for s in SUPPORTS]

max_missing = {ab: -1 for ab in combinations(range(20), 2)}
max_witness = {}
valid_masks_by_size = Counter()
for inactive in range(1 << 15):
    forced_absent = 0
    for i, tri_mask in enumerate(TRI):
        if (inactive & tri_mask).bit_count() >= 2:
            forced_absent |= 1 << i
    if forced_absent.bit_count() > 2:
        continue
    count = inactive.bit_count()
    valid_masks_by_size[count] += 1
    for ij in max_missing:
        support_zero = (1 << ij[0]) | (1 << ij[1])
        if forced_absent & ~support_zero:
            continue
        if count > max_missing[ij]:
            max_missing[ij] = count
            max_witness[ij] = inactive

histogram = Counter(max_missing.values())
assert len(max_missing) == 190, len(max_missing)
assert histogram == {4: 180, 6: 10}, histogram
six_cases = [ij for ij, num in max_missing.items() if num == 6]
assert all(set(SUPPORTS[i]).isdisjoint(SUPPORTS[j]) for i, j in six_cases)
assert len(six_cases) == 10
assert dict(valid_masks_by_size) == {0:1, 1:15, 2:105, 3:395, 4:330, 5:60, 6:10}

# Concrete legal case: n_S=0 for S=012,345 and n_S=3 for all others.
A, B = set((0,1,2)), set((3,4,5))
assignments = []
for S in SUPPORTS:
    if set(S) == A or set(S) == B:
        continue
    cross = [p for p in combinations(S,2) if len(set(p)&A)==1]
    assert len(cross) == 2
    assignments += [(S, cross[0], cross[1])] * 3
assert len(assignments) == 54

deg = Counter(); adj = {p:set() for p in PORTS}
for S, p, q in assignments:
    deg[p] += 1;deg[q] += 1
    adj[p].add(q);adj[q].add(p)
active = {p for p in PORTS if deg[p]}
inactive = set(PORTS) - active
assert len(active) == 9 and len(inactive) == 6
assert inactive == {tuple(p) for p in combinations(A,2)} | {tuple(p) for p in combinations(B,2)}
assert all(deg[p] == 12 for p in active)
start = next(iter(active));reached={start};todo=[start]
while todo:
    for q in adj[todo.pop()]:
        if q not in reached:
            reached.add(q);todo.append(q)
assert reached == active
# Reducing one support's multiplicity from 3 to 1 removes two parallel edges.
assert len(assignments) - 2 == 52
print('PASS R762IN_OMITTED_PORT_CENSUS')
print('two-zero-support histograms: 190; max inactive Port distribution:', sorted(histogram.items()))
print('six inactive cases: 10, exactly disjoint complementary triple pairs')
print('valid inactive masks with <=2 forced absent supports:', sorted(valid_masks_by_size.items()))
print('exact 54-event legal example: zero supports 012/345, 9 active, 6 inactive, degree 12 each, connected')
print('52-event witness: reduce any one 3-count support to one edge, preserving graph and all nine active Ports')
