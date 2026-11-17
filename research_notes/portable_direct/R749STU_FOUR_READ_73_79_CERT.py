#!/usr/bin/env python3
"""Exact R749STU IVT collision + four-read Bernstein separation certificate.

Requires Python 3 and SymPy. Uses integer/rational arithmetic throughout.
Auxiliary five-source observer only, not a native X6/BRC equivalence proof.
"""
from fractions import Fraction
from pathlib import Path
import json
import sympy as sp

W=(1,1,2,3,6)
N=97
part=[0]*(N+1)
part[0]=1
for w in W:
    for n in range(w,N+1):
        part[n]+=part[n-w]
C=[0]*(N+1); T=[0]*(N+1)
for n in range(1,N+1):
    C[n]=C[n-1]+part[n-1]
    T[n]=T[n-1]+C[n-1]
assert [(C[n],T[n]) for n in (73,79,85,91,97)] == [
    (707343,8931013), (1020943,13914446),
    (1436968,21025004), (1978664,30933812),
    (2672553,44459556)]

def S(n): return 18*n**4+54*n**3-345*n**2+2070*n-16315
def Y(n,e,d):
    return sp.Rational(n**3)*(T[n]+e)/(C[n]+d)-sp.Rational(S(n),108)

def bernstein_tensor(P,x,z):
    P=sp.Poly(sp.expand(P),x,z)
    m,k=P.degree(x),P.degree(z)
    a=P.as_dict()
    return [sum(a.get((r,t),0)*
                sp.Rational(sp.binomial(i,r),sp.binomial(m,r))*
                sp.Rational(sp.binomial(j,t),sp.binomial(k,t))
                for r in range(i+1) for t in range(j+1))
            for i in range(m+1) for j in range(k+1)], (m,k)

def bernstein_univariate(P,t):
    P=sp.Poly(sp.expand(P),t)
    m=P.degree()
    return [sum(P.nth(r)*sp.Rational(sp.binomial(i,r),sp.binomial(m,r))
                for r in range(i+1)) for i in range(m+1)]

# Exact three-read collision via rational IVT bracket.
D=sp.symbols('D')
lo,hi=sp.Rational(-909,1000),sp.Rational(-908,1000)
xs=[];vs=[]
for i in range(2):
    n=73+6*i
    target=sp.cancel(Y(79+6*i,sp.Integer(1),D))
    xx=sp.cancel((target+sp.Rational(S(n),108))/n**3)
    xs.append(xx)
    vs.append(sp.cancel(C[n]*xx-T[n]))
d=sp.cancel((vs[0]-vs[1])/(xs[1]-xs[0]))
e=sp.cancel(vs[0]+xs[0]*d)
t=sp.symbols('t')
Dt=lo+(hi-lo)*t
interval={}
for name,expr in [('x1_minus_x0',xs[1]-xs[0]),('e_plus_2',e+2),
                  ('2_minus_e',2-e),('d_plus_2',d+2),('2_minus_d',2-d)]:
    rat=sp.cancel(expr.subs(D,Dt))
    numerator,denominator=sp.fraction(rat)
    A=bernstein_univariate(numerator,t)
    B=bernstein_univariate(denominator,t)
    assert len(A)==3 and len(B)==3
    assert all(v>0 for v in A+B) or all(v<0 for v in A+B),name
    interval[name]={'numerator_min_abs':str(min(abs(v) for v in A)),
                    'denominator_min_abs':str(min(abs(v) for v in B)),
                    'sign':str(sp.sign(A[0]))}
residual=sp.cancel(Y(85,e,d)-Y(91,sp.Integer(1),D))
rlo=sp.cancel(residual.subs(D,lo))
rhi=sp.cancel(residual.subs(D,hi))
assert rlo<0<rhi
for endpoint in (lo,hi):
    ev=sp.cancel(e.subs(D,endpoint))
    dv=sp.cancel(d.subs(D,endpoint))
    assert -2<ev<2 and -2<dv<2
    for i in range(2):
        assert sp.cancel(Y(73+6*i,ev,dv)-Y(79+6*i,sp.Integer(1),endpoint))==0

# Entire continuous real nuisance cube: two separate tensor Bernstein boxes.
a=(9261513,-33843268,40729637,-16165583)
K=sp.Integer(146200)
x,z,u,v=sp.symbols('x z u v')
cert={}; delta=sp.Integer(0)
for n,sign in ((73,1),(79,-1)):
    L=sum(a[j]*Y(n+6*j,u,v) for j in range(4))
    prod=sp.prod(C[n+6*j]+v for j in range(4))
    poly=sp.cancel(108*sign*(L-K)*prod)
    poly=sp.expand(poly.subs({u:-2+4*x,v:-2+4*z}))
    b,deg=bernstein_tensor(poly,x,z)
    assert tuple(deg)==(1,4) and len(b)==10 and all(w>0 for w in b)
    bound=sp.Rational(min(b),108*sp.prod(C[n+6*j]+2 for j in range(4)))
    cert[str(n)]={'bernstein_degrees':list(deg),
                  'bernstein_coefficients':[str(c) for c in b],
                  'min_coefficient':str(min(b)),
                  'uniform_margin':str(bound)}
    delta+=bound
expected=sp.Rational(722997167446021926834455947339144,
                     4444935850061982688915244893275)
assert delta==expected and delta>0
eta=delta/(2*sum(abs(c) for c in a))
assert eta==sp.Rational(361498583723010963417227973669572,
                       444493589451134118953507178242744893275)
out={'unit':'R749STU','date':'2026-11-17',
     'frozen_science_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
     'status':'AUTHOR_EXACT_NOT_REVIEWED','candidates':[73,79],
     'nuisance':'two fixed real nuisance pairs in [-2,2]^2',
     'three_read_collision':{'E':'1','D_bracket':[str(lo),str(hi)],
       'third_residual_at_lo':str(rlo),'third_residual_at_hi':str(rhi),
       'interval_sign_certificates':interval},
     'four_read_separator':{'integer_coefficients':list(a),'K':str(K),
       'bernstein_boxes':cert,'strict_uniform_margin':str(delta),
       'noise_per_read_eta_strict_less_than':str(eta),
       'strict_positive_coefficients':'20/20'},
     'conclusion':'m_initial({73,79})=4',
     'scope':'five-source auxiliary scalar observer; no native X6/Port/Cell equivalence',
     'next':'Construct typed BRC/provenance-preserving future-operation readout'}
Path(__file__).with_name('R749STU_FOUR_READ_73_79_RESULTS.json').write_text(
    json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS: exact 3-read IVT collision, 20/20 Bernstein positives, 4-read separator')
print('delta=',delta,'eta<',eta)
