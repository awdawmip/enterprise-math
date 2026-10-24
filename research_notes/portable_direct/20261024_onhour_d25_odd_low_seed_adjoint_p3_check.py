#!/usr/bin/env python3
"""Author-side exact checks for D25 odd-low-seed Jacobi-adjoint p^3 result.

Only Python's exact Fraction arithmetic and integer modular reductions are used.
No native benchmark, Source admission or independent mathematical review is inferred.
"""
from fractions import Fraction as Q
from math import factorial


def primes_upto(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00'*(((n-i*i)//i)+1)
    return [i for i in range(n+1) if sieve[i]]


def residue(x, p, exp):
    mod = p**exp
    assert x.denominator % p, ("nonunit denominator", p, x)
    return (x.numerator * pow(x.denominator, -1, mod)) % mod


def valuation_int(x, p):
    if x == 0:
        return 1000000
    k=0
    while x % p == 0:
        x//=p
        k+=1
    return k


def valuation(x,p):
    return valuation_int(x.numerator,p)-valuation_int(x.denominator,p)


def source_terms(r):
    # Independent original rational source-ratio path (unreduced hypergeometric).
    A=Q(factorial(6*r),3**(6*r)*factorial(2*r)**3)
    R=Q(1)
    out=[]
    for n in range(4*r+1):
        out.append(A*(6*n+12*r+1)*R)
        if n<4*r:
            R*=Q((4*r+2*n+1)*(3*n+1)*(3*n+2),
                 36*(n+1)*(2*r+n+1)*(4*r+n+1))
    return A,out


def odd_seed_jet(r,p):
    assert p==12*r-5 and p>=19
    K=4*r-3
    u=Q(1)
    D=E=Q(0)
    C=F=M2=M5=nD=dC=nE=Q(0)
    for n in range(K+1):
        c=u*Q(10,(3*n+2)*(3*n+5))
        C+=c
        F+=u
        M2+=u*Q(3,3*n+2)
        M5+=u*Q(3,3*n+5)
        nD+=(n+1)*c*D
        dC+=c*D
        nE+=(n+1)*c*(D*D-E)
        if n<K:
            j=n
            D+=(Q(1,2*(j-K))+Q(1,3*(j-K-1))
                -Q(1,2*j+1-2*K)-Q(1,3*j+8))
            E+=(Q(1,4*(j-K)**2)+Q(1,9*(j-K-1)**2)
                -Q(1,(2*j+1-2*K)**2)-Q(1,(3*j+8)**2))
            u*=Q((j-K)*(j-K-1),
                 2*(j+1))*Q(2,2*j+1-2*K)
    L=Q(5,27)*(4*M2-(p+5)*M5+3*F)
    # Exact rational moment identity, not just an observed congruence.
    assert 2*(6*K+7)*M2-(3*K+5)*(3*K+8)*M5 == -3*p*F
    # Independent rational c_n recomputation checks exact p*L factor.
    csum=Q(0)
    for n in range(K+1):
        numerator=Q(1)
        denominator=Q(1)
        for j in range(n):
            numerator*=(-K+j)*(-K-1+j)
            denominator*=(Q(1,2)-K+j)*2*(j+1)
        csum+=(n+1)*Q(10,(3*n+2)*(3*n+5))*numerator/denominator
    assert csum == p*L
    return C,L,nD,dC,nE,M2,M5,F


def check_one_prime(p):
    assert p>=19 and (p+5)%12==0
    r=(p+5)//12
    K=4*r-3
    A,terms=source_terms(r)
    U,V,W=terms[-3:]
    for n,t in enumerate(terms):
        expected=0 if n<=K else (1 if n==K+1 else 2)
        assert valuation(t,p)==expected, (p,n,expected,valuation(t,p))
    assert valuation(A,p)==0
    assert valuation(U,p)==1
    assert residue(V+W,p,3)==residue(Q(103*p,1500)*U,p,3)
    C,L,nD,dC,nE,M2,M5,F=odd_seed_jet(r,p)
    assert all(valuation(x,p)>=0 for x in (C,L,nD,dC,nE,M2,M5,F))
    predicted=(A*(C+6*L+6*nD+p*(dC+3*nE))
               + U/p*(1+Q(103*p,1500)))
    actual=sum(terms,Q(0))/p
    assert valuation(sum(terms,Q(0)),p)>=1
    predicted_residue=residue(predicted,p,2)
    actual_residue=residue(actual,p,2)
    assert predicted_residue==actual_residue,(p,r,predicted_residue,actual_residue)
    return (p,r,actual_residue,residue(U/p,p,2),residue((V+W)/p**2,p,1))


def jacobi_checks():
    # Independently evaluate the polynomial derivative and polynomial moments.
    for K in range(1,26,2):
        u=Q(1)
        units=[]
        for n in range(K+1):
            units.append(u)
            if n<K:
                u*=Q((n-K)*(n-K-1), 2*(n+1))*Q(2,2*n+1-2*K)
        F=sum(units,Q(0))
        deriv=sum((n*un for n,un in enumerate(units)),Q(0))
        assert deriv==(K+1)*F, (K,F,deriv)
        M2=sum((un*Q(3,3*n+2) for n,un in enumerate(units)),Q(0))
        M5=sum((un*Q(3,3*n+5) for n,un in enumerate(units)),Q(0))
        assert 2*(6*K+7)*M2-(3*K+5)*(3*K+8)*M5==-3*(3*K+4)*F
    return 13


if __name__=='__main__':
    print('Jacobi/moment exact odd-degree checks:',jacobi_checks())
    p19=[];other=[]
    for p in primes_upto(1000):
        if p>=19 and p%12==7:
            row=check_one_prime(p)
            (p19 if p%24==19 else other).append(row)
    print('p≡19(mod24) target primes:',len(p19),'ALL PASS')
    print('p≡7(mod24) additional primes:',len(other),'ALL PASS')
    for row in [x for x in p19 if x[0] in (19,43,67,163,211,283,307)]:
        print('p,r,S_r/p mod p²,U/p mod p²,(V+W)/p² mod p:',row)
    print('PASS: odd LOW seed first-digit theorem and independent full third-digit jet checked')
