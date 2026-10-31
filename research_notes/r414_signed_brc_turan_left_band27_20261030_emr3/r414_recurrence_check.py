#!/usr/bin/env python3
"""Independent exact triangular Catalan recurrence and bounded Turan scan.
No SymPy or external network required. Recurrence proved by
(1+t)^2=(1+t^2)+2t; no fitted coefficients.
"""
from math import comb
import json
from pathlib import Path

def cat(n):
    return comb(2*n,n)//(n+1)

def direct_delta(r,s):
    return sum(comb(r-s,j) * ((comb(2*s,r-2*j) if 0<=r-2*j<=2*s else 0)
        - (comb(2*s,r-2*j-1) if 0<=r-2*j-1<=2*s else 0))
        for j in range(r-s+1))

def triangular(N):
    prior=[]
    for r in range(N+1):
        current=[0]*(r+1)
        current[r]=cat(r)
        for s in range(r-1,-1,-1):
            current[s]=current[s+1]-2*prior[s]
        yield r,current
        prior=current

def horner(a,x):
    out=0
    for v in a: out=out*x+v
    return out

J=json.loads(Path(__file__).with_name('R414_EVIDENCE.json').read_text())
assert J['schema']=='ENTERPRISE_MATH_R414_TURAN_FIXED_S27_ONLY_V1'
checks=0
new_region_tests=0
cert_checks=0
first_uncovered=None
all28=0
for r,row in triangular(320):
    if r in (4,5,28,29,99,128,155,156,157,255,320):
        for s in range(r+1):
            assert row[s]==direct_delta(r,s),(r,s)
            checks+=1
    def H(s): return comb(r+s,2*s)*row[s]
    if r>=28:
        s=27
        D=H(s)**2-H(s-1)*H(s+1)
        assert D>0,(r,s)
        cert=J['certificates'][r%2]
        x=(r-r%2)//2-cert['m0']
        c=cat(r//2-1 if r%2==0 else r//2)
        assert horner(cert['denominator_coefficients_desc'],x)*D==horner(cert['numerator_coefficients_desc'],x)*(comb(r+s,2*s)*c)**2
        cert_checks+=1
    # Unknown zone after R406 right k<=128, and R414 left s<=27.
    for s in range(28,r-128):
        k=r-s
        assert k>=129
        if first_uncovered is None: first_uncovered=(r,s)
        D=H(s)**2-H(s-1)*H(s+1)
        assert D>0,(r,s)
        new_region_tests+=1
        if s==28: all28+=1
print('R414_RECURRENCE_PASS', 'direct_coefficients=',checks,
      's27_cert_crosschecks=',cert_checks,
      'uncovered_region_positive_grid=',new_region_tests,
      'first_uncovered=',first_uncovered,
      's28_unknown_grid=',all28)
