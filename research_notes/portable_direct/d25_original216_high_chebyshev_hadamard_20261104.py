#!/usr/bin/env python3
"""Portable exact modular D25 high-port Chebyshev/Hadamard verifier; no native Source claim."""
from math import factorial, comb

def primes_upto(n):
    a=bytearray(b'\x01')*(n+1); a[:2]=b'\x00\x00'
    for d in range(2,int(n**0.5)+1):
        if a[d]: a[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [p for p in range(7,n+1) if a[p] and p%6==1]

def sample(p):
    r=(p-1)//6; k0=3*r+1; m=p**3; a=[1]
    for k in range(4*r+1):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,m)%m)
    assert a[4*r+1]==0
    y=[a[k0+s]//(p*p) for s in range(r)]
    assert all(a[k0+s]%(p*p)==0 for s in range(r))
    alpha=(3*r+2)*pow(factorial(k0),-4,p)*pow(216,-k0,p)%p
    assert y[0]%p==alpha
    q=beta=zpow=1; high=0
    for s in range(r):
        v=alpha*q*beta*zpow%p
        assert v==y[s]%p
        alternate=alpha*pow(r,-1,p)*pow(-32,s,p)*comb(r+s,2*s+1)
        alternate=alternate*pow(factorial(s),4,p)*pow(factorial(2*s+1),-2,p)%p
        assert alternate==v
        high=(high+(4+6*s)*v)%p
        if s+1<r:
            q=q*2*(s+1-r)*(s+1+r)*pow((s+1)*(2*s+3),-1,p)%p
            beta=beta*4*(s+1)**2*pow((2*s+3)**2,-1,p)%p
            zpow=zpow*pow(2,-1,p)%p
    assert high==sum((6*(k0+s)+1)*y[s] for s in range(r))%p
    M=None
    if p%24 in (13,19):
        quartic=[1];h=3*r
        for k in range(h):
            numer=(4*k+1)*(4*k+2)*(4*k+3)*(4*k+4)
            quartic.append(quartic[-1]*numer*pow(2304*(k+1)**4,-1,m)%m)
        vhalf=sum((8*k+1)*quartic[k] for k in range(h+1))%m
        low=sum((6*k+1)*a[k] for k in range(k0))%m
        d=(low-vhalf)%m;assert d%(p*p)==0;M=d//(p*p)
        highfull=sum((6*(k0+s)+1)*a[k0+s] for s in range(r))%m
        assert highfull%(p*p)==0 and highfull//(p*p)%p==high
        assert vhalf==p and (low+highfull-p)%m==p*p*((M+high)%p)
    return (p,r,alpha,high,M)

def main():
    arr=[sample(p) for p in primes_upto(2000)]
    print('PASS primes=%d high_positions=%d target_classes=%d' %
          (len(arr),sum(x[1] for x in arr),sum(x[4] is not None for x in arr)))
    for x in arr:
        if x[0] in (7,13,19,37,373): print(x)
if __name__=='__main__': main()
