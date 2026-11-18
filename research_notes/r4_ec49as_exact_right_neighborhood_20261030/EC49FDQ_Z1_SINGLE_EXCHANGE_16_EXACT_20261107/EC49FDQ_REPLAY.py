#!/usr/bin/env python3
"""EC49FDQ: exact signed-X6 five-key replacement integer optima.

Reproduction:
 OPENBLAS_NUM_THREADS=1 python EC49FDQ_REPLAY.py 1512 7,3,1 8,2,1
 Dependencies: NumPy, SciPy >=1.11.
Frozen science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Each output contains matching explicit witness, dual bound and independent
in-process rational-rank/native-prefix check; not a formal checker proof.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import numpy as np
from scipy.sparse import coo_matrix
from scipy.optimize import milp, Bounds, LinearConstraint
import sys, json, time
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
PRIM={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
LETTERS='acdefg'
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
       (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
       (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0);CLAUSES=(18,20,33,40)
SEED={2:['de','ed','ce','ec'],3:['feg','gef']}
FAMILIES={
 '1512':((3,1,1),(4,2,1),(4,3,1),(4,4,1),(5,5,1)),
 '1513':((3,1,1),(4,2,1),(5,2,1),(6,2,1),(7,3,1)),
 '2200':((3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1)),
 '2203':((3,1,1),(4,1,1),(5,2,1),(6,2,1),(7,3,1))}
QUOTAS={'1512':(4,2,2,2,4,2),'1513':(4,2,2,2,4,2),
        '2200':(2,4,2,2,4,2),'2203':(2,4,2,2,4,2)}
def steps(w):return tuple(v for c in w for v in PRIM[c])
def prefix(w):
 s=steps(w);return set(s[:n] for n in range(1,len(s)+1))
def key(w):return tuple(steps(w).count(i) for i in (1,2,3))
@lru_cache(None)
def language(h,k):
 x,y,z=k;r=x+y-h-1;cnt=[z-1,0,r,z,h+1-y-2*z,h+1-x]
 out=[]
 if min(cnt)<0:return ()
 def rec(q,state,w):
  if q==h:
   if SIG[state] in (1,2,4,8,16,32):out.append((SIG[state],w))
   return
  for j,x in enumerate(cnt):
   if x and TRANS[state][j]!=8:
    cnt[j]-=1;rec(q+1,TRANS[state][j],w+LETTERS[j]);cnt[j]+=1
 for n in range(r+1):
  cnt[1]=n;cnt[2]=r-n;rec(0,0,'')
 return tuple(out)

def obs(word):
 state=[]
 for name,prev in (('N',0),('N',1),('N',2),('A',0),('A',2),
                   ('B',0),('B',1),('AB',0),('BA',0)):
  cur=name
  for t in steps(word):
   if prev==1 and t==2:
    if cur=='N':cur='A'
    elif cur=='B':cur='BA'
   elif prev==2 and t==1:
    if cur=='N':cur='B'
    elif cur=='A':cur='AB'
   prev=t
  state.append(('N','A','B','AB','BA').index(cur))
 return state
def rank_Q(ws):
 out=[obs(w) for w in ws]
 mat=[[Fraction(int(o[i]==b)) for o in out for b in range(5)] for i in range(9)]
 rk=0
 for j in range(len(mat[0])):
  pivot=next((x for x in range(rk,9) if mat[x][j]),None)
  if pivot is None:continue
  mat[rk],mat[pivot]=mat[pivot],mat[rk]
  a=mat[rk][j];mat[rk]=[x/a for x in mat[rk]]
  for i in range(rk+1,9):
   if mat[i][j]:
    a=mat[i][j];mat[i]=[x-a*y for x,y in zip(mat[i],mat[rk])]
  rk+=1
  if rk==9:break
 return rk
def audit(chosen,keys,quota):
 assert set(chosen)==set(range(2,10))
 seen=set();full=[]
 for h,ws in chosen.items():
  assert len(ws)==(len(SEED[h]) if h<=3 else quota[h-4])
  assert len(ws)==len(set(ws))
  assert rank_Q(ws)==9,(h,ws)
  for w in ws:
   assert len(w)==h and key(w) in keys
   s=steps(w)
   assert tuple(s.count(i)-s.count(-i) for i in (1,2,3))==(2,0,0)
   seen.add(key(w));full.append(w)
 assert seen==set(keys),(seen,keys)
 return len(set().union(*(prefix(w) for w in full)))

def solve(case,knew,limit=60):
 t=time.time();old=FAMILIES[case];oldkey=old[-1]
 keys=sorted((set(old)-{oldkey})|{knew});assert len(keys)==5
 paid=set().union(*(prefix(w) for ws in SEED.values() for w in ws))
 assert len(paid)==42
 child=[{}];parent=[-1];prims=[()];cost=[0];candidates=[]
 for h in range(4,10):
  for k in keys:
   for sig,w in language(h,k):
    p=0
    for x in steps(w):
     q=child[p].get(x)
     if q is None:
      q=len(child);child[p][x]=q;child.append({});parent.append(p)
      prims.append(prims[p]+(x,));cost.append(int(prims[q] not in paid))
     p=q
    candidates.append((h,sig,k,w,p))
 n=len(child)-1;m=len(candidates);nvars=n+m
 rows=[];cols=[];vals=[]
 for q in range(1,n+1):
  row=q-1;rows.append(row);cols.append(q-1);vals.append(1.)
  if parent[q]>0:
   rows.append(row);cols.append(parent[q]-1);vals.append(-1.)
 for j,(h,sig,k,w,p) in enumerate(candidates):
  row=n+j;rows.extend((row,row));cols.extend((n+j,p-1));vals.extend((1.,-1.))
 base=n+m
 byh=defaultdict(list);byk=defaultdict(list)
 for j,(h,sig,k,w,p) in enumerate(candidates):
  byh[h].append(j);byk[k].append(j)
  for c,mask in enumerate(CLAUSES):
   if sig & mask:
    rows.append(base+4*(h-4)+c);cols.append(n+j);vals.append(1.)
 for kk,k in enumerate(k for k in keys if k!=(3,1,1)):
  for j in byk[k]:
   rows.append(base+24+kk);cols.append(n+j);vals.append(1.)
 for h in range(4,10):
  for j in byh[h]:
   rows.append(base+28+h-4);cols.append(n+j);vals.append(1.)
 A=coo_matrix((np.array(vals,float),
               (np.array(rows,np.int32),np.array(cols,np.int32))),
              shape=(base+34,nvars)).tocsr()
 lo=np.full(A.shape[0],-np.inf);hi=np.full(A.shape[0],np.inf)
 hi[:base]=0;lo[base:base+28]=1
 # Root child has no parent, so it is an admissible paid prefix variable.
 for q in child[0].values():hi[q-1]=1
 for h in range(4,10):
  lo[base+28+h-4]=hi[base+28+h-4]=QUOTAS[case][h-4]
 obj=np.concatenate((np.array(cost[1:],float),np.zeros(m)))
 con=LinearConstraint(A,lo,hi)
 bounds=Bounds(np.zeros(nvars),np.ones(nvars))
 result=milp(obj,integrality=np.ones(nvars),bounds=bounds,
             constraints=con,options={'time_limit':limit,'mip_rel_gap':0.0})
 out={'case':case,'old':list(oldkey),'new':list(knew),
      'keys':keys,'frozen_pin':PIN,'candidate_words':m,
      'trie_edges':n,'rows':A.shape[0],'nonzeros':A.nnz,
      'solver_status':int(result.status),
      'solver_message':result.message,
      'elapsed_seconds':round(time.time()-t,2),
      'mip_gap':getattr(result,'mip_gap',None),
      'dual_bound_total':42+(getattr(result,'mip_dual_bound',None) or 0),
      'primal_total':42+float(result.fun) if result.fun is not None else None}
 if result.x is not None:
  chosen={h:list(SEED[h]) for h in (2,3)}
  for h in range(4,10):
   chosen[h]=sorted(w for j,(hh,s,k,w,p) in enumerate(candidates)
                    if hh==h and result.x[n+j]>0.5)
  if result.status==0:
   out['witness']={str(h):chosen[h] for h in chosen}
   out['audit_edges']=audit(chosen,keys,QUOTAS[case])
   assert out['audit_edges']==round(out['primal_total'])
  else:
   out['partial_word_counts']={h:len(ws) for h,ws in chosen.items()}
 return out

if __name__=='__main__':
 fid=sys.argv[1] if len(sys.argv)>1 else '1512'
 ks=[tuple(map(int,arg.split(','))) for arg in sys.argv[2:]]
 for k in ks:
  print(json.dumps(solve(fid,k,60),ensure_ascii=False),flush=True)
