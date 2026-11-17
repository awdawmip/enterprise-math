#!/usr/bin/env python3
"""Exact W59A Dirichlet rate-gauge polynomial checks: stdlib only."""
from fractions import Fraction as F

def poly_mul_linear(a, constant):
    out=[F(0)]*(len(a)+1)
    for i,v in enumerate(a):
        out[i] += constant*v
        out[i+1] += v
    return out

def poly_sub(a,b):
    return [(a[i] if i<len(a) else F(0))-(b[i] if i<len(b) else F(0))
            for i in range(max(len(a),len(b)))]

def det_x_minus_cL(n,c):
    # D_n=(x-2c)D_(n-1)-c**2 D_(n-2).
    d0=[F(1)]
    if n==0:return d0
    d1=[-2*c,F(1)]
    for k in range(2,n+1):
        d2=poly_sub(poly_mul_linear(d1,-2*c),[c*c*x for x in d0])
        d0,d1=d1,d2
    return d1

def check():
    scales=(F(1,2),F(3,5),F(1),F(2),F(7,3))
    cases=0
    for M in range(2,11):
        n=M-1
        baseline=det_x_minus_cL(n,F(1))
        for c in scales:
            poly=det_x_minus_cL(n,c)
            assert poly==[b*c**(n-j) for j,b in enumerate(baseline)]
            # An interior step or boundary-to-cemetery step has rate c.
            assert c/(2*c)==F(1,2)
            cases+=1
    assert cases==45
    return {"cases":cases,"M":"2..10","scales":list(map(str,scales)),
            "exact_rational":True,"mathematical_acceptance":False}

if __name__=="__main__":
    print(check())
