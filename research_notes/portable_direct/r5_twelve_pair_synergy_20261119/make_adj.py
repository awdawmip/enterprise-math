#!/usr/bin/env python3
# Exact binary window adjacency: 101 query prices × 256 sources × 256 targets.
# Scientific input SHA256 pinned below. Integer operations only.
import json, hashlib
from pathlib import Path
root=Path(__file__).resolve().parent
src=(root/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(src).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(src)
tau=int(json.loads((root/'stages_18.json').read_text())['U'])-1
with (root/'window_adj.bin').open('wb') as out:
 for k in range(214,315):
  a=list(map(int,data['counts_and_cohorts'][str(k)]['counts']))
  assert len(a)==256
  for x in a: out.write(bytes(0<=y-x<=tau for y in a))
assert (root/'window_adj.bin').stat().st_size==101*256*256
print("EXACT_ADJ_READY",101*256*256)
