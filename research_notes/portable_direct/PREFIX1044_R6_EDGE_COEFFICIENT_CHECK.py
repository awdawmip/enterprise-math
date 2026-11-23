"""Exact scalar spectral edge coefficient checks for PREFIX-1044.

The recurrence samples are finite consistency checks, not a proof of a limit;
the edge asymptotic follows from the paper's Morse/coarea argument.
"""
from fractions import Fraction
import math
import sympy as s

pi = s.pi
Q = 6*s.eye(5) - s.ones(5)
assert Q.det() == 6**4
assert Q.eigenvals() == {s.Integer(1): 1, s.Integer(6): 4}

V5 = pi**s.Rational(5, 2)/s.gamma(s.Rational(7, 2))
tail_cdf = s.simplify(V5/((2*pi)**5 * s.sqrt(Q.det())))
rho_edge = s.simplify(s.Rational(5, 2)*tail_cdf)
g_edge = s.simplify(s.Rational(-18144 + 37512 - 6768, 5)*rho_edge)
collision_edge = s.simplify(rho_edge*36**s.Rational(5, 2)*s.gamma(s.Rational(5, 2)))
beta_k0 = s.simplify(g_edge*36**s.Rational(5, 2)*s.gamma(s.Rational(7, 2)))

assert tail_cdf == 1/(2160*pi**3)
assert rho_edge == 1/(864*pi**3)
assert g_edge == s.Rational(35,12)/pi**3
assert collision_edge == s.Rational(27,4)/pi**s.Rational(5,2)
assert beta_k0 == 42525/pi**s.Rational(5,2)
assert s.Rational(10368 - 6552 - 792, 5) == s.Rational(3024, 5)
assert s.Rational(3024*36, 5) == s.Rational(108864, 5)

# Inherited PREFIX-1035 integer recurrence: direct finite, exact crosscheck.
a = [1,6,66]
for r in range(2,201):
    numerator = (2*(2*r+1)*(14*r**4+28*r**3+28*r**2+14*r+3)*a[r]
                 -4*r**3*(196*r**2+59)*a[r-1]
                 +1152*(2*r-1)*r**2*(r-1)**2*a[r-2])
    quotient, remainder = divmod(numerator, (r+1)**5)
    assert remainder == 0
    a.append(quotient)

c = float(collision_edge.evalf(17))
for r in (25, 50, 100, 200):
    approx = float(Fraction(a[r], 36**r))*r**2.5
    print(f"r={r} scaled_A6={approx:.12f} theoretical={c:.12f}")
    assert abs(approx - c) < 0.01
print("PREFIX1044_EXACT_EDGE_COEFFICIENTS_PASSED")
