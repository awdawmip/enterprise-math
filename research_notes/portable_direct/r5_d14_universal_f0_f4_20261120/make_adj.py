#!/usr/bin/env python3
# Rebuild exact ordered endpoint-incidence windows from the frozen R5 input.
import json,hashlib
from pathlib import Path
r=Path(__file__).parent
raw=(r/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
j=json.loads(raw)
tau=int(json.loads((r/"stages_18.json").read_text())["U"])-1
with (r/"window_adj.bin").open("wb") as f:
 for k in range(214,315):
  a=list(map(int,j["counts_and_cohorts"][str(k)]["counts"]))
  assert len(a)==256
  for x in a:
   f.write(bytes(0<=y-x<=tau for y in a))
assert (r/"window_adj.bin").stat().st_size==101*256*256
print("VERIFIED_ENDPOINT_ADJ",101*256*256)
