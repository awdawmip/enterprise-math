#!/usr/bin/env python3
"""Exact author checks for D25 middle-rank reciprocal second-order defects.

Only Python stdlib. Rational checks validate the canonical factorial lift;
mod-p checks validate the stated finite-field port. Neither is a native
crystalline/CM run nor a theorem-admission/reviewer certificate.
"""
from fractions import Fraction
from math import comb, factorial


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


def rational_case(m):
    L, U = m + 1, 2 * m
    a = {
        j: Fraction((-1) ** (m+j+1) * factorial(m) * factorial(j-m-1)
                    * factorial(2*m), factorial(2*m-j) * factorial(j)**2)
        for j in range(L, U + 1)
    }
    h = {
        k: Fraction(2 * factorial(m) * factorial(2*m) * factorial(k-1)**2,
                    factorial(k+m) * factorial(k+2*m))
        for k in range(1, U + 1)
    }
    v = {j: a[j] / 2**j for j in a}
    g = {k: 2**k * h[k] for k in h}
    for n in range(U + 3):
        Mv = 2*n*n*v.get(n, 0) - (n-1-m)*(n-1-2*m)*v.get(n-1, 0)
        Ng = (n+m)*(n+2*m)*g.get(n, 0) - 2*(n-1)**2*g.get(n-1, 0)
        assert Mv == (2*L*L*v[L] if n == L else 0), (m,n,"M")
        assert Ng == (4 if n == 1 else -2*U*U*g[U] if n == U+1 else 0), (m,n,"N")
    assert sum((3*j-2*m)*a[j] for j in a) == comb(2*m,m)
    assert (3*m*sum(k*h[k] for k in h) + 2*m*m*sum(h.values())
            == 2 - U*U*h[U])
    return True


def finite_field_case(p):
    assert is_prime(p) and p % 6 == 1
    m = (p-1)//6
    L, U = m+1, 2*m
    fac = [1]*p
    for n in range(1,p):
        fac[n] = fac[n-1]*n % p
    def div(n,d):
        assert d % p
        return n*pow(d, p-2, p)%p
    a = {}
    h = {}
    for j in range(L,U+1):
        a[j] = div((-1)**(m+j+1)*fac[m]*fac[j-m-1]*fac[2*m],
                   fac[2*m-j]*fac[j]*fac[j])
    for k in range(1,U+1):
        h[k] = div(2*fac[m]*fac[2*m]*fac[k-1]*fac[k-1],
                   fac[k+m]*fac[k+2*m])
    v = {j: div(a[j],pow(2,j,p)) for j in a}
    g = {k: pow(2,k,p)*h[k]%p for k in h}
    for n in range(U+3):
        Mv = (2*n*n*v.get(n,0) - (n-1-m)*(n-1-2*m)*v.get(n-1,0))%p
        Ng = ((n+m)*(n+2*m)*g.get(n,0) - 2*(n-1)**2*g.get(n-1,0))%p
        assert Mv == (2*L*L*v[L]%p if n == L else 0), (p,n,"M")
        assert Ng == (4%p if n == 1 else (-2*U*U*g[U])%p if n == U+1 else 0), (p,n,"N")
    assert sum((3*j-2*m)*a[j] for j in a)%p == comb(2*m,m)%p
    assert (3*m*sum(k*h[k] for k in h) + 2*m*m*sum(h.values())
            - 2 + U*U*h[U])%p == 0
    return True


def main():
    for m in range(1,31):
        rational_case(m)
    primes = [p for p in range(7,998) if p%6==1 and is_prime(p)]
    for p in primes:
        finite_field_case(p)
    print(f"PASS rational_lifts=30, finite_field_primes={len(primes)}, range=7..997")


if __name__ == "__main__":
    main()
