#!/usr/bin/env python3
"""Generate exact 101 x 256 x 256 ordered endpoint adjacency from frozen centers.
The characteristic bit at (i,j) is 0 <= N_j - N_i <= tau.
"""
from pathlib import Path
import json, hashlib
p=Path(__file__).parent
raw=(p/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(raw)
tau=int(json.loads((p/"stages_18.json").read_text())["U"])-1
assert tau==58182461585441404127941754879
with (p/"window_adj.bin").open("wb") as out:
 for k in range(214,315):
  a=list(map(int,data["counts_and_cohorts"][str(k)]["counts"]))
  assert len(a)==256
  for x in a:out.write(bytes(0<=y-x<=tau for y in a))
assert (p/"window_adj.bin").stat().st_size==101*256*256
print("EXACT_ADJ_OK",101*256*256)
