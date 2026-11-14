#!/usr/bin/env python3
"""Build independent native-prefix C++ input from frozen legal words and witnesses."""
from collections import defaultdict
from itertools import combinations
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,validate_profile
C=list(all_words())
cov=defaultdict(set)
with open('EC49FJK_CATALOG.tsv','w') as fp:
 for lab,w in C:
  k=raw_key(w);cov[k].add(lab)
  fp.write(f'{lab[0]}\t{lab[1]}\t{k[0]}\t{k[1]}\t{k[2]}\t{w}\n')
assert len(cov)==94 and len(C)==178850
records=[]
with open('EC49FJK_CASES.tsv','w') as fp:
 for profile in W['profiles']:
  rows,paths=validate_profile(profile);sp=defaultdict(int);sk=defaultdict(int)
  for i,(r,ps) in enumerate(zip(rows,paths)):
   sk[raw_key(r['word'])]|=1<<i
   for p in ps:sp[p]|=1<<i
  oldkeys=set(sk);seen=0
  for Q in combinations(range(24),6):
   mask=sum(1<<i for i in Q)
   if sum((v&mask)==v for v in sp.values())!=24:continue
   released={k for k,v in sk.items() if (v&mask)==v}
   if not released:continue
   assert len(released)==1
   F={p for p,v in sp.items() if (v&mask)!=v};assert len(F)==70
   fixed=oldkeys-released;labels=[(rows[i]['window'],rows[i]['signature']) for i in Q]
   uncovered={lab for lab in labels if not any(lab in cov[k] for k in fixed)}
   candidates=[k for k in cov if k not in fixed and uncovered.issubset(cov[k])]
   def keytext(ks):return ';'.join(','.join(map(str,k)) for k in sorted(ks))
   opts='|'.join(keytext(fixed|{k}) for k in candidates)
   fp.write(f'{profile["profile_id"]}\t{",".join(map(str,Q))}\t{";".join(f"{h},{sig}" for h,sig in labels)}\t{opts}\t{";".join(p.hex() for p in sorted(F))}\n')
   seen+=1
   records.append((profile['profile_id'],Q,len(candidates)))
  assert seen==9
assert len(records)==18
print('MAKE_EC49FJK_INPUT_PASS cases=18 options_total='+str(sum(k for _,_,k in records)))
