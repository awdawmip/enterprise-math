#!/usr/bin/env python3
"""Standalone exact-integer proof checker for F7 e_15=1/2.

Reads a frozen base85+zlib certificate containing 4730 little-endian int16
values Q=16*q. No numerical solver, scipy or numpy is used by this checker.
"""
import base64
import hashlib
import itertools
from pathlib import Path
import struct
import sys
import zlib

B = 15
SHA256 = '281b5bd19664a6e31d0ddff5f5ef1ff56deab5b4fc47814bf366407ba370d180'
FILENAME = 'F7_R478_B15_Exact_Sixteenths_Witness_20261122.b85'

def key(r, v):
    x, y = 2 * r - v, r - v
    return abs(x), y

def index_keys():
    R = list(range(-2 * B, 2 * B + 1))
    T = {r: range(2*r-min(B,r+B), 2*r-max(-B,r-B)+1) for r in R}
    idx = {}
    for i, r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r],T[u]):
                for rr in (r,u):
                    k = key(rr,v)
                    if k[1] != 0 and k not in ((2,1), (1,-1)) and k not in idx:
                        idx[k] = len(idx)
    return idx

def verify(source):
    raw = zlib.decompress(base64.b85decode(source.read_text(encoding='ascii').strip()))
    assert len(raw) == 2 * 4730
    assert hashlib.sha256(raw).hexdigest() == SHA256
    vals = struct.unpack('<4730h',raw)
    idx = index_keys()
    assert len(idx) == len(vals) == 4730
    assert min(vals) == 8 and max(vals) == 16
    def Q(x,y):
        if y == 0:
            return 0 if x == 0 else 16
        k = (abs(x),y)
        if k in ((2,1),(1,-1)):
            return 8
        return vals[idx[k]]
    maximum, arg, tight, nonzero = 0, None, 0, 0
    for a,b,c,d in itertools.product(range(-B,B+1),repeat=4):
        k = a - 2*b - c + 2*d
        delta = Q(a+k,b+k) + Q(c-k,d-k) - Q(a,b) - Q(c,d)
        if abs(delta) > maximum:
            maximum, arg = abs(delta), (a,b,c,d)
        if abs(delta) == 8:
            tight += 1
        if delta:
            nonzero += 1
    assert maximum == 8 and tight == 33416 and nonzero == 627428
    print('CERTIFIED: F7 B15 E=1/2', 'inputs=',31**4,'free_q=',4730,
          'max_abs_16D=',maximum,'tight_inputs=',tight,
          'nonzero_inputs=',nonzero,'attainment=',arg,
          'sha256=',SHA256)

if __name__ == '__main__':
    default=Path(__file__).resolve().parent.parent/'research_artifacts'/FILENAME
    verify(Path(sys.argv[1]) if len(sys.argv)>1 else default)
