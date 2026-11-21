#!/usr/bin/env python3
"""R762IB exact, exhaustive parity-core checker for the six-axis Port candidate.

No floating point, nonstandard dependencies, external data or native P000 lift.
Enumerate GF(2) incidence kernel, exact half-incidence signability,
two-axis-support overlap, and all S6 label orbits.
"""
from collections import defaultdict
from itertools import combinations, permutations

T = list(combinations(range(6), 3))
assert len(T) == 20

# Six row constraints over F2; construct a 14-dimensional nullspace basis.
rows = [sum(1 << j for j, s in enumerate(T) if axis in s)
        for axis in range(6)]
pivots = {}
for row in rows:
    while row:
        p = row.bit_length() - 1
        if p not in pivots:
            pivots[p] = row
            break
        row ^= pivots[p]
free = [j for j in range(20) if j not in pivots]
assert len(pivots) == 6 and len(free) == 14
basis = []
for f in free:
    v = 1 << f
    for p in sorted(pivots):
        if ((pivots[p] & v).bit_count() & 1):
            v ^= 1 << p
    assert all((row & v).bit_count() % 2 == 0 for row in rows)
    basis.append(v)


def balanced(ids):
    """Exact subset sum: choose support occurrences with H/2 incidence."""
    degrees = [sum(axis in T[j] for j in ids) for axis in range(6)]
    assert all(d % 2 == 0 for d in degrees)
    target = tuple(d // 2 for d in degrees)
    half = len(ids) // 2
    left, right = [(0,) * 6], [(0,) * 6]
    for j in ids[:half]:
        s = T[j]
        vec = tuple(int(a in s) for a in range(6))
        left += [tuple(x + y for x, y in zip(t, vec)) for t in left[:]]
    for j in ids[half:]:
        s = T[j]
        vec = tuple(int(a in s) for a in range(6))
        right += [tuple(x + y for x, y in zip(t, vec)) for t in right[:]]
    lookup = set(right)
    return any(tuple(y - x for x, y in zip(l, target)) in lookup
               for l in left)


def connected(ids):
    """G2 only: adjacent supports overlap in exactly two native axes."""
    seen = {ids[0]}
    todo = [ids[0]]
    population = set(ids)
    while todo:
        j = todo.pop()
        for k in population - seen:
            if len(set(T[j]) & set(T[k])) == 2:
                seen.add(k)
                todo.append(k)
    return len(seen) == len(ids)


counts = defaultdict(lambda: [0, 0, 0, 0])
bad = set()
visited = set()
for word in range(1 << len(basis)):
    mask = 0
    for j, b in enumerate(basis):
        if (word >> j) & 1:
            mask ^= b
    assert mask not in visited
    visited.add(mask)
    if mask == 0:
        continue
    ids = [j for j in range(20) if (mask >> j) & 1]
    assert len(ids) % 2 == 0
    degree = [sum(a in T[j] for j in ids) for a in range(6)]
    assert all(d % 2 == 0 for d in degree)
    key = len(ids)
    is_balanced = balanced(ids)
    is_connected = connected(ids)
    counts[key][0] += 1
    counts[key][1] += int(not is_balanced)
    counts[key][2] += int(is_connected)
    counts[key][3] += int(is_connected and not is_balanced)
    if not is_balanced:
        bad.add(mask)

expected = {
    4: [165, 30, 90, 0],
    6: [1200, 180, 1020, 0],
    8: [3930, 0, 3915, 0],
    10: [5792, 20, 5772, 0],
    12: [3930, 0, 3930, 0],
    14: [1200, 0, 1200, 0],
    16: [165, 0, 165, 0],
    20: [1, 0, 1, 0],
}
assert len(visited) == (1 << 14)
assert dict(counts) == expected, (dict(counts), expected)
assert len(bad) == 230

lookup = {frozenset(s): i for i, s in enumerate(T)}
permutations_of_triples = [
    [lookup[frozenset(p[a] for a in s)] for s in T]
    for p in permutations(range(6))
]
assert len(permutations_of_triples) == 720


def renamed(mask, mapping):
    out = 0
    for i in range(20):
        if (mask >> i) & 1:
            out |= 1 << mapping[i]
    return out


orbits = []
left = set(bad)
while left:
    representative = min(left)
    orbit = {renamed(representative, mapping)
             for mapping in permutations_of_triples}
    assert orbit <= bad
    left -= orbit
    orbits.append((representative, len(orbit)))
assert orbits == [(3273, 180), (12576, 30), (119623, 20)], orbits
assert not left

print("PASS R762IB: GF2 rank=6; 16384 parity cores; three S6 obstruction orbits")
for weight in sorted(expected):
    print("weight", weight, "even-core / unsignable / G2-connected / both:",
          expected[weight])
for rep, size in orbits:
    print("obstruction representative", rep, "orbit_size", size,
          "supports", ["".join(map(str, T[j]))
                       for j in range(20) if (rep >> j) & 1])
