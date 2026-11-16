#!/usr/bin/env python3
"""R749SSL exact three-read no-go certificate. Python standard library only."""
from fractions import Fraction as F
import json

def counts(N):
    a=[0]*(N+1);a[0]=1
    for w in (1,1,2,3,6):
        for n in range(w,N+1): a[n]+=a[n-w]
    C=[0]*(N+1);T=[0]*(N+1)
    for q in range(1,N+1):
        C[q]=C[q-1]+a[q-1]
        T[q]=T[q-1]+C[q-1]
    return C,T
C,T=counts(40)
assert [(C[q],T[q]) for q in (7,8,13,14,19,20)]==[(65,91),(98,156),(506,1261),(662,1767),(2106,7447),(2576,9553)]

def S(q): return 18*q**4+54*q**3-345*q**2+2070*q-16315
def Y(q,e,d): return q**3*(F(T[q])+e)/(F(C[q])+d)-F(S(q),108)
def x(j,e):
    q=7+6*j;p=8+6*j
    return (Y(q,e,F(-1))+F(S(p),108))/p**3
def det(rows):
    a,b,c=rows[0];d,e,f=rows[1];g,h,i=rows[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
def cons(e):
    return det([(F(1),-x(j,e),x(j,e)*C[8+6*j]-T[8+6*j]) for j in range(3)])
def P(e): return 5957265452844*e**2-5464016404300823*e+35816460863863
for z in (F(0),F(1),F(2)):
    assert cons(z)==-P(z)/191164619161600000
# cons(e) is degree <=2, so exact equality at three points proves identity.
assert P(F(0))>0 and P(F(1,100))<0
assert 2*5957265452844*F(1,100)-5464016404300823<0

def alt(e):
    H=151241499*e-18047271191
    d=2*(202246101*e+4057501031)/H
    ep=3*(425014044*e*e-46558027037*e-65798686651)/(8*H)
    return ep,d
def inverse(e):
    a=x(0,e);b=x(1,e)
    d=(T[14]-T[8]-b*C[14]+a*C[8])/(b-a)
    ep=a*(C[8]+d)-T[8]
    return ep,d
for z in (F(0),F(1,100),F(1),F(2)):
    assert alt(z)==inverse(z)
    assert x(1,z)-x(0,z)==-(151241499*z-18047271191)/17027727360
# Cross-products of the rational identities have degree <=3:
# four exact test points, with nonzero denominators, prove the formulas.
assert 151241499*F(1,100)-18047271191<0
assert 555733701*F(1,100)-9932269129<0
assert 1275042132*F(1,100)**2-53017890425<0
assert 91360279103-142093945095*F(1,100)>0

out={
 "schema":"R749SSL_THREE_READ_UNKNOWN_CUTOFF_OBSTRUCTION_V1",
 "status":"PASS",
 "cutoffs":[7,8],
 "first_state_d":"-1",
 "first_state_e":"unique root in (0,1/100) of P(e)",
 "P_high_to_low":["5957265452844","-5464016404300823","35816460863863"],
 "determinant_identity":"cons(e)=-P(e)/191164619161600000",
 "alternative":{"H":"151241499*e-18047271191",
  "d":"2*(202246101*e+4057501031)/H",
  "e":"3*(425014044*e^2-46558027037*e-65798686651)/(8*H)",
  "bounds":"-1<d<0 and 1<e<2 on [0,1/100]"},
 "verification":"exact rational determinant polynomial, endpoint isolation signs, 4-point rational inverse identities and interval bounds",
 "scope":"existential three-read real-error collision only; integer and four-read questions open"
}
with open("R749SSL_THREE_READ_EXACT_OBSTRUCTION_RESULTS.json","w",encoding="utf-8") as f:
    json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
print("PASS",out["determinant_identity"])
