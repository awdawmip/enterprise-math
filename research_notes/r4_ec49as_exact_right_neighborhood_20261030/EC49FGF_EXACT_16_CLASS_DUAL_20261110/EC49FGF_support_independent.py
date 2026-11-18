#!/usr/bin/env python3
"""Independent exact DFA/count-state coverage audit; standard library only."""
from collections import defaultdict
from itertools import combinations
from VERIFY_EC49FGF import OPS,T,SIG,REQ,BASE,EARLY,LATE
cur={(0,0,0,0,0,0)};cover=defaultdict(set);live={}
for h in range(1,10):
    nxt=set()
    for q,e,a,b,f,g in cur:
        for j,op in enumerate(OPS):
            nq=T[q][j]
            if nq==8:continue
            nxt.add((nq,e+(op=='e'),a+(op=='a'),b+(op in ('c','d')),
                     f+(op=='f'),g+(op=='g')))
    cur=nxt;live[h]=len(cur)
    if h in REQ:
        for q,e,a,b,f,g in cur:
            if e==a+1 and SIG[q] in REQ[h]:
                cover[2*e+b+f,b+g,e].add((h,SIG[q]))
forced={(3,0,1),(2,1,1)}
demand={(h,s) for h in REQ for s in REQ[h]}
covers=[]
for tri in combinations(sorted(set(cover)-forced),3):
    ks=forced|set(tri)
    if set().union(*(cover[k] for k in ks))==demand:
        covers.append(frozenset(ks))
expected={frozenset(set(BASE)|{a,b}) for a in EARLY for b in LATE}
assert len(cover)==94 and set(covers)==expected and len(covers)==16
print('SUPPORT_VERIFIED',len(cover),'eligible raw keys,',len(covers),'five-key profiles, H9 live states',live[9])
