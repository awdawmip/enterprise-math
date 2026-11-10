#!/usr/bin/env python3
"""Exact p-power cubic-moment carry checker. Author-side, NOT native H0/B0."""
from math import comb

def valuation_unit(x,p):
    v=0
    while x%p==0:
        x//=p
        v+=1
    return v,x

def exact_coefficient_stream(p,n,precision):
    modulus=p**precision
    v,u=0,1
    constant=pow(36,-1,modulus)
    for k in range(n):
        yield k,(u*p**v)%modulus if v<precision else 0,v
        if k+1==n:
            break
        factor=constant
        for z in (2*k+1,3*k+1,3*k+2):
            e,t=valuation_unit(z,p)
            v+=e
            factor=factor*t%modulus
        e,t=valuation_unit(k+1,p)
        v-=3*e
        assert v>=0,(p,k,v)
        factor=factor*pow(t,-3,modulus)%modulus
        u=u*factor%modulus

def verify(p,r):
    n=p**r
    modulus=p**(3*r+1)
    moments=[0]*4
    for k,a,v in exact_coefficient_stream(p,n,3*r+1):
        for j in range(min(k,3)+1):
            moments[j]=(moments[j]+comb(k,j)*a)%modulus
    observed=(27*(moments[2]+2*moments[3])-moments[0]-11*moments[1])%modulus
    expected=(-p**(3*r))%modulus
    assert observed==expected,(p,r,observed,expected)
    return p,r,n,observed

if __name__=="__main__":
    tests=((5,2),(7,2),(7,3),(11,2),(13,2),(19,2),(31,2))
    for p,r in tests:
        print("PASS",*verify(p,r))
