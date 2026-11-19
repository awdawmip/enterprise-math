#!/usr/bin/env python3
"""Independently reconstruct W's seven priced maximal joint response support families."""
from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
src=(p/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(src).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(src)
tau=int(json.loads((p/"stages_18.json").read_text())["U"])-1
W=(0,16,32,48,1,64,17,80,18,24,34,82)
best={}
for k in range(214,315):
 x=[int(data["counts_and_cohorts"][str(k)]["counts"][i]) for i in W]
 endpoints=[2*v-tau for v in x]
 masks={sum(1<<j for j,v in enumerate(x) if abs(2*v-y)<=tau) for y in endpoints}
 family=tuple(sorted(m for m in masks if not any(m!=n and (m&n)==m for n in masks)))
 if family==(4095,):continue
 best[family]=min(k,best.get(family,k))
actual=[f"{k} {len(fam)} "+" ".join(map(str,fam)) for fam,k in sorted(best.items(),key=lambda x:x[1])]
reference=[s for s in (p/"W_ENDPOINT_FAMILIES.txt").read_text().splitlines() if s and not s.startswith("#")]
assert actual==reference,(actual,reference)
assert len(actual)==7
print("PASS_W_ENDPOINT_RECONSTRUCTION",len(actual),"actions",len(W),"labels",len(range(214,315)),"prices")
