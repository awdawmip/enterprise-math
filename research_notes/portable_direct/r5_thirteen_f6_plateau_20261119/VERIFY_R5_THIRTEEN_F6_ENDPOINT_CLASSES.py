#!/usr/bin/env python3
"""Independent R5 13-label 244-way exact interval support and CSV check.
Reconstructs from frozen integer centers, not C++ binary adjacency.
Does not independently recompute f>=1 Bellman DP.
"""
import hashlib,json,csv,collections
from pathlib import Path
r=Path(__file__).parent
raw=(r/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
obj=json.loads(raw)
tau=int(json.loads((r/"stages_18.json").read_text())["U"])-1
centers={k:tuple(map(int,obj["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)}
W=(0,16,32,48,1,64,17,80,18,24,34,82)
rows=list(csv.DictReader((r/"R5_THIRTEEN_F0_F6_ALL244.csv").open()))
assert len(rows)==244
classes={}
for row in rows:
 t=int(row["t"]);h=W+(t,)
 assert t not in W
 priced={}
 for k,cc in centers.items():
  a=[cc[i] for i in h]
  masks={sum(1<<j for j,w in enumerate(a) if abs(2*w-(2*v-tau))<=tau) for v in a}
  fam=tuple(sorted(m for m in masks if not any(m!=v and (m&v)==m for v in masks)))
  if fam==(8191,):continue
  priced[fam]=min(k,priced.get(fam,k))
 signature=tuple(sorted((cost,fam) for fam,cost in priced.items()))
 clazz=classes.setdefault(signature,len(classes))
 assert clazz==int(row["class"]), (t,clazz,row["class"])
 assert tuple(int(row["f"+str(i)]) for i in range(7))==(735,1685,2635,3585,4535,5485,6435)
assert len(classes)==48
hist=collections.Counter()
for s,cls in classes.items():
 hist[cls]=sum(1 for t in rows if int(t["class"])==cls)
assert dict(collections.Counter(hist.values()))=={1:20,2:8,4:8,8:8,28:4}
print("PASS_R5_THIRTEEN_244_INDEPENDENT_ENDPOINT_SIGNATURES",len(rows),len(classes))
