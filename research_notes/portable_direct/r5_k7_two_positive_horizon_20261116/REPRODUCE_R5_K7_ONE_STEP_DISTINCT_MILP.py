#!/usr/bin/env python3
"""R5 seven-cycle one-step positive Set MILP, distinct undominated source centres.
Requires scipy 1.17.0 / HiGHS; solver infeasibility is numerical evidence,
not a separately supplied formal unsatisfiability certificate.
"""
import json
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix
K=7; N=1<<K
q=[sum(((u>>i)&1)*((u>>((i+1)%K))&1) for i in range(K)) for u in range(N)]
G=[sum(1<<u for u in range(N) if not (u&~r) and 0<=q[r]-q[u]<=2) for r in range(N)]
C=[r for r in range(N) if not any(r!=z and (G[r]&~G[z])==0 for z in range(N))]
assert len(C)==57
U=[[u|(1<<a) for u in range(N)] for a in (0,1)]
index=0
x={r:i for i,r in enumerate(C)};index+=len(C)
y={}
for r in C:
    for a in range(2):
        for t in C:y[r,a,t]=index;index+=1
z={}
for u in range(N):
    for r in C:
        if G[r]>>u&1:z[u,r]=index;index+=1
rows=[];cols=[];vals=[];lo=[];hi=[]
def constraint(pairs,lower,upper):
    row=len(lo);lo.append(lower);hi.append(upper)
    for j,v in pairs:
        rows.append(row);cols.append(j);vals.append(v)
for r in C:
    for a in range(2):
        constraint([(y[r,a,t],1) for t in C]+[(x[r],-1)],0,0)
for (r,a,t),j in y.items():
    constraint([(j,1),(x[t],-1)],-np.inf,0)
for u in range(N):
    constraint([(z[u,r],1) for r in C if (u,r) in z],1,np.inf)
for (u,r),j in z.items():
    for a in range(2):
        constraint([(j,1)]+[(y[r,a,t],-1) for t in C if G[t]>>U[a][u]&1],-np.inf,0)
# This upper bound is explicit because we are testing a fixed size.
constraint([(x[r],1) for r in C],-np.inf,18)
A=coo_matrix((vals,(rows,cols)),shape=(len(lo),index)).tocsc()
obj=np.zeros(index)
for r in C:obj[x[r]]=1
result=milp(obj,integrality=np.ones(index),bounds=Bounds(np.zeros(index),np.ones(index)),
            constraints=LinearConstraint(A,np.array(lo),np.array(hi)),
            options={'time_limit':70,'mip_rel_gap':0.0})
print(json.dumps({'status':int(result.status),'message':result.message,
                  'centres':len(C),'raw_states':N,'variables':index,
                  'constraints':len(lo),'nonzeros':len(vals),
                  'size_cap':18,'objective':None if result.fun is None else float(result.fun),
                  'mip_gap':None if getattr(result,'mip_gap',None) is None else float(result.mip_gap),
                  'review':'NOT_REVIEWED'},indent=2))
assert result.status==2, 'Expected HiGHS infeasible for M<=18 in distinct/nondominated model'
