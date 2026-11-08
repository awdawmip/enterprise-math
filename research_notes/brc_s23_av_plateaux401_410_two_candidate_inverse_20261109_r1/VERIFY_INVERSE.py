#!/usr/bin/env python3
"""Exact two-candidate index lookup for the S23/AV candidate staircase."""
from fractions import Fraction as F
from random import Random
Q=10**26
LO=545569623581288298975349314
HI=LO+1
Elo=79*LO-431*Q
Ehi=79*HI-431*Q
Dlo=2074774*Q-380295*HI
Dhi=2074774*Q-380295*LO
assert 0<Dlo<Dhi<Elo<Ehi
alpha_lo=F(Dlo,Ehi);alpha_hi=F(Dhi,Elo)
gamma_lo=380295+79*alpha_lo
gamma_hi=380295+79*alpha_hi

def ceil_frac(x):return -(-x.numerator//x.denominator)
def a(i):
    v=(i*alpha_lo).__floor__()
    assert v==(i*alpha_hi).__floor__(), ('alpha_floor_needs_refinement',i)
    return v
def H(i):return 380295*i+79*a(i)+510
def lookup(h):
    assert h>=511
    x=h-510
    kl=ceil_frac(F(x,1)/gamma_hi)
    ku=ceil_frac(F(x,1)/gamma_lo)
    assert kl==ku, ('gamma_inverse_needs_refinement',h,kl,ku)
    return kl if h<=H(kl) else kl+1

assert H(400)==152136996 and H(410)==155940420
for i in range(1,412):
    assert (i*gamma_lo).__floor__()==(i*gamma_hi).__floor__(),i
for h in range(511,10511):
    k=lookup(h)
    assert (k==1 or H(k-1)<h) and h<=H(k), (h,k)
for i in range(1,411):
    for h in [max(511,H(i-1)+1) if i>1 else 511,H(i)-1,H(i),H(i)+1]:
        if h>=511:
            k=lookup(h)
            assert (k==1 or H(k-1)<h) and h<=H(k),(i,h,k)
rng=Random(20261109)
for _ in range(2000):
    h=rng.randint(511,H(410))
    k=lookup(h)
    assert (k==1 or H(k-1)<h) and h<=H(k), (h,k)
print('PASS_TWO_CANDIDATE_INVERSE_10000_SMALL_1640_BOUNDARY_2000_RANDOM')
print('PASS_UNIFORM_GAMMA_FLOORS_1_TO_411')
print('H_400',H(400),'H_410',H(410),'example_at_155940420',lookup(H(410)))
count=0
for i in range(1,411):
    for h in [H(i)-1,H(i),H(i)+1]:
        if h<511:continue
        k=ceil_frac(F(h-510,1)/gamma_hi)
        if lookup(h)==k+1:
            print('NONTRIVIAL_SECOND_CANDIDATE',h,'naive_k',k,'correct_i',k+1)
            count+=1;break
    if count>=3:break
assert count>=1
