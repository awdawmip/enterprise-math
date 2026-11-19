#!/usr/bin/env python3
import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parent
src=(root/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(src).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
data=json.loads(src)
tau=int(json.loads((root/'stages_18.json').read_text())['U'])-1
with (root/'window_adj.bin').open('wb') as f:
 for k in range(214,315):
  vals=list(map(int,data['counts_and_cohorts'][str(k)]['counts']))
  assert len(vals)==256
  for a in vals:
   f.write(bytes(0<=b-a<=tau for b in vals))
assert (root/'window_adj.bin').stat().st_size==101*256*256
print('ADJ prepared',101*256*256)
