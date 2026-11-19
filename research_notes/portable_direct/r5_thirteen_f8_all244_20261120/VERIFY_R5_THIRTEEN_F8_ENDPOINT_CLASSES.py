#!/usr/bin/env python3
"""Independent full 244-way interval support / priced signature / result-table audit.
Requires frozen EXACT_R5_ALL_101_BUDGETS.json and stages_18.json alongside this file.
Does not independently re-solve all f=7,8 Bellman states.
"""
from pathlib import Path
from collections import Counter
import hashlib, json, csv
root = Path(__file__).parent
raw = (root/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
obj = json.loads(raw)
tau = int(json.loads((root/'stages_18.json').read_text())['U'])-1
centers = {k:tuple(map(int,obj['counts_and_cohorts'][str(k)]['counts'])) for k in range(214,315)}
W=(0,16,32,48,1,64,17,80,18,24,34,82)
rows=list(csv.DictReader((root/'ALL244_VALUES_F0_F8.csv').open()))
cert=list(csv.DictReader((root/'CLASS_CERTIFICATE_F7_F8.csv').open()))
assert len(rows)==244 and len(cert)==48
reps={int(z['signature_class']):int(z['representative_t']) for z in cert}
assert sorted(reps)==list(range(48))
assert all(int(z['f7_exact'])==7385 and int(z['f8_exact'])==8335 for z in cert)
found={}
frequency=Counter()
for row in rows:
 t=int(row['t'])
 h=W+(t,)
 assert t not in W and len(set(h))==13
 priced={}
 for k,cc in centers.items():
  a=[cc[i] for i in h]
  # Doubled LEFT endpoint. Unlike the main C++ code, no adjacency binary is used.
  masks={sum(1<<j for j,w in enumerate(a) if abs(2*w-(2*v-tau))<=tau) for v in a}
  fam=tuple(sorted(m for m in masks if not any(m!=z and m&z==m for z in masks)))
  if fam==(8191,):continue
  priced[fam]=min(k,priced.get(fam,k))
 signature=tuple(sorted((cost,fam) for fam,cost in priced.items()))
 if signature not in found:
  found[signature]=len(found)
  assert reps[found[signature]]==t,(found[signature],t)
 cl=found[signature]
 frequency[cl]+=1
 assert tuple(int(row['f'+str(i)]) for i in range(9))==tuple(735+950*i for i in range(9))
assert sorted(int(row['t']) for row in rows)==sorted(set(range(256))-set(W))
assert len(found)==48
assert Counter(frequency.values())=={1:20,2:8,4:8,28:4}
print('PASS_R5_F8_INDEPENDENT_ENDPOINTS',len(rows),'LABELS',len(found),'CLASSES')
