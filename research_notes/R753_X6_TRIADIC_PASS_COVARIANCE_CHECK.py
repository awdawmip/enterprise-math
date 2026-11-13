#!/usr/bin/env python3
"""R753 exact finite cyclic-port BRC/V29 checker. Standard library only."""
from itertools import combinations, permutations, product

D=6
SIGN=(-1,1)
AXES=range(D)

def canon(seq):
    t=tuple(seq)
    return min(t[i:]+t[:i] for i in range(3))

def states():
    out=set()
    for aa in combinations(AXES,3):
        for ss in product(SIGN, repeat=3):
            p=tuple(zip(aa,ss))
            out.add(canon(p))
            out.add(canon((p[0],p[2],p[1])))
    return sorted(out)

def batch(x):
    return frozenset((x[i], x[(i+1)%3]) for i in range(3))

def relabel(x,g):
    return canon(tuple((g[a],s) for a,s in x))

def relabel_batch(b,g):
    return frozenset((((g[a],s),(g[c],t))) for ((a,s),(c,t)) in b)

def sign_flip(x):
    return canon(tuple((a,-s) for a,s in x))

def oneedge(x):
    i=min(range(3),key=lambda j:x[j][0])
    return x[i],x[(i+1)%3]

def main():
    X=states()
    assert len(X)==320
    BX=[batch(x) for x in X]
    assert all(len(b)==3 for b in BX) and len(set(BX))==320
    assert all(batch(sign_flip(x)) != batch(x) for x in X)
    # Same directed-edge multiplicity at source and sink: Delta u = 0.
    for b in BX:
        for p in set(sum(([a,c] for a,c in b), [])):
            assert sum(a==p for a,c in b)==sum(c==p for a,c in b)
    checks=0
    for g in permutations(AXES):
        for x in X:
            assert batch(relabel(x,g)) == relabel_batch(batch(x),g)
            checks+=1
    assert checks==230400
    x=canon(((0,1),(1,1),(2,1)))
    g=(1,0,2,3,4,5)
    assert oneedge(relabel(x,g)) != tuple((g[a],s) for a,s in oneedge(x))
    twins=sum(1 for x in X if x<sign_flip(x))
    assert twins==160
    print("R753_X6_TRIADIC_PASS_EQUIVARIANT_BATCH_EXACT_PASS")
    print(dict(states=len(X), distinct_ledgers=len(set(BX)),
               covariance_checks=checks, sign_twin_pairs=twins,
               passes_per_batch=3, one_pass_equivariant_selector=False))
if __name__=="__main__":
    main()
