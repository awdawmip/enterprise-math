"""Exact X0(6) -> Fricke 3+/2+ two-leg Gauss correspondence checker.
Author-side symbolic checks; requires sympy, not a native p373 benchmark.
"""
from math import comb
import sympy as S

x = S.symbols('x')
s = S.sqrt(2)


def truncated_eta_quotient(exponents, cutoff=12):
    coefficients = [1] + [0] * cutoff
    for delta, power in exponents.items():
        for n in range(delta, cutoff + 1, delta):
            factor = [0] * (cutoff + 1)
            for k in range(cutoff // n + 1):
                factor[k*n] = ((-1)**k * comb(power, k)
                               if power >= 0 else comb(-power+k-1, k))
            out = [0] * (cutoff + 1)
            for i, a in enumerate(coefficients):
                for j in range(cutoff+1-i):
                    out[i+j] += a*factor[j]
            coefficients = out
    return coefficients


def laurent(coefficients):
    return sum(a * x**(i-1) for i, a in enumerate(coefficients))


T = laurent(truncated_eta_quotient({1: 5, 2: -1, 3: 1, 6: -5}))
H2 = laurent(truncated_eta_quotient({1: 24, 2: -24}))
H3 = laurent(truncated_eta_quotient({1: 12, 3: -12}))
assert S.series((T+9)**3 * H2 - T**3 * (T+8), x, 0, 4).removeO() == 0
assert S.series((T+8)**2 * H3 - T**2 * (T+9), x, 0, 3).removeO() == 0

t = S.symbols('t')
h2 = t**3*(t+8)/(t+9)**3
h3 = t**2*(t+9)/(t+8)**2
z = S.factor(108*h3/(h3+27)**2)
w = S.factor(256*h2/(h2+64)**2)
assert S.cancel(z - 108*t**2*(t+9)*(t+8)**2/(t+12)**6) == 0
assert S.cancel(w - 256*t**3*(t+8)*(t+9)**3/(t*t+36*t+216)**4) == 0

nza = 108*t**2*(t+9)*(t+8)**2
dza = (t+12)**6
nwb = 256*t**3*(t+8)*(t+9)**3
dwb = (t*t+36*t+216)**4
P = S.Poly(2*nza-dza,t)
Q = S.Poly(9*nwb-dwb,t)
assert S.gcd(P,Q) == S.Poly(t*t-72,t)
for u in [6*s,-6*s]:
    assert S.simplify(z.subs(t,u)-S.Rational(1,2)) == 0
    assert S.simplify(w.subs(t,u)-S.Rational(1,9)) == 0
    assert S.simplify((S.diff(z,t)/S.diff(w,t)).subs(t,u)-u*S.Rational(9,32)) == 0


def pullback(a,b,X):
    Px = (1-(a+b+1)*X)/(X*(1-X))
    Qx = -a*b/(X*(1-X))
    deriv = S.diff(X,t)
    return (S.factor(Px*deriv - S.diff(deriv,t)/deriv),
            S.factor(Qx*deriv**2))


pa,qa = pullback(S.Rational(1,6), S.Rational(1,3), z)
pb,qb = pullback(S.Rational(1,8), S.Rational(3,8), w)
d = S.factor((pb-pa)/2)
assert S.factor(d - 6*t/((t+12)*(t*t+36*t+216))) == 0
assert S.factor(qb - (S.diff(d,t)+d*d+pa*d+qa)) == 0
# The t=infinity germ is normalized. Elliptic crossings need connection data.
assert S.simplify(((t+12)**2/(t*t+36*t+216)).subs(t,6*s)-s/2) == 0
print('PASS: eta quotients, exact degree (6,8) maps, unique shared special fiber t^2=72, Gauss gauge/jet')
