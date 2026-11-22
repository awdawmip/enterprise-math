#!/usr/bin/env python3
"""T6 maximal-p13, valuation-one order3 (0,3)/(1,2) exact finite audit.
Reuses original published p13 q0->q1->q2 exact saturated lattice chain.
Author finite proof only, not independent review or formal Native Result.
"""
import importlib.util
from itertools import combinations_with_replacement
from pathlib import Path
from sympy import Matrix

src=Path(__file__).with_name("T6_P13_Q2_ALL_SPLITS_GLOBAL_AFFINE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p13_q2",src)
prev=importlib.util.module_from_spec(spec)
spec.loader.exec_module(prev)
P,N=prev.P,prev.N
for r in range(1,P):
    prev.search.__globals__['atom'][(3,r)]=Matrix(1,N,prev.prior.particular(3,r))

states3=[[(3,r)] for r in range(1,P)]
states3.extend([[(1,r),(2,s)] for r in range(1,P) for s in range(1,P)])
states3.extend([[(1,r) for r in rs] for rs in
                combinations_with_replacement(range(1,P),3)])
assert len(states3)==520
states2=[[(2,r)] for r in range(1,P)]
states2.extend([[(1,r),(1,s)] for r,s in
                combinations_with_replacement(range(1,P),2)])
assert len(states2)==90
s03=[prev.search(st,[]) for st in states3]
s12=[prev.search([(1,r)],st) for r in range(1,P)
     for st in states2 if not set([(1,r)]).intersection(st)]
def record(v):
    return {'raw':len(v),'GS_nodes':sum(t[0] for t in v),
            'sphere_leaves':sum(t[1] for t in v),
            'budget_valid':sum(t[2] for t in v)}
summary={'0,3':record(s03),'1,2':record(s12)}
assert summary=={
 '0,3':{'raw':520,'GS_nodes':2075,'sphere_leaves':0,'budget_valid':0},
 '1,2':{'raw':936,'GS_nodes':3417,'sphere_leaves':1,'budget_valid':0}}
# The one relaxed-sphere leaf: exact 13-adic congruences but side masses too large.
u=[39,21,33,-8,1,-19,0,-2,5,-3,-5,-4]
for j in range(1,7):
    mod=P**j
    assert (sum(x*pow(r,-j,mod) for r,x in enumerate(u,1))+
            pow(18,-j,mod)-pow(17,-j,mod)-pow(19,-j,mod))%mod==0
q0plus=sum(w*max(0,x) for w,x in zip(prev.W,u))
q0minus=sum(w*max(0,-x) for w,x in zip(prev.W,u))
assert (q0plus,q0minus)==(2891,3794)
assert (q0plus+233,q0minus+466)==(3124,4260)
assert sum((w*x)**2 for w,x in zip(prev.W,u))==5795199<=7879829
print('AUTHOR_EXACT_P13_ORDER3_RESULT',summary)
print('unique_relaxed_leaf',{'plus':[(1,5)],'minus':[(1,4),(1,6)],
      'q0_signed':u,'original_masses':[3124,4260],
      'budget_valid':False,'global_T6':'OPEN'})
