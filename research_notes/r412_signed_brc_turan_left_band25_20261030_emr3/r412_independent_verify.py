#!/usr/bin/env python3
"""R412 independent standard-library integer checks of published coefficient certificate.

This tests selected integer values, including outside SymPy producer's r<=120 grid.
Universal claim continues to rely on producer's exact symbolic rational identity.
"""
import json
from math import comb
from pathlib import Path

s=25
J=json.loads(Path(__file__).with_name('R412_EVIDENCE.json').read_text())
assert J['schema']=='ENTERPRISE_MATH_R412_TURAN_FIXED_S25_ONLY_V1'

def delta_direct(r,s):
    return sum(comb(r-s,j) * ((comb(2*s,r-2*j) if 0<=r-2*j<=2*s else 0) - (comb(2*s,r-2*j-1) if 0<=r-2*j-1<=2*s else 0)) for j in range(r-s+1))

def catalan(n):
    return comb(2*n,n)//(n+1)

def delta_kernel(r,s):
    return sum(comb(s-1,j)*2**(s-1-j)*catalan((r-s+j)//2) for j in range(s) if (r-s+j)%2==0)

def H(r,s):
    return comb(r+s,2*s)*delta_direct(r,s)

def eval_poly(coeff,x):
    y=0
    for a in coeff: y=y*x+a
    return y

runs=0
for c in J['certificates']:
    eps=c['parity']; m0=c['m0']; P=c['numerator_coefficients_desc']; Q=c['denominator_coefficients_desc']
    assert len(P)==25+eps and len(Q)==25+eps and min(P)>0 and min(Q)>0
    for r in [2*m0+eps,2*m0+eps+2,2*m0+eps+100,2*m0+eps+200,2*m0+eps+400]:
        assert r>s and r%2==eps
        for t in (s-1,s,s+1):
            assert delta_direct(r,t)==delta_kernel(r,t)
        D=H(r,s)**2-H(r,s-1)*H(r,s+1)
        B=comb(r+s,2*s)
        C=catalan(r//2-1 if eps==0 else r//2)
        xx=(r-eps)//2-m0
        assert eval_poly(Q,xx)*D==eval_poly(P,xx)*(B*C)**2
        assert D>0
        runs+=1
print('R412_INDEPENDENT_INTEGER_PASS',runs,'points,',runs*3,'Catalan-kernel checks')
