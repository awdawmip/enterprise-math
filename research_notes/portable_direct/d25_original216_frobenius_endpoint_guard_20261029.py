#!/usr/bin/env python3
"""Exact integer guard for original A216 3F2. NOT native H0/B0."""
from math import comb, isqrt
def primes_below(limit):
    return [p for p in range(5,limit) if all(p%d for d in range(2,isqrt(p)+1))]
def original_coeff_mod(n,p,k=4):
    mod=p**k
    return comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod)%mod
def endpoint_by_recurrence(p):
    mod=p**4; a=1
    for n in range(p-1):
        a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod)%mod
    assert a%(p**3)==0
    return a
def binom_modp_lucas(n,k,p):
    z=1
    while n or k:
        a,b=n%p,k%p
        if b>a: return 0
        z=z*comb(a,b)%p
        n//=p; k//=p
    return z
def direct_A_modp(n,p):
    return original_coeff_mod(n,p,k=1)
def lucas_A_modp(n,p):
    return binom_modp_lucas(2*n,n,p)**2*binom_modp_lucas(3*n,n,p)*pow(216,-n,p)%p
def base_p_digit_sum(n,p):
    s=0
    while n:
        s+=n%p; n//=p
    return s
def valuation_by_digits(n,p):
    return (5*base_p_digit_sum(n,p)-base_p_digit_sum(2*n,p)-base_p_digit_sum(3*n,p))//(p-1)
def int_p_valuation(n,p):
    if not n: return None
    k=0
    while n%p==0:
        k+=1; n//=p
    return k
def support_by_digits(n,p):
    bound=(p-1)//3
    while n:
        if n%p>bound: return False
        n//=p
    return True
def main():
    ps=primes_below(1200)
    for p in ps:
        mod=p**4; a=endpoint_by_recurrence(p)
        assert a//p**3==p-1,(p,a)
        assert original_coeff_mod(p-1,p)==a
        assert original_coeff_mod(p,p,k=1)==pow(18,-1,p)
        c=(2*p-1)*(3*p-2)*(3*p-1)*pow(36,-1,mod)%mod
        boundary=-c*a%mod
        assert boundary==(-p**3*pow(18,-1,mod))%mod
    exhaust=(5,7,11,13,19); block_count=0
    for p in exhaust:
        for N in range(p*p):
            v=direct_A_modp(N,p)
            assert v==lucas_A_modp(N,p)
            assert bool(v)==support_by_digits(N,p)
            block_count+=1
    pair_count=0
    for p in (5,7,11,13,17,19,23,31,43):
        for u in range(7):
            for r in range(p):
                assert direct_A_modp(p*u+r,p)==direct_A_modp(u,p)*direct_A_modp(r,p)%p
                pair_count+=1
    valuation_count=0
    for p in (5,7,11,13,17,19,23,29,31,37,43):
        for n in range(1,201):
            c=comb(2*n,n)**2*comb(3*n,n)
            assert valuation_by_digits(n,p)==int_p_valuation(c,p)
            valuation_count+=1
    p=373; a=endpoint_by_recurrence(p); mod=p**4
    c=(2*p-1)*(3*p-2)*(3*p-1)*pow(36,-1,mod)%mod
    bound=-c*a%mod
    assert bound==(-p**3*pow(18,-1,mod))%mod
    print('PASS_ORIGINAL_A216_SHARP_PF_ENDPOINT primes_5_le_p_lt_1200',len(ps))
    print('PASS_DIRECT_INTEGER_LUCAS_SUPPORT_P2_BLOCKS',block_count,'p=',exhaust)
    print('PASS_DIRECT_INTEGER_LUCAS_PAIR_LAW',pair_count,'cases')
    print('PASS_KUMMER_DIGIT_SUM_VALUATION',valuation_count,'cases')
    print('P373',{'p2':p**2,'p3':p**3,'p4':p**4,'a_pminus1_modp4':a,
          'a_pminus1_overp3_modp':a//p**3,'a_p_modp':direct_A_modp(p,p),
          'PF_boundary_coeff_modp4':bound,'nonzero_modp4':bound!=0,
          'support_digits_below_p':(p-1)//3+1,
          'support_digits_below_p2':((p-1)//3+1)**2,
          'valuation_n_pminus1_p_pplus1':[(n,valuation_by_digits(n,p)) for n in (p-1,p,p+1)]})
if __name__=='__main__': main()
