#!/usr/bin/env python3
"""EC49FTO: exact-rational checks for f(a) proportional a, g(b) proportional b.
This checks the price-prior corollary, not the native original-index Bellman.
"""
from fractions import Fraction as Q
from itertools import combinations
import json

alo,ahi=Q(3,4),Q(49,64)
blo,bhi=Q(7,16),Q(57,128)
m0,m1,m2,m3=Q(11457,512),Q(1461,64),Q(1469,64),Q(187,8)
alpha,beta=Q(44,45),Q(10,9)

def L(m):
    return (4*m+2647)/3696 if m<m1 else (8*m+173)/480
def U(m):
    return (64*m+1411)/3840 if m<m2 else Q(3,4)
def a(m,z):
    return (47-m)/945+alpha*z
def b(m,z):
    return Q(1,27)-m/54+beta*z
def integral_ab(m,z0,z1):
    A=(47-m)/945; B=Q(1,27)-m/54
    return (A*B*(z1-z0)+(A*beta+B*alpha)*(z1*z1-z0*z0)/2+
            alpha*beta*(z1**3-z0**3)/3)
def mass_cont(m):
    return Q(16,945)*integral_ab(m,L(m),U(m))
def mass_atom(m):
    if m<=m2: return Q(0)
    ac=(740-m)/945;bs=(47-m)/54
    return bs*(ahi**2-ac**2)/108
def cdf(m,t):
    lo,hi=L(m),U(m)
    if t<=lo: return Q(0)
    if t>=Q(3,4) or (m<=m2 and t>=hi): return Q(1)
    numer=Q(16,945)*integral_ab(m,lo,min(t,hi))
    return numer/(mass_cont(m)+mass_atom(m))
def integral_poly(coeffs,lower,upper):
    return sum((c*(upper**(k+1)-lower**(k+1))/(k+1)
                for k,c in coeffs.items()),Q(0))

poly={1: ahi**2/Q(2)-Q(77*77,2*105*105),
      2: -Q(77*6,105*105),
      3: -Q(36,2*105*105)}
num=integral_poly(poly,blo,bhi)
den=(ahi**2-alo**2)/2*(bhi**2-blo**2)/2
pclip=num/den
assert pclip==Q(109942873,241690050),pclip
assert L(m0)==U(m0) and L(m3)==U(m3)==Q(3,4)
assert U(m2)==Q(3,4)
assert a(m2,Q(3,4))==(740-m2)/945
for m in (m0+(m1-m0)/3,m1+(m2-m1)/3,m2+(m3-m2)/3):
    lo,hi=L(m),U(m)
    assert Q(0)<=lo<hi<=Q(3,4)
    for j in range(9):
        z=lo+(hi-lo)*j/8
        assert alo<=a(m,z)<=ahi and blo<=b(m,z)<=bhi
        assert integral_ab(m,lo,z)>=0
ms=[]
for ll,rr in ((m0,m1),(m1,m2),(m2,m3)):
    ms.extend([ll+(rr-ll)*k/11 for k in range(1,11)])
zs=[Q(11,16)+(Q(3,4)-Q(11,16))*k/30 for k in range(31)]
count=0
for ma,mb in combinations(ms,2):
    for z in zs:
        assert cdf(mb,z)<=cdf(ma,z),(ma,mb,z,cdf(ma,z),cdf(mb,z))
        count+=1
for m in ms:
    assert mass_cont(m)>0 and mass_atom(m)>=0
    assert cdf(m,Q(3,4))==1
report={"schema":"EC49FTO_LOGCONCAVE_PRIOR_EXACT_FRACTION_CHECK_V1",
"frozen_scientific_input":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
"example":"Independent prior f(a) proportional a, g(b) proportional b",
"clipping_probability":str(pclip),
"m_points":len(ms),"thresholds":len(zs),
"rational_stochastic_order_comparisons":count,
"status":"EXACT_FRACTION_REGRESSION_PASSED; analytic theorem separate",
"native_Bellman_rerun":False,"formal_review":False}
print(json.dumps(report,indent=2,ensure_ascii=False))
