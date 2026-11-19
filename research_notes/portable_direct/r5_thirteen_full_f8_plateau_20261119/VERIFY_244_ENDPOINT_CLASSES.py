#!/usr/bin/env python3
"""Independent integer-left-endpoint reconstruction for all 244 label classes.
Inputs: frozen source JSON and stages_18.json supplied by the reproducible archive.
Does not trust solver's precomputed binary adjacency or Bellman values.
"""
import csv,json,hashlib,collections
from pathlib import Path
root=Path(__file__).parent
raw=(root/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
j=json.loads(raw)
tau=int(json.loads((root/"stages_18.json").read_text())["U"])-1
W=(0,16,32,48,1,64,17,80,18,24,34,82)
C={k:list(map(int,j["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)}
evidence=list(csv.DictReader((root/"R5_F7F8_CLASSES.csv").open()))
assert len(evidence)==48
first={}; hist=collections.Counter(); mapping=[]
for t in range(256):
 if t in W:continue
 h=W+(t,); priced={}
 for k,all_centers in C.items():
  centers=[all_centers[i] for i in h]
  masks=set()
  for x in centers:
   y=2*x-tau
   masks.add(sum((1<<b) for b,z in enumerate(centers) if abs(2*z-y)<=tau))
  maximal=tuple(sorted(m for m in masks if not any(m!=n and (m&n)==m for n in masks)))
  if maximal==(8191,):continue
  priced[maximal]=min(k,priced.get(maximal,k))
 signature=tuple(sorted((k,fam) for fam,k in priced.items()))
 index=first.setdefault(signature,len(first))
 row=evidence[index]
 assert index==int(row["class"])
 if t==int(row["representative_t"]):assert hist[index]==0
 assert int(row["f7_value"])==7385 and int(row["f8_value"])==8335
 mapping.append((t,index))
 hist[index]+=1
assert len(mapping)==244 and len(first)==48
assert all(hist[i]==int(row["member_count"]) for i,row in enumerate(evidence))
assert all(next(t for t,c in mapping if c==i)==int(row["representative_t"]) for i,row in enumerate(evidence))
with (root/"R5_F7F8_244_LABEL_CLASSES.csv").open("w") as out:
 out.write("t,class,f7,f8\n")
 for t,c in mapping:out.write(f"{t},{c},7385,8335\n")
print("PASS_244_CLASSES",len(mapping),len(first))
