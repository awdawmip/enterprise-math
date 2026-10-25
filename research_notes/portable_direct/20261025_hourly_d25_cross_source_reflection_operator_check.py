#!/usr/bin/env python3
"""Exact modular author checks for a D25 cross-source reflection kernel. No native CM run."""
from math import comb

def primes(limit):
    return [p for p in range(7,limit+1) if p%6==1 and all(p%d for d in range(2,int(p**.5)+1))]

def check(p, original=True):
    m=(p-1)//6
    f=[1]*p
    for n in range(1,p):f[n]=f[n-1]*n%p
    def div(a,b):
        assert b%p
        return (a%p)*pow(b%p,-1,p)%p
    u=[comb(m,j)*comb(2*m,j)%p for j in range(m+1)]
    c=[]
    for ell in range(1,m+1):
        n=p-ell
        # Direct two-zero derivative formula; independent of Wilson complement.
        a=div(2*(-1)**m*f[m]*f[2*m]*f[n-m-1]*f[n-2*m-1],f[n]**2)
        b=div(2*f[m]*f[2*m]*f[ell-1]**2,f[m+ell]*f[2*m+ell])
        assert a==b,(p,ell,a,b)
        c.append(a)
    assert c[0]==div(18,5)
    for ell in range(1,m):
        assert c[ell]==div(c[ell-1]*ell**2,(m+ell+1)*(2*m+ell+1))
    # L=theta^2-z(theta-m)(theta-2m) on negative Laurent V.
    L={}
    for ell,v in enumerate(c,1):
        L[-ell]=(L.get(-ell,0)+ell**2*v)%p
        L[1-ell]=(L.get(1-ell,0)-(ell+m)*(ell+2*m)*v)%p
    edge=m*m*c[-1]%p
    assert {e:v for e,v in L.items() if v}=={0:p-2,-m:edge},(p,L)
    # L U=0, coefficientwise.
    LU={}
    for j,v in enumerate(u):
        LU[j]=(LU.get(j,0)+j*j*v)%p
        LU[j+1]=(LU.get(j+1,0)-(j-m)*(j-2*m)*v)%p
    assert all(v==0 for v in LU.values())
    # Ordered signed corner and its positive-rank projection.
    P={}
    direct=0
    for j in range(1,m+1):
        for ell in range(1,j+1):
            k=j-ell
            v=u[j]*c[ell-1]%p
            P[k]=(P.get(k,0)+v)%p
            direct=(direct+div((6*k+1)*v,18)*pow(2,-(p+k),p))%p
    trace=div(sum((6*k+1)*v*pow(2,-k,p) for k,v in P.items()),36)
    assert direct==trace,(p,direct,trace)
    # Independent O(m) prefix-moment arithmetic layout.
    S0=S1=fast=0
    for j in range(1,m+1):
        a=c[j-1]*pow(2,j,p)%p
        S0=(S0+a)%p
        S1=(S1+j*a)%p
        fast=(fast+u[j]*pow(2,-j,p)*((6*j+1)*S0-6*S1))%p
    assert trace==div(fast,36)
    native=None
    if original:
        mod=p**3
        r=[1]
        for n in range(p-1):
            r.append(r[-1]*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,mod)%mod)
        Q=sum((6*(j+k)+1)*r[j]*r[k] for j in range(p) for k in range(p-j,p))%mod
        assert Q%(p*p)==0
        native=Q//(p*p)
        assert trace==native,(p,trace,native)
    return p,c[0],edge,trace,native

if __name__=="__main__":
    ps=primes(373)
    for p in ps:
        result=check(p)
        if p in (7,13,19,37,43,373):print(result)
    for p in (1327,19963):print(check(p,original=False))
    print("PASS:",len(ps),"prime cases with independent original signed Q; two larger reflection/operator/trace cases")
