#!/usr/bin/env python3
"""Check the published EC49FNL supplement's complete finite certificate.

This checker is stdlib-only. The full original-word/native-C++ and independent
Python source files and their FINISHED logs reside in the companion full archive.
It verifies the compressed 220-row vector and all 2916 four-root allocations
for each profile, including the exact sharp second best and key-swap contrast.
"""
from pathlib import Path
from itertools import product
import base64
import hashlib
import json
import zlib

D = Path(__file__).resolve().parent
raw = zlib.decompress(base64.b64decode(
    (D / "COMPACT_EVIDENCE_EC49FNL.b64").read_text().strip(), validate=True))
assert hashlib.sha256(raw).hexdigest() == (
    "2bae5c339f2174b1336c2c38b69402033a5860d4bf4d9d10c1dcf0a573db4156")
bundle = json.loads(raw)
rows = bundle["rows"]
assert len(rows) == 220
assert [row[0] for row in rows] == list(range(30500, 30720))
assert all(type(cost) is int and cost > 0 for _, cost, _ in rows)
assert min(row[1] for row in rows) == 96
assert [idx for idx, val, _ in rows if val == 96] == [30709, 30711]
assert max(row[1] for row in rows) == 206
assert [idx for idx, val, _ in rows if val == 206] == [30697]

Q = [5, 7, 11, 13, 15, 17, 19, 21]
P = [11, 13, 15, 17, 19, 21]
assert set(P) < set(Q)
profs = {}
all_costs = []
for case in ("30709", "30711"):
    words = bundle["witnesses"][case]
    assert len(words) == 24 and len({tuple(x[0]) for x in words}) == 24
    keys = {tuple(x[2]) for x in words}
    assert len(keys) <= 7
    raw_roots = bundle["root_tables"][case]
    assert set(raw_roots) == {"3", "5", "6", "7"}
    roots = {int(r): (v["labels"], v["costs"]) for r, v in raw_roots.items()}
    assert roots[3][0] == P and roots[7][0] == Q
    assert len(roots[5][0]) == len(roots[6][0]) == 12
    assert set(roots[5][0]).isdisjoint(roots[6][0])
    assert set(roots[5][0]) | set(roots[6][0]) == set(range(24))
    for r, (labels, vals) in roots.items():
        assert len(vals) == 1 << len(labels)
        assert vals[0] == 0
        assert all(type(x) is int and x >= 0 for x in vals)
    pos = {r: {lab: i for i, lab in enumerate(roots[r][0])} for r in roots}
    base = {lab: (5 if lab in pos[5] else 6) for lab in range(24)}
    opts = [[base[l], 7] + ([3] if l in pos[3] else []) for l in Q]
    assert 1 == len([[]]) and 3 ** 6 * 2 ** 2 == 2916
    baseline = roots[5][1][-1] + roots[6][1][-1]
    assert baseline == 96
    scores = []
    sharp = []
    best_nonbaseline = 10 ** 9
    from collections import Counter
    hist = Counter()
    for alpha in product(*opts):
        by_label = dict(zip(Q, alpha))
        masks = {r: 0 for r in roots}
        changed = False
        for lab in range(24):
            dest = by_label.get(lab, base[lab])
            masks[dest] |= 1 << pos[dest][lab]
            if dest != base[lab]:
                changed = True
        value = sum(roots[r][1][mask] for r, mask in masks.items())
        gap = value - baseline
        assert gap >= 0
        scores.append(value)
        hist[gap] += 1
        if changed:
            if gap < best_nonbaseline:
                best_nonbaseline, sharp = gap, [alpha]
            elif gap == best_nonbaseline:
                sharp.append(alpha)
        else:
            assert value == baseline
    assert len(scores) == 2916
    assert best_nonbaseline == 8 and len(sharp) == 3
    assert scores.count(96) == 1
    assert hist == {int(k): v for k, v in
                    bundle["assignment"][case]["histogram"].items()}
    assert bundle["assignment"][case]["number_assignments"] == 2916
    assert bundle["assignment"][case]["minimum_count"] == 3
    assert bundle["assignment"][case]["nonbaseline_min"] == 8
    assert bundle["assignment"][case]["baseline"] == 96
    all_costs.append(scores)
    profs[case] = (baseline, best_nonbaseline, len(sharp))
    print("PASS", case, "baseline=96", "sharp_gap=8",
          "allocations=2916", "sharp_alternatives=3")

low = sum(x < y for x, y in zip(*all_costs))
tie = sum(x == y for x, y in zip(*all_costs))
high = sum(x > y for x, y in zip(*all_costs))
assert (low, tie, high) == (137, 1602, 1177)
assert max(abs(x-y) for x, y in zip(*all_costs)) == 3
print("PASS finite interval=220, double case optimum=96,"
      " all four-root assignment costs and exact landscape contrast")
