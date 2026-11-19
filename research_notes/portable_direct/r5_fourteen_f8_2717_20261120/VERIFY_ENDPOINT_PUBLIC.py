#!/usr/bin/env python3
"""Independent doubled-left-endpoint cross-check of priced 14-way R5 supports."""
from pathlib import Path
from hashlib import sha256
from subprocess import check_output
import json,csv
root=Path(__file__).resolve().parent
src=(root/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert sha256(src).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
data=json.loads(src)
tau=int(json.loads((root/'stages_18.json').read_text())['U'])-1
W=(0,16,32,48,1,64,17,80,18,24,34,82)
result=json.loads((root/'RESULT.json').read_text())
assert tau==int(result['tau'])
def maximal(ms):
 ms=set(ms)
 return tuple(sorted(m for m in ms if not any(m!=n and (m&n)==m for n in ms)))
def independent(u,v):
 h=W+(u,v)
 classes={}
 for k in range(214,315):
  cs=list(map(int,data['counts_and_cohorts'][str(k)]['counts']))
  selected=[cs[i] for i in h]
  masks=[sum(1<<j for j,d in enumerate(selected)
             if abs(2*d-(2*x-tau))<=tau) for x in selected]
  fam=maximal(masks)
  if fam==((1<<14)-1,):continue
  classes[fam]=min(k,classes.get(fam,k))
 return sorted(({'cost':k,'masks':list(fam)} for fam,k in classes.items()),key=lambda x:x['cost'])
with (root/'CLASSES_14.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==29646
sizes={}
for r in rows:
 p=int(r['representative_u']),int(r['representative_v'])
 sizes[p]=sizes.get(p,0)+1
assert len(sizes)==1906
records=result.get('representatives') or result['rep_values']
reps=[(r['u'],r['v']) for r in records]
assert len(reps)==len(set(reps))==13
for r in records:
 u,v=r['u'],r['v']
 assert sizes[u,v]==r.get('member_count',r.get('price_aware_class_size'))
 recorded=json.loads(check_output([str(root/'dump14'),str(root/'window_adj.bin'),str(u),str(v)],text=True))['actions']
 assert recorded==independent(u,v),(u,v)
assert sum(sizes[p] for p in reps)==2717
print('PASS_R5_FOURTEEN_ENDPOINTS 13 unique_representatives 2717 covered_pairs')
