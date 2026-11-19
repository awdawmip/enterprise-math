#!/usr/bin/env python3
"""Rebuild exact 101 x 256 x 256 R5 scalar left-endpoint window adjacency.
Requires byte-pinned EXACT_R5_ALL_101_BUDGETS.json in the working directory.
"""
import json, hashlib
from pathlib import Path
p=Path("EXACT_R5_ALL_101_BUDGETS.json")
raw=p.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(raw)
tau=58182461585441404127941754879
with open("window_adj.bin","wb") as out:
    for k in range(214,315):
        ns=list(map(int,data["counts_and_cohorts"][str(k)]["counts"]))
        assert len(ns)==256
        for x in ns:
            out.write(bytes(0<=y-x<=tau for y in ns))
assert Path("window_adj.bin").stat().st_size==101*256*256
assert hashlib.sha256(Path("window_adj.bin").read_bytes()).hexdigest()=="daad32bc5c4f1a11361f1389c0e95d2de349a4870f7c240179f44d02d2d282af"
print("PASS_EXACT_WINDOW_ADJ",101*256*256)
