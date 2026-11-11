#!/usr/bin/env python3
"""R728: exact finite BRC candidate port-conflict source-ID partition verification.

Native X6 axis families are labels 0..5; a branch is an unordered partition
of *individually labeled* source IDs into three-distinct-axis triples. A
candidate exclusive port block {0,1} excludes triples containing both axes.
No heartbeat time evolution or physical V29/V39 event is simulated.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial

AXES = tuple(range(6))
BLOCKS = ((0,1),(2,),(3,),(4,),(5,))
ALL = tuple(combinations(AXES, 3))
PORT = tuple(t for t in ALL if not (0 in t and 1 in t))
assert len(ALL) == 20 and len(PORT) == 16

def vectors(total, n=6):
    if n == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for tail in vectors(total-x,n-1):
                yield (x,) + tail

def source_id_recursion(edges):
    by_pivot = {i: tuple(e for e in edges if i in e) for i in AXES}
    @lru_cache(None)
    def ways(a):
        if not any(a): return 1
        pivot = next(i for i in AXES if a[i])
        value = 0
        for e in by_pivot[pivot]:
            if not all(a[i] > 0 for i in e): continue
            rest = list(a)
            for i in e: rest[i] -= 1
            partners = [i for i in e if i != pivot]
            value += a[partners[0]] * a[partners[1]] * ways(tuple(rest))
        return value
    return ways

def poly_layers(edges, max_m):
    level = {(0,)*6: 1}
    layers = {0:level}
    for m in range(1,max_m+1):
        nxt = Counter()
        for a,mult in level.items():
            for edge in edges:
                b = list(a)
                for i in edge: b[i] += 1
                nxt[tuple(b)] += mult
        level = dict(nxt)
        layers[m] = level
    return layers

def block_count(a):
    return tuple(sum(a[i] for i in group) for group in BLOCKS)

def verify():
    full = source_id_recursion(ALL)
    port = source_id_recursion(PORT)
    cf = poly_layers(ALL,4)
    cp = poly_layers(PORT,4)
    expected = [
        (1,56,20,16,1,1,4,4),
        (2,462,141,99,10,6,55,42),
        (3,2002,580,378,124,96,306,202),
        (4,6188,1751,1088,4960,2448,1086,663)
    ]
    for m,n_expected,full_feasible,port_feasible,max_full,max_port,changed,blocked in expected:
        total = nf = np = mf = mp = dc = nb = 0
        for a in vectors(3*m):
            total += 1
            f,p = full(a),port(a)
            assert (f > 0) == (max(a) <= m), (m,a,'full-feas')
            assert (p > 0) == (max(block_count(a)) <= m), (m,a,'port-feas')
            fac = 1
            for k in a: fac *= factorial(k)
            assert f * factorial(m) == cf[m].get(a,0) * fac,(m,a,'full-poly')
            assert p * factorial(m) == cp[m].get(a,0) * fac,(m,a,'port-poly')
            assert 0 <= p <= f
            nf += (f > 0)
            np += (p > 0)
            mf = max(mf,f)
            mp = max(mp,p)
            dc += (f != p)
            nb += (f > 0 and p == 0)
        actual = (m,total,nf,np,mf,mp,dc,nb)
        assert actual == (m,n_expected,full_feasible,port_feasible,max_full,max_port,changed,blocked), actual
        print("m=",m,"total=",total,"eligible_full=",nf,"eligible_port=",np,
              "max_full=",mf,"max_port=",mp,"changed=",dc,"blocked=",nb)
    a = (1,1,1,1,1,1)
    b = (2,0,1,1,1,1)
    assert block_count(a) == block_count(b) == (2,1,1,1,1)
    assert (port(a),port(b)) == (6,6)
    assert (full(a),full(b)) == (10,6)
    assert (full((2,1,1,1,1,0)),port((2,1,1,1,1,0))) == (6,0)
    for perm in permutations(AXES):
        transported = {tuple(sorted(perm[i] for i in t)) for t in PORT}
        expected_edge_set = {t for t in ALL if not (perm[0] in t and perm[1] in t)}
        assert transported == expected_edge_set
    print("R728_PORT_CONFLICT_EXACT_PASS")

if __name__ == "__main__":
    verify()
