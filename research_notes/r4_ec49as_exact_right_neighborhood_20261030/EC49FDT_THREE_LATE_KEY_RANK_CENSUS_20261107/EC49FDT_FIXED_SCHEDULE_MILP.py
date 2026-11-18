#!/usr/bin/env python3
"""Reproduce eight fixed-late-key signed-native X6 prefix optima, frozen EC49FDT.
Requires scipy>=1.11, numpy; this is the executed local MILP's portable
algorithm, with no external source imports or absolute paths.
"""
import itertools, collections, json, sys
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
PRIM={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
      'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
LETTERS='acdefg'
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
       (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
       (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
CLAUSES=(18,20,33,40)
SCHEDULE={4:(3,2,1),5:(3,4,1),6:(3,4,1),
          7:(4,6,1),8:(4,6,1),9:(4,6,1)}
SEEDS=[{2:list(r),3:list(p)}
       for r in [('ce','ed','ge'),('de','ec','fe')]
       for p in [('feg','gef'),('feg','gfe'),
                 ('fge','gef'),('fge','gfe')]]
TARGETS=[114,118,114,118,124,124,128,128]

def steps(w):
 return tuple(x for c in w for x in PRIM[c])
def prefixes(w):
 s=steps(w);return {s[:i] for i in range(1,len(s)+1)}
def signature(w):
 q=0
 for c in w:q=TRANS[q][LETTERS.index(c)]
 return SIG[q]
def key(w):
 return tuple(steps(w).count(i) for i in (1,2,3))

def language(h,k):
 x,y,z=k
 r=x+y-h-1;nf=h+1-y-2*z;ng=h+1-x
 if min(r,nf,ng)<0:return {}
 result=collections.defaultdict(list)
 counts=[z-1,0,0,z,nf,ng]
 for nc in range(r+1):
  counts[1]=nc;counts[2]=r-nc
  def rec(w):
   if len(w)==h:
    s=signature(w)
    if s:result[s].append(w)
    return
   for j in range(6):
    if counts[j]:
     counts[j]-=1;rec(w+LETTERS[j]);counts[j]+=1
  rec('')
 return result

def direct_audit(paths):
 pre=set();keys=set();signatures=set()
 for h in range(2,10):
  seen=set();ms=0
  for w in paths[h]:
   assert len(w)==h
   s=steps(w)
   assert tuple(s.count(i)-s.count(-i) for i in (1,2,3))==(2,0,0)
   assert w not in seen
   seen.add(w)
   q=signature(w);assert q in (1,2,4,8,16,32)
   ms|=q;signatures.add(q);keys.add(key(w));pre.update(prefixes(w))
  assert all(ms&clause for clause in CLAUSES)
 assert len(keys)==5 and len(signatures)==6
 return len(pre)

def solve(early):
 paid=set().union(*(prefixes(w) for words in early.values() for w in words))
 children=[{}];parents=[-1];pref=[()]
 terminal=collections.defaultdict(list);endword={};word_count=0
 for h in range(4,10):
  for sig,ws in language(h,SCHEDULE[h]).items():
   for w in ws:
    assert key(w)==SCHEDULE[h]
    word_count+=1;cur=0
    for axis in steps(w):
     nxt=children[cur].get(axis)
     if nxt is None:
      nxt=len(children);children[cur][axis]=nxt
      children.append({});parents.append(cur);pref.append(pref[cur]+(axis,))
     cur=nxt
    terminal[h,sig].append(cur);endword[h,sig,cur]=w
 n=len(children)-1
 rows=[];cols=[];vals=[]
 for node in range(1,n+1):
  row=node-1;rows.append(row);cols.append(row);vals.append(1)
  if parents[node]>0:
   rows.append(row);cols.append(parents[node]-1);vals.append(-1)
 for h in range(4,10):
  for j,cl in enumerate(CLAUSES):
   row=n+4*(h-4)+j
   for s in (1,2,4,8,16,32):
    if s&cl:
     for node in terminal[h,s]:
      rows.append(row);cols.append(node-1);vals.append(1)
 A=coo_matrix((np.asarray(vals,float),(rows,cols)),shape=(n+24,n)).tocsr()
 lo=np.full(n+24,-np.inf);hi=np.full(n+24,np.inf)
 hi[:n]=0;lo[n:]=1
 for node in children[0].values():hi[node-1]=1
 cost=np.array([int(p not in paid) for p in pref[1:]],dtype=float)
 ans=milp(cost,integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),
          constraints=LinearConstraint(A,lo,hi),
          options={'mip_rel_gap':0.0,'time_limit':180})
 assert ans.status==0 and ans.x is not None,ans.message
 assert abs(ans.fun-ans.mip_dual_bound)<1e-6
 chosen=dict(early)
 for h in range(4,10):
  observed={}
  for s in (1,2,4,8,16,32):
   for node in terminal[h,s]:
    if ans.x[node-1]>.5:
     observed[s]=endword[h,s,node];break
  chosen[h]=list(dict.fromkeys(next(observed[s] for s in observed if s&cl) for cl in CLAUSES))
 witness_cost=direct_audit(chosen)
 assert witness_cost==round(len(paid)+ans.fun)
 return {'seed':early,'prepaid_prefix_edges':len(paid),'late_candidate_words':word_count,
         'late_trie_edges':n,'status':ans.status,'mip_gap':ans.mip_gap,
         'integer_optimum':witness_cost,'dual_bound':len(paid)+ans.mip_dual_bound,
         'witness':{str(h):chosen[h] for h in range(2,10)}}

def run():
 results=[]
 for i,seed in enumerate(SEEDS):
  r=solve(seed)
  assert r['integer_optimum']==TARGETS[i]
  print(i,r['prepaid_prefix_edges'],r['late_candidate_words'],
        r['late_trie_edges'],r['integer_optimum'],flush=True)
  results.append(r)
 print(json.dumps({'science_pin':PIN,'scope':'eight fixed early seeds and one full BRC key per late horizon',
                   'results':results},indent=2))

if __name__=='__main__':run()
