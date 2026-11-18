#!/usr/bin/env python3
"""Exact finite singleton lower bound on four-path replacements in EC49FGJ A/B.

Derived necessary condition: for any fixed background F and candidate label i,
min_w |P(w) \ F| <= total budget B(Q). Uses the complete pinned nine-state
enumerator for each original seven-key allowlist and a native-prefix index.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json,itertools,time
from model_ec49fgv import words, REQ, STEPS
P=Path(__file__).parent
D=json.loads((P/'EC49FGJ_SEVEN_KEY_94_WITNESSES.json').read_text())
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert D['frozen_scientific_pin']==PIN

def native_prefix(w):
 b=b'';a=[]
 for ch in w:
  for x in STEPS[ch]:
   b+=bytes((x+3,));a.append(b)
 return a

def prefix_index(keys):
 idx=defaultdict(dict);base={};nw=Counter()
 for h in REQ:
  for k in sorted(keys):
   for sig,w in words(h,k):
    label=(h,sig);pp=native_prefix(w);L=len(pp)
    nw[label]+=1;base[label]=min(base.get(label,1000),L)
    for p in pp:
     d=idx[p];d[label]=min(d.get(label,1000),L)
 return idx,base,nw

def profile_screen(pr):
 rows=sorted(pr['demands'],key=lambda x:(x['window'],x['signature']))
 labels=[(r['window'],r['signature']) for r in rows]
 path=[set(native_prefix(r['word'])) for r in rows]
 keys=set()
 for r in rows:
  pp=[ax for ch in r['word'] for ax in STEPS[ch]]
  keys.add(tuple(pp.count(ax) for ax in (1,2,3)))
 assert len(keys)==7
 idx,base,nw=prefix_index(keys)
 screen={'count':0,'single_label_strictly_excluded':0,'nontrivial_remaining':0,
         'by_budget':Counter(),'rejected_by_budget':Counter()}
 retained=[]
 for Q in itertools.combinations(range(24),4):
  qset=set(Q)
  F=set().union(*(path[i] for i in range(24) if i not in qset))
  B=93-len(F)
  if B<0:continue
  screen['count']+=1;screen['by_budget'][B]+=1
  minima={labels[i]:base[labels[i]] for i in Q}
  for prefix in F:
   for label,L in idx.get(prefix,()).items():
    if label in minima:
     d=L-len(prefix)
     if d<minima[label]:minima[label]=d
  if any(minima[label]>B for label in minima):
   screen['single_label_strictly_excluded']+=1
   screen['rejected_by_budget'][B]+=1
  else:
   screen['nontrivial_remaining']+=1
   retained.append({'quad':list(Q),'labels':[list(labels[i]) for i in Q],
                    'B':B,'singleton_minimums':[minima[labels[i]] for i in Q]})
 return {**{k:(dict(sorted(v.items())) if isinstance(v,Counter) else v)
            for k,v in screen.items()},
         'profile':pr['profile_id'],
         'cache_keys':[list(x) for x in sorted(keys)],
         'candidate_word_count':sum(nw.values()),
         'indexed_prefix_count':len(idx),'retained':retained}

if __name__=='__main__':
 r={'schema':'EC49FGV_SINGLETON_SCREEN_20261110','pin':PIN,
    'profiles':[profile_screen(pr) for pr in D['profiles']]}
 (P/'EXACT_EC49FGT_SINGLETON.json').write_text(json.dumps(r,indent=2)+'\n')
 assert [x['single_label_strictly_excluded'] for x in r['profiles']]==[4832,4832]
 assert [x['nontrivial_remaining'] for x in r['profiles']]==[2734,2734]
 print('EC49FGV_SINGLETON_PASS',[(x['profile'],x['candidate_word_count'])
                                for x in r['profiles']])
