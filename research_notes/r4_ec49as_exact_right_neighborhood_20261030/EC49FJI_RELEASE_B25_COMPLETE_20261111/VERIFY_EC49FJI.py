#!/usr/bin/env python3
"""EC49FJI: exhaustive released-key radius-6 B=25 proof, frozen EC49FGW model.
Copy EC49FGW_RADIUS5_SCREEN.py and EC49FGJ_SEVEN_KEY_94_WITNESSES.json
from pinned PR #1730 evidence beside this script. Python >=3.9; exact integer arithmetic.
"""
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,pref,validate_profile
from collections import defaultdict,Counter
from itertools import combinations
import json
B=25; CAP=26
catalog=defaultdict(list); coverage=defaultdict(set)
for lab,w in all_words():
 k=raw_key(w);catalog[lab,k].append(w);coverage[k].add(lab)
assert len(coverage)==94 and sum(map(len,catalog.values()))==178850

def must_restore(labs,fixed,missing_key):
 """No choice of one replacement key other than missing_key covers all labels."""
 remaining=[lab for lab in labs if not any(lab in coverage[k] for k in fixed)]
 return not any(k not in fixed and k!=missing_key and all(lab in coverage[k] for lab in remaining) for k in coverage)

def exact_min(F,labs,keys):
 ch=[{}];terminal=[0];cost=[0]
 for j,lab in enumerate(labs):
  for k in keys:
   for w in catalog.get((lab,k),()):
    u=0
    for p in pref(w):
     a=p[-1];v=ch[u].get(a)
     if v is None:
      v=len(ch);ch[u][a]=v;ch.append({});terminal.append(0);cost.append(int(p not in F))
     u=v
    terminal[u]|=1<<j
 dp=[None]*len(ch)
 for u in range(len(ch)-1,-1,-1):
  e=terminal[u];s={m:0 for m in range(64) if m&~e==0}
  for v in ch[u].values():
   ns=s.copy()
   for a,ca in s.items():
    for b,cb in dp[v].items():
     if a&b:continue
     c=ca+cb+cost[v]; ab=a|b
     if c<ns.get(ab,CAP):ns[ab]=c
   s={a:c for a,c in ns.items() if c<CAP}
  dp[u]=s
 return dp[0].get(63,CAP),len(ch)

results=[];hist=Counter()
for pr in W['profiles']:
 rows,paths=validate_profile(pr)
 assert len(rows)==24
 psup=defaultdict(int);ksup=defaultdict(int)
 for i,(r,ps) in enumerate(zip(rows,paths)):
  ksup[raw_key(r['word'])]|=1<<i
  for p in ps:psup[p]|=1<<i
 assert len(psup)==94 and len(ksup)==7
 count=0
 for Q in combinations(range(24),6):
  mask=sum(1<<i for i in Q)
  if sum((s&mask)==s for s in psup.values())!=26:continue
  released=[k for k,s in ksup.items() if (s&mask)==s]
  if not released:continue
  assert len(released)==1
  F={p for p,s in psup.items() if (s&mask)!=s}
  labs=[(rows[i]['window'],rows[i]['signature']) for i in Q]
  fixed=set(ksup)-set(released)
  assert len(F)==68 and must_restore(labs,fixed,released[0])
  opt,nodes=exact_min(F,labs,set(ksup))
  assert opt==26,(pr['profile_id'],Q,opt)
  orig=set().union(*(set(paths[i]) for i in range(24)))
  assert len(orig)==94 and len(orig-F)==26
  results.append({'profile':pr['profile_id'],'Q':list(Q), 'exact_increment':opt,'trie_nodes':nodes})
  hist[nodes]+=1;count+=1
 assert count==8,(pr['profile_id'],count)
assert len(results)==16
print(json.dumps({'schema':'EC49FJI_AUTHOR_FINITE_V1','science_pin':PIN,
 'cases':len(results),'cost_total':94,'trie_histogram':dict(hist),'results':results},indent=2))
print('EC49FJI_ALL_16_PASS')
