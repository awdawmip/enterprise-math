#!/usr/bin/env python3
"""EC49FBJ: native X6 signed-prefix minimum MILP. SciPy 1.17.0. Frozen science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab."""
from itertools import permutations
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
OP={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]]
SIG=[0,0,4,1,16,32,8,2,0]; IDX={c:i for i,c in enumerate('acdefg')}; CLAUSES=[18,20,33,40];BASE=['fe','ge','feg','gef']
def words(h,k):
 x,y,z=k;a=z-1;e=z;r=x+y-h-1;f=h+1-y-2*z;g=h+1-x
 if min(a,e,r,f,g)<0:return set()
 out=set()
 for i in range(r+1):
  ss='a'*a+'e'*e+'c'*i+'d'*(r-i)+'f'*f+'g'*g
  if len(ss)!=h:raise ValueError((h,k,ss))
  out.update(''.join(p) for p in permutations(ss))
 return out
def obs(w):
 st=0
 for c in w:st=T[st][IDX[c]]
 return SIG[st]
def valid(w):
 signed=[0]*6
 for c in w:
  for s in OP[c]:signed[abs(s)-1]+=1 if s>0 else -1
 return signed==[2,0,0,0,0,0] and obs(w)!=0
def key_word(w):return tuple(sum(s==i for c in w for s in OP[c]) for i in (1,2,3))
def run(L,M,sec):
 parent=[-1];children=[{}];mask=[0];fixed=set();terminal={}
 def insert(w,bit=-1):
  at=0
  for c in w:
   for step in OP[c]:
    v=children[at].get(step)
    if v is None:
     v=len(parent);children[at][step]=v;parent.append(at);children.append({});mask.append(0)
    at=v
    if bit<0:fixed.add(at)
  if bit>=0:mask[at]|=bit
  return at
 for w in BASE:insert(w)
 raw={};eligible={}
 for h in range(4,10):
  key=L if h<=6 else M;pool=words(h,key);good=[w for w in pool if valid(w)]
  raw[h]=len(pool);eligible[h]=len(good)
  for w in good:
   s=obs(w);bit=0
   if h<9:
    for i,c in enumerate(CLAUSES):
     if s&c:bit|=1<<(4*(h-4)+i)
   elif s==16:bit=1<<20
   elif s==32:bit=1<<21
   if bit:terminal[(h,w)]=(insert(w,bit),s,key)
 n=len(parent)-1
 rows=[];cols=[];vals=[];lo=[];hi=[]
 for v in range(1,n+1):
  p=parent[v]
  if p>0:
   z=len(lo);rows.extend((z,z));cols.extend((v-1,p-1));vals.extend((1,-1));lo.append(-np.inf);hi.append(0)
 clauses=[[] for _ in range(22)]
 for v in range(1,n+1):
  bit=mask[v]
  while bit:
   j=(bit&-bit).bit_length()-1;clauses[j].append(v-1);bit&=bit-1
 if not all(clauses):raise ValueError('signature clause missing')
 for cl in clauses:
  z=len(lo);rows.extend([z]*len(cl));cols.extend(cl);vals.extend([1]*len(cl));lo.append(1);hi.append(np.inf)
 A=coo_matrix((np.array(vals,dtype=float),(rows,cols)),shape=(len(lo),n)).tocsr()
 cost=np.ones(n);lower=np.zeros(n);upper=np.ones(n)
 for v in fixed:cost[v-1]=0;lower[v-1]=1
 sol=milp(cost,integrality=np.ones(n),bounds=Bounds(lower,upper),constraints=LinearConstraint(A,np.array(lo),np.array(hi)),options={'time_limit':sec,'mip_rel_gap':0})
 selected=[]
 if sol.x is not None:
  for (h,w),(v,s,k) in terminal.items():
   if sol.x[v-1]>.5:selected.append([h,w,s,list(k)])
 report={'L':L,'M':M,'status':int(sol.status),'message':sol.message,'trie_edges':n,'prepaid':len(fixed),'raw':raw,'eligible':eligible,'extra_objective':float(sol.fun) if sol.fun is not None else None,'dual_bound_extra':float(sol.mip_dual_bound) if getattr(sol,'mip_dual_bound',None) is not None else None,'gap':float(sol.mip_gap) if getattr(sol,'mip_gap',None) is not None else None,'selected_words':selected}
 print(json.dumps(report,indent=2));out=Path(__file__).resolve().parent/('REPORT_'+''.join(map(str,L))+'_'+''.join(map(str,M))+'.json');out.write_text(json.dumps(report,indent=2))
if __name__=='__main__':
 run(tuple(map(int,sys.argv[1].split(','))),tuple(map(int,sys.argv[2].split(','))),int(sys.argv[3]) if len(sys.argv)>3 else 45)
