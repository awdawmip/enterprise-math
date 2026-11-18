#!/usr/bin/env python3
"""Exact finite EC49FGN: two fixed-16 prefix-coherent H7/H8 optimizations.
Run from a checkout of PR #1730. Pure stdlib; all BRC operations are frozen.
"""
import importlib.util, itertools, json
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
source=ROOT/'EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py'
spec=importlib.util.spec_from_file_location('ec49fgn_brc_frozen',source)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
OPS,T,SIG,STEPS,REQ=(getattr(m,k) for k in ('OPS','T','SIG','STEPS','REQ'))
J=json.loads((ROOT/'EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json').read_text())
assert J['frozen_scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def observe(w):
 q=0
 for op in w:
  q=T[q][OPS.index(op)]
  if q==8:return None
 return SIG[q]

def pref(w):
 q=();a=set()
 for op in w:
  for v in STEPS[op]:q=q+(v,);a.add(q)
 return a

def key_endpoint(w):
 k=[0,0,0];pos=[0]*6
 for op in w:
  for step in STEPS[op]:
   ax=abs(step)-1
   pos[ax]+=1 if step>0 else -1
   if step>0:k[ax]+=1
 return tuple(k),tuple(pos)

def all_h8_coherent():
 pool=defaultdict(list); counts=Counter();keys=set()
 # Every 8-operation native path has 0<=x<=16, 0<=y<=8, 1<=z<=8.
 # Exact X6 endpoint forces a=z-1,c+d=x+y-9,f=9-y-2z,g=9-x.
 for x in range(17):
  for y in range(9):
   for z in range(1,9):
    a=z-1;b=x+y-9;f=9-y-2*z;g=9-x
    if min(a,b,f,g)<0:continue
    for c in range(b+1):
     n=[a,c,b-c,z,f,g]
     def visit(w,q):
      if len(w)==8:
       s=SIG[q]
       if s not in REQ[8]:return
       counts[s]+=1;keys.add((x,y,z))
       # Original H7 must have the SAME signature and the exact X6 endpoint.
       # Last opcode c,d,f,g is zero-displacement; a/e are not.
       if w[-1] not in 'cdfg' or observe(w[:7])!=s:return
       k,e=key_endpoint(w);k7,e7=key_endpoint(w[:7])
       assert k==(x,y,z) and e==e7==(2,0,0,0,0,0)
       pool[s].append(w)
       return
      for j,op in enumerate(OPS):
       q2=T[q][j]
       if n[j] and q2!=8:
        n[j]-=1;visit(w+op,q2);n[j]+=1
     visit('',0)
 assert sum(counts.values())==125680 and len(keys)==50
 assert [len(pool[s]) for s in (1,2,4,8)]==[17172,20418,17172,20418]
 return counts,pool

def bitindices(v):
 while v:
  b=v&-v;yield b.bit_length()-1;v-=b

def check(profile,pool):
 fixed=[d['word'] for d in profile['demands'] if d['window'] not in (7,8)]
 assert len(fixed)==16
 F=set().union(*(pref(w) for w in fixed))
 assert len(F)==78
 allprefix=set();allkeys=set()
 labels=set();h7={};h8={}
 for d in profile['demands']:
  h,s,w=d['window'],d['signature'],d['word']
  assert len(w)==h and s in REQ[h] and observe(w)==s
  assert (h,s) not in labels
  labels.add((h,s));k,e=key_endpoint(w)
  assert e==(2,0,0,0,0,0)
  allkeys.add(k);allprefix.update(pref(w))
  if h==7:h7[s]=w
  if h==8:h8[s]=w
 assert labels=={(h,s) for h in REQ for s in REQ[h]}
 assert len(allkeys)==7 and len(allprefix)==94
 assert all(h8[s].startswith(h7[s]) for s in (1,2,4,8))
 assert len(allprefix-F)==16
 ids={};cand={}
 for s in (1,2,4,8):
  masks=set()
  for w in pool[s]:
   delta=pref(w)-F
   if len(delta)>15:continue
   mask=0
   for node in delta:
    if node not in ids:ids[node]=len(ids)
    mask|=1<<ids[node]
   masks.add(mask)
  cand[s]=masks
 left={a|b for a in cand[1] for b in cand[2] if (a|b).bit_count()<=15}
 right={a|b for a in cand[4] for b in cand[8] if (a|b).bit_count()<=15}
 ml=min(x.bit_count() for x in left)
 mr=min(x.bit_count() for x in right)
 assert ml==mr==8
 # A pair of disjoint group masks has >=8+8=16 new edges.
 # It is therefore exhaustive to inspect only pairs with shared bits.
 inv=defaultdict(set)
 for v in right:
  for b in bitindices(v):inv[b].add(v)
 tested=0
 for u in left:
  overlap=set()
  for b in bitindices(u):overlap.update(inv.get(b,()))
  for v in overlap:
   tested+=1
   assert (u|v).bit_count()>15
 return dict(profile=profile['profile_id'],fixed_edges=78,
   coherent_h8_counts={str(s):len(pool[s]) for s in (1,2,4,8)},
   retained_masks={str(s):len(cand[s]) for s in (1,2,4,8)},
   native_prefix_ids=len(ids),pair_12_masks=len(left),pair_48_masks=len(right),
   minimum_pair_edges=[ml,mr],overlapping_cross_checks=tested,
   exact_optimum=94,exact_no_93=True)

def main():
 counts,pool=all_h8_coherent()
 reports=[check(p,pool) for p in J['profiles']]
 assert [(r['native_prefix_ids'],r['overlapping_cross_checks']) for r in reports]==[(8180,47552),(8177,48448)]
 print(json.dumps({'schema':'EC49FGN_COHERENT_EXACT_V1',
 'frozen_input':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'all_h8_candidate_counts':dict(counts),'all_h8_keys':50,
 'reports':reports},indent=2,sort_keys=True))
if __name__=='__main__':main()
