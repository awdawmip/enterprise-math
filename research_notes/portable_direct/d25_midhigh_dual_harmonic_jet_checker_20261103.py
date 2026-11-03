#!/usr/bin/env python3
"""Exact p-adic dual middle/high harmonic jet and p^4 H2 source check.

All arithmetic uses integers modulo p**2 after extracting the exact p-valuation
of original factorial coefficients; no floating point, model proxy or native H0/B0.
"""
from math import isqrt


def primes_up_to(limit):
    for n in range(7, limit + 1):
        if n % 6 != 1:
            continue
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def unit_factorial_table(p, maximum, modulus):
    table = [1] * (maximum + 1)
    for n in range(1, maximum + 1):
        x = n
        while x % p == 0:
            x //= p
        table[n] = table[n - 1] * x % modulus
    return table


def original_b_unit(k, p, modulus, factorial):
    val = 2 * k // p + 3 * k // p  # valid for k < p and 3k < p**2
    unit = factorial[2 * k] * factorial[3 * k] % modulus
    unit = unit * pow(factorial[k], -5, modulus) % modulus
    unit = unit * pow(216, -k, modulus) % modulus
    return val, unit


def check(p):
    r = (p - 1) // 6
    n = 3 * r
    mod = p * p
    chi = 1 if pow(6, (p - 1) // 2, p) == 1 else -1
    qp2 = ((pow(2, p - 1, p * p) - 1) // p) % p
    qp3 = ((pow(3, p - 1, p * p) - 1) // p) % p
    eps = (3 + (qp2 - 3 * qp3) * pow(2, -1, p)) % p
    factorial = unit_factorial_table(p, 3 * (4 * r + 1), mod)
    u = 1
    f = 1
    e = 0
    jjet = 0
    weighted_y_mod_p2 = 0
    h2_original = 0
    dual_adj_lhs = [0] * 5
    for s in range(r):
        if s:
            t = s
            d = t * (36 * t * t - 1)
            u = u * 9 * (2 * t - 1) ** 3 * pow(d, -1, mod) % mod
            f = f * d * pow(9 * (2 * t + 1) ** 3, -1, mod) % mod
            e = (e + pow(2 * t, -1, p) + 3 * pow(6 * t - 1, -1, p)
                 + 3 * pow(6 * t + 1, -1, p) - 3 * pow(2 * t - 1, -1, p)) % p
            jjet = (jjet + pow(2 * t, -1, p) + 3 * pow(6 * t - 1, -1, p)
                    + 3 * pow(6 * t + 1, -1, p) - 3 * pow(2 * t + 1, -1, p)) % p
        assert u * f % mod == pow(2 * s + 1, -3, mod), ('dual exact', p, s)
        j = n - s
        k = p - j
        v_x, x = original_b_unit(j, p, mod, factorial)
        v_y, y = original_b_unit(k, p, mod, factorial)
        assert (v_x, v_y) == (1, 2), ('valuations', p, j, k)
        x_pred = (-2 * chi * u * (1 + p * (eps + e))) % mod
        y_pred = (chi * pow(9, -1, mod) * f *
                  (1 + p * (eps - 3 + jjet))) % mod
        assert x == x_pred, ('middle', p, s, x, x_pred)
        assert y == y_pred, ('high', p, s, y, y_pred)
        product_pred = (-2 * pow(9 * (2 * s + 1) ** 3, -1, mod) *
                        (1 + p * (2 * eps - 3 + e + jjet))) % mod
        assert x * y % mod == product_pred, ('product direct', p, s)
        kappa = (2 * eps - 3 + e + jjet - 3 * pow(2 * s + 1, -1, p)) % p
        assert x * y % mod == (pow(36 * j ** 3, -1, mod) * (1 + p * kappa)) % mod, ('j-normalized', p, s)
        weighted_y_mod_p2 = (weighted_y_mod_p2 + (6 * k + 1) * y) % mod
        h2_original = (h2_original + (6 * k + 1) * y_pred) % mod
        t = s + 1
        A0 = t * (6 * t - 1) * (6 * t + 1) * pow(9, -1, mod) % mod
        D = ((108 * t * t + 4 * t - 1) * pow(18 * (2 * t + 1), -1, mod)) % mod
        kedge = n + t
        Ak = (2 * t + 1) ** 3 * (2 * kedge + 1) * (3 * kedge + 1) * (3 * kedge + 2)
        Ak = Ak * pow(36 * (kedge + 1) ** 3, -1, mod) % mod
        assert Ak == (A0 + p * D) % mod, ('adjoint coefficient', p, s)
        Ps = [1, s, s * s, s ** 3, 6 * s + 4]
        Pt = [1, t, t * t, t ** 3, 6 * t + 4]
        for i in range(5):
            Lp = ((A0 + p * D) * Pt[i] - (2 * s + 1) ** 3 * Ps[i]) % mod
            dual_adj_lhs[i] = (dual_adj_lhs[i] + Lp * y) % mod
    assert h2_original == weighted_y_mod_p2
    v_r, y_r_unit = original_b_unit(4 * r + 1, p, mod, factorial)
    assert v_r == 3, ('exit valuation', p)
    y_r = p * y_r_unit % mod
    f_last = f
    expected_y_r = p * chi * pow(18, -1, mod) * f_last % mod
    assert y_r == expected_y_r, ('exit high source', p)
    Pr = [1, r, r * r, r ** 3, 6 * r + 4]
    P0 = [1, 0, 0, 0, 4]
    Y0 = (chi * pow(9, -1, mod) * (1 + p * (eps - 3))) % mod
    for i in range(5):
        boundary = ((2 * r + 1) ** 3 * Pr[i] * y_r - P0[i] * Y0) % mod
        assert dual_adj_lhs[i] == boundary, ('lifted adjoint boundary', p, i, dual_adj_lhs[i], boundary)
    return {'p': p, 'r': r, 'chi': chi, 'epsilon': eps,
            'H2_over_p2_mod_p2': weighted_y_mod_p2, 'H2_mod_p4': (p * p * weighted_y_mod_p2) % p**4}


def main():
    sample = {}
    count = 0
    total = 0
    for p in primes_up_to(2000):
        result = check(p)
        count += 1
        total += result['r']
        if p in (7, 13, 19, 37, 373):
            sample[p] = result
    print('PASS', count, 'primes p=1 mod6 up to 2000;', total, 'paired original middle/high positions')
    for p, result in sample.items():
        print(result)

if __name__ == '__main__':
    main()
