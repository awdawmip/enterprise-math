#!/usr/bin/env python3
"""Exact 6-of-24 census, original seven keys retained, high budgets 24,25,27,28,29."""
from pathlib import Path
import sys,json,hashlib
from itertools import combinations
from collections import Counter,defaultdict
P=Path(__file__).resolve().parent
sys.path.insert(0,str((P/'../EC49FJR').resolve()))
from ec49fjd_shared import W,PIN,raw_key,pref,validate_profile

def encode(keys):return ';'.join(','.join(map(str,k)) for k in sorted(keys))
counts=Counter(); cases=[]
with (P/'FJT_CASES.tsv').open('w') as fh:
 for profile in W['profiles']:
  rows,paths=validate_profile(profile);psu=defaultdict(int);ksu=defaultdict(int)
  for i,(row,ps) in enumerate(zip(rows,paths)):
   ksu[raw_key(row['word'])]|=1<<i
   for p in ps:psu[p]|=1<<i
  assert len(psu)==94 and len(ksu)==7
  keys=encode(ksu)
  for Q in combinations(range(24),6):
   mask=sum(1<<i for i in Q)
   b=sum((s&mask)==s for s in psu.values())-1
   if b not in (24,25,27,28,29):continue
   released=sum((s&mask)==s for s in ksu.values())
   if released:continue
   F={p for p,s in psu.items() if (s&mask)!=s}
   assert len(F)==93-b
   labels=[(rows[i]['window'],rows[i]['signature']) for i in Q]
   fh.write(f'{profile["profile_id"]}\t{",".join(map(str,Q))}\t{";".join(f"{h},{s}" for h,s in labels)}\t{keys}\t{";".join(p.hex() for p in sorted(F))}\n')
   counts[(profile['profile_id'],b)]+=1
   cases.append({'profile':profile['profile_id'],'positions':Q,'B':b})
assert len(cases)==232,(len(cases),counts)
summary={'schema':'EC49FJT_NONRELEASED_HIGH_B_V1','frozen_scientific_pin':PIN,'cases':len(cases),'counts':{f'{p}_B{b}':n for (p,b),n in sorted(counts.items())},'case_index':cases}
(P/'FJT_INPUT_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
for name in ('FJT_CASES.tsv','FJT_INPUT_SUMMARY.json'):
 f=P/name; print(name,f.stat().st_size,hashlib.sha256(f.read_bytes()).hexdigest())
print('FJT_GENERATOR_PASS',counts)
