#!/usr/bin/env python3
"""Exact checker for EM-FREE-F6D046-R14 P46 arithmetic audit."""
from math import gcd
from functools import reduce
import json
import sympy as sp

T,t=sp.symbols('T t')
A=t**4+24*t**3+192*t**2+528*t+144
D=t**2+12*t+24
checks={}
checks['disc_A']=sp.discriminant(A,t)==-(2**16)*(3**5)
checks['disc_D']=sp.discriminant(D,t)==(2**4)*3
checks['resultant_A_D']=sp.resultant(A,D,t)==-(2**8)*(3**3)
checks['genus_C46']=2*5-2==2*(2*1-2)+8
checks['prym_dimension']=5-1==4

local={
  5:[1,0,0,0,-30,0,0,0,625],
  7:[1,0,5,0,0,0,245,0,2401],
  11:[1,0,4,0,22,0,484,0,14641],
  13:[1,0,25,-40,328,-520,4225,0,28561],
}
for p,c in local.items():
    checks[f'functional_{p}']=(c[8]==p**4 and c[7]==p**3*c[1] and c[6]==p**2*c[2] and c[5]==p*c[3])
checks['factor_13']=sp.expand((1+4*T+13*T**2)*(1-4*T+28*T**2-100*T**3+364*T**4-676*T**5+2197*T**6))==sum(local[13][i]*T**i for i in range(9))

# Exact Rabin irreducibility certificate search for P_7 after reduction mod ell.
def trim(a,l):
    a=[x%l for x in a]
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b,l):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]=(c[i]+x)%l
    for i,x in enumerate(b):c[i]=(c[i]+x)%l
    return trim(c,l)
def sub(a,b,l):return add(a,[(-x)%l for x in b],l)
def mul(a,b,l):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%l
    return trim(c,l)
def divmodp(a,b,l):
    a=trim(a,l);b=trim(b,l);q=[0]*max(1,len(a)-len(b)+1);inv=pow(b[-1],-1,l)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b);u=a[-1]*inv%l;q[k]=u
        for j,x in enumerate(b):a[j+k]=(a[j+k]-u*x)%l
        a=trim(a,l)
    return trim(q,l),trim(a,l)
def monic(a,l):
    a=trim(a,l);u=pow(a[-1],-1,l);return [(u*x)%l for x in a]
def gcdp(a,b,l):
    while trim(b,l)!=[0]:_,r=divmodp(a,b,l);a,b=b,r
    return monic(a,l)
def modp(a,f,l):return divmodp(a,f,l)[1]
def powmodp(a,n,f,l):
    out=[1];a=modp(a,f,l)
    while n:
        if n&1:out=modp(mul(out,a,l),f,l)
        a=modp(mul(a,a,l),f,l);n//=2
    return trim(out,l)

P7=local[7]
certificate=None
for ell in list(sp.primerange(2,200)):
    if P7[-1]%ell==0:continue
    f=monic(P7,ell);x=[0,1]
    r8=powmodp(x,ell**8,f,ell)
    r4=powmodp(x,ell**4,f,ell)
    g=gcdp(f,sub(r4,x,ell),ell)
    if r8==x and g==[1]:
        certificate={'ell':ell,'monic_coefficients_ascending':f,'x_ell8_remainder':r8,'gcd_x_ell4_minus_x':g}
        break
checks['P7_rabin_certificate']=certificate is not None
checks['P7_Q_irreducible']=bool(sp.Poly(sum(P7[i]*T**i for i in range(9)),T,domain=sp.QQ).is_irreducible)
checks['inert_even_7']=all(P7[i]==0 for i in range(1,9,2))
checks['inert_even_11']=all(local[11][i]==0 for i in range(1,9,2))

out={
 'schema':'EM_FREE_F6D046_P46_ARITHMETIC_AUDIT_VERIFICATION_V1',
 'researcher_id':'EM-FREE-F6D046',
 'research_unit':'EM-FREE-F6D046-R14-P46-ARITHMETIC-AUDIT',
 'all_passed':all(checks.values()),
 'check_count':len(checks),
 'checks':checks,
 'irreducibility_certificate_p7':certificate,
 'theorem':'P46_IS_Q_SIMPLE',
 'boundary':'GEOMETRIC_SIMPLICITY_NOT_IMPLIED'
}
print(json.dumps(out,ensure_ascii=False,indent=2))
raise SystemExit(0 if out['all_passed'] else 1)
