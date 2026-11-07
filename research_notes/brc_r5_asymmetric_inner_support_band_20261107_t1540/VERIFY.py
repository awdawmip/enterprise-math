#!/usr/bin/env python3
"""Exact rational verifier for the R5 asymmetric signed-support band.
All arithmetic uses Python's Fraction; no external packages.
"""
from fractions import Fraction as F

Q = lambda x: F(x)
R = tuple(map(Q, ('1/10','1/2','3/4','1','5/4','3/2','19/10')))
LM, LP = -Q('351/17291'), Q('351/16589')
LOW, HIGH = -Q('1/56'), Q('9/344')

def calc(x):
    g,a,b,u,v,w,z = x
    c0, c1, c2 = 13*a/40+b/80, a/10+9*b/40, 3*a/40+21*b/80
    m = (
        509*u/900+47*z/180+67*(v-z)/162+w/100,
        c0-u, (g-a)/2,
        1-g+c1-v+191*(u+w)/450+43*z/90+14*(v-z)/81,
        (g-b)/2, c2-w,
        u/100+47*z/180+67*(v-z)/162+509*w/900)
    tp = 1+g+(3*a+5*b)/8+u/2+v+3*w/2
    tq = 1+g+(a+b)/2+u+v+w
    return m,tp,tq,(c0,c1,c2)

def support(x, lam):
    m,_,_,_ = calc(x)
    return sum((1-(1+lam)*r)*mass for r,mass in zip(R,m)
               if 1-(1+lam)*r > 0)

def slacks(x):
    g,a,b,u,v,w,z = x
    _,_,_,(_,c1,_) = calc(x)
    return (u,c1-v,w,9*b/40-v+z,1-g)

# Anchors from immutable R5 predecessor research note, 8902141f486f...
ANCHORS = (
    (LM,Q('22146/86455'),Q('6694/86455'),Q('3016/86455'),
     tuple(map(Q,('22473/345820','7789/69164','46129/345820','81757/622476','0')))),
    (Q(0),Q('13269/53000'),Q('391/6625'),Q('364/6625'),
     tuple(map(Q,('3999/53000','1283/10600','7127/53000','247/1800','117/10600')))),
    (LP,Q('20391/82945'),Q('3184/82945'),Q('6526/82945'),
     tuple(map(Q,('26373/331780','7789/66356','42229/331780','81757/597204','0'))))
)

def certified_gap(x, spec):
    lam,B,alpha,beta,mu = spec
    _,tp,tq,_ = calc(x)
    lhs = B+alpha*(tp-Q('31/10'))+beta*(tq-Q('31/10'))-support(x,lam)
    rhs = sum(mi*si for mi,si in zip(mu,slacks(x)))
    return lhs-rhs

basis = [tuple(Q(0) for _ in range(7))]
for k in range(7):
    basis.append(tuple(Q(int(j==k)) for j in range(7)))
for spec in ANCHORS:
    assert all(weight >= 0 for weight in spec[4])
    for x in basis:
        assert certified_gap(x,spec) == 0
        m,_,_,_ = calc(x)
        assert sum(m)==1 and sum(r*mass for r,mass in zip(R,m))==1
print('PASS_24_ANCHOR_CERTIFICATE_IDENTITIES_AND_16_MOMENT_IDENTITIES')

def optimal_flow(e):
    a,b = (44-504*e)/53, (44+344*e)/53
    return (Q(1),a,b,Q(0),a/10+9*b/40,Q(0),a/10)

def valid(x):
    g,a,b,u,v,w,z = x
    m,_,_,(c0,c1,c2) = calc(x)
    return (0 <= a <= g <= 1 and 0 <= b <= g and 0 <= u <= c0
            and 0 <= v <= c1 and 0 <= w <= c2 and 0 <= z <= a/10
            and 0 <= v-z <= 9*b/40 and all(t >= 0 for t in m))

for e in (LOW,HIGH,Q(0),Q('1/100'),-Q('1/100')):
    x = optimal_flow(e)
    m,tp,tq,_ = calc(x)
    assert valid(x) and tp==Q('31/10')+e and tq==Q('31/10')-e
    assert 9*x[2]*x[6]==4*x[1]*(x[4]-x[6])
    assert sum(m)==1 and sum(r*j for r,j in zip(R,m))==1
    for lam,B,alpha,beta,mu in ANCHORS:
        assert support(x,lam)==B+(alpha-beta)*e
print('PASS_ENDPOINT_LEGALITY_SEEDLESS_RELATION_TIMES_AND_SHARPNESS')

BASE = Q('13269/53000')
def formula(e,lam):
    common = BASE+Q('27/6625')*e
    if lam < 0:
        return common-(Q('45413/159000')+Q('112987/59625')*e)*lam
    return common-(Q('641/3000')+Q('2359/1125')*e)*lam

for e in (Q(0),Q(1)):
    for lam in (LM,Q(0),LP):
        assert support(optimal_flow(e),lam) == formula(e,lam)
# Each piece is bilinear in (epsilon,lambda), so corners determine it exactly.
print('PASS_ALL_REAL_BILINEAR_FORMULAS_BY_EXACT_COEFFICIENT_CHECK')

for e, expected in ((Q('1/100'),(
       Q('172207/225000'),Q('144601/298125'),Q('311/100'),Q('309/100'))),
       (-Q('1/100'),(
       Q('181643/225000'),Q('132074/298125'),Q('309/100'),Q('311/100')))):
    x = optimal_flow(e)
    m,tp,tq,_ = calc(x)
    eq = sum(m[:3])
    ep = 1-sum(R[j]*m[j] for j in range(3))
    assert (ep,eq,tp,tq)==expected
    assert (eq-(1-ep))==formula(e,Q(0))
print('PASS_TWO_ASYMMETRIC_FOUR_OBSERVER_WITNESSES')
print('PASS_R5_ASYMMETRIC_CENTRAL_LAMBDA_BAND_EXACT_ALL_REAL')
