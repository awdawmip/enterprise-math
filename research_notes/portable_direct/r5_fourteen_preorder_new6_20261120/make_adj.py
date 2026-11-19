#!/usr/bin/env python3
"""Recreate exact 101x256x256 directed center-window adjacency from frozen R5 input."""
from pathlib import Path
import json,hashlib
root=Path(__file__).parent
raw=(root/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
j=json.loads(raw)
tau=int(json.loads((root/"stages_18.json").read_text())["U"])-1
assert tau==58182461585441404127941754879
equal_tau=0
with (root/"window_adj.bin").open("wb") as f:
 for k in range(214,315):
  a=list(map(int,j["counts_and_cohorts"][str(k)]["counts"]))
  assert len(a)==256
  for x in a:
   equal_tau+=sum(y-x==tau for y in a)
   f.write(bytes(0<=y-x<=tau for y in a))
assert equal_tau==0
assert (root/"window_adj.bin").stat().st_size==101*256*256
print("PASS_R5_FROZEN_ADJ",101*256*256,"CENTER_DIFF_EQUALS_TAU",equal_tau)
