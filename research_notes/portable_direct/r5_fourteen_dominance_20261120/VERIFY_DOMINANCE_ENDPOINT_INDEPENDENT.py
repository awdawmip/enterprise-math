#!/usr/bin/env python3
"""Independent exact doubled-endpoint vs recorded priced support dominance on 82 classes."""
from pathlib import Path
import csv,json,hashlib,random
root=Path(__file__).parent
raw=(root/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(raw)
tau=int(json.loads((root/"stages_18.json").read_text())["U"])-1
centers={k:tuple(map(int,data["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)}
W=(0,16,32,48,1,64,17,80,18,24,34,82)
reps={int(r["class"]):(int(r["u"]),int(r["v"])) for r in csv.DictReader(open(root/"R5_14_CLASS_REPS.csv"))}
rows=list(csv.DictReader(open(root/"R5_F8_DOMINANCE_COVERAGE_22.csv")))
bench=[int(r["class"]) for r in csv.DictReader(open(root/"BENCHMARKS_22.csv"))]
assert len(reps)==len(rows)==1906 and len(bench)==22
def actions(i):
 h=W+reps[i];minimal={}
 for k in centers:
  x=[centers[k][name] for name in h]
  eps=[2*v-tau for v in x]
  m={sum(1<<j for j,y in enumerate(x) if abs(2*y-e)<=tau) for e in eps}
  mx=tuple(sorted(s for s in m if not any(s!=t and (s&t)==s for t in m)))
  if mx==(16383,):continue
  minimal[mx]=min(k,minimal.get(mx,k))
 return [(price,m) for m,price in minimal.items()]
def swap(m):
 return (m&~(3<<12))|((m&(1<<12))<<1)|((m&(1<<13))>>1)
def dominant(A,B):
 return all(any(ca<=cb and all(any((ma&mb)==ma for mb in masks_b) for ma in masks_a)
                for ca,masks_a in A) for cb,masks_b in B)
R=random.Random(20261120)
covered=[int(r["class"]) for r in rows if int(r["certified"])]
uncovered=[int(r["class"]) for r in rows if not int(r["certified"])]
selected=sorted(set(bench+R.sample(covered,35)+R.sample(uncovered,25)))
refs={b:actions(b) for b in bench}
for i in selected:
 A=actions(i)
 expected=bool(int(rows[i]["certified"]))
 observed=any(dominant(A,refs[b]) or dominant(A,[(cost,tuple(swap(x) for x in masks)) for cost,masks in refs[b]]) for b in bench)
 assert observed==expected,(i,expected,observed)
print("PASS_INDEPENDENT_14_DOMINANCE_ENDPOINT",len(selected),"classes",sum(int(rows[i]["certified"]) for i in selected),"covered")
