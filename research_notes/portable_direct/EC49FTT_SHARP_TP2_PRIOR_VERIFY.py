#!/usr/bin/env python3
"""EC49FTT: exact rational verification of a sharp C-infinity prior threshold.

Only the inherited high-gap external price-prior transform is used;
there is no native Bellman reexecution. Python standard library only.
"""
from fractions import Fraction as F
from hashlib import sha256
import json

m2,m3 = F(1469,64),F(187,8)
tmax = m3-m2
u,v = F(1997623522965,22125568),F(1034635,2158592)

def r0(m):
    t=m3-m
    return -F(25,41)+u/(164*t+166005)+v/t

def r0_direct(m):
    return -F(25,256)*(64*m-1055)*(256*m-35545)/((8*m-187)*(328*m-339677))

def r0_derivative(m):
    t=m3-m
    return 164*u/(164*t+166005)**2+v/t**2

def r_lambda(m,lmbda):
    return r0(m)+lmbda*(m3-m)

def atommass(m,lmbda):
    r=r_lambda(m,lmbda)
    return r/(1+r)

def K0(m,z):
    aa=(47-m)/945+F(44,45)*z
    bb=F(1,27)-m/54+F(10,9)*z
    return F(16,945)*(1+aa+bb)

def L(m):return (8*m+173)/480

def A0(m):
    t=m3-m
    return t*(164*t+166005)/267907500

def B0(m):
    t=m3-m
    return -(64*t-441)*(256*t+29561)/43893964800

def ac(b):return (77+6*b)/105

def d(b):return F(49,64)-ac(b)

def m_from_b(b):return 47-54*b

def f(b):
    mm=m_from_b(b)
    return 54*A0(mm)*(m3-mm)/d(b)

crit=r0_derivative(m2)
assert tmax==F(27,64)
assert crit==F(171167905504400,63545784776721)
assert F(2)<crit<F(3)
assert all(d(b)>0 for b in (F(7,16),F(113,256),F(57,128)))
assert f(F(7,16))==0 and f(F(57,128))>0

# Formula independent of the closed-form partial-fraction decomposition.
for j in range(1,65):
    m=m2+tmax*F(j,65)
    assert r0(m)==r0_direct(m)
    assert r0(m)==B0(m)/A0(m)
    assert r0_derivative(m)>crit
    assert r0_derivative(m)<r0_derivative(m+tmax/F(512))

# Strict TP2 (nonzero positive determinants) at interior rational rectangles.
tp2_checks=0
for i in (1,3,6,12):
    ma=m2+tmax*F(i,40)
    mb=m2+tmax*F(i+3,40)
    low=L(mb)+(F(3,4)-L(mb))/4
    high=L(mb)+3*(F(3,4)-L(mb))/4
    det=K0(ma,low)*K0(mb,high)-K0(ma,high)*K0(mb,low)
    assert det>0
    tp2_checks+=1

# Exact atom mass at the interior witness of failure when lambda=3.
p,q=m2+F(1,128),m2+F(1,64)
assert m2<p<q<m3
r_gap=r_lambda(p,F(3))-r_lambda(q,F(3))
a_gap=atommass(p,F(3))-atommass(q,F(3))
assert r_gap>0 and a_gap>0
# Shape at the exact sharp threshold: strictly increasing on every interior interval.
for i in range(1,65):
    m=m2+tmax*F(i,66)
    assert r0_derivative(m)-crit>0
    assert r0_derivative(m)-F(3)<0 if i==1 else True

cert={
  "schema":"EC49FTT_SHARP_SMOOTH_TP2_PRIOR_CERT_V1",
  "status":"AUTHOR_PROVED_EXACT_FRACTION_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED",
  "scientific_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
  "external_pricing_parent":"EC49FTS PR2797@7dcff5e1e3713ac34f57484563ab6cdc57b9dd9a",
  "m_interval":[str(m2),str(m3)],
  "t_max":str(tmax),
  "sharp_lambda":str(crit),
  "sharp_lambda_decimal_reference":format(float(crit),'.12f'),
  "continuous_kernel":"K0(m,z)=16/945*(1+a(m,z)+b(m,z)); strictly TP2",
  "prior":"h_lambda=1+a+b+lambda*f(b)*psi((a-ac(b))/d(b))",
  "psi":"smooth positive-on-(0,1] flat bump normalized to integral 1 on [0,1]",
  "ratio_identity":"r_lambda(m)=r0(m)+lambda*(187/8-m)",
  "exact_fosd_parameter_set":"0<=lambda<=sharp_lambda",
  "failure_witness_lambda":"3",
  "failure_m_early":str(p), "failure_m_late":str(q),
  "r_atom_ratio_early_minus_late":str(r_gap),
  "atom_probability_early_minus_late":str(a_gap),
  "fraction_r0_check_count":64,
  "strict_tp2_minor_check_count":tp2_checks,
  "native_bellman_reexecuted":False,
  "project_formal_review":False
}
print(json.dumps(cert,ensure_ascii=False,indent=2))
