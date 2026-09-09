#!/usr/bin/env python3
"""Phase-A blind reduction checker for RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-REPLICATION.

This checker uses only the task-local blind inputs. It does not import any
withheld degree-6 map, target twist, symbolic replay, or period-scaling answer.
"""

import sympy as sp

R, t, w = sp.symbols("R t w")
I = sp.I
sqrt2 = sp.sqrt(2)
sqrt3 = sp.sqrt(3)
sqrt6 = sp.sqrt(6)
lam = 35 + 24 * sqrt2 - 20 * sqrt3 - 14 * sqrt6
k = -I * 3 ** sp.Rational(1, 4) * (sqrt6 - 2)
F = R**3 - 3 * R
h = (R + 2) * t

# 1. Field identities from the blind task input.
assert sp.simplify(k**2 - (12 * sqrt2 - 10 * sqrt3)) == 0
assert sp.simplify(lam - ((2 - sqrt3) * (sqrt3 - sqrt2)) ** 2) == 0
j = sp.simplify(256 * (1 - lam + lam**2) ** 3 / (lam**2 * (1 - lam) ** 2))
assert sp.simplify(j**2 - 4834944 * j + 14670139392) == 0

# 2. The principal differential is exactly phi=(t+k)dR/(w*t), so its zero
# divisor upstairs is the pullback of t=-k, provided the cubic is reduced.
disc = sp.factor(-4 * (-3) ** 3 - 27 * (-k**2) ** 2)  # discriminant of R^3-3R-k^2
assert sp.simplify(disc) != 0

# 3. The conjugate-ratio trial X=((t+k)/(t-k))^2 cannot satisfy the required
# square-class normalization for lambda*: it would force L/(R+2) to be square
# on C. A necessary condition is cancellation at both points R=-2, t=±i√2;
# the exact residues are nonzero.
L = sp.expand((1 - lam) * (F + k**2) + 2 * k * (1 + lam) * t)
res_plus = sp.simplify(L.subs({R: -2, t: I * sqrt2}))
res_minus = sp.simplify(L.subs({R: -2, t: -I * sqrt2}))
assert res_plus != 0
assert res_minus != 0

# 4. The natural U0=((t+k)/w)^2 always gives a degenerate genus-0 square family
# F(U0)=U0*(U0-A)^2; this verifies the recorded route boundary without claiming
# exclusion of all nondegenerate maps.
A = sp.symbols("A")
U0 = (t + k) ** 2 / h
sqrt_family = ((t + k) / w) * (U0 - A)
expr = sp.together(sqrt_family**2 - U0 * (U0 - A) ** 2)
num, _den = expr.as_numer_denom()
assert sp.factor(num.subs(w**2, h)) == 0

print("RB_CM24_BLIND_PHASE_A_REDUCTION_CHECK_PASS")
