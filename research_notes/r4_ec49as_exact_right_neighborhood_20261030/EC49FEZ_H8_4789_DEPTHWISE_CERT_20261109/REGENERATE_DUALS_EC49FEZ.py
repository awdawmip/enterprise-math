#!/usr/bin/env python3
"""Explore full pooled key LP. Floating-point solution is a search heuristic, NOT a proof.
Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json,time,sys
import numpy as np
from scipy.sparse import coo_array
from scipy.optimize import linprog
from collections import defaultdict
from VERIFY_EC49FEZ import words,eligible,signed_steps

def build(mixed,hs):
 high=set(hs)|{3}
 pool={(3,1,1)}
 for h in sorted(high-{3}):pool.update(eligible(h,(16,) if h==mixed else (16,32)))
 G=[]
 for h in range(2,10):
  labels=(1,8,16) if h==mixed else ((16,32) if h in high else (1,2,4,8))
  for sig in labels:
   W={w for k in pool for label,w in words(h,k) if label==sig}
   assert W
   G.append((h,sig,W))
 return pool,G

def native_prefixes(w):
 p=()
 for s in signed_steps(w):
  p=p+(s,)
  yield p

def explore(mixed,hs,time_limit=60):
 start=time.monotonic();pool,G=build(mixed,tuple(map(int,hs)))
 all_words=[];gids=[];prefix_id={};pair_id={};links=[]; word_ids=[]
 for gi,(_,_,wordset) in enumerate(G):
  for w in sorted(wordset):
   j=len(all_words);all_words.append(w);gids.append(gi)
   for p in native_prefixes(w):
    pid=prefix_id.setdefault(p,len(prefix_id));pair=pair_id.setdefault((gi,pid),len(pair_id))
    links.append(pair);word_ids.append(j)
 n=len(all_words);npref=len(prefix_id);m=len(pair_id)
 print('Prepared',mixed,hs,'pool',len(pool),'nwords',n,'npref',npref,'gp-pairs',m,'word-prefix-links',len(links),'build-secs',round(time.monotonic()-start,2),flush=True)
 A=coo_array((np.r_[np.ones(len(links)), -np.ones(m)],
   (np.r_[np.asarray(links,dtype=np.int32),np.arange(m,dtype=np.int32)],
   np.r_[np.asarray(word_ids,dtype=np.int32), np.array([n+pid for (_,pid) in pair_id],dtype=np.int32)])),
   shape=(m,n+npref)).tocsr()
 E=coo_array((np.ones(n),(np.asarray(gids,dtype=np.int32),np.arange(n,dtype=np.int32))),shape=(23,n+npref)).tocsr()
 print('Solving',flush=True)
 res=linprog(np.r_[np.zeros(n),np.ones(npref)],A_ub=A,b_ub=np.zeros(m),A_eq=E,b_eq=np.ones(23),bounds=(0,None),method='highs',options={'time_limit':time_limit})
 print('Solver',res.status,res.message,'objective',getattr(res,'fun',None),'seconds',round(time.monotonic()-start,2),flush=True)
 if res.status==0:
  Q=10**6
  dual=np.floor(np.maximum(0,-res.ineqlin.marginals)*Q+1e-8).astype(np.int64)
  loads=defaultdict(int)
  for (_,p),weight in zip(pair_id,dual):loads[p]+=int(weight)
  assert all(v<=Q for v in loads.values())
  wordweight=np.zeros(n,dtype=np.int64)
  np.add.at(wordweight,word_ids,dual[links])
  gamma=[int(np.min(wordweight[np.array(gids)==g])) for g in range(23)]
  LB=sum(gamma)
  result={'LP_objective':res.fun,'certificate_exact_numerator':LB,'Q':Q,'cert_integer_lower_bound':(LB+Q-1)//Q,'words':n,'pairs':m,'positive_weights':int(np.count_nonzero(dual)),'time_s':time.monotonic()-start}
  print('RESULT',json.dumps(result),flush=True)
  if LB>93*Q:
   cert={'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','mixed':mixed,'highset':hs,'Q':Q,'gamma':gamma,'weights':[[int(i),int(v)] for i,v in enumerate(dual) if v>0]}
   p=f'DUAL_H{mixed}_{hs}.json'
   with open(p,'w') as f:json.dump(cert,f)
   print('CERT_CREATED',p,flush=True)
  return result
if __name__=='__main__':explore(int(sys.argv[1]),sys.argv[2],float(sys.argv[3]) if len(sys.argv)>3 else 60)
