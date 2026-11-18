#!/usr/bin/env python3
"""EC49FBR: exact conditional nine-window BRC-X6 prefix-union MILPs."""
from collections import defaultdict
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

OPS='acdefg'
STEP={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIGN=(0,0,4,1,16,32,8,2,0)
CLAUSES={1:(0,),4:(1,),8:(2,),2:(3,),16:(0,1),32:(2,3)}
ROOT=['fe','ge','feg','gef']; L=(4,2,1)
LATE={
 (6,4,1):['fegffggc','fegffggd','gefffggc','gefffggd','fegffgggf','gefffgggf'],
 (7,3,2):['fegaefgc','fegaefgd','gefaefgc','gefaefgd','fegaefggf','gefaefggf']}
def native(w):return tuple(i for c in w for i in STEP[c])
def edges(words):return {p[:j] for w in words for p in [native(w)] for j in range(1,len(p)+1)}
def words(h,key):
 x,y,z=key; nc=x+y-h-1
 cnt={'a':z-1,'c':0,'d':0,'e':z,'f':h+1-y-2*z,'g':h+1-x}
 if min(cnt['a'],cnt['e'],cnt['f'],cnt['g'],nc)<0:return
 for n in range(nc+1):
  cnt['c']=n;cnt['d']=nc-n;seq=[]
  def go(st,k):
   if k==0:
    if SIGN[st] in CLAUSES:yield ''.join(seq),SIGN[st]
    return
   for j,c in enumerate(OPS):
    if cnt[c] and T[st][j]!=8:
     cnt[c]-=1;seq.append(c)
     yield from go(T[st][j],k-1)
     seq.pop();cnt[c]+=1
  yield from go(0,h)
def solve(M):
 paid=edges(ROOT+LATE[M]); assert len(paid) in (54,58)
 parents=[]; paths=[]; idx={():-1}; labels=defaultdict(set); ends={}; census=defaultdict(int)
 for h,key in {4:L,5:L,6:M,7:M}.items():
  for w,s in words(h,key):
   census[h]+=1;pre=();old=-1
   for d in native(w):
    pre+=d,
    if pre not in idx:
     idx[pre]=len(parents);parents.append(old);paths.append(pre)
    old=idx[pre]
   ends[(h,w)]=old
   for k in CLAUSES[s]:labels[(h,k)].add(old)
 assert len(labels)==16
 r=[];c=[];v=[];lb=[];ub=[]
 for i,p in enumerate(parents):
  if p>=0:
   j=len(lb);r.extend((j,j));c.extend((i,p));v.extend((1,-1));lb.append(-np.inf);ub.append(0)
 for lab in sorted(labels):
  j=len(lb)
  for i in labels[lab]:r.append(j);c.append(i);v.append(1)
  lb.append(1);ub.append(np.inf)
 n=len(parents);A=coo_matrix((v,(r,c)),shape=(len(lb),n)).tocsr()
 costs=np.array([int(p not in paid) for p in paths],dtype=float)
 result=milp(costs,integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),constraints=LinearConstraint(A,lb,ub),options={'mip_rel_gap':0,'time_limit':120})
 assert result.status==0 and result.mip_gap==0,(result.status,result.message)
 selected={i for i,x in enumerate(result.x) if x>.5};chosen={h:[] for h in range(4,8)}
 for (h,w),i in ends.items():
  if i in selected:chosen[h].append(w)
 added=[w for ls in chosen.values() for w in ls]
 assert len(edges(ROOT+LATE[M]+added))==len(paid)+round(result.fun)
 for h,ww in chosen.items():
  got=set()
  for w in ww:
   state=0
   for op in w:state=T[state][OPS.index(op)]
   got.update(CLAUSES[SIGN[state]])
  assert got=={0,1,2,3}
 return {'M':M,'base':len(paid),'extra':int(round(result.fun)),'total':len(paid)+round(result.fun),'dual_lower_bound':result.mip_dual_bound,'gap':result.mip_gap,'variables':n,'rows':len(lb),'candidates':dict(census),'selected':{str(h):sorted(ws) for h,ws in chosen.items()}}
if __name__=='__main__':
 import json
 print(json.dumps([solve(m) for m in LATE],ensure_ascii=False,indent=2))
