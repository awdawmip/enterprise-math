#!/usr/bin/env python3
"""Exact 3-demand union bound after exact 1- and 2-demand screens, radius 7."""
import sys,json,itertools,hashlib,time
from collections import defaultdict,Counter
from pathlib import Path
ROOT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'EC49FJR'))
from ec49fjd_shared import W,PIN,raw_key,pref,validate_profile,all_words
allcat=list(all_words());assert len(allcat)==178850
report=[]
for profile in W['profiles']:
 rows,original=validate_profile(profile)
 keys={raw_key(d['word']) for d in rows}
 by=defaultdict(list)
 for lab,w in allcat:
  if raw_key(w) in keys:by[lab].append(pref(w))
 sup=defaultdict(int);ksu=defaultdict(int)
 for i,(d,ps) in enumerate(zip(rows,original)):
  ksu[raw_key(d['word'])]|=1<<i
  for p in ps:sup[p]|=1<<i
 assert len(sup)==94 and len(ksu)==7
 counters=defaultdict(Counter);samples=[];cache={}
 for Q in itertools.combinations(range(24),7):
  mask=sum(1<<i for i in Q)
  if any((s&mask)==s for s in ksu.values()):continue
  B=sum((s&mask)==s for s in sup.values())-1
  if B not in (5,7):continue
  F=frozenset(p for p,s in sup.items() if (s&mask)!=s)
  labels=[(rows[i]['window'],rows[i]['signature']) for i in Q]
  def opts(lab):
   key=(F,lab,B)
   if key not in cache:
    tmp=set()
    for ps in by[lab]:
     if len(ps)>B and ps[len(ps)-B-1] not in F:continue
     i=0
     while i<len(ps) and ps[i] in F:i+=1
     if len(ps)-i<=B:tmp.add(frozenset(ps[i:]))
    cache[key]=tuple(tmp)
   return cache[key]
  choices={l:opts(l) for l in labels}
  if not all(choices.values()):
   counters[B]['singleton']+=1;continue
  badpair=next(((a,b) for a,b in itertools.combinations(labels,2) if not any(len(x|y)<=B for x in choices[a] for y in choices[b])),None)
  if badpair:
   counters[B]['pair']+=1;continue
  # Check high-window demand triples first (for speed); exact cross-branch union.
  triples=sorted(itertools.combinations(labels,3),key=lambda t:(-sum(x[0] for x in t),t))
  badtriple=None
  for a,b,c in triples:
   if not any(len(x|y|z)<=B for x in choices[a] for y in choices[b] for z in choices[c]):
    badtriple=(a,b,c,min(len(x|y|z) for x in choices[a] for y in choices[b] for z in choices[c]));break
  if badtriple:
   counters[B]['triple']+=1
   if len(samples)<20:samples.append({'Q':Q,'budget':B,'three_labels':badtriple[:3],'exact_min':badtriple[3]})
  else:
   counters[B]['unresolved']+=1
 print('TRIPLE',profile['profile_id'],dict(counters), 'cache',len(cache),flush=True)
 report.append({'profile':profile['profile_id'],'budgets':{str(k):dict(v) for k,v in counters.items()},'examples':samples,'cache':len(cache)})
obj={'schema':'EC49FJV_RADIUS7_TRIPLE_V1','pin':PIN,'results':report}
p=ROOT/'R7_TRIPLE_B5_B7_REPORT.json';p.write_text(json.dumps(obj,indent=2)+'\n')
print('TRIPLE_PASS',hashlib.sha256(p.read_bytes()).hexdigest())
