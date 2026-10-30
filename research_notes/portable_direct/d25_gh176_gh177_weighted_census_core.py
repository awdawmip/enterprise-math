#!/usr/bin/env python3
"""Exact 216-weighted census: finite evidence, not a universal proof."""
from collections import Counter
from math import comb
from hashlib import sha256


def primes(bound=12000):
    isprime=bytearray(b'\x01')*bound
    isprime[:2]=b'\x00\x00'
    for k in range(2,int((bound-1)**0.5)+1):
        if isprime[k]: isprime[k*k:bound:k]=b'\x00'*(((bound-1-k*k)//k)+1)
    return (p for p in range(5,bound) if isprime[p])


def weighted(p):
    mod=p**3
    fac=[1]*p
    for k in range(1,p):fac[k]=fac[k-1]*k%mod
    invfac=[1]*p
    invfac[-1]=pow(fac[-1],-1,mod)
    for k in range(p-1,0,-1):invfac[k-1]=invfac[k]*k%mod
    inv36=pow(36,-1,mod)
    a=1; value=1; slope=0
    for k in range(1,p):
        ik=fac[k-1]*invfac[k]%mod
        a=a*(2*k-1)*(3*k-2)*(3*k-1)*inv36*pow(ik,3,mod)%mod
        value=(value+(6*k+1)*a)%mod
        slope=(slope+k*(6*k+1)*a)%p
    return value,slope


def gauss(p,x):
    m=(p-1)//6
    c=1;f=1;xfp=0
    for k in range(1,m+1):
        c=c*(m-k+1)*(2*m-k+1)*x*pow(2*k*k,-1,p)%p
        f=(f+c)%p;xfp=(xfp+k*c)%p
    return f,(f+12*xfp)%p,xfp


def raw216(p):
    mod=p**3;v=0;factor=1;inv=pow(216,-1,mod)
    for k in range(p):
        v=(v+(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*factor)%mod
        factor=factor*inv%mod
    return v


def main():
    counts=Counter();branches=Counter();rows=[];anchors={}
    raw={5,7,11,13,19,31,37,157,373,1327}
    for p in primes():
        a,deriv=weighted(p)
        assert a==(p if p%3==1 else (-p)%(p**3)),(p,a)
        counts[p%24]+=1
        branch='N/A'
        if p%6==1:
            f,L,fp=gauss(p,1)
            assert f*L%p==0 and (f!=0 or L!=0)
            u=12*fp*fp%p if f==0 else f*f*pow(12,-1,p)%p
            assert u!=0 and u==deriv,(p,u,deriv)
            m=(p-1)//6
            f2,L2,_=gauss(p,2)
            assert f2==comb(3*m,m)%p and L2==(-f2*pow(3,-1,p))%p
            assert L2!=0
            _,Lspecial,_=gauss(p,2*pow(3,-1,p)%p)
            assert Lspecial!=0,('exception_at_2_over_3',p)
            branch='F_ZERO' if f==0 else 'L_ZERO'
            branches[(p%24,branch)]+=1
            if p%24 in (13,19):
                delta=(a-p)//(p*p)%p
                root_correction=-delta*pow(u,-1,p)%p
                assert (a+p*p*root_correction*u)%(p**3)==p
        if p in raw:
            assert raw216(p)==a
            anchors[p]=(a,deriv,branch)
        rows.append(f'{p},{p%24},{a},{deriv},{branch}\n')
    print('COUNTS',dict(sorted(counts.items())))
    print('BRANCHES',dict(sorted(branches.items())))
    print('ANCHORS',dict(sorted(anchors.items())))
    print('DATA_SHA256',sha256(''.join(rows).encode()).hexdigest())
    print('TESTED',len(rows),'prime mod p^3 values, root channel and p-adic slopes')
    print('PASS_GH176_GH177_SIGNED_EXACT_BOUND_12000')


if __name__=='__main__':main()
