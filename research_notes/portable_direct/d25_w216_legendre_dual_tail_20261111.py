#!/usr/bin/env python3
"""Exact original W216 p^3 / dual finite-field tail checks.
Author-side UNREVIEWED/NOT_ADMITTED; not native H0/B0.
"""
from math import factorial, isqrt

def is_prime(p):
    return p >= 2 and all(p % d for d in range(2,isqrt(p)+1))

def original_coefficients(p):
    M=p**3
    a=[1]
    for k in range(p-1):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M)%M)
    return a

def normalized_unit_factorials(p,k):
    def unit_fact(n):
        q,r=divmod(n,p)
        return ((-1)**q * factorial(q) * factorial(r)) % p
    v=(2*k)//p+(3*k)//p
    unit=unit_fact(2*k)*unit_fact(3*k)*pow(216,-k,p)*pow(factorial(k),-5,p)%p
    return v,unit

def verify(p):
    assert is_prime(p) and p>3
    n=(p-1)//2
    a=original_coefficients(p)
    b_n=a[n]//p%p
    character=pow(6,(p-1)//2,p)
    character=-1 if character==p-1 else character
    assert character in(-1,1)
    assert b_n==(-2*character)%p,(p,b_n,character)
    v,u=normalized_unit_factorials(p,n)
    assert v==1 and u==b_n
    if p%6!=1:
        return (p,character,b_n,None,None,None)
    m=(p-1)//6
    for k in range(2*m+1,3*m+1):
        vk,uk=normalized_unit_factorials(p,k)
        assert vk==1 and uk==a[k]//p%p,(p,k,vk,uk)
    I1=range(2*m+1,3*m+1)
    I2=range(3*m+1,4*m+1)
    direct=sum((6*k+1)*(a[k]//(p*p)) for k in I2)%p
    mirrored=sum((1-6*k)*pow(36*k**3*(a[k]//p%p),-1,p) for k in I1)%p
    assert direct==mirrored
    q=1
    dual=H=der=0
    for j in range(m):
        H=(H+q)%p
        der=(der+2*j*q)%p  # derivative at x=1/2
        dual=(dual+(6*j+4)*q)%p
        if j+1<m:
            q=q*(j+1)*(6*j+5)*(6*j+7)*pow(9*(2*j+3)**3,-1,p)%p
    assert dual==(4*H+3*der)%p
    dual_tail=character*pow(9,-1,p)*dual%p
    assert dual_tail==mirrored,(p,dual,dual_tail,mirrored)
    full=sum((6*k+1)*a[k] for k in range(p))%(p**3)
    short=sum((6*k+1)*a[k] for k in range(n+1))%(p**3)
    assert (short+p*p*dual_tail)%(p**3)==full
    if p==373:
        assert (character,b_n,H,der,dual,dual_tail,short,full)==(-1,2,121,284,217,266,14887176,373)
    return (p,character,b_n,dual,dual_tail,full)

if __name__=='__main__':
    selected=[5,7,11,13,17,19,23,31,37,43,61,67,73,79,97,109,139,157,193,373,541,733]
    for p in selected:
        print('p=%-3d chi6=%2d b_n=%-3d D=%-4s tail=%-4s W=%s' % verify(p))
    print('ALL CENTRAL UNIT AND DUAL HYPERGEOMETRIC TAIL ASSERTIONS PASSED')
