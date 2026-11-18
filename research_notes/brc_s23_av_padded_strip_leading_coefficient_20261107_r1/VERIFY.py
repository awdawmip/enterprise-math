#!/usr/bin/env python3
"""Author checks for universal parameter-range padded count-strip S23 decoder.

Exact finite tests check full ordered-output and count-overlap identities.
The asymptotic uniformity proof is in PROOF.md, not inferred from finite tests.
"""
from fractions import Fraction
from itertools import product
from math import ceil, comb, floor, log, sqrt

ALPHA = Fraction(2, 3)
BETA = Fraction(56, 57)
WIDTH = BETA-ALPHA
LEGAL = [(Fraction(1, 2), Fraction(1, 2)),
         (Fraction(1, 2), Fraction(7, 8)),
         (Fraction(7, 8), Fraction(1, 2)),
         (Fraction(7, 8), Fraction(7, 8)),
         (Fraction(3, 5), Fraction(5, 7))]


def strip(m):
    # Overpadding is deliberate: it includes all moderate-deviation windows.
    w = ceil(sqrt(m*log(m+2)))+1
    lo = max(0, (ALPHA.numerator*m)//ALPHA.denominator-w)
    hi = min(m, -((-BETA.numerator*m)//BETA.denominator)+w)
    assert 0 <= lo <= hi <= m
    return lo, hi


def pmf(n,k,p):
    return Fraction(comb(n,k))*p**k*(1-p)**(n-k)


def conditional_overlap(m,p):
    lo,hi=strip(m)
    uniform=Fraction(1,hi-lo+1)
    return sum((min(pmf(m,k,p),uniform) for k in range(lo,hi+1)),Fraction())


def count_overlap(n,z,p):
    return sum((pmf(n,m,1-z)*conditional_overlap(m,p)
                for m in range(n+1)),Fraction())


def full_word_overlap(n,a,c):
    z=(1-a)*c; b=1-a-z
    overlap=Fraction(); decoded_total=Fraction(); true_total=Fraction()
    for word in product((1,3,4), repeat=n):
        r=word.count(3); m=n-r; k=word.count(1)
        lo,hi=strip(m)
        true=a**k*z**r*b**(m-k)
        decoded=(z**r*(1-z)**m / ((hi-lo+1)*comb(m,k))) if lo<=k<=hi else Fraction()
        overlap+=min(true,decoded)
        true_total+=true
        decoded_total+=decoded
    assert true_total==decoded_total==1
    return overlap


def leading_square(a,c):
    z=(1-a)*c; b=(1-a)*(1-c); s=1-z
    return Fraction(4)*a*b/(s**3*WIDTH**2)


assert WIDTH==Fraction(6,19)
assert leading_square(Fraction(7,8),Fraction(7,8))==Fraction(4)*Fraction(3584,185193)/WIDTH**2
assert Fraction(0)<leading_square(Fraction(7,8),Fraction(7,8))
print('p_range',ALPHA,BETA,'width',WIDTH)
for a,c in LEGAL:
    z=(1-a)*c; p=a/(1-z)
    assert ALPHA<=p<=BETA
    for n in (2,3,4,5):
        assert count_overlap(n,z,p)==full_word_overlap(n,a,c),(a,c,n)
    print(f'parameter a={a} c={c}: leading C={sqrt(float(leading_square(a,c))):.12f}, exact n=5 overlap={float(count_overlap(5,z,p)):.12f}')

for ai in range(8,15):
    for ci in range(8,15):
        a=Fraction(ai,16);c=Fraction(ci,16)
        assert leading_square(a,c)>=leading_square(Fraction(7,8),Fraction(7,8))

# Exact finite-n objective values; these are tests and useful benchmark measurements.
a=c=Fraction(7,8)
z=(1-a)*c; p=a/(1-z)
for n in (8,16,32,64):
    overlap=count_overlap(n,z,p)
    old=sum((pmf(n,m,1-z)*sum((min(pmf(m,k,p),Fraction(1,m+1)) for k in range(m+1)),Fraction()) for m in range(n+1)),Fraction())
    print(f'corner n={n} strip_overlap={float(overlap):.12f} old_uniform_overlap={float(old):.12f}')

print('PASS_S23_AV_PADDED_COUNT_STRIP_UNIFORM_ASYMPTOTIC_EXACT_FINITE_20261107')
