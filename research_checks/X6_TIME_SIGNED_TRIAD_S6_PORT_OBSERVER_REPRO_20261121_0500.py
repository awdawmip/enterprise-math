#!/usr/bin/env python3
"""Exact S6 signed-distinct-triad orbit and future-port-observer check (candidate model)."""
from itertools import permutations, combinations, product
from collections import Counter
from math import comb, factorial, ceil, log2
G=list(permutations(range(6)))
D=[tuple(zip(A,s)) for A in combinations(range(6),3) for s in product((-1,1),repeat=3)]
def act(g,q):return tuple(sorted(((g[a],s) for a,s in q)))
def inv(g):return tuple(g.index(a) for a in range(6))
def pos(q):return sum(s==1 for _,s in q)
assert len(G)==720 and len(D)==160
orbits={}
classes={}
query_checks=rotation_checks=law_checks=0
for k in range(4):
    mark=next(q for q in D if pos(q)==k)
    orbit={act(g,mark) for g in G}
    assert orbit=={q for q in D if pos(q)==k}
    orbits[k]=len(orbit)
    signature=Counter()
    for g in G:
        local_mark=act(inv(g),mark)
        assert [q for q in D if act(g,q)==mark]==[local_mark]
        signature[local_mark]+=1
        query_checks+=len(D)
    assert len(signature)==comb(3,k)*comb(6,3)
    assert set(signature.values())=={factorial(k)*factorial(3-k)*factorial(3)}
    classes[k]=(len(signature),next(iter(signature.values())),ceil(log2(len(signature))))
    for h in G:
        for g in (G[0],G[91],G[-1]):
            gh=tuple(g[h[i]] for i in range(6))
            assert act(inv(gh),mark)==act(inv(h),act(inv(g),mark))
            rotation_checks+=1
for mask in range(16):
    for g in G:
        for q in D:
            assert bool(mask&(1<<pos(q)))==bool(mask&(1<<pos(act(g,q))))
            law_checks+=1
q=((0,1),(1,1),(2,1)); other=((0,1),(1,1),(3,1))
assert pos(q)==pos(other)==3 and q!=other
print({'orbits':orbits,'classes':classes,'invariant_laws':16,
'law_checks':law_checks,'query_checks':query_checks,'rotation_checks':rotation_checks,
'witness':(q,other),'mismatches':0})
