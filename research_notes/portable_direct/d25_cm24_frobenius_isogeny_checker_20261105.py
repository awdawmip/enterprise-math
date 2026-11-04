#!/usr/bin/env python3
"""Independent exact CM−24 Galois/isogeny certificate; Python standard library."""
from math import isqrt
Z=(0,0,0,0); ONE=(1,0,0,0)
def plus(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def sub(x,y): return plus(x,neg(y))
def mul(x,y):
    z=[0]*4
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            c=i&j
            z[i^j]+=a*b*(2 if c&1 else 1)*(3 if c&2 else 1)
    return tuple(z)
def num(n): return (n,0,0,0)
def red(x,p): return tuple(v%p for v in x)
def power(x,n,p=0):
    ans=ONE
    while n:
        if n&1:
            ans=mul(ans,x)
            if p: ans=red(ans,p)
        x=mul(x,x)
        if p: x=red(x,p)
        n//=2
    return ans
def prime(p): return p>=2 and all(p%k for k in range(2,isqrt(p)+1))
def qpoly(t):
    return plus(sub(plus(sub(power(t,4),mul(num(140),power(t,3))),
                        mul(num(294),power(t,2))),mul(num(140),t)),ONE)
def jdiff(t,j):
    lhs=mul(j,mul(power(t,2),power(sub(ONE,t),2)))
    rhs=mul(num(256),power(plus(sub(ONE,t),power(t,2)),3))
    return sub(lhs,rhs)
def run():
    roots={(e,d):(35,24*e,20*d,14*e*d) for e in (-1,1) for d in (-1,1)}
    for (e,d),t in roots.items():
        assert qpoly(t)==Z
        assert jdiff(t,(2417472,1707264*e,0,0))==Z
        assert mul(t,roots[(e,-d)])==ONE
    S=4834944; P=14670139392
    assert P==2417472**2-2*1707264**2
    assert S**3-P**2+1485*P*S-162000*S*S+41097375*P+8748000000*S-157464000000000==0
    count={5:0,13:0}
    for p in range(5,20001):
        if p%24 not in count or not prime(p): continue
        assert pow(2,(p-1)//2,p)==p-1
        assert pow(3,(p-1)//2,p)==(p-1 if p%24==5 else 1)
        for e,d in roots:
            t=roots[(e,d)]
            other=roots[(-e,(-d if p%24==5 else d))]
            assert red(power(t,p,p),p)==red(other,p)
            trace=plus(t,other); norm=mul(t,other)
            if p%24==5:
                assert trace==(70,0,0,28*e*d)
                assert norm==(49,0,0,20*e*d)
            else:
                assert trace==(70,0,40*d,0)
                assert norm==(97,0,56*d,0)
        count[p%24]+=1
    print('PASS exact CM roots/j/Phi2; prime counts:', count,
          'four-branch Frobenius checks:', 4*sum(count.values()))
if __name__=='__main__': run()
