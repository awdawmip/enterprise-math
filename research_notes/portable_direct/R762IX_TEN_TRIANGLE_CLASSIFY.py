#!/usr/bin/env python3
"""Exact enumeration of all-essential 10-triangle families on six-axis Ports.
No solver dependencies. Complements R762IX_STAR_TEN_TRIPLE_VERIFY.py.
"""
from itertools import combinations
import json

PORTS = list(combinations(range(6), 2))
TRIPLES = list(combinations(range(6), 3))
pi = {p: i for i, p in enumerate(PORTS)}
V = [tuple(pi[p] for p in combinations(t, 2)) for t in TRIPLES]

def components(support_ids):
    parent = list(range(15))
    def root(v):
        while v != parent[v]:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for s in support_ids:
        a, b, c = V[s]
        parent[root(a)] = root(b)
        parent[root(a)] = root(c)
    return len({root(v) for v in range(15)})

def main():
    essential = []
    scanned = 0
    for ten in combinations(range(20), 10):
        scanned += 1
        baseline = components(ten)
        if all(components(ten[:j]+ten[j+1:]) > baseline for j in range(10)):
            essential.append(sum(1 << s for s in ten))
    stars = [sum(1 << s for s, t in enumerate(TRIPLES) if a in t)
             for a in range(6)]
    assert scanned == 184756
    assert len(essential) == len(stars) == 6
    assert set(essential) == set(stars)
    print(json.dumps({'status':'PASS R762IX STAR CLASSIFICATION',
                      'domain':'all C(20,10) support families',
                      'checked':scanned,'all_essential':len(essential),
                      'star_masks':sorted(stars)},sort_keys=True))

if __name__ == '__main__':
    main()
