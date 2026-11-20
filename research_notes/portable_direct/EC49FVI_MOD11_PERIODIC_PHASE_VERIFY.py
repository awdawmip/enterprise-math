#!/usr/bin/env python3
"""EC49FVI: exact F_11 projective certificate for an infinite rational-phase lattice.

Python standard library only. Finite-field arithmetic is exact; independent
rational spot checks use fractions.Fraction.
"""
from fractions import Fraction
from pathlib import Path

P = 11
U = Fraction(4822040484, 8132285009)
GAMMA = Fraction(141024, 1653649)

def red(q):
    q = Fraction(q)
    assert q.denominator % P != 0
    return q.numerator * pow(q.denominator, -1, P) % P

u, g = red(U), red(GAMMA)
inv637 = pow(637, -1, P)
assert (u, g) == (4, 6)

# x, a, b, L_a, L_b; a=1-(1-x)*L_a, b=1-(1-x)*L_b.
rows = []
for x in range(P):
    L = (637 - 3*x)*inv637 % P
    M = u*(1+g*x) % P
    a = (1-(1-x)*L) % P
    b = (1-(1-x)*M) % P
    rows.append((x, a, b, L, M))
assert [x for x,a,b,L,M in rows if L == M] == [3]
assert rows[3] == (3, 10, 10, 10, 10)

c = red(Fraction(-3, 637))
d = u*g % P
assert (c, d) == (3, 2)

def projective_values(h, n):
    """Evaluate divided-difference G_{h,n} on all P^1(F_11)."""
    assert h > 0 and n > 0
    vals = []
    for x,a,b,L,M in rows:
        if L != M:
            vals.append(((pow(a,h,P)*pow(L,n,P)
                     - pow(b,h,P)*pow(M,n,P)) * pow((L-M)%P, -1, P))%P)
        else:
            # Derivative of F(L)=[1-(1-x)*L]^h * L^n.
            vals.append((pow(L,n-1,P)*pow(a,h-1,P)
                     *(n*a - h*(1-x)*L))%P)
    # Leading coefficient at degree 2h+n-1, including projective infinity.
    vals.append(((pow(c,h+n,P)-pow(d,h+n,P))
                 *pow((c-d)%P,-1,P))%P)
    return tuple(vals)

# Independently symbolic: G_1,2 = -3*x^3-5*x^2+x-5 mod 11.
seed = tuple((-3*x**3-5*x*x+x-5)%P for x in range(P)) + (8,)
assert projective_values(1,2) == seed
assert seed == (6,10,8,4,2,6,9,4,6,8,3,8)

# Exclude singular point x=3. Nonzero field powers depend only on mod-10 exponents.
allowed = {}
for h10 in range(10):
    good = []
    for n10 in range(10):
        h = h10 or 10
        n = n10 or 10
        values = projective_values(h,n)
        if all(values[j] for j in range(12) if j != 3):
            good.append(n10)
    allowed[h10] = tuple(good)
expected = {
    0:(1,3,7,9), 1:(2,3,4,7,8), 2:(1,3,5,6),
    3:(1,2,4,6,9), 4:(1,2,5,7), 5:(2,4,6,8),
    6:(3,5,8,9), 7:(1,4,6,8,9), 8:(4,5,7,9),
    9:(2,3,6,7,8),
}
assert allowed == expected
assert sum(map(len, allowed.values())) == 44

# CRT lifts: exponent mod-10 dependence plus derivative n+2h mod 11.
certified = []
for h in range(1,111):
    for n in range(1,111):
        predicted = n%10 in expected[h%10] and (n+2*h)%11 != 0
        observed = all(projective_values(h,n))
        assert predicted == observed, (h,n,predicted,observed)
        if observed:
            certified.append((h%110,n%110))
assert len(certified) == 4840

# Direct lifted-exponent observations.
for h,n in ((1,2),(1,112),(111,112),(221,332),(111,2)):
    if (h%110,n%110) in certified:
        assert projective_values(h,n) == projective_values(
            h%110 or 110, n%110 or 110)

# Exact rational checks (supplementary, not the proof).
for x in (Fraction(1,11),Fraction(7,20),Fraction(29,30)):
    A = x*(640-3*x)/637
    B = 1-U*(1-x)*(1+GAMMA*x)
    assert 0 < A < B < 1
    for h,n in ((1,2),(1,112),(111,112)):
        assert A**h*(1-A)**n != B**h*(1-B)**n

out = Path(__file__).with_name("EC49FVI_MOD11_4840_CLASSES.csv")
out.write_text("h_mod110,n_mod110\n"+''.join(
    f"{h},{n}\n" for h,n in certified), encoding="utf-8")
print("FIELD: F_11; singular x=3, a=L=10; infinity c=3,d=2")
print("BASE G_1,2: -3*x^3-5*x^2+x-5 mod 11")
print("BASE P^1 VALUES:", ','.join(map(str,seed)))
for h,ns in expected.items():
    print(f"h mod 10={h}: permitted n mod 10={list(ns)}")
print("NON-SINGULAR PATTERNS: 44/100")
print("PERIODIC PROJECTIVE CERTIFICATES: 4840/12100 positive exponent classes")
print("INFINITE PRIMITIVE FAMILY: h=1, n=2+110*j, j>=0")
print("ALL PASS")
