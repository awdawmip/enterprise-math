#!/usr/bin/env python3
"""Original-216 minimal order and source-preserving exact recurrence checker."""
from fractions import Fraction
from math import comb

def b(n):
    return Fraction(comb(2*n,n)**2*comb(3*n,n), 216**n)
def rho(n):
    return Fraction((2*n+1)*(3*n+1)*(3*n+2),36*(n+1)**3)
def exact_test():
    B=[b(k) for k in range(32)]
    S=[]
    s=Fraction(0)
    for k in range(32):
        s+=(6*k+1)*B[k]
        S.append(s)
    for k in range(31):
        assert B[k+1]==rho(k)*B[k]
        old=S[k-1] if k else Fraction(0)
        assert 36*(k+1)**3*(6*k+1)*(S[k+1]-S[k]) == \
            (6*k+7)*(2*k+1)*(3*k+1)*(3*k+2)*(S[k]-old)
        R=lambda j:4-12*j
        rem=Fraction(66*k*k+113*k+49,9*(k+1)**3)*B[k]
        assert (6*k+1)*B[k]==R(k+1)*B[k+1]-R(k)*B[k]+rem
    A,C=-12,4
    assert -18*A-216==0 and -63*A-18*C-684==0
    assert -68*A-81*C-756 == -264
    return len(S)-1
def prime_mod(p):
    mod=p**3
    coefficient=1
    total=0
    for k in range(p):
        total=(total+(6*k+1)*coefficient)%mod
        if k<p-1:
            num=(2*k+1)*(3*k+1)*(3*k+2)
            den=36*(k+1)**3
            coefficient=coefficient*num*pow(den,-1,mod)%mod
    direct=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*
               pow(216,-k,mod) for k in range(p))%mod
    assert total==direct
    return total
if __name__=="__main__":
    import json
    count=exact_test()
    values={str(p):prime_mod(p) for p in [13,19,37,43,373]}
    print(json.dumps(dict(schema="D25_ORIGINAL_216_MINIMAL_ORDER_CHECK_V1",
         exact_rational_steps=count, affine_obstruction_k2=-264,
         original_W_mod_p3=values,native_H0_B0_executed=False,
         status="AUTHOR_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED"),sort_keys=True,indent=2))
