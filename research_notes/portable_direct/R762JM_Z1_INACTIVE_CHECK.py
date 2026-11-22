#!/usr/bin/env python3
"""Finite exact check of 92 inactive-Port sets for each single missing support."""
from itertools import combinations
from collections import Counter
import json

A=range(6)
P=list(combinations(A,2))
S=list(combinations(A,3))
Pidx={p:i for i,p in enumerate(P)}
TRI={s:set(Pidx[p] for p in combinations(s,2)) for s in S}

def is_matching(M):
    return len({a for k in M for a in P[k]})==2*len(M)

ans=[]
for z in S:
    eligible=[]
    for mask in range(1<<15):
        M={k for k in range(15) if mask>>k&1}
        if all(len(M&ports)<=1 for s,ports in TRI.items() if s!=z):
            eligible.append(M)
    hist=Counter(map(len,eligible))
    ms=sum(is_matching(m) for m in eligible)
    nm=len(eligible)-ms
    assert len(eligible)==92 and ms==76 and nm==16
    assert dict(sorted(hist.items()))=={0:1,1:15,2:48,3:25,4:3}
    Z=TRI[z]
    outside={i for i,p in enumerate(P) if set(p).isdisjoint(z)}
    for M in eligible:
        if not is_matching(M):
            assert len(M&Z)>=2 and len(M-Z)<=1 and M-Z<=outside
    ans.append({'missing_support':z,'eligible_sets':len(eligible),
                'matchings':ms,'nonmatchings':nm,'by_size':dict(sorted(hist.items()))})

print(json.dumps({'result':'PASS','missing_support_choices':len(S),
    'per_missing_support':{'total':92,'matchings':76,'nonmatchings':16,
    'by_size':{0:1,1:15,2:48,3:25,4:3}},
    'total_labelled_missing_support_and_inactive_port_pairs':sum(q['eligible_sets'] for q in ans),
    'scope':'LOCAL_SUPPORT_POSITIVITY_ONLY; NOT EVEN_DEGREE OR EULER'},
    ensure_ascii=False,indent=2))
