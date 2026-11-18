from ec49fjd_shared import *
from itertools import combinations
from collections import defaultdict,Counter
from pathlib import Path
import json,time,hashlib
P=Path(__file__).parent
N=0;kscreen=Counter(); metrics=[]; options=[]
with (P/'B18_CATALOG.tsv').open('w') as c:
 for lab,w in cat:
  k=raw_key(w); c.write(f'{lab[0]}\t{lab[1]}\t{k[0]}\t{k[1]}\t{k[2]}\t{w}\n')
with (P/'B18_CASES.tsv').open('w') as out:
 for pr in W['profiles']:
  rows,paths=validate_profile(pr)
  ks=[raw_key(d['word']) for d in rows]; originalkeys=frozenset(ks)
  psup=defaultdict(int);ksup=defaultdict(int)
  for i,(k,ps) in enumerate(zip(ks,paths)):
   ksup[k]|=1<<i
   for p in ps:psup[p]|=1<<i
  j=0
  for Q in combinations(range(24),6):
   m=sum(1<<i for i in Q)
   if sum(s&m==s for s in psup.values())!=19:continue
   R=frozenset(k for k,s in ksup.items() if s&m==s)
   if not R:continue
   F=frozenset(p for p,s in psup.items() if s&m!=s)
   labs=tuple((rows[i]['window'],rows[i]['signature']) for i in Q)
   fixed=originalkeys-R
   forced=all(not key_cover(labs,fixed,len(R),ban) for ban in R)
   if forced:
    newoptions=[originalkeys]
   else:
    assert len(fixed)==6
    allowednew=[]
    for k in cover:
     if k in fixed:continue
     if not any(any(len(pref(w))-sum(p in F for p in pref(w))<=18 for w in bykey[k].get(lab,[])) for lab in labs):continue
     allowednew.append(k)
    assert R.issubset(set(allowednew)),(pr['profile_id'],Q)
    newoptions=[fixed|frozenset([k]) for k in allowednew]
   def encodekeys(K):return ';'.join(','.join(map(str,k)) for k in sorted(K))
   opt='|'.join(encodekeys(o) for o in newoptions)
   labels=';'.join(f'{h},{s}' for h,s in labs)
   fps=';'.join(p.hex() for p in sorted(F))
   out.write(f'{pr["profile_id"]}\t{",".join(map(str,Q))}\t{labels}\t{opt}\t{fps}\n')
   j+=1;kscreen['unforced' if not forced else 'forced']+=1
   kscreen['keyset_options']+=len(newoptions)
   if not forced:options.append({'profile':pr['profile_id'],'Q':Q,'candidates':len(newoptions)})
  assert j==418,(pr['profile_id'],j)
  metrics.append({'profile_id':pr['profile_id'],'positions':j})
print('KEYSCREEN',dict(kscreen));print('UNFORCED',options)
for x in ['B18_CATALOG.tsv','B18_CASES.tsv']:
 b=(P/x).read_bytes();print(x,len(b),hashlib.sha256(b).hexdigest())
