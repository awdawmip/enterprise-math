#!/usr/bin/env python3
"""Independent finite-field verification of the D25 exceptional-pair duality.
No external dependencies; F_p[t]/(t**6) arithmetic and factorial/harmonic forms.
"""
from math import factorial


def primes_to(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for k in range(2,int(n**.5)+1):
        if sieve[k]:
            sieve[k*k:n+1:k]=b'\x00'*(((n-k*k)//k)+1)
    return [k for k in range(n+1) if sieve[k]]


def prod_modpoly(x,y,p,d=6):
    z=[0]*d
    for i,u in enumerate(x):
        for j,v in enumerate(y[:d-i]):
            z[i+j]=(z[i+j]+u*v)%p
    return z


def exceptional_coefficients(p,m):
    a,b,c=2*m,3*m,4*m
    # Exact coefficient recursion for M_j(t) in F_p[t]/(t^6).
    pol=[1,0,0,0,0,0]
    um=None
    for j in range(5*m):
        if j==m: um=pol[0]
        h=j+1
        fac=pow((-2*h*h*h)%p,-1,p)
        num=[1,0,0,0,0,0]
        for s in (a,b,c):
            num=prod_modpoly(num,[(s-j)%p,1,0,0,0,0],p)
        invden=[pow((3*pow(h,-1,p))%p,k,p) for k in range(6)]
        pol=prod_modpoly(pol,num,p)
        pol=prod_modpoly(pol,invden,p)
        pol=[x*fac%p for x in pol]
    if um is None: raise AssertionError('no exceptional')
    return um,pol


def verify(p):
    assert p%6==1 and p>5
    m=(p-1)//6
    u,pol=exceptional_coefficients(p,m)
    v3,v4,v5=pol[3],pol[4],pol[5]
    assert pol[:3]==[0,0,0] and u and v3
    # From factorial shape and Wilson's reflection, exact prediction:
    v3_pred=pow(m*m*u%p,-1,p)
    # Harmonic ratio of the cubic and quartic terms:
    h=[0]*(5*m+1)
    h2=[0]*(5*m+1)
    for j in range(1,len(h)):
        inv=pow(j,-1,p)
        h[j]=(h[j-1]+inv)%p
        h2[j]=(h2[j-1]+inv*inv)%p
    ratio=(3*h[5*m]+sum(h[s]-h[5*m-s-1] for s in (2*m,3*m,4*m)))%p
    simple=(2*h[m]+h[2*m]+11*pow(6*m,-1,p))%p
    log_second=(-5*h2[m]-h2[2*m]*pow(2,-1,p)+49*pow(72*m*m,-1,p))%p
    beta=(log_second+simple*simple*pow(2,-1,p))%p
    assert v3==v3_pred and v4 == (v3*ratio)%p and ratio==simple
    assert v5==v3*beta%p
    return (p,m,u,v3,v4,v5,ratio,beta,4*v3%p)


def main():
    ps=[p for p in primes_to(3000) if p%6==1]
    results=[verify(p) for p in ps]
    for p in [7,13,19,373,1009]:
        if p%6==1:
            result=verify(p)
            print('p,m,u_m,v3,v4,v5,v4/v3,v5/v3,paired_t3 =',result)
    print('VERIFIED',len(results),'target primes <=3000; independent Fp truncated polynomial recurrence')


if __name__=='__main__':main()
