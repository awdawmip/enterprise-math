#!/usr/bin/env python3
"""Exact author-side research checker: optimal cubic Clausen cutoff.

For p == 1 mod 6, p >= 7, a_n=(1/2)_n(1/3)_n(2/3)_n/(2^n(n!)^3)
=binom(2n,n)^2*binom(3n,n)/216^n. No floating point.
Portable mathematical evidence only; not a Source-native experiment.
"""
from math import comb, isqrt


def prime_list(bound):
    a = bytearray(b'\x01') * bound
    if bound > 0: a[0] = 0
    if bound > 1: a[1] = 0
    for k in range(2, isqrt(bound - 1) + 1):
        if a[k]:
            a[k*k::k] = b'\x00' * (((bound-1-k*k)//k)+1)
    return [p for p in range(7, bound) if a[p] and p%6 == 1]


def ordinal_level(n, m):
    return 0 if n<=2*m else 1 if n<=3*m else 2 if n<=4*m else 3


def boundary_unit(p):
    m=(p-1)//6
    n0=4*m+1
    ff=1; rfact=1
    for j in range(1,n0+1):
        ff=ff*j%p
        if j==2*m+1: rfact=ff
    # Factorial unit from (2n)!/p and (3n)!/p² at n=(2p+1)/3.
    unit=(-2*rfact*pow(ff,-5,p)*pow(216,-n0,p))%p
    assert unit
    return n0,unit


def normalized_tail(p):
    """Compute first omitted scalar digit without mod p^4 arithmetic."""
    n0,c=boundary_unit(p)
    inv=[0]*p
    inv[1]=1
    for j in range(2,p):
        inv[j]=p - (p//j)*inv[p%j]%p
    inv36=pow(36,-1,p)
    q=0
    for n in range(n0,p):
        q=(q+(6*n+1)*c)%p
        if n < p-1:
            c=(c*(2*n+1)*(3*n+1)*(3*n+2)*inv36*pow(inv[n+1],3,p))%p
            assert c
    return q


def direct_recurrence(p):
    """Independent modular recurrence under p^4 and complete valuation check."""
    m=(p-1)//6
    n0,u=boundary_unit(p)
    mod=p**4
    a=[1]
    for n in range(p-1):
        num=(2*n+1)*(3*n+1)*(3*n+2)
        den=36*(n+1)**3
        a.append(a[-1]*num*pow(den,-1,mod)%mod)
    for n,x in enumerate(a):
        level=ordinal_level(n,m)
        assert x%p**level == 0 and x%p**(level+1) != 0, (p,n,level)
    assert a[n0]%p**4 == p**3*u
    # Coefficientwise exact L3 error: only X^(4m+1) survives.
    forcing=(-pow(n0,3,p)*u)%p
    assert forcing
    weighted=((6*n0+1)*u)%p
    assert (6*n0+1)%p == 3 and weighted
    full=sum((6*n+1)*x for n,x in enumerate(a))%mod
    short=sum((6*n+1)*x for n,x in enumerate(a[:n0]))%mod
    diff=(full-short)%mod
    assert diff%p**3 == 0
    q=(diff//p**3)%p
    assert q == normalized_tail(p)
    # Raw factorial/binomial independent anchor formula for discarded term.
    if p in (7,13,19,157,373,1327):
        raw=comb(2*n0,n0)**2*comb(3*n0,n0)*pow(216,-n0,mod)%mod
        assert raw == a[n0]
    return (p,m,n0,u,forcing,weighted,q,full%p**3)


def main():
    checked=[direct_recurrence(p) for p in prime_list(5000)]
    assert len(checked)==330
    assert len([r for r in checked if r[0]%24 in (13,19)])==166
    extended=prime_list(12000)
    assert len(extended)==711
    zeros=[p for p in extended if normalized_tail(p)==0]
    assert zeros == [1327], zeros
    rows={r[0]:r for r in checked}
    for anchor in (7,13,19,157,373,1327):
        print('ANCHOR p m N unit forcing_unit weighted_unit Q_p A_p_mod_p3',rows[anchor])
    print('SCOPED_P3_POLYNOMIAL_MINIMAL_DEGREE N=4m ALL_PRIMES_BY_PROOF')
    print('EXACT_P4_SCALAR_Q_ZERO_UNDER_12000',zeros)
    print('COUNTS mod_p4_direct',len(checked),'frozen_class',166,'fast_p4_scalar',len(extended))
    print('PASS_GH172_GH173_OPTIMAL_CLAUSEN_CUTOFF_SCALAR_CANCELLATION_EXACT')


if __name__=='__main__':
    main()
