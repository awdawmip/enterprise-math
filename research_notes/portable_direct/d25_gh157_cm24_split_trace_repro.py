#!/usr/bin/env python3
"""Small exact reproduction of the CM(-24) split trace representation."""
from math import comb,isqrt
def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))
def xy(p):
    z=[]
    for x in range(isqrt(p//2)+1):
        t=p-2*x*x
        if t>=0 and t%3==0:
            y=isqrt(t//3)
            if 3*y*y==t:z.append((x,y))
    return z
def H(p):
    n=(p-1)//2; B=(pow(8,-1,p),pow(12,-1,p)); z=(0,0);v=(1,0)
    for k in range(n//2+1):
        c=comb(n,k)*comb(n-k,k)%p
        z=((z[0]+c*v[0])%p,(z[1]+c*v[1])%p)
        v=((v[0]*B[0]+2*v[1]*B[1])%p,(v[0]*B[1]+v[1]*B[0])%p)
    return z
tested=0
for p in range(11,4000,24):
    if not prime(p):continue
    pairs=xy(p)
    assert len(pairs)==1,(p,pairs)
    x,y=pairs[0]
    assert x%2==0 and y%2==1
    t=6*y*y-4*x*x;h=H(p)
    assert t%p==h[0]**2%p and h[1]==0 and t%8==6
    tested+=1
assert tested==71
assert xy(3347)==[(40,7)]
assert 6*7**2-4*40**2==-6106
assert 3347**2+1+6106==11208516
print("PASS_CM24_SPLIT_TRACE_REPRO",tested,"p3347",-6106,11208516)
