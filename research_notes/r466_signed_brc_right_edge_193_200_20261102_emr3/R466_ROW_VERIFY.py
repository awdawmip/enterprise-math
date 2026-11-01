#!/usr/bin/env python3
"""R466 exact integer row verification for r=217,219,221,223."""
from math import comb
from hashlib import sha256

def cat(n): return comb(2*n,n)//(n+1)
def a_row(r):
    k=(r-1)//2
    return [comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*cat(k-q)
           for q in range((s-1)//2+1)) for s in range(r,1,-1)]
def raw(r,s):
    h=r-s
    def c(n,j): return comb(n,j) if 0<=j<=n else 0
    return comb(r+s,2*s)*sum(comb(h,q)*(c(2*s,r-2*q)-c(2*s,r-2*q-1)) for q in range(h+1))
def alt(r,s):
    h=r-s
    return comb(2*r-h,h)*sum(comb(h,q)*(-2)**q*cat(r-q) for q in range(h+1))
def feed(d,n):
    assert n>=0
    b=n.to_bytes(max(1,(n.bit_length()+7)//8),'big')
    d.update(len(b).to_bytes(4,'big')); d.update(b)
cs,ms=sha256(),sha256()
number=raw_checks=0
for r in (217,219,221,223):
    a=a_row(r); assert len(a)==r-1
    def z(j): return a[j] if 0<=j<len(a) else 0
    for j,x in enumerate(a):
        assert x>0; feed(cs,x)
        d2=x*x-z(j-1)*z(j+1)
        d3=x**3-2*x*z(j-1)*z(j+1)+z(j-2)*z(j+1)**2+z(j-1)**2*z(j+2)-z(j-2)*x*z(j+2)
        assert d2>0 and d3>0,(r,j)
        feed(ms,d2); feed(ms,d3); number+=1
    for s in sorted({2,3,4,(r+1)//2,r-3,r-2,r-1,r}):
        assert a[r-s]==raw(r,s)==alt(r,s),(r,s)
        raw_checks+=1
assert number==876 and raw_checks==32
assert cs.hexdigest()=='833ac4906729cfec0c48a218e27ca0b462e26d17c65d090a09e0cd69d0106549'
assert ms.hexdigest()=='46034ba3ec0ded7a6f8b1e7030d61a2ea0b5b0af32755c6b99e17486b12f42df'
print('R466_ROW_EXACT_PASS',number*3,raw_checks,cs.hexdigest(),ms.hexdigest())
