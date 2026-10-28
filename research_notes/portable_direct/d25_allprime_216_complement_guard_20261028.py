#!/usr/bin/env python3
"""Exact finite ring certificate for universal original-216 high-band reflection.
AUTHOR-SIDE test, NOT original H0/B0 native benchmark.
"""
from math import comb, isqrt


def primes_below(n):
    out = []
    for k in range(5, n):
        if all(k % j for j in range(2, isqrt(k) + 1)):
            out.append(k)
    return out


def original_coefficients(p, power=3):
    mod = p ** power
    arr = [1]
    for k in range(p - 1):
        inv = pow(36 * (k + 1) ** 3, -1, mod)
        arr.append((arr[-1] * (2*k+1) * (3*k+1) * (3*k+2) * inv) % mod)
    return arr


def published_comparator_coefficients(p, power=3):
    mod = p ** power
    arr = [1]
    for k in range(p - 1):
        inv = pow(288 * (k + 1) ** 3, -1, mod)
        arr.append((arr[-1] * (2*k+1) * (4*k+1) * (4*k+3) * inv) % mod)
    return arr


def check_prime(p):
    h = (p-1)//2
    lo = (p+2)//3  # ceil(p/3) for every p>3
    mod=p**3
    arr=original_coefficients(p)
    bb=published_comparator_coefficients(p)
    mirror=0
    pairs=0
    for j in range(lo, h+1):
        low=arr[j]
        high=arr[p-j]
        assert low % p==0 and high % (p*p)==0
        u=(low//p)%p
        v=(high//(p*p))%p
        assert u and v
        assert (u*v*36*j**3)%p==1, (p,j,u,v)
        mirror=(mirror+(1-6*j)*v)%p
        pairs+=1
    a_low=sum((6*n+1)*arr[n] for n in range(h+1))%mod
    a_tail=sum((6*n+1)*arr[n] for n in range(h+1,p))%mod
    expected_tail=(p*p*mirror)%mod
    assert a_tail==expected_tail, (p,a_tail,expected_tail)
    b_low=sum((8*n+1)*bb[n] for n in range(h+1))%mod
    b_tail=sum((8*n+1)*bb[n] for n in range(h+1,p))%mod
    assert b_tail==0, (p,b_tail)
    assert (a_low-b_low)%(p*p)==0, (p,a_low,b_low)
    assert (a_low+a_tail-b_low-b_tail)%mod==0, (p,a_low,a_tail,b_low,b_tail)
    if p in (5,7,11,13,19,37,43,211,373):
        for n in (lo,h,p-lo):
            factorial=comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod)%mod
            assert arr[n]==factorial, (p,n)
    return pairs,{
        'p':p,'halfcut_digit':((a_low-b_low)%mod)//(p*p),
        'complement_digit':a_tail//(p*p),
        'B_tail_digit':b_tail//(p*p),
        'A_full_minus_B_full':(a_low+a_tail-b_low-b_tail)%mod,
        'pairs':pairs,'lower_j':lo,'upper_j':h
    }


def main():
    ps=primes_below(1300)
    pairs=0
    target=[]
    other=[]
    witnesses=[]
    for p in ps:
        z,w=check_prime(p)
        pairs+=z
        if p%6==1: target.append(p)
        else: other.append(p)
        if p in (5,7,11,13,19,37,43,211,373): witnesses.append(w)
    assert 373 in target and 5 in other
    print('PASS_D25_A216_UNIVERSAL_REFLECTION',len(ps),'primes <1300;',pairs,'paired indices')
    print('FROZEN_CLASS_COUNT',sum(p%24 in (13,19) for p in ps))
    print('NEW_P_MOD_6_EQ_5_EXTENSION',len(other),'primes')
    for w in witnesses:print('PORT_WITNESS',w)


if __name__=='__main__':main()
