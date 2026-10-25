#!/usr/bin/env python3
"""Exact signed finite-field checks of the projected cross-source Clausen law; not native CM."""
from math import comb

def primes(limit):
    return [p for p in range(7,limit+1) if p%6==1 and all(p%d for d in range(2,int(p**.5)+1))]

def verify(p):
    m=(p-1)//6
    f=[1]*p
    for n in range(1,p): f[n]=f[n-1]*n%p
    def div(a,b): return (a%p)*pow(b%p,-1,p)%p
    u=[comb(m,j)*comb(2*m,j)%p for j in range(m+1)]
    c=[div(2*f[m]*f[2*m]*f[ell-1]**2,f[m+ell]*f[2*m+ell]) for ell in range(1,m+1)]
    Y={}
    for j,a in enumerate(u):
        for ell,b in enumerate(c,1):
            k=j-ell
            Y[k]=(Y.get(k,0)+a*b)%p
    P={k:v for k,v in Y.items() if k>=0}
    inv3,inv2,twothirds=div(1,3),div(1,2),div(2,3)
    H={}
    for k,v in Y.items():
        H[k]=(H.get(k,0)+k**3*v)%p
        H[k+1]=(H.get(k+1,0)-(k+inv3)*(k+inv2)*(k+twothirds)*v)%p
    edge=m*m*c[-1]%p
    rhs={}
    for j,a in enumerate(u):
        rhs[j]=(rhs.get(j,0)-6*j*a)%p
        rhs[j-m]=(rhs.get(j-m,0)+edge*(3*j-m)*a)%p
    assert {k:v for k,v in H.items() if v}=={k:v for k,v in rhs.items() if v},(p,"Laurent")
    leakage=Y.get(-1,0)
    assert leakage==18*m*edge*u[m]%p,(p,"boundary cancellation")
    HP={}
    for k,v in P.items():
        HP[k]=(HP.get(k,0)+k**3*v)%p
        HP[k+1]=(HP.get(k+1,0)-(k+inv3)*(k+inv2)*(k+twothirds)*v)%p
    want={k:(-6*k*u[k])%p for k in range(m+1)}
    assert all(HP.get(k,0)==v for k,v in want.items())
    assert all(k in want or not v for k,v in HP.items())
    a=[1]
    for k in range(1,m+1):
        a.append(div(a[-1]*(k-1+inv3)*(k-1+inv2)*(k-1+twothirds),k**3))
    suffix=0
    closed=[0]*(m+1)
    for j in range(m,0,-1):
        suffix=(suffix+div(u[j],j*j*a[j]))%p
        closed[j-1]=6*a[j-1]*suffix%p
    assert all(P.get(k,0)==closed[k] for k in range(m+1)),(p,"Clausen resolvent")
    T=div(sum((6*k+1)*P.get(k,0)*pow(2,-k,p) for k in range(m)),36)
    Tclosed=div(sum((6*k+1)*closed[k]*pow(2,-k,p) for k in range(m)),36)
    assert T==Tclosed
    return p,P.get(0,0),leakage,T

if __name__=="__main__":
    small=primes(373)
    for p in small:
        v=verify(p)
        if p in (7,13,19,37,43,373):print(v)
    for p in (1327,19963):print(verify(p))
    print("PASS",len(small),"small primes plus p=1327 and p=19963")
