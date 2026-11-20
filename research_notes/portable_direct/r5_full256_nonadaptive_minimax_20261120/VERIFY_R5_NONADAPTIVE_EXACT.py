#!/usr/bin/env python3
"""Exact finite certificate for the full-256 R5 nonadaptive minimax theorem.

Run with unchanged EXACT_R5_ALL_101_BUDGETS.json and stages_18.json
from the frozen R5 scientific evidence bundle. Standard library only.
The accompanying RESEARCH.md proves the symbolic all-f conclusion.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent
source = root / "EXACT_R5_ALL_101_BUDGETS.json"
stages = root / "stages_18.json"
expected_hash = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
assert hashlib.sha256(source.read_bytes()).hexdigest() == expected_hash
data = json.loads(source.read_text())
stage = json.loads(stages.read_text())
assert stage["frozen_sha256"] == expected_hash
tau = int(stage["U"]) - 1
assert tau == 58182461585441404127941754879
K = tuple(range(214, 315))
N = [[int(x) for x in data["counts_and_cohorts"][str(k)]["counts"]] for k in K]
assert len(N) == 101 and all(len(row) == 256 for row in N)

# For closed correctness intervals, disjointness is strict center gap > tau.
separators = {}
for h in range(256):
    for j in range(h + 1, 256):
        pattern = sum(1 << q for q in range(101) if abs(N[q][h] - N[q][j]) > tau)
        separators.setdefault(pattern, []).append((h, j))
assert sum(map(len, separators.values())) == 32640
assert 0 not in separators
minimal = []
for p in sorted(separators, key=lambda t: (t.bit_count(), t)):
    if not any((p & q) == q for q in minimal):
        minimal.append(p)

def mask(*prices):
    return sum(1 << (k-214) for k in prices)

A = [
    mask(*range(214, 219)),
    mask(214, *range(216, 222)),
    mask(*range(215, 222)),
    mask(*range(223, 291)),
    mask(*range(296, 313)),
]
assert len(separators) == 53 and set(minimal) == set(A)
assert all(any((p & q) == q for q in A) for p in separators)
witnesses = [(9, 12), (1, 2), (2, 8), (0, 64), (16, 32)]
for p, pair in zip(A, witnesses):
    assert pair in separators[p]

weights = [72, 72, 72, 223, 296]
for k in K:
    price_load = sum(w for p,w in zip(A,weights) if p & (1 << (k-214)))
    assert price_load <= k, (k, price_load)
assert sum(weights) == 735
triple = (216, 223, 296)
assert sum(triple) == 735 and all(any(p & (1 << (k-214)) for k in triple) for p in A)
freq = Counter()
for p, pairs in separators.items():
    hits = sum(bool(p & (1 << (k-214))) for k in triple)
    freq[hits] += len(pairs)
assert freq == Counter({1:2448, 2:12192, 3:18000})

# If each physical budget can be used at most once, exhaustive small-prefix
# enumeration and exact greedy disjoint middle/late action sets are sufficient.
distinct = {}
early_sets = [set(range(214, 219)),
              {214, 216, 217, 218, 219, 220, 221},
              set(range(215, 222))]
for f in range(4):
    m = 2*f + 1
    if m > 5:
        distinct[f] = None
        continue
    candidates = []
    for bits in range(1 << 8):
        subset = [k for k in range(214, 222) if (bits >> (k-214)) & 1]
        if all(sum(k in pat for k in subset) >= m for pat in early_sets):
            candidates.append((sum(subset), subset))
    low_cost, low = min(candidates)
    distinct[f] = (low_cost + sum(range(223, 223+m)) + sum(range(296, 296+m)),
                   low + list(range(223, 223+m)) + list(range(296, 296+m)))
assert [distinct[i][0] for i in (0, 1, 2)] == [735, 2214, 3914]
assert distinct[3] is None

print("PASS: SHA256, 32640 pairs, 53 separation types, five minimal witnesses")
print("PASS: 101 dual price inequalities and three-query upper certificate")
print("PASS: exact nonadaptive C_f=735*(2*f+1), all integer f>=0 (symbolic proof in RESEARCH.md)")
print("PASS: distinct-query f=0,1,2 minima 735,2214,3914; f>=3 impossible")
print("triple separation histogram:",dict(sorted(freq.items())))
print("distinct optimal query sets:",distinct)
