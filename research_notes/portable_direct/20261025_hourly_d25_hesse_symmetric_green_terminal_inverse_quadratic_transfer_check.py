"""Author exact-Fraction checks for D25 symmetric Hesse Green inverse.

Finite checks are regressions, not theorem proofs or CM/divided-power experiments.
"""
from fractions import Fraction as Q
from math import factorial, gcd

PS = (13, 19, 37, 43, 61, 67, 211, 373)


def add(a, b):
    n = max(len(a), len(b))
    return [(a[j] if j < len(a) else 0) + (b[j] if j < len(b) else 0) for j in range(n)]


def mul_y(a):
    return [0] + a


def s_polynomials(n):
    s = [[Q(2)], [Q(1)]]
    for k in range(2, n + 1):
        left, right = s[-1], s[-2]
        neg = [-x for x in mul_y(right)]
        s.append(add(left, neg))
    return s[: n + 1]


def mod_fraction(fr, mod):
    fr = Q(fr)
    assert gcd(fr.denominator, mod) == 1, (fr, mod)
    return fr.numerator * pow(fr.denominator, -1, mod) % mod


def case(p):
    m, n = (p - 1) // 6, (p - 1) // 3
    c = [Q(factorial(3*k), 27**k * factorial(k)**3) for k in range(n+1)]
    s = s_polynomials(n)
    # Reconstruct even G from original coefficients and S_k(Y)=X^k+(1-X)^k.
    direct = [Q(0)] * (m+1)
    for k in range(n+1):
        for j in range(min(m, len(s[k])-1)+1):
            direct[j] += c[k]*s[k][j]/2
    C = Q(p+1, 9)*c[n]
    inv = [Q(0)] * (m+1)
    inv[m] = (-1)**m*c[n]
    for j in range(m-1, -1, -1):
        mu = Q((6*j+1)*(6*j+2), 9)
        inv[j] = (Q((j+1)**2)*inv[j+1] + Q(p, 2)*C*(s[n][j] if j < len(s[n]) else 0))/mu
    assert inv == direct, (p, "rational coefficient disagreement")
    h = Q(1)
    for j in range(m+1):
        if j:
            h *= Q(4*(6*(j-1)+1)*(3*(j-1)+1), 18*j*j)
        assert mod_fraction(inv[j], p) == mod_fraction(h, p), (p, j)
    y = Q(1, 8)
    v = sum(g*y**j for j, g in enumerate(inv))
    dv = sum(j*inv[j]*y**(j-1) for j in range(1, m+1))
    return {"p": p, "m": m, "g1_8_p2": mod_fraction(v, p*p), "gp1_8_p": mod_fraction(dv, p)}


if __name__ == "__main__":
    for p in PS:
        print(case(p))
