"""Exact symbolic audit of the order-four optimized Chernoff expansion.

Run: python VERIFY.py
Requires sympy; algebra only, with rational coefficients (no floats).
This checks the algebra and derivative bounds, not analytic continuation itself.
"""
import sympy as S
s, v = S.symbols('s v', real=True)
k = s / (2 - s)
d1 = (1 - k) / S.Integer(6)
# delta_*(s,v) = d1*v + O(v**3), uniformly as v->0.
# Only d1 enters the order-v^4 coefficient by stationarity.
alpha = v + v**3 / 3
gamma = k*v + k**3*v**3 / 3
X = s / 2 * (1 - v**2 / 2 - v**4 / 8)
Y = (2 - s) / 2 * (1 - k**2*v**2 / 2 - k**4*v**4 / 8)
U, V = alpha*d1*v, -gamma*d1*v
Z = S.expand(X * (1+U+U**2/2) + Y * (1+V+V**2/2))
z2 = S.factor(Z.coeff(v, 2))
z4 = S.factor(Z.coeff(v, 4))
assert S.simplify(z2 + s/(2*(2-s))) == 0
assert S.simplify(z4 + s*(31*s*s-62*s+40)/(72*(2-s)**3)) == 0
# T = 1 - s + s*sqrt(1-v*v).
t2, t4 = -s/2, -s/8
f4 = S.factor((z4-z2**2/2) - (t4-t2**2/2)/(2-s))
expected_v4 = -s*(1-s)*(9*s*s-40*s+4)/(72*(2-s)**3)
assert S.simplify(f4-expected_v4) == 0
Qh = S.factor(16*f4/(s*(1-s)))
expected_Qh = -2*(9*s*s-40*s+4)/(9*(2-s)**3)
assert S.simplify(Qh-expected_Qh) == 0
qprime = S.factor(S.diff(Qh,s))
expected_prime = 2*(68+44*s-9*s*s)/(9*(2-s)**4)
assert S.simplify(qprime-expected_prime) == 0
assert Qh.subs(s,0)==-S.Rational(1,9)
assert Qh.subs(s,1)==6
assert S.solve(9*s*s-40*s+4,s)==[(20-2*S.sqrt(91))/9,(20+2*S.sqrt(91))/9]
assert S.simplify(Qh.subs(s,(20-2*S.sqrt(91))/9))==0
print('PASS_BRC_S23_UNIFORM_SMALL_CONTRAST_GLOBAL_UNIQUENESS_ALGEBRA_20261104')
print('coefficient_h4=',Qh)
print('derivative=',qprime)
print('endpoint_normalized=(-1/9, 6)')
print('derivative_lower_bound=17/18 for s in [0,1] (elementary interval bound)')
print('symbolic_arithmetic=sympy_exact; real_analyticity=proved_in_PROOF.md')
