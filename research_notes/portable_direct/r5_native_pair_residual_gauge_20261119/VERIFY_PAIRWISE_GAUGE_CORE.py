#!/usr/bin/env python3
"""Standalone exact core verifier for R5 native pairwise separation and error gauge.
Run with unchanged frozen EXACT_R5_ALL_101_BUDGETS.json and stages_18.json
in the same folder. A fuller independent Bellman cross-check is in the linked
local reproducibility archive.
"""
import collections
import hashlib
import itertools
import json
from pathlib import Path

P = Path(__file__).resolve().parent
SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
raw = (P / "EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest() == SHA
data = json.loads(raw)["counts_and_cohorts"]
C = {k: tuple(map(int, data[str(k)]["counts"])) for k in range(214, 315)}
assert len(C) == 101 and all(len(row) == 256 for row in C.values())
meta = json.loads((P / "stages_18.json").read_text())
assert meta["frozen_sha256"] == SHA
L, U = int(meta["L"]), int(meta["U"])
T = list(map(int, meta["stage_taus"]))
critical = sorted({
    abs(row[h] - row[g])
    for row in C.values()
    for h in range(256)
    for g in range(h+1, 256)
    if L < abs(row[h] - row[g]) < U
})
assert T == [L] + critical and len(critical) == 17
pairs = list(itertools.combinations(range(256), 2))
assert len(pairs) == 32640

def max_supports(row, tau):
    masks = set()
    for left in set(row):
        m = 0
        for h, val in enumerate(row):
            if left <= val <= left + tau:
                m |= (1 << h)
        masks.add(m)
    return tuple(sorted(
        (m for m in masks if not any(m != q and (m & q) == m for q in masks)),
        key=lambda x: (x.bit_count(), x)
    ))

histograms = []
for i, tau in enumerate(T):
    hist = collections.Counter()
    for h, g in pairs:
        kappa = next((k for k in range(214,315)
                      if abs(C[k][h] - C[k][g]) > tau), None)
        assert kappa is not None
        hist[kappa] += 1
    assert sum(hist.values()) == len(pairs)
    assert set(hist).issubset({214, 215, 223, 294, 295, 296})
    histograms.append(hist)

upper = U - 1
hist = collections.Counter()
for h, g in pairs:
    kappa = next((k for k in range(214,315)
                  if abs(C[k][h]-C[k][g]) > upper), None)
    assert kappa is not None
    hist[kappa] += 1
assert hist == {214:30528, 215:1216, 223:512, 295:320, 296:64}
assert max(hist) == 296
core = (214,215,216,217,223,295,296)
F = {k:max_supports(C[k],upper) for k in core}
# Independent interval-response criterion, 228480 named pair/action cases.
for k in core:
    for h,g in pairs:
        together = any(((m>>h)&1) and ((m>>g)&1) for m in F[k])
        assert together == (abs(C[k][h]-C[k][g]) <= upper)

witnesses = {}
for k in (216,217):
    for j in range(214,k):
        found = next((s for s in F[j]
                      if all((s & q) != s for q in F[k])), None)
        assert found is not None, (j,k)
        witnesses[(j,k)] = tuple(h for h in range(256) if found>>h&1)
assert len(witnesses) == 5

# Verify the exact transformation from full capped counters to relative gauge.
def gauge(e,f):
    m = min(e)
    if m > f:
        return None
    R = f-m
    return R,tuple(min(R+1,x-m) for x in e)

def gauge_update(s,mask):
    R,d = s
    v = [x+(0 if mask>>h&1 else 1) for h,x in enumerate(d)]
    delta = min(v)
    if delta > R:
        return None
    return R-delta,tuple(min(R-delta+1,x-delta) for x in v)

checked = 0
for n in range(2,5):
    for f in range(4):
        for e in itertools.product(range(f+2),repeat=n):
            s = gauge(e,f)
            if s is None:continue
            for mask in range(1<<n):
                next_e=tuple(min(f+1,x+(0 if mask>>h&1 else 1))
                             for h,x in enumerate(e))
                assert gauge(next_e,f) == gauge_update(s,mask)
                checked += 1
assert checked == 17544

# A closed-form two-state recurrence is independent of center-table enumeration.
from functools import lru_cache
@lru_cache(None)
def two(r,s,cost):
    if r<0 or s<0:return 0
    return cost + max(two(r-1,s,cost),two(r,s-1,cost))
for cost in (214,215,223,294,295,296):
    for r in range(9):
        for s in range(9):
            assert two(r,s,cost) == (r+s+1)*cost

print("PASS_R5_NATIVE_PAIR_GAUGE_CORE",
      len(T),len(pairs),"f8_pair_lower",17*max(hist),
      "gauge_checks",checked,"joint_witnesses",len(witnesses))
