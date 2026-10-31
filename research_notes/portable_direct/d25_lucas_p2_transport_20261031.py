#!/usr/bin/env python3
"""Exact first p-adic Lucas transport at integer-carrier square-divisor progressions.

Author-side exact signed combinatorial calculation; original native H0/B0
benchmark and canonical Source approval are separate.
"""
from math import comb


def signed_U_mod(l, p, gamma=1):
    """Full original binomial carrier with test weight 6k+gamma mod p^2."""
    modulus=p*p
    total=0
    for k in range(2*l+1):
        t=((6*k+gamma)*(-1 if k%2 else 1)*pow(2,2*l-k,modulus))%modulus
        term=(comb(3*l,k)%modulus)*(comb(2*l,k)%modulus)*(comb(4*l,k)%modulus)
        total=(total+t*term)%modulus
    return total


def digit_product(p, t):
    """Unweighted Lucas high-port from base-p digits of 3t,2t,4t."""
    tops=[3*t,2*t,4*t]
    inv2=pow(2,-1,p)
    product=1
    while any(tops):
        a,b,c=(n%p for n in tops)
        v=0
        for k in range(min(a,b,c)+1):
            v+=pow(-inv2,k,p)*comb(a,k)*comb(b,k)*comb(c,k)
        product=product*v%p
        tops=[n//p for n in tops]
    return product


def low_observer(p, l, gamma):
    tops=[(s*l)%p for s in (3,2,4)]
    inv2=pow(2,-1,p)
    return sum((6*k+gamma)*pow(-inv2,k,p)*comb(tops[0],k)*comb(tops[1],k)*comb(tops[2],k)
               for k in range(min(tops)+1))%p


def run():
    probes=0
    nonzero_controls=0
    for p in (5,7,11,13,17,19):
        seed=(p*p-1)//6
        assert (6*seed+1)==p*p
        for gamma in (1,1+p,1+2*p):
            assert low_observer(p,seed,gamma)==0, (p,gamma)
            seed_u=signed_U_mod(seed,p,gamma)
            if seed_u:
                nonzero_controls+=1
            for t in range(5 if p<=11 else 3):
                l=seed+p*p*t
                target=signed_U_mod(l,p,gamma)
                high=digit_product(p,t)
                pred=pow(2,2*p*p*t,p*p)*seed_u*high%(p*p)
                assert pred==target,(p,t,gamma,seed_u,high,pred,target)
                if gamma==1:
                    assert target==0,(p,t,target)
                probes+=1
                print('TRANSPORT',p,t,gamma,'seed',seed_u,'high',high,'observed',target,'pred',pred)
    print('PASS_D25_P2_LUCAS_ARITHMETIC_PROGRESSION_TRANSPORT')
    print('EXACT_PROBES',probes,'NONZERO_SEED_CONTROLS',nonzero_controls)


if __name__=='__main__':
    run()
