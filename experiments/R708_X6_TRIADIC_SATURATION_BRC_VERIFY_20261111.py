#!/usr/bin/env python3
"""R708 exact test, candidate equal-q Cell-local three-distinct-axis partitions."""
from itertools import product,combinations
from functools import lru_cache
from math import factorial
from fractions import Fraction

@lru_cache(None)
def D(n):
    if not any(n): return 1
    if sum(n)%3: return 0
    a=next(i for i,v in enumerate(n) if v)
    s=0
    for b,c in combinations([i for i in range(6) if i!=a and n[i]>0],2):
        q=list(n)
        for i in (a,b,c):q[i]-=1
        s+=n[b]*n[c]*D(tuple(q))
    return s

def greedy(n):
    r=list(n); answer=[]
    while any(r):
        t=sorted(range(6),key=lambda i:(-r[i],i))[:3]
        if any(r[i]==0 for i in t): return None
        for i in t: r[i]-=1
        answer.append(tuple(t))
    return answer

def weights(n,i,j):
    out={}
    for k in range(6):
        if k in (i,j) or n[k]==0: continue
        q=list(n)
        for a in (i,j,k): q[a]-=1
        out[k]=n[k]*D(tuple(q))
    return out

profiles=feasible=pair_checks=two_sat=0
for n in product(range(4),repeat=6):
    if sum(n)%3: continue
    profiles+=1
    m=sum(n)//3
    can=max(n)<=m
    assert (D(n)>0)==can
    if not can: continue
    feasible+=1
    g=greedy(n)
    assert g is not None and len(g)==m
    assert tuple(sum(i in t for t in g) for i in range(6))==n
    sat={i for i in range(6) if n[i]==m and m>0}
    if len(sat)>=2:
        two_sat+=1
        assert D(n)==factorial(m)**2
    for i,j in combinations([a for a in range(6) if n[a]>0],2):
        w=weights(n,i,j)
        got={k for k,v in w.items() if v>0}
        expected={k for k in range(6) if k not in (i,j)
                  and n[k]>0 and sat.issubset({i,j,k})}
        assert got==expected
        assert sum(w.values())<=D(n)
        pair_checks+=1

a=(3,3,3,0,0,0);b=(3,3,1,1,1,0)
assert D(a)==D(b)==36
assert weights(a,0,1)=={2:12}
assert weights(b,0,1)=={2:4,3:4,4:4}
assert sum(weights(b,2,3).values())==0
assert Fraction(sum(weights(b,0,1).values()),D(b))==Fraction(1,3)
assert (profiles,feasible,pair_checks,two_sat)==(1366,1135,10755,390)
print("R708_X6_TRIADIC_SATURATION_BRC_EXACT_PASS",profiles,feasible,pair_checks,two_sat)
