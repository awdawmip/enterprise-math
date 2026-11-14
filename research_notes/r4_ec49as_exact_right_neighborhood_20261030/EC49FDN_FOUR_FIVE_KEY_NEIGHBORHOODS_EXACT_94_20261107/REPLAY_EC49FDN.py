#!/usr/bin/env python3
"""EC49FDN: reproduce four exact mixed-horizon five-key optima from 94-edge witnesses.
Python 3 + numpy + scipy>=1.11; run OPENBLAS_NUM_THREADS=1 python ec49fdn_replay.py
Requires sibling EC49FDL_TEN_MIXED_PAIR_EXACT_20261107/REPLAY_EC49FDL_PORTABLE.py
The six-state masks and signed X6 observations are inherited byte-for-byte.
"""
import sys, json, importlib.util
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import numpy as np
from scipy.sparse import coo_matrix
from scipy.optimize import milp, Bounds, LinearConstraint, linprog

parent=Path(__file__).resolve().parent
external=parent.parent/'EC49FDL_TEN_MIXED_PAIR_EXACT_20261107'/'REPLAY_EC49FDL_PORTABLE.py'
if not external.exists():
 external=parent/'REPLAY_EC49FDL_PORTABLE.py'
spec=importlib.util.spec_from_file_location('frozen_fdl',external)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
assert f.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
BASE={2:['de','ed','ce','ec'],3:['feg','gef']}
CASE={
 '1512':{4:['defg','edfg','fegc','gefc'],5:['fegfg','geffg'],6:['fegfgg','geffgg'],7:['fegfggg','geffggg']},
 '1513':{4:['defg','edfg','fegc','gefc'],5:['fegfg','geffg'],6:['fegfgf','geffgf'],7:['fegfgff','geffgff']},
 '2200':{4:['fegg','gefg'],5:['feggd','gefgd','feggc','gefgc'],6:['fegggf','gefggf'],7:['fegggfg','gefggfg']},
 '2203':{4:['fegf','geff'],5:['fegfd','geffd','fegfc','geffc'],6:['fegfgf','geffgf'],7:['fegfgff','geffgff']},
}

def verify_six_signature_rank_clause():
 rep={}
 for row in CASE.values():
  for words in row.values():
   for w in words:
    state=0
    for ch in w:state=f.TRANS[state][f.LETTERS.index(ch)]
    rep[f.SIG[state]]=w
 assert len(rep)==6 and set(rep)=={1,2,4,8,16,32}
 rank9_masks=[]
 for mask in range(64):
  words=[rep[1<<j] for j in range(6) if mask & (1<<j)]
  rank=f.rank_Q(words) if words else 0
  agrees=(rank==9)==all(mask & clause for clause in f.CLAUSES)
  assert agrees,(mask,rank)
  if rank==9:rank9_masks.append(mask)
 assert len(rank9_masks)==25
 return rank9_masks

def native_key(w):
 steps=f.steps(w)
 return tuple(steps.count(k) for k in range(1,7))

def audit(paths):
 allw=[w for h in range(2,10) for w in paths[h]]
 count=len(set().union(*(f.prefix(w) for w in allw)))
 assert {tuple(native_key(w)) for w in allw}.__len__()==5
 assert len({tuple(f.observer(w)) for w in allw})<=6
 for h in range(2,10):
  assert f.rank_Q(paths[h])==9,h
  for w in paths[h]:
   s=f.steps(w)
   assert len(w)==h and tuple(s.count(k)-s.count(-k) for k in range(1,7))==(2,0,0,0,0,0)
 return count

def reproduce(case):
 src=CASE[case]
 roots=src[7]
 paths={**BASE,**src,8:[w+t for w in roots for t in 'cd'],9:[w+'fg' for w in roots]}
 assert audit(paths)==94
 keys=sorted({native_key(w)[:3] for row in paths.values() for w in row})
 assert len(keys)==5
 paid=set().union(*(f.prefix(w) for ws in BASE.values() for w in ws))
 assert len(paid)==42
 children=[{}];parent_node=[-1];word=[''];cost=[0]
 terminal=defaultdict(set);labels={}
 for h in range(4,10):
  for k in keys:
   for sig,ws in f.language(h,k).items():
    for w in ws:
     p=0
     for code in f.code(w):
      next_p=children[p].get(code)
      if next_p is None:
       next_p=len(children);children[p][code]=next_p;children.append({})
       parent_node.append(p);word.append(word[p]+code)
       encoded=tuple((-('abc'.index(c)+1) if c.islower() else 'ABC'.index(c)+1) for c in word[next_p])
       cost.append(int(encoded not in paid))
      p=next_p
     terminal[h,sig].add(p);labels[h,sig,p]=w
 n=len(children)-1
 rows=[];cols=[];vals=[]
 for q in range(1,n+1):
  row=q-1;rows.append(row);cols.append(q-1);vals.append(1)
  if parent_node[q]>0:
   rows.append(row);cols.append(parent_node[q]-1);vals.append(-1)
 for h in range(4,10):
  for j,mask in enumerate(f.CLAUSES):
   row=n+4*(h-4)+j
   for sig in (1,2,4,8,16,32):
    if sig&mask:
     for q in terminal[h,sig]:
      rows.append(row);cols.append(q-1);vals.append(1)
 A=coo_matrix((np.array(vals,float),(rows,cols)),shape=(n+24,n)).tocsr()
 lo=np.full(n+24,-np.inf);hi=np.full(n+24,np.inf)
 hi[:n]=0;lo[n:]=1
 for p in children[0].values():hi[p-1]=1
 c=np.array(cost[1:],float)
 con=LinearConstraint(A,lo,hi);bounds=Bounds(np.zeros(n),np.ones(n))
 lp=milp(c,integrality=np.zeros(n),bounds=bounds,constraints=con)
 ip=milp(c,integrality=np.ones(n),bounds=bounds,constraints=con,options={'time_limit':60,'mip_rel_gap':0})
 assert lp.status==ip.status==0 and abs(ip.mip_gap)<1e-10
 assert round(42+ip.fun)==94 and abs(42+ip.mip_dual_bound-94)<1e-7
 # Build an explicit legal witness from chosen terminals (at most 4 per horizon).
 chosen={2:BASE[2],3:BASE[3]}
 for h in range(4,10):
  selected={}
  for sig in (1,2,4,8,16,32):
   for p in terminal[h,sig]:
    if ip.x[p-1]>.5:
     selected[sig]=labels[h,sig,p];break
  chosen[h]=list(dict.fromkeys(next(selected[s] for s in selected if s&mask)
                               for mask in f.CLAUSES))
 assert audit(chosen)==94
 fractionals=sum(1 for x in lp.x if 1e-7<x<1-1e-7)
 return {'case':case,'keys':[list(k) for k in keys],'candidate_words':len(labels),
  'trie_edges':n,'milp_rows':A.shape[0],'milp_nonzeros':A.nnz,
  'prepaid_edges':42,'lp_bound':42+lp.fun,'lp_fractional_nodes':fractionals,
  'integer_optimum':42+ip.fun,'integer_dual_bound':42+ip.mip_dual_bound,'mip_gap':ip.mip_gap,
  'witness':{str(k):v for k,v in chosen.items()},'witness_edges':audit(chosen)}

if __name__=='__main__':
 result={'frozen_science_pin':f.PIN,'scope':'H2/H3 original fixed; H4-H9 any of exact five full cache keys within each EC49FAJ 94-edge case, including intra-horizon mixing; original six observation signatures',
  'rank9_signature_masks':verify_six_signature_rank_clause(),
  'cases':[reproduce(k) for k in CASE]}
 print(json.dumps(result,indent=2,ensure_ascii=False))
