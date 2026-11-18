#!/usr/bin/env python3
"""Native-X6 complete positive BRC-key pooled prefix optimization.
Frozen source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Candidate scientific result until exact integer certificate independently verified.
"""
import json,sys,time
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_array
from WORD_MODEL_EC49FET import words_with_label,native_prefixes
from EC49FEU_STANDALONE import keys as eligible_keys
Q=10**6
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def make_groups(mixed,highset):
    high=set(highset)|{3}
    assert mixed in high and 9 in high and len(high)==5
    K_pool={(3,1,1)}
    for h in sorted(high-{3}):
        need=frozenset((16,)) if h==mixed else frozenset((16,32))
        K_pool.update(eligible_keys(h,need))
    K_pool=tuple(sorted(K_pool))
    G=[]
    for h in range(2,10):
        sigs=(1,8,16) if h==mixed else ((16,32) if h in high else (1,2,4,8))
        for sig in sigs:
            ws=sorted({w for key in K_pool for label,w in words_with_label(h,key) if label==sig})
            assert ws,(h,sig,highset)
            G.append((h,sig,ws))
    assert len(G)==23
    return K_pool,G

def solve(mixed,highset,out_dir):
  t=time.monotonic();pool,G=make_groups(mixed,highset)
  words=[];gids=[];pref={};pairs={};wi=[];row=[]
  for gi,(_,_,W) in enumerate(G):
    for w in W:
      j=len(words);words.append(w);gids.append(gi)
      for p in native_prefixes(w):
        ip=pref.setdefault(p,len(pref));ix=pairs.setdefault((gi,ip),len(pairs));wi.append(j);row.append(ix)
  n=len(words);npref=len(pref);m=len(pairs)
  print('prepared',mixed,highset,'pool',len(pool),'words',n,'pairs',m,'prefixes',npref, 'secs',round(time.monotonic()-t,1),flush=True)
  A=coo_array((np.r_[np.ones(len(row)),-np.ones(m)],
         (np.r_[np.asarray(row,np.int32),np.arange(m,dtype=np.int32)],
          np.r_[np.asarray(wi,np.int32),np.array([n+p for g,p in pairs],np.int32)])),
         shape=(m,n+npref)).tocsr()
  E=coo_array((np.ones(n),(np.asarray(gids,np.int32),np.arange(n,dtype=np.int32))),shape=(23,n+npref)).tocsr()
  res=linprog(np.r_[np.zeros(n),np.ones(npref)],A_ub=A,b_ub=np.zeros(m),A_eq=E,b_eq=np.ones(23),bounds=(0,None),method='highs')
  assert res.status==0,res.message
  W=np.floor(np.maximum(0,-res.ineqlin.marginals)*Q+1e-7).astype(np.int64)
  loads=defaultdict(int)
  for (_,p),v in zip(pairs,W):loads[p]+=int(v)
  assert all(v<=Q for v in loads.values())
  sums=[0]*n
  for j,r in zip(wi,row):sums[j]+=int(W[r])
  gamma=[min(sums[j] for j,g in enumerate(gids) if g==i) for i in range(23)]
  LB=sum(gamma)
  cert={'schema':'EC49FEW_UNIVERSAL_POOLED_PREFIX_DUAL_V1','science_pin':PIN,
      'mixed_horizon':mixed,'late_high_horizons':list(highset),
      'Q':Q,'gamma':gamma,'t_sparse':[[int(i),int(v)] for i,v in enumerate(W) if v>0],
      'semantics':'Every five-key inventory of the branch is a subset of pooled eligible full BRC keys. Native signed microstep words, dual first-seen group/prefix pair.'}
  out_dir=Path(out_dir);out_dir.mkdir(exist_ok=True,parents=True)
  path=out_dir/f'UNIVERSAL_H{mixed}_{"".join(map(str,highset))}.json'
  path.write_text(json.dumps(cert,separators=(',',':'))+'\n')
  stats={'mixed':mixed,'late_high_horizons':list(highset),'eligible_pool_keys':len(pool),'pooled_words':n,'prefixes':npref,'group_prefix_pairs':m,
         'nonzero_integer_weights':len(cert['t_sparse']),'lp_finding_only':float(res.fun),'exact_dual_numerator':int(LB),'Q':Q,
         'integer_lower_bound':int((LB+Q-1)//Q),'elapsed_s':round(time.monotonic()-t,3), 'certificate_file':path.name}
  print(json.dumps(stats),flush=True)
  return stats
if __name__=='__main__':
 m=int(sys.argv[1]);high=tuple(map(int,sys.argv[2]));solve(m,high,sys.argv[3])