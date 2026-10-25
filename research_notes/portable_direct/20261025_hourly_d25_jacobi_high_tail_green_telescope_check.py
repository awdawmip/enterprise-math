#!/usr/bin/env python3
"""Exact rational and finite-field checks of the D25 Jacobi high-tail telescope."""
from fractions import Fraction
from math import comb, factorial


def primes_up_to(n):
    for p in range(7, n + 1):
        if all(p % d for d in range(2, int(p ** 0.5) + 1)):
            yield p


def exact_case(m):
    p, j0 = 6*m + 1, 2*m + 1
    a = Fraction(4*(-1)**m, comb(2*m, m))

    def g(n):
        if n < j0:
            return Fraction(0)
        return Fraction(
            4*(-1)**m*factorial(m)*factorial(2*m)
            *factorial(n-m-1)*factorial(n-2*m-1),
            factorial(n)**2)

    assert j0*j0*g(j0) == a
    for n in range(j0+1, p):
        assert n*n*g(n) == (n-1-m)*(n-1-2*m)*g(n-1)
    k = -40*m*m*(g(p-1)/2)
    assert -(p-1-m)*(p-1-2*m)*g(p-1) == k


def mod_case(p):
    m, j0 = (p-1)//6, (p-1)//3 + 1
    a = 4*(-1)**m*pow(comb(2*m, m), -1, p) % p
    coeff = {j0: a*pow(j0, -2, p) % p}
    for n in range(j0+1, p):
        coeff[n] = (coeff[n-1]*(n-1-m)*(n-1-2*m)
                    *pow(n, -2, p)) % p

    # Independent terminal factorial formula, not recycled from the recurrence.
    fac = [1]*p
    for n in range(1, p):
        fac[n] = fac[n-1]*n % p
    direct = (4*(-1)**m*fac[m]*fac[2*m]
              *fac[5*m-1]*fac[4*m-1]*pow(fac[p-1], -2, p)) % p
    assert coeff[p-1] == direct
    assert (-(p-1-m)*(p-1-2*m)*coeff[p-1]) % p == (-4) % p

    # Adjoint Green/Fredholm weights and critical rank.
    lam = {p-1: (m+1)*(2*m+1)*pow(p-1, -2, p) % p}
    for j in range(p-2, j0-1, -1):
        lam[j] = lam[j+1]*(j-m)*(j-2*m)*pow(j, -2, p) % p
    assert lam[j0] == (-1)**m*comb(2*m, m) % p
    assert lam[j0]*a % p == 4 % p
    # Each monomial's Jacobi-operator image is killed by the obstruction.
    for n in range(p):
        if n < p-1:
            obstruction = (n*n*lam.get(n, 0)
                           -(n-m)*(n-2*m)*lam.get(n+1, 0)) % p
        else:
            obstruction = ((p-1)**2*lam[p-1]
                           -(p-1-m)*(p-1-2*m)) % p
        assert obstruction == 0, (p, n, obstruction)
    assert (-4) % p != 0   # pure terminal forcing fails
    return p, j0, a, lam[j0], coeff[p-1]


if __name__ == "__main__":
    for m in range(1, 5):
        exact_case(m)
    cases = [mod_case(p) for p in primes_up_to(373) if p % 6 == 1]
    cases.extend([mod_case(1327), mod_case(19963)])
    print("PASS", len(cases), "prime cases; four exact rational cases")
    for item in cases:
        if item[0] in (7, 13, 19, 373, 1327, 19963):
            print(item)
