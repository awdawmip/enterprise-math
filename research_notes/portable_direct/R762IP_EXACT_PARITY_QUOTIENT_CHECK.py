#!/usr/bin/env python3
"""Exact GF(2) component quotient for support-assigned Port edges; all integer."""
from itertools import combinations, product
from random import Random

PORTS = tuple(combinations(range(6), 2))
SUPPORTS = tuple(combinations(range(6), 3))
P = {s: i for i, s in enumerate(PORTS)}
TRI = tuple(tuple(P[x] for x in combinations(s, 2)) for s in SUPPORTS)


def quotient_feasible(n, inactive):
    parent = list(range(15))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def join(a, b):
        a, b = root(a), root(b)
        if a != b:
            parent[a] = b
    for i, triangle in enumerate(TRI):
        live = [v for v in triangle if not (inactive >> v & 1)]
        if n[i] and len(live) < 2:
            return False
        if n[i] >= 2 and len(live) == 3:
            join(live[0], live[1]); join(live[1], live[2])
    fixed = 0
    choices = []
    for i, triangle in enumerate(TRI):
        if n[i] == 0:
            continue
        live = [v for v in triangle if not (inactive >> v & 1)]
        if len(live) == 2:
            if n[i] % 2:
                fixed ^= (1 << root(live[0])) ^ (1 << root(live[1]))
        elif n[i] == 1:
            choices.append([(1 << root(a)) ^ (1 << root(b))
                            for a, b in combinations(live, 2)])
    for assignment in product(*choices):
        signature = fixed
        for x in assignment:
            signature ^= x
        if signature == 0:
            return True
    return False


def brute_feasible(n, inactive):
    outcomes = []
    for i, amount in enumerate(n):
        if not amount:
            continue
        live = [v for v in TRI[i] if not (inactive >> v & 1)]
        edge_masks = [(1 << u) ^ (1 << v) for u, v in combinations(live, 2)]
        if not edge_masks:
            return False
        outcomes.extend([edge_masks] * amount)
    if not outcomes:
        return True
    return any(not __import__('functools').reduce(int.__xor__, assignment, 0)
               for assignment in product(*outcomes))


missing = {SUPPORTS.index((1, 3, 4)), SUPPORTS.index((2, 4, 5))}
inactive = sum(1 << P[tuple(int(c) for c in label)] for label in ('01', '24', '25', '45'))
n = [0 if i in missing else 3 for i in range(20)]
assert sum(n) == 54
assert all(sum(inactive >> v & 1 for v in TRI[i]) <= 1
           for i in range(20) if n[i] > 0)
assert not quotient_feasible(n, inactive)
# The three only positive supports containing Port 14 are 014, 124, 145.
port14 = P[(1, 4)]
forced_incidence = []
for i, s in enumerate(SUPPORTS):
    if n[i] and port14 in TRI[i]:
        live = [v for v in TRI[i] if not (inactive >> v & 1)]
        assert len(live) == 2 and port14 in live
        forced_incidence.append((s, n[i]))
assert forced_incidence == [((0, 1, 4), 3), ((1, 2, 4), 3), ((1, 4, 5), 3)]
assert sum(k for _, k in forced_incidence) == 9

rng = Random(762119)
checked = 0
for _ in range(1200):
    counts = [0] * 20
    chosen = rng.sample(range(20), rng.randrange(0, 5))
    for j in chosen:
        counts[j] = rng.randrange(1, 4)
    if sum(counts) > 8:
        continue
    inactive_mask = rng.randrange(1 << 15)
    a = quotient_feasible(counts, inactive_mask)
    b = brute_feasible(counts, inactive_mask)
    assert a == b, (counts, inactive_mask, a, b)
    checked += 1
assert checked > 750, checked
print('PASS R762IP_EXACT_PARITY_QUOTIENT, brute-force crosscheck instances:', checked)
print('54-event incidence-compatible obstruction: inactive 01,24,25,45; support zeros 134,245')
print('forced degree at Port 14 = 9 (odd); parity-infeasible despite potential connectivity')
