#!/usr/bin/env python3
"""Build independent joint response families from exact doubled left endpoints.
Usage: python3 MAKE_INDEPENDENT_ACTIONS.py 2 130 144
"""
from pathlib import Path
import json,hashlib,sys
root=Path(__file__).parent
raw=(root/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(raw)
tau=int(json.loads((root/"stages_18.json").read_text())["U"])-1
assert tau==58182461585441404127941754879
C={k:tuple(map(int,data["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)}
W=(0,16,32,48,1,64,17,80,18,24,34,82)
for t in map(int,sys.argv[1:]):
 assert t not in W and 0<=t<256
 ids=W+(t,);priced={}
 for k,whole in C.items():
  centers=[whole[i] for i in ids]
  masks=set()
  for x in centers:
   y=2*x-tau
   masks.add(sum(1<<j for j,z in enumerate(centers) if abs(2*z-y)<=tau))
  fam=tuple(sorted(mask for mask in masks if not any(mask!=n and (mask&n)==mask for n in masks)))
  if fam!=(8191,):priced[fam]=min(k,priced.get(fam,k))
 actions=sorted((k,fam) for fam,k in priced.items())
 dest=root/f"ACTIONS_T{t}.txt"
 dest.write_text(f"13 {len(actions)}\n"+"".join(f"{k} {len(ms)} "+" ".join(map(str,ms))+"\n" for k,ms in actions))
 print("ACTIONS_READY",t,len(actions),hashlib.sha256(dest.read_bytes()).hexdigest())
