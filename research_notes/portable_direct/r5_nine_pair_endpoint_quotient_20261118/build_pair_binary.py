#!/usr/bin/env python3
"""Create exact 256x256 forward reachability matrices for the fifth noise interval."""
import hashlib
import json
from pathlib import Path

PIN_SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L = 25845652773852463277015040000
U = 58182461585441404127941754880

raw = Path("EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest() == PIN_SHA
counts = json.loads(raw)["counts_and_cohorts"]
assert len(counts) == 101
for name, tau in (("L", L), ("U", U - 1)):
    data = bytearray()
    for k in range(214, 315):
        centers = [int(z) for z in counts[str(k)]["counts"]]
        assert len(centers) == 256
        for a in centers:
            data.extend(1 if a <= b <= a + tau else 0 for b in centers)
    path = Path(f"R5_PAIR_FORWARD_{name}.bin")
    path.write_bytes(data)
    print(name, len(data), hashlib.sha256(data).hexdigest())
