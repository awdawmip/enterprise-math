#!/usr/bin/env python3
"""F7 r492 exact necessary-repair certificate for the fixed B30 q at B31.

Rebuilds r491's B30 q on all integer coordinates; checks 171 B31 inputs with
pairwise disjoint free evenness-orbit supports. Works for arbitrary real q'.
Run from any directory using Python standard library only.
"""
import base64
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import zlib

ROOT = Path(__file__).resolve().parent.parent
B0 = 30
RAW_SHA = "7a49938391a054b9f022d29063d8a10344ef92ca1d3f9667d29aba3b33092e3f"
FIXED = {(2, 1), (1, -1)}

def old_index():
    R = list(range(-2*B0, 2*B0+1))
    T = {r: range(2*r-min(B0,r+B0), 2*r-max(-B0,r-B0)+1) for r in R}
    out = {}
    for i, r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r], T[u]):
                for rr in (r, u):
                    key = (abs(2*rr-v), rr-v)
                    if key[1] and key not in FIXED and key not in out:
                        out[key] = len(out)
    return out

def main():
    path = ROOT / "research_artifacts/F7_R491_B30_Exact_Quarter_Witness_20261122.b85"
    raw = zlib.decompress(base64.b85decode(path.read_text().strip()))
    assert len(raw) == 18688 and hashlib.sha256(raw).hexdigest() == RAW_SHA
    assert Counter(raw) == {2:11844, 3:5519, 4:1325}
    index = old_index()
    assert len(index) == len(raw)

    def Q(x, y):
        if y == 0:
            return 0 if x == 0 else 4
        key = (abs(x), y)
        return 2 if key in FIXED or key not in index else raw[index[key]]

    cert = ROOT / "research_artifacts/F7_R492_B31_171_Disjoint_Violation_Quadruples_20261122.json"
    rows = json.loads(cert.read_text())
    assert len(rows) == 171 and len({tuple(row) for row in rows}) == 171
    used = set()
    counts = Counter()
    weight_total = 0
    for quad in rows:
        assert len(quad) == 4 and all(type(z) is int and -31 <= z <= 31 for z in quad)
        a,b,c,d = quad
        k = a-2*b-c+2*d
        terms = [(a+k,b+k,1),(c-k,d-k,1),(a,b,-1),(c,d,-1)]
        d4 = sum(sign*Q(x,y) for x,y,sign in terms)
        assert abs(d4) in (3,4), (quad,d4)
        coeffs = Counter()
        for x,y,sign in terms:
            key = (abs(x),y)
            if y != 0 and key not in FIXED:
                coeffs[key] += sign
        coeffs = {key:coef for key,coef in coeffs.items() if coef}
        assert coeffs and all(abs(coef)==1 for coef in coeffs.values())
        assert used.isdisjoint(coeffs), quad
        used.update(coeffs)
        weight = abs(d4)-2
        counts[weight] += 1
        weight_total += weight
    assert counts == {1:154,2:17}, counts
    assert len(used) == 436 and weight_total == 188
    print("F7 r492 CERTIFIED: 171 disjoint B31 violations; 436 distinct free orbit keys")
    print("weights: 154*1 + 17*2 = 188 quarter-units")
    print("Any B31 half-error q' modifies >=171 orbit variables vs r491 q30")
    print("sum of abs(q'-q30) on certified keys >= 47")

if __name__ == "__main__":
    main()
