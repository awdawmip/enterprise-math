#!/usr/bin/env python3
"""R762IX exact Port--Euler checker. Standard library only; no numerical solver.
Run: python R762IX_STAR_TEN_TRIPLE_VERIFY.py
Two embedded 45-event witness arrays cover 540 all-active ordered (star, absent, single)
histograms by S6 symmetry. Two-inactive-or-more active sets use the direct
3->1 parallel-edge reduction condition in the accompanying argument.
"""
from itertools import combinations, permutations
from hashlib import sha256
import json

A = range(6)
PORTS = list(combinations(A, 2))
TRIPLES = list(combinations(A, 3))
P_INDEX = {p:i for i,p in enumerate(PORTS)}
T_INDEX = {s:i for i,s in enumerate(TRIPLES)}
VERTS = [tuple(P_INDEX[p] for p in combinations(t, 2)) for t in TRIPLES]
EDGES = [list(combinations(v, 2)) for v in VERTS]

# Each group of three entries lists the multiplicities of the three edge pairs
# in EDGES[s] for TRIPLES[s]. Original star is axis 0, reduction at (0,1,2).
# Type A: absent 123, single 124 (intersection 2).
# Type B: absent 123, single 145 (intersection 1).
CERTS = {
    2: (
        0,1,0, 2,1,0, 3,0,0, 1,0,2, 0,0,3,
        1,0,2, 1,0,2, 0,2,1, 0,3,0, 0,3,0,
        0,0,0, 1,0,0, 2,0,0, 0,0,2, 1,0,1,
        1,0,1, 1,0,1, 0,2,0, 0,2,0, 0,2,0,
    ),
    1: (
        1,0,0, 3,0,0, 3,0,0, 0,1,2, 0,0,3,
        1,0,2, 0,0,3, 0,3,0, 0,3,0, 0,2,1,
        0,0,0, 2,0,0, 2,0,0, 1,0,1, 1,0,1,
        0,0,1, 0,0,2, 0,1,1, 0,2,0, 0,2,0,
    ),
}

def counts(star_axis, absent, single, reduced):
    c = [3 if star_axis in s else 2 for s in TRIPLES]
    c[T_INDEX[absent]] = 0
    c[T_INDEX[single]] = 1
    assert c[T_INDEX[reduced]] == 3
    c[T_INDEX[reduced]] = 1
    return c

def permute_support(s, perm):
    return tuple(sorted(perm[a] for a in s))

def permute_allocation(x, perm):
    """Reindex support and its 3 *unordered Port--Port* edges exactly."""
    y = [0] * 60
    for s, triple in enumerate(TRIPLES):
        new_s = T_INDEX[permute_support(triple, perm)]
        for k, (u, v) in enumerate(EDGES[s]):
            new_ports = tuple(sorted((
                P_INDEX[permute_support(PORTS[u], perm)],
                P_INDEX[permute_support(PORTS[v], perm)]
            )))
            new_k = EDGES[new_s].index(new_ports)
            y[3*new_s + new_k] += x[3*s + k]
    assert sum(y) == sum(x)
    return y

def check(x, c):
    assert len(x) == 60 and len(c) == 20
    assert all(isinstance(v, int) and 0 <= v <= 3 for v in x)
    assert sum(c) == sum(x) == 45
    graph = [set() for _ in range(15)]
    degree = [0] * 15
    for s in range(20):
        assert sum(x[3*s:3*s+3]) == c[s]
        for k, (u, v) in enumerate(EDGES[s]):
            w = x[3*s+k]
            if w:
                degree[u] += w
                degree[v] += w
                graph[u].add(v)
                graph[v].add(u)
    assert all(d > 0 and d % 2 == 0 for d in degree)
    seen = {0}
    todo = [0]
    for u in todo:
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    assert len(seen) == 15
    return degree

def main():
    base = {
        2: (1, 2, 4),
        1: (1, 4, 5),
    }
    z = (1, 2, 3)
    fixed_reduced = (0, 1, 2)
    covered = {}
    for overlap, q in base.items():
        x = CERTS[overlap]
        assert len(x) == 60
        c = counts(0, z, q, fixed_reduced)
        check(x,c)
        orbit = {}
        for perm_tail in permutations(range(1, 6)):
            perm = (0,) + perm_tail
            zz, qq = permute_support(z, perm), permute_support(q, perm)
            key = (zz, qq)
            yy = permute_allocation(x,perm)
            rr = permute_support(fixed_reduced,perm)
            cc = counts(0,zz,qq,rr)
            check(yy,cc)
            orbit.setdefault(key, (yy,rr))
        assert len(orbit) == {2:60, 1:30}[overlap]
        assert not (set(orbit) & set(covered))
        covered.update(orbit)
    all_nonstar = [s for s in TRIPLES if 0 not in s]
    assert len(covered) == 90
    assert set(covered) == {(z,q) for z in all_nonstar for q in all_nonstar if z!=q}
    count=0
    stream = bytearray()
    for star_axis in range(6):
        # Swap native axis 0 with the desired star axis. This verifies all 540
        # ordered labelled (star-axis, missing support, single support) cases.
        sw = list(range(6))
        sw[0],sw[star_axis] = sw[star_axis],sw[0]
        for (zz,qq), (x,r) in sorted(covered.items()):
            aa = permute_support(zz,sw)
            bb = permute_support(qq,sw)
            rr = permute_support(r,sw)
            xx = permute_allocation(x,sw)
            cc = counts(star_axis,aa,bb,rr)
            check(xx,cc)
            stream.extend(bytes(xx))
            count+=1
    assert count == 540
    print(json.dumps({
        'status':'PASS R762IX',
        'certificates':2,
        's5_orbit_sizes':{'shared_two':60,'shared_one':30},
        'ordered_pairs_per_star':90,
        'all_active_histograms_checked':count,
        'witness_stream_sha256':sha256(stream).hexdigest(),
        'base_certificate_sha256':{str(k):sha256(bytes(v)).hexdigest() for k,v in CERTS.items()},
        'model':'frozen six-axis composite Port--Euler; not native signed P000',
    },sort_keys=True,ensure_ascii=False))

if __name__ == '__main__':
    main()
