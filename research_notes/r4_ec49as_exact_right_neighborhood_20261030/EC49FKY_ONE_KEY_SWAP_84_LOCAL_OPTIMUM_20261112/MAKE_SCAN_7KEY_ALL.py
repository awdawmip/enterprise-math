#!/usr/bin/env python3
"""Enumerate entire frozen BRC catalogue, the 84-witness key neighborhood,
produce all exactly covered one-key swaps and literal signed native inputs."""
import collections,json,sys
from pathlib import Path
FROZEN=Path(__file__).resolve().parent.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'
sys.path.insert(0,str(FROZEN))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,pref,raw_key
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
cat=list(all_words()); labs=sorted({a for a,w in cat}); ids={a:i for i,a in enumerate(labs)}
assert len(cat)==178850 and len(labs)==24
byk=collections.defaultdict(list); covk=collections.defaultdict(int)
for lab,w in cat:
 k=raw_key(w); byk[k].append((ids[lab],pref(w)[-1].hex())); covk[k]|=1<<ids[lab]
keys=sorted(covk)
assert len(keys)==94
base={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
full=(1<<24)-1
sets=[dict(origin='EC49FKX_84',keyset=sorted(base),dropped=None,added=None)]
rejected=0
for old in sorted(base):
 for new in keys:
  if new in base:continue
  ks=base-{old}|{new}; cover=0
  for k in ks:cover|=covk[k]
  if cover==full:sets.append(dict(origin='ONE_KEY_SWAP',keyset=sorted(ks),dropped=old,added=new))
  else:rejected+=1
assert len(sets)==193 and rejected==417
with open('SCAN_SETS_ALL.json','w') as f:json.dump(sets,f)
with open('SCAN_ALL_DATA.txt','w') as f:
 f.write(str(len(sets))+'\n')
 for s in sets:
  rows=[r for k in s['keyset'] for r in byk[tuple(k)]]
  f.write(str(len(rows))+'\n')
  for lab,steps in rows:f.write(str(lab)+' '+steps+'\n')
print('EC49FKY_FROZEN_CATALOGUE_PASS',len(cat),'raw_keys',len(keys),
      'one_key_swaps',609,'coverage_impossible',rejected,
      'covered_swaps',len(sets)-1,'total_instances',len(sets))
