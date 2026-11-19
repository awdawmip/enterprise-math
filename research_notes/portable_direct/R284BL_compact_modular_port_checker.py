#!/usr/bin/env python3
"""R284BL exact 3x3 star-Port modular witness; Python standard library only."""
import hashlib
import json
from itertools import product
from math import isqrt

P = 100_003
H = 2
DELTA = 3
CONTROLS = (25_614, 64_524, 70_267, 34_320, 67_846)

def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))

def determinant(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)

def residue(matrix):
    d0, d1, d2, z1, z2 = CONTROLS
    c00,c01,c02,c10,c11,c12,c20,c21,c22 = matrix
    entries = ((d0-c00, -c01-z1, -c02-z2),
               (-c10, d1-c11, -c12),
               (-c20, -c21, d2-c22))
    direct = determinant(entries) % P
    # Independent six-permutation expansion.
    perms = ((0,1,2,1),(0,2,1,-1),(1,0,2,-1),
             (1,2,0,1),(2,0,1,1),(2,1,0,-1))
    check = sum(s*entries[0][a]*entries[1][b]*entries[2][c]
                for a,b,c,s in perms) % P
    assert direct == check
    return direct

def run():
    assert prime(P)
    candidates = list(product(range(1, H+1), repeat=9))
    values = [residue(c) for c in candidates]
    assert len(candidates) == H**9 == 512
    assert len(set(values)) == len(values)
    ordered = sorted(values)
    gaps = [(ordered[(i+1)%len(values)]-ordered[i]) % P
            for i in range(len(values))]
    gap = min(gaps)
    assert gap == 8 and gap > 2*DELTA
    i = gaps.index(gap)
    for c, v in zip(candidates,values):
        for e in range(-DELTA, DELTA+1):
            observed = (v+e) % P
            matches = [x for x in ordered
                       if min((observed-x)%P,(x-observed)%P) <= DELTA]
            assert matches == [v]
    return {
        "p":P,"candidate_count":len(candidates),
        "controls":CONTROLS,"min_cyclic_gap":gap,
        "min_gap_centers":[ordered[i],ordered[(i+1)%len(values)]],
        "tested_noisy_reads":len(values)*(2*DELTA+1),
        "candidate_order_residues":values,
        "sorted_residues":ordered,
        "sorted_residue_csv_sha256":hashlib.sha256(
            ",".join(map(str,ordered)).encode()).hexdigest()
    }

if __name__ == "__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
