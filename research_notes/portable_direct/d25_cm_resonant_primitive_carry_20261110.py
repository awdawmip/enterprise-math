#!/usr/bin/env python3
"""Exact signed p-adic Legendre primitive certificate. Does not execute native H0/B0."""
from math import comb

def poly(n,m):
    return [((-1)**k*comb(n,k)*comb(n+k,k))%m for k in range(n+1)]

def conv(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):out[i+j]=(out[i+j]+u*v)%p
    return out

def add(u,v,m):return ((u[0]+v[0])%m,(u[1]+v[1])%m)
def mul(u,v,m):return ((u[0]*v[0]+2*u[1]*v[1])%m,(u[0]*v[1]+u[1]*v[0])%m)
def sc(u,c,m):return (u[0]*c%m,u[1]*c%m)
def ev(a,x,m):
    z=(0,0)
    for v in reversed(a):z=add(mul(z,x,m),(v,0),m)
    return z

def divp(a,p):
    assert a[0]%p==a[1]%p==0
    return ((a[0]//p)%p,(a[1]//p)%p)

def check(p):
    q=(p-1)//4; m=p*p
    P=poly(q,m);Q=poly(3*q,m);a=[v%p for v in P]
    assert all(Q[k]%p==(P[k]%p if k<=q else 0) for k in range(3*q+1))
    rho=P[q]*(Q[3*q]//p)%p
    assert rho==p-2
    J=[((Q[k]-(P[k] if k<=q else 0))%m//p)%p for k in range(3*q+1)]
    sq=conv(a,a,p);mixed=conv(a,[v%p for v in Q],p)
    I=[0]+[v*pow(k+1,-1,p)%p for k,v in enumerate(sq)]
    integral=[0]+[v*pow(k+1,-1,p)%p for k,v in enumerate(mixed[:-1])]+[rho]
    assert len(integral)==p+1
    assert all(integral[k]==((I[k] if k<len(I) else 0)-(2 if k==p else 0))%p
               for k in range(p+1))

    aj=conv(a,[k*J[k]%p for k in range(1,len(J))],p)
    bj=conv([k*a[k]%p for k in range(1,len(a))],J,p)
    W=[((aj[k] if k<len(aj) else 0)-(bj[k] if k<len(bj) else 0))%p
       for k in range(max(len(aj),len(bj)))]
    lhs=[0]*(len(W)+2)
    for k,v in enumerate(W):
        lhs[k+1]=(lhs[k+1]+v)%p; lhs[k+2]=(lhs[k+2]-v)%p
    assert all(lhs[k]==(-2*q*((I[k] if k<len(I) else 0)-
                              (2 if k==p else 0)))%p for k in range(len(lhs)))

    s=(pow(2,-1,m),-pow(3,-1,m)%m);sm=(s[0]%p,s[1]%p)
    ps=ev(P,s,m);qs=ev(Q,s,m);U=divp(ps,p)
    Js=divp(((qs[0]-ps[0])%m,(qs[1]-ps[1])%m),p)
    D=ev([k*a[k]%p for k in range(1,len(a))],sm,p)
    Is=ev(I,sm,p)
    defect=add(Is,sc(add((1,0),sc(sm,-1,p),p),-2,p),p)
    assert sc(mul(D,Js,p),pow(36,-1,p),p)==sc(defect,2*q,p)
    assert Is[0]==1 and defect[0]==0 and U[0]==0 and Js[0]==0
    g=[1]
    for k in range(1,p):
        g.append(g[-1]*(4*k-3)*(4*k-1)*pow(16*k*k,-1,m)%m)
    gs=ev(g,s,m);G=divp(gs,p)
    assert sc(gs,4,m)==add(sc(ps,3,m),qs,m)
    assert G==add(U,sc(Js,pow(4,-1,p),p),p)
    corrected=add(sc(mul(D,U,p),2,p),sc(defect,-9,p),p)
    assert corrected==sc(mul(D,G,p),2,p)
    return {'p':p,'q':q,'rho':rho,'D':D,'I':Is,'J':Js,
            'P_over_p':U,'G_over_p':G,
            'UD_residual':add(corrected,(0,-3),p)}

def prime(n):
    return n>=2 and all(n%j for j in range(2,int(n**.5)+1))

if __name__=="__main__":
    rows=[check(p) for p in range(13,1000,24) if prime(p)]
    assert len(rows)==22 and all(r['UD_residual']==(0,0) for r in rows)
    print("22 primes p<1000: coefficient carry and signed Wronskian PASS")
    print("CM p^2 original-Gauss independent-path and target: FINITE PASS")
    print("Native H0/B0: NOT_RUN; all-prime UD: OPEN")
    print("p373:",next(v for v in rows if v["p"]==373))
