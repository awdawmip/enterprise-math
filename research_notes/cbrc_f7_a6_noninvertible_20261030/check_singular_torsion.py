#!/usr/bin/env python3
"""Exact finite regression for F7 A6 fixed-scalar maps with singular torsion blocks.

Regression only: the published universal theorem is proved algebraically.
Requires sympy 1.14+ for integer Smith normal form; uses exact arithmetic.
"""
from collections import Counter
from itertools import permutations, product
from math import prod
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

C = Matrix([[1, 1], [1, -1]])
D = Matrix.diag(C, C)
ALL_P = [p for p in permutations(range(4)) if p[0] // 2 != p[1] // 2]
assert len(ALL_P) == 16


def pmat(p):
    return Matrix(4, 4, lambda i, j: int(p[j] == i))


def rank_mod3(B):
    if int(B.det()) % 3:
        return 2
    return int(any(int(v) % 3 for v in B))


def snf_diag(M):
    S = smith_normal_form(M, domain=ZZ)
    return [abs(int(S[i, i])) for i in range(min(S.rows, S.cols))]


def presentation(A, K, B):
    return Matrix.vstack(
        Matrix.hstack(A, Matrix.zeros(4, 2), Matrix.zeros(4, 2)),
        Matrix.hstack(K, B, 3 * Matrix.eye(2)),
    )


def prime_part(invariants, p):
    out = []
    for x in invariants:
        v = 1
        while x % p == 0:
            x //= p
            v *= p
        if v > 1:
            out.append(v)
    return sorted(out)


def conserved_Q2(A, w):
    return sum(v != 0 for v in D * A * w) == sum(v != 0 for v in D * w)


def main():
    p_list = ALL_P
    Bs = [Matrix(2, 2, t) for t in product(range(3), repeat=4)]
    ranks = Counter(rank_mod3(B) for B in Bs)
    assert ranks == Counter({0: 1, 1: 32, 2: 48})
    A0 = D * pmat(p_list[0]) * D
    assert abs(int(A0.det())) == 16

    support_checks = 0
    for p in p_list:
        P = pmat(p)
        for ks in ((1, 1, 1, 1), (3, 3, 3, 3), (2, -1, 3, 1)):
            A = D * P * Matrix.diag(*ks) * D
            assert D * A == 2 * P * Matrix.diag(*ks) * D
            assert abs(int(A.det())) == 16 * prod(abs(k) for k in ks)
            e = Matrix([1, 0, 0, 0])
            h = D * A * e
            assert (sum(h[j] != 0 for j in (0, 1)),
                    sum(h[j] != 0 for j in (2, 3))) == (1, 1)
            for t in product((-1, 0, 1), repeat=4):
                assert conserved_Q2(A, Matrix(t))
                support_checks += 1

    K_samples = (
        Matrix.zeros(2, 4),
        Matrix([[1, 0, 0, 0], [0, 0, 0, 0]]),
        Matrix([[1, 0, 1, 0], [0, 1, 0, 1]]),
    )
    index_checks = 0
    for p in p_list[:4]:
        for ks in ((1, 1, 1, 1), (3, 3, 3, 3), (2, -1, 3, 1)):
            A = D * pmat(p) * Matrix.diag(*ks) * D
            for B in Bs:
                r = rank_mod3(B)
                for K in K_samples:
                    ss = snf_diag(presentation(A, K, B))
                    assert all(n > 0 for n in ss)
                    assert prod(ss) == abs(int(A.det())) * (3 ** (2-r))
                    index_checks += 1

    non_split_checks = 0
    type_histogram = Counter()
    for vec in product(range(3), repeat=4):
        K = Matrix([[vec[0], vec[1], 0, 0], [vec[2], vec[3], 0, 0]])
        r = rank_mod3(K[:, :2])
        ds = snf_diag(presentation(3 * A0, K, Matrix.zeros(2, 2)))
        assert prod(ds) == 16 * (3**6)
        expected_three = sorted([9]*r + [3]*(6-2*r))
        assert prime_part(ds, 3) == expected_three
        assert prime_part(ds, 2) == [2, 2, 4]
        type_histogram[r] += 1
        non_split_checks += 1
    assert type_histogram == Counter({0: 1, 1: 32, 2: 48})

    out = {
        "status": "PASS",
        "scope": "exact auxiliary F7 A6 fixed-support-scalar group only",
        "split_permutations": len(p_list),
        "torsion_B_rank_distribution": dict(sorted(ranks.items())),
        "free_support_regression_cases": support_checks,
        "torsion_index_kernel_snf_cases": index_checks,
        "three_primary_K_regression_cases": non_split_checks,
        "three_primary_K_rank_distribution": dict(sorted(type_histogram.items())),
        "three_primary_types_by_K_rank": {
            str(r): sorted([9]*r+[3]*(6-2*r)) for r in range(3)
        },
        "two_primary_type": [2, 2, 4],
        "universal_proof_is_algebraic": True,
        "independent_review_or_native_admission": False,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
