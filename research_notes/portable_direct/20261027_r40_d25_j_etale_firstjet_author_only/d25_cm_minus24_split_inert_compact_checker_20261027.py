#!/usr/bin/env python3
"""Finite exact CM(-24)-shaped trace check; not an infinite theorem or native run."""
from math import isqrt

LIMIT = 40000
s = bytearray([1]) * LIMIT
s[0] = s[1] = 0
for q in range(2, isqrt(LIMIT-1)+1):
    if s[q]:
        s[q*q::q] = bytes([0])*(1+(LIMIT-1-q*q)//q)
counts = {1: 0, 7: 0, 13: 0, 19: 0}
for p in range(7,LIMIT):
    if not s[p] or p%6 != 1:
        continue
    r=(p-1)//6
    t=a=1
    inv=[0]*(r+1)
    inv[1]=1
    for k in range(2,r+1):
        inv[k]=-(p//k)*inv[p%k]%p
    for k in range(1,r+1):
        t=t*(r-k+1)*(2*r-k+1)*((p+1)//2)*inv[k]**2%p
        a=(a+t)%p
    f=[1]*(2*r+1)
    for k in range(1,2*r+1):
        f[k]=f[k-1]*k%p
    g=[1]*(2*r+1)
    g[-1]=pow(f[-1],p-2,p)
    for k in range(2*r,0,-1):
        g[k-1]=g[k]*k%p
    b=0
    halfk=1
    for k in range(r+1):
        b=(b+f[r]*g[k]*g[r-k]*f[2*r]*g[k]*g[2*r-k]*halfk)%p
        halfk=halfk*((p+1)//2)%p
    assert a==b,(p,"two routes")
    reps=[]
    for v in range(isqrt(p//6)+1):
        z=p-6*v*v
        x=isqrt(z)
        if x*x==z:
            reps.append((x if x%3==1 else -x,v))
    m=p%24
    assert (pow((-6)%p,(p-1)//2,p)==1)==(m in (1,7))
    if m in (1,7):
        assert len(reps)==1 and a==(2*reps[0][0])%p,(p,a,reps)
    else:
        assert a==0 and not reps,(p,a,reps)
    counts[m]+=1
assert counts=={1:501,7:526,13:532,19:530}
print("PASS 2089 p<40000",counts,"inert_zeros=1062 split_matches=1027")
