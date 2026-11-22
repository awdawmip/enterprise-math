#!/usr/bin/env python3
"""Standard-library-only exact verifier for R762IW.
Usage: python R762IW_VERIFY_CERTS.py R762IW_CERTS.b64
"""
import base64
import hashlib
from itertools import combinations
import json
from pathlib import Path
import sys
import zlib

PORTS = list(combinations(range(6), 2))
TRIPLES = list(combinations(range(6), 3))
pi = {p: i for i, p in enumerate(PORTS)}
ti = {t: i for i, t in enumerate(TRIPLES)}
SUPPORT_VERTICES = [tuple(pi[p] for p in combinations(t, 2)) for t in TRIPLES]
SUPPORT_EDGES = [list(combinations(v, 2)) for v in SUPPORT_VERTICES]
GEN = []
for i in range(5):
    p = list(range(6))
    p[i], p[i+1] = p[i+1], p[i]
    GEN.append(tuple(ti[tuple(sorted(p[a] for a in t))] for t in TRIPLES))


def permute_mask(mask, perm):
    result = 0
    for i in range(20):
        if mask >> i & 1:
            result |= 1 << perm[i]
    return result


def component_count(sub):
    parent = list(range(15))
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for i in sub:
        a, b, c = SUPPORT_VERTICES[i]
        parent[root(a)] = root(b)
        parent[root(a)] = root(c)
    return len({root(v) for v in range(15)})


def all_essential(mask):
    support = [s for s in range(20) if mask >> s & 1]
    before = component_count(support)
    return all(component_count(support[:i]+support[i+1:]) > before for i in range(9))


def representatives():
    essential = set()
    for support in combinations(range(20), 9):
        mask = sum(1 << s for s in support)
        if all_essential(mask):
            essential.add(mask)
    assert len(essential) == 240
    uncovered = {(mask, z) for mask in essential for z in range(20) if not mask >> z & 1}
    assert len(uncovered) == 2640
    reps = []
    while uncovered:
        seed = min(uncovered)
        seen, queue = {seed}, [seed]
        for m, z in queue:
            for perm in GEN:
                nxt = (permute_mask(m, perm), perm[z])
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        assert seen <= uncovered
        uncovered -= seen
        reps.append((seed, len(seen)))
    assert len(reps) == 9
    assert [n for _, n in reps] == [60, 60, 360, 180, 360, 360, 720, 360, 180]
    return reps


def inactive_masks(z):
    for bitset in range(1 << 15):
        if all(sum(not (bitset >> v & 1) for v in SUPPORT_VERTICES[s]) >= 2
               for s in range(20) if s != z):
            yield bitset


def verify_one(mask, absent, missing, counts, x):
    assert len(x) == 60 and all(0 <= val <= 3 for val in x)
    assert sum(counts) == 45
    assert sum(c == 3 for c in counts) == 8
    assert sum(c == 1 for c in counts) == 1
    assert sum(c == 2 for c in counts) == 10
    assert counts[absent] == 0
    degree = [0] * 15
    graph = [set() for _ in range(15)]
    for s in range(20):
        assert sum(x[3*s:3*s+3]) == counts[s]
        for j, (u, v) in enumerate(SUPPORT_EDGES[s]):
            c = x[3*s+j]
            if c:
                assert not (missing >> u & 1 or missing >> v & 1)
                degree[u] += c
                degree[v] += c
                graph[u].add(v)
                graph[v].add(u)
    active = {v for v in range(15) if not (missing >> v & 1)}
    assert all(degree[v] >= 2 and degree[v] % 2 == 0 for v in active)
    assert all(degree[v] == 0 for v in range(15) if v not in active)
    seen = {min(active)}
    queue = list(seen)
    for u in queue:
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    assert seen == active


def main():
    encoded = Path(sys.argv[1]).read_text().strip()
    raw = zlib.decompress(base64.b64decode(encoded))
    assert len(raw) == 12420
    assert hashlib.sha256(raw).hexdigest() == '15d611b1e80d16b45ab9ec471c233e826d60bb6f189377041c566acaa2631035'
    reps = representatives()
    offset = 0
    tested = 0
    for (mask, absent), orbit_size in reps:
        reduce_s = next(s for s in range(20) if mask >> s & 1)
        counts = [3 if mask >> s & 1 else (0 if s == absent else 2) for s in range(20)]
        counts[reduce_s] = 1
        local = 0
        for missing in inactive_masks(absent):
            packet = raw[offset:offset+15]
            assert len(packet) == 15
            offset += 15
            x = [(b >> (2*j)) & 3 for b in packet for j in range(4)]
            verify_one(mask, absent, missing, counts, x)
            tested += 1
            local += 1
        assert local == 92
    assert offset == len(raw) and tested == 828
    print(json.dumps({'result': 'PASS R762IW', 'verified_witnesses': tested,
                      'base_orbits': len(reps), 'essential_pairs': sum(n for _, n in reps),
                      'scope_covered_by_symmetry': 242880,
                      'raw_sha256': hashlib.sha256(raw).hexdigest()}))


if __name__ == '__main__':
    main()
