#!/usr/bin/env python3
"""Exact enumeration certificate for R750. Finite typed Port graph, no physical propagation."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
D=6
ports=[(i,s) for i in range(D) for s in (-1,1)]
V=tuple(frozenset(p) for p in combinations(ports,2) if p[0][0]!=p[1][0])
axis=lambda v:frozenset(x[0] for x in v)
edge=lambda v,w:len(v&w)==1 and len({x[0] for x in v|w})==3
adj={v:tuple(w for w in V if edge(v,w)) for v in V}
assert len(V)==60 and all(len(adj[v])==16 for v in V)
for v in V:
 for w in adj[v]:
  z=v^w
  assert z in adj[w] and (w^z)==v
  assert axis(z)==axis(v)^axis(w)
rows=[]
for n in range(1,5):
 ambient=[(v,) for v in V]
 for _ in range(n-1):
  ambient=[p+(w,) for p in ambient for w in adj[p[-1]]]
 a=Counter(tuple(axis(v) for v in p) for p in ambient)
 if n==1: fixed=ambient
 else:
  fixed=[]
  for v in V:
   for w in adj[v]:
    seq=[v,w]
    while len(seq)<n:seq.append(seq[-2]^seq[-1])
    fixed.append(tuple(seq))
 f=Counter(tuple(axis(v) for v in p) for p in fixed)
 assert len(ambient)==60*16**(n-1)
 assert len(a)==15*8**(n-1)
 assert len(fixed)==(60 if n==1 else 960)
 assert len(f)==(15 if n==1 else 120)
 assert set(f)<=set(a)
 assert set(f.values())==({4} if n==1 else {8})
 assert set(a.values())=={2**(n+1)}
 assert set(fixed)<=set(ambient)
 tvs=Fraction(0) if n<2 else 1-Fraction(1,16**(n-2))
 tvu=Fraction(0) if n<2 else 1-Fraction(1,8**(n-2))
 rows.append(dict(n=n,resampled_signed=len(ambient),resampled_unsigned=len(a),
                  fixed_signed=len(fixed),fixed_unsigned=len(f),
                  signed_lifts=2**(n+1),fixed_sign_lifts=(4 if n==1 else 8),
                  signed_tv=str(tvs),unsigned_tv=str(tvu),
                  signed_divergence_bits=4*max(0,n-2),
                  unsigned_divergence_bits=3*max(0,n-2),
                  conditional_sign_bits=max(0,n-2)))
out=dict(result="R750_X6_C1_OBSERVER_TOWER_EXACT_PASS",d=D,
         signed_states=60,unsigned_states=15,signed_degree=16,unsigned_degree=8,
         verified_signed_directed_edges=960,n_values=[1,2,3,4],rows=rows,
         native_v29_v39_executed=False)
print(json.dumps(out,indent=2,ensure_ascii=False))
