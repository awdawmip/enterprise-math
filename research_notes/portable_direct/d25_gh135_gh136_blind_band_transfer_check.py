#!/usr/bin/env python3
"""GH135-136 finite-field exact transfer/check; reuse published GH129 coefficient tools."""
from math import comb, isqrt
from d25_gh129_blind_band_check import (
    add, mul, scale, neg, inv, fact_tables, coefficient_prediction,
)

def marked_B(p):
    return (pow(8, -1, p), pow(12, -1, p))

def recurrence_values(p, B):
    N=(p-1)//2
    fac,ifac=fact_tables(p)
    m1,_=coefficient_prediction(p,B,1,fac,ifac)
    m2,_=coefficient_prediction(p,B,2,fac,ifac)
    leading=scale(mul(B,add((1,0),scale(B,-4,p),p),p),4,p)
    assert leading!=(0,0),"smooth marked parameter required"
    m=[None,m1,m2]
    for s in range(1,N-1):
        b=scale(add((1,0),scale(B,-8,p),p),2*(2*s+1),p)
        num=add(mul(scale(b,s,p),m[s+1],p),scale(m[s],16*s*s-1,p),p)
        den=scale(leading,s*(s+1),p)
        m.append(mul(num,inv(den,p),p))
    assert len(m)==N+1
    return m,fac,ifac

def check_triangular(p,B,vals,fac,ifac):
    h=(p-3)//4;N=(p-1)//2;s0=h+1
    m0,parts0=coefficient_prediction(p,B,s0,fac,ifac)
    m1,parts1=coefficient_prediction(p,B,s0+1,fac,ifac)
    A0,E0=parts0[4:6]
    A1,E1=parts1[4:6]
    assert (E0,E1)==((1,0),(0,0))
    FB=mul(B,add((1,0),scale(B,-4,p),p),p)
    def power(a,n):
        z=(1,0)
        while n:
            if n&1:z=mul(z,a,p)
            a=mul(a,a,p);n>>=1
        return z
    exact_A1=scale(power(FB,h),(-1)**h*comb(N,h),p)
    assert A1==exact_A1 and A1!=(0,0)
    assert (m0,m1)==(vals[s0],vals[s0+1])
    probe=range(s0+1,N+1) if p<=107 else [s0+1,s0+2,1000,N-1,N]
    for s in probe:
        _,parts=coefficient_prediction(p,B,s,fac,ifac)
        As,Es=parts[4:6]
        assert Es==(0,0)
        assert vals[s]==mul(mul(As,inv(A1,p),p),m1,p)
    U=neg(mul(m1,inv(A1,p),p),p)
    V=neg(add(m0,mul(A0,U,p),p),p)
    C=power(U,p);D=power(V,p)
    H=add(D,scale(mul(B,C,p),2,p),p)
    S1=neg(mul(C,add(V,scale(mul(power(B,p),U,p),2,p),p),p),p)
    assert (H,C,D)==(parts0[0],parts0[2],parts0[3])
    assert S1==scale(mul(parts0[1],power(H,p),p),2,p)
    return (s0,A0,A1,U,V,S1)

def check_coeff_identity(p):
    assert p%4==3 and p>=7
    h=(p-3)//4;N=(p-1)//2;t=3*h+1
    fact=[1]*p
    for j in range(1,p):fact[j]=fact[j-1]*j%p
    ifact=[pow(v,-1,p) for v in fact]
    for a in range(h+1):
        c=fact[t]*ifact[a]*ifact[2*h+1-2*a]*ifact[h+a]%p
        target=(-1)**(h+a)*comb(N,h)*comb(h,a)*pow(4,a,p)%p
        assert c==target,(p,a,c,target)
    return h+1

def main():
    primes=(7,11,19,23,31,43,47,59,67,71,79,83,103,107,127,131,139,151,163,167,179,191,199,211,227,239,251,263,271,283,307,331,347,359,367,379,383,419,431,443,463,467,479,487,499)
    polys=0
    for p in primes:
        assert all(p%d for d in range(2,isqrt(p)+1))
        polys+=check_coeff_identity(p)
    total=0;cases=0
    for p in (11,19,43,59,83,107):
        for B in (marked_B(p),(3,1),(4,0)):
            if B in ((0,0),(pow(4,-1,p),0)):continue
            vals,fac,ifac=recurrence_values(p,B)
            for s in range(1,(p-1)//2+1):
                direct,_=coefficient_prediction(p,B,s,fac,ifac)
                assert vals[s]==direct,(p,B,s)
                total+=1
            check_triangular(p,B,vals,fac,ifac)
            cases+=1
    extra=check_coeff_identity(3347)
    print("PASS_GH135_FULL_BAND_RECURRENCE field_cases",cases,"moments",total)
    print("PASS_GH136_EXACT_POLYNOMIAL_CENTRAL_COEFFICIENT small_prime_instances",len(primes),"coefficients",polys,"p3347_coefficients",extra)
    p=3347;B=marked_B(p);N=(p-1)//2;h=(p-3)//4
    vals,fac,ifac=recurrence_values(p,B)
    for s in [1,2,3,h,h+1,h+2,h+3,h+4,1000,N-1,N]:
        direct,_=coefficient_prediction(p,B,s,fac,ifac)
        assert vals[s]==direct
    middle=check_triangular(p,B,vals,fac,ifac)
    assert middle==(837,(837,1149),(954,0),(0,2702),(568,998),(0,362))
    assert (vals[837],vals[838],vals[839])==((2268,0),(0,2829),(97,0))
    print("P3347_CENTRAL_CERTIFICATE",middle,"m_s0_s0+1_s0+2",vals[837:840])
    print("PASS_GH135_GH136_PORTABLE_EXACT")

if __name__=="__main__":main()
