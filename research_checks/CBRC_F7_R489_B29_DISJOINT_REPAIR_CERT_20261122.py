#!/usr/bin/env python3
"""Exact B29 audit of the fixed r488 B28 witness; 42 old-coordinate repair obstructions.
Run from repository checkout: python research_checks/CBRC_F7_R489_B29_DISJOINT_REPAIR_CERT_20261122.py
This checker reuses the fixed r488 B28 witness, never optimizes or changes its values.
"""
from collections import Counter, defaultdict
from pathlib import Path
import base64
import hashlib
import zlib

from CBRC_F7_R488_B28_EXACT_QUARTER_CERT_20261122 import indexed_keys

B = 29
ORIGINAL_SHA256 = "fa01c131e431a7ff708dbffc9974c44dcb8e2f126349bcbe8ba6ee5bc7a1fd6d"
WITNESSES = [
    (-57, -53, -86, -78, 3),
    (-12, 24, -16, 53, 3),
    (-36, 9, -65, 12, 3),
    (-24, 18, -53, 27, 3),
    (-11, 20, -22, 49, 3),
    (-20, 17, -49, 29, 3),
    (-36, 45, -46, 61, -3),
    (-13, 35, -15, 41, -3),
    (-36, 41, -43, 53, -3),
    (-47, 39, -66, 49, -3),
    (-44, 42, -60, 55, -3),
    (-42, 45, -55, 62, -3),
    (-46, 40, -64, 51, -3),
    (-38, 41, -47, 56, -3),
    (-42, 48, -57, 67, -3),
    (-49, 40, -69, 54, -3),
    (-48, 42, -67, 57, -3),
    (-52, -38, -75, -49, -3),
    (-50, 26, -71, 27, -3),
    (-9, 43, -20, 57, -3),
    (-26, 49, -27, 69, -3),
    (-22, 52, -27, 75, -3),
    (-55, 36, -81, 46, -3),
    (-54, 38, -79, 49, -3),
    (-34, 50, -45, 71, -3),
    (-22, 51, -21, 73, -3),
    (-56, 22, -83, 27, -3),
    (-43, 38, -60, 47, -3),
    (-32, 54, -40, 79, -3),
    (-32, 55, -38, 81, -3),
    (10, 56, 11, 83, -3),
    (34, 54, 43, 83, -3),
    (-43, 8, -57, 22, -3),
    (-57, -46, -85, -63, -3),
    (-41, 11, -53, 16, -3),
    (-40, 10, -51, 28, -3),
    (-44, 46, -59, 64, -3),
    (-44, 44, -62, 59, -3),
    (-45, 46, -62, 63, -3),
    (-47, 41, -65, 54, -3),
    (-46, 47, -65, 65, -3),
    (-45, 39, -61, 54, -3),
]

def main():
    base = Path(__file__).resolve().parent.parent
    encoded = (base / "research_artifacts/F7_R488_B28_Exact_Quarter_Witness_20261122.b85").read_text().strip()
    values = zlib.decompress(base64.b85decode(encoded))
    assert hashlib.sha256(values).hexdigest() == ORIGINAL_SHA256
    ix = indexed_keys()
    assert len(ix) == len(values) == 16294
    assert Counter(values) == {2: 10390, 3: 4709, 4: 1195}

    def Q(x, y):
        if y == 0:
            return 0 if x == 0 else 4
        key = (abs(x), y)
        if key in ((2, 1), (1, -1)):
            return 2
        return values[ix[key]] if key in ix else 2

    def mutable(rr, v):
        x, y = 2 * rr - v, rr - v
        k = (abs(x), y)
        return k if y != 0 and k not in ((2, 1), (1, -1)) else None

    R = range(-2*B, 2*B + 1)
    T = {r: range(2*r - min(B, r+B), 2*r - max(-B, r-B)+1) for r in R}
    count_half = Counter()
    old_only_bad = 0
    four_old_distinct = 0
    for r in R:
        for u in range(r+1, 2*B+1):
            vals_t, vals_s = defaultdict(list), defaultdict(list)
            for t in T[r]:
                vals_t[Q(2*r-t, r-t) - Q(2*u-t, u-t)].append(t)
            for s in T[u]:
                vals_s[Q(2*r-s, r-s) - Q(2*u-s, u-s)].append(s)
            for ft, ts in vals_t.items():
                for fs, ss in vals_s.items():
                    delta = fs-ft
                    count_half[delta] += len(ts)*len(ss)
                    if abs(delta) > 2:
                        for t in ts:
                            for s in ss:
                                support = [mutable(rr, v) for rr, v in ((r,t),(u,s),(r,s),(u,t))]
                                if all(key is None or key in ix for key in support):
                                    old_only_bad += 1
                                if len(set(support)) == 4 and None not in support and all(key in ix for key in support):
                                    four_old_distinct += 1

    full = Counter()
    for delta, n in count_half.items():
        full[delta] += n
        full[-delta] += n
    full[0] += sum(len(T[r])**2 for r in R)
    expected = {-4:88, -3:9288, -2:379057, -1:2798567, 0:5743361,
                1:2798567, 2:379057, 3:9288, 4:88}
    assert dict(full) == expected
    assert sum(full.values()) == 59**4 == 12117361
    assert sum(n for d, n in full.items() if abs(d)>2) == 18752
    assert old_only_bad == 9152 and four_old_distinct == 7355

    used = set()
    assert len(WITNESSES) == 42
    for r,u,t,s,claimed in WITNESSES:
        a,b,c,d = 2*r-t, r-t, 2*u-s, u-s
        assert -B <= min(a,b,c,d) and max(a,b,c,d) <= B
        k = a - 2*b - c + 2*d
        assert k == t-s
        actual = Q(a+k,b+k)+Q(c-k,d-k)-Q(a,b)-Q(c,d)
        assert actual == claimed and abs(actual) == 3
        support = [mutable(rr,v) for rr,v in ((r,t),(u,s),(r,s),(u,t))]
        assert None not in support and len(set(support)) == 4
        assert all(key in ix and key not in used for key in support)
        used.update(support)
    assert len(used) == 168
    print("EXACT r489: B29 default r488 extension has 18,752 violations, max |4D|=4.")
    print("Old-only half: 9,152; all-old distinct-four half: 7,355.")
    print("42 disjoint signed |4D|=3 witness rows / 168 old mutable keys.")
    print("Any B29 half-error repair requires >=42 changed B28 keys and old L1 >=21/2.")
    print("Histogram", dict(sorted(full.items())))

if __name__ == "__main__":
    main()
