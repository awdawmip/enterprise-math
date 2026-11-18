from ec49fjd_shared import *
from itertools import combinations
from collections import defaultdict
from pathlib import Path
P=Path(__file__).parent
with (P/'B17_CATALOG.tsv').open('w') as f:
 for (h,s),w in cat:
  x,y,z=raw_key(w)
  f.write(f'{h}\t{s}\t{x}\t{y}\t{z}\t{w}\n')
with (P/'B17_CASES.tsv').open('w') as out:
 for pr in W['profiles']:
  rows,paths=validate_profile(pr);ks=[raw_key(d['word']) for d in rows]
  ksup=defaultdict(int);psup=defaultdict(int)
  for i,(k,ps) in enumerate(zip(ks,paths)):
   ksup[k]|=1<<i
   for p in ps:psup[p]|=1<<i
  originalkeys=frozenset(ksup)
  for Q in combinations(range(24),6):
   qm=sum(1<<i for i in Q)
   if sum(s&qm==s for s in psup.values())!=18:continue
   released=frozenset(k for k,s in ksup.items() if s&qm==s)
   if not released:continue
   F=frozenset(p for p,s in psup.items() if s&qm!=s)
   labs=tuple((rows[i]['window'],rows[i]['signature']) for i in Q)
   fixed=originalkeys-released
   if all(not key_cover(labs,fixed,len(released),ban) for ban in released):continue
   assert len(fixed)==6 and len(released)==1
   candidates=[]
   for k in cover:
    if k in fixed:continue
    # Necessary, sound budget screen for participation of the new key.
    if not any(any(len(pref(w))-sum(p in F for p in pref(w))<=17 for w in bykey[k].get(lab,[])) for lab in labs):continue
    candidates.append(k)
   assert released.issubset(set(candidates))
   fk=';'.join(','.join(map(str,k)) for k in sorted(fixed))
   ck=';'.join(','.join(map(str,k)) for k in sorted(candidates))
   labels=';'.join(f'{h},{s}' for h,s in labs)
   fps=';'.join(p.hex() for p in sorted(F))
   out.write(f'{pr["profile_id"]}\t{",".join(map(str,Q))}\t{labels}\t{fk}\t{ck}\t{fps}\n')
print('catalog',len(cat),'unforced_cases',sum(1 for l in (P/'B17_CASES.tsv').open()))
