#!/usr/bin/env python3
"""Independent 0-1 native prefix tree formulation, checked on two witnessed M4 strata.
Unlike OR-mask DP, minimize binary active node/edge variables under ancestor-closure
and terminal-cover linear constraints using SciPy HiGHS MILP.
"""
import json,subprocess
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_array
from MODEL_EC49EU import P0
import EC49EW_S4_SEARCH as a
import EC49EW_S6_SEARCH as b
ROOT=Path(__file__).parent
S4=(P0,)+tuple(tuple([*p,0,0,0]) for p in [(4,2,1),(4,2,1),(4,3,1),(5,4,1),(5,4,1)])
S6=(P0,)+tuple(tuple([*p,0,0,0]) for p in [(3,1,1),(3,2,1),(3,3,1),(4,4,1),(4,4,1)])

def solve(label,ps,trie_fn,expected):
 data,n,*_=trie_fn(ps)
 lines=data.splitlines();N,K=map(int,lines[0].split());assert N==n
 par=[];paid=[];masks=[]
 for line in lines[1:]:
  i,j,k=map(int,line.split());par.append(i);paid.append(j);masks.append(k)
 assert len(par)==N
 rows=[];cols=[];vals=[];lb=[];ub=[]
 def row(entries,L,U):
  r=len(lb)
  for c,v in entries:rows.append(r);cols.append(c);vals.append(float(v))
  lb.append(float(L));ub.append(float(U))
 for i in range(1,N):row([(par[i],1),(i,-1)],0,np.inf)
 for k in range(K):
  terms=[i for i in range(N) if masks[i]&(1<<k)]
  assert terms
  row([(i,1) for i in terms],1,np.inf)
 A=coo_array((np.array(vals,dtype=np.float64),(np.array(rows,dtype=np.int32),np.array(cols,dtype=np.int32))),shape=(len(lb),N)).tocsr()
 obj=np.array([0 if i==0 or paid[i] else 1 for i in range(N)],dtype=float)
 lower=np.zeros(N);lower[0]=1
 for i in range(1,N):
  if paid[i]:lower[i]=1
 bounds=Bounds(lower,np.ones(N))
 result=milp(c=obj,integrality=np.ones(N,dtype=np.int32),bounds=bounds,constraints=LinearConstraint(A,np.array(lb),np.array(ub)),options={'time_limit':24,'mip_rel_gap':0})
 actual=float(result.fun+28) if result.fun is not None else None
 if result.status==0:assert round(actual)==expected,(label,actual,expected)
 return {'case':label,'nodes':N,'required_terminal_colors':K,'milp_variables':N,'constraints':len(lb),'solver_status':int(result.status),'solver_message':result.message,'total_E':actual,'dual_lower_bound':float(result.mip_dual_bound+28) if result.mip_dual_bound is not None else None,'gap':float(result.mip_gap) if result.mip_gap is not None else None,'expected':expected}
res=[solve('H7_M4_S4',S4,a.trie,92),solve('H7_M4_S6_T2T4',S6,b.trie,72)]
report={'status':'PASS' if all(r['solver_status']==0 for r in res) else 'PARTIAL','model':'independent 0-1 MILP terminal cover, tree closure and paid edges','cases':res}
(ROOT/'EC49EW_MILP_EXECUTED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
