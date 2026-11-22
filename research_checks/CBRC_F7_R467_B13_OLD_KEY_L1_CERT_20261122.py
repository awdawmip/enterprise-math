#!/usr/bin/env python3
"""Exact integer verification of r467: B13 old-key L1 repair lower bound."""
import hashlib
import itertools
import json
import sys
from pathlib import Path

M = 30_000_000_000_000
TABLE_SHA256 = "340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5"
PACK = [[-13,11,11,-12],[12,-11,-8,13],[-12,0,-9,13],[1,-1,8,-13],[13,-9,-9,0],[-10,13,0,0],[9,-13,12,0],[8,0,0,-13],[-4,0,13,-7],[13,-3,13,-11],[-1,-1,6,-13],[7,-12,-13,-2],[-12,0,10,-13],[-12,11,13,6],[-13,10,12,0],[-3,-13,-9,0],[-11,0,-13,9],[-12,-13,-13,2],[8,-11,0,13],[13,0,-7,13],[-13,-6,10,0],[-1,-1,-6,13],[13,-8,-10,12],[-2,-13,-1,-1],[12,-12,12,13],[-13,-4,0,0],[6,-11,-13,0],[-2,13,-1,-1],[-1,4,-13,8],[10,5,13,13],[8,-5,13,12],[-1,-13,-2,-7],[3,0,13,-10],[13,-1,-8,12],[-13,5,8,1],[-1,6,-13,4],[11,13,-11,5],[2,7,1,13],[13,3,-1,-1],[8,0,-13,0],[-8,0,13,-5],[-13,-12,-7,7],[-13,0,-11,9],[13,0,10,-12],[5,-13,-4,3],[-3,13,-11,12],[11,-2,7,-13],[-3,-4,4,-13],[-13,0,-3,-7],[-5,8,-5,13],[-13,0,12,0],[-8,8,-13,7],[13,0,3,-12],[-13,1,5,0],[-4,13,8,-3],[-13,-13,-8,-4],[13,0,-12,9],[-13,0,1,-12],[10,-8,-11,-13]]
EXPECTED_MARGIN_SUM = 329_038_543_438_489

def key(x, y):
    return (abs(x), y)

def mutable(s):
    return s[1] != 0 and s not in ((2, 1), (1, -1))

def points(z):
    a, b, c, d = z
    t = a - 2*b - c + 2*d
    return ((a+t,b+t), (c-t,d-t), (a,b), (c,d))

def verify(table_path):
    data = Path(table_path).read_bytes()
    assert hashlib.sha256(data).hexdigest() == TABLE_SHA256
    increments = {(x, y): n for x, y, n in json.loads(data)}
    assert len(increments) == 2813

    def scaled_q(x, y):
        if x == 0 and y == 0:
            return 0
        if y == 0:
            return M
        return M//2 + increments.get(key(x, y), 0)

    old = set()
    for z in itertools.product(range(-12,13), repeat=4):
        old.update(key(*p) for p in points(z))
    assert len(old) == 3073

    assert len(PACK) == 59
    occupied = set()
    total_margin = 0
    for z in PACK:
        assert len(z) == 4 and all(-13 <= c <= 13 for c in z)
        p = points(z)
        support = {key(*v) for v in p}
        assert support <= old
        coeff = {}
        for i, v in enumerate(p):
            s = key(*v)
            if mutable(s):
                coeff[s] = coeff.get(s, 0) + (1 if i < 2 else -1)
        assert coeff and all(abs(c) <= 1 for c in coeff.values())
        assert occupied.isdisjoint(coeff)
        occupied.update(coeff)
        residual = scaled_q(*p[0])+scaled_q(*p[1])-scaled_q(*p[2])-scaled_q(*p[3])
        assert abs(residual) > M//2
        total_margin += abs(residual) - M//2
    assert total_margin == EXPECTED_MARGIN_SUM
    print("CERTIFIED: 59 old-key-disjoint violated B13 inputs")
    print("Old footprint:", len(old), "key supports in packing:", len(occupied))
    print("Exact L1 repair lower bound:", f"{total_margin}/{M}")

if __name__ == "__main__":
    verify(sys.argv[1])
