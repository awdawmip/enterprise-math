#!/usr/bin/env python3
"""Complete 24-label, fixed-five-key integer trie optimization (SciPy/HiGHS).
Requires scipy >= 1.11 and numpy. Solved zero-gap MIP is finite computation evidence.
"""
from collections import defaultdict
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix
import numpy as np, json
from VERIFY_EC49FGE import OPS,T,SIG,STEPS,NEED,EXPECTED_FIVE,W,native

def candidates(h,k):
 x,y,z=k
 a=z-1; r=x+y-h-1; f=h+1-y-2*z; g=h+1-x
 if min(a,r,f,g)<0:return ()
 words=[]
 for c in range(r+1):
  left=[a,c,r-c,z,f,g]
  def visit(s,q):
   if len(s)==h:
    if SIG[q] in NEED[h]:words.append((SIG[q],s))
    return
   for i,t in enumerate(OPS):
    if left[i]:
     nq=T[q][i]
     if nq==8:continue
     left[i]-=1;visit(s+t,nq);left[i]+=1
  visit('',0)
 return words

def run():
 nodes={'':0}; parent=[-1]; weight=[0]; child=[{}]; need=defaultdict(set)
 for h in NEED:
  for k in sorted(EXPECTED_FIVE):
   for sig,w in candidates(h,k):
    root=0;prefix=''
    for c in w:
     prefix+=c
     if prefix not in nodes:
      new=len(parent);nodes[prefix]=new;parent.append(root);weight.append(len(STEPS[c]));child.append({});child[root][c]=new
     root=nodes[prefix]
    need[(h,sig)].add(root)
 assert len(need)==24
 N=len(parent)-1
 rows=[];cols=[];vals=[];lower=[];upper=[]
 def add(terms,low,high):
  idx=len(lower)
  for col,val in terms:rows.append(idx);cols.append(col);vals.append(val)
  lower.append(low);upper.append(high)
 for i in range(1,len(parent)):
  if parent[i]:add(((i-1,1),(parent[i]-1,-1)),-np.inf,0)
 for h in NEED:
  for sig in NEED[h]:
   add(((n-1,1) for n in need[(h,sig)]),1,np.inf)
 discount=[]
 for p,kids in enumerate(child):
  for a,b in (('c','f'),('d','g')):
   if a in kids and b in kids:
    var=N+len(discount);discount.append((p,a,b))
    add(((var,1),(kids[a]-1,-1)),-np.inf,0)
    add(((var,1),(kids[b]-1,-1)),-np.inf,0)
 objective=np.asarray(weight[1:]+[-1]*len(discount),dtype=float)
 A=coo_matrix((vals,(rows,cols)),shape=(len(lower),len(objective))).tocsr()
 ans=milp(objective,integrality=np.ones(len(objective)),bounds=Bounds(0,1),constraints=LinearConstraint(A,lower,upper),options={'mip_rel_gap':0.0,'time_limit':60})
 assert ans.status==0 and ans.fun==112 and ans.mip_dual_bound==112 and ans.mip_gap==0,ans
 P=set()
 for group in W.values():
  for w in group.values():
   seq=native(w);P.update(seq[:j] for j in range(1,len(seq)+1))
 assert len(P)==112
 result={'fixed_keys':sorted(map(list,EXPECTED_FIVE)),'demand_count':len(need),'candidate_operation_nodes':N,'discount_variables':len(discount),'linear_constraints':A.shape[0],'nonzeros':A.nnz,'status':ans.status,'objective':int(ans.fun),'dual_bound':int(ans.mip_dual_bound),'mip_gap':ans.mip_gap,'independent_declared_witness_cost':len(P)}
 with open('MILP_REPORT_EC49FGE.json','w') as f:json.dump(result,f,indent=2);f.write('\n')
 print('EC49FGE_FIVE_KEY_EXACT_MILP_PASS',json.dumps(result,sort_keys=True))
 return result

if __name__=='__main__':run()
