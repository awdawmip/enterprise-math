#!/usr/bin/env python3
"""C317 independent exact-integer/rational test of finite port-moment horizon theorem.

This is a typed auxiliary signed labelled rational-vector model; it does not
execute a native GF(2)-BRC model or validate C195/H168 input constants.
"""
from fractions import Fraction
from math import factorial, prod
import json


def rank_q(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    m, n = len(a), len(a[0])
    rank = 0
    for j in range(n):
        pos = next((i for i in range(rank, m) if a[i][j]), None)
        if pos is None:
            continue
        a[rank], a[pos] = a[pos], a[rank]
        lead = a[rank][j]
        a[rank] = [v / lead for v in a[rank]]
        for i in range(m):
            if i != rank and a[i][j]:
                scale = a[i][j]
                a[i] = [u - scale * v for u, v in zip(a[i], a[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def determinant_z(rows):
    n = len(rows)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in rows]
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[n - 1][n - 1]


def matrix(starts, h, q):
    return [[a**k - (a + h)**k for a in starts] for k in range(1, q + 1)]


def do_tests():
    rank_trials = det_trials = exact_horizon_trials = 0
    for r in range(1, 8):
        for h in range(1, 5):
            for base in (0, 7, 75):
                starts = [base + i * (h + 1) + i * i for i in range(r)]
                assert len(set(starts)) == r
                endpoints = [v for a in starts for v in (a, a + h)]
                assert len(set(endpoints)) == 2 * r
                full = matrix(starts, h, r)
                vandermonde = prod(starts[j] - starts[i] for i in range(r) for j in range(i + 1, r))
                expected = (-h)**r * factorial(r) * vandermonde
                assert determinant_z(full) == expected
                det_trials += 1
                for q in range(r + 4):
                    assert rank_q(matrix(starts, h, q)) == min(r, q)
                    rank_trials += 1
                for degree in range(4):
                    for steps in range(5):
                        q = degree * steps
                        assert rank_q(matrix(starts, h, q)) == min(r, q)
                        exact_horizon_trials += 1
    # C316 formal tagged residue channels: 75->77 and 76->78
    rows = matrix([75, 76], 2, 2)
    assert rows == [[-2, -2], [-304, -308]]
    assert determinant_z(rows) == 8
    # x = v1-v2 invisible to total and one affine label gain, visible at two steps.
    coeffs = (1, -1)
    moments = [sum((a**k - (a + 2)**k) * c for a, c in zip((75, 76), coeffs)) for k in (0, 1, 2)]
    assert moments == [0, 0, 4]
    reconstruction_trials = 0
    for a in range(-12, 13):
        for b in range(-12, 13):
            y1 = -2 * a - 2 * b
            y2 = -304 * a - 308 * b
            rec_a = Fraction(y2 - 154 * y1, 4)
            rec_b = Fraction(152 * y1 - y2, 4)
            assert (rec_a, rec_b) == (a, b)
            for p in ((1, 0), (0, 1), (3, -2), (-4, 5)):
                for z in ((1, 0), (0, 1), (2, 3)):
                    direct = (a * (p[0] + p[1] * 75) * (z[0] + z[1] * 75)
                              - a * (p[0] + p[1] * 77) * (z[0] + z[1] * 77)
                              + b * (p[0] + p[1] * 76) * (z[0] + z[1] * 76)
                              - b * (p[0] + p[1] * 78) * (z[0] + z[1] * 78))
                    reconstructed = (rec_a * (p[0] + p[1] * 75) * (z[0] + z[1] * 75)
                                      - rec_a * (p[0] + p[1] * 77) * (z[0] + z[1] * 77)
                                      + rec_b * (p[0] + p[1] * 76) * (z[0] + z[1] * 76)
                                      - rec_b * (p[0] + p[1] * 78) * (z[0] + z[1] * 78))
                    assert direct == reconstructed
                    reconstruction_trials += 1
    return {
        "research_unit": "C317_AUXILIARY_SIGNED_PORT_MOMENT_HORIZON",
        "arithmetic": "exact_integer_and_Fraction_only",
        "rank_trials": rank_trials,
        "determinant_trials": det_trials,
        "degree_steps_rank_trials": exact_horizon_trials,
        "two_step_reconstruction_trials": reconstruction_trials,
        "explicit_C316_pair_matrix": rows,
        "explicit_C316_pair_determinant": 8,
        "hidden_one_step_visible_two_step_moments": moments,
        "test_status": "PASS",
        "bounds": "finite tests corroborate a separately proved theorem; no native source/experiment or C195 physical claim"
    }


if __name__ == "__main__":
    print(json.dumps(do_tests(), indent=2, sort_keys=True))
