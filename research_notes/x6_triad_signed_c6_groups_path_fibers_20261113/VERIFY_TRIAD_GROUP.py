#!/usr/bin/env python3
"""Exact exhaustive finite signed-permutation enumeration for X6 triad candidate families."""
from collections import deque
from itertools import combinations
from math import factorial
import json
N=6
I=tuple(range(1,N+1))
def compose(f,g): return tuple((1 if x>0 else -1)*f[abs(x)-1] for x in g)
def gen(i,j,k,l=None):
    a=list(I);a[i]=j+1;a[j]=k+1;a[k]=-(i+1)
    if l is not None:
        assert l not in (i,j,k)
        a[l]=-(l+1)
    return tuple(a)
def closure(gens):
    found={I};q=deque([I])
    while q:
        a=q.popleft()
        for b in gens:
            c=compose(a,b)
            if c not in found:found.add(c);q.append(c)
    return found
def stats(g):
    p={tuple(abs(v) for v in a) for a in g}
    k={a for a in g if tuple(abs(v) for v in a)==I}
    return len(g),len(p),len(k)
triads=list(combinations(range(N),3))
uncomp=[gen(*t) for t in triads]
comp=[gen(*t,l) for t in triads for l in range(N) if l not in t]
g1=closure(uncomp);g2=closure(comp)
assert (len(uncomp),stats(g1)) == (20,(23040,360,64))
assert (len(comp),stats(g2)) == (60,(11520,360,32))
assert all(sum(v<0 for v in a)%2==0 for a in g2)
def words(a,b):
    d=[y-x for x,y in zip(a,b)]
    m=sum(abs(x) for x in d)
    v=factorial(m)
    for x in d:v//=factorial(abs(x))
    return m,v
e1=(1,0,0,0,0,0);e2=(0,1,0,0,0,0);e3=(0,0,1,0,0,0)
assert words(e1,e2)==words(e2,e3)==words(e1,e3)==(2,2)
result={"status":"PASS_X6_TRIAD_GROUPS_EXACT","frozen_source":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "uncompensated":{"generators":20,"group":"(C2)^6 semidirect A6","orders":stats(g1),"det_each":-1},
        "compensated":{"generators":60,"group":"(C2)^5 semidirect A6","orders":stats(g2),"det_each":1},
        "witness":{"concatenated_count":4,"concatenated_length":4,"direct_count":2,"direct_length":2}}
print(json.dumps(result,ensure_ascii=False,indent=2))
