from VERIFY_EC49FBK_MIN import *
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
BASE=('fe','ge','feg','gef')
L=(5,2,1)
words={}
for h in (4,5,6):
 d=eligible(h,L)
 for w,t in d.items():words[(h,w)]=sig(w)
par=[-1];nodes=[{}];fixed=set();term={}
for h,w in [(-1,w) for w in BASE]+list(words):
 at=0
 for step in native(w):
  if step not in nodes[at]:
   nodes[at][step]=len(par);par.append(at);nodes.append({})
  at=nodes[at][step]
  if h==-1:fixed.add(at)
 if h!=-1:term[(h,w)]=at
clauses=[(h,s) for h in (4,5,6) for s in ((1,2,4,8) if h<=5 else (16,32))]
lo=[];hi=[];rows=[];cols=[];vals=[]
for v in range(1,len(par)):
 if par[v]:
  j=len(lo);lo.append(-np.inf);hi.append(0);rows+= [j,j];cols+=[v-1,par[v]-1];vals+=[1,-1]
for h,s in clauses:
 vs=[v for (k,w),v in term.items() if h==k and words[(k,w)]==s]
 j=len(lo);lo.append(1);hi.append(np.inf)
 for v in vs:rows.append(j);cols.append(v-1);vals.append(1)
n=len(par)-1
cost=np.ones(n);lb=np.zeros(n);ub=np.ones(n)
for v in fixed:cost[v-1]=0;lb[v-1]=1
A=coo_matrix((vals,(rows,cols)),shape=(len(lo),n)).tocsr()
sol=milp(cost,integrality=np.ones(n),bounds=Bounds(lb,ub),constraints=LinearConstraint(A,lo,hi),options={'mip_rel_gap':0,'time_limit':60})
print('status',sol.status,'fun',sol.fun,'dual',sol.mip_dual_bound,'gap',sol.mip_gap,'nodes',n)
selected=[]
for h,s in clauses:
 for (k,w),v in term.items():
  if k==h and words[(k,w)]==s and sol.x[v-1]>.5:
   selected.append((h,w,s));break
print(selected)
prev=set()
for w in BASE:
 t=native(w);prev.update(t[:j] for j in range(1,len(t)+1))
for h,w,s in selected:
 t=native(w);prev.update(t[:j] for j in range(1,len(t)+1))
print('early_edges',len(prev),'N',len(selected))
for h,w,s in selected:
 t=native(w+'fff');prev.update(t[:j] for j in range(1,len(t)+1))
print('lifted_edges',len(prev))
