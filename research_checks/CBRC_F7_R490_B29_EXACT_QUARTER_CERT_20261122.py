#!/usr/bin/env python3
"""F7 r490: exact original-input audit for the fixed B29 quarter-grid witness.

Run from the Enterprise Math checkout:
    python research_checks/CBRC_F7_R490_B29_EXACT_QUARTER_CERT_20261122.py

The fixed certificate is independent of the LP search. All residual tests use
integer arithmetic on the original four-input shear expression.
"""
from pathlib import Path
from collections import Counter
import base64
import hashlib
import itertools
import zlib

B = 29
FILENAME = "F7_R490_B29_Exact_Quarter_Witness_20261122.b85"
RAW_SHA256 = "ab344024836e8f6439ba6feffc19d1758493afe90613ebb1890aec3cbc96f8c7"
EXPECTED = {-2: 259262, -1: 2578390, 0: 5883031, 1: 3025404, 2: 371274}

def indexed_keys():
    R = list(range(-2 * B, 2 * B + 1))
    T = {r: range(2*r - min(B, r+B), 2*r - max(-B, r-B) + 1) for r in R}
    index = {}
    for i, r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r], T[u]):
                for rr in (r, u):
                    x, y = 2*rr - v, rr - v
                    key = (abs(x), y)
                    if y and key not in ((2, 1), (1, -1)) and key not in index:
                        index[key] = len(index)
    return index

def main():
    data_path = Path(__file__).resolve().parent.parent / "research_artifacts" / FILENAME
    encoded = data_path.read_text(encoding="utf8").strip()
    values = zlib.decompress(base64.b85decode(encoded))
    assert hashlib.sha256(values).hexdigest() == RAW_SHA256
    index = indexed_keys()
    assert len(index) == len(values) == 17470
    assert Counter(values) == {2: 11134, 3: 5109, 4: 1227}

    def Q(x, y):
        if y == 0:
            return 0 if x == 0 else 4
        key = (abs(x), y)
        if key in ((2, 1), (1, -1)):
            return 2
        return values[index[key]] if key in index else 2

    assert Q(0, 0) == 0
    assert Q(2, 1) == Q(-1, -1) == 2
    histogram = Counter()
    for a, b, c, d in itertools.product(range(-B, B + 1), repeat=4):
        k = a - 2*b - c + 2*d
        four_D = Q(a+k, b+k) + Q(c-k, d-k) - Q(a, b) - Q(c, d)
        assert abs(four_D) <= 2, (a, b, c, d, k, four_D)
        histogram[four_D] += 1

    assert dict(histogram) == EXPECTED
    assert sum(histogram.values()) == 59**4 == 12117361
    assert max(abs(i) for i in histogram) == 2
    print("CERTIFIED: F7 e_B=1/2 for every integer 1<=B<=29")
    print("Full original-input evaluations:", sum(histogram.values()))
    print("Indexed Q coordinates:", len(index))
    print("Exact histogram of 4D:", dict(sorted(histogram.items())))
    print("Raw-byte SHA256:", RAW_SHA256)

if __name__ == "__main__":
    main()
