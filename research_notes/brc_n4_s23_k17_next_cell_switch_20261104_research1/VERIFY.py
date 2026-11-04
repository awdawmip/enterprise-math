#!/usr/bin/env python3
"""Exact Fraction / isqrt interval certificate for BRC S23 K=17 phase extension.
No floating point, external packages, or numerical optimizers.
"""
from fractions import Fraction as F
from math import isqrt

N=34  # atanh log terms; logs' arguments confined to a small vicinity of 1
S=10**48

def I(x):
    if isinstance(x, tuple): return x
    v=F(x); return (v,v)

def add(a,b):
    a=I(a); b=I(b);return (a[0]+b[0],a[1]+b[1])
def neg(a):
    a=I(a);return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    a=I(a);b=I(b);v=[x*y for x in a for y in b];return min(v),max(v)
def div(a,b):
    b=I(b);assert 0<b[0];return mul(a,(1/b[1],1/b[0]))
def sqrti(x):
    x=F(x);assert x>0
    k=isqrt((x.numerator*S*S)//x.denominator)
    lo=F(k,S);hi=F(k+1,S)
    assert lo**2<=x<hi**2
    return (lo,hi)
def log_rational(x):
    x=F(x);assert 0<x
    y=(x-1)/(x+1); assert abs(y)<F(1,3),('log argument out of efficient range',str(x))
    t=y; partial=F(0)
    for k in range(N):
        partial+=2*t/F(2*k+1)
        t*=y*y
    bound=2*abs(t)/(F(2*N+1)*(1-y*y))
    return (partial-bound,partial+bound)
def logi(a):
    a=I(a);assert a[0]>0
    return (log_rational(a[0])[0],log_rational(a[1])[1])

a=F(11,21);b=F(10,21)
def info(s):
    s=F(s)
    u=mul(s,sqrti(a*b))
    qt=add(1-s,mul(2,u))
    qb=add(u,sqrti((1-a*s)*(1-b*s)))
    ct=neg(logi(qt));fh=neg(logi(qb))
    h=logi(a/b)
    ell=logi(F(1-b*s,1-a*s))
    r=div(ell,add(h,ell))
    cb=add(mul(r,logi(div(r,a*s))),mul(sub(1,r),logi(div(sub(1,r),1-a*s))))
    return ct,fh,cb,qt,qb

# s=1/8 and s=1/8+1/100000: 8T+2B strictly beats pure B.
for s in (F(1,8),F(1,8)+F(1,100000)):
    ct,fh,cb,qt,qb=info(s)
    left=sub(add(mul(8,ct),mul(2,fh)),mul(17,cb))
    assert left[0]>0
    print('mixed_wins_at',str(s),'gap_lower_gt',str((left[0]*10**15).numerator//(left[0]*10**15).denominator)+'/10^15')
# s=1/8+3/100000: pure B strictly beats 8T+2B by the separated-information upper bound.
s=F(1,8)+F(3,100000)
ct,fh,cb,qt,qb=info(s)
right=sub(mul(15,cb),mul(8,ct))
assert right[0]>0
print('pure_B_wins_at',str(s),'gap_lower_gt',str((right[0]*10**15).numerator//(right[0]*10**15).denominator)+'/10^15')
# s=13/100: independent simple radical-only certificate for pure B dominance.
ct2,fh2,cb2,qt2,qb2=info(F(13,100))
right2=sub(mul(15,fh2),mul(8,ct2))
assert right2[0]>0
qt8=I(1);qb15=I(1)
for _ in range(8): qt8=mul(qt8,qt2)
for _ in range(15): qb15=mul(qb15,qb2)
radical=sub(qt8,qb15)
assert radical[0]>0
print('radical_independent_certificate_13_100_lower_gt',str((radical[0]*10**15).numerator//(radical[0]*10**15).denominator)+'/10^15')
print('PASS_S23_K17_RESIDUE_REDUCTION_SWITCH_EXISTENCE_RATIONAL_CERT_20261104')
print('Checked: 4 rational s endpoints; 34-term rigorous atanh log remainders; sqrt interval 10^-48 grid. Reduction lemma in PROOF.md is analytic.')
