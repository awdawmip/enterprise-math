#!/usr/bin/env python3
"""Original-source exact fixed Cell slice metric interface verification.
This is ONLY for the registered two-generator slice, NOT full native signed X6.
Full universal bound is proved in companion research note; finite tests corroborate.
"""
from collections import Counter
from hashlib import sha1
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import sys

EXPECTED_ORIGINAL_BLOB = '2aa70d8f8509dc31d73f6891b97f9fdf7377df2a'
PATH = (Path(sys.argv[1]) if len(sys.argv) > 1 else
        Path(__file__).resolve().parents[1] / 'src/enterprise_math/_cell_slice_codec.py')
source = PATH.read_bytes()
actual_sha = sha1(f'blob {len(source)}\0'.encode() + source).hexdigest()
assert actual_sha == EXPECTED_ORIGINAL_BLOB, (actual_sha, EXPECTED_ORIGINAL_BLOB)
spec = spec_from_file_location('_verified_original_cell_slice_codec', PATH)
module = module_from_spec(spec)
spec.loader.exec_module(module)

def l1(p, q):
    return sum(abs(a-b) for a,b in zip(p,q))

def run():
    counts = Counter()
    directions = {'E1+': (1,0), 'E1-': (-1,0),
                  'E2+': (0,1), 'E2-': (0,-1)}
    for m in range(-20,21):
        for n in range(-20,21):
            p=(m,n)
            a=module.encode(p)
            assert module.decode(a)==p
            for label, (dx,dy) in directions.items():
                q=(m+dx,n+dy)
                b=module.encode(q)
                assert module.code_step(a,label)==b
                code_distance=l1(a,b)
                assert 1<=code_distance<=3
                counts[code_distance]+=1
    assert counts=={1:4080, 2:2563, 3:81}, counts
    pairs=0
    points=[(m,n) for m in range(-7,8) for n in range(-7,8)]
    for p,q in combinations(points,2):
        raw=l1(p,q)
        observed=l1(module.encode(p),module.encode(q))
        assert 2*observed>=raw and observed<=3*raw
        pairs+=1
    assert pairs==25200
    # Both optimal constants are attained using exact original code.
    assert module.encode((-1,-1))==(0,1,2,0,0,0)
    assert module.encode((0,0))==(0,1,1,0,0,0)
    assert l1(module.encode((-1,-1)),module.encode((0,0)))==1
    assert l1((-1,-1),(0,0))==2
    assert module.encode((-1,-2))==(1,0,3,0,0,0)
    assert l1(module.encode((-1,-2)),module.encode((-1,-1)))==3
    assert l1((-1,-2),(-1,-1))==1
    print('PASS_X6_LP003_FIXED_CELL_SLICE_SHARP_BILIPSCHITZ_ORIGINAL_CODEC')
    print('original_source_git_blob=',actual_sha)
    print('primitive_step_checks=',sum(counts.values()),'distribution=',dict(counts))
    print('pair_checks=',pairs)
    print('sharp_constants=1/2,3')
    print('registered_fixed_2axis_chart_only=true; full_signed_X6_claim=false')

if __name__=='__main__':
    run()
