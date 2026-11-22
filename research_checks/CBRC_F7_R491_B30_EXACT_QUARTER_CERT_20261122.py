#!/usr/bin/env python3
"""F7 r491: exact B30 minimax certificate, exhaustive original 61^4 inputs.

Run: python research_checks/CBRC_F7_R491_B30_EXACT_QUARTER_CERT_20261122.py
The fixed quarter-grid witness is independent of LP search execution.
"""
from collections import Counter
from pathlib import Path
import base64
import hashlib
import itertools
import zlib

B = 30
FILENAME = "F7_R491_B30_Exact_Quarter_Witness_20261122.b85"
RAW_SHA256 = "7a49938391a054b9f022d29063d8a10344ef92ca1d3f9667d29aba3b33092e3f"
EXPECTED = {-2: 288904, -1: 2898222, 0: 6685565, 1: 3512054, 2: 461096}

def indexed_keys():
    R = list(range(-2*B, 2*B+1))
    T = {r: range(2*r - min(B, r+B), 2*r - max(-B, r-B) + 1) for r in R}
    index = {}
    for i, r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r], T[u]):
                for rr in (r, u):
                    x, y = 2*rr-v, rr-v
                    k = (abs(x), y)
                    if y and k not in ((2, 1), (1, -1)) and k not in index:
                        index[k] = len(index)
    return index

def main():
    path = Path(__file__).resolve().parent.parent / "research_artifacts" / FILENAME
    raw = zlib.decompress(base64.b85decode(path.read_text(encoding="utf8").strip()))
    assert hashlib.sha256(raw).hexdigest() == RAW_SHA256
    index = indexed_keys()
    assert len(index) == len(raw) == 18688
    assert Counter(raw) == {2: 11844, 3: 5519, 4: 1325}

    def Q(x, y):
        if y == 0:
            return 0 if x == 0 else 4
        k = (abs(x), y)
        if k in ((2, 1), (1, -1)):
            return 2
        return raw[index[k]] if k in index else 2

    assert Q(0, 0) == 0 and Q(2, 1) == Q(-1, -1) == 2
    histogram = Counter()
    for a, b, c, d in itertools.product(range(-B, B+1), repeat=4):
        k = a - 2*b - c + 2*d
        D4 = Q(a+k, b+k) + Q(c-k, d-k) - Q(a, b) - Q(c, d)
        assert abs(D4) <= 2, (a,b,c,d,k,D4)
        histogram[D4] += 1
    assert dict(histogram) == EXPECTED
    assert sum(histogram.values()) == 61**4 == 13845841
    assert max(map(abs, histogram)) == 2
    print("CERTIFIED F7 finite e_B=1/2 for all integers 1<=B<=30")
    print("original-input count", sum(histogram.values()))
    print("indexed free coordinates", len(index))
    print("histogram", dict(sorted(histogram.items())))
    print("raw SHA256", RAW_SHA256)

if __name__ == "__main__":
    main()
