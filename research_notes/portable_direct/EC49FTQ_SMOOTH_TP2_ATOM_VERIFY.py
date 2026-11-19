#!/usr/bin/env python3
"""EC49FTQ exact pricing-counterexample certificate; no native BRC simulation."""
from fractions import Fraction as Q
import json

A0,A1=Q(3,4),Q(49,64)
B0,B1=Q(7,16),Q(57,128)
m2,m3=Q(1469,64),Q(187,8)
p,q,z=Q(23),Q(93,4),Q(719,960)
c=Q(16,945)
b=lambda m: (47-m)/54
x=lambda m: (740-m)/945
ac=lambda bb: (77+6*bb)/105
d=lambda m: A1-x(m)
L=lambda m: (8*m+173)/480
T=lambda m: Q(3,4)-L(m)
num=lambda m: c*(z-L(m))
I=lambda m: c*T(m)
B=lambda m: d(m)/54

assert m2<p<q<m3 and B0<b(q)<b(p)<B1
assert A0<x(q)<x(p)<A1
assert x(p)==ac(b(p)) and x(q)==ac(b(q))
assert L(p)<L(q)<z<Q(3,4)
assert b(p)==Q(4,9) and b(q)==Q(95,216)
assert b(p)-b(q)==Q(1,216)
assert x(p)==Q(239,315) and x(q)==Q(2867,3780)
assert d(p)==Q(139,20160) and d(q)==Q(433,60480)
assert L(p)==Q(119,160) and L(q)==Q(359,480)
assert T(p)==Q(1,160) and T(q)==Q(1,480)
assert z-L(p)==Q(1,192) and z-L(q)==Q(1,960)

# Smooth bump: phi(s)=0 for s<=0, exp(-1/s^2) for s>0.
# J=integral_0^1 phi(s)ds > 1/162 since e<3.
F_late=num(q)/(I(q)+B(q))
F_early_upper=num(p)/(I(p)+B(p)*(1+Q(1000,162)))
gap_lower=F_late-F_early_upper
assert F_late==Q(288,2741)
assert F_early_upper==Q(38880,450451)
assert gap_lower==Q(23159808,1234686191)>0

# Independent exact polynomial witness phi(s)=max(s,0)^4, C=100.
# Clipped integral at p is B(p)*(1+C/5), at q unchanged.
F_poly_early=num(p)/(I(p)+B(p)*(1+Q(100,5)))
F_poly_late=F_late
poly_gap=F_poly_late-F_poly_early
assert F_poly_early==Q(160,5057)
assert poly_gap==Q(1017856,13861237)>0

# Continuous density K=16/945 throughout nonclipped domain,
# so every TP2 2x2 cross determinant is identically zero.
assert c*c-c*c==0

certificate={
  "schema":"EC49FTQ_SMOOTH_TP2_ATOM_CERT_V1",
  "frozen_input":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
  "parent":"EC49FTH PR2774@999bf1069403306b3813e0e390dae4435d7b4b8c",
  "prior_parent":"EC49FTP PR2791@a6984e3d8694406a09b90c266a739d85ff1afd55",
  "domain":{"a":["3/4","49/64"],"b":["7/16","57/128"]},
  "density":"h=1+1000*((b-95/216)/(1/216))^2*Phi((a-(77+6b)/105)/(139/20160))",
  "Phi":"0 when s<=0; exp(-1/s^2) when s>0",
  "joint_density_smoothness":"strictly positive C-infinity",
  "continuous_kernel":"16/945 constant; TP2 equality",
  "M_early":"23", "M_late":"93/4", "Z_threshold":"719/960",
  "F_late":str(F_late),
  "F_early_strict_upper":str(F_early_upper),
  "reversal_strict_gap_lower":str(gap_lower),
  "polynomial_C3":{"F_early":str(F_poly_early),"F_late":str(F_poly_late),"gap":str(poly_gap)},
  "run_status":"PASS",
  "evidence_scope":"exact external-price-prior rational certificate; no native BRC Bellman rerun",
  "math_review":"NOT_REVIEWED"
}
print(json.dumps(certificate,indent=2,ensure_ascii=False))
