#!/usr/bin/env python3
"""Exact verification for R749SMN (abstract adaptive signed-source Walsh tree).
No native V29/V39 operation is claimed.
"""
from itertools import product
import json

PRIME = 1000000007

def rank_mod(rows):
    a = [[int(v) % PRIME for v in row] for row in rows]
    if not a:
        return 0
    k = 0
    for j in range(len(a[0])):
        i = next((i for i in range(k, len(a)) if a[i][j]), None)
        if i is None:
            continue
        a[k], a[i] = a[i], a[k]
        inv = pow(a[k][j], -1, PRIME)
        for i in range(k + 1, len(a)):
            if a[i][j]:
                z = a[i][j] * inv % PRIME
                for t in range(j, len(a[0])):
                    a[i][t] = (a[i][t] - z * a[k][t]) % PRIME
        k += 1
        if k == len(a):
            break
    return k

def leaves(r, a, b, c, P, Bm, Bp):
    # Root bias P/2, child biases B/2. Multiply every leaf likelihood by 16.
    out = []
    for sr, sc in product((-1, 1), repeat=2):
        mask, B = (b, Bm) if sr == -1 else (c, Bp)
        row = []
        for x in range(1 << r):
            ca = -1 if (a & x).bit_count() & 1 else 1
            cm = -1 if (mask & x).bit_count() & 1 else 1
            row.append((2 + sr * P * ca) * (2 + sc * B * cm))
        out.append(row)
    return out

def contrast_coefficients(r, a, b, c, P, Bm, Bp):
    # Fourier nonconstant coefficient rows, up to nonzero uniform scalings.
    specs = ((P, ((a, 1),)),
             (Bm, ((b, 2), (a ^ b, -P))),
             (Bp, ((c, 2), (a ^ c, P))))
    out = []
    for scale, terms in specs:
        v = [0] * ((1 << r) - 1)
        for mask, val in terms:
            if mask != 0:
                v[mask - 1] += scale * val
        out.append(v)
    return out

def classified(r, a, b, c, P, Bm, Bp):
    if a and P:
        return 1 + int(Bm != 0 and b not in (0, a)) + int(Bp != 0 and c not in (0, a))
    if P == 0:
        return len({m for m, B in ((b, Bm), (c, Bp)) if m and B})
    # Zero source-mask root; deterministic routes can make a branch unreachable.
    s = set()
    if P != 2 and Bm and b:
        s.add(b)
    if P != -2 and Bp and c:
        s.add(c)
    return len(s)

def main():
    cases = 0
    per_source_rank = {}
    max_likelihood_rank = 0
    for r in (1, 2, 3):
        for a, b, c in product(range(1 << r), repeat=3):
            for P, Bm, Bp in product((-2, -1, 0, 1, 2), (-2, 0, 1, 2), (-2, 0, 1, 2)):
                direct = rank_mod(leaves(r, a, b, c, P, Bm, Bp))
                spectral = rank_mod(contrast_coefficients(r, a, b, c, P, Bm, Bp))
                closed = classified(r, a, b, c, P, Bm, Bp)
                assert direct - 1 == spectral == closed, (r, a, b, c, P, Bm, Bp, direct, spectral, closed)
                cases += 1
                per_source_rank[str(r)] = per_source_rank.get(str(r), 0) + 1
                max_likelihood_rank = max(max_likelihood_rank, direct)
    assert rank_mod(leaves(2, 1, 2, 2, 1, 1, 1)) == 4
    assert rank_mod(leaves(2, 1, 1, 2, 1, 1, 1)) == 3
    assert rank_mod(leaves(2, 1, 2, 2, 0, 1, 1)) == 2
    assert rank_mod(leaves(2, 1, 2, 3, 1, 1, 1)) == 4
    outcome = {
      "schema": "ENTERPRISE_MATH_R749SMN_EXACT_CHECK_V1",
      "status": "PASS",
      "date": "2026-11-13",
      "frozen_scientific_input": "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
      "model": "abstract adaptive publicly-observed depth-two signed Walsh source observer",
      "arithmetic": "integer likelihood numerator x16; modular rank prime 1000000007; 4x4 likelihood minors <=24*16^4 < prime; Walsh minors <=6*8^3 < prime",
      "parameter_domains": {
        "source_ranks": [1, 2, 3],
        "masks": "all ordered a,b,c in F2^r including zero",
        "root_bias_numerators_over_2": [-2, -1, 0, 1, 2],
        "child_bias_numerators_over_2": [-2, 0, 1, 2]
      },
      "number_exact_cases": cases,
      "per_rank_cases": per_source_rank,
      "max_likelihood_rank": max_likelihood_rank,
      "comparisons": ["direct leaf-rank", "Walsh coefficient-rank", "closed-form-rank"],
      "witness_ranks": {
        "root_1_children_2_2": 4,
        "root_1_children_1_2": 3,
        "erased_root_children_2_2": 2
      },
      "scope": "Finite exact-grid validation; general real-bias claims established separately by algebraic proof."
    }
    print("PASS", cases, per_source_rank, "maximum likelihood rank", max_likelihood_rank)
    with open("R749SMN_DEPENDENT_PORT_TREE_RESULTS.json", "w", encoding="utf-8") as f:
        json.dump(outcome, f, ensure_ascii=False, indent=2)
        f.write("\n")

if __name__ == "__main__":
    main()
