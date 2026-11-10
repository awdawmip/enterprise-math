#!/usr/bin/env python3
"""Independent direct candidate-word crosscheck of exact per-key singleton minima.
Sample is deterministic with representative positive/negative and released-key cases.
The final exact screen enumerates all 42,504 five-subsets; this is a crosscheck.
"""
import json,itertools,collections,random
from EC49FGW_RADIUS5_SCREEN import W,P,all_words,pref,raw_key,validate_profile
from EC49FGW_KEY_SCREEN import min_new_keys_needed,get_key_index
catalog=list(all_words()); by_label=collections.defaultdict(list)
for l,w in catalog:by_label[l].append((w,raw_key(w)))
samples=[(0,1,2,15,19),(0,1,2,17,21),(0,1,4,15,19),(0,1,2,14,18),(0,3,9,18,23)]
rng=random.Random(20261110)
while len(samples)<15:
 q=tuple(sorted(rng.sample(range(24),5)))
 if q not in samples:samples.append(q)
checks=[]
for pr in W['profiles']:
 rows,paths=validate_profile(pr)
 labs=[(r['window'],r['signature']) for r in rows]
 ks=[raw_key(r['word']) for r in rows]
 idx,base,_=get_key_index(catalog,set().union(*paths))
 for Q in samples:
  fixed=set().union(*(paths[i] for i in range(24) if i not in Q))
  B=93-len(fixed); retained={ks[i] for i in range(24) if i not in Q}
  if B<0:continue
  opts=[]
  for i in Q:
   lab=labs[i]
   local={}
   for w,k in by_label[lab]:
    d=len(set(pref(w))-fixed)
    if d<local.get(k,1000):local[k]=d
   fromidx={k:v for (l,k),v in base.items() if l==lab}
   for p in fixed:
    for (ll,k),L in idx[p].items():
     if ll==lab:fromidx[k]=min(fromidx.get(k,1000),L-len(p))
   assert fromidx==local,(pr['profile_id'],Q,lab,fromidx,local)
   opts.append({k for k,v in local.items() if v<=B})
  if any(not z for z in opts):need=1000
  else:need=min_new_keys_needed(opts,retained)
  checks.append({'profile':pr['profile_id'],'Q':Q,'B':B,
                 'free_key_slots':7-len(retained),'key_cover_minimum':need,
                 'feasible_key_cover':need<=7-len(retained)})
assert len(checks)>=10
(P/'EXACT_SAMPLE_CROSSCHECK_EC49FGW.json').write_text(
 json.dumps({'schema':'EC49FGW_INDEPENDENT_DIRECT_WORD_SAMPLE_V1',
             'checked':len(checks),'samples':checks},indent=2)+'\n')
print('EC49FGW_DIRECT_CROSSCHECK_PASS',len(checks))
