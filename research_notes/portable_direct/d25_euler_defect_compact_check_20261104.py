#!/usr/bin/env python3
"""D25 finite Euler defect certificate: exact Z-coefficient identities + p^2 Gauss ports."""
from math import comb, isqrt

def primes(N):
    return [p for p in range(5,N+1,2)
            if p%8 in (5,7) and all(p%d for d in range(3,isqrt(p)+1,2))]

def params(p):
    q=p//8
    a,b,c,d=((5*q+3,7*q+4,q,3*q+1) if p%8==5
             else (7*q+6,5*q+4,3*q+2,q))
    return a,b,c,d,(p+1)//2,q

def value(cs,z,m,weighted=False):
    return sum(v*pow(z,k,m)*(1+16*k if weighted else 1)
               for k,v in enumerate(cs))%m

def check(p):
    a,b,c,d,h,q=params(p)
    assert a+b==(3*p-1)//2 and a+d==b+c==p-1
    H=[comb(a,k)*comb(b,k) for k in range(min(a,b)+1)]
    J=[comb(c,k)*comb(d,k) for k in range(q+1)]
    if p<=251:
        Y=[sum((-1)**(n-k)*comb(h,n-k)*J[k]
               for k in range(max(0,n-h),min(n,q)+1))
           for n in range(h+q+1)]
        HH=H+[0]*(len(Y)-len(H))
        assert all((x-y)%p==0 for x,y in zip(HH,Y))
        E=[(x-y)//p for x,y in zip(HH,Y)]
        T=[sum((-1)**(n-k)*comb(h-1,n-k)*J[k]
               for k in range(max(0,n-h+1),min(n,q)+1))
           for n in range(h+q)]
        for n in range(len(E)):
            assert (n+1)**2*(E[n+1] if n+1<len(E) else 0)\
                   -(n-a)*(n-b)*E[n]==h*(T[n] if n<len(T) else 0)
    m=p*p; z=pow(9,-1,m); u=pow(8*z,h,m)
    f,g=1,0
    term=1; f=0; g=0
    for k in range(p):
        t=term*pow(z,k,m)%m
        f=(f+t)%m;g=(g+(16*k+1)*t)%m
        if k+1<p:
            term=term*(8*k+1)*(8*k+3)*pow(64*(k+1)**2,-1,m)%m
    hv=value(H,z,m);jv=value(J,z,m)
    gh=value(H,z,m,True)
    jder=sum(k*v*pow(z,k-1,m) for k,v in enumerate(J) if k)%m
    yv=u*jv%m
    gy=u*(16*z*jder-p*jv)%m
    assert (hv-yv)%p==(gh-gy)%p==0
    # Independent source-operator inversion modulo p, no H-E subtraction.
    B=[comb(h-1,k)*(-1)**k % p for k in range(h)]
    jmod=[v%p for v in J]
    w=[sum(jmod[i]*B[k-i] for i in range(max(0,k-h+1),min(k,q)+1))%p
       for k in range(h+q)]
    ee=[0]
    for k,v in enumerate(w):
        ee.append(((k-a)*(k-b)*ee[-1]+h*v)*pow((k+1)**2,-1,p)%p)
    # Final coefficient may be nonzero; E has degree at most h+q.
    ejet=value(ee,z,p)
    ewjet=value(ee,z,p,True)
    e=((hv-yv)%m)//p;ew=((gh-gy)%m)//p
    assert (e,ew)==(ejet,ewjet),(p,e,ew,ejet,ewjet)
    l=((f-hv)%m)//p;lw=((g-gh)%m)//p
    assert f==(yv+p*(e+l))%m
    assert g==(gy+p*(ew+lw))%m
    if p%24 in (13,23):
        assert jv%p==0 and f==0
    else:
        assert jder%p==0 and g==0
    return (p,e,ew,l,lw)

if __name__=='__main__':
    ps=primes(2000)
    results=[check(p) for p in ps]
    assert len(ps)==157 and sum(p<=251 for p in ps)==28
    print('PASS: 157 original Gauss p^2 / two Euler ports; 28 exact polynomial inhomogeneity')
    print('samples (p,E(z0),weighted-E(z0),Gauss-minus-H jet,weighted jet):')
    for x in results:
        if x[0] in (13,23,29,373): print(x)
