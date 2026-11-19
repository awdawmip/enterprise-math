#!/usr/bin/env python3
"""R284AQ: exact rational rank-one diagonal/non-diagonal Port observer checks.
Python 3 standard library. Prints reproducible JSON; no floating arithmetic.
"""
from fractions import Fraction as F
from itertools import permutations
import json
import random


def det(a):
    n = len(a)
    if n == 0:
        return F(1)
    a = [[F(x) for x in row] for row in a]
    sign = 1
    den = F(1)
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if j is None:
                return F(0)
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) / den
            a[i][k] = F(0)
        den = pivot
    return F(sign) * a[-1][-1]


def det_leibniz(a):
    n = len(a)
    total = F(0)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        v = F((-1) ** inversions)
        for i in range(n):
            v *= a[i][p[i]]
        total += v
    return total


def cmatrix(a, b):
    return [[a[i] * b[j] for j in range(len(b))] for i in range(len(a))]


def pencil(C, d, edge=None, s=0):
    n = len(C)
    out = [[(d[i] if i == j else F(0)) - C[i][j] for j in range(n)] for i in range(n)]
    if edge is not None:
        u, v = edge
        out[u][v] -= s
    return out


def diag_formula(a, b, d):
    n = len(a)
    return (F(1) if not d else __import__('math').prod(d)) - sum(
        a[i] * b[i] * __import__('math').prod(d[j] for j in range(n) if j != i)
        for i in range(n)
    )


def edge_formula(C, d, u, v, s):
    assert u != v
    from math import prod
    return -s * C[v][u] * prod(d[i] for i in range(len(d)) if i not in (u, v))


def run():
    rng = random.Random(28401711)
    total = 0
    direct_leibniz = 0
    diagonal = 0
    edge = 0
    gauge = 0
    recovered = 0
    for m in range(2, 7):
        for _ in range(20):
            a = [F(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(m)]
            b = [F(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(m)]
            scale = [F(rng.randint(1, 5), rng.randint(1, 5)) for _ in range(m)]
            aprime = [scale[i] * a[i] for i in range(m)]
            bprime = [b[i] / scale[i] for i in range(m)]
            C, Cprime = cmatrix(a, b), cmatrix(aprime, bprime)
            d = [F(rng.randint(1, 6)) for _ in range(m)]
            original = det(pencil(C, d))
            assert original == diag_formula(a, b, d)
            assert original == det(pencil(Cprime, d))
            diagonal += 1
            if m <= 4:
                assert original == det_leibniz(pencil(C, d))
                direct_leibniz += 1
            for u, v in ((0, 1), (m - 1, 0)):
                s = F(rng.randint(1, 5), rng.randint(1, 5))
                diff = det(pencil(C, d, (u, v), s)) - original
                assert diff == edge_formula(C, d, u, v, s)
                edge += 1
            # m-1 edges (0->1->...->m-1) suffice for reconstruction.
            c = [C[i][i] for i in range(m)]
            a_rec = [F(1)]
            for i in range(m - 1):
                measured = det(pencil(C, [F(1)] * m, (i, i + 1), 1)) - det(pencil(C, [F(1)] * m))
                assert measured == -C[i + 1][i]
                a_rec.append(a_rec[-1] * (-measured) / c[i])
            b_rec = [c[i] / a_rec[i] for i in range(m)]
            assert cmatrix(a_rec, b_rec) == C
            recovered += 1
            # Disconnected measurements: distinct component gauges preserve all probed coefficients.
            cut = m // 2
            two_scale = [F(2) if i < cut else F(3) for i in range(m)]
            a2 = [two_scale[i] * a[i] for i in range(m)]
            b2 = [b[i] / two_scale[i] for i in range(m)]
            C2 = cmatrix(a2, b2)
            assert C2 != C and [C2[i][i] for i in range(m)] == c
            assert det(pencil(C2, d)) == original
            for i in range(m - 1):
                if i == cut - 1:
                    continue
                assert C2[i + 1][i] == C[i + 1][i]
            gauge += 1
            total += 1
    # Explicit two-channel strictly positive substochastic pair.
    e = F(1, 100)
    C = [[e, 2 * e], [3 * e, 6 * e]]
    Cp = [[e, e], [6 * e, 6 * e]]
    assert max(sum(row) for row in C) < 1
    assert max(sum(row) for row in Cp) < 1
    D = [F(1), F(1)]
    assert det(pencil(C, D)) == det(pencil(Cp, D)) == F(93, 100)
    assert det(pencil(C, D, (1, 0), e)) - det(pencil(Cp, D, (1, 0), e)) == -e * e
    assert det(pencil(C, D, (1, 0), e)) == F(93, 100) - 2 * e * e
    assert det(pencil(Cp, D, (1, 0), e)) == F(93, 100) - e * e
    return {
        'record': 'R284AQ', 'arithmetic': 'exact Python Fraction', 'seed': 28401711,
        'cases': total, 'diagonal_identity_checks': diagonal,
        'independent_leibniz_checks': direct_leibniz,
        'off_diagonal_intervention_checks': edge,
        'connected_path_full_recovery_checks': recovered,
        'disconnected_gauge_ambiguity_checks': gauge,
        'explicit_positive_stable_example': {
            'epsilon': '1/100', 'C': [['1/100', '1/50'], ['3/100', '3/50']],
            'C_prime': [['1/100', '1/100'], ['3/50', '3/50']],
            'diagonal_response_at_I': '93/100', 'probe': 'E_21, s=1/100',
            'response_C': str(F(93, 100) - 2 * e * e),
            'response_C_prime': str(F(93, 100) - e * e),
            'difference': str(-e * e)
        }, 'status': 'PASS'
    }

if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
