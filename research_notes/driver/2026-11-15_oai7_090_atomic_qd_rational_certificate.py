#!/usr/bin/env python3
"""Exact rational enclosure audit of q(n), d(n) for the 15 OAI7 roots.

No third-party dependencies. Uses the analytic factorization of the
exact trigonometric polynomial, NOT a rerun of check_certificate.py.
"""
from fractions import Fraction as F
from math import factorial

R = (0, 1, 3, 4, 7, 9, 12, 13, 16, 19, 21, 25, 27, 28, 31)
PI0 = F(314159265358979323846264338327950288419716939937510, 10**50)
PI1 = PI0 + F(1, 10**50)
SCALE = 10**10

def atan_partial(base, count=41):
    x = F(1, base)
    return sum(((-1)**j * x**(2*j+1) / (2*j+1)
                for j in range(count)), F(0))

a5, a239 = atan_partial(5), atan_partial(239)
e5, e239 = F(1, 5)**83/83, F(1, 239)**83/83
# Strict interval from the alternating arctangent series and Machin identity.
assert PI0 < 16*(a5-e5)-4*a239
assert 16*a5-4*(a239-e239) < PI1

def round_down(x):
    return F((x*SCALE).__floor__(), SCALE)

def round_up(x):
    return F((x*SCALE).__ceil__(), SCALE)

def trig_enclosure(k):
    # x0 = pi_lower*k/36; |true x - x0| <= delta.
    x = PI0*F(k, 36)
    delta = (PI1-PI0)*F(k, 36)
    s = sum(((-1)**j * x**(2*j+1)/factorial(2*j+1)
             for j in range(14)), F(0))
    c = sum(((-1)**j * x**(2*j)/factorial(2*j)
             for j in range(15)), F(0))
    # Alternating tail (decreasing from this order) plus Lipschitz-1 delta.
    es = x**29/factorial(29) + delta
    ec = x**30/factorial(30) + delta
    return ((round_down(s-es), round_up(s+es)),
            (round_down(c-ec), round_up(c+ec)))

TRIG = {k: trig_enclosure(k) for k in range(1, 32)}
assert all(TRIG[k][0][0] > 0 for k in TRIG)

def multiply(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)

def cot_enclosure(k):
    (sl, sh), (cl, ch) = TRIG[k]
    values = [c/s for c in (cl, ch) for s in (sl, sh)]
    return min(values), max(values)

def bound(n):
    qlo, qhi = (PI0/F(18))**2, (PI1/F(18))**2
    dlo = dhi = F(0)
    for r in R:
        if r == n:
            continue
        k = abs(n-r)
        (sl, sh), _ = TRIG[k]
        qlo *= 4*sl*sl
        qhi *= 4*sh*sh
        low, high = cot_enclosure(k)
        if n < r:
            low, high = -high, -low
        dlo += low
        dhi += high
    return (qlo, qhi), multiply((PI0/F(18), PI1/F(18)), (dlo, dhi))

bounds = {n: bound(n) for n in R}
assert min(q[0] for q, d in bounds.values()) > F(157, 1000)
assert max(q[1] for q, d in bounds.values()) < F(40)
assert max(max(abs(d[0]),abs(d[1])) for q, d in bounds.values()) < F(283, 100)
assert F(32467, 100000) < bounds[1][0][0] < bounds[1][0][1] < F(32469,100000)
assert F(3285, 10000) < bounds[1][1][0] < bounds[1][1][1] < F(3286,10000)

def six_decimal_bds(x):
    base = 10**6
    return str(F((x[0]*base).__floor__(),base)), str(F((x[1]*base).__ceil__(),base))

if __name__ == "__main__":
    for n, (q,d) in bounds.items():
        print(n, *six_decimal_bds(q), *six_decimal_bds(d))
    print("CERTIFIED: 0.157 < min Q, max Q < 40, max |D| < 2.83")
