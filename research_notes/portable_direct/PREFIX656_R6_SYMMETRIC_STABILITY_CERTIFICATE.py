#!/usr/bin/env python3
"""PREFIX-656: exact rational implication certificate.

Scientific input is the frozen 189-layer signed-survivor statistical observer.
All load-bearing numerical inequalities are inherited strictly from
PREFIX-643/654/655; this code checks their algebraic consequences.
"""
from fractions import Fraction as F
import json

L,R=F(3,20),F(1,6)
z0,h=F(19,128),F(1,2**18)
a,b=z0-h,z0+h
Q0,Q1=F(12),F(24)
C=F(1930)
p_gap={12:F(226),24:F(785)}
z_slope={12:F(9476),24:F(31590)}
checks=0

def ck(cond,label):
    global checks
    assert cond,label
    checks+=1

ck(R-L==F(1,60),"p width")
ck(a==F(38911,262144),"z lower")
ck(b==F(38913,262144),"z upper")
ck(b<L,"disjoint transposed boxes")
ck(a<b,"positive z width")
ck(p_gap[12]/Q0<p_gap[24]/Q1,"p endpoint ratio")
ck(z_slope[12]/Q0<z_slope[24]/Q1,"z endpoint ratio")
ck(C/2==F(965),"strong convexity")
p_scaled=min(p_gap[12]/Q0,p_gap[24]/Q1)
z_scaled=min(z_slope[12]/Q0,z_slope[24]/Q1)
p_linear_coefficient=p_scaled/(R-L)
ck(p_linear_coefficient==F(1130),"p scaled linear deficit")
ck(z_scaled==F(2369,3),"z scaled linear deficit")

slot={}
for q in (12,24):
    cp=p_gap[q]/(R-L)
    cz=z_slope[q]
    ck(cp>0 and cz>0,"positive coefficients "+str(q))
    ck(cp>=p_linear_coefficient*q,"p coefficient "+str(q))
    ck(cz>=z_scaled*q,"z coefficient "+str(q))
    slot[str(q)]={
        "strict_p_linear_coefficient":str(cp),
        "strict_z_linear_coefficient":str(cz),
        "strict_p_quadratic_coefficient":str(F(965)*q*q),
        "p_distance_upper_if_deficit_under_1_over_1000":str(F(1,1000)/cp),
        "z_distance_upper_if_deficit_under_1_over_1000":str(F(1,1000)/cz)
    }

# The proof is analytic: D_q/q and -V_{q,z}/q are affine in q.
# Check the endpoint interpolation constants exactly, plus test values.
for q in (F(12),F(15),F(18),F(21),F(24)):
    lam=(q-Q0)/(Q1-Q0)
    ck((1-lam)*p_gap[12]/Q0+lam*p_gap[24]/Q1>=p_scaled,
       "affine p "+str(q))
    ck((1-lam)*z_slope[12]/Q0+lam*z_slope[24]/Q1>=z_scaled,
       "affine z "+str(q))

# Symbolic symmetry comes from w(n,m)=w(m,n), not a numeric test.
ck(2*a<2*L,"symmetric distinct corners")
variance={
  "12":["47425459/1000","47425460/1000"],
  "24":["192190134/1000","192190135/1000"]
}
for lo,hi in variance.values():
    ck(F(lo)<F(hi),"variance strict interval")

assert checks==29,checks
result={
 "schema":"EM_PREFIX656_SYMMETRIC_ERROR_BOUND_V1",
 "date":"2026-11-10",
 "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "dependencies":[
  "PREFIX-643@ae7872ca18676397fcc0dd9424fb77e08928bee7",
  "PREFIX-654@429849fc4985a5e3b475f09b1d446ab853a15b1b",
  "PREFIX-655@3dc372940c317cf540c96fc02b55284462549bac"],
 "rectangles":{
  "B1":{"first":[str(L),str(R)],"second":[str(a),str(b)]},
  "B2":{"first":[str(a),str(b)],"second":[str(L),str(R)]}},
 "q_range":["12","24"],
 "universal_deficit_coefficients":{
  "first_linear":"1130*q*(p-L)",
  "second_linear":"(2369/3)*q*(z-a)",
  "first_quadratic":"965*q^2*(p-L)*(R-p)"},
 "q_specific":slot,
 "corner_variance_enclosures":variance,
 "corner_set":[[str(L),str(a)],[str(a),str(L)]],
 "source_of_inequalities":"Exact inherited PREFIX643/654/655 bounds and proved affine interpolation / symmetry",
 "checked_only":"Arithmetic and algebraic consequences of inherited strict inequalities",
 "new_native_96port_run":False,
 "checks_passed":checks,
 "result":"ALL_CHECKS_PASS"
}
print(json.dumps(result,indent=2,ensure_ascii=False))
print("ALL_CHECKS_PASS",checks)
