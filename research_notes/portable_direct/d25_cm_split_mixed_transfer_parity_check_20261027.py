#!/usr/bin/env python3
"""Exact external-model transfer discriminator for D25, author-only portable check.

This is NOT the original native H0/B0 experiment or a proof of LIFT.
"""
from math import comb


def mixed_sequence_coefficient(n):
    """A_n=108^n[z^n] 2F1(1/6,1/3;1;z)^3, direct triple convolution."""
    f = [1]
    for k in range(n):
        num = 6 * (6*k+1)*(3*k+1)*f[-1]
        den = (k+1)**2
        assert num % den == 0
        f.append(num//den)
    f2 = [sum(f[j]*f[m-j] for j in range(m+1)) for m in range(n+1)]
    return sum(f2[j]*f[n-j] for j in range(n+1))


def mixed_sequence_recurrence(n):
    """Independent exact order-two recurrence from OEIS A393983."""
    if n==0: return 1
    a,b = 1,18
    for k in range(n-1):
        numerator = (6*(36*k**4+198*k**3+424*k**2+417*k+158)*b
                     -324*(k+1)*(2*k+1)*(3*k+2)*(6*k+5)*a)
        denominator=(k+2)**4
        assert numerator % denominator == 0
        a,b = b,numerator//denominator
    return b


def original_weighted_w_binom(p):
    mod=p**4
    denom=pow(216,-1,mod)
    return sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(denom,k,mod)
               for k in range(p)) % mod


def original_weighted_w_recurrence(p):
    mod=p**4
    inv36=pow(36,-1,mod)
    q=1
    acc=0
    for k in range(p):
        acc=(acc+(6*k+1)*q)%mod
        if k+1<p:
            q=q*(2*k+1)*(3*k+1)*(3*k+2)*inv36*pow(k+1,-3,mod)%mod
    return acc


def legendre(a,p):
    r=pow(a%p,(p-1)//2,p)
    assert r in (1,p-1)
    return 1 if r==1 else -1


def check(p):
    assert p in (13,19,37,43,373) and p%24 in (13,19)
    assert legendre(-3,p)==1 and legendre(-6,p)==-1 and legendre(2,p)==-1
    mod=p**4
    a=mixed_sequence_coefficient(p)
    a2=mixed_sequence_recurrence(p)
    assert a==a2 and a%mod==18
    w=original_weighted_w_binom(p)
    w2=original_weighted_w_recurrence(p)
    assert w==w2 and w%p**3==p
    assert (w-p)%p**3==0
    k=((w-p)%mod)//p**3
    scaled=(p*a*pow(18,-1,mod))%mod
    assert scaled==p and (w-scaled)%mod==(k*p**3)%mod
    assert k!=0
    return p,legendre(-3,p),legendre(-6,p),a%mod,w,k,len(str(a))


def main():
    print("p chi(-3) chi(-6) A_p_mod_p4 W_p_mod_p4 fourth_digit_defect digits_A")
    for p in (13,19,37,43,373): print(*check(p))
    print("CHECKED_FINITE_ONLY; NATIVE_H0B0_NOT_EXECUTED; AUTHOR_SIDE_UNREVIEWED")


if __name__=='__main__': main()
