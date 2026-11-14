from ec49fjd_shared import *
from itertools import combinations
from collections import defaultdict,Counter
from pathlib import Path
import json,time,hashlib
P=Path(__file__).parent
stats=[];cases=[]
with (P/'B25_CATALOG.tsv').open('w') as fh:
 for lab,w in cat:
  k=raw_key(w);fh.write(f'{lab[0]}\t{lab[1]}\t{k[0]}\t{k[1]}\t{k[2]}\t{w}\n')
with (P/'B25_CASES.tsv').open('w') as fh:
 for profile in W['profiles']:
  rows,paths=validate_profile(profile)
  ksu=defaultdict(int);psu=defaultdict(int)
  for i,(row,ps) in enumerate(zip(rows,paths)):
   ksu[raw_key(row['word'])]|=1<<i
   for p in ps:psu[p]|=1<<i
  original=frozenset(ksu)
  seen=0
  for Q in combinations(range(24),6):
   mask=sum(1<<i for i in Q)
   if sum(s&mask==s for s in psu.values())!=26:continue
   R=frozenset(k for k,s in ksu.items() if s&mask==s)
   if not R:continue
   F=frozenset(p for p,s in psu.items() if s&mask!=s)
   assert len(F)==68
   labels=tuple((rows[i]['window'],rows[i]['signature']) for i in Q)
   fixed=original-R
   forced=all(not key_cover(labels,fixed,len(R),ban) for ban in R)
   assert forced and len(R)==1, (profile['profile_id'],Q,forced,R)
   def enc(K):return ';'.join(','.join(map(str,k)) for k in sorted(K))
   fh.write(f'{profile["profile_id"]}\t{",".join(map(str,Q))}\t{";".join(f"{h},{s}" for h,s in labels)}\t{enc(original)}\t{";".join(p.hex() for p in sorted(F))}\n')
   cases.append({'profile':profile['profile_id'],'Q':list(Q),'labels':[list(x) for x in labels], 'released_key':[list(k) for k in R]})
   seen+=1
  assert seen==8,(profile['profile_id'],seen)
  stats.append({'profile':profile['profile_id'],'cases':seen,'all_keys_forced':seen})
(Path(P/'B25_CASE_SUMMARY.json')).write_text(json.dumps({'frozen_science_pin':PIN,'profiles':stats,'cases':cases},indent=2)+'\n')
for x in ['B25_CATALOG.tsv','B25_CASES.tsv','B25_CASE_SUMMARY.json']:
 b=(P/x).read_bytes();print(x,len(b),hashlib.sha256(b).hexdigest())
