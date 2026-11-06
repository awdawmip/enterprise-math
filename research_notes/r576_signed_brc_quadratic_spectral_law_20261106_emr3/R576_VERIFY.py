#!/usr/bin/env python3
"""R576 independent rational all-order leading-moment recurrence.
The all-m, k->infinity theorem uses an algebraic/analytic proof;
this script verifies low-order exact coefficients, selected signs, and an exact coefficient upper bound.
"""
from fractions import Fraction
from math import factorial, comb

M=128
alpha={j:Fraction(24*8**j,factorial(2*j+4)) for j in range(1,M+1)}
L={}
for m in range(1,M+1):
    L[m]=-sum((-1)**j*alpha[j]*L[m-j] for j in range(1,m))-m*(-1)**m*alpha[m]
assert L[1] == Fraction(4,15)
assert L[14] == Fraction(753757553004522635264,613998964100175243164104559326171875)
assert L[16] == -Fraction(7125033312365462511026176,291941157455530823743452615345611572265625)
# Algebraic coefficients of F(z)=3(cos(sqrt(8z))-1+4z)/(8z^2)
for j in range(1,65):
    assert Fraction(3,8)*((-1)**(j+2)*8**(j+2))/factorial(2*j+4) == (-1)**j*alpha[j]
# Independent elementary coefficient bound for 2<=k, 1<=j<=2k-1.
def C(n): return comb(2*n,n)//(n+1)
def H(k,s):
    r=2*k+1
    return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*C(k-q)
                                  for q in range(min(k,(s-1)//2)+1))
for k in range(2,101):
    h=H(k,2)
    for j in range(1,2*k):
        a=Fraction(H(k,j+2),h)
        assert a <= 4*(75*k*k)**j
print('LC1',L[1])
print('LC14',L[14])
print('LC16',L[16])
print('LC18',L[18])
print('LC20',L[20])
print('NONZERO_LC_M_1_TO_128',sum(L[m]!=0 for m in range(1,M+1)))
print('SIGNS_1_TO_32',''.join('+' if L[m]>0 else '-' if L[m]<0 else '0' for m in range(1,33)))
print('FORMAL_COSINE_COEFFICIENTS_CHECKED j=1..64')
print('COEFFICIENT_UPPER_BOUND_EXACT_CHECK k=2..100 j=1..2k-1')
print('R576_ALL_ORDER_LC_LOG_EXPONENT_PASS')
