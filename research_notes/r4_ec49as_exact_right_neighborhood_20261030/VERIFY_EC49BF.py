#!/usr/bin/env python3
"""EC49BF quantitative near-endpoint exact check; not an independent review."""
from fractions import Fraction as Q
from itertools import product
import json
import sympy as S

eta=S.symbols('eta',real=True)
t=S.symbols('t',real=True)
A={(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)}
X=lambda t:[[(11-8*t)/16,0,t/4,0,(5+4*t)/16],
            [0,1,0,0,0],[1,0,0,0,0]]

def q_fiber(x,c,u,e):
    q=[x[w][c]*(S.Rational(1,2)+(2*u-1)*(1-w)*e)/3 for w in range(3)]
    return q,sum(q)

# Exact full-information rational attainment.
x=[[Q(5,16),0,Q(3,16),0,Q(1,2)],[0,1,0,0,0],[1,0,0,0,0]]
assert all(sum(row)==1 for row in x)
assert sum((1,1,2,2,0)[c]*x[w][c] for w in range(3) for c in range(5))==Q(43,16)
spent=score=Q(0)
fibers=[]
for c,u in product(range(4),range(2)):
    q=[x[w][c]*(Q(1,2)+(2*u-1)*(1-w)*Q(1,2))/3 for w in range(3)]
    mass=sum(q)
    p=Q(4,5) if (c,u)==(0,1) else Q(1)
    spent+=p*mass
    score+=p*sum(max(Q(0),43*a-16*mass) for a in q)/172
    if mass:
        nz=[w for w in range(3) if q[w]>0]
        assert len(nz)==1 and (c,u,nz[0]) in A
        fibers.append([c,u,nz[0],str(mass),str(p)])
assert spent==Q(13,16) and score==Q(351,2752)

# Exact algebraic F(eta) lower-witness identity on the entire interval.
s=S.sqrt(19-26*eta)
tstar=(27-10*eta-4*s)/(8*(1+2*eta))
pstar=(8*eta+s)/(4*(1+2*eta))
xr=X(tstar)
assert all(S.simplify(sum(row)-1)==0 for row in xr)
assert S.simplify(sum((1,1,2,2,0)[c]*xr[w][c]
                      for w in range(3) for c in range(5))-S.Rational(43,16))==0
spent_r=score_r=0
for c,u in product(range(4),range(2)):
    q,m=q_fiber(xr,c,u,eta)
    p=pstar if (c,u)==(0,1) else 1
    spent_r+=p*m
    score_r+=p*sum(43*q[w]-16*m for w in range(3) if (c,u,w) in A)/172
F=(2752*eta**2+42*eta+1397-172*(1-2*eta)*s)/(8256*(1+2*eta))
assert S.simplify(spent_r-S.Rational(13,16))==0
assert S.simplify(score_r-F)==0

# Every score is bilinear in (eta,t): checking the rectangle's corners is exact.
checks=0
for c,u in product(range(4),range(2)):
    q,m=q_fiber(X(t),c,u,eta)
    for w in range(3):
        f=S.expand(43*q[w]-16*m)
        sign=1 if (c,u,w) in A else -1
        for ee,tt in product([S.Rational(99,200),S.Rational(1,2)],
                             [S.Rational(3,4),S.Rational(4,5)]):
            assert sign*f.subs({eta:ee,t:tt})>=0
            checks+=1

# Finite examples are only diagnostics; the all-real impurity lemma is proved in PROOF.
n=0
for a,b,c in product(range(15),repeat=3):
    tot=a+b+c
    if not tot:continue
    assert 27*tot-sum(max(0,43*v-16*tot) for v in (a,b,c))>=32*(tot-max(a,b,c))
    n+=1

C=Q(351,2752)
bounds={str(e):str(C-(1-2*e)/(172*(1+2*e)))
        for e in [Q(99,200),Q(199,400),Q(499,1000),Q(1,2)]}
print(json.dumps({'result':'PASS','scope':'auxiliary only; author-side, unreviewed',
 'sharp_eta_half':str(score),'first_cost':str(Q(43,48)),
 'second_cost':str(spent),'endpoint_pure_fibers':fibers,
 'symbolic_F_lower_identity':True,'bilinear_corners':checks,
 'finite_triple_diagnostics':n,'uniform_exact_bounds':bounds},
 indent=2,sort_keys=True))
