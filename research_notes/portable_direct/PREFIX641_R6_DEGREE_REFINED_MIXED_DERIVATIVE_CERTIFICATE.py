#!/usr/bin/env python3
"""PREFIX-641 exact integer and rational implication certificate.

Inputs: the fixed statistical observer moments (PREFIX-622);
full z-bracket endpoint gradient signs (PREFIX-631); and
center-slice Bernstein certificate (PREFIX-639).
Does not run the original native graph or the parent recurrence.
"""
from fractions import Fraction as F
from json import dumps
from pathlib import Path

N=189
h=F(1,2**26)
z0=F(19,128)
p0,p1=F(3,20),F(1,6)
checks=[]
def ck(name,ok):
    assert ok,name
    checks.append(name)

# Degree-specific Bernstein survivor derivative control sums.
A=sum(n for n in range(N))
B=2*sum(n*(n-1) for n in range(N))
C=sum(n*(n+1) for n in range(N))
D=2*sum(n*(n-1)*(n+1) for n in range(N))
E=sum(n for n in range(N))+sum(n+1 for n in range(N))
J=2*sum(n*(n-1)*(n+1)*(n+2) for n in range(N))
K=2*(J+2*A*C+E*B+2*N*D)+F(D,12)
Kold=25*N*N*(N-1)**3
ck("A_exact",A==17766)
ck("B_exact",B==4429656)
ck("C_exact",C==2250360)
ck("D_exact",D==631225980)
ck("E_exact",E==35721==N*N)
ck("J_exact",J==96451329744)
ck("K_new_exact",K==1146545169525)
ck("K_improves_old",K<Kold)
ck("moment_equality",all((n+1)*(n+2)==(n+1)**2+(n+1) for n in range(N)))
ck("z_band_in_parent",F(37,256)<z0-h<z0+h<F(39,256))
ck("mu_p_lower",F(274)-C*h>273)
ck("mu_p_upper",F(321)+C*h<322)
ck("curvature_margin",K*h<F(17100))
ck("curvature_lower",F(27100)-K*h>10000)
ck("curvature_upper",F(48100)+K*h<65200)
ck("q_integral",F(1,12)-F(1,24)==F(1,24))
ck("valley_gap_lower",F(273,65200)/24==F(91,521600))
ck("valley_gap_upper",F(322,10000)/24==F(161,120000))
ck("valley_order_and_width",0<F(91,521600)<F(161,120000)<p1-p0)
ck("radius_growth",h/F(1,2**28)==4)
ck("strong_concavity_lower",F(273**2,65200)>1)
ck("strong_concavity_upper",F(322**2,10000)<11)
ck("gap_improvement_low",F(91,521600)>F(91,568000))
ck("gap_improvement_up",F(161,120000)<F(161,48000))

result={
 "schema":"PREFIX641_R6_DEGREE_REFINED_GLOBAL_MIXED_DERIVATIVE_V1",
 "frozen_scientific_input":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "parent_provenance":["PREFIX-622 exact moment identities","PREFIX-631 full transverse band endpoint gradient signs","PREFIX-639 central slice Bernstein coefficient envelopes"],
 "bounds":{"N":N,"A":A,"B":B,"C":C,"D":D,"E":E,"J":J,
 "K2":str(K),"previous_K2":str(Kold),"radius":str(h),
 "K2_h":str(K*h),"K0_h":str(C*h),
 "p1":"[3/20,1/6]","p2":"[19/128-2^-26,19/128+2^-26]",
 "q":"[12,24] real","mu_p":"273 < mu_p < 322",
 "Fq_pp":"10000 < Fq_pp < 65200",
 "c12_minus_c24":"91/521600 < c(12,z)-c(24,z) < 161/120000",
 "-Phi_tt":"273^2/65200 < -Phi_tt < 322^2/10000"},
 "checks":checks,"status":"ALL_CHECKS_PASS",
 "review":"AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED",
 "scope":"Finite signed two-information-direction statistical observer; frozen native graph and parent Bernstein computation are not rerun"
}
if __name__=="__main__":
    Path(__file__).with_name("PREFIX641_R6_RESULTS.json").write_text(
      dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS",len(checks))
    print("K2",K,"previous",Kold,"K2*h",K*h)
