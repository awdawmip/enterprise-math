from ec49fjd_shared import *
from itertools import combinations
from collections import defaultdict
from pathlib import Path
P=Path(__file__).parent
with (P/'B23_CASES.tsv').open('w') as out:
 for pr in W['profiles']:
  rows,paths=validate_profile(pr);ks=[raw_key(d['word']) for d in rows]
  ksup=defaultdict(int);psup=defaultdict(int)
  for i,(k,ps) in enumerate(zip(ks,paths)):
   ksup[k]|=1<<i
   for p in ps:psup[p]|=1<<i
  originalkeys=frozenset(ksup)
  for Q in combinations(range(24),6):
   qm=sum(1<<i for i in Q)
   if sum(s&qm==s for s in psup.values())!=24:continue
   released=frozenset(k for k,s in ksup.items() if s&qm==s)
   if not released:continue
   F=frozenset(p for p,s in psup.items() if s&qm!=s)
   labs=tuple((rows[i]['window'],rows[i]['signature']) for i in Q)
   fixed=originalkeys-released
   forced=all(not key_cover(labs,fixed,len(released),ban) for ban in released)
   assert len(F)==70 and len(fixed)==6 and len(released)==1
   candidates=[]
   if forced: candidates=sorted(released)
   else:
    for k in cover:
     if k in fixed:continue
     if not any(any(len(pref(w))-sum(p in F for p in pref(w))<=23 for w in bykey[k].get(lab,[])) for lab in labs):continue
     candidates.append(k)
   assert released.issubset(set(candidates)),(pr['profile_id'],Q)
   fk=';'.join(','.join(map(str,k)) for k in sorted(fixed))
   ck=';'.join(','.join(map(str,k)) for k in sorted(candidates))
   labels=';'.join(f'{h},{s}' for h,s in labs)
   fps=';'.join(p.hex() for p in sorted(F))
   out.write(f'{pr["profile_id"]}\t{",".join(map(str,Q))}\t{labels}\t{fk}\t{ck}\t{fps}\n')
   print(pr['profile_id'],Q,'forced',forced,'keys',len(candidates),flush=True)
print('n_cases',sum(1 for l in (P/'B23_CASES.tsv').open()))
