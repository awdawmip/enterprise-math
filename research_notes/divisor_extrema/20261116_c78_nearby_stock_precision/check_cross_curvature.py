"""Certify curvature of the physical gradient-direction level at (1,1).

A third-order rational Taylor jet of the signed scalar is enough. A jet
is keyed by its exponents in the two increments, including factorials
in the coefficients. The entire check uses only the standard library.
"""
from fractions import Fraction as F
from math import factorial
import json
from itertools import product

def generalized_binomial(a, i):
    result=F(1)
    for j in range(i):
        result *= (a-j)/(j+1)
    return result

def monomial(a,b):
    return {(i,j):generalized_binomial(F(a),i)*generalized_binomial(F(b),j)
            for i,j in product(range(4),repeat=2) if i+j<=3}

def plus(a,b,factor=1):
    return {key:a.get(key,0)+factor*b.get(key,0) for key in a.keys()|b.keys()}

def mul(a,b):
    result={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if i+j+k+l<=3:
                key=(i+k,j+l)
                result[key]=result.get(key,0)+v*w
    return result

def inverse(a):
    one={(0,0):F(1)}
    scale=1/a[0,0]
    delta=plus(one,a,-scale)
    square=mul(delta,delta)
    result=plus(plus(one,delta),plus(square,mul(square,delta)))
    return {key:v*scale for key,v in result.items()}

def derivative(a,d):
    if d==0:
        return {(i-1,j):i*v for (i,j),v in a.items() if i}
    return {(i,j-1):j*v for (i,j),v in a.items() if j}

def check():
    one={(0,0):F(1)}
    signed=monomial(F(15,4),F(21,2))
    signed=mul(signed,plus(one,monomial(F(15,4),0),-4))
    signed=mul(signed,plus(one,monomial(-F(9,4),F(9,4)),-4))
    signed=mul(signed,inverse(plus(one,monomial(F(51,4),F(9,4)),448)))
    signed=mul(signed,inverse(plus(one,monomial(F(66,4),F(9,4)),1792)))
    gx,gy=derivative(signed,0),derivative(signed,1)
    slope=mul(gx,inverse(gy))
    p,r=slope[1,0],slope[0,1]
    curvature=2*slope[2,0]*r*r-2*slope[1,1]*p*r+2*slope[0,2]*p*p
    assert gy[0,0]==F(130510035,1296233546498)
    assert curvature==F(16419447248012829849022150969912949050415029,
                        326528292421176874878713490630597776400000)
    assert p and r
    return {"signed_y":str(gy[0,0]),"grad_direction_level":["%s"%p,"%s"%r],
            "curvature_numerator":str(curvature)}

if __name__=='__main__':
    print(json.dumps(check(),indent=2))
