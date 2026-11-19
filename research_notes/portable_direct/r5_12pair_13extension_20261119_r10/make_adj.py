#!/usr/bin/env python3
"""Build frozen 101 x 256 x 256 exact interval-left-endpoint adjacency.
Input JSON and stages_18.json are included in the matching local ZIP bundle.
"""
import json,hashlib
from pathlib import Path
root=Path(__file__).parent
raw=(root/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
j=json.loads(raw)
tau=int(json.loads((root/"stages_18.json").read_text())["U"])-1
with (root/"window_adj.bin").open("wb") as out:
    for k in range(214,315):
        centers=list(map(int,j["counts_and_cohorts"][str(k)]["counts"]))
        assert len(centers)==256
        for x in centers:
            out.write(bytes(0<=y-x<=tau for y in centers))
assert (root/"window_adj.bin").stat().st_size==101*256*256
print("ADJ_EXACT_READY",101*256*256)
