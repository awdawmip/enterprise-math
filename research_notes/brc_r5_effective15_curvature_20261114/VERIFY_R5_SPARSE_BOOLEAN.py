#!/usr/bin/env python3
"""Exact 15-variable Möbius transform and four-cluster Boolean certificate for R5.
Import the adjacent frozen event constructor and direct center-cover solver.
This does not claim native X6 or formal Task admission.
"""
from collections import Counter
from VERIFY_R5_EFFECTIVE15_CURVATURE import ACTIVE, frozen, center_count, closed_points

EXPECTED = {
    (): 213,
    (2,3,4): -1,
    (5,): -1,
    (2,3,4,5): 1,
    (6,): -1,
    (5,6): 1,
    (2,3,4,5,6): -1,
    (8,): -1,
    (9,): -1,
    (8,9): 1,
    (10,11,12): -1,
    (9,10,11,12): 1,
    (8,9,10,11,12): -1,
    (12,13): -1,
    (10,11,12,13): 1,
    (9,10,11,12,13): -1,
    (8,9,10,11,12,13): 1,
    (16,): -1,
    (25,26,27): -1,
}

def boolean_formula(mask):
    b = {ACTIVE[i]: (mask >> i) & 1 for i in range(len(ACTIVE))}
    A = int(bool(b[5] or b[6])) + int(bool(b[2] and b[3] and b[4] and (not b[5] or b[6])))
    B = int(bool(b[8] or b[9])) + int(bool(b[12] and (b[13] or (b[10] and b[11] and (b[8] or not b[9])))))
    C = b[16]
    E = b[25]*b[26]*b[27]
    return 213 - A - B - C - E

def main():
    points, cuts = frozen()
    assert len(ACTIVE)==15 and len(points)==954 and len(cuts)==28
    n=1<<15
    values=[center_count(closed_points(points,cuts,m)) for m in range(n)]
    assert all(values[mask]==boolean_formula(mask) for mask in range(n))
    coefficients=values.copy()
    for j in range(15):
        bit=1<<j
        for mask in range(n):
            if mask&bit: coefficients[mask] -= coefficients[mask^bit]
    actual={tuple(ACTIVE[i] for i in range(15) if mask>>i&1):v
            for mask,v in enumerate(coefficients) if v}
    assert actual==EXPECTED, (actual,EXPECTED)
    by_degree=Counter()
    for cuts_set,coefficient in actual.items(): by_degree[len(cuts_set)]+=coefficient
    assert [by_degree[q] for q in range(7)]==[213,-5,1,-3,3,-3,1]
    assert all(q<=6 for q in by_degree)
    print("PASS_EXACT_R5_SPARSE_FOUR_CLUSTER_BOOLEAN 32768 assignments, 19 nonzero Möbius terms")
if __name__=="__main__": main()
