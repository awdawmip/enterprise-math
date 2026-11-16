#!/usr/bin/env python3
"""Exact reproducible R228: reversible state-dependent reset source ideal spectra.
Python 3 standard library only; no floating point or network use.
"""
from fractions import Fraction as F
from math import comb, factorial
import json


def stirling2(n, r):
    rows = [1]
    for h in range(1, n + 1):
        nxt = [0] * (h + 1)
        for j in range(1, h + 1):
            nxt[j] = j * (rows[j] if j < len(rows) else 0) + rows[j - 1]
        rows = nxt
    return rows[r] if r < len(rows) else 0


def weights(m, k, L):
    return [factorial(r) * m**L *
            sum(stirling2(L + 1, j + 1) for j in range(min(r, L) + 1))
            for r in range(k + 1)]


def stationary(pi, alpha):
    v = [pi[i] / (1 - alpha[i]) for i in range(len(pi))]
    z = sum(v)
    return [x / z for x in v]


def exact_moments(pi, alpha, m, L, max_n):
    """Killed-submatrix formula for n=1,...,max_n, exact rationals."""
    k = len(pi) - 1
    rho = stationary(pi, alpha)
    W = weights(m, k, L)
    result = [F(0) for _ in range(max_n + 1)]
    for mask in range(1 << k):
        D = [0] + [j + 1 for j in range(k) if mask >> j & 1]
        v = [rho[i] for i in D]
        w = W[mask.bit_count()]
        for n in range(1, max_n + 1):
            result[n] += w * sum(v)
            s = sum(v[j] * (1 - alpha[D[j]]) for j in range(len(D)))
            v = [v[j] * alpha[D[j]] + s * pi[D[j]] for j in range(len(D))]
    return result


def direct_moments(pi, alpha, m, L, max_n):
    """Independent DP on (current label, cumulative support) with 2^k masks."""
    k = len(pi) - 1
    rho = stationary(pi, alpha)
    W = weights(m, k, L)
    T = [sum(comb(k - r, s - r) * W[s] for s in range(r, k + 1))
         for r in range(k + 1)]
    dist = {(i, 0 if i == 0 else 1 << (i - 1)): rho[i] for i in range(k + 1)}
    result = [F(0) for _ in range(max_n + 1)]
    for n in range(1, max_n + 1):
        result[n] = sum(pr * T[mask.bit_count()] for (_, mask), pr in dist.items())
        if n == max_n:
            break
        new = {}
        for (i, mask), pr in dist.items():
            for j in range(k + 1):
                pij = (alpha[i] if i == j else 0) + (1 - alpha[i]) * pi[j]
                next_mask = mask if j == 0 else mask | (1 << (j - 1))
                key = (j, next_mask)
                new[key] = new.get(key, F(0)) + pr * pij
        dist = new
    return result


def mod_fraction(x, p):
    return x.numerator % p * pow(x.denominator % p, -1, p) % p


def modular_moments(pi, alpha, m, L, max_n, p):
    k = len(pi) - 1
    rho = stationary(pi, alpha)
    a = [mod_fraction(v, p) for v in alpha]
    q = [mod_fraction(v, p) for v in pi]
    r = [mod_fraction(v, p) for v in rho]
    W = weights(m, k, L)
    f = [0] * (max_n + 1)
    for mask in range(1 << k):
        D = [0] + [j + 1 for j in range(k) if mask >> j & 1]
        v = [r[i] for i in D]
        w = W[mask.bit_count()] % p
        for n in range(1, max_n + 1):
            f[n] = (f[n] + w * sum(v)) % p
            s = sum(v[j] * (1 - a[D[j]]) for j in range(len(D))) % p
            v = [(v[j] * a[D[j]] + s * q[D[j]]) % p
                 for j in range(len(D))]
    return f


def hankel_rank_det(f, L, degree, p):
    """Row elimination in F_p, returning (rank, determinant)."""
    A = [f[L + i:L + i + degree].copy() for i in range(degree)]
    det, rank = 1, 0
    for j in range(degree):
        piv = next((i for i in range(j, degree) if A[i][j]), None)
        if piv is None:
            return rank, 0
        if piv != j:
            A[j], A[piv] = A[piv], A[j]
            det = -det % p
        v = A[j]
        t = v[j]
        det = det * t % p
        inv = pow(t, -1, p)
        for i in range(j + 1, degree):
            row = A[i]
            if row[j] == 0:
                continue
            factor = row[j] * inv % p
            row[j] = 0
            for c in range(j + 1, degree):
                row[c] = (row[c] - factor * v[c]) % p
        rank += 1
    return rank, det


def run():
    checks = 0
    small_configs = 0
    for k in (1, 2, 3):
        for L in (1, 2):
            for m in (1, 12):
                for scale in (10, 16):
                    alpha = [F(i + 1, scale) for i in range(k + 1)]
                    pi = [F(i + 1, (k + 1) * (k + 2) // 2)
                          for i in range(k + 1)]
                    end = max(L, 2) + 4
                    e = exact_moments(pi, alpha, m, L, end)
                    d = direct_moments(pi, alpha, m, L, end)
                    for n in range(max(1, L), end + 1):
                        assert e[n] == d[n], (k, L, m, scale, n)
                        checks += 1
                    for n in range(max(1, L), end - 2):
                        assert e[n] >= e[n + 1]
                        assert e[n] - 2 * e[n + 1] + e[n + 2] >= 0
                        checks += 2
                    small_configs += 1
    k, m, L = 6, 12, 2
    alpha = [F(i + 1, 20) for i in range(7)]
    pi = [F(i + 1, 28) for i in range(7)]
    rho = stationary(pi, alpha)
    W = weights(m, k, L)
    assert W == [144, 576, 1440, 4320, 17280, 86400, 518400]
    degree = (k + 2) * (1 << (k - 1)) - k
    assert degree == 250
    exact = exact_moments(pi, alpha, m, L, 6)
    assert exact[2] == F(10703531240028, 10002565)
    assert exact[3] == F(55145714582097, 56014364)
    primes = [1000000007, 1000000009]
    certs = []
    for p in primes:
        moments = modular_moments(pi, alpha, m, L, L + 2*degree - 2, p)
        for n in range(L, 7):
            assert moments[n] == mod_fraction(exact[n], p)
        rank, det = hankel_rank_det(moments, L, degree, p)
        assert rank == degree and det != 0
        certs.append({'prime': p, 'rank': rank, 'determinant_mod_prime': det})
    assert [x['determinant_mod_prime'] for x in certs] == [8827868, 569768765]
    return {
        'schema': 'EM_R228_EXACT_REPRODUCTION_V1',
        'status': 'PASS',
        'model': 'stationary reversible sticky-reset source chain',
        'parameters': {'k': k, 'm': m, 'L': L,
                       'alpha': [str(x) for x in alpha],
                       'pi': [str(x) for x in pi],
                       'rho': [str(x) for x in rho]},
        'degree_upper_bound': degree,
        'rational_hankel_full_rank': True,
        'modular_certificates': certs,
        'exact_moments': {str(n): str(exact[n]) for n in range(2, 7)},
        'finite_regression': {'configurations': small_configs,
                              'exact_equalities_and_difference_checks': checks,
                              'k_values': [1, 2, 3], 'L_values': [1, 2],
                              'm_values': [1, 12], 'alpha_scales': [10, 16]},
        'arithmetic': 'Python Fraction and modular integers, no floating point',
        'review': 'NOT_REVIEWED',
        'native_effect_histogram': 'NOT_EXECUTED'
    }


if __name__ == '__main__':
    outcome = run()
    output = __import__('pathlib').Path(__file__).with_name('R228_verification.json')
    output.write_text(json.dumps(outcome, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': outcome['status'],
                      'certificates': outcome['modular_certificates'],
                      'finite_checks': outcome['finite_regression']}, indent=2))
