#!/usr/bin/env python3
"""PREFIX-650 exact-rational certificate for signed curvature and two-slot extrapolation.
Inputs are strict cumulant envelopes independently published by PREFIX-649.
This runs no original 189-layer / 96-port simulator.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

a_lo, a_hi = Q(108), Q(110)
b_lo, b_hi = Q(335), Q(338)
c_lo, c_hi = Q(-1266), Q(-1153)
d_lo, d_hi = Q(14638), Q(86111)
t_hi = Q(1,12)
checks = 0

def certify(test, name):
    global checks
    assert test, name
    checks += 1

def serial(x):
    return {"numerator":x.numerator,"denominator":x.denominator,
            "decimal":format(float(x),'.12g')}

B_lower = b_lo-a_hi*t_hi
certify(B_lower>325,"positive denominator")
certify(Q(325)>Q(18)**2,"sqrt denominator lower")
certify(a_lo>0 and b_lo>0 and c_hi<0 and d_lo>0,"strict signs")
N1 = a_hi*(a_hi*a_hi*t_hi*t_hi+a_hi*b_hi*t_hi-15*a_hi*c_lo+28*b_hi*b_hi)
D1 = 4*Q(325)**3*18
M1=N1/D1
certify(M1<Q(1,4),"skew curvature")
certify(N1>0 and D1>0,"skew fraction")
N2=(6*a_hi*a_hi*d_hi+14*b_hi**3-24*a_hi*b_hi*c_lo
    +t_hi*(22*a_hi*b_hi*b_hi-12*a_hi*a_hi*c_lo))
D2=Q(325)**4
M2=N2/D2
certify(M2<Q(3,4),"kurt curvature")
certify(N2>0 and D2>0,"kurt fraction")
q=Q(12)
e1=Q(1,4)/(4*q*q)
e2=Q(3,4)/(4*q*q)
certify(e1==Q(1,2304),"skew extrapolation")
certify(e2==Q(1,768),"kurt extrapolation")
certify(M1/(4*q*q)<e1,"strict skew margin")
certify(M2/(4*q*q)<e2,"strict kurt margin")

def poly_eval(coeffs,t):
    return sum((v*t**k for k,v in enumerate(coeffs)),Q(0))
def derivative(coeffs):
    return [(i+1)*coeffs[i+1] for i in range(len(coeffs)-1)]

# Rational coefficient identity checks at 3 sample points for each
# of 3 parameter witnesses. Symbolic derivation is in the paper.
for a,b,c,d in [(Q(109),Q(337),Q(-1209),Q(50374)),
                (Q(108),Q(335),Q(-1153),Q(14638)),
                (Q(110),Q(338),Q(-1266),Q(86111))]:
    n=[c,-3*b,a]
    dn=derivative(n)
    for t in [Q(0),Q(1,24),Q(1,12)]:
        B= b-a*t
        N=poly_eval(n,t)
        dN=poly_eval(dn,t)
        # D=2*B^(5/2)*g1'(t)
        D=2*dN*B+3*a*N
        certify(-D==6*b*b-3*a*c-a*b*t+a*a*t*t,"first skew derivative")
        dD=2*(2*a*B-a*dN)+3*a*dN
        second_scaled=2*dD*B+5*a*D
        certify(second_scaled==-a*(a*a*t*t+a*b*t-15*a*c+28*b*b),
                "second skew derivative")
        H=2*a*d-6*b*c+(14*b*b-6*a*c)*t-3*a*b*t*t+a*a*t**3
        Hp=14*b*b-6*a*c-6*a*b*t+3*a*a*t*t
        got=Hp*B+3*a*H
        want=6*a*a*d+14*b**3-24*a*b*c+t*(22*a*b*b-12*a*a*c)
        certify(got==want,"second kurt derivative")

payload={
  "record":"PREFIX-650-R6",
  "status":"AUTHOR_PROVED_EXACT_RATIONAL_CHECKED_UNREVIEWED_NOT_ADMITTED",
  "dependencies":["PREFIX-645","PREFIX-648","PREFIX-649"],
  "region":"|p-1/6|<=2^-29; |z-19/128|<=2^-29; q>=12",
  "curvature_bounds":{"skew":"-1/4<gamma1''(t)<0","kurt":"0<gamma2''(t)<3/4"},
  "exact_intermediate":{"B_lower":serial(B_lower),"N1_upper":serial(N1),
    "D1_lower":str(D1),"M1_upper":serial(M1),"N2_upper":serial(N2),
    "D2_lower":str(D2),"M2_upper":serial(M2)},
  "two_slot_bounds":{
    "skew":"gamma1_inf < 2*gamma1(24)-gamma1(12) < gamma1_inf + 1/2304",
    "kurt":"gamma2_inf - 1/768 < 2*gamma2(24)-gamma2(12) < gamma2_inf",
    "general":"skew extrapolation is upper by < 1/(16*q^2); kurt extrapolation lower by < 3/(16*q^2)"},
  "exact_checks_passed":checks,
  "upstream_189_layers_recomputed":False,
  "native_96_port_recomputed":False
}
Path(__file__).with_name("PREFIX650_R6_RESULTS.json").write_text(
    json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"ALL_CHECKS_PASS {checks}")
print("M1",M1,"M2",M2)
print("RICHARDSON_ERRORS_q12",e1,e2)
