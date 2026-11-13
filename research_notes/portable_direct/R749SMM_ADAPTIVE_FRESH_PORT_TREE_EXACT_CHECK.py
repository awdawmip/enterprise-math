#!/usr/bin/env python3
"""Exact Walsh rank checker for R749SMM, a publicly observed adaptive parity tree.
No native Enterprise Math event arithmetic is asserted or performed here.
"""
from fractions import Fraction as Q
from itertools import product
import json


def rank(rows):
    mat = [list(r) for r in rows]
    n = len(mat)
    m = len(mat[0])
    pivotrow = 0
    for col in range(m):
        i = next((i for i in range(pivotrow, n) if mat[i][col]), None)
        if i is None:
            continue
        mat[pivotrow], mat[i] = mat[i], mat[pivotrow]
        denom = mat[pivotrow][col]
        mat[pivotrow] = [x / denom for x in mat[pivotrow]]
        for j in range(pivotrow + 1, n):
            if mat[j][col]:
                factor = mat[j][col]
                mat[j] = [a - factor * b for a, b in zip(mat[j], mat[pivotrow])]
        pivotrow += 1
        if pivotrow == n:
            break
    return pivotrow


def nodes(depth):
    return tuple(''.join(b) for k in range(depth) for b in product('01', repeat=k))


def tree_rows(depth, biases, masks=None):
    names = nodes(depth)
    if masks is None:
        masks = {s: 1 << i for i, s in enumerate(names)}
    states = range(1 << len(names))
    rows = []
    for bits in product('01', repeat=depth):
        hist = ''
        row = []
        for source in states:
            h = ''
            prob = Q(1)
            for bit in bits:
                node_bias = biases[h]
                signed = 1 if bit == '1' else -1
                parity = -1 if (masks[h] & source).bit_count() & 1 else 1
                prob *= (1 + node_bias * signed * parity) / 2
                h += bit
            row.append(prob)
        rows.append(row)
    return rows


def check(depth, biases):
    arr = tree_rows(depth, biases)
    got = rank(arr)
    expected = 1 + sum(v != 0 for v in biases.values())
    assert got == expected, (depth, got, expected, biases)
    assert all(sum(r[s] for r in arr) == 1 for s in range(len(arr[0])))
    return got


def main():
    tests = 0
    counts = {}
    for d in (1, 2, 3):
        ns = nodes(d)
        rks = {}
        for active in product((False, True), repeat=len(ns)):
            lam = {name: Q(1,2) if b else Q(0) for name, b in zip(ns, active)}
            r = check(d, lam)
            rks[str(r)] = rks.get(str(r), 0) + 1
            tests += 1
        counts[str(d)] = rks
    # Signed, deterministic, or erased channels: exact rational verification.
    extra_biases=(Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1))
    for k in range(30):
        ns=nodes(3)
        lam={s:extra_biases[(k+3*j+j*j)%len(extra_biases)] for j,s in enumerate(ns)}
        check(3,lam)
        tests+=1
    # The GF(2)-independent source-mask condition is essential.
    d=2
    r_all_informative_repeated=rank(tree_rows(d,{s:Q(1,2) for s in nodes(d)},
                                        masks={s:1 for s in nodes(d)}))
    assert r_all_informative_repeated == 2
    outcome={"schema":"ENTERPRISE_MATH_R749SMM_EXACT_CHECK_V1",
             "status":"PASS","date":"2026-11-13",
             "theorem":"For independent node-specific Walsh masks, rank(K)=1+#nonzero node-biases",
             "frozen_scientific_input":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
             "arithmetic":"Python standard library Fraction, exhaustive sources for depth 1,2,3; exact rational row rank",
             "exhaustive_zero_nonzero_patterns":2**1+2**3+2**7,
             "additional_signed_deterministic_profiles":30,
             "total_profiles":tests,"rank_distributions":counts,
             "dependent_masks_counterexample_rank":r_all_informative_repeated,
             "scope":"Author-side finite model regression; arbitrary finite-depth proof is algebraic and separate from grid"}
    with open('/mnt/data/em_research/R749SMM_ADAPTIVE_FRESH_PORT_TREE_RESULTS.json','w') as f:
        json.dump(outcome,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print('PASS',tests,'adaptive-tree exact profiles',counts,'dependent-mask rank',r_all_informative_repeated)


if __name__ == '__main__':
    main()
