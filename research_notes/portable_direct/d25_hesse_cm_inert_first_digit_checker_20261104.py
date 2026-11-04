#!/usr/bin/env python3
"""Exact finite-field checks of the D25 sextic-to-Hesse CM bridge.
Author-side portable checker; not the native fixed-373 H0/B0 experiment.
"""
from math import comb


def prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def pair_add(a, b, p):
    return ((a[0]+b[0]) % p, (a[1]+b[1]) % p)


def pair_mul(a, b, p):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % p,
            (a[0]*b[1] + a[1]*b[0]) % p)


def pair_pow(a, n, p):
    v = (1, 0)
    while n:
        if n & 1:
            v = pair_mul(v, a, p)
        a = pair_mul(a, a, p)
        n //= 2
    return v


def pair_inv(a, p):
    den = (a[0]*a[0] - 2*a[1]*a[1]) % p
    v = pow(den, -1, p)
    return ((a[0]*v) % p, (-a[1]*v) % p)


def eval_hesse(p):
    assert p % 6 == 1
    r = (p-1)//6
    half = pow(2, -1, p)
    quarter = pow(4, -1, p)
    z = (2*quarter % p, quarter)
    minus_z = (-z[0], -z[1])
    assert pair_mul((4, 0), pair_mul(z, pair_add((1, 0), minus_z, p), p), p) == (half, 0)

    # Hesse Hasse polynomial, H(z) = sum (3k)!/(27^k k!^3) z^k.
    H, coeff, power = (0, 0), 1, (1, 0)
    for k in range(2*r+1):
        H = pair_add(H, pair_mul((coeff, 0), power, p), p)
        if k < 2*r:
            coeff = (coeff*(3*k+1)*(3*k+2)*(3*k+3) *
                     pow(27*(k+1)**3, -1, p)) % p
            power = pair_mul(power, z, p)

    # Finite quadratic transform and pre-existing Clausen square.
    F, Fx, term = 0, 0, 1
    for k in range(r+1):
        F = (F+term) % p
        Fx = (Fx+k*term) % p
        if k < r:
            term = (term*(r-k)*(2*r-k)*half *
                    pow((k+1)**2, -1, p)) % p

    # Direct 216 original source, with its first moment retained.
    A, M, a = 0, 0, 1
    for k in range(2*r+1):
        A = (A+a) % p
        M = (M+k*a) % p
        if k < 2*r:
            a = (a*(2*k+1)*(3*k+1)*(3*k+2) *
                 pow(36*(k+1)**3, -1, p)) % p

    j = pair_mul((27, 0), pair_mul(
        pair_pow(pair_add((1, 0), pair_mul((8, 0), z, p), p), 3, p),
        pair_inv(pair_mul(z, pair_pow(pair_add((1, 0), minus_z, p), 3, p), p), p),
        p), p)
    assert j == (2417472 % p, 1707264 % p), (p, j)
    hilbert = pair_add(pair_add(pair_mul(j, j, p),
        pair_mul((-4834944, 0), j, p), p), (14670139392 % p, 0), p)
    assert hilbert == (0, 0), (p, hilbert)
    assert H == (F, 0), (p, H, F)
    assert A == F*F % p, (p, A, F)
    assert M == 2*F*Fx % p, (p, M, F, Fx)
    return {'p': p, 'F': F, 'H': H, 'A': A, 'M': M, 'j': j}


def test_polynomial_transform(p):
    r = (p-1)//6
    left = [0]*(2*r+1)
    for k in range(r+1):
        c = comb(r,k)*comb(2*r,k)*4**k % p
        for ell in range(k+1):
            left[k+ell] = (left[k+ell] + c*comb(k,ell)*(-1)**ell) % p
    right = [comb(2*r,k)*comb(4*r,k) % p for k in range(2*r+1)]
    assert left == right, (p, left, right)


def main():
    total = inert = split = extra = 0
    probes = []
    for p in range(7, 10001):
        if not prime(p) or p % 6 != 1:
            continue
        data = eval_hesse(p)
        is_inert = p % 24 in (13,19)
        assert (data['F'] == 0) == is_inert, data
        assert (data['A'] == 0) == is_inert, data
        if is_inert:
            assert data['M'] == 0, data
            inert += 1
        else:
            split += 1
        total += 1
        if p <= 211:
            test_polynomial_transform(p)
            extra += 1
        if p in (7,13,19,31,37,43,97,373):
            probes.append(data)
    print(f'eligible_primes_7_to_10000={total}; inert_zero={inert}; '
          f'split_nonzero={split}; polynomial_transform_extra={extra}; failures=0')
    for d in probes:
        print(d)


if __name__ == '__main__':
    main()
