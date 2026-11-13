"""R44 small self-contained exact regression. Python stdlib only."""
from bisect import bisect_right
from fractions import Fraction
from math import isqrt

def enclosure(b):
    d=1<<b; s=isqrt(2*d*d)
    return Fraction(s-d,d), Fraction(s+1-d,d)

def cert_owner(b,m,t):
    d=1<<b;s=isqrt(2*d*d);q=2*d;u=2*s+1-2*d
    hist=sorted(((z*u)%q,z) for z in range(m));rr=[v for v,z in hist]
    for k,(r,z) in enumerate(hist):
        y,a=hist[(k+1)%m];g=(y-r)%q
        if not(g>abs(a-z) and q-g>abs(a-z)):return None
    r=(t*u)%q;k=(bisect_right(rr,r)-1)%m
    a=hist[k][1];z=hist[(k+1)%m][1]
    left=(r-rr[k])%q;right=(rr[(k+1)%m]-r)%q
    g=(rr[(k+1)%m]-rr[k])%q
    if left+right==g and (left>abs(t-a) or t==a and left==0) and right>abs(t-z):
        return k
    return None

def exact_owner(m,t,theta):
    h=sorted(range(m),key=lambda z:(z*theta)%1)
    x=(t*theta)%1
    for k,z in enumerate(h):
        nxt=h[(k+1)%m]
        lo=(z*theta)%1; hi=(nxt*theta)%1
        if (lo<=x<hi) if lo<hi else (x>=lo or x<hi):return k
    raise AssertionError('no owner')

def brute(m,J,N,theta):
    tau=[None]*m
    for t in range(J-N,J):tau[exact_owner(m,t,theta)]=t
    return tau

def run(m,J,N,K):
    dlo,dhi=enclosure(70);theta=(dlo+dhi)/2
    bits=3
    # Initial oracle uses a highly refined enclosure and is checked by
    # a pointwise O(N) enumeration of the source labels.
    tau=brute(m,J,N,theta)
    while any(cert_owner(bits,m,t) is None for t in range(J-N,J)):
        bits+=1
    assert all(cert_owner(bits,m,t)==exact_owner(m,t,theta) for t in range(J-N,J))
    refinements=0
    for t in range(J,J+K):
        while cert_owner(bits,m,t) is None:
            bits+=1;refinements+=1
        k=cert_owner(bits,m,t)
        assert k==exact_owner(m,t,theta)
        before=tau[:];tau[k]=t
        departing=t-N
        if departing in tau:
            bad=tau.index(departing)
            tau[bad]=None
            for s in range(t-N+1,t+1):
                if exact_owner(m,s,theta)==bad:tau[bad]=s
        assert tau==brute(m,t+1,N,theta)
        changed=[i for i,(a,b) in enumerate(zip(before,tau)) if a!=b]
        assert len(changed)<=2
        for x in (t-N,t,t+1):
            pred=lambda a: int(a is None or a<x)
            assert sum(pred(a) for a in tau)-sum(pred(a) for a in before)==sum(pred(tau[i])-pred(before[i]) for i in changed)
    return bits,refinements

if __name__=='__main__':
    for c in ((8,35,30,80),(8,200,60,80),(10,-25,20,80)):
        print('PASS_R44_COMPACT',c,run(*c))
