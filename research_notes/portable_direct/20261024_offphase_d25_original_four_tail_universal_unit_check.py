#!/usr/bin/env python3
"""Exact author regression for a proved p-free factorial/Wilson identity.

Scientific scope: only source-fixed original WZ tails at p=6m+1 >= 13,
and the distinct moving-rank FIVE second digit. Not a native CM experiment,
not independent review, and not a replacement for the algebraic proof.
No external dependencies and no network or mutations of project state.
"""
from fractions import Fraction as F
from math import factorial, gcd, isqrt


def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def modfrac(x, mod):
    assert isinstance(x, F) and gcd(x.denominator, mod) == 1, (x, mod)
    return x.numerator * pow(x.denominator, -1, mod) % mod


def source_V(r, n):
    # Genuine original WZ factorial kernel; no auxiliary Cauchy substitution.
    return F(
        factorial(6*r)*factorial(4*r+2*n)*factorial(3*n),
        3**(6*r)*216**n*factorial(2*r)*factorial(n)**2
        *factorial(2*r+n)**2*factorial(4*r+n),
    )


def source_U(p):
    # Exact prior old-rank unit identity from the authentic WZ source.
    m=(p-1)//6
    x=F(2*m, 108**(p-1))
    for k in range(2, 2*m+1):
        x*=F(k-p,k)**2
    for j in range(1,p-1):
        x*=F(j+p,j)**2
    for j in range(1,2*m):
        x/=F(j+p,j)
    return x


def original_C(p):
    return F(
        (p+1)*(2*p-1)**2*(30*p*p+77*p+40),
        2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5),
    )


TAU = (F(39,220), F(57,4928), F(1125,670208), F(22599,67020800))
SUM_TAU = F(752427,3942400)
EXAMPLES = {13:(10,0,148), 19:(2,6,45), 31:(1,25,166),
            109:(56,0,255), 211:(141,25,41427)}


def run():
    primes = [p for p in range(13,300) if p%6 == 1 and prime(p)]
    assert len(primes) == 27
    for p in primes:
        m=(p-1)//6
        normalized = source_V(m+1,4*m+1)/p**2
        sigma=modfrac(normalized,p)
        assert sigma != 0 and sigma == modfrac(F(3,220),p),p
        tails=[]
        for j in range(1,5):
            n=4*m+j
            tail = (6*n+12*(m+1)+1)*source_V(m+1,n)/p**2
            assert modfrac(tail,p) == modfrac(TAU[j-1],p),(p,j)
            tails.append(tail)
        tail_sum=modfrac(sum(tails),p)
        assert tail_sum == modfrac(SUM_TAU,p),p
        if p in (13,109):
            assert tail_sum == 0
        else:
            assert tail_sum != 0
        original_five_normalized = source_U(p)*original_C(p) + p*sum(tails)
        q2=(2**(p-1)-1)//p
        q3=(3**(p-1)-1)//p
        predicted=F(2,3)+p*(q3-F(4,3)*q2-F(233173,3942400))
        exact = modfrac(original_five_normalized,p*p)
        assert exact == modfrac(predicted,p*p),p
        if p in EXAMPLES:
            assert (sigma,tail_sum,exact)==EXAMPLES[p],p
    print({"scope":"source-fixed original WZ", "primes":len(primes),
           "range":"13<=p<300, p=1 mod6", "failures":[],
           "checked":["original factorial sigma", "four separately labeled tails",
                      "additive four-tail readout", "original old-edge + FIVE mod p^2"]})


if __name__ == '__main__':
    run()
