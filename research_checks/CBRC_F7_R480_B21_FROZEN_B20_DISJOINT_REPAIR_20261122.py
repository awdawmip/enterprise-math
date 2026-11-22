#!/usr/bin/env python3
"""Exact F7 B20 -> B21 old-coordinate repair obstruction.
Uses original r479 B20 witness and 55 fixed disjoint B21 quadruples.
No solver, floating point, or network access.
"""
import base64
import hashlib
import itertools
import zlib
from collections import Counter
from pathlib import Path

EXPECTED_B20_SHA = 'c393685154755cf9f5c943334ceb247fe1c2ad73bcf8835fcdb41c1087012a36'
QUADS_B85 = 'c-mdjOAbRJ2nEnNYtcl&@BTMdlyYf0c*%K)fLeu1D|MGf)wz;0Ig&l8Nl7x8%FL*A3ZE}oONF}?h#4%y<L&0iD`yF}otuB${_I>X+Xh>7LK5OgoFu4(RSjhK9-)a)h?&q~VHNE+LI>URB#bITa<5Zkm^dL1dXp}{>u2@XcozGH|J?ly9%w_E*dfi$AprR(abJW!+W2H5'
EXPECTED_QUADS_SHA = '91296dd050299efa9237ae671e5e9e3dd5be129717bee840dcc5129fb143c466'

def index(b):
    R = list(range(-2*b, 2*b+1))
    T = {r: range(2*r-min(b,r+b), 2*r-max(-b,r-b)+1) for r in R}
    ix = {}
    for i, r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r], T[u]):
                for rr in (r, u):
                    x, y = 2*rr-v, rr-v
                    key = (abs(x), y)
                    if y and key not in ((2,1),(1,-1)) and key not in ix:
                        ix[key] = len(ix)
    return ix

def check():
    root = Path(__file__).resolve().parent.parent
    packed = (root/'research_artifacts'/'F7_R479_B20_Exact_Quarter_Witness_20261122.b85').read_text().strip()
    Q20 = zlib.decompress(base64.b85decode(packed))
    assert hashlib.sha256(Q20).hexdigest() == EXPECTED_B20_SHA
    ix = index(20)
    assert len(ix) == len(Q20) == 8358

    def Q(x, y):
        if y == 0:
            return 0 if x == 0 else 4
        key = abs(x), y
        if key in ((2,1),(1,-1)):
            return 2
        return Q20[ix[key]] if key in ix else 2

    def mutable_key(x, y):
        key = abs(x), y
        return key if y and key not in ((2,1), (1,-1)) else None

    quad_text = zlib.decompress(base64.b85decode(QUADS_B85))
    assert hashlib.sha256(quad_text).hexdigest() == EXPECTED_QUADS_SHA
    quads = [tuple(map(int, row.split(','))) for row in quad_text.decode().splitlines()]
    assert len(quads) == len(set(quads)) == 55

    used = set()
    gaps = []
    for a, b, c, d in quads:
        assert all(-21 <= v <= 21 for v in (a,b,c,d))
        k = a-2*b-c+2*d
        points = ((a+k,b+k),(c-k,d-k),(a,b),(c,d))
        dq = Q(*points[0]) + Q(*points[1]) - Q(*points[2]) - Q(*points[3])
        assert abs(dq) > 2
        coeff = Counter()
        for s, (x,y) in zip((1,1,-1,-1), points):
            key = mutable_key(x,y)
            if key is not None:
                assert key in ix
                coeff[key] += s
        coeff = {p:c for p,c in coeff.items() if c}
        assert coeff and max(abs(c) for c in coeff.values()) == 1
        assert used.isdisjoint(coeff)
        used.update(coeff)
        gaps.append(abs(dq)-2)

    assert len(used) == 124
    assert Counter(gaps) == {1:53, 2:2}
    assert sum(gaps) == 57
    print('CERTIFIED: 55 disjoint B21 violations on old B20 variables;')
    print('old keys:',len(used),'sum quarter gaps:',sum(gaps),
          'minimum old-coordinate changes: 55; minimum old L1(q): 57/4 = 14.25')

if __name__ == '__main__':
    check()
