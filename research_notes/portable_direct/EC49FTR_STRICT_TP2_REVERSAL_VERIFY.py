#!/usr/bin/env python3
"""EC49FTR: exact rational bounds for smooth strict-TP2 atom reversal.
External price prior, no native Bellman rerun; standard library only.
"""
from fractions import Fraction as F
import json

p,q,t=F(23),F(93,4),F(3071,4096)
L=lambda m:(8*m+173)/480
A=lambda m:(8*m-187)*(328*m-339677)/F(4286520000)
B=lambda m:-(64*m-1055)*(256*m-35545)/F(43893964800)
X=lambda m:(740-m)/945
B_unit=lambda m:(F(49,64)-X(m))/54
C=1000

def primitive(m,z):
    return F(16,945)*((1+(47-m)/945+F(1,27)-m/54)*z
                    +(F(44,45)+F(10,9))*z*z/2)
def numerator(m):return primitive(m,t)-primitive(m,L(m))

# Exact lower bound J>1/162 for Phi(s)=exp(-1/s^2) on (0,1]:
# on [1/2,1], Phi>=exp(-4)>1/81 because e<3.
rp_lower=(B(p)+C*B_unit(p)/162)/A(p)
rq=B(q)/A(q)
F_early_upper=numerator(p)/(A(p)+B(p)+C*B_unit(p)/162)
F_late=numerator(q)/(A(q)+B(q))
assert F(1469,64)<p<q<F(187,8)
assert L(q)<t<F(3,4)
assert rp_lower-rq==F(158980872564325,190572643785024)>0
assert F_late==F(4802228009,25942353984)
assert F_early_upper==F(141169363569,823185364544)
assert F_late-F_early_upper==F(284041223446367875,20854849727977080804)>0

# Independent C^3 polynomial witness: C=100, Phi(s)=max(s,0)^4, J=1/5.
F_polynomial_early=numerator(p)/(A(p)+B(p)+F(100,5)*B_unit(p))
assert F_polynomial_early==F(5228494947,71818503872)
assert F_polynomial_early<F_late

print(json.dumps({
 "schema":"EC49FTR_STRICT_TP2_REVERSAL_CERT_V1",
 "parent":"EC49FTR PR2795",
 "frozen_science":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
 "density":"h_C(a,b)=1+a+b+1000*((b-95/216)/(1/216))^2*Phi((a-(77+6b)/105)/(139/20160))",
 "Phi":"0 for s<=0 and exp(-1/s^2) for s>0",
 "continuous_kernel":"strictly TP2, inherited from h0=1+a+b, unchanged on nonclipped supports",
 "p":str(p),"q":str(q),"z_threshold":str(t),
 "r_p_strict_lower_minus_r_q":str(rp_lower-rq),
 "F_q_exact":str(F_late),"F_p_strict_upper":str(F_early_upper),
 "F_q_minus_F_p_lower":str(F_late-F_early_upper),
 "C3_polynomial_F_p":str(F_polynomial_early),
 "status":"AUTHOR_PROVED_EXACT_RATIONAL_BOUND_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED"
},ensure_ascii=False,indent=2))
