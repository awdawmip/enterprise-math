#!/usr/bin/env python3
"""Exact finite-ring checker for the D25 Frobenius-compensated Green identity.
External arithmetic only: not a native H0/B0 run, Source checkpoint or admission.
"""
from math import comb

def prime_list(limit):
    sieve=[True]*(limit+1)
    sieve[:2]=[False,False]
    for k in range(2,int(limit**0.5)+1):
        if sieve[k]:
            sieve[k*k:limit+1:k]=[False]*(((limit-k*k)//k)+1)
    return [p for p in range(7,limit+1) if sieve[p] and p%6==1]

def coefficients(p, mod):
    r=(p-1)//6; n=2*r
    fact=[1]
    for i in range(1,2*n+1):
        fact.append(fact[-1]*i%mod)
    inv2=pow(2,-1,mod)
    a=[0]*(r+1)
    for m in range(r+1):
        j=r-m
        num=fact[2*n-2*j]
        den=(pow(2,n,mod)*fact[j]*fact[n-j]*fact[n-2*j])%mod
        a[m]=((-1)**j*num*pow(den,-1,mod))%mod
    z=sum(a[m]*pow(inv2,m,mod) for m in range(r+1))%mod
    e=sum(2*m*a[m]*pow(inv2,m-1,mod) for m in range(1,r+1))%mod
    return a,z,e

def gauss_half_value(p):
    mod=p*p
    term=1; val=1
    for k in range(1,p):
        term=term*(6*k-5)*(3*k-2)*pow(36*k*k,-1,mod)%mod
        val=(val+term)%mod
    return val

def integral_quotient(a,p):
    r=len(a)-1
    h=[0]*(2*r+1)
    for i,ai in enumerate(a):
        for j,aj in enumerate(a):
            h[i+j]=(h[i+j]+ai*aj)%p
    inv2=pow(2,-1,p)
    return sum(v*pow(inv2,k,p)*pow(2*k+1,-1,p) for k,v in enumerate(h))%p

def check_prime(p):
    r=(p-1)//6; n=2*r; mod=p*p
    a,z,e=coefficients(p,mod)
    y=gauss_half_value(p)
    assert (y-z)%p==0
    d=((y-z)%mod)//p
    j=integral_quotient([v%p for v in a],p)
    invdegree=pow(2*n+1,-1,p)
    if p%24 in (13,19):
        assert z%p==0 and y%p==0
        assert e%p and pow(2,(p-1)//2,p)==p-1
        predicted=-2*(j+invdegree)*pow(9*e,-1,p)%p
        assert d==predicted,(p,d,predicted)
        a0=y//p
        assert (z//p+d)%p==a0
        return {'p':p,'r':r,'legendre_carry':z//p,
                'green_deformation':d,'integral_J':j,'frobenius_correction':invdegree,
                'E':e%p,'a0':a0,
                'first_digit_residual':(12*a0*(-e*pow(4,-1,p))-1)%p}
    return {'p':p,'r':r,'nonzero_legendre':z%p}

def convolution(a,b,p):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                o[i+j]=(o[i+j]+x*y)%p
    return o

def full_polynomial_check(p):
    r=(p-1)//6; n=2*r; M=p*p
    a,_,_=coefficients(p,p)
    P=[0]*(n+1)
    for m,am in enumerate(a):
        P[2*m]=am
    yg=[0]*p; yg[0]=1
    for k in range(1,p):
        yg[k]=yg[k-1]*(6*k-5)*(3*k-2)*pow(18*k*k,-1,M)%M
    zg=[0]*p; zg[0]=1
    for k in range(1,r+1):
        num=(k-1-r)*(2*k+2*r-1)
        zg[k]=zg[k-1]*num*pow(2*k*k,-1,M)%M
    D_z=[]
    for k in range(p):
        v=(yg[k]-zg[k])%M
        assert v%p==0,(p,k,v)
        D_z.append(v//p)
    D_x=[0]*(2*p-1)
    for k,dk in enumerate(D_z):
        if not dk:
            continue
        for j in range(k+1):
            D_x[2*j]=(D_x[2*j]+dk*(-1)**j*comb(k,j))%p
    pd=[i*P[i]%p for i in range(1,len(P))]
    dd=[i*D_x[i]%p for i in range(1,len(D_x))]
    u=convolution(P,dd,p)
    v=convolution(pd,D_x,p)
    W=[0]*(max(len(u),len(v))+2)
    for i in range(len(W)-2):
        a0=u[i] if i<len(u) else 0
        b0=v[i] if i<len(v) else 0
        W[i]=(W[i]+a0-b0)%p
        W[i+2]=(W[i+2]-a0+b0)%p
    PP=convolution(P,P,p)
    target=[0]*len(W)
    inv9=pow(9,-1,p)
    for i,coef in enumerate(PP):
        if coef:
            target[i+1]=coef*pow(i+1,-1,p)*inv9%p
    target[p]=(target[p]-inv9*pow(2*n+1,-1,p))%p
    for i,(x,y) in enumerate(zip(W,target)):
        assert x==y,(p,i,x,y)
    return {'p':p,'polynomial_degree':len(W)-1,'Frobenius_coefficient':W[p]}

if __name__=='__main__':
    primes=prime_list(997)
    results=[check_prime(p) for p in primes]
    targets=[x for x in results if x['p']%24 in (13,19)]
    print('CHECK_SCOPE all p<=997, p%6=1:',len(results),'target13/19:',len(targets))
    for x in targets:
        if x['p'] in [13,19,37,61,109,373]:
            print('CERTIFICATE',x)
    print('SCALAR_CM_FROBENIUS_GREEN_CHECK PASS',len(targets))
    for pp in [7,13,19,37,61,109,373]:
        print('WHOLE_POLYNOMIAL_PASS',full_polynomial_check(pp))
