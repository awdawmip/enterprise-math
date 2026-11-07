#!/usr/bin/env python3
"""Exact finite checks: S23/AV observer-adaptive count-strip decoder.
All-real asymptotic limit is a separate analytic proof in PROOF.md.
"""
from fractions import Fraction as F
from math import sqrt, log, ceil, comb
from itertools import product

ZMIN, ZMAX = F(1,16), F(7,16)
LEGAL = [(F(1,2),F(1,2)), (F(1,2),F(7,8)),
         (F(7,8),F(1,2)), (F(7,8),F(7,8)),
         (F(5,7),F(7,8)), (F(3,5),F(5,7))]


def fiber(z):
    umin=max(F(1,8), F(8,7)*z)
    umax=min(F(1,2), 2*z)
    return (1-umax)/(1-z), (1-umin)/(1-z)


def strip(n,r):
    assert 0 <= r <= n
    zhat=min(ZMAX,max(ZMIN,F(r,n)))
    low, high = fiber(zhat)
    m=n-r
    W=ceil(4*sqrt(n*log(n+2)))+1
    A=max(0,(m*low).numerator//(m*low).denominator-W)
    D=min(m,-(-(m*high).numerator//(m*high).denominator)+W)
    assert 0<=A<=D<=m
    return A,D


def pmf(n,k,p):
    return F(comb(n,k))*p**k*(1-p)**(n-k)


def full_overlap(n,a,c):
    z=(1-a)*c; b=1-a-z
    total_target=total_decoded=overlap=F()
    for word in product((1,3,4),repeat=n):
        r=word.count(3);m=n-r;k=word.count(1)
        A,D=strip(n,r)
        target=a**k*z**r*b**(m-k)
        decoded=z**r*(1-z)**m/((D-A+1)*comb(m,k)) if A<=k<=D else F()
        total_target+=target;total_decoded+=decoded
        overlap+=min(target,decoded)
    assert total_target==total_decoded==1
    return overlap


def count_overlap(n,a,c):
    z=(1-a)*c;p=a/(1-z)
    out=F()
    for r in range(n+1):
        m=n-r;A,D=strip(n,r)
        v=sum((min(pmf(m,k,p),F(1,D-A+1)) for k in range(A,D+1)),F())
        out+=pmf(n,r,z)*v
    return out


def cfiber_square(z):
    if z==ZMIN or z==ZMAX:
        return None
    pp,pm=fiber(z)
    width=pm-pp
    return 4*pm*(1-pm)/((1-z)*width*width)


assert fiber(ZMIN)==(F(14,15),F(14,15))
assert fiber(ZMAX)==(F(8,9),F(8,9))
assert fiber(F(1,4))==(F(2,3),F(20,21))
assert cfiber_square(F(1,4))==F(80,27)
for i in range(1, 61):
    z=F(1,16)+F(3*i,8*61)
    low,high=fiber(z)
    assert low<=high
    assert cfiber_square(z)>=F(80,27)

for a,c in LEGAL:
    z=(1-a)*c; low,high=fiber(z);p=a/(1-z)
    assert low<=p<=high
    for n in (2,3,4,5):
        assert full_overlap(n,a,c)==count_overlap(n,a,c),(a,c,n)
    print(f'legal a={a} c={c} z={z} fiber=[{low},{high}] n5_overlap={float(count_overlap(5,a,c)):.12f}')

for n,z in ((1000,F(1,4)),(20000,F(1,4)),(20000,F(7,64))):
    r=n*z
    if r.denominator==1:
        A,D=strip(n,int(r))
        print(f'strip n={n} z={z}: range=[{A},{D}] length={D-A+1} full_length={n-int(r)+1}')

print('PASS_S23_AV_ADAPTIVE_OBSERVER_STRIP_UNIFORM_COEFFICIENT_EXACT_FINITE_20261107')
