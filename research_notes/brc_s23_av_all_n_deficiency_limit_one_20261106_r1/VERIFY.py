#!/usr/bin/env python3
"""Exact arithmetic certificate for an m-point same-observer packing in S23/AV.
All probabilities are rational; no external dependencies.
"""
from fractions import Fraction as F
from math import comb

z=F(1,4)
a=(F(1,2),F(17,28),F(5,7))
assert a[1]-a[0] == a[2]-a[1] == F(3,28)
for ai in a:
    c=z/(1-ai)
    assert F(1,2) <= ai <= F(7,8)
    assert F(1,2) <= c <= F(7,8)
    p=(ai,z,1-ai-z)
    assert sum(p)==1 and all(x>=0 for x in p)
    print('parameter',str(ai),'c=',str(c),'P=',','.join(map(str,p)))

def cumulative(n,p,k):
    # recurrence with exact rational values, at n=1000 manageable
    b=(1-p)**n
    s=b
    for j in range(k):
        b = b*F(n-j,j+1)*p/(1-p)
        s+=b
    return s

n=1000
# Strict Voronoi cells on first-stop count. No tie at these thresholds.
lo=(a[0]+a[1])/2
hi=(a[1]+a[2])/2
klo=(n*lo).numerator//(n*lo).denominator
khi=(n*hi).numerator//(n*hi).denominator
assert (lo,hi,klo,khi)==(F(31,56),F(37,56),553,660)
s0=cumulative(n,a[0],klo)
s1=cumulative(n,a[1],khi)-cumulative(n,a[1],klo)
s2=1-cumulative(n,a[2],khi)
for s in (s0,s1,s2): assert F(0)<=s<=1
bound=(s0+s1+s2-1)/3
assert bound > F(13,20)    # stronger finite-n 0.65 certificate
assert bound < F(2,3)
# For any parameter-independent kernel, Q=B(z)^n L is common to all 3 cases.
# Disjoint decision events imply max_i TV(P_i^n,Q) >= (sum P_i(E_i)-1)/3.
# Bound is stored exactly as 3 rational finite binomial sums and checked here.
print('n',n,'classifier_count_thresholds',klo,khi)
print('verified_n1000_lower_gt_13_20',bound > F(13,20))
print('n1000_exact_lower_decimal_18',f'{float(bound):.18f}')
print('verified_n1000_lower_gt_1_2',bound > F(1,2))

# Chebyshev all-n bound for all integers m>=2:
# delta_n >= 1 - 1/m - 196*(m-1)^2/(9*n).
def cheb(n,m):
    assert n>=1 and m>=2
    return 1-F(1,m)-F(196*(m-1)**2,9*n)
assert cheb(1000,3)==F(652,1125)
assert cheb(10000,10)==F(1809,2500) # 0.7236
print('cheb_n1000_m3',cheb(1000,3))
print('cheb_n10000_m10',cheb(10000,10))
print('PASS_S23_ALL_N_DEFICIENCY_LIMIT_ONE_EXACT_20261106')
