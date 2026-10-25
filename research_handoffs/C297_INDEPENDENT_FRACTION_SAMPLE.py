#!/usr/bin/env python3
"""Independent direct full-Fraction check of a prespecified sparse sample.
The all-250 endpoint certificate is C297_REPLAY_512_EXACT.py.
"""
import base64,zlib,json
from pathlib import Path
from fractions import Fraction as R
import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as c288

paths,_=c288.build_paths()
parents=json.loads(Path('C296_125_EXACT_DYADIC_256_BRACKETS.json').read_text())['records']
arr=zlib.decompress(base64.b64decode(Path('C297_K512_SUFFIX256_CERTIFICATE.b64').read_text()))
W,_=s.floor_fixed_masses()
idxs=tuple(range(0,125,8)) # 16 predeclared paths, 32 endpoints
assert len(idxs)==16
for i in idxs:
    k=(int(parents[i]['dyadic_left_integer'])<<256)+int.from_bytes(arr[32*i:32*(i+1)],'big')
    for off in (0,1):
        t=R(k+off,1<<512)
        v=tuple(a+t*b for a,b in zip(paths[i]['w'],paths[i]['d']))
        x=s.original_F(v,W)
        assert (x<s.Q) if off==0 else (x>s.Q),(i,off)
print('C297_INDEPENDENT_FULL_FRACTION_32_ENDPOINTS_PASS')
