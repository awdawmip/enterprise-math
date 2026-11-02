#!/usr/bin/env python3
"""EC49EXD finite exact signed-native X6 / symbolic BRC proof reproduction.
Dependencies: predecessor VERIFY_EC49ER.py (2026-11-03 frozen native model).
The script enumerates all h=2..7 return words, certifies essential observer
signature families, computes strict lower bounds, and validates witness.
Exact trie work can be long: run on an uninterrupted execution environment.
"""
from VERIFY_EC49ER import *
from collections import defaultdict, Counter
from itertools import product
import json,time
T4=frozenset(signature(w) for w in BASE)
T2=frozenset(signature(w) for w in ('feg','gef'))
assert len(T4)==4 and len(T2)==2 and not T4&T2

class N:
 def __init__(self):self.kids={};self.mask=0

def optimistic_min(by_sig,free):
 labels={s:i for i,s in enumerate(sorted(by_sig))}
 root=N();nn=1
 for sig,ww in by_sig.items():
  for w in ww:
   node=root
   for step in path(w):
    if step not in node.kids:node.kids[step]=N();nn+=1
    node=node.kids[step]
   node.mask|=1<<labels[sig]
 def dp(node,pref):
  rows={0:0}
  for step,child in node.kids.items():
   nested=dp(child,pref+(step,));t={}
   for m,v in rows.items():
    for n,w in nested.items():
     key=m|n;cost=v+w
     if cost<t.get(key,10**20):t[key]=cost
   rows=t
  if pref:
   charge=int(pref not in free);t={0:0}
   for mask,val in rows.items():
    key=mask|node.mask
    if key and val+charge<t.get(key,10**20):t[key]=val+charge
   rows=t
  return rows
 return dp(root,())[(1<<len(labels))-1],nn

def run():
 t=time.monotonic();fs=fibers()
 group={};counts={};types={}
 for h in range(2,8):
  if h==7:
   d=defaultdict(list)
   for z in product(OPS,repeat=h):
    w=''.join(z)
    if displacement(w)==(2,0,0,0,0,0):d[poscount(w)].append(w)
   fs[h]=dict(d)
  counts[h]=sum(len(x) for x in fs[h].values())
  group[h]={p:essential(ws) for p,ws in fs[h].items()}
  group[h]={p:s for p,s in group[h].items() if s}
  assert all(s in (T4,T2) for s in group[h].values())
  types[h]=(sum(s==T4 for s in group[h].values()),sum(s==T2 for s in group[h].values()))
 assert tuple(counts.values())==(8,51,304,1770,10224,58947),counts
 assert tuple(types.values())==((1,0),(3,1),(7,2),(13,4),(22,6),(34,9)),types
 p0=poscount('ce')
 schedules=[(p0,)+ps for ps in product(*(sorted(group[h]) for h in range(3,8)))
            if len({p0,*ps})==4]
 assert len(schedules)==26207,len(schedules)
 print('ENUMERATION PASS; M4',len(schedules),'rank-fibers',types,flush=True)
 # Complete finite terminal increment bound: 101 fibers, with all earlier
 # returning words made free (a superset of possible paid prefixes).
 universal=set(PAID_BASE);terminal=[]
 for h in range(3,8):
  for p,req in group[h].items():
   by=defaultdict(list)
   for w in fs[h][p]:
    sig=signature(w)
    if sig in req:by[sig].append(w)
   v,n=optimistic_min(by,universal)
   assert v>=2*len(req),(h,p,v)
   terminal.append((h,p,len(req),v,n))
  for ws in fs[h].values():universal.update(prefixes(ws))
 assert len(terminal)==101
 print('TERMINAL LEMMA PASS',len(terminal),flush=True)
 # Every distinct h5 schedule prefix: exact signed native prefix trie DP.
 p5=sorted({s[:4] for s in schedules})
 assert len(p5)==426,len(p5)
 e5={q:exact_trie_opt(fs,{h:q[h-2] for h in range(3,6)})['E'] for q in p5}
 residue=[s for s in schedules
   if e5[s[:4]]+2*(len(group[6][s[4]])+len(group[7][s[5]]))<72]
 assert len(residue)==212,len(residue)
 print('H5 screening PASS',len(schedules)-len(residue),flush=True)
 p6=sorted({s[:5] for s in residue});assert len(p6)==196,len(p6)
 e6={q:exact_trie_opt(fs,{h:q[h-2] for h in range(3,7)})['E'] for q in p6}
 rest=[s for s in residue if e6[s[:5]]+2*len(group[7][s[5]])<72]
 assert len(rest)==4,len(rest)
 final=[]
 for s in rest:
  assert e6[s[:5]]==66 and group[7][s[5]]==T2
  free=set(PAID_BASE)
  for h in range(3,7):
   for w in fs[h][s[h-2]]:
    if signature(w) in group[h][s[h-2]]:free.update(prefixes([w]))
  by=defaultdict(list)
  for w in fs[7][s[5]]:
   if signature(w) in T2:by[signature(w)].append(w)
  v,n=optimistic_min(by,free);assert v==6,(s,v)
  final.append({'schedule':[list(p) for p in s],'E6':66,'h7_extra_lower':v,'trie_nodes':n})
 witness={2:'ce de ec ed'.split(),3:'feg gef'.split(),
  4:'fegg gefg'.split(),5:'feggg gefgg'.split(),
  6:'fegggc fegggd gefggc gefggd'.split(),
  7:'fegggfg gefggfg'.split()}
 allwords=[w for ws in witness.values() for w in ws]
 for h,ws in witness.items():
  assert all(displacement(w)==(2,0,0,0,0,0) for w in ws)
  assert len({poscount(w) for w in ws})==1
  assert rational_rank({signature(w) for w in ws})==9
 assert (len(prefixes(allwords)),len({poscount(ws[0]) for ws in witness.values()}),
         len({signature(w) for w in allwords}))==(72,4,6)
 result={'status':'PASS','research_id':'EC49EXD','theorem':'H7 M4 S<=6 min E=72',
   'return_words':counts,'rank_fiber_types':types,'all_schedules':len(schedules),
   'h5_distinct':len(p5),'h5_screened':len(schedules)-len(residue),
   'h6_distinct':len(p6),'h6_screened':len(residue)-len(rest),
   'final_cases':final,'terminal_lemma_cases':len(terminal),
   'elapsed_seconds':round(time.monotonic()-t,2)}
 with open('EC49EXD_REPLAY_EXECUTED.json','w') as f:json.dump(result,f,indent=2)
 print('PASS EC49EXD E=72',result,flush=True)
if __name__=='__main__':run()
