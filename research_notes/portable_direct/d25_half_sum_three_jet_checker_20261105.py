#!/usr/bin/env python3
"""Independent integer verification of exact three-jet decomposition of original 216 half-sum.
No floating point and no external dependencies. Target primes p=6n+1.
"""
from math import comb, isqrt
import json


def primes(limit):
    for x in range(7, limit + 1):
        if x % 6 != 1:
            continue
        if all(x % d for d in range(2, isqrt(x) + 1)):
            yield x


def normalized_jet(p):
    assert p > 3 and p % 6 == 1
    n = (p - 1) // 6
    N, K, Q = 3*n, 2*n, 4*n
    m = p**3
    inv = lambda z: pow(z % m, -1, m)
    def term_u(j):
        # The three p-adic shifts from exact -N, -K, -Q base parameters.
        u0 = inv(2*(j-N))
        u1 = inv(3*(j-K))
        u2 = 2*inv(3*(j-Q))
        return (u0+u1+u2)%m, (u0*u0+u1*u1+u2*u2)%m

    b, l, qsum = 1, 0, 0
    s0, s1, s2 = 0, 0, 0
    # 0<=k<=K: p-adic unit branch, all three base Pochhammer factors nonzero.
    for k in range(K+1):
        w = 6*k+1
        s0 = (s0 + w*b)%m
        s1 = (s1 + w*b*l)%m
        s2 = (s2 + w*b*(l*l-qsum)*inv(2))%m
        if k < K:
            uk, qk = term_u(k)
            l = (l+uk)%m
            qsum = (qsum+qk)%m
            b = b*(k-N)*(k-K)*(k-Q)*inv(2*(k+1)**3)%m

    # K<k<=N: the (-K+p/3)_k factor has precisely one p/3 factor.
    bstar = 1
    for j in range(K+1):
        bstar = bstar*(j-N)*(j-Q)*inv(2*(j+1)**3)%m
        if j < K:
            bstar = bstar*(j-K)%m
        else:
            bstar = bstar*inv(3)%m
    lstar = 0
    for j in range(K+1):
        lstar = (lstar + inv(2*(j-N)) + 2*inv(3*(j-Q)))%m
        if j!=K:
            lstar = (lstar+inv(3*(j-K)))%m
    for k in range(K+1, N+1):
        w=6*k+1
        s1 = (s1 + w*bstar)%m
        s2 = (s2 + w*bstar*lstar)%m
        if k < N:
            lstar = (lstar + inv(2*(k-N)) + inv(3*(k-K)) + 2*inv(3*(k-Q)))%m
            bstar = bstar*(k-N)*(k-Q)*(k-K)*inv(2*(k+1)**3)%m

    direct = sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m) for k in range(N+1))%m
    lift = (s0+p*s1+p*p*s2)%m
    assert lift == direct, (p,lift,direct)
    # also direct numerical shell p² T_A
    full = sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m) for k in range(p))%m
    assert (full-direct)% (p*p) == 0
    ta = ((full-direct)//(p*p))%p
    second_digit = ((direct-p)//(p*p))%p if (direct-p) % (p*p)==0 else None
    return {'p':p,'n':n,'S0_mod_p3':s0,'S1_mod_p2':s1%(p*p),'S2_mod_p':s2%p,'half_mod_p3':direct,'full_mod_p3':full,'T_A':ta,'half_second_digit':second_digit,'target_residual':(full-p)%m}

if __name__=='__main__':
    results=[normalized_jet(p) for p in primes(997)]
    assert len(results)==80
    assert all(r['target_residual']==0 for r in results), 'finite original full sum residue mismatch'
    assert all(r['half_second_digit'] is not None for r in results)
    points=[next(a for a in results if a['p']==p) for p in (7,13,19,139,373)]
    outcome={'schema':'D25_ORIGINAL_216_HALF_JET_CHECK_V1','date':'2026-11-05','domain':'all checked primes 7<=p<=997, p=1 mod6','count':len(results),'failures':0,'sample':points,'scope':'exact finite modular checks; algebraic finite expansion proved separately; native H0/B0 not performed'}
    output='d25_half_sum_three_jet_results_20261105.json'
    with open(output,'w') as f:json.dump(outcome,f,ensure_ascii=False,indent=2)
    print(json.dumps(outcome,ensure_ascii=False,indent=2))
