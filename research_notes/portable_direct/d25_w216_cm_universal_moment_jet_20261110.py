#!/usr/bin/env python3
"""Exact W216 CM moment-jet validation; no floats or external dependencies.

Original W216 factorial-ratio coefficients, independent terminating CM polynomial
and rational/local Gauss ODE recurrence are intentionally separate paths.
AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.
"""
from fractions import Fraction
from math import comb, isqrt


def isprime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def universal_jet(jmax):
    h = [Fraction(0), Fraction(1)]
    for n in range(jmax - 1):
        h.append((-(n + 1)*h[n + 1]
                  + (4*n*n + 2*n + Fraction(2, 9))*h[n])
                 / ((n + 2)*(n + 1)))
    alpha = [Fraction(0), Fraction(0)]
    for j in range(2, jmax + 1):
        coeff = sum((h[a]*h[j-a] for a in range(1, j)), Fraction(0))
        alpha.append(coeff / Fraction(2**(j-2)))
    return h, alpha


def modrat(x, p):
    return x.numerator * pow(x.denominator, -1, p) % p


def check_first_jets(p, jmax=8):
    assert p >= 13 and p % 24 in (13, 19)
    m = (p-1)//6
    z = pow(2, -1, p)
    hb = [comb(m, k)*comb(2*m, k) % p for k in range(m+1)]
    H = sum(c*pow(z, k, p) for k, c in enumerate(hb)) % p
    Hp = sum(k*c*pow(z, k-1, p) for k, c in enumerate(hb) if k) % p
    assert H == 0 and Hp != 0, (p, H, Hp)

    # Original binomial A: (2k+1)(3k+1)(3k+2)/[36(k+1)^3].
    A = 1
    moments = [0]*(jmax+1)
    for k in range(p):
        for j in range(min(k, jmax)+1):
            moments[j] = (moments[j] + comb(k, j)*A) % p
        if k+1 < p:
            A = (A*(2*k+1)*(3*k+1)*(3*k+2)
                 *pow(36*(k+1)**3, -1, p)) % p
    assert moments[0] == moments[1] == 0
    assert moments[2] == Hp*Hp*pow(4, -1, p) % p
    _, alpha = universal_jet(jmax)
    for j in range(2, jmax+1):
        assert moments[j] == moments[2]*modrat(alpha[j], p) % p, (p, j)
    return moments


def check_full_array(p):
    """Independent Pascal/Newton array and modular (not Fraction) ODE."""
    assert p >= 13 and p % 24 in (13, 19)
    A = 1
    moments = [0]*p
    row = [1]
    for k in range(p):
        for j, b in enumerate(row):
            moments[j] = (moments[j] + b*A) % p
        if k+1 < p:
            A = A*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3, -1, p) % p
            row = [1]+[(row[j-1]+row[j]) % p for j in range(1, len(row))]+[1]
    h = [0, 1]
    for n in range(p-2):
        f = (4*n*n+2*n+2*pow(9, -1, p)) % p
        h.append((-(n+1)*h[n+1] + f*h[n])*pow((n+2)*(n+1), -1, p) % p)
    assert len(h) == p
    assert moments[0] == moments[1] == 0 and moments[2] != 0
    m2 = moments[2]
    for j in range(2, p):
        cj = sum(h[a]*h[j-a] for a in range(1, j)) % p
        alpha = cj*pow(pow(2, -1, p), j-2, p) % p
        assert moments[j] == m2*alpha % p, (p, j)
    m = (p-1)//6
    assert all(value == 0 for value in moments[2*m+1:])
    return len(moments)


def main():
    _, alpha = universal_jet(8)
    for j in range(2, 9):
        print('alpha', j, '=', alpha[j])
    target = [p for p in range(13, 2001) if isprime(p) and p % 24 in (13, 19)]
    for p in target:
        M = check_first_jets(p)
        if p in (13, 19, 37, 43, 373, 997):
            print('witness', p, 'M2-M6', M[2:7])
    assert len(target) == 77
    print('PASS', len(target), 'target primes;', len(target)*7, 'j=2..8 checks')
    for p in (13, 19, 37, 43, 61, 109, 373):
        print('FULL_PASS', p, check_full_array(p), 'moment indices')


if __name__ == '__main__':
    main()
