#!/usr/bin/env python3
"""R762KJ: exact geometric 47-hole classifier for the unsigned M3 Port-Euler observer.
Standard library only. Frozen P000 V5 @a72226e2; predecessor R762KI @211070ca.
"""
from itertools import combinations, product
from collections import Counter

missing = {(0, 1), (2, 3), (4, 5)}
ports = [p for p in combinations(range(6), 2) if p not in missing]
index = {p: i for i, p in enumerate(ports)}
triples = list(combinations(range(6), 3))
edges = {s: list(combinations([index[p] for p in combinations(s, 2) if p in index], 2))
         for s in triples}
forced = [s for s in triples if len(edges[s]) == 1]
flexible = [s for s in triples if len(edges[s]) == 3]
assert len(forced) == 12 and len(flexible) == 8

A = ((0, 2), (0, 3), (1, 2), (1, 3))
B = ((0, 4), (0, 5), (1, 4), (1, 5))
C = ((2, 4), (2, 5), (3, 4), (3, 5))
grids = (A, B, C)

def boundary(edge):
    return (1 << edge[0]) ^ (1 << edge[1])

force_space = {0}
for s in forced:
    delta = boundary(edges[s][0])
    force_space |= {x ^ delta for x in tuple(force_space)}
assert len(force_space) == 512

def grid_feature(mask, grid):
    chosen = [p for p in grid if mask & (1 << index[p])]
    n = len(chosen)
    if n != 2:
        return ('full' if n == 4 else 'empty', None)
    (a, b), (c, d) = chosen
    if a == c:
        return ('line-second', a)
    if b == d:
        return ('line-first', b)
    first0 = min(p[0] for p in grid)
    second0 = min(p[1] for p in grid)
    return ('diagonal', (a - first0) ^ (b - second0))

def is_geometric_hole(mask):
    f = [grid_feature(mask, g) for g in grids]
    weights = [sum(bool(mask & (1 << index[p])) for p in g) for g in grids]
    if any(w not in (2, 4) for w in weights):
        return False
    full = [i for i, w in enumerate(weights) if w == 4]
    if len(full) >= 2:
        return True
    if len(full) == 1:
        k = full[0]
        return ((k == 0 and f[1][0] == f[2][0] == 'line-second') or
                (k == 1 and f[0][0] == 'line-second' and f[2][0] == 'line-first') or
                (k == 2 and f[0][0] == f[1][0] == 'line-first'))
    if all(t == 'diagonal' for t, _ in f):
        return (f[0][1] ^ f[1][1] ^ f[2][1]) == 1
    return ((f[0][0] == f[1][0] == 'line-second' and
             f[2][0] == 'diagonal' and f[0][1] == f[1][1]) or
            (f[0][0] == 'line-first' and f[1][0] == 'diagonal' and
             f[2][0] == 'line-second' and f[0][1] == f[2][1]) or
            (f[0][0] == 'diagonal' and f[1][0] == f[2][0] == 'line-first' and
             f[1][1] == f[2][1]))

def component(p):
    if max(p) <= 3: return 0
    if min(p) <= 1: return 1
    return 2

type_bit = {frozenset((0, 1)): 1, frozenset((0, 2)): 2,
            frozenset((1, 2)): 4}

# Direct 3^8 enumeration, independent of the older GF(2) DP.
observed = set()
for choice in product(range(3), repeat=8):
    b = 0
    types = 0
    for k, s in enumerate(flexible):
        edge = edges[s][choice[k]]
        b ^= boundary(edge)
        p, q = (ports[i] for i in edge)
        types |= type_bit[frozenset((component(p), component(q)))]
    if types.bit_count() >= 2:
        observed.add(b)
holes = force_space - observed
structural = {x for x in force_space if is_geometric_hole(x)}
assert holes == structural and len(holes) == 47

# A second exact parity propagation computes all 28 pair-specific obstruction planes.
opts = {}
for s in flexible:
    for count in (1, 2):
        local = set()
        rows = (((j,) for j in range(3)) if count == 1 else
                ((i, j) for i in range(3) for j in range(i, 3)))
        for row in rows:
            b = 0
            for k in row:
                b ^= boundary(edges[s][k])
            local.add(b)
        opts[s, count] = local

def parity_reachable(upgrades):
    current = {0}
    for i, s in enumerate(flexible):
        current = {a ^ b for a in current
                   for b in opts[s, 2 if i in upgrades else 1]}
    return current & force_space

planes = {}
for i, j in combinations(range(8), 2):
    p = force_space - parity_reachable({i, j})
    assert len(p) == 4
    x = 0
    for b in p:
        x ^= b
    assert x == 0
    planes[(i, j)] = p
assert set().union(*planes.values()) == holes
multiplicity = Counter(b for plane in planes.values() for b in plane)
assert Counter(multiplicity.values()) == {1: 28, 4: 18, 12: 1}
assert {b for b in holes if multiplicity[b] == 12} == {(1 << 12) - 1}

weight_class = Counter()
def grid_weights(b):
    return tuple(sorted(sum(bool(b & (1 << index[p])) for p in g)
                        for g in grids))
for b in holes:
    weight = grid_weights(b)
    weight_class[weight] += 1
    assert multiplicity[b] == {
        (2,2,2): 1, (2,2,4): 1, (2,4,4): 4, (4,4,4): 12
    }[weight]
assert weight_class == {
    (2,2,2): 16, (2,2,4): 12, (2,4,4): 18, (4,4,4): 1
}

orbit_sizes = Counter()
for (i, j), plane in planes.items():
    distance = sum((a in flexible[i]) != (a in flexible[j])
                   for a, b in sorted(missing))
    orbit_sizes[distance] += 1
    distribution = Counter(grid_weights(b) for b in plane)
    expected = ({(2,2,4): 1, (2,4,4): 2, (4,4,4): 1}
                if distance == 1 else
                {(2,2,2): 1, (2,4,4): 3})
    assert distribution == expected
assert orbit_sizes == {1: 12, 2: 12, 3: 4}
print("PASS: 6561 direct choices, 512 forced boundaries, 47 exactly classified holes")
print("PASS: 28 two-upgrade planes, 112 incidences, multiplicities 1/4/12")
print("PASS: cube-distance counts 12/12/4 and structural plane profiles")
