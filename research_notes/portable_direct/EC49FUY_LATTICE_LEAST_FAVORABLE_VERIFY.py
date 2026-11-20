"""EC49FUY: exact rational dual and lattice-phase asymptotic checks.

The 4 finite-n cases are exact using Fraction. The phase approximation
is floating point, and is explicitly not a proof of the limit theorem.
"""
from fractions import Fraction as Q
from math import comb, ceil, exp, log

E = Q(31597745, 1653649)
beta = Q(3, 637)
u0 = Q(21829245984, 45529434409)
uE = Q(21829245984, 45529434409 - 456083905 * E)
x = Q(7, 20)
T0 = (1-x) * (1-beta*x)
TE = (1-x) * (1-beta*x+beta*E*x)
a, amin, bmax, b = 1-T0, 1-TE, 1-u0*T0, 1-uE*TE
assert a == Q(983, 2800)
assert b == Q(122610119576, 203307125225)
assert 0 < amin < a < b < bmax < 1
assert a*(1-a) < b*(1-b)   # exact certificate for t < 1/2

def mass(n, p):
    return [Q(comb(n, k)) * p**k * (1-p)**(n-k) for k in range(n+1)]

def full_dual(n):
    A, Am, Bm, B = [mass(n, p) for p in (a, amin, bmax, b)]
    d0 = [v-u for u,v in zip(A, Bm)]
    dE = [v-u for u,v in zip(Am, B)]
    candidates = {Q(0), Q(1)}
    for z,w in zip(d0,dE):
        if z != w:
            lam = z/(z-w)
            if 0 < lam < 1:
                candidates.add(lam)
    def advantage(lam):
        return sum(max(Q(0), (1-lam)*z+lam*w) for z,w in zip(d0,dE))
    min_adv, lam = min((advantage(y), y) for y in candidates)
    return lam, (1-min_adv)/2

def cross_dual(n):
    A, B = mass(n,a), mass(n,b)
    candidates = {Q(0), Q(1)}
    for u,v in zip(A,B):
        candidates.add(u/(u+v))
    def overlap(lam):
        return sum(min((1-lam)*u, lam*v) for u,v in zip(A,B))/2
    return max((overlap(y), y) for y in candidates)

af, bf = float(a), float(b)
Alog = log(bf*(1-af)/(af*(1-bf)))
t = log((1-af)/(1-bf)) / Alog
ra = af*(1-t)/(t*(1-af))
rb = bf*(1-t)/(t*(1-bf))
L = ra*(1-1/rb)/(1-ra)
c = log(L)/Alog
assert 0 < t < 0.5 and 0 < ra < 1 < rb and Alog > 0
lo = 1/(1+exp(Alog*(c+1)))
hi = 1/(1+exp(Alog*c))
print('p0=',a, 'qE=',b)
print(f't={t:.12f}, c={c:.12f}, phase-envelope=[{lo:.12f},{hi:.12f}]')
for n in (30,50,80,100):
    lam, risk = full_dual(n)
    cross_risk, cross_lam = cross_dual(n)
    j = ceil(n*t+c)
    predicted = 1/(1+exp(Alog*(j-n*t)))
    print(f'n={n} exact-full-lambda={float(lam):.12f} '
          f'exact-cross-lambda={float(cross_lam):.12f} '
          f'phase-prediction={predicted:.12f} exact-risk={float(risk):.12g}')
    assert 0 <= lam <= 1
    assert risk >= cross_risk
print('PASS: 4 exact rational full-dual/cross-dual checks; analytic phase formula evaluated')
