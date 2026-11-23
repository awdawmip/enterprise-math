#!/usr/bin/env python3
"""Finite BRC observer: exact distribution consistency and convex-order coupling.
Frozen Stage46 candidate W=J12-6I, X6 joint Cell-port-grade observer.
Uses exact A6 collision recurrence and published 3-shift positive-port contrast;
no new native physics or external reference computation.
"""
from fractions import Fraction
from math import comb
from hashlib import sha256
import json


def A6_values(N):
    A=[1,6,66]
    for r in range(2,N+3):
        num=(2*(2*r+1)*(14*r**4+28*r**3+28*r**2+14*r+3)*A[r]
            -4*r**3*(196*r**2+59)*A[r-1]
            +1152*(2*r-1)*r*r*(r-1)**2*A[r-2])
        den=(r+1)**5
        assert num%den==0
        A.append(num//den)
    return A


def contrast(m,A):
    q=(Fraction(-72*(72*m*m+163*m+80),5*(m+1))*A[m+1]
       +Fraction(2*(144*m**3+1135*m*m+2367*m+1310),5*(m+1)*(m+2))*A[m+2]
       -Fraction(2*(m+8)*(2*m+5),5*(m+2))*A[m+3])
    assert q.denominator==1
    return q.numerator


def run(N=240):
    A=A6_values(N)
    a=[contrast(m,A) for m in range(N+1)]
    a0,a1,a2=a[:3]
    assert (a0,a1,a2)==(2412,25620,386028)
    T={}
    row=a[:]
    allh=sha256()
    oldh=sha256()
    for k in range(N+1):
        assert all(z>0 for z in row)
        for m,z in enumerate(row):
            allh.update(f'{m},{k},{z}\n'.encode())
            if m>0: oldh.update(f'{m},{k},{z}\n'.encode())
            if m+k in (1,2,10,30,100,240): T[(m+k,m)]=z
        row=[36*row[i]-row[i+1] for i in range(len(row)-1)]
    if N==240:
        assert oldh.hexdigest()=='ba12049d9510eabf3abef8326249de88d7edcfdf88f1d990d2539a51bae8afc8'
    C=Fraction(36*a1-a2,a0)
    mean=Fraction(a1,a0)
    basevar=Fraction(a2,a0)-mean*mean
    assert C==Fraction(14897,67)
    assert basevar==Fraction(1907744,40401)
    table={}
    for n in (1,2,10,30,100,240):
        if n>N: continue
        p=[Fraction(comb(n,m)*T[(n,m)],a0*36**n) for m in range(n+1)]
        assert all(v>0 for v in p)
        assert sum(p)==1
        y=[Fraction(36*m,n) for m in range(n+1)]
        EY=sum(p[i]*y[i] for i in range(n+1))
        EY2=sum(p[i]*y[i]*y[i] for i in range(n+1))
        assert EY==mean
        assert EY2-mean*mean==basevar+C/n
        table[str(n)]={'positive_bins':n+1,'mean':str(EY),'variance':str(EY2-mean*mean)}
    for n in (2,10,30,100,240):
        prev={m:T[(n-1,m)] for m in range(n)} if n-1 in (1,2,10,30,100,240) else None
        if prev is not None:
            for m in range(n):
                p0=Fraction(comb(n-1,m)*prev[m],a0*36**(n-1))
                p1=(Fraction(n-m,n)*Fraction(comb(n,m)*T[(n,m)],a0*36**n)
                   +Fraction(m+1,n)*Fraction(comb(n,m+1)*T[(n,m+1)],a0*36**n))
                assert p0==p1
    # Exact coupling L2 gap and convexity of x^2 (strict) at n=10,N=240.
    n=10
    gap=C*(Fraction(1,n)-Fraction(1,N))
    assert gap>0
    return {'schema':'PREFIX1029_FINITE_EXCHANGEABLE_CONVEX_ORDER_CHECK_V1',
            'N':N,'positive_pairs':(N+1)*(N+2)//2,
            'old_witness_sha256':oldh.hexdigest(),
            'full_witness_sha256':allh.hexdigest(),
            'mean':str(mean),'baseline_variance':str(basevar),
            'scale_variance_coefficient':str(C),
            'selected_exact_checks':table,
            'coupling_L2_squared_gap_n10_N240':str(gap),
            'status':'EXACT_INTEGER_AND_RATIONAL_CHECK; PAPER_PROOF_NOT_INDEPENDENTLY_REVIEWED'}

if __name__=='__main__':
    cert=run(240)
    with open('/mnt/data/em_prefix1029/PREFIX1029_R6_CONVEX_ORDER_CERT.json','w') as h:
        json.dump(cert,h,indent=2)
        h.write('\n')
    print(json.dumps(cert,indent=2))
