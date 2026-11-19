#!/usr/bin/env python3
"""EC49FUA exact rational tests for full-support all-epsilon price law.
Requires only Python stdlib; not a native BRC Bellman or independent review.
"""
from fractions import Fraction as F
import json

m0,m1,m2,m3=F(11457,512),F(1461,64),F(1469,64),F(187,8)
E=F(1048576,18958647)
U,C=F(3,4),F(16,945)
def L(m):
    return (4*m+2647)/3696 if m<m1 else (8*m+173)/480
def R(m):
    return (64*m+1411)/3840 if m<m2 else U
def atom(m):
    if m<m2: return F(0),F(0)
    d=F(49,64)-(740-m)/945
    alpha,beta=F(525,8),F(35,32)
    p=m*U+(m*beta+U*alpha)*d/2+alpha*beta*d*d/3
    return d/54,d*p/54
def cdf(m,eps,z):
    l,r=L(m),R(m)
    if z<=l: return F(0)
    if z>=U or (m<m2 and z>=r): return F(1)
    n=min(z,r)
    b0,b1=atom(m)
    num=C*((n-l)-eps*m*(n*n-l*l)/2)
    den=C*((r-l)-eps*m*(r*r-l*l)/2)+b0-eps*b1
    return num/den
def atom_probability(m,eps):
    b0,b1=atom(m)
    l,r=L(m),R(m)
    continuous=C*((r-l)-eps*m*(r*r-l*l)/2)
    return (b0-eps*b1)/(continuous+b0-eps*b1)

assert E<F(1,18)
assert (4*m1+2647)/3696==(8*m1+173)/480
assert (64*m2+1411)/3840==U
assert (8*m3+173)/480==U
assert L(m0)==R(m0)==F(4549,6144)
# phase1 W grows, phase2 W=9/1280, both L' >=1/924.
Wmax=F(9,1280)
assert (R(m1)-L(m1))==Wmax
assert (R(m2)-L(m2))==Wmax
assert F(1,60)-F(1,924)<F(1,64)
delta=1-F(1,18)*23*U
tmax=F(1,18)*23*Wmax/delta
tprimemax=(F(1,18)*(Wmax+23*F(1,64))/delta+
           F(1,18)**2*23*Wmax*(U+23*F(1,60))/delta**2)
shiftloss=Wmax*tprimemax/(8*(1-tmax/2)*(1-tmax))
margin=F(1,924)-shiftloss
assert delta==F(1,24)
assert tmax==F(69,320)
assert tprimemax==F(1303,1600)
assert shiftloss==F(11727,11465680)
assert margin==F(157483,2648572080)>0
assert atom_probability(m2,F(0))==F(115,223)
assert atom_probability(m2,E)==F(3310244525,8132285009)
assert F(0)<atom_probability(m2,E)<atom_probability(m2,F(0))<1

# Regression only: 3 phases x seven exact interior levels,
# 5 epsilon values, 17 absolute thresholds, adjacent comparisons.
ms=[]
for lo,hi in ((m0,m1),(m1,m2),(m2,m3)):
    ms += [lo+(hi-lo)*F(j,8) for j in range(1,8)]
epsilons=[F(-100),F(-1),F(0),E/2,E]
thresholds=[F(11,16)+(U-F(11,16))*F(j,16) for j in range(17)]
checks=0
for eps in epsilons:
    for a,b in zip(ms,ms[1:]):
        for z in thresholds:
            fa,fb=cdf(a,eps,z),cdf(b,eps,z)
            assert F(0)<=fb<=fa<=F(1),(eps,a,b,z,fa,fb)
            checks+=1
assert checks==1700
result={
    "schema":"EC49FUA_FULL_SUPPORT_EPSILON_FOSD_CERT_V1",
    "scientific_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
    "domain_M":"(11457/512,187/8)",
    "domain_epsilon":"(-infinity,1048576/18958647]",
    "m_phase_boundaries":["11457/512","1461/64","1469/64","187/8"],
    "quantile_derivative_rational_lower_bound":str(margin),
    "quantile_shape_t_upper_bound":str(tmax),
    "quantile_shape_derivative_upper_bound":str(tprimemax),
    "top_atom_jump_epsilon_0":str(atom_probability(m2,F(0))),
    "top_atom_jump_epsilon_E":str(atom_probability(m2,E)),
    "finite_rational_regression_count":checks,
    "proof_status":"AUTHOR_PROVED_PARENT_DEPENDENT_NOT_REVIEWED",
    "native_BRC_recomputed":False,
    "project_Review_completed":False
}
print(json.dumps(result,indent=2,ensure_ascii=False))
