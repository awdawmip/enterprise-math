#!/usr/bin/env python3
"""Exact half-path BRC check and finite sixth-root saddle certificate."""
from collections import defaultdict
from itertools import combinations, product
from math import comb

AXES=range(6)
PORTS=list(combinations(AXES,2))
SUPPORTS=list(combinations(AXES,3))
EDGES=[]
for i,p in enumerate(PORTS):
    for j,q in enumerate(PORTS):
        if i != j and len(set(p)&set(q))==1:
            support=tuple(sorted(set(p)|set(q)))
            EDGES.append((i,j,support))
assert len(EDGES)==15*8
assert {s:sum(1 for _,_,t in EDGES if s==t) for s in SUPPORTS}=={s:6 for s in SUPPORTS}

# Exhaust all sixth-root phases theta_i = k_i*pi/3, checking the maximal-modulus necessary condition
mag=bal=[]
mag=[];bal=[]
for k in product(range(6), repeat=6):
    t=[sum(k[i] for i in s) for s in SUPPORTS]
    if all(v%3==0 for v in t):
        mag.append(k)
        if len({(v//3)%2 for v in t})==1:
            bal.append(k)
assert len(mag)==192, len(mag)
assert len(bal)==6 and set(bal)==set((a,)*6 for a in range(6)),bal

# Gram check: includes every ordered Port transition and independently selected +/- support increment.
adj=[[] for _ in PORTS]
for i,j,s in EDGES: adj[i].append((j,s))
state={(0,(0,)*6):1}
results=[]
expected=[1,16,624,34688,2413424,200986368,19705107552]
for r in range(6):
    k=sum(n*n for n in state.values())
    assert k==expected[r],(r,k,expected[r])
    assert sum(state.values())==16**r
    results.append({'r':r,'m':2*r,'K_m':str(k),'half_path_fibers':len(state)})
    if r<5:
        nxt=defaultdict(int)
        for (p,v),c in state.items():
            for q,s in adj[p]:
                for sign in (-1,1):
                    w=tuple(v[i]+sign*(i in s) for i in AXES)
                    nxt[(q,w)]+=c
        state=nxt
# Exact covariance, derived directly from all 120 directed Port edges.
assert all(sum(i in s for _,_,s in EDGES)==60 for i in AXES)
assert all(sum(i in s and j in s for _,_,s in EDGES)==24 for i in AXES for j in AXES if i<j)
print('PASS R762HX')
print('periodic sixth-root candidates =',len(mag),'; gauge-balanced peaks =',len(bal))
print('support covariance diag=1/2, offdiag=1/5, det=729/200000')
print('K_m exact BRC Gram counts:',results)
