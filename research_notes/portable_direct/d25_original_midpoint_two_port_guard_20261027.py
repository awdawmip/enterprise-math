#!/usr/bin/env python3
"""Exact original W/S midpoint two-port check; author-side only.
No substitute for H0/B0 divided-power native benchmark.
"""
from fractions import Fraction
from math import factorial


def primes_below(n):
    a=bytearray(b'\x01')*n
    a[:2]=b'\x00\x00'
    for j in range(2,int(n**.5)+1):
        if a[j]:
            a[j*j::j]=b'\x00'*len(a[j*j::j])
    return [i for i in range(n) if a[i]]


def vp(n,p):
    r=0
    while n and n%p==0:
        n//=p
        r+=1
    return r


def pfree_fact(n,p):
    ans=1
    for j in range(1,n+1):
        z=j
        while z%p==0:
            z//=p
        ans=(ans*z)%p
    return ans


def normalized_midpoint(p):
    h=(p-1)//2
    result=[]
    for k in (h,h+1):
        a=factorial(k)%p
        denw=pow(a,5,p)*pow(216,k,p)%p
        dens=pow(a,4,p)*pow(2304,k,p)%p
        wu=(6*k+1)*pfree_fact(2*k,p)*pfree_fact(3*k,p)*pow(denw,-1,p)%p
        su=(8*k+1)*pfree_fact(4*k,p)*pow(dens,-1,p)%p
        result.append((wu,su))
    return tuple(result)


def w(k):
    return Fraction((6*k+1)*factorial(2*k)*factorial(3*k),
                    factorial(k)**5*216**k)


def s(k):
    return Fraction((8*k+1)*factorial(4*k),
                    factorial(k)**4*2304**k)


def exact_normalized(x,p,exponent):
    assert vp(x.numerator,p)==exponent
    assert vp(x.denominator,p)==0
    return (x.numerator//p**exponent)*pow(x.denominator,-1,p)%p


def test():
    cases=[p for p in primes_below(1000) if p>=7 and p%6==1]
    assert len(cases)==80
    spots={7,13,19,37,43,211,373}
    for p in cases:
        h=(p-1)//2
        (u,v),(u2,v2)=normalized_midpoint(p)
        chi=pow(6,h,p)
        assert chi in (1,p-1)
        sign=1 if chi==1 else -1
        assert u==4*sign%p and v==3
        assert u2==4*sign*pow(9,-1,p)%p
        assert v2==5*pow(36,-1,p)%p
        d0=(u-v)%p
        d1=(u2-v2)%p
        assert d0==(4*sign-3)%p
        assert d1==(16*sign-5)*pow(36,-1,p)%p
        if p>7:
            assert (108*d1-5*d0)*pow(7,-1,p)%p==u
            assert (108*d1-12*d0)*pow(7,-1,p)%p==v
        else:
            assert (d0,d1)==(0,0)
        if p in spots:
            assert exact_normalized(w(h),p,1)==u
            assert exact_normalized(s(h),p,1)==v
            assert exact_normalized(w(h+1),p,2)==u2
            assert exact_normalized(s(h+1),p,2)==v2
        if p==373:
            assert h==186
            assert (u,v,u2,v2,d0,d1)==(369,3,41,197,366,217)
    print("PASS_D25_ORIGINAL_MIDPOINT_TWO_PORT",
          {"primes_7_to_997_1mod6":len(cases),
           "independent_rational_checks":sorted(spots),
           "p373":(369,3,41,197,366,217),
           "p7_exception":(0,0),
           "native_H0B0_executed":False})


if __name__=="__main__":
    test()
