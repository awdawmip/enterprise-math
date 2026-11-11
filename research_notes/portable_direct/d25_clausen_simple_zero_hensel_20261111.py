#!/usr/bin/env python3
"""Exact author-side regression for D25 Clausen simple-zero/Hensel theorem.

Finite exact checks, not a universal proof. No native H0/B0, no CLAIM.
"""
from math import comb

PRIMES = (13, 19, 37, 43, 109, 139, 157, 373)


def check(p: int):
    assert p % 24 in (13, 19)
    m = (p - 1) // 6
    modulus = p ** 4
    inv216 = pow(216, -1, modulus)
    a = 1
    original = []
    signed_sum = 0
    signed_derivative = 0
    for k in range(p):
        original.append(a)
        signed_sum = (signed_sum + (6*k+1)*a) % modulus
        signed_derivative = (signed_derivative + 2*k*(6*k+1)*a) % modulus
        if k + 1 < p:
            numerator = (2*k+1)*(2*k+2)*(3*k+1)*(3*k+2)*(3*k+3)
            a = a*numerator*inv216*pow(k+1, -5, modulus) % modulus
    # Independent original-binomial construction.
    independent = sum((6*k+1)*comb(2*k, k)**2*comb(3*k, k)
                      *pow(inv216, k, modulus) for k in range(p)) % modulus
    assert signed_sum == independent

    # c[k] is the 2F1 polynomial coefficient ALREADY evaluated at x=1/2.
    c = [1]
    for k in range(1, m+1):
        c.append(c[-1]*(6*k-5)*(3*k-2)*pow(36*k*k, -1, p) % p)
    f0 = sum(c) % p
    fprime = 2*sum(k*ck for k, ck in enumerate(c)) % p
    assert f0 == 0 and fprime != 0

    # Check all original unweighted Clausen square coefficients at x=1/2.
    conv = [0]*p
    for i, ci in enumerate(c):
        for j, cj in enumerate(c):
            conv[i+j] = (conv[i+j]+ci*cj) % p
    for k in range(p):
        assert conv[k] == original[k] % p, (p, k)

    slope = signed_derivative % p
    assert slope == 6*fprime*fprime % p and slope != 0
    assert signed_sum % p**3 == p
    third_digit = ((signed_sum-p)//p**3) % p
    root_delta_p3 = -third_digit*pow(slope, -1, p) % p
    return p, m, f0, fprime, slope, signed_sum, third_digit, root_delta_p3


def main():
    print("p,m,f0,fprime,slope,W_mod_p4,third_digit,root_delta_p3")
    for p in PRIMES:
        print(",".join(map(str, check(p))))
    assert check(373)[-1] == 181
    print("PASS: 8 prime cases, all coefficients of Clausen mod p,")
    print("two independent W mod p^4 algorithms, signed slope/Hensel.")


if __name__ == "__main__":
    main()
