#!/usr/bin/env python3
"""Independent left-endpoint action construction for a 14-label R5 pair."""
from pathlib import Path
import json,hashlib,sys
root=Path(__file__).parent
if len(sys.argv)!=3: raise SystemExit("usage: python BUILD_ORACLE_14_ACTIONS.py u v")
u,v=map(int,sys.argv[1:3])
W=[0,16,32,48,1,64,17,80,18,24,34,82]
H=W+[u,v]
assert len(H)==14 and len(set(H))==14
raw=(root/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(raw)
tau=int(json.loads((root/"stages_18.json").read_text())["U"])-1
classes={}
for k in range(214,315):
 c=[int(data["counts_and_cohorts"][str(k)]["counts"][i]) for i in H]
 endpoints=[2*x-tau for x in c]
 masks={sum(1<<j for j,y in enumerate(c) if abs(2*y-e)<=tau) for e in endpoints}
 top=tuple(sorted(s for s in masks if not any(s!=m and s&m==s for m in masks)))
 if top==(16383,):continue
 classes[top]=min(k,classes.get(top,k))
actions=sorted((price,masks) for masks,price in classes.items())
fn=root/f"ORACLE_14_ACTIONS_U{u}_V{v}.txt"
with fn.open("w") as f:
 print(14,len(actions),file=f)
 for price,masks in actions:print(price,len(masks),*masks,file=f)
print(u,v,len(actions),hashlib.sha256(fn.read_bytes()).hexdigest())
