#!/usr/bin/env python3
"""Independent, exact check of the D25 original-endpoint n-direction telescope.

Author-side arithmetic only. Not a Source Result or native benchmark.
All reported congruences use integer modular arithmetic or exact fractions.
"""
from fractions import Fraction as F
from math import factorial, comb
import json
import sys


def inv(a, modulus):
    return pow(a % modulus, -1, modulus)


def frac_mod(value, modulus):
    value = F(value)
    return value.numerator * inv(value.denominator, modulus) % modulus


def regular_factor(n):
    return F((1-3*n)*(6*n+3),(3*n+2)*(3*n+1))


def full_factor(n,p):
    return F((2*p+1-3*n)*(2*p+3+6*n),(3*n+p+2)*(3*n+2*p+1))


def low_jet_H(n,m):
    return sum((F(1,2*(j-m))-F(1,3*j+2)-F(2,3*j+1) for j in range(n)), F(0))


def factor_jet_L(n):
    return F(2,1-3*n)+F(2,6*n+3)-F(1,3*n+2)-F(2,3*n+1)


def exact_small(m):
    p=6*m+1
    nmax=4*m
    R=[F(1)]
    for n in range(nmax+1):
        R.append(R[-1]*F((4*m+2*n+1)*(3*n+1)*(3*n+2),36*(n+1)*(2*m+n+1)*(4*m+n+1)))
    raw=sum(((6*n+2*p-1)*R[n] for n in range(nmax+1)), F(0))
    diff=-12*(nmax+1)*R[nmax+1]+p*sum((full_factor(n,p)*R[n] for n in range(nmax+1)),F(0))
    assert raw==diff
    q=F(factorial(12*m)*factorial(2*m),216**m*factorial(6*m)*factorial(8*m))
    q_product=F(1,3*216**m)
    for a in range(2*m,p-1): q_product*=1+F(p,a)
    assert q==q_product
    assert R[nmax]/R[2*m]==q*q
    alpha2=F((p+2)*(4*p+1),3*(2*p+1))
    c4=F(-8*p*p+14*p-3,4*p-1)
    u2=R[2*m]/p
    exact_decomp=(sum((full_factor(n,p)*R[n] for n in range(m+1)),F(0))
        +sum((full_factor(n,p)*R[n] for n in range(m+1,nmax) if n !=2*m),F(0))
        +(alpha2+c4*q*q)*u2)
    assert raw/p==exact_decomp
    return p


def strip_factorial_mod_p(limit,p):
    vals=[1]*(limit+1)
    for t in range(1,limit+1):
        a=t
        while a%p==0:a//=p
        vals[t]=vals[t-1]*(a%p)%p
    return vals


def term_unit_at_high(n,m,p,ufac):
    # v_p(R_(m,n))=1 in the range m+1 <= n <= 4m.
    top=ufac[4*m+2*n]*pow(factorial(2*m),2,p)*ufac[3*n]
    bot=pow(216,n,p)*pow(ufac[2*m+n],2,p)*ufac[4*m+n]*pow(factorial(n),2,p)
    return (top%p)*inv(bot,p)%p


def original_via_recurrence_mod_p3(m,p):
    modulus=p**3
    A=factorial(6*m)*inv(pow(3,6*m,modulus)*pow(factorial(2*m),3,modulus),modulus)%modulus
    nmax=4*m
    v=0
    u=1
    total=0
    for n in range(nmax+1):
        assert v==(0 if n<=m else 1),(p,n,v)
        total=(total+A*(6*n+12*m+1)*u*pow(p,v,modulus))%modulus
        if n==nmax: break
        numerator=[4*m+2*n+1,3*n+1,3*n+2]
        denominator=[36,n+1,2*m+n+1,4*m+n+1]
        vd=0
        def strip(x):
            nonlocal vd
            while x%p==0:
                vd+=1
                x//=p
            return x
        num=1;den=1
        for x in numerator:num=num*strip(x)%modulus
        plus=vd
        vd=0
        for x in denominator:den=den*strip(x)%modulus
        v+=plus-vd
        u=u*num*inv(den,modulus)%modulus
    return total,A


def one_carry_jet_mod_p2(m,p):
    modulus=p*p
    uf=strip_factorial_mod_p(2*p+1,p)
    low=0
    for n in range(m+1):
        b=F((-1)**n*comb(m,n),2**n)
        part=b*regular_factor(n)
        low=(low+frac_mod(part,modulus)+p*frac_mod(part*(low_jet_H(n,m)+factor_jet_L(n)),p))%modulus
    high=0
    for n in range(m+1,4*m):
        if n==2*m:continue
        high=(high+frac_mod(regular_factor(n),p)*term_unit_at_high(n,m,p,uf))%p
    hm=sum((inv(a,p) for a in range(1,2*m)),0)%p
    fq6=(pow(6,p-1,p*p)-1)//p
    carry_c=(F(19,9)-F(2,3)*hm-F(1,3)*fq6)
    c=(1+p*frac_mod(carry_c,p))%modulus
    # Exact p-free factorial identity for R_(m,2m)/p.
    u2=(factorial(p-1)*factorial(2*m-1)*inv(pow(216,2*m,modulus)*pow(factorial(4*m),2,modulus),modulus))%modulus
    u2=u2*(1+p*hm)%modulus
    result=(low+p*high+u2*c)%modulus
    first_cauchy=(-2*inv(pow(2,m,p),p)
        +2*sum(((-1)**j*comb(m,j)*inv(pow(2,j,p)*(3*j+1),p) for j in range(m+1)),0)
        +3*sum(((-1)**j*comb(m,j)*inv(pow(2,j,p)*(3*j+2),p) for j in range(m+1)),0)
        +u2)%p
    return result,first_cauchy,low,high,u2,c


def primes_upto(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for d in range(2,int(limit**0.5)+1):
        if sieve[d]:
            sieve[d*d::d] = b"\x00" * ((limit-d*d)//d+1)
    return (p for p in range(2,limit+1) if sieve[p])

def main(limit):
    checked=0
    target_classes=0
    records=[]
    for p in primes_upto(limit):
        if p<7:continue
        if p%6!=1:continue
        m=(p-1)//6
        raw,A=original_via_recurrence_mod_p3(m,p)
        assert raw%p==0,(p,'not divisible')
        normalized=raw//p*inv(A,p*p)%(p*p)
        calc,first,low,high,u2,c=one_carry_jet_mod_p2(m,p)
        assert normalized==calc,(p,'jet mismatch',normalized,calc)
        assert calc%p==first,(p,'first digit mismatch')
        rhs=pow(4,p-1,p*p)*pow(factorial(2*m),3,p*p)*inv(factorial(p-1),p*p)%(p*p)
        if p%24 in (13,19):
            target_classes+=1
            assert rhs==calc,(p,'target issue',calc,rhs)
        records.append(dict(p=p,m=m,normalized=normalized,jet=calc,target=rhs,
                            first=first,high_mod_p=high,carry_u2=u2,carry_coeff=c,
                            hard_target_class=p%24 in (13,19)))
        checked+=1
    small=[exact_small(m) for m in range(1,9)]
    print(json.dumps(dict(limit=limit,primes_checked=checked,target_class_primes=target_classes,
        exact_rational_parameters_6m_plus_1=small,first_three=records[:3],last_three=records[-3:]),indent=2))
    import pathlib
    path=pathlib.Path('/mnt/data/enterprise_math/d25_one_carry_validation.json')
    path.write_text(json.dumps(dict(scope='author exact arithmetic; not Source benchmark',
        limit=limit,exact_rational_parameters_6m_plus_1=small,records=records),ensure_ascii=False,indent=2)+'\n')
    print('RECORDS_FILE',path)


if __name__=='__main__':
    main(int(sys.argv[1]) if len(sys.argv)>1 else 1000)
