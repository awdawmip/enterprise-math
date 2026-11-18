#!/usr/bin/env python3
"""Full 7-key cover and exact six-label signed-trie cases, release B=16,17,18,19.

Scientific input frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Exhaust all A/B choose(24,6) fixed backgrounds and all complete key combinations.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,validate_profile
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
C=list(all_words());cov=defaultdict(set)
with open('EC49FJQ_CATALOG.tsv','w') as f:
 for lab,w in C:
  k=raw_key(w);cov[k].add(lab)
  f.write(f'{lab[0]}\t{lab[1]}\t{k[0]}\t{k[1]}\t{k[2]}\t{w}\n')
assert len(C)==178850 and len(cov)==94
counts=Counter();option_hist=Counter();records=[]
with open('EC49FJQ_CASES.tsv','w') as f:
 for profile in W['profiles']:
  rows,paths=validate_profile(profile);sp=defaultdict(int);sk=defaultdict(int)
  for i,(r,ps) in enumerate(zip(rows,paths)):
   sk[raw_key(r['word'])]|=1<<i
   for p in ps:sp[p]|=1<<i
  assert len(sp)==94 and len(sk)==7
  allkeys=set(sk)
  for Q in combinations(range(24),6):
   mask=sum(1<<i for i in Q)
   rem=sum((v&mask)==v for v in sp.values());B=rem-1
   if B not in (16,17,18,19):continue
   released={k for k,v in sk.items() if (v&mask)==v}
   if not released:continue
   fixed=allkeys-released;r=len(released)
   assert r in (1,2), (profile['profile_id'],Q,r)
   F={p for p,v in sp.items() if (v&mask)!=v}
   assert len(F)==93-B
   labels=[(rows[i]['window'],rows[i]['signature']) for i in Q]
   missing={lab for lab in labels if all(lab not in cov[k] for k in fixed)}
   # Every possible completion (<=7 total full keys) is included in at least
   # one superset consisting of the five/six fixed keys + r new keys.
   # Enumerate all keys outside fixed, including an extra key which may
   # improve prefixes even when another key alone covers the missing labels.
   candidate=[k for k in cov if k not in fixed]
   choices=[t for t in combinations(candidate,r) if missing.issubset(set().union(*(cov[k] for k in t)))]
   if r==1:
    assert set(choices)==set((k,) for k in candidate if missing.issubset(cov[k]))
   assert choices,(profile['profile_id'],Q,B)
   assert any(set(t)==released for t in choices)
   def keytext(keys):return ';'.join(','.join(map(str,k)) for k in sorted(keys))
   opts='|'.join(keytext(fixed|set(choice)) for choice in choices)
   f.write(f'{profile["profile_id"]}\t{",".join(map(str,Q))}\t{";".join(f"{h},{sig}" for h,sig in labels)}\t{opts}\t{";".join(p.hex() for p in sorted(F))}\n')
   counts[(profile['profile_id'],B,r)]+=1;option_hist[(B,r,len(choices))]+=1
   records.append({'profile':profile['profile_id'],'B':B,'Q':list(Q),'r':r,'key_choices':len(choices),'retained_prefixes':len(F)})
expected={(p,B,r):n for p in 'AB' for (B,r,n) in [(16,1,64),(17,1,868),(17,2,68),(18,1,386),(18,2,32),(19,1,298),(19,2,10)]}
assert dict(counts)==expected,(counts,expected)
assert len(records)==3452,len(records)
Path('EC49FJQ_INPUT_REPORT.json').write_text(json.dumps({'science_pin':PIN,'catalog_words':len(C),'complete_keys':len(cov),
 'counts':{f'{p}_B{B}_r{r}':n for (p,B,r),n in sorted(counts.items())},
 'key_choice_count':sum(row['key_choices'] for row in records),
 'key_choice_histogram':{f'B{B}_r{r}_N{N}':n for (B,r,N),n in sorted(option_hist.items())},
 'cases':records},indent=2)+'\n')
print('EC49FJQ_INPUT_PASS',len(records),'KEYSET_TRIES',sum(row['key_choices'] for row in records),'HIST',dict(option_hist))
