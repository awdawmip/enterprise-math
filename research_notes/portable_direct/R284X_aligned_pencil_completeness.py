#!/usr/bin/env python3
"""Exact Fraction test of single-row/column pencil completeness and Hall boundary."""
from fractions import Fraction as Q
import itertools
import json
import random
from R284W_common_kernel_certificate import determinant, rank, M_at, cofactor_ab, certificate


def rank_deficient_column_restriction(A, touched):
    k = len(A)
    cols = [j for j in range(k) if j not in touched]
    return bool(cols) and rank([[row[j] for j in cols] for row in A], len(cols)) < len(cols)


def common_kernel(A, edits):
    k = len(A)
    touched_cols = {j for i, j in edits}
    touched_rows = {i for i, j in edits}
    right = rank_deficient_column_restriction(A, touched_cols)
    rows = [i for i in range(k) if i not in touched_rows]
    left = bool(rows) and rank([[A[i][j] for i in rows] for j in range(k)], len(rows)) < len(rows)
    return right or left


def pencil(A, edits, z):
    B = [row[:] for row in A]
    for (i, j), t in zip(edits, z):
        B[i][j] += t
    return B


def main():
    rng = random.Random(28424)
    tested = 0
    zero_pencils = 0
    matching_present_zero = 0
    for k in (2, 3, 4, 5):
        for m in (1, 2, 3):
            for trial in range(80):
                A = [[Q(rng.randrange(-1, 2)) for _ in range(k)] for _ in range(k)]
                # Force actual singular baselines in one out of three tests.
                if trial % 3 == 0:
                    A[-1] = A[0][:]
                row = rng.randrange(k)
                edits = [(row, rng.randrange(k)) for _ in range(m)]
                is_zero = all(determinant(pencil(A, edits, z)) == 0
                              for z in itertools.product((Q(0), Q(1)), repeat=m))
                has_common_kernel = common_kernel(A, edits)
                assert is_zero == has_common_kernel, (k, m, trial, A, edits)
                tested += 1
                if is_zero:
                    zero_pencils += 1
                    # Matching on baseline-entry support only; not a symbolic Hall test.
                    if all(any(A[i][j] for j in range(k)) for i in range(k)):
                        matching_present_zero += 1
    # Five-port witness where Hall deficiency holds but no constant kernel exists.
    n = 5
    W = [[Q(0) for _ in range(n)] for _ in range(n)]
    for u, v in [(0,1),(0,2),(2,0),(2,1),(3,0),(4,0)]:
        W[u][v] = Q(1,8)
    main_edit = (1,4)
    other_edits = [(3,0),(4,0),(2,1),(2,2)]
    M0 = M_at(W, [], [])
    cert = certificate(M0, 3, 0, main_edit, other_edits)
    assert cert == {'endpoint_excluded':False,'right':False,'left':False,'matching':False}
    comparisons = 0
    for z in itertools.product((Q(0), Q(1,16)), repeat=4):
        old = cofactor_ab(M_at(W, [main_edit]+other_edits, [Q(0)]+list(z)), 3,0)
        new = cofactor_ab(M_at(W, [main_edit]+other_edits, [Q(1,8)]+list(z)), 3,0)
        expect = (Q(1,8)+z[0]) * (1-z[3])
        assert old == new == expect
        assert determinant(M_at(W, [main_edit]+other_edits, [Q(0)]+list(z))) > 0
        assert determinant(M_at(W, [main_edit]+other_edits, [Q(1,8)]+list(z))) > 0
        comparisons += 1
    return {'schema':'EM_R284X_EXACT_CHECK_V1','status':'PASS',
            'arithmetic':'Fraction exact elimination, deterministic finite tests',
            'seed':28424,'aligned_matrix_pencil_cases':tested,
            'identically_zero_aligned_pencils':zero_pencils,
            'baseline_fully_nonzero_row_zero_pencils':matching_present_zero,
            'five_port_hall_deficit_no_constant_kernel':True,
            'five_port_exact_x_pair_comparisons':comparisons,
            'five_port_observer':'F_30','main_edit':'1->4',
            'other_edits':['3->0','4->0','2->1','2->2'],
            'five_port_numerator':'(1/8+z1)*(1-z4)',
            'scope':'Finite tests corroborate the separately proved aligned-row theorem; no native X6 claims.'}


if __name__ == '__main__':
    print(json.dumps(main(),indent=2,sort_keys=True,ensure_ascii=False))
