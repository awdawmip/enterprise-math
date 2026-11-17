#!/usr/bin/env python3
"""Regenerate exact maximal readout-support families from pinned R5 center counts."""
import hashlib
import json
import sys
from pathlib import Path

H = (18,24,82,34,17,0,1,2,3,144,208,255,50,66,4,5)
K = (214,215,216,223,296)
TAU = 58182461585441404127941754879
EXPECTED = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"

def maximal_supports(centers):
    blocks = {}
    for i, v in enumerate(centers):
        blocks[v] = blocks.get(v, 0) | (1 << i)
    raw = {
        sum(mask for c, mask in blocks.items() if lo <= c <= lo + TAU)
        for lo in blocks
    }
    return tuple(sorted(s for s in raw if not any(s != t and s & t == s for t in raw)))

def main():
    base = Path(__file__).resolve().parent
    src = Path(sys.argv[1]) if len(sys.argv) == 2 else base / "EXACT_R5_ALL_101_BUDGETS.json"
    raw = src.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED
    table = json.loads(raw)["counts_and_cohorts"]
    assert set(str(k) for k in range(214,315)).issubset(table)
    rows = [f"{len(H)} {len(K)}"]
    for k in K:
        counts = table[str(k)]["counts"]
        assert len(counts) == 256
        supports = maximal_supports([int(counts[h]) for h in H])
        rows.append(f"{k} {len(supports)} " + " ".join(map(str, supports)))
    text = "\n".join(rows) + "\n"
    expected_actions = base / "ACTIONS_H16_PLUS_5.txt"
    assert text == expected_actions.read_text()
    print("PASS_R5_H16_MAXIMAL_SUPPORTS_FROZEN_COUNTS")

if __name__ == "__main__":
    main()
