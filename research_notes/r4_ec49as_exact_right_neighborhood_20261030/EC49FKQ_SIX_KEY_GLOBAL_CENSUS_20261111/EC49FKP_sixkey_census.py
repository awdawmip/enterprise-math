#!/usr/bin/env python3
"""Exact minimal-cover enumeration of six full BRC cache keys, frozen EC49FGW catalogue."""
import collections,itertools,sys,json,time
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P))
import EC49FGW_RADIUS5_SCREEN as g
labels=sorted((h,s) for h,ss in g.REQ.items() for s in ss); LI={x:i for i,x in enumerate(labels)};FULL=(1<<len(labels))-1
masks=collections.defaultdict(int)
for lab,w in g.all_words():masks[g.raw_key(w)]|=1<<LI[lab]
assert len(masks)==94
forced=[(2,16),(2,32),(3,16),(4,1),(7,1)]
keyfamilies=[tuple(k for k in sorted(masks) if masks[k]>>LI[x]&1) for x in forced]
assert [len(a) for a in keyfamilies]==[1,1,2,7,34]
assert all(not(set(a)&set(b)) for i,a in enumerate(keyfamilies) for b in keyfamilies[i+1:])
quints=list(itertools.product(*keyfamilies));assert len(quints)==476
five={frozenset(k) for k in quints if all(k) and (masks[k[0]]|masks[k[1]]|masks[k[2]]|masks[k[3]]|masks[k[4]])==FULL}
assert len(five)==16
six=set(); allK=tuple(masks)
for qq in quints:
 base=set(qq); v=0
 for k in base:v|=masks[k]
 for k in allK:
  if k not in base and v|masks[k]==FULL:
   six.add(frozenset((*base,k)))
assert all(len(k)==6 and __import__('functools').reduce(int.__or__,[masks[v] for v in k],0)==FULL for k in six)
contain5=sum(any(f<=s for f in five) for s in six)
new6=len(six)-contain5
res={'schema':'EC49FKP_SIX_FULL_RAW_KEY_COVER_CENSUS_V1','scientific_pin':g.PIN,'key_count':len(masks),'label_count':len(labels),'five_disjoint_label_families':[len(x) for x in keyfamilies], 'enumerated_five_family_quintuples':len(quints),'five_key_covers':len(five),'six_key_covers':len(six),'six_key_covers_containing_five_cover':contain5,'minimal_six_key_covers':new6,'all_minimal_six_key_covers':[sorted(map(list,s)) for s in sorted((x for x in six if not any(f<=x for f in five)),key=lambda x:tuple(sorted(x)))]}
(P/'EC49FKP_SIXKEY_CENSUS.json').write_text(json.dumps(res,indent=2)+'\n')
print('EC49FKP_SIX_KEY_CENSUS_PASS',json.dumps({k:v for k,v in res.items() if k!='all_minimal_six_key_covers'}),flush=True)
