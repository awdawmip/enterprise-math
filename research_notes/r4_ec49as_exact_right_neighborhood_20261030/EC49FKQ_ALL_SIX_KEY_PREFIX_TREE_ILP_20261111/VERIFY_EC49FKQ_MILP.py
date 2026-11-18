#!/usr/bin/env python3
"""Exact integer MIP encoding for frozen six-key BRC signed native microstep prefix tree.
If solver reaches optimality, proof is relative to the HiGHS 0-1 MIP solve.
Explicit witnesses are independently checked as exact signed native paths.
This is the actually executed EC49FKQ code (local original filename TRY_SIX_KEY_TREE_MILP.py).
"""
import sys,time,json,collections
from EC49FGW_RADIUS5_SCREEN import all_words,pref,raw_key,REQ
import numpy as np
import scipy.sparse as sp
from scipy.optimize import Bounds, LinearConstraint, milp
BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1)}
EXTRAS=[((5,4,1),(5,5,1)), ((5,4,1),(6,4,1)), ((6,3,1),(6,4,1)), ((6,3,1),(7,3,1)), ((6,4,1),(6,6,1)), ((6,4,1),(7,5,1)), ((6,4,1),(7,6,1)), ((6,4,1),(8,4,1)), ((6,4,1),(8,5,1))]
idx=int(sys.argv[1]) if len(sys.argv)>1 else 0
T=float(sys.argv[2]) if len(sys.argv)>2 else 40
key=BASE|set(EXTRAS[idx]); words=[(a,w,pref(w)) for a,w in all_words() if raw_key(w) in key]
node={p:j for j,p in enumerate(sorted({p for a,w,ps in words for p in ps},key=lambda x:(len(x),x)))}
num=len(node); bylab=collections.defaultdict(set)
for a,w,ps in words: bylab[a].add(node[ps[-1]])
assert len(bylab)==24
parent=[]
for p,j in node.items():
 parent.append(node.get(p[:-1],-1))
assert all(parent[j]<j for j in range(num) if parent[j]>=0)
rr=[];cc=[];vv=[]; lb=[];ub=[]
for j,k in enumerate(parent):
 if k<0:continue
 i=len(lb);rr.extend([i,i]);cc.extend([j,k]);vv.extend([1,-1]);lb.append(-np.inf);ub.append(0.)
for a,ks in bylab.items():
 i=len(lb)
 for j in ks:rr.append(i);cc.append(j);vv.append(1.)
 lb.append(1.);ub.append(np.inf)
A=sp.coo_matrix((vv,(rr,cc)),shape=(len(lb),num)).tocsr()
print('SIZE',idx,'words',len(words),'nodes',num,'constraints',len(lb), 'labels', len(bylab),flush=True)
r=milp(c=np.ones(num), integrality=np.ones(num), bounds=Bounds(0,1),constraints=LinearConstraint(A,np.array(lb),np.array(ub)),options={'time_limit':T,'mip_rel_gap':0.0})
print('SOLVER',idx,'status',r.status,'message',r.message,'primal',r.fun,'bound',getattr(r,'mip_dual_bound',None),'gap',getattr(r,'mip_gap',None),flush=True)
if r.x is not None:
 selected={p for p,j in node.items() if r.x[j]>0.5}; chosen={}
 for a,w,ps in words:
  if a not in chosen and ps[-1] in selected:chosen[a]=w
 assert len(chosen)==24
 cost=len(set().union(*(set(pref(w)) for w in chosen.values())))
 assert cost<=len(selected)
 print('WITNESS',cost, 'solver_selected',len(selected), 'labels',len(chosen),flush=True)
 path=f'MIP_WITNESS_{idx}.json';open(path,'w').write(json.dumps({'set_index':idx,'keys':sorted(map(list,key)),'solver_status':int(r.status),'solver_bound':r.mip_dual_bound,'cost':cost,'demand_words':{f'{a[0]}-{a[1]}':w for a,w in sorted(chosen.items())}},indent=2)+'\n')
