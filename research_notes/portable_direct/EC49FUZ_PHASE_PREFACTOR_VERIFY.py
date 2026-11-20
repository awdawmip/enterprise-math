"""EC49FUZ exact arithmetic + numeric checks for the fixed-width phase theorem.

Only Python standard library. Rational certificates are exact; logarithms,
exp and asymptotic-display comparisons are floating point, not proof.
"""
from fractions import Fraction as Q
from math import comb, log, exp, sqrt, pi, ceil

E, beta = Q(31597745, 1653649), Q(3, 637)
u0 = Q(21829245984, 45529434409)
uE = Q(21829245984, 45529434409 - 456083905 * E)
x = Q(7, 20)
T0 = (1-x)*(1-beta*x)
TE = (1-x)*(1-beta*x+beta*E*x)
am, a, b, bp = 1-TE, 1-T0, 1-uE*TE, 1-u0*T0
assert a == Q(983, 2800) and b == Q(122610119576, 203307125225)
assert 0 < am < a < b < bp < 1
R, S = (1-a)/(1-b), b*(1-a)/(a*(1-b))
assert R == Q(642450515711, 392959331856)
assert S == Q(9686199446504, 3448919850129)
assert R.numerator % 29 == 0 and R.denominator % 29 != 0
assert S.numerator % 29 != 0 and S.denominator % 29 != 0
print('PASS: v_29(R)>0 and v_29(S)=0; t=log(R)/log(S) irrational')

def mass(n, p):
    return [Q(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1)]

def exact_bayes(n):
    A, AM, B, BP = mass(n,a), mass(n,am), mass(n,b), mass(n,bp)
    d0 = [bp0-aa for bp0,aa in zip(BP,A)]
    dE = [bb-amm for bb,amm in zip(B,AM)]
    candidates = {Q(0), Q(1)}
    for z,w in zip(d0,dE):
        if z != w:
            y = z/(z-w)
            if 0 < y < 1:
                candidates.add(y)
    def f(lam):
        return (1-sum(max(Q(0),(1-lam)*v+lam*w)
                      for v,w in zip(d0,dE)))/2
    full_risk, full_lam = max((f(z),z) for z in candidates)
    cross_lams = {Q(0),Q(1)} | {aa/(aa+bb) for aa,bb in zip(A,B)}
    def g(lam):
        return sum(min((1-lam)*aa,lam*bb) for aa,bb in zip(A,B))/2
    cross_risk, cross_lam = max((g(z),z) for z in cross_lams)
    assert full_risk >= cross_risk
    return full_risk, full_lam, cross_risk, cross_lam

af,bf = float(a),float(b)
Alog = log(float(S))
t = log(float(R))/Alog
ra = af*(1-t)/(t*(1-af))
rb = bf*(1-t)/(t*(1-bf))
L = ra*(1-1/rb)/(1-ra)
c = log(L)/Alog
C = t*log(t/af)+(1-t)*log((1-t)/(1-af))
sigma = sqrt(t*(1-t))
assert 0 < af < t < bf < 1 and 0 < ra < 1 < rb

def h(d):
    # prefactor of e^{-nC}/sqrt(n) at the optimizing lattice kink
    common = exp(d*log(rb))/(1+exp(Alog*d))
    return common*(1/(rb-1)+1/(1-ra))/(2*sqrt(2*pi)*sigma)

def lam(d):
    return 1/(1+exp(Alog*d))

dstar = log(log(rb)/(-log(ra)))/Alog
assert c < dstar < c+1
assert abs(h(c)-h(c+1)) < 1e-12
assert h(dstar) > h(c)
print(f'phase: t={t:.12f}, c={c:.12f}, C={C:.12f}')
print(f'weight accumulation interval [{lam(c+1):.12f},{lam(c):.12f}]')
print(f'normalized risk accumulation interval [{h(c):.12f},{h(dstar):.12f}]')
for n in (30,50,80,100):
    full,fl,cross,cl = exact_bayes(n)
    d = ceil(n*t+c)-n*t
    scale = sqrt(n)*exp(n*C)
    assert c-1e-10 <= d < c+1+1e-10
    print(f'n={n:3d}: lambda_full={float(fl):.12f}, '
          f'lambda_cross={float(cl):.12f}, '
          f'full_scaled={scale*float(full):.12f}, '
          f'cross_scaled={scale*float(cross):.12f}, '
          f'limiting_h={h(d):.12f}')
print('ALL PASS: exact finite dual, 29-adic witness, analytic prefactor crosschecks')
