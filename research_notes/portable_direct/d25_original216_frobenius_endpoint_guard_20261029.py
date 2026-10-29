#!/usr/bin/env python3
"""Exact integer guard for the original A216 3F2, NOT a native H0/B0 run.

Independent inputs: a_n = C(2n,n)^2*C(3n,n)/216**n, theta=z d/dz,
L = theta**3 - (z/2)(theta+1/2)(theta+1/3)(theta+2/3).
All modular divisions use inverses of p-units; no floating point.
"""
from math import comb, isqrt


def primes_below(limit):
    return [p for p in range(5,limit)
            if all(p % d for d in range(2,isqrt(p)+1))]


def original_coeff_mod(n,p,k=4):
    mod=p**k
    return (comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod))%mod


def endpoint_by_recurrence(p):
    """No division by p: iterate n=0,...,p-2 in (Z/p^4Z)."""
    mod=p**4; a=1
    for n in range(p-1):
        a = (a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod))%mod
    assert a % (p**3)==0, (p,'wrong valuation')
    return a


def binom_modp_lucas(n,k,p):
    z=1
    while n or k:
        a,b=n%p,k%p
        if b>a:
            return 0
        z=z*comb(a,b)%p
        n//=p;k//=p
    return z


def direct_A_modp(n,p):
    return original_coeff_mod(n,p,k=1)


def lucas_A_modp(n,p):
    return (binom_modp_lucas(2*n,n,p)**2
            *binom_modp_lucas(3*n,n,p)
            *pow(216,-n,p))%p


def base_p_digit_sum(n,p):
    total=0
    while n:
        total += n%p
        n//=p
    return total


def valuation_by_digits(n,p):
    return (5*base_p_digit_sum(n,p)
            -base_p_digit_sum(2*n,p)
            -base_p_digit_sum(3*n,p))//(p-1)


def int_p_valuation(n,p):
    if not n:
        return None
    k=0
    while n%p==0:
        n//=p;k+=1
    return k


def support_by_digits(n,p):
    bound=(p-1)//3
    while n:
        if n%p > bound:
            return False
        n//=p
    return True


def main():
    ps=primes_below(1200)
    for p in ps:
        mod=p**4
        a=endpoint_by_recurrence(p)
        assert a//p**3 == p-1, ('a_(p-1)/p^3',p,a)
        # Independent exact-integer binomial coefficient path for the endpoint.
        assert original_coeff_mod(p-1,p)==a, ('binomial endpoint',p)
        ap=original_coeff_mod(p,p,k=1)
        assert ap==pow(18,-1,p), ('a_p',p,ap)
        c=(2*p-1)*(3*p-2)*(3*p-1)*pow(36,-1,mod)%mod
        boundary=-c*a%mod
        expected=-(p**3)*pow(18,-1,mod)%mod
        assert boundary==expected, ('PF boundary',p,boundary,expected)
    # Independent direct full integer binomial checks for every N in finite p^2 blocks.
    exhaustive=(5,7,11,13,19)
    observed=0
    for p in exhaustive:
        for N in range(p*p):
            r=direct_A_modp(N,p)
            assert r==lucas_A_modp(N,p), ('digit binomial Lucas',p,N)
            assert bool(r)==support_by_digits(N,p), ('digit support',p,N,r)
            observed+=1
    # Verify the product law in finite digit blocks, including carry cases.
    pairs=0
    for p in (5,7,11,13,17,19,23,31,43):
        for n in range(7):
            an=direct_A_modp(n,p)
            for r in range(p):
                left=direct_A_modp(p*n+r,p)
                right=an*direct_A_modp(r,p)%p
                assert left==right,(p,n,r,left,right)
                pairs+=1
    valuation_tests=0
    for p in (5,7,11,13,17,19,23,29,31,37,43):
        for n in range(1,201):
            c=comb(2*n,n)**2*comb(3*n,n)
            assert valuation_by_digits(n,p)==int_p_valuation(c,p),(p,n)
            valuation_tests += 1
    p=373
    a=endpoint_by_recurrence(p)
    mod=p**4
    c=(2*p-1)*(3*p-2)*(3*p-1)*pow(36,-1,mod)%mod
    bound=(-c*a)%mod
    assert bound==(p**4-p**3*pow(18,-1,mod)%mod)%mod
    print('PASS_ORIGINAL_A216_SHARP_PF_ENDPOINT primes_5_le_p_lt_1200',len(ps))
    print('PASS_DIRECT_INTEGER_LUCAS_SUPPORT_P2_BLOCKS',observed,'p=',exhaustive)
    print('PASS_DIRECT_INTEGER_LUCAS_PAIR_LAW',pairs,'cases')
    print('PASS_KUMMER_DIGIT_SUM_VALUATION',valuation_tests,'cases')
    print('P373',{'p2':p**2,'p3':p**3,'p4':p**4,
        'a_pminus1_modp4':a,'a_pminus1_overp3_modp':a//p**3,
        'a_p_modp':direct_A_modp(p,p),
        'PF_boundary_coeff_modp4':bound,
        'nonzero_modp4':bound!=0,
        'support_digits_below_p':(p-1)//3+1,
        'support_digits_below_p2':((p-1)//3+1)**2,
        'valuation_n_pminus1_p_pplus1':[(n,valuation_by_digits(n,p))
          for n in (p-1,p,p+1)]})

if __name__ == '__main__':
    main()
