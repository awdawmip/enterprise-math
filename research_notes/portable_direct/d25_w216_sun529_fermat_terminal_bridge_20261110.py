#!/usr/bin/env python3
"""Exact original W216 216-Fermat quotient terminal-jet and Sun 5.29 bridge.
AUTHOR_SIDE / UNREVIEWED / NOT_NATIVE_H0_B0. Python integers only.
"""
from fractions import Fraction
from math import comb

TARGET_PRIMES=(13,19,37,43,61,67,109,139,157,163,181,229,373)
NON_TARGET_PRIMES=(5,7,11,17,23,29,31,41,47,53)

def rational_identity(n):
    a=[Fraction(comb(2*k,k)**2*comb(3*k,k),216**k) for k in range(n)]
    w=sum((6*k+1)*a[k] for k in range(n))
    f=[sum(a[k]/(k+1)**r for k in range(n)) for r in range(3)]
    boundary=(9-6*n-Fraction(13,3*n)+Fraction(2,3*n*n))*a[-1]
    assert w == -2*f[0]+Fraction(13,3)*f[1]-Fraction(2,3)*f[2]+boundary

def term_and_moments(p):
    mod=p**3
    inv216=pow(216,-1,p**5)
    power=1
    ff=[0,0,0]
    w=0
    terminal=None
    for k in range(p):
        numerator=comb(2*k,k)**2*comb(3*k,k)
        ak=numerator*power%mod
        w=(w+(6*k+1)*ak)%mod
        ff[0]=(ff[0]+ak)%mod
        # The only p-divisible k+1 here occurs at k=p-1.
        for r in (1,2):
            if k+1==p:
                assert numerator%p**3==0
                item=(numerator//p**r)*power%mod
            else:
                item=(numerator*power*pow(k+1,-r,mod))%mod
            ff[r]=(ff[r]+item)%mod
        if k==p-1:
            terminal=(numerator//p**3)*power%(p*p)
        power=power*inv216%(p**5)
    return ff,w,terminal

def unconditional_bridge(p):
    f,w,_=term_and_moments(p)
    mod=p**3; half=pow(2,-1,mod); third=pow(3,-1,mod)
    q=(pow(216,p-1,p*p)-1)//p
    e=(f[2]-13*half*f[1]+5*half*p)%mod
    expected=(-2*f[0]-2*third*e+2*third*p*p*q)%mod
    assert (w-p)%mod==expected,(p,w,expected)

def target_check(p):
    mod=p**3
    ff,w,aunit=term_and_moments(p)
    q=(pow(216,p-1,p*p)-1)//p
    u=((aunit+1)//p)%p
    assert aunit%p==p-1
    assert u==(q-13*pow(2,-1,p))%p
    ep=p*p
    product=1
    for j in range(1,p-1):
        product=product*(1+p*pow(j,-1,ep))%ep
    for j in range(1,p):
        product=product*(1+p*pow(j,-1,ep))%ep
    for j in range(1,p-2):
        product=product*(1+2*p*pow(j,-1,ep))%ep
    exact_product=2*pow((p-1)**2*(p-2)*pow(216,p-1,ep),-1,ep)*product%ep
    assert exact_product==aunit
    half=pow(2,-1,mod)
    E=(ff[2]-13*half*ff[1]+5*half*p)%mod
    assert ff[0]%(p*p)==E%(p*p)==(w-p)%(p*p)==0
    alpha=ff[0]//(p*p)%p
    epsilon=E//(p*p)%p
    lift=(w-p)//(p*p)%p
    predicted=(-2*alpha-2*pow(3,-1,p)*epsilon+2*pow(3,-1,p)*q)%p
    assert lift==predicted
    return (p,alpha,epsilon,q,u,lift)

if __name__=="__main__":
    for n in range(1,13):
        rational_identity(n)
    print("PASS: twelve exact rational telescoper cases")
    for p in NON_TARGET_PRIMES:
        unconditional_bridge(p)
    print("PASS: ten non-target primes for unconditional mod p^3 bridge")
    for p in TARGET_PRIMES:
        unconditional_bridge(p)
        print("target(p,alpha,epsilon,q,u,lift)=",target_check(p))
    print("PASS: thirteen target primes and exact endpoint-product crosschecks")
