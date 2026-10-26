#!/usr/bin/env python3
"""Author-only exact check for third p-adic digit of the negative Green kernel."""
from fractions import Fraction as Q
from math import factorial

def is_prime(p):
    return p>=2 and all(p%d for d in range(2,int(p**0.5)+1))

def C(t):
    return Q(4**t * factorial(t)**2, factorial(2*t))

def F(m):
    return Q(2**(4*m-1)*factorial(2*m-1)*factorial(2*m),factorial(4*m))

def green(m,h):
    p=6*m+1
    out=Q(1,p-2*h-1)
    for k in range(h+1,2*m):
        out*=Q(p-2*k,p-2*k-1)
    return out

def boundary(m):
    p=6*m+1
    out=Q(1)
    for k in range(1-2*m,2*m):
        out*=Q(p-2*k,p-2*k-1)
    return out

def E(N,t):
    return Q(1,2*N+1)-Q(1,2*t+1)+sum((Q(1,2*r-1)-Q(1,2*r) for r in range(t+1,N+1)),Q(0))

def delta(t):
    return sum((Q(1,(2*r-1)**2)-Q(1,(2*r)**2) for r in range(1,t+1)),Q(0))

def mod(x,p,power):
    q=p**power
    assert x.denominator%p, 'not p integral'
    return (x.numerator%q)*pow(x.denominator%q,-1,q)%q

def check(m):
    p=6*m+1
    assert is_prime(p)
    N=2*m-1
    f=F(m)
    tests=0
    for t in range(N):
        first=E(N,t)
        second=Q(1,(2*t+1)**2)+Q(1,(2*N+1)**2)+delta(t)+delta(N)
        pred=-f*C(t)/Q(2*t+1)*(1+p*first+Q(p*p,2)*(first*first+second))
        actual=green(m,-t-1)/p
        assert mod(actual-pred,p,3)==0,(p,t,'negative',mod(actual-pred,p,3))
        tests+=1
    pred=-f*C(N)*(1+Q(p,2*N+1)+p*p*(delta(N)+Q(1,(2*N+1)**2)))
    actual=boundary(m)/p
    assert mod(actual-pred,p,3)==0,(p,'boundary',mod(actual-pred,p,3))
    tests+=1
    # Independently test the channel-tagged exact Ward identity at p^3.
    if m<=7:
        import importlib.util
        from pathlib import Path
        src=Path(__file__).with_name('20261026_hourly_d25_negative_orientation_source_adjoint_r11_check.py')
        spec=importlib.util.spec_from_file_location('d25_lower_adj',src)
        obj=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(obj)
        jets,moments,source,CHANNELS=obj.jets,obj.moments,obj.source,obj.CHANNELS
        u=jets(m)
        L=1-2*m
        for a,b in CHANNELS:
            S={n:source(m,u,a,b,n) for n in range(L,2*m)}
            YL=moments(m,u,a,b,L,1)-Q(p-L,2)*moments(m,u,a,b,L)
            direct=sum((green(m,h)*S[h] for h in range(2*m)),Q(0))/(p*f)
            pred=Q(0)
            for t in range(N):
                first=E(N,t)
                second=Q(1,(2*t+1)**2)+Q(1,(2*N+1)**2)+delta(t)+delta(N)
                pred+= C(t)/Q(2*t+1)*(1+p*first+Q(p*p,2)*(first*first+second))*S[-t-1]
            pred-=C(N)*(1+Q(p,2*N+1)+p*p*(delta(N)+Q(1,(2*N+1)**2)))*YL
            assert mod(direct-pred,p,3)==0,(p,a,b,'three-digit source Ward')
            tests+=1
    return p,tests

if __name__=='__main__':
    total=0
    for m in range(1,25):
        if is_prime(6*m+1):
            p,k=check(m)
            print('p=',p,'third-digit PASS=',k)
            total+=k
    print('ALL THIRD-DIGIT ASSERTIONS PASS=',total)
