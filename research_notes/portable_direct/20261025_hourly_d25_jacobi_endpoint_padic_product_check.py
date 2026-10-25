#!/usr/bin/env python3
"""Exact p-local checks for the D25 Jacobi endpoint harmonic/Fermat jet.

This is an auxiliary finite-ring model, not a native CM experiment or review.
"""
from fractions import Fraction
from math import factorial


def primes_up_to(n):
    for p in range(7, n + 1):
        if all(p % d for d in range(2, int(p ** 0.5) + 1)):
            yield p


def case(p):
    assert p >= 7 and p % 6 == 1
    m = (p - 1) // 6
    mod = p ** 3
    fac = [1] * p
    for j in range(1, p):
        fac[j] = fac[j - 1] * j % mod

    # Independent original factorial route.
    w = (2 * (-1) ** m * fac[m] * fac[2 * m]
         * fac[5 * m - 1] * fac[4 * m - 1]
         * pow(fac[p - 1], -2, mod)) % mod
    idx = list(range(1, m + 2)) + list(range(1, 2 * m + 2))
    h1 = sum(pow(j, -1, mod) for j in idx) % mod
    h2 = sum(pow(j, -2, mod) for j in idx) % mod
    pref = 2 * pow((m + 1) * (2 * m + 1), -1, mod) % mod

    # Exact complementary-factorial finite product.
    prod = 1
    for j in idx:
        prod = prod * (1 - p * pow(j, -1, mod)) % mod
    w_product = pref * pow(prod, -1, mod) % mod

    # Taylor coefficients over p-local rational numbers.
    half = pow(2, -1, mod)
    w_jet = pref * (1 + p * h1 + p * p * ((h1*h1 + h2) * half)) % mod
    assert w == w_product == w_jet, (p, w, w_product, w_jet)

    k = -40 * m * m * w % mod
    endpoint = k * pow(2, -p, mod) % mod
    q2 = (pow(2, p - 1) - 1) // p
    a = (h1 - 27 * pow(10, -1, mod)) % mod
    b = ((h1*h1 + h2) * half
         - 27 * pow(10, -1, mod) * h1
         + 279 * pow(100, -1, mod)) % mod
    k_jet = (-4 * (1 + p * a + p*p * b)) % mod
    endpoint_jet = (-2 * (1 + p*(a - q2)
                         + p*p*(b - a*q2 + q2*q2))) % mod
    assert k == k_jet, (p, k, k_jet)
    assert endpoint == endpoint_jet, (p, endpoint, endpoint_jet)
    assert k % p == (-4) % p and endpoint % p == (-2) % p
    return (p, w % (p*p), k % (p*p), endpoint % (p*p),
            h1 % p, q2 % p)


def rational_check(p):
    m = (p - 1) // 6
    n = p - 1
    w = Fraction(2 * (-1)**m * factorial(m)*factorial(2*m)
                 * factorial(5*m-1)*factorial(4*m-1),
                 factorial(n)**2)
    product = Fraction(1)
    for j in list(range(1,m+2))+list(range(1,2*m+2)):
        product *= (1 - Fraction(p,j))
    assert w == Fraction(2, (m+1)*(2*m+1)) / product


if __name__ == "__main__":
    for p in [7, 13, 19]:
        rational_check(p)
    results = [case(p) for p in primes_up_to(373) if p % 6 == 1]
    results.extend([case(1327), case(19963)])
    print("PASS:", len(results), "primes, p-local mod p^3, three exact Q checks")
    for item in results:
        if item[0] in (7, 13, 19, 373, 1327, 19963):
            print("p,w(mod p^2),K(mod p^2),E(mod p^2),H1(mod p),q2(mod p) =", item)
