"""R64 exact compact verifier; run `python check_r64_min.py`."""
from fractions import Fraction as F
from bisect import bisect_right
from math import floor

def hist(th,m):
    h=sorted((z*th%1,z) for z in range(m))
    assert len(set(v for v,z in h))==m
    return h

def win(th,m,j,x,source,z):
    h=hist(th,m); pos=[v for v,_ in h]
    return max((t for t in source if h[bisect_right(pos,(x+(t-j)*th)%1)-1][1]==z),default=None)

def safe(a,b,L,U):
    v,w=a+b*L,a+b*U
    return floor(v)==floor(w) and v.denominator!=1 and w.denominator!=1

def cert(th,L,U,m,j,x,source,z):
    h=hist(th,m); labs=[a for v,a in h]
    for a,b in zip(labs,labs[1:]+labs[:1]):
        if not safe(F(0),F(a-b),L,U):return False
    nxt=labs[(labs.index(z)+1)%m]
    tstar=win(th,m,j,x,source,z)
    for t in source:
        if tstar is None or t>=tstar:
            if not safe(x,F(t-j-z),L,U) or not safe(x,F(t-j-nxt),L,U):return False
    return True

p=262204504569236716045286;q=10**24
L=F(p,q);U=F(p+1,q);th=F(2*p+1,2*q);j=q+2
src={j-1,j-q}
assert win(F(4*p+1,4*q),2,j,F(0),src,1)==j-1
assert win(F(4*p+3,4*q),2,j,F(0),src,0)==j-q
assert cert(th,L,U,2,j,F(0),src,1)
assert all(win(L+(U-L)*F(i,32),2,j,F(0),src,1)==j-1 for i in range(33))

a=F(1,30);b=F(1003,30000);j=10000;x=F(8,15)
assert win(a,13,j,x,{9,15,6042},12)==6042
assert win(b,13,j,x,{9,15,6042},12)==15
assert not cert(a,a,b,13,j,x,{9,15,6042},12)

# Both times 1 and 8 have the same phase at 2/7; branches at time 8 remain distinct.
th=F(2,7);j=20;x=F(0);z=hist(th,2)[bisect_right([v for v,_ in hist(th,2)],(x+(8-j)*th)%1)-1][1]
assert [win(th,2,j,x,ts,z) for ts in ({1,8},{1,8},{1},set())]==[8,8,1,None]
print('R64_MIN_PASS: frozen selected label, stale-index counterexample, duplicate-phase/branch deletion')
