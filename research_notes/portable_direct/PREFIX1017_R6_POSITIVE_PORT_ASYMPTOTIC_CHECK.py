"""PREFIX-1017: exact arithmetic checks of a BRC-derived terminal observer.

The scientific input is the frozen Stage46 candidate, via PREFIX-1016's
proved three-shift formula. This is *not* a replacement BRC trajectory.
Requires Python 3 and SymPy; no floating-point scientific computation.
"""
from math import comb
from fractions import Fraction
import sympy as sp

LIMIT = 300
A = [1] * (LIMIT + 4)
for d in range(2, 7):
    A = [sum(comb(n, k)**2 * A[n-k] for k in range(n+1))
         for n in range(LIMIT + 4)]

def delta(m):
    c1 = Fraction(-72*(72*m*m + 163*m + 80), 5*(m+1))
    c2 = Fraction(2*(144*m**3 + 1135*m*m + 2367*m + 1310),
                  5*(m+1)*(m+2))
    c3 = Fraction(-2*(m+8)*(2*m+5), 5*(m+2))
    z = c1*A[m+1] + c2*A[m+2] + c3*A[m+3]
    assert z.denominator == 1
    return z.numerator

t = sp.symbols("t")
a, b, g = sp.symbols("alpha beta gamma")
m = 1/t
c = [
    -sp.Rational(72, 5)*(72*m*m + 163*m + 80)/(m+1),
    sp.Rational(2, 5)*(144*m**3 + 1135*m*m + 2367*m + 1310)/((m+1)*(m+2)),
    -sp.Rational(2, 5)*(m+8)*(2*m+5)/(m+2),
]
series = 0
for s, coefficient in zip((1, 2, 3), c):
    asymptotic = 36**s * (1+s*t)**(-sp.Rational(5, 2))
    correction = (1 + a*t/(1+s*t) +
                  b*t**2/(1+s*t)**2 + g*t**3/(1+s*t)**3)
    series += coefficient * asymptotic * correction
series = sp.series(series, t, 0, 3).removeO()
expected = 226800*t + (sp.Rational(1178064, 5)*a - 2263140)*t*t
assert sp.simplify(series - expected) == 0
assert sp.simplify(series.subs(a, -sp.Rational(5,8))
                   - (226800*t - 2410398*t*t)) == 0
assert sp.Rational(226800,36**3) == sp.Rational(175,36)
assert (sp.Rational(-2410398,36**3)
        - sp.Rational(226800,36**3)*(-sp.Rational(5,8)-sp.Rational(15,2))
        == -sp.Rational(73,6))

values = [delta(m) for m in range(1, LIMIT+1)]
assert all(z > 0 for z in values)
assert [values[i-1] for i in [1,2,3,4,6]] == [
    25620, 386028, 7124592, 149251656, 81969197100
]
print("EXACT POSITIVE CHECKED: n=5..304")
print("SYMBOLIC COEFFICIENTS: 226800, -2410398")
for mm in (20,50,100,200,300):
    print(mm, str(Fraction(mm*delta(mm), A[mm+3])),
          "two-term", str(sp.Rational(175,36)-sp.Rational(73,6*mm)))
