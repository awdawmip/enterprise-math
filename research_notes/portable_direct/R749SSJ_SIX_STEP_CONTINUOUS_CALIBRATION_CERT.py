#!/usr/bin/env python3
"""Exact R749SSJ certificate; Python standard library only."""
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

WEIGHTS=(1,1,2,3,6); BASE=36; DEGREE=11
N=BASE+5+6*DEGREE+6+1
shell=[0]*N; shell[0]=1
for w in WEIGHTS:
    for m in range(w,N):
        shell[m]+=shell[m-w]
mark_shell=[0]*N
for m in range(1,N):
    mark_shell[m]=mark_shell[m-1]+shell[m-1]
C=[0]*N; T=[0]*N
for q in range(1,N):
    C[q]=C[q-1]+shell[q-1]
    T[q]=T[q-1]+mark_shell[q-1]
assert [(C[q],T[q]) for q in (5,6,7,8,11,28)]==[(25,25),(41,50),(65,91),(98,156),(281,600),(10126,51356)]

def g(q,e,d):
    c,cp=C[q]+d,C[q+6]+d
    return (T[q+6]+e)*c-(T[q]+e)*cp-c*cp

def newton(values):
    out=[]
    while values:
        out.append(values[0])
        values=[values[i+1]-values[i] for i in range(len(values)-1)]
    return out

finite=0; least=None
for q in range(6,BASE):
    for e in range(-2,3):
        for d in range(-2,3):
            n=g(q,e,d)
            assert n>0,(q,e,d,n)
            finite+=1
            if least is None or n<least[0]:
                least=(n,q,e,d)
assert least==(39,6,2,-2)

tail=0; minimum=None; eighth=set()
for r in range(6):
    for e in range(-2,3):
        for d in range(-2,3):
            values=[g(BASE+r+6*j,e,d) for j in range(DEGREE+1)]
            a=newton(values)
            assert len(a)==12 and all(z>0 for z in a[:9]) and all(z==0 for z in a[9:]),(r,e,d,a)
            eighth.add(a[8])
            mm=min(a[:9]);minimum=mm if minimum is None else min(minimum,mm)
            tail+=1
assert tail==150 and eighth=={69552} and minimum==69552
lead=Fraction(69552,factorial(8)*6**8)
assert lead==Fraction(23,22394880)
assert lead*4320**2==Fraction(115,6)

# Two different bounded real parameter points have the same first reading.
q=6; u=Fraction(T[q],C[q])
assert u==Fraction(T[q]+u,C[q]+1)
second_0=Fraction(T[q+6],C[q+6])
second_1=Fraction(T[q+6]+u,C[q+6]+1)
assert second_1-second_0==Fraction(-5707,1978660)
assert (C[6],T[6],C[12],T[12])==(41,50,380,881)

# Exact continuous-parameter inverse for one rational test pair.
q=12; e=Fraction(7,5);d=Fraction(-4,3)
x0=Fraction(T[q]+e,C[q]+d)
x1=Fraction(T[q+6]+e,C[q+6]+d)
d2=Fraction(T[q+6]-T[q]-x1*C[q+6]+x0*C[q],x1-x0)
e2=x0*(C[q]+d2)-T[q]
assert (d2,e2)==(d,e)

results={
 "unit":"R749SSJ",
 "status":"PASS",
 "frozen_science_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
 "model":"five labeled positive sources w=(1,1,2,3,6)",
 "q_domain":"integers q>=6",
 "error_domain":"real (e,d) in [-2,2]^2; endpoint/concavity proof extending integer certificate",
 "proved_strict_gap":"X(q+6,e,d)-X(q,e,d)>1 for every integer q>=6 and real e,d in [-2,2]",
 "finite_checks":finite,
 "finite_minimum_gap_numerator":{"value":least[0],"q":least[1],"e":least[2],"d":least[3]},
 "tail_base":BASE,
 "tail_polynomial_degree_bound":DEGREE,
 "positive_tail_certificates":tail,
 "eighth_newton_coefficient":69552,
 "ninth_to_eleventh_newton_differences":"all zero",
 "minimum_positive_newton_coefficient":minimum,
 "asymptotic_q_squared_times_gap_excess":"115/6",
 "real_square_extension":"G decreases in e and is concave in d; e=2,d=±2 suffice",
 "fiber_witness":{"q":6,"pairs":[["0","0"],["50/41","1"]],"first_ratio":"50/41","future_difference":"-5707/1978660"},
 "continuous_parameter_inverse_sample":"PASS",
 "integer_rounding_sufficient_noise_condition":"delta<1/(2*(C_q+C_(q+6)+5)) for each raw-ratio observation",
 "open":"unknown-q smooth Y ordered-pair global injectivity and native signed-BRC interface"
}
Path("R749SSJ_SIX_STEP_CONTINUOUS_CALIBRATION_RESULTS.json").write_text(json.dumps(results,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(results,sort_keys=True,indent=2,ensure_ascii=False))
