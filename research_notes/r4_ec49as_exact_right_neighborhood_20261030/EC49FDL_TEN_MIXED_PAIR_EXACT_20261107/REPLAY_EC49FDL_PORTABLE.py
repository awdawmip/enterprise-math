#!/usr/bin/env python3
"""EC49FDL: complete mixed-key rank-nine signed-X6 prefix MILP, 10 finite key pairs.
Reproduction: OPENBLAS_NUM_THREADS=1 python REPLAY_EC49FDL_PORTABLE.py [8|11|all]
Requires Python3, NumPy, SciPy (milp/HiGHS). Integer witness independently rechecked.
"""
import sys, json
from collections import defaultdict
from fractions import Fraction
import numpy as np
from scipy.sparse import coo_array
from scipy.optimize import milp, Bounds, LinearConstraint
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
KEYS={8:((5,3,1),(3,7,1)),108:((5,3,1),(9,1,1)),17:((4,3,1),(4,6,1)),
      68:((5,2,1),(8,2,1)),123:((5,3,1),(9,7,1)),40:((5,3,1),(4,6,1)),
      96:((5,3,1),(8,2,1)),1:((3,3,1),(5,5,1)),45:((5,1,1),(7,3,1)),
      11:((4,2,1),(6,4,1))}
PRIMITIVE={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
           'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
CODE={-1:'a',1:'A',-2:'b',2:'B',-3:'c',3:'C'}
LETTERS='acdefg'
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
       (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
       (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
CLAUSES=(18,20,33,40)  # E|F, C|F, D|G, J|G
BASE={2:['fe','ge'],3:['feg','gef']}
STATES=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
def steps(word):return tuple(i for c in word for i in PRIMITIVE[c])
def code(word):return ''.join(CODE[i] for i in steps(word))
def prefix(word):
 p=steps(word);return {p[:i] for i in range(1,len(p)+1)}
def language(h,key):
 x,y,z=key; r=x+y-h-1
 counts={'a':z-1,'c':0,'d':r,'e':z,'f':h+1-y-2*z,'g':h+1-x}
 out=defaultdict(list)
 if min(counts.values())<0:return out
 def dfs(state,w):
  if len(w)==h:
   if SIG[state] in (1,2,4,8,16,32):out[SIG[state]].append(w)
   return
  for i,c in enumerate(LETTERS):
   if counts[c] and TRANS[state][i]!=8:
    counts[c]-=1;dfs(TRANS[state][i],w+c);counts[c]+=1
 for n in range(r+1):
  counts['c']=n;counts['d']=r-n;dfs(0,'')
 return out

def observer(word):
 ans=[]
 for name,prev in STATES:
  cur=name
  for t in steps(word):
   if prev==1 and t==2:
    if cur=='N':cur='A'
    elif cur=='B':cur='BA'
   elif prev==2 and t==1:
    if cur=='N':cur='B'
    elif cur=='A':cur='AB'
   prev=t
  ans.append(BUCKETS.index(cur))
 return ans
def rank_Q(words):
 outs=[observer(w) for w in words]
 a=[[Fraction(int(out[i]==b)) for out in outs for b in range(5)] for i in range(9)]
 rank=0
 for j in range(len(a[0])):
  pivot=next((r for r in range(rank,9) if a[r][j]),None)
  if pivot is None:continue
  a[rank],a[pivot]=a[pivot],a[rank];v=a[rank][j];a[rank]=[t/v for t in a[rank]]
  for i in range(rank+1,9):
   v=a[i][j]
   if v:a[i]=[t-v*s for t,s in zip(a[i],a[rank])]
  rank+=1
  if rank==9:break
 return rank

def validate(selection, keys):
 allwords=[]; observed_keys=set(); all_signatures=set(); per_h=[]
 for h in range(2,10):
  ws=BASE[h] if h<4 else selection[h]
  assert ws and rank_Q(ws)==9
  per_h.append(len(ws))
  for w in ws:
   assert len(w)==h
   ss=steps(w)
   assert tuple(ss.count(i)-ss.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
   k=tuple(ss.count(i) for i in range(1,7))
   assert h<4 or k[:3] in keys
   observed_keys.add(k);all_signatures.add(tuple(observer(w)))
   allwords.append(w)
 assert len(observed_keys)==5 and len(all_signatures)<=6
 return len(set().union(*(prefix(w) for w in allwords))),per_h

def solve(pair_id,time_limit=40):
 keys=KEYS[pair_id];fixed=set().union(*(prefix(w) for h in BASE for w in BASE[h]))
 assert len(fixed)==16
 nodes=[''];child=[{}];parent=[-1];cost=[0.];term=defaultdict(set);allwords=[]
 for h in range(4,10):
  for k in keys:
   for s,ws in language(h,k).items():
    for word in ws:
     allwords.append((h,s,k,word));p=0
     for t in code(word):
      q=child[p].get(t)
      if q is None:
       q=len(child);child[p][t]=q;child.append({});parent.append(p)
       nodes.append(nodes[p]+t);cost.append(float(tuple(-'abc'.index(c)-1 if c.islower() else 'ABC'.index(c)+1 for c in nodes[q]) not in fixed))
      p=q
     term[h,s].add(p)
 n=len(nodes);rows=[];cols=[];vals=[]
 for q in range(1,n):
  rows.append(q-1);cols.append(q);vals.append(1.)
  if parent[q]>0:rows.append(q-1);cols.append(parent[q]);vals.append(-1.)
 for h in range(4,10):
  for j,mask in enumerate(CLAUSES):
   for s in (1,2,4,8,16,32):
    if s&mask:
     for q in term[h,s]:rows.append(n-1+4*(h-4)+j);cols.append(q);vals.append(1.)
 A=coo_array((np.array(vals,float),(np.array(rows,np.int32),np.array(cols,np.int32))),shape=(n-1+24,n)).tocsr()
 low=np.full(n-1+24,-np.inf);upper=np.full(n-1+24,np.inf)
 upper[:n-1]=0.;low[n-1:]=1.
 for q in child[0].values():upper[q-1]=np.inf
 result=milp(np.array(cost),integrality=np.ones(n,np.int8),bounds=Bounds(np.zeros(n),np.ones(n)),
             constraints=LinearConstraint(A,low,upper),options={'time_limit':time_limit,'mip_rel_gap':0.0})
 assert result.status==0 and result.mip_gap==0,(result.status,result.message)
 selected={nodes[i] for i in np.flatnonzero(result.x>0.5)}
 chosen=defaultdict(list)
 for h,s,k,w in allwords:
  if code(w) in selected:chosen[h].append(w)
 edge_count,counts=validate(chosen,keys)
 assert edge_count==round(16+result.fun)
 return {'pair_index':pair_id,'keys':keys,'exact_optimum':edge_count,'candidate_words':len(allwords),
         'trie_nodes':n,'nonzeros':int(A.nnz),'mip_gap':result.mip_gap,
         'dual_bound_plus_seed':float(result.mip_dual_bound+16),'chosen':dict(chosen),'word_counts_h2_h9':counts,
         'scientific_input':PIN}
if __name__=='__main__':
 ids=list(KEYS) if len(sys.argv)==1 or sys.argv[1]=='all' else [int(sys.argv[1])]
 for i in ids:print(json.dumps(solve(i),ensure_ascii=False),flush=True)
