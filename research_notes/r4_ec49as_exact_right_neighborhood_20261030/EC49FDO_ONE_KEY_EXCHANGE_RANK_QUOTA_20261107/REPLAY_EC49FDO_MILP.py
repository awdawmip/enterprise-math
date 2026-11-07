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

def reproduce(case,old_key,new_key):
 src=CASE[case]
 roots=src[7]
 paths={**BASE,**src,8:[w+t for w in roots for t in 'cd'],9:[w+'fg' for w in roots]}
 assert audit(paths)==94
 keys=sorted({native_key(w)[:3] for row in paths.values() for w in row})
 assert old_key in keys and (new_key not in keys or new_key == old_key)
 keys=sorted((set(keys)-{old_key})|{new_key})
 assert len(keys)==5 and (3,1,1) in keys
 assert len(keys)==5
 paid=set().union(*(f.prefix(w) for ws in BASE.values() for w in ws))
 assert len(paid)==42
 children=[{}];parent_node=[-1];word=[''];cost=[0]
 terminal=defaultdict(set);labels={};terms_by_key=defaultdict(set);terms_by_h=defaultdict(set)
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
     terminal[h,sig].add(p);labels[h,sig,p]=w;terms_by_key[k].add(p);terms_by_h[h].add(p)
 n=len(children)-1
 # Two variable families: x_v is paid signed-prefix inclusion; y_j explicitly
 # chooses an observation word. An internal prefix of a longer word need not
 # consume a shorter horizon's word slot.
 candidates=list(labels.items());m=len(candidates)
 rows=[];cols=[];vals=[]
 for q in range(1,n+1):
  row=q-1;rows.append(row);cols.append(q-1);vals.append(1)
  if parent_node[q]>0:
   rows.append(row);cols.append(parent_node[q]-1);vals.append(-1)
 for j,((h,s,p),w) in enumerate(candidates):
  row=n+j
  rows.extend((row,row));cols.extend((n+j,p-1));vals.extend((1,-1))
 for h in range(4,10):
  for j,mask in enumerate(f.CLAUSES):
   row=n+m+4*(h-4)+j
   for idx,((hh,s,p),w) in enumerate(candidates):
    if hh==h and s&mask:
     rows.append(row);cols.append(n+idx);vals.append(1)
 otherkeys=[k for k in keys if k!=(3,1,1)]
 for j,k in enumerate(otherkeys):
  row=n+m+24+j
  for idx,((h,s,p),w) in enumerate(candidates):
   if native_key(w)[:3]==k:
    rows.append(row);cols.append(n+idx);vals.append(1)
 quotas={4:4,5:2,6:2,7:2,8:4,9:2}
 for h in range(4,10):
  row=n+m+28+(h-4)
  for idx,((hh,s,p),w) in enumerate(candidates):
   if hh==h:rows.append(row);cols.append(n+idx);vals.append(1)
 A=coo_matrix((np.array(vals,float),(rows,cols)),shape=(n+m+34,n+m)).tocsr()
 lo=np.full(n+m+34,-np.inf);hi=np.full(n+m+34,np.inf)
 hi[:n+m]=0;lo[n+m:n+m+28]=1
 for h in range(4,10):
  row=n+m+28+(h-4);lo[row]=hi[row]=quotas[h]
 for p in children[0].values():hi[p-1]=1
 c=np.concatenate((np.array(cost[1:],float),np.zeros(m)))
 con=LinearConstraint(A,lo,hi);bounds=Bounds(np.zeros(n+m),np.ones(n+m))
 lp=milp(c,integrality=np.zeros(n+m),bounds=bounds,constraints=con)
 ip=milp(c,integrality=np.ones(n+m),bounds=bounds,constraints=con,options={'time_limit':60,'mip_rel_gap':0})
 assert lp.status==ip.status==0 and abs(ip.mip_gap)<1e-10
 assert abs(ip.fun-ip.mip_dual_bound)<1e-6
 # The terminal quota forces exactly the established number of horizon words
 # in these three probes; include every selected terminal so key usage is retained.
 chosen={2:BASE[2],3:BASE[3]}
 for h in range(4,10):
  chosen[h]=sorted({w for idx,((hh,s,p),w) in enumerate(candidates) if hh==h and ip.x[n+idx]>.5})
  assert len(chosen[h])==quotas[h],(case,h,len(chosen[h]))
 assert audit(chosen)==round(42+ip.fun)
 fractionals=sum(1 for x in lp.x if 1e-7<x<1-1e-7)
 return {'case':case,'old_key':old_key,'new_key':new_key,'keys':[list(k) for k in keys],'candidate_words':len(labels),
  'trie_edges':n,'milp_rows':A.shape[0],'milp_nonzeros':A.nnz,
  'prepaid_edges':42,'lp_bound':42+lp.fun,'lp_fractional_nodes':fractionals,
  'integer_optimum':42+ip.fun,'integer_dual_bound':42+ip.mip_dual_bound,'mip_gap':ip.mip_gap,
  'witness':{str(k):v for k,v in chosen.items()},'witness_edges':audit(chosen)}

if __name__=='__main__':
 probes=[('1512',(5,5,1),(5,5,1)),
         ('1512',(5,5,1),(6,4,1)),
         ('1512',(5,5,1),(4,6,1))]
 result={'schema':'EC49FDO_THREE_FIVE_KEY_EXACT_MILPS_V1',
         'frozen_science_pin':f.PIN,
         'quota_H4_to_H9':[4,2,2,2,4,2],
         'rank9_masks':verify_six_signature_rank_clause(),
         'probes':[reproduce(*spec) for spec in probes]}
 print(json.dumps(result,indent=2,ensure_ascii=False))
