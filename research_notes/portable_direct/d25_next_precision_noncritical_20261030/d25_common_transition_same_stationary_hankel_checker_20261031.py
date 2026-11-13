#!/usr/bin/env python3
"""Exact integer checker for a shared numeric hidden-label transition/Hankel witness.

The hidden transition matrix and initial source weights are identical for A and B.
The two types differ only in their positive integer emission kernels.
No native X6 computation or independent mathematical review is performed.
"""
from itertools import product
from math import comb, factorial, prod
import json
from pathlib import Path

Z = (1, -1, -1, 1)
PARAMS = ((1, 1), (2, 1), (1, 2))


def model(m, c, d):
    n = 2 * m - 1
    p = n + 1
    w = tuple(comb(n, 2 * k) for k in range(m))
    wsum = sum(w)
    s = c + d * wsum
    t = tuple(tuple(c * (i == j) + d * w[j] for j in range(m)) for i in range(m))
    h_a = tuple(2 * k for k in range(m))
    h_b = tuple(n - 2 * k for k in range(m))
    kernel = lambda h: tuple(tuple(p + h[k] * z for z in Z) for k in range(m))
    j_a, j_b = kernel(h_a), kernel(h_b)
    assert wsum == 2 ** (n - 1)
    assert tuple(comb(n, v) for v in h_b) == w
    assert sorted(h_a) == list(range(0, n + 1, 2))
    assert sorted(h_b) == list(range(1, n + 1, 2))
    assert all(v > 0 for row in t for v in row)
    assert all(sum(row) == s for row in t)
    assert all(w[i] * t[i][j] == w[j] * t[j][i] for i in range(m) for j in range(m))
    assert all(all(v > 0 for v in row) and sum(row) == 4 * p for J in (j_a, j_b) for row in J)
    return w, t, j_a, j_b, s


def word_count(weights, t, kernels, word):
    v = weights
    for y in word:
        emitted = tuple(v[i] * kernels[i][y] for i in range(len(v)))
        v = tuple(sum(emitted[i] * t[i][j] for i in range(len(v))) for j in range(len(v)))
    return sum(v)


def main():
    cases = []
    full_word_checks = 0
    structural_cases = 0
    for m in range(1, 7):
        n = 2 * m - 1
        for c, d in PARAMS:
            w, t, ja, jb, s = model(m, c, d)
            structural_cases += 1
            record = {"m": m, "c": c, "d": d, "N": n,
                      "common_initial_weights": list(w),
                      "same_numeric_transition": [list(row) for row in t] if m <= 2 else "exact-form-asserted",
                      "row_sum": s,
                      "full_word_exhaustive": m <= 3}
            if m <= 3:
                for horizon in range(n + 1):
                    difference_l1, total_a, total_b = 0, 0, 0
                    for word in product(range(4), repeat=horizon):
                        a = word_count(w, t, ja, word)
                        b = word_count(w, t, jb, word)
                        predicted = (s * c ** (n - 1) * (-1)**n * factorial(n) *
                                     prod(Z[y] for y in word)) if horizon == n else 0
                        assert a - b == predicted, (m,c,d,word,a,b,predicted)
                        difference_l1 += abs(a - b)
                        total_a += a
                        total_b += b
                        full_word_checks += 1
                    assert total_a == total_b == sum(w) * (4 * (n + 1) * s) ** horizon
                    assert difference_l1 == ((4 ** n) * s * c ** (n - 1) * factorial(n) if horizon == n else 0)
                if m == 2 and c == d == 1:
                    record["m2_all_zero_length3"] = {
                        "A": word_count(w,t,ja,(0,0,0)),
                        "B": word_count(w,t,jb,(0,0,0)),
                        "first_split_l1": (4 ** n) * s * c ** (n - 1) * factorial(n),
                        "total_each": sum(w) * (4 * (n + 1) * s) ** n}
            else:
                # A single targeted new-word witness; prior all-word formula is proved symbolically.
                word=(0,)*n
                a=word_count(w,t,ja,word)
                b=word_count(w,t,jb,word)
                assert a-b == s * c ** (n-1) * (-1)**n * factorial(n)
                record["all_zero_first_split_signed_gap"] = a-b
            cases.append(record)
    cert={"status":"PASS", "scope":"AUTHOR_EXACT_INTEGER_AUXILIARY_BRC_ONLY",
          "claim":"same numeric strictly-positive reversible transition AND same initial distribution reach sharp uniform 2m-1 distinguishing horizon",
          "structural_parameter_cases":structural_cases,
          "exhaustive_word_parameter_domain":{"m":[1,2,3],"c_d_pairs":PARAMS,
                                                "horizon":"0..2m-1, all 4^t ordered output words"},
          "exhaustive_word_pair_comparisons":full_word_checks,
          "larger_m_structural_and_witness_checks":[4,5,6],
          "proof_scope":"all integers m>=1,c,d>=1 via parity-reflection of binomial weights and prior integer keep/reset decomposition",
          "cases":cases,
          "admission":"UNREVIEWED_NOT_ADMITTED_NOT_NATIVE"}
    path=Path(__file__).with_name('d25_common_transition_same_stationary_hankel_author_check_20261031.json')
    path.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'PASS {structural_cases} structural configurations; {full_word_checks} complete ordered-word comparisons')
    print(next(x for x in cases if x['m']==2 and x['c']==1 and x['d']==1)['m2_all_zero_length3'])

if __name__=='__main__':
    main()
