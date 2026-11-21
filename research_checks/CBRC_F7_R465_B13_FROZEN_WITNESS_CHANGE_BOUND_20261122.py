#!/usr/bin/env python3
"""Exact finite audit of the frozen CBRC F7 r464 B=12 witness on B=13.

Input: the 62,463-byte r464 JSON witness, SHA256 pinned below.
No optimizer, floating point, or unverified native review is used.
"""
import collections
import hashlib
import itertools
import json
import sys
from pathlib import Path

M = 30_000_000_000_000
WITNESS_SHA256 = "340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5"

def key(x, y):
    return (abs(x), y)

def main(path):
    data = Path(path).read_bytes()
    assert hashlib.sha256(data).hexdigest() == WITNESS_SHA256
    rows = json.loads(data)
    assert len(rows) == 2813 and rows == sorted(rows)
    increments = {(a,b):n for a,b,n in rows}
    assert len(increments) == len(rows)

    def q(x, y):
        if (x, y) == (0, 0): return 0
        if y == 0: return M
        if key(x,y) in ((2,1),(1,-1)): return M//2
        return M//2 + increments.get(key(x,y), 0)

    def support_and_residual(z):
        a,b,c,d = z
        k = a - 2*b - c + 2*d
        points = [(a+k,b+k),(c-k,d-k),(a,b),(c,d)]
        return frozenset(key(*p) for p in points), q(*points[0])+q(*points[1])-q(*points[2])-q(*points[3])

    footprint = set()
    for z in itertools.product(range(-12,13),repeat=4):
        support, residual = support_and_residual(z)
        assert abs(residual) <= M//2
        footprint.update(support)
    assert len(footprint) == 3073

    violations = []
    total_b13_violations = 0
    max_abs = 0
    for z in itertools.product(range(-13,14),repeat=4):
        support, residual = support_and_residual(z)
        max_abs = max(max_abs,abs(residual))
        if abs(residual) > M//2:
            total_b13_violations += 1
            if support <= footprint:
                violations.append((z, support, residual))

    assert total_b13_violations == 16432
    assert max_abs == 48016153472784
    assert len(violations) == 7916
    frequencies = collections.Counter(p for _,support,_ in violations for p in support)
    violations.sort(key=lambda rec:(sum(frequencies[p] for p in rec[1]),len(rec[1]),rec[0]))
    occupied = set()
    selection = []
    for z,support,residual in violations:
        if support.isdisjoint(occupied):
            selection.append((z,support,residual))
            occupied.update(support)
    assert len(selection) == 53
    assert len(occupied) == 210
    assert all(abs(residual)>M//2 and support <= footprint for _,support,residual in selection)
    print('B12 referenced even-coordinate keys:',len(footprint))
    print('B13 violated inputs:',total_b13_violations)
    print('B13 violations fully supported on B12 footprint:',len(violations))
    print('Pairwise-disjoint old-footprint violating supports:',len(selection))
    print('Lower bound on changed B12 scalar coordinates for any B13 correction:',len(selection))
    print('Maximum B13 error:',max_abs,'/',M)
    print('Example old-footprint violation: z=(0,-13,0,1), D numerator=-18539061660897')
    return selection

if __name__ == '__main__':
    main(sys.argv[1])
