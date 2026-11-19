#!/usr/bin/env python3
import json, hashlib
from pathlib import Path

root = Path(__file__).parent
raw = (root / "EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest() == "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
j = json.loads(raw)
stages = json.loads((root / "stages_18.json").read_text())
tau = int(stages["U"]) - 1
assert tau == 58182461585441404127941754879
with (root / "window_adj.bin").open("wb") as f:
    for k in range(214, 315):
        counts = [int(v) for v in j["counts_and_cohorts"][str(k)]["counts"]]
        assert len(counts) == 256
        for x in counts:
            f.write(bytes(0 <= y - x <= tau for y in counts))
assert (root / "window_adj.bin").stat().st_size == 101 * 256 * 256
print("WINDOW_ADJ_READY 6619136")
