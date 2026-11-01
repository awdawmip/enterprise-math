#!/usr/bin/env python3
"""Exact CM Frobenius and 2-primary torsion-tower checks for GH-120."""
from math import isqrt


def find_xy(p):
    for x in range(1, isqrt(p // 2) + 1):
        rem = p - 2 * x * x
        if rem > 0 and rem % 3 == 0:
            y = isqrt(rem // 3)
            if y > 0 and 3 * y * y == rem:
                return x, y
    raise ValueError(p)


def cm_mul(z, w):
    a, b = z
    c, d = w
    return a * c - 6 * b * d, a * d + b * c


def cm_pow(z, n):
    acc = (1, 0)
    while n:
        if n & 1:
            acc = cm_mul(acc, z)
        n >>= 1
        if n:
            z = cm_mul(z, z)
    return acc


def cm_norm(z):
    return z[0] * z[0] + 6 * z[1] * z[1]


def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def signed_frobenius(p):
    assert p >= 11 and p % 8 == 3
    if p % 24 == 19:
        return (p, 0), 'inert'
    x, y = find_xy(p)
    return (-(2 * x * x - 3 * y * y), 2 * x * y), 'split'


def expected_k(n):
    return 1 if n & 1 else v2(n) + 2


def check(p, max_degree=12):
    pi, kind = signed_frobenius(p)
    assert cm_norm(pi) == p * p
    observed = []
    for n in range(1, max_degree + 1):
        z = cm_pow(pi, n)
        w = (z[0] - 1, z[1])
        k = expected_k(n)
        factor = 1 << k
        assert w[0] % factor == w[1] % factor == 0
        quotient = (w[0] // factor, w[1] // factor)
        assert quotient[0] % 2 == 1
        assert cm_norm(quotient) % 2 == 1
        assert v2(cm_norm(w)) == 2 * k
        observed.append((n, k))
    return p, kind, observed


if __name__ == '__main__':
    for p in (11, 19, 43, 59, 83, 107, 347, 3347):
        p, kind, records = check(p)
        print('PASS_TOWER', p, kind, records)
    print('PASS_GH120_CM_2PRIMARY_ALL_EXTENSION_DEGREES')
