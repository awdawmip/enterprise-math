#!/usr/bin/env python3
"""PREFIX-651 exact rational implication certificate. See accompanying proof."""
from fractions import Fraction as Q
from pathlib import Path
import json

passed=[]
def verify(k,truth):
    assert truth,k
    passed.append(k)
def obj(x):
    return {"numerator":x.numerator,"denominator":x.denominator}

alo,ahi=Q(108),Q(110)
blo,bhi=Q(335),Q(338)
clo,chi=Q(-1266),Q(-1153)
dlo,dhi=Q(14638),Q(86111)
t=Q(1,12)
Bmin=blo-ahi*t
verify("B_lower",Bmin==Q(1955,6))
verify("B_positive",Bmin>325)
verify("sqrt_B_lower",325>18**2)
verify("input_signs",alo>0 and blo>0 and chi<0 and dlo>0)
N1=3*ahi**2*(ahi**2*t**2+3*ahi*bhi*t-35*ahi*clo+66*bhi**2)
D1=8*Q(325)**4*18
N2=6*ahi*(4*ahi**2*dhi+11*ahi*bhi**2*t-6*ahi**2*clo*t-18*ahi*bhi*clo+13*bhi**3)
D2=Q(325)**5
M1,M2=N1/D1,N2/D2
verify("M1_exact",M1==Q(54117127669,192786750000))
verify("M2_exact",M2==Q(730778040872,725181640625))
verify("M1_lt_3_10",0<M1<Q(3,10))
verify("M2_lt_11_10",0<M2<Q(11,10))
weights=[Q(1,3),-Q(2),Q(8,3)]
nodes=[Q(1),Q(1,2),Q(1,4)]
for degree in range(3):
    verify("Lagrange_degree_"+str(degree),
           sum(w*x**degree for w,x in zip(weights,nodes))==(1 if degree==0 else 0))
verify("cubic_interpolation_constant",sum(w*x**3 for w,x in zip(weights,nodes))==Q(1,8))
q=Q(12)
e1,e2=Q(3,10)/(48*q**3),Q(11,10)/(48*q**3)
verify("skew_q12",e1==Q(1,276480))
verify("kurt_q12",e2==Q(11,829440))
verify("strict_skew_margin",M1/(48*q**3)<e1)
verify("strict_kurt_margin",M2/(48*q**3)<e2)

# Polynomial differentiation identities after clearing fractional powers.
def val(v,t):return sum(x*t**i for i,x in enumerate(v))
def deriv(v):return [i*v[i] for i in range(1,len(v))]
for a,b,c,d in [(Q(109),Q(337),Q(-1209),Q(50374)),
                (Q(108),Q(335),Q(-1153),Q(14638)),
                (Q(110),Q(338),Q(-1266),Q(86111))]:
    for s in (Q(0),Q(1,24),Q(1,12)):
        B=b-a*s
        N=[c,-3*b,a];Np=deriv(N)
        D=2*val(Np,s)*B+3*a*val(N,s)
        Dp=2*val(deriv(Np),s)*B+a*val(Np,s)
        E=2*Dp*B+5*a*D
        U=-a*(a*a*s*s+a*b*s-15*a*c+28*b*b)
        Up=-a*(2*a*a*s+a*b)
        verify("second_skew_"+str(len(passed)),E==U)
        verify("third_skew_"+str(len(passed)),
               2*B*Up+7*a*U ==
               -3*a*a*(a*a*s*s+3*a*b*s-35*a*c+66*b*b))
        H=6*a*a*d+14*b**3-24*a*b*c+s*(22*a*b*b-12*a*a*c)
        Hp=22*a*b*b-12*a*a*c
        verify("third_kurt_"+str(len(passed)),
               Hp*B+4*a*H ==
               6*a*(4*a*a*d+11*a*b*b*s-6*a*a*c*s-18*a*b*c+13*b**3))

result={"record":"PREFIX-651-R6",
 "status":"AUTHOR_PROVED_EXACT_RATIONAL_IMPLICATION_CHECKED_UNREVIEWED_NOT_ADMITTED",
 "frozen_scientific_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "domain":"abs(p-1/6)<=2^-29; abs(z-19/128)<=2^-29; q,2q,4q admissible, q>=12",
 "bounds":{"g1_third":"-3/10<g1'''<0","g2_third":"0<g2'''<11/10",
           "M1":obj(M1),"M2":obj(M2)},
 "q12_error":{"skew":obj(e1),"kurt":obj(e2)},
 "checks_passed":len(passed),"check_names":passed,
 "dependencies":["PREFIX-645","PREFIX-648","PREFIX-649","PREFIX-650"],
 "reran_189_layer":False,"reran_native_96_port":False}
Path(__file__).with_name("PREFIX651_R6_RESULTS.json").write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS",len(passed))
print("M1",M1,"M2",M2)
