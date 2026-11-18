#!/usr/bin/env python3
"""Independent mixed-integer prefix-closure oracle for EC49FFS H4/H6 one key."""
from collections import Counter
import json
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix
from VERIFY_EC49FFS_COMPACT import words,X
K=(5,3,1)
DEMANDS=tuple((h,s) for h in (4,6) for s in (1,2,4,8))
P={}; W=[]; WP=[]
for h in (4,6):
 for w,s in words(h,K):
  axis=tuple(z for c in w for z in X[c]); ids=[]
  for i in range(1,len(axis)+1):
   prefix=axis[:i]
   if prefix not in P:P[prefix]=len(P)
   ids.append(P[prefix])
  W.append((h,s,w));WP.append(ids)
NW=len(W); NP=len(P);N=NW+NP
ri=[];ci=[];vals=[];lo=[];hi=[];row=0
for demand in DEMANDS:
 for j,(h,s,w) in enumerate(W):
  if (h,s)==demand:ri.append(row);ci.append(j);vals.append(1)
 lo.append(1);hi.append(np.inf);row+=1
for j,ids in enumerate(WP):
 for p in ids:
  ri.extend((row,row));ci.extend((j,NW+p));vals.extend((1,-1))
  lo.append(-np.inf);hi.append(0);row+=1
A=coo_matrix((np.array(vals,dtype=float),(ri,ci)),shape=(row,N)).tocsr()
c=np.zeros(N);c[NW:]=1
r=milp(c,integrality=np.ones(N),bounds=Bounds(np.zeros(N),np.ones(N)),constraints=LinearConstraint(A,lo,hi),options={'time_limit':90,'mip_rel_gap':0})
assert r.success and round(r.fun)==88 and r.mip_gap==0,(r.message,r.fun,r.mip_gap)
chosen=[W[j] for j in range(NW) if r.x[j]>.5];union=set()
for h,s,w in chosen:
 axis=tuple(z for c in w for z in X[c]);union.update(axis[:i] for i in range(1,len(axis)+1))
assert len(union)==88 and { (h,s) for h,s,w in chosen}==set(DEMANDS)
print(json.dumps({'key':K,'windows':[4,6],'word_count':NW,'prefix_count':NP,'variables':N,
 'constraints':row,'optimum':int(round(r.fun)),'mip_gap':r.mip_gap,
 'witness':[{'h':h,'signature':s,'word':w} for h,s,w in chosen],
 'direct_union_check':len(union),'solver_message':r.message},indent=2))
