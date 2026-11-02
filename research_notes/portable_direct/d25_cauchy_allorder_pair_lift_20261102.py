#!/usr/bin/env python3
"""Exact p^3 Cauchy carry lift, preserving ordered (m,s) source.

The source a_m(1/2)^m u_s is compared with terminating binomial T_m v_s
and a 3-band product whose first s half-parameter factors cancel exactly.
All modular checks use integer arithmetic; no floating point.
No mathematical admission, C1 proof, or native H0/B0 execution is claimed.
"""
from math import isqrt


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * ((n-i*i)//i + 1)
    return [p for p in range(7, n+1) if sieve[p] and p % 6 == 1]


def check(p, verify_pairs=False):
    assert p >= 7 and p % 6 == 1
    r = (p-1) // 6
    M = p**3
    inv = [0] + [pow(n, -1, M) for n in range(1, 4*r+1)]
    i2, i3, i4, i9, i36 = (pow(n, -1, M) for n in (2,3,4,9,36))
    c = b = t = v = 1  # c=a_m*2^{-m}; b=(1/2)_m/(2^m*m!); t=T_m
    U = V = E = F = G = 0
    alpha = sigma2 = beta = tau2 = 0
    H = Hbin = Hharm = Hquad = 0
    P1 = P2 = P3 = 1  # half, one-third, two-thirds deformation products
    factors = [1]
    c_list = [1]
    u_list = [0]
    t_list = [1]
    v_list = [0]
    first_prefix = [1]
    other_prefix = [1]
    joint_pointwise = 0
    for m in range(1, 2*r + 1):
        x3,x2,x4 = inv[3*r-m+1], inv[2*r-m+1], inv[4*r-m+1]
        # Original independent hypergeometric recurrence and reflection source.
        c = c * (2*m-1)*(3*m-2)*(3*m-1)*i36*pow(inv[m],3,M) % M
        b = b * (2*m-1)*i4*inv[m] % M
        u = -pow(4*m*b % M,-1,M) % M
        U = (U + u) % M
        H = (H + (6*m+1)*c*U) % M
        # Terminating binomial source, using independent recurrences.
        t = -t*(3*r-m+1)*(2*r-m+1)*(4*r-m+1)*i2*pow(inv[m],3,M) % M
        if m == 1:
            v = pow(6*r,-1,M)
        else:
            v = -v*2*(m-1)*inv[3*r-m+1] % M
        V = (V + v) % M
        # Exact first-band cancellation at s<=m, plus un-cancelled two bands.
        f1 = (1-p*i2*x3) % M
        f2 = (1-p*i3*x2) % M
        f3 = (1-2*p*i3*x4) % M
        P1=P1*f1 % M
        P2=P2*f2 % M
        P3=P3*f3 % M
        assert c == t*P1*P2*P3 % M, ('a source',p,m)
        assert u == v*pow(P1,-1,M) % M, ('reflection source',p,m)
        # First and squared power sums of the three factor families.
        beta = (beta + i2*x3) % M
        tau2 = (tau2 + i4*x3*x3) % M
        alpha = (alpha + i2*x3 + i3*x2 + 2*i3*x4) % M
        sigma2 = (sigma2 + i4*x3*x3 + i9*x2*x2 + 4*i9*x4*x4) % M
        E = (E + v*beta) % M
        F = (F + v*beta*beta) % M
        G = (G + v*tau2) % M
        obs = (6*m+1)*t % M
        Hbin = (Hbin + obs*V) % M
        Hharm = (Hharm + obs*(E-alpha*V)) % M
        quadratic = ((alpha*alpha-sigma2)*V - 2*alpha*E + F + G)*i2 % M
        Hquad = (Hquad + obs*quadratic) % M
        # Strong pointwise p^3 test of the proposed moment closure.
        predicted = t*(V + p*(E-alpha*V) + p*p*quadratic) % M
        assert c*U % M == predicted, ('pointwise moment lift',p,m)
        if verify_pairs:
            c_list.append(c)
            u_list.append(u)
            t_list.append(t)
            v_list.append(v)
            first_prefix.append(P1)
            other_prefix.append(P2*P3 % M)
    assert H == (Hbin + p*Hharm + p*p*Hquad)%M, ('full p^3 lift',p)
    if verify_pairs:
        for m in range(1,2*r+1):
            for s in range(1,m+1):
                pair = t_list[m]*v_list[s]*first_prefix[m]*pow(first_prefix[s],-1,M)*other_prefix[m] % M
                assert pair == c_list[m]*u_list[s]%M, ('ordered-pair exact carrier',p,m,s)
                joint_pointwise += 1
    char2=1 if p%8 in (1,7) else -1
    C1=3*(char2-1)
    second=((H-C1)%M//p)%p if (H-C1)%p==0 else None
    third=(((H-C1-p*second)%M)//(p*p))%p if second is not None else None
    return dict(p=p,r=r,character2=char2,H_mod_p3=H,Hbin_mod_p3=Hbin,
                harmonic_mod_p2=Hharm%(p*p),quadratic_mod_p=Hquad%p,
                C1_residue=(H-C1)%p,second_digit=second,third_digit=third,
                ordered_pairs_checked=joint_pointwise)


if __name__ == '__main__':
    import sys
    bound=int(sys.argv[1]) if len(sys.argv)>1 else 3000
    ps=primes_upto(bound)
    samples=[];good=0;pairs=0
    for p in ps:
        q=check(p, verify_pairs=p in (7,13,19,31,37,43,373))
        good+=q['C1_residue']==0
        pairs+=q['ordered_pairs_checked']
        if p in (7,13,19,31,37,43,373,1171): samples.append(q)
    print('P3_PAIR_LIFT_AND_MOMENT_CLOSURE PASS %s/%s p=1(mod6), 7<=p<=%s'%(len(ps),len(ps),bound))
    print('INDEPENDENT_ORDERED_PAIRS PASS',pairs)
    print('C1_FINITE_CHECK_NOT_PROOF',good,'/',len(ps))
    for s in samples: print(s)
