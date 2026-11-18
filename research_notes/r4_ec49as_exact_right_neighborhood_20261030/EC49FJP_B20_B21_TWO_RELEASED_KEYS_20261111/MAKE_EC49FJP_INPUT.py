#!/usr/bin/env python3
"""Exact released-two-original-key B20/B21: exhaustive pair-cover then signed prefix-trie."""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,validate_profile
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
C=list(all_words()); cov=defaultdict(set)
with open('EC49FJP_CATALOG.tsv','w') as f:
 for lab,w in C:
  k=raw_key(w);cov[k].add(lab)
  f.write(f'{lab[0]}\t{lab[1]}\t{k[0]}\t{k[1]}\t{k[2]}\t{w}\n')
assert len(C)==178850 and len(cov)==94
counts=Counter(); rows_record=[]
with open('EC49FJP_CASES.tsv','w') as f:
 for profile in W['profiles']:
  rows,paths=validate_profile(profile); sp=defaultdict(int);sk=defaultdict(int)
  for i,(r,ps) in enumerate(zip(rows,paths)):
   sk[raw_key(r['word'])]|=1<<i
   for p in ps:sp[p]|=1<<i
  assert len(sp)==94 and len(sk)==7
  allkeys=set(sk)
  for Q in combinations(range(24),6):
   mask=sum(1<<i for i in Q)
   removed=sum((v&mask)==v for v in sp.values())
   B=removed-1
   if B not in (20,21):continue
   released={k for k,v in sk.items() if (v&mask)==v}
   if len(released)!=2:continue
   fixed=allkeys-released
   assert len(fixed)==5
   F={p for p,v in sp.items() if (v&mask)!=v}
   assert len(F)==93-B
   labels=[(rows[i]['window'],rows[i]['signature']) for i in Q]
   missing={lab for lab in labels if all(lab not in cov[k] for k in fixed)}
   candidate_keys=[k for k in cov if k not in fixed and cov[k]&missing]
   allowed_pairs=[(k1,k2) for k1,k2 in combinations(candidate_keys,2) if missing.issubset(cov[k1]|cov[k2])]
   assert len(allowed_pairs)==1 and set(allowed_pairs[0])==released,(profile['profile_id'],Q,allowed_pairs)
   def keytext(keys):return ';'.join(','.join(map(str,k)) for k in sorted(keys))
   opts='|'.join(keytext(fixed|set(pair)) for pair in allowed_pairs)
   f.write(f'{profile["profile_id"]}\t{",".join(map(str,Q))}\t{";".join(f"{h},{sig}" for h,sig in labels)}\t{opts}\t{";".join(p.hex() for p in sorted(F))}\n')
   counts[(profile['profile_id'],B)]+=1
   rows_record.append({'profile':profile['profile_id'],'B':B,'Q':list(Q),
                       'fixed_prefixes':len(F),'forced_pair':sorted(map(list,released)),
                       'allowed_added_key_pairs':len(allowed_pairs)})
assert dict(counts)=={('A',20):8,('A',21):1,('B',20):8,('B',21):1},counts
assert len(rows_record)==18
Path('EC49FJP_INPUT_REPORT.json').write_text(json.dumps({'science_pin':PIN,'catalog_words':len(C),'complete_keys':len(cov),
 'counts':{f'{p}_B{b}':n for (p,b),n in sorted(counts.items())},'cases':rows_record},indent=2)+'\n')
print('EC49FJP_PAIR_COVER_PASS',dict(counts))
