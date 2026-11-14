#!/usr/bin/env python3
"""Exact EC49FGM H8 block audit. Run in the research-line checkout; stdlib only."""
import importlib.util, itertools, json
from pathlib import Path
P=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('brc_frozen',P/'EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
OPS,T,SIG,STEPS,REQ=(getattr(m,k) for k in ('OPS','T','SIG','STEPS','REQ'))
K=[tuple(map(int,line.split()[:3])) for line in (P/'EC49FGK_SEVEN_KEY_COVER_TAXONOMY_20261110/EC49FGK_key_masks.txt').read_text().splitlines() if line.strip()]
J=json.loads((P/'EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json').read_text())
assert len(K)==94 and J['frozen_scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
def candidates(h,key):
 x,y,z=key; a=z-1;b=x+y-h-1;f=h+1-y-2*z;g=h+1-x
 if min(a,b,f,g)<0:return
 for c in range(b+1):
  n=[a,c,b-c,z,f,g]
  def rec(w,q):
   if len(w)==h:
    if SIG[q] in REQ[h]:yield SIG[q],w
    return
   for j,op in enumerate(OPS):
    if n[j] and T[q][j]!=8:
     n[j]-=1; yield from rec(w+op,T[q][j]); n[j]+=1
  yield from rec('',0)
def prefixes(w):
 seq=[];out=set()
 for op in w:
  for v in STEPS[op]:seq.append(v);out.add(tuple(seq))
 return out
by_sig={s:[] for s in (1,2,4,8)}
for key in K:
 for sig,w in candidates(8,key):by_sig[sig].append(w)
assert sum(map(len,by_sig.values()))==125680
out={'schema':'EC49FGM_EXACT_H8_FIXED20_V1','pin':J['frozen_scientific_pin'],'candidate_h8_words':125680,'profiles':[]}
for profile in J['profiles']:
 fixed=[d['word'] for d in profile['demands'] if d['window']!=8]
 base=set().union(*(prefixes(w) for w in fixed));assert len(fixed)==20 and len(base)==86
 original={d['signature']:d['word'] for d in profile['demands'] if d['window']==8}
 assert len(set().union(base,*(prefixes(w) for w in original.values())))==94
 ids={};keep={}
 for sig,ws in by_sig.items():
  masks=[]
  for w in ws:
   delta=prefixes(w)-base
   if len(delta)>7:continue
   z=0
   for node in delta:
    if node not in ids:ids[node]=len(ids)
    z|=1<<ids[node]
   masks.append(z)
  keep[sig]=masks
 p12=[a|b for a,b in itertools.product(keep[1],keep[2]) if (a|b).bit_count()<=7]
 p48=[a|b for a,b in itertools.product(keep[4],keep[8]) if (a|b).bit_count()<=7]
 impossible=all((a|b).bit_count()>7 for a,b in itertools.product(p12,p48))
 assert impossible
 out['profiles'].append({'profile':profile['profile_id'],'fixed_native_edges':86,'retained':{str(s):len(v) for s,v in keep.items()},'pair_cross_tests':len(p12)*len(p48),'no_h8_plus_7_edges_even_unlimited_keys':impossible,'exact_optimum_native_edges':94})
print(json.dumps(out,indent=2,sort_keys=True))
