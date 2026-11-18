#!/usr/bin/env python3
"""R284Y: exact rational coefficient/minor and nonnegative Port cut checks.
No external dependencies; deterministic and reproducible.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from random import Random
import json


def det(mat):
    n = len(mat)
    if n == 0:
        return Q(1)
    a = [[Q(x) for x in row] for row in mat]
    out = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        p = a[j][j]
        out *= p
        for i in range(j + 1, n):
            factor = a[i][j] / p
            for h in range(j + 1, n):
                a[i][h] -= factor * a[j][h]
    return out


def subdet(a, omit_rows, omit_cols):
    return det([[a[i][j] for j in range(len(a)) if j not in omit_cols]
                for i in range(len(a)) if i not in omit_rows])


def coefficient(a, edges, subset):
    # For A(z) = A0 + sum z_t E_(i_t,j_t), with zero-based indices.
    chosen = [edges[t] for t in subset]
    rr = [t[0] for t in chosen]
    cc = [t[1] for t in chosen]
    if len(rr) != len(set(rr)) or len(cc) != len(set(cc)):
        return Q(0)
    ordered = sorted(chosen)
    seq = [j for _, j in ordered]
    inversion_parity = sum(seq[i] > seq[j] for i in range(len(seq))
                           for j in range(i + 1, len(seq)))
    sign = -1 if (sum(rr) + sum(cc) + inversion_parity) % 2 else 1
    return sign * subdet(a, set(rr), set(cc))


def det_with_edits(a, edges, mask):
    out = [row[:] for row in a]
    for j, (r, c) in enumerate(edges):
        if (mask >> j) & 1:
            out[r][c] += 1
    return det(out)


def coefficients_via_mobius(a, edges):
    n = len(edges)
    vals = [det_with_edits(a, edges, s) for s in range(1 << n)]
    # The binary-cube Möbius transform is exact for multi-affine determinants.
    for bit in range(n):
        for mask in range(1 << n):
            if mask & (1 << bit):
                vals[mask] -= vals[mask ^ (1 << bit)]
    return vals


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def test_random():
    rng = Random(28419)
    count = coeff_count = nonmatching = 0
    for k in (2, 3, 4):
        for m in (1, 2, 3):
            for _ in range(80):
                a = [[Q(rng.randrange(-2, 3)) for _ in range(k)] for _ in range(k)]
                edges = [(rng.randrange(k), rng.randrange(k)) for _ in range(m)]
                observed = coefficients_via_mobius(a, edges)
                for mask, got in enumerate(observed):
                    S = [t for t in range(m) if mask & (1 << t)]
                    want = coefficient(a, edges, S)
                    assert got == want, (k, m, a, edges, S, got, want)
                    coeff_count += 1
                    if len({edges[t][0] for t in S}) != len(S) or len({edges[t][1] for t in S}) != len(S):
                        assert want == 0
                        nonmatching += 1
                count += 1
    return count, coeff_count, nonmatching


def test_abstract_witness():
    B = [[Q(t) for t in row] for row in (
        (1, 2, 3, 1),
        (1, 3, 1, 1),
        (1, 3, 1, 1),
        (2, 1, 2, 2),
    )]
    edges = [(0, 0), (1, 1)]
    cc = [str(coefficient(B, edges, subset)) for subset in ([], [0], [1], [0, 1])]
    assert cc == ['0'] * 4
    assert det([[B[i][j] for j in (0, 1, 2)] for i in (0, 1, 3)]) == -10
    assert all(x > 0 for row in B for x in row)
    assert [B[1][j] - B[2][j] for j in range(4)] == [Q(0)] * 4
    assert [B[i][0] - B[i][3] for i in range(4)] == [Q(0)] * 4
    assert det_with_edits(B, edges, 3) == 0
    # Unique left kernel (0,1,-1,0), destroyed by E22;
    # unique right kernel (1,0,0,-1), destroyed by E11.
    return {'coefficients': cc, 'rank3_minor': '-10', 'baseline_support_matching': True,
            'no_constant_left_or_right_kernel': True}


def make_W(x, z, t):
    # Six ports 0..5. Other rows are zero except target 5->3.
    W = [[Q(0) for _ in range(6)] for _ in range(6)]
    edges = {
        (0, 1): Q(1, 8), (1, 0): Q(1, 10),
        (0, 4): Q(1, 9), (0, 5): Q(1, 11) + z,
        (1, 4): Q(1, 13), (1, 5): Q(1, 17),
        (2, 0): Q(1, 12) + t, (2, 1): Q(1, 15),
        (3, 0): Q(1, 14), (3, 1): Q(1, 16),
        (2, 4): Q(1, 18), (2, 5): Q(1, 20),
        (3, 4): Q(1, 22), (3, 5): Q(1, 24),
        (5, 3): x,
    }
    for (i, j), value in edges.items():
        W[i][j] = value
    assert all(sum(row) < Q(1) for row in W)
    return W


def test_port_cut():
    cases = 0
    examples = []
    for z, t in product((Q(0), Q(1, 64)), repeat=2):
        W0 = make_W(Q(0), z, t)
        M = [[(Q(1) if i == j else Q(0)) - W0[i][j] for j in range(6)] for i in range(6)]
        # Observer F_{a=2,b=4}; target x on u=5,v=3.
        cofactor0 = subdet(M, {4}, {2})  # (-1)^(2+4)=+1
        W1 = make_W(Q(1, 64), z, t)
        M1 = [[(Q(1) if i == j else Q(0)) - W1[i][j] for j in range(6)] for i in range(6)]
        coeff_x = (subdet(M1, {4}, {2}) - cofactor0) * 64
        R, C, S, P, T = (0, 1, 2, 3), (0, 1, 4, 5), (0, 1), (2, 3), (4, 5)
        A = [[M[i][j] for j in C] for i in R]
        G = [[M[i][j] for j in S] for i in S]
        g00, g01 = G[0]
        g10, g11 = G[1]
        dG = g00*g11 - g01*g10
        Ginv = [[g11/dG, -g01/dG], [-g10/dG, g00/dG]]
        Wps = [[W0[i][j] for j in S] for i in P]
        Wsq = [[W0[i][j] for j in T] for i in S]
        Wpq = [[W0[i][j] for j in T] for i in P]
        gprod = mul(mul(Wps, Ginv), Wsq)
        Tr = [[Wpq[i][j] + gprod[i][j] for j in range(2)] for i in range(2)]
        dT = det(Tr)
        assert det(A) == dG * dT
        assert coeff_x == -det(A)
        assert det(M) > 0 and det(M1) > 0 and dG > 0
        cases += 1
        examples.append({'z':str(z), 't':str(t), 'transfer_det':str(dT), 'complement_det':str(det(A)), 'numerator_x_coeff':str(coeff_x)})
    return cases, examples


if __name__ == '__main__':
    cases, comparisons, nonmatch = test_random()
    example = test_abstract_witness()
    cut_count, port_details = test_port_cut()
    result = {
        'schema': 'R284Y_EXACT_CHECK_V1',
        'status': 'PASS',
        'seed': 28419,
        'arithmetic': 'Python fractions.Fraction exact rational',
        'random_pencils': cases,
        'exact_coefficients_checked': comparisons,
        'nonmatching_subset_zero_checks': nonmatch,
        'abstract_matching_present_witness': example,
        'six_port_transfer_cases': cut_count,
        'six_port_examples': port_details,
        'scope': 'Random checks corroborate; universal claims rest on symbolic determinant proofs',
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
