#!/usr/bin/env python3
"""R762N: exact signed-X6 candidate BRC observer and sign-flip checks."""
from itertools import product
from collections import Counter
from math import prod

Q = list(product((0, 1), repeat=3))
idx = {s: i for i, s in enumerate(Q)}
edges = [(idx[s], idx[tuple(x ^ (i == j) for i, x in enumerate(s))])
         for s in Q for j in range(3) if s[j] == 0]
laws = list(product((0, 1), repeat=8))

def comps(mask):
    roots = list(range(8))
    def root(u):
        while roots[u] != u:
            u = roots[u]
        return u
    for i, (u, v) in enumerate(edges):
        if mask >> i & 1:
            roots[root(u)] = root(v)
    return list(Counter(root(v) for v in range(8)).values())

def observe(a, mask):
    return tuple(a[u] + a[v] for i, (u, v) in enumerate(edges)
                 if mask >> i & 1)

connected = Counter()
for mask in range(1 << 12):
    sizes = comps(mask)
    exact = len({observe(a, mask) for a in laws})
    assert exact == prod((1 << m) - 1 for m in sizes)
    if len(sizes) == 1:
        connected[mask.bit_count()] += 1
assert dict(sorted(connected.items())) == {7:384, 8:408, 9:212, 10:66, 11:12, 12:1}
tree = next(m for m in range(1 << 12) if m.bit_count() == 7 and len(comps(m)) == 1)
assert len({observe(a, tree) for a in laws}) == 255
assert len({(observe(a, tree), a[0]) for a in laws}) == 256
for mask in range(1 << 12):
    if mask.bit_count() <= 6:
        for v in range(8):
            assert len({(observe(a, mask), a[v]) for a in laws}) < 256
W = {tuple(4 * (a[idx[(s, t, 0)]] + 2 * a[idx[(s, t, 1)]])
           for s, t in product((0, 1), repeat=2)) for a in laws}
assert len(W) == 256
for parity in (0, 1):
    for flip in Q:
        for s in Q:
            if sum(s) % 2 == parity:
                next_s = tuple(x ^ y for x, y in zip(s, flip))
                assert (sum(next_s) % 2 == parity) == (sum(flip) % 2 == 0)
print({'edge_subsets':4096, 'laws':256, 'connected_by_size':dict(sorted(connected.items())),
       'spanning_trees':connected[7], 'unweighted_signatures':255,
       'weighted_signatures':len(W), 'candidate_update_cases':128})
