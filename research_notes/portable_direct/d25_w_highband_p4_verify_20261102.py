#!/usr/bin/env python3
"""Original 216 Ramanujan high-index p^4 reflection; independent integer checks."""
from math import comb, isqrt
import json

def primes_up_to(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[0:2]=b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if sieve[d]: sieve[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [p for p in range(7,n+1) if p%6==1 and sieve[p]]

def checked_prime(p):
    r=(p-1)//6; mod=p*p; full=p**4
    fact=[1]*p; harm=[0]*p
    for j in range(1,p):
        fact[j]=fact[j-1]*j%mod
        harm[j]=(harm[j-1]+pow(j,-1,p))%p
    w=((fact[p-1]+1)%mod)//p
    q=((pow(216,p-1,mod)-1)%mod)//p
    def ratio_factor(j,d):
        return pow(fact[j-1],5,mod)*pow(fact[2*j-1]*fact[d]%mod,-1,mod)%mod
    B=[1]; b=1
    for k in range(1,p):
        num=(2*k)*(2*k-1)*(3*k)*(3*k-1)*(3*k-2)
        b=b*num*pow(216*k**5,-1,full)%full
        B.append(b)
    direct=sum((6*k+1)*B[k] for k in range(3*r+1,p))%full
    assert direct%p**2==0
    T=(direct//p**2)%mod
    middle=[]; upper=[]
    for j in range(2*r+1,3*r+1):
        k=p-j; d=3*j-p
        alpha=-pow(216,j-1,mod)*ratio_factor(j,d-1)%mod
        c=(w+2*harm[2*j-1]+2*harm[d-1]-5*harm[j-1]-q)%p
        assert B[k]%p**2==0
        assert (B[k]//p**2)%mod==alpha*(1+p*c)%mod
        middle.append((j,alpha,c))
    for j in range(1,2*r+1):
        k=p-j
        ups=-2*pow(216,j-1,p)*ratio_factor(j,3*j-1)%p
        assert B[k]%p**3==0
        assert (B[k]//p**3)%p==ups
        upper.append((j,ups))
    M0=sum((1-6*j)*a for j,a,c in middle)%mod
    Mw=6*p*sum(a for j,a,c in middle)%mod
    Mc=p*sum((1-6*j)*a*c for j,a,c in middle)%mod
    U=p*sum((1-6*j)*v for j,v in upper)%mod
    assert (M0+Mw+Mc+U)%mod==T
    if p in (7,13,19,31,37,43,73,373):
        for j in (1,2*r,2*r+1,3*r):
            if 1<=j<=3*r:
                k=p-j
                assert (comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,full))%full==B[k]
    return {'p':p,'T_mod_p2':T,'digits':[T%p,(T%mod)//p],'ports':[M0,Mw,Mc,U],
            'wilson_quotient_mod_p':w,'fermat_quotient_216_mod_p':q}

if __name__=='__main__':
    examples=[]; selected={7,13,19,31,37,43,73,373,1171,3019}
    primes=primes_up_to(10000)
    for p in primes:
        row=checked_prime(p)
        if p in selected: examples.append(row)
    print(json.dumps({'schema':'D25_W_HIGHBAND_P4_VERIFIER_V1',
        'status':'AUTHOR_SIDE_EXACT_FINITE_EVIDENCE',
        'tested_primes':len(primes),'all_passed':True,'examples':examples},indent=2))
