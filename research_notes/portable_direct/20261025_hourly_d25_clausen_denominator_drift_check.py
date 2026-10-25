#!/usr/bin/env python3
"""Exact terminating Clausen and denominator correction test (author-only)."""
from fractions import Fraction
from math import factorial, gcd

PRIMES = (7, 13, 19, 31, 37, 43, 73, 103)

def poch(x, n):
    out = 1
    for j in range(n):
        out *= x + j
    return out

def residue(value, modulus):
    value = Fraction(value)
    assert gcd(value.denominator, modulus) == 1
    return value.numerator * pow(value.denominator, -1, modulus) % modulus

def verify(p):
    m = (p - 1) // 6
    assert 6 * m + 1 == p
    c = Fraction(1, 1) - Fraction(p, 2)
    a = [Fraction(poch(-m, n) * poch(-2*m, n),
                  poch(c,n) * factorial(n)) for n in range(m+1)]
    square = [sum((a[j] * a[k-j]
                   for j in range(max(0,k-m),min(m,k)+1)), Fraction(0))
              for k in range(2*m+1)]
    b = [Fraction(poch(-2*m,n)*poch(-3*m,n)*poch(-4*m,n),
                  poch(c,n)*poch(1-p,n)*factorial(n)) for n in range(2*m+1)]
    assert square == b, (p, "Clausen coefficient")
    for n in range(p):
        h = sum((Fraction(1,j) for j in range(1,n+1)), Fraction(0))
        h2 = sum((Fraction(1,j*j) for j in range(1,n+1)), Fraction(0))
        aa = Fraction(factorial(n), poch(c,n))
        cc = Fraction(factorial(n)**2,poch(c,n)*poch(1-p,n))
        aa_expected = 1 + Fraction(p,2)*h + Fraction(p*p,8)*(h*h+h2)
        cc_expected = 1 + Fraction(3*p,2)*h + Fraction(p*p,8)*(9*h*h+5*h2)
        assert residue(aa-aa_expected,p**3)==0,(p,n,"A")
        assert residue(cc-cc_expected,p**3)==0,(p,n,"C")
    assert residue(Fraction(2*m*m,c)-2*m*m,p*p) == p*m*m%(p*p)
    return p

if __name__ == "__main__":
    for p in PRIMES:
        print("PASS", verify(p))
    print(f"PASS {len(PRIMES)} primes, all specified exact rational and p-local tests")
