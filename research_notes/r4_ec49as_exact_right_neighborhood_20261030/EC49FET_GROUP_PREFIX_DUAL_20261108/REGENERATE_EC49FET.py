#!/usr/bin/env python3
"""Recompute group-aware prefix dual certificates for 25 finite inventories.
Requires SciPy (HiGHS) and NumPy; only VERIFY_EC49FET.py is authoritative for exact verification.
Usage: python REGENERATE_EC49FET.py CASES_EC49FET.json certificates/ [449 ...]
Output weights are rounded down to integer multiples of 1/1e6 and all constraints rechecked independently.
"""
import sys,json,time
from collections import defaultdict
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_array
from WORD_MODEL_EC49FET import words_with_label,native_prefixes

SCHEMA='EC49FET_STRONG_GROUP_PREFIX_DUAL_V1'

def solve(index,spec,Q=1000000):
 K=tuple(map(tuple,spec['keys']));high=set(spec['high'])
 labels=[];words=[];gids=[];prefixes={};pairs={};wi=[];row=[]
 for h in range(2,10):
  ss=(1,8,16) if h==3 else ((16,32) if h in high else (1,2,4,8))
  for s in ss:
   gid=len(labels);labels.append((h,s))
   for w in sorted({w for k in K for s2,w in words_with_label(h,k) if s2==s}):
    j=len(words);words.append(w);gids.append(gid)
    for p in native_prefixes(w):
     q=prefixes.setdefault(p,len(prefixes))
     k=(gid,q);rr=pairs.setdefault(k,len(pairs))
     wi.append(j);row.append(rr)
 assert len(labels)==23 and all(g in gids for g in range(23))
 n=len(words);npref=len(prefixes);nc=len(pairs)
 incid=len(wi);rr=np.r_[np.array(row,dtype=np.int32),np.arange(nc,dtype=np.int32)]
 cc=np.r_[np.array(wi,dtype=np.int32),np.array([n+p for g,p in pairs],dtype=np.int32)]
 val=np.r_[np.ones(incid),-np.ones(nc)]
 Aub=coo_array((val,(rr,cc)),shape=(nc,n+npref)).tocsr()
 E=coo_array((np.ones(n),(np.array(gids,dtype=np.int32),np.arange(n,dtype=np.int32))),shape=(23,n+npref)).tocsr()
 c=np.r_[np.zeros(n),np.ones(npref)]
 res=linprog(c,A_ub=Aub,b_ub=np.zeros(nc),A_eq=E,b_eq=np.ones(23),bounds=(0,None),method='highs')
 assert res.status==0,res.message
 weights=np.floor(np.maximum(0,-res.ineqlin.marginals)*Q+1e-7).astype(np.int64)
 cap={}
 for (g,p),v in zip(pairs,weights):cap[p]=cap.get(p,0)+int(v)
 assert max(cap.values())<=Q
 scores=[0]*n
 for j,r in zip(wi,row):scores[j]+=int(weights[r])
 gamma=[min(scores[j] for j,g in enumerate(gids) if g==i) for i in range(23)]
 assert sum(gamma)>97*Q
 cert={'schema':SCHEMA,'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
       'case':int(index),'high':list(spec['high']),'keys':list(spec['keys']),'Q':Q,'gamma':gamma,
       't_sparse':[[int(i),int(v)] for i,v in enumerate(weights) if v>0],
       'duality':'indexed by first-seen group-prefix pair, sorted complete words per group'}
 return cert

def main():
 specs=json.load(open(sys.argv[1]));out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
 ids=list(map(str,sys.argv[3:])) or list(specs)
 for i in ids:
  start=time.time();cert=solve(i,specs[i]);file=out/('strong_'+i+'.json')
  file.write_text(json.dumps(cert,separators=(',',':')))
  print(i,sum(cert['gamma'])/cert['Q'],round(time.time()-start,2),file,flush=True)
if __name__=='__main__':main()