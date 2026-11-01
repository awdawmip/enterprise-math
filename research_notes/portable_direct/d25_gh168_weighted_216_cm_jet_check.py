#!/usr/bin/env python3
"""Exact source-indexed p-adic weighted-216 jet at X=1, p≡13,19 mod24.
Checks independent recurrences in Z/p^3Z and global mod-p Clausen coefficients.
No native H0/B0 divided-power or Source admission is attempted.
"""
from math import isqrt


def targets(limit):
    for p in range(13, limit):
        if p % 24 not in (13, 19):
            continue
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def original_two_f_one(p):
    """Return low p-reduced coefficients of _2F1(1/6,1/3;1;X/2)."""
    m=(p-1)//6
    coeff=[1]
    for n in range(m):
        b=coeff[-1]*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,p)%p
        coeff.append(b)
    return coeff


def original_weighted_three_f_two(p, u=1):
    """Independent original 216 binomial hypergeometric coefficient recurrence, mod p^3."""
    mod=p**3
    c=1
    A=0
    A_prime=0
    A_second=0
    x=1+p*p*u
    power=1
    for n in range(p):
        A=(A+(6*n+1)*c*power)%mod
        A_prime=(A_prime+n*(6*n+1)*c)%p
        A_second=(A_second+n*(n-1)*(6*n+1)*c)%p
        if n<p-1:
            c=c*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod)%mod
            power=power*x%mod
    return A,A_prime,A_second


def check_prime(p, verify_full_coeffs):
    m=(p-1)//6
    coeff=original_two_f_one(p)
    cm=sum(coeff)%p
    h=sum((12*i+1)*v for i,v in enumerate(coeff))%p
    slope=h*h*pow(12,-1,p)%p
    assert cm==0,(p,'CM0',cm)
    assert h,(p,'unit h',h)
    original, direct_slope, direct_curvature=original_weighted_three_f_two(p, 0)
    perturbed,_,_=original_weighted_three_f_two(p, 1)
    assert (original-p)%(p*p)==0,(p,'first digit',original)
    assert direct_slope==slope,(p,'weighted original jet',direct_slope,slope)
    assert direct_curvature==h*h*pow(18,-1,p)%p,(p,'weighted curvature',direct_curvature)
    assert 3*direct_curvature%p==2*direct_slope%p,(p,'universal curvature ratio')
    assert (perturbed-original)%(p**3)==p*p*slope,(p,'jet response',perturbed,original,slope)
    if verify_full_coeffs:
        # Exact coefficientwise Clausen at X=any; do not infer from sampled values.
        # The truncated product f^2+12X f f' must agree with full weighted 216 sequence mod p.
        prod=[0]*(2*m+1)
        tangent=[0]*(2*m+1)
        for i,bi in enumerate(coeff):
            for j,bj in enumerate(coeff):
                prod[i+j]=(prod[i+j]+bi*bj)%p
                tangent[i+j]=(tangent[i+j]+12*j*bi*bj)%p
        weighted_mod=[0]*p
        a=1
        for n in range(p):
            weighted_mod[n]=(6*n+1)*a%p
            if n<p-1:
                a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,p)%p
        for n in range(p):
            expected=(prod[n]+tangent[n])%p if n<=2*m else 0
            assert expected==weighted_mod[n], (p,'coefficientwise Clausen',n,expected,weighted_mod[n])
    return {'p':p,'m':m,'h_mod_p':h,'jet_slope':slope,
            'A_1_mod_p3':original,'A_1_plus_p2_mod_p3':perturbed,
            'curvature':direct_curvature,
            'delta_at_1':((original-p)%(p**3))//(p*p),
            'delta_at_1_plus_p2':((perturbed-p)%(p**3))//(p*p),
            'coefficientwise':verify_full_coeffs}


if __name__=='__main__':
    checked=[]
    checked_full=0
    for p in targets(5000):
        chk=check_prime(p,verify_full_coeffs=p<=283)
        checked.append(chk)
        checked_full+=bool(chk['coefficientwise'])
        if p in (13,19,37,157,373):
            print(chk)
    assert len(checked)==166
    print('checked_target_primes',len(checked),'checked_all_CLAUSEN_coefficients_at_primes',checked_full)
    print('nonzero_weighted_jets',sum(r['jet_slope']!=0 for r in checked))
    print('PASS_GH168_ORIGINAL_WEIGHTED_216_CM_JET_TRANSVERSALITY_EXACT')
