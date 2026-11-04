#!/usr/bin/env python3
"""D25 Sun truncation p^3 defect: exact integer/quadratic-ring checks."""
from math import comb

def qmul(a,b,m):
    return ((a[0]*b[0]+2*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def qadd(a,b,m):return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def qsc(a,k,m):return (a[0]*k%m,a[1]*k%m)
def qev(c,x,m,der=False):
    a=(0,0);v=(1,0)
    for j in range(1 if der else 0,len(c)):
        a=qadd(a,qsc(v,j*c[j] if der else c[j],m),m);v=qmul(v,x,m)
    return a

def source(p,d):
    m=p**3; den={3:27,4:64}[d]; t=pow({3:8,4:36}[d],-1,m)
    x=(pow(2,-1,m),pow(4 if d==3 else 3,-1,m))
    T=(0,-pow(4 if d==3 else 24,-1,m)%m)
    c=[comb(2*k,k)*comb(d*k,(d-2)*k)*pow(den,-k,m)%m for k in range(p)]
    h=[comb(2*k,k)*v%m for k,v in enumerate(c)]
    f2=[0]*(2*p-1); hh=[0]*(2*p-1)
    for i in range(p):
        for j in range(p): f2[i+j]=(f2[i+j]+c[i]*c[j])%m
    for k in range(p):
        for j in range(k+1):hh[k+j]=(hh[k+j]+(-1)**j*comb(k,j)*h[k])%m
    D=[(u-v)%m for u,v in zip(f2,hh)]
    assert D[:p]==[0]*p and all(v%p**2==0 for v in D) and D[p]==0
    E=[v//p**2 for v in D]
    A=sum(h[k]*pow(t,k,m) for k in range(p))%m
    M=sum(k*h[k]*pow(t,k,m) for k in range(p))%m
    F=qev(c,x,m);Fp=qev(c,x,m,True)
    Ep=qev(E,(x[0]%p,x[1]%p),p,True); Ev=qev(E,(x[0]%p,x[1]%p),p)
    assert qadd(qmul(F,F,m),qsc(Ev,-p*p,m),m)==(A,0)
    mm=qadd(qmul(T,qmul(F,Fp,m),m),qsc(qmul(qsc(T,pow(2,-1,p),p),Ep,p),-p*p,m),m)
    assert mm==(M,0) and all(v%p==0 for v in F)
    assert qev(E,(x[0]%p,x[1]%p),p)[1]==0
    xx=(x[0]%p,x[1]%p); xp=(1,0)
    for _ in range(p):xp=qmul(xp,xx,p)
    assert xp==((1-xx[0])%p,(-xx[1])%p)
    return A,M,F,Fp,T,Ev,Ep

def check(p):
    a=source(p,3);b=source(p,4);m=p**3
    A,MA,Fa,Fpa,Ta,Ea,Epa=a;B,MB,Fb,Fpb,Tb,Eb,Epb=b
    U=lambda F:tuple(v//p%p for v in F)
    sq=qadd(qmul(U(Fa),U(Fa),p),qsc(qmul(U(Fb),U(Fb),p),-1,p),p)
    df=qadd(Eb,qsc(Ea,-1,p),p)
    CC=qadd(qsc(qmul(Ta,qmul(Fa,Fpa,m),m),6,m),qsc(qmul(Tb,qmul(Fb,Fpb,m),m),-8,m),m)
    assert all(v%p**2==0 for v in CC)
    core=tuple(v//p**2%p for v in CC)
    correction=qadd(qsc(qmul(Ta,Epa,p),-3,p),qsc(qmul(Tb,Epb,p),4,p),p)
    weighted=qadd(core,correction,p)
    D=(A-B)%m//p**2; mo=(6*MA-8*MB)%m//p**2
    assert qadd(sq,df,p)==(D,0) and weighted==(mo,0)
    assert (D+mo)%p==0
    return p,D,mo,sq,df,core,correction

def prime(n):return n>1 and all(n%i for i in range(2,int(n**.5)+1))
if __name__=='__main__':
    primes=[p for p in range(5,501) if prime(p) and p%24 in (13,19)]
    result=[check(p) for p in primes]
    print('checked_primes=',len(result),'failed=0')
    for r in result:
        if r[0] in (13,19,373):print(r)
