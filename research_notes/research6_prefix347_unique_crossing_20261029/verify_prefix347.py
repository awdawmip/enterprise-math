#!/usr/bin/env python3
"""PREFIX-347 exact interval proof: unique T6 crossing in PREFIX-346 bracket.

All decision predicates rational interval arithmetic. Six algebraic roots and
45 source-labelled BRC products are independently re-executed via PREFIX-342.
No sampling or float predicates. Claim concerns constructed six-arc T6 only.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,runpy
from sympy import Matrix,Rational as Q
v=runpy.run_path(str(Path(__file__).with_name('verify_prefix342.py')))
IV,ci=v['IV'],v['ci']
zadd,zmul,zconj,zscalar=v['zadd'],v['zmul'],v['zconj'],v['zscalar']
znorm2,zdotconj,rvec,rdot=v['znorm2'],v['zdotconj'],v['rvec'],v['rdot']
sources,ports,q3,L=v['sources'],v['ports'],v['q3'],v['L']
assert len(sources)==len(ports)==6
hlo=F(166639681,100000000)
hhi=F(83319841,50000000)
h=IV(hlo,hhi)
y=h-1
assert y.lo>0
radlo=q3-(hhi-1)**2
radhi=q3-(hlo-1)**2
assert radlo>0 and radhi>radlo

def lo_sqrt(x,scale):
    k=isqrt((x.numerator*scale*scale)//x.denominator)
    p=F(k,scale)
    assert p*p<=x and (p+F(1,scale))**2>x
    return p
scale=10**35
s=IV(lo_sqrt(radlo,scale),lo_sqrt(radhi,scale)+F(1,scale))
assert s.lo*s.lo<=radlo and s.hi*s.hi>=radhi
# Source shapes b_j = conj(w_j)/q3 * a_j;
# points are z(h)*b_j, with z=+/-s(h)+i(h-1).
b=[[zmul(zscalar(1/q3,zconj(w)),ak) for ak in a] for a,w in zip(sources,ports)]
P={};dP={}
for j in range(6):
    for sign in ('-','+'):
        eps=1 if sign=='+' else -1
        z=ci(eps*s,y)
        zp=ci(-eps*y/s,1)
        P[j,sign]=[zmul(z,ak) for ak in b[j]]
        dP[j,sign]=[zmul(zp,ak) for ak in b[j]]
contact=[(0,'-'),(1,'+'),(3,'-'),(3,'+'),(4,'+')]
R=[rvec(P[k]) for k in contact]
D=[[q-p for p,q in zip(R[0],R[k])] for k in range(1,5)]
G=[[rdot(D[i],D[j]) for j in range(4)] for i in range(4)]
rhs=[G[i][i]/2 for i in range(4)]

def mid(x):return (x.lo+x.hi)/2
def imax(x):return max(abs(x.lo),abs(x.hi))
def round_frac(x,scale):return F((x.numerator*scale)//x.denominator,scale)
GM=Matrix([[Q(round_frac(mid(G[i][j]),10**12).numerator,round_frac(mid(G[i][j]),10**12).denominator) for j in range(4)] for i in range(4)])
assert GM.det()!=0
BM=GM.inv()
B=[[F(int(BM[i,j].p),int(BM[i,j].q)) for j in range(4)] for i in range(4)]
beta0=[round_frac(sum((B[i][j]*mid(rhs[j]) for j in range(4)),F(0)),10**12) for i in range(4)]
E=[[IV(int(i==j))-sum((B[i][k]*G[k][j] for k in range(4)),IV(0)) for j in range(4)] for i in range(4)]
e=max(sum((imax(E[i][j]) for j in range(4)),F(0)) for i in range(4))
u=[sum((B[i][k]*(rhs[k]-sum((G[k][j]*beta0[j] for j in range(4)),IV(0))) for k in range(4)),IV(0)) for i in range(4)]
assert e<F(1,1),('non-invertible interval Gram certificate',float(e))
delta=max(imax(z) for z in u)/(1-e)
beta=[IV(z-delta,z+delta) for z in beta0]
alpha=[IV(1)-sum(beta,IV(0))]+beta
assert all(a.lo>0 for a in alpha),('not positive',alpha)
C=[R[0][i]+sum((beta[j]*D[j][i] for j in range(4)),IV(0)) for i in range(6)]
r2=rdot([R[0][k]-C[k] for k in range(6)],[R[0][k]-C[k] for k in range(6)])
slack={}
for key,p in P.items():
    if key in contact:continue
    dd=rdot([z-w for z,w in zip(rvec(p),C)],[z-w for z,w in zip(rvec(p),C)])
    gap=r2-dd
    slack[str(key)]=gap
    assert gap.lo>0,(key,'not inside',float(gap.lo),float(gap.hi))
conv={}
for j,(a,w) in enumerate(zip(sources,ports)):
    cen=[(C[2*k],C[2*k+1]) for k in range(3)]
    t=zscalar(1/q3,zmul(zdotconj(cen,a),zconj(w)))
    conv[str(j)]=t[1]
    assert t[1].hi<0,(j,'no convexity',float(t[1].hi))
# Derivative formula obtained via equality of five contact distances:
# dR²/dh=2 Σ alpha_i <p_i-c, p'_i> where c= Σ alpha_i p_i.
# It does not require differentiating alpha because Σ alpha_i(p_i-c)=0.
# All alpha are positive and their exact affine Gram solution on the interval.
deriv=IV(0)
for key,weight in zip(contact,alpha):
    rp=rvec(P[key]); rv=rvec(dP[key])
    deriv+=2*weight*rdot([z-w for z,w in zip(rp,C)],rv)
assert deriv.hi<0,('derivative not negative',float(deriv.lo),float(deriv.hi))
assert e<F(1,100000)
assert delta<F(1,400000)
assert min(a.lo for a in alpha)>F(1,10000)
assert min(g.lo for g in slack.values())>F(3,1000)
assert max(t.hi for t in conv.values()) < -F(97,100)
assert -F(19811,10000) < deriv.lo <= deriv.hi < -F(19808,10000)
# Bracket sign follows from PREFIX-346 verified explicit four-point variance lower
# and a common rational covering upper. Reuse actual upstream checker below.
u346=runpy.run_path(str(Path(__file__).with_name('verify_prefix346.py')))
# The preceding run asserts the left/right strict signs using exact Fractions.
result={
 'schema':'PREFIX347_SIX_ARC_STRICT_MONOTONIC_CROSSING_CERTIFICATE_V1',
 'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL_T6_STRICT_MONOTONICITY',
 'h_bracket':[str(hlo),str(hhi)], 'L':str(L),
 'support':[list(k) for k in contact],
 'gram_inverse_error_upper':str(e),
 'four_beta_error_upper':str(delta),
 'contact_weight_lower_bounds':[str(a.lo) for a in alpha],
 'min_noncontact_slack_lower':str(min(g.lo for g in slack.values())),
 'strict_arc_convexity_im_t_upper':str(max(t.hi for t in conv.values())),
 'radius_interval_over_bracket':[str(r2.lo),str(r2.hi)],
 'radius_squared_derivative_interval':[str(deriv.lo),str(deriv.hi)],
 'conclusion':'For fixed six Banach-certified source arcs T6, MEB²(T6(h)) is strictly decreasing on the entire closed h-bracket; hence the PREFIX346 crossing exists and is unique.',
 'boundary':'Does NOT prove S=T6, uniqueness/full-source risk crossing, native X6 or physical transfer.',
 'method':'Exact Fraction interval enclosing all h and exact Newton-Banach roots; certified Gram inverse (Neumann residual); positive support, 7 strict noncontacts, exact analytic full-arc convexity, envelope derivative; upstream endpoint sign check executed.'
}
Path(__file__).with_name('RESULTS_PREFIX347.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(result['status'])
print('inverse error',float(e),'beta error',float(delta),'min weight',float(min(a.lo for a in alpha)))
print('min 7 slack',float(min(g.lo for g in slack.values())),'max Im(t)',float(max(t.hi for t in conv.values())))
print('d(R²)/dh bound',float(deriv.lo),float(deriv.hi))
