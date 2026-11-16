#!/usr/bin/env python3
"""Exact one-operation horizon obstruction: genuine-source k=6 J={0,1} slack=2.
Input pin 435e77af0d180eac32bd1f9c4c464bc4010b7551; Python standard library.
"""
from collections import Counter
from itertools import product
import json

K,N,M=6,64,10
FULL=(1<<N)-1
q=[sum(((r>>i)&1)*((r>>((i+1)%K))&1) for i in range(K)) for r in range(N)]
G=[sum(1<<u for u in range(N) if (u&~r)==0 and 0<=q[r]-q[u]<=2) for r in range(N)]
centres=tuple(r for r in range(N) if not any(r!=z and (G[r]&~G[z])==0 for z in range(N)))
assert len(centres)==22
NEXT=[[(u&~(1<<i))|(b<<i) for u in range(N)] for i,b in ((0,0),(0,1),(1,0),(1,1))]
serves=[tuple(j for j,r in enumerate(centres) if (G[r]>>u)&1) for u in range(N)]
covers=set()

def search(chosen,mask):
    if mask==FULL:
        if len(chosen)==M:covers.add(tuple(sorted(centres[j] for j in chosen)))
        return
    if len(chosen)>=M:return
    u=min((u for u in range(N) if not ((mask>>u)&1)),
          key=lambda v:sum(j not in chosen for j in serves[v]))
    for j in serves[u]:
        if j not in chosen:search(chosen+(j,),mask|G[centres[j]])
search((),0)
assert len(covers)==116

unavailable=0
coverage_hist=Counter()
family_results=[]
for C in sorted(covers):
    unique=[[] for _ in range(M)]
    for u in range(N):
        js=[j for j,r in enumerate(C) if (G[r]>>u)&1]
        if len(js)==1:unique[js[0]].append(u)
    options=[[tuple(j2 for j2,r2 in enumerate(C) if all((G[r2]>>NEXT[op][u])&1 for u in unique[j]))
              for op in range(4)] for j in range(M)]
    if any(not opts for row in options for opts in row):
        unavailable+=1
        continue
    floating=[(j,op,opts) for j,row in enumerate(options) for op,opts in enumerate(row) if len(opts)>1]
    fixed=[[opts[0] for opts in row] for row in options]
    best=0
    local=Counter()
    for assignment in product(*(z[2] for z in floating)):
        tab=[row[:] for row in fixed]
        for (j,op,_),target in zip(floating,assignment):tab[j][op]=target
        # A raw initial u is one-step feasible iff some chosen output state
        # covers u and all 4 image snapshots after an operation.
        good=sum(any((G[r]>>u)&1 and all((G[C[tab[j][op]]]>>NEXT[op][u])&1 for op in range(4))
                     for j,r in enumerate(C)) for u in range(N))
        coverage_hist[good]+=1
        local[good]+=1
        best=max(best,good)
    family_results.append({'centres':list(C),'free_edges':len(floating),
                           'tables':sum(local.values()),'max_initial_snapshots':best,
                           'coverage_histogram':dict(sorted(local.items()))})
assert unavailable==110
assert len(family_results)==6
assert sum(coverage_hist.values())==584
assert max(coverage_hist)<N

# One explicit static witness (zero-operation horizon): all raw states covered.
static=list(sorted(covers)[0])
assert all(any((G[r]>>u)&1 for r in static) for u in range(N))

# Eleven-state upper witness inherited from the exact coherent-cube construction.
witness=(( (0,1),(60,61,62,63) ),((),(51,)),((),(43,)),
         ((1,),(37,39)),((),(27,)),((),(23,)),((),(15,)))
assert sum(len(c) for _,c in witness)==11
for t in range(16):
    assert any(all((G[cs[sum(((a>>i)&1)<<h for h,i in enumerate(S))]]>>((t<<2)|a))&1
                   for a in range(4)) for S,cs in witness)

out={'status':'PASS_R5_K6_SHARP_HORIZON_ONE_NO_TEN',
     'science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
     'model':'canonical genuine-source ring k=6, slack2, named Set on bits 0,1',
     'raw_states':N,'source_centres':N,'nondominated_centres':len(centres),
     'static_ten_centre_covers':len(covers),
     'rejected_by_unique_raw_one_step':unavailable,
     'remaining_centre_families':len(family_results),
     'one_step_transition_tables_exhausted':sum(coverage_hist.values()),
     'one_step_coverage_histogram':dict(sorted(coverage_hist.items())),
     'maximum_one_step_coverage':max(coverage_hist),
     'families':family_results,'static_ten_centre_witness':static,
     'zero_horizon_minimum':10,'one_horizon_minimum':11,
     'eleven_state_witness':'R5_TWO_CONTROL_CUBE_COVER_THEOREM.md',
     'review':'NOT_REVIEWED'}
print(json.dumps(out,sort_keys=True,indent=2))
