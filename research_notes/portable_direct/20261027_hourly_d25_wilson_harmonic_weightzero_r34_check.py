#!/usr/bin/env python3
"""Author-only exact p-adic source certificate for D25 R34 (not native task execution)."""
from fractions import Fraction
from math import factorial, gcd


def primes_mod_19_24(bound=2000):
    for p in range(19, bound):
        if p % 24 != 19:
            continue
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            yield p


def frac_mod(a: Fraction, n: int):
    assert gcd(a.denominator, n) == 1
    return (a.numerator * pow(a.denominator, -1, n)) % n


def H(n, degree=1):
    return sum((Fraction(1, j**degree) for j in range(1, n + 1)), Fraction(0))


def verify(p):
    assert p % 24 == 19
    k = (3*p-1)//8
    r = (p-3)//8
    R = (p-1)//2
    assert 2*k == p-1-2*r and 3*k == p+r and 4*k == p+R
    q = (factorial(p-1)+1)//p
    A = H(r) + H(2*r)
    B = (A*A + H(2*r, 2) - H(r, 2))/2
    C = Fraction(factorial(r), 4*factorial(2*r)*factorial(k)**5*216**k)
    D = Fraction(factorial(R), factorial(k)**4*2304**k)
    e1 = 9+A-2*q
    e2 = B-2*q*A+q*q+9*(A-2*q)
    raw_w_div_p = Fraction((6*k+1)*factorial(2*k)*factorial(3*k)//p, factorial(k)**5*216**k)
    raw_s_div_p2 = Fraction((8*k+1)*factorial(4*k)//(p*p), factorial(k)**4*2304**k)
    w_formula = C*(1+p*e1+p*p*e2)
    s_formula = -3*D*(1+p*(H(R)-q))
    mod_w, mod_s = p**3, p**2
    assert frac_mod(raw_w_div_p,mod_w) == frac_mod(w_formula,mod_w), (p,'W')
    assert frac_mod(raw_s_div_p2,mod_s) == frac_mod(s_formula,mod_s), (p,'S')
    dif = raw_w_div_p - p*raw_s_div_p2
    dif_formula = w_formula + 3*p*D*(1+p*(H(R)-q))
    assert frac_mod(dif,p**3) == frac_mod(dif_formula,p**3), (p,'DIFF')
    assert frac_mod(C,p) != 0 and frac_mod(D,p) != 0
    return (p,k,r,frac_mod(raw_w_div_p, p**3),frac_mod(raw_s_div_p2,p**2),frac_mod(dif,p**3))

if __name__=='__main__':
    rows=[verify(p) for p in primes_mod_19_24()]
    print('PASS',len(rows),'primes p<2000, p=19 mod24; three exact assertions each')
    print('p k r W/p mod p^3 S/p^2 mod p^2 (W-S)/p mod p^3')
    for x in rows:
        if x[0] in (19,43,67,139,163,211,331,499):
            print(*x)
