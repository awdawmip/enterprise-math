#!/usr/bin/env python3
"""Exact author-side R39 checks for unchanged-input W2/S2 overlap transfer.

Python standard library only. Uses p-free original factorial products,
independently of short transfer products. Not native original-class H0/B0.
"""
from fractions import Fraction
from math import factorial

def prime_list(limit):
    result=[]
    for p in range(7,limit+1):
        if p%6!=1: continue
        if all(p%q for q in range(2,int(p**0.5)+1)): result.append(p)
    return result

def unitfac(n,p,modulus):
    assert n<p*p
    out=1
    for i in range(1,n+1):
        out=out*(i//p if i%p==0 else i)%modulus
    return out

def inv(x,modulus):
    return pow(x%modulus,-1,modulus)

def step_product(p,shift,count,modulus):
    v=1
    for i in range(1,count+1):
        v=v*(i+shift)*inv(i,modulus)%modulus
    return v

def original_normalized(p,k,modulus):
    # Genuine w_k/p^2 and s_k/p^2, including the weight zero at p=13 mod24.
    w=(6*k+1)*unitfac(2*k,p,modulus)*unitfac(3*k,p,modulus)
    w*=inv(unitfac(k,p,modulus)**5*pow(216,k,modulus),modulus)
    s=(8*k+1)*unitfac(4*k,p,modulus)
    s*=inv(unitfac(k,p,modulus)**4*pow(2304,k,modulus),modulus)
    return w%modulus,s%modulus

def regularized_factor(p,k,a,b,r,modulus):
    return (2*factorial(k)*factorial(r)*pow(3,k,modulus)
            *inv(factorial(a)*factorial(b)*pow(32,k,modulus),modulus))%modulus

def compact_factor(p,k,a,b,r,modulus):
    return regularized_factor(p,k,a,b,r,modulus)*(8*k+1)*inv(6*k+1,modulus)%modulus

def regularized_transfer_mod(p,k,modulus):
    a,b,r=2*k-p,3*k-p,4*k-2*p
    c=regularized_factor(p,k,a,b,r,modulus)
    numerator=step_product(p,p,p-1,modulus)*step_product(p,2*p,r,modulus)%modulus
    denominator=step_product(p,p,a,modulus)*step_product(p,p,b,modulus)%modulus
    return c*numerator*inv(denominator,modulus)%modulus

def exact_transfer_mod(p,k,modulus):
    a,b,r=2*k-p,3*k-p,4*k-2*p
    assert 0<=a<p and 0<=b<p and 0<=r<p and k<p
    c=compact_factor(p,k,a,b,r,modulus)
    numerator=step_product(p,p,p-1,modulus)*step_product(p,2*p,r,modulus)%modulus
    denominator=step_product(p,p,a,modulus)*step_product(p,p,b,modulus)%modulus
    return c*numerator*inv(denominator,modulus)%modulus

def harmonic_mod(n,p):
    return sum(pow(i,-1,p) for i in range(1,n+1))%p

def first_jet_mod(p,k):
    modulus=p*p
    a,b,r=2*k-p,3*k-p,4*k-2*p
    c=compact_factor(p,k,a,b,r,modulus)
    e=(harmonic_mod(p-1,p)+2*harmonic_mod(r,p)
       -harmonic_mod(a,p)-harmonic_mod(b,p))%p
    return c*(1+p*e)%modulus

def original_fraction_ratio(k):
    w=Fraction((6*k+1)*factorial(2*k)*factorial(3*k),
               factorial(k)**5*216**k)
    s=Fraction((8*k+1)*factorial(4*k),factorial(k)**4*2304**k)
    return s/w

def exact_fraction_transfer(p,k):
    a,b,r=2*k-p,3*k-p,4*k-2*p
    out=Fraction(2*(8*k+1)*factorial(k)*factorial(r)*3**k,
                 (6*k+1)*factorial(a)*factorial(b)*32**k)
    for i in range(1,p): out*=Fraction(p+i,i)
    for i in range(1,r+1): out*=Fraction(2*p+i,i)
    for n in (a,b):
        for i in range(1,n+1): out/=Fraction(p+i,i)
    return out

def main():
    primes=prime_list(997)
    npos=0;special=0;rows=[]
    for p in primes:
        m=(p-1)//6
        modulus=p**3
        pairW=0;pairS=0;S=0
        for j in range(2*m,3*m):
            k=p-1-j
            wn,sn=original_normalized(p,k,modulus)
            assert wn%p!=0
            lam=sn*inv(wn,modulus)%modulus
            assert exact_transfer_mod(p,k,modulus)==lam,(p,j,'exact')
            assert first_jet_mod(p,k)==lam%(p*p),(p,j,'jet')
            tau=regularized_transfer_mod(p,k,modulus)
            assert tau%p!=0
            assert tau*(8*k+1)*inv(6*k+1,modulus)%modulus==lam
            if k<4*m:
                tau_next=regularized_transfer_mod(p,k+1,modulus)
                num=(4*k+1)*(4*k+2)*(4*k+3)
                den=16*(2*k+1)*(3*k+1)*(3*k+2)
                assert den%p!=0,(p,k)
                assert tau_next==tau*num*inv(den,modulus)%modulus
            if 8*k+1==5*p:
                special+=1
                assert p%24==13 and lam%p==0 and lam%(p*p)!=0
                a,b,r=2*k-p,3*k-p,4*k-2*p
                expected=(10*factorial(k)*factorial(r)*pow(3,k,p)
                    *inv((6*k+1)*factorial(a)*factorial(b)*pow(32,k,p),p))%p
                assert (lam//p)%p==expected
                if p in (13,37,181,373,733):
                    rows.append((p,j,k,wn%p,lam%(p*p),(lam//p)%p,expected))
            else:
                assert lam%p!=0,(p,j)
            npos+=1
            pairW=(pairW+wn)%(p*p)
            pairS=(pairS+sn)%(p*p)
            S=(S+wn*(1-lam))%(p*p)
        assert S==(pairW-pairS)%(p*p)
        if p in (13,19,181,373,733):
            rows.append((p,'paired mod p^2',pairW,pairS,S,None,None))
    fractions=0
    for p in (7,13,19,37):
        m=(p-1)//6
        for j in range(2*m,3*m):
            k=p-1-j
            assert exact_fraction_transfer(p,k)==original_fraction_ratio(k)
            fractions+=1
    print('PASS primes=',len(primes),'paired_index_assertions=',npos,
          'weight_zero_indices=',special,'independent_fraction_checks=',fractions)
    for row in rows:print('ROW',row)

if __name__=='__main__':main()
