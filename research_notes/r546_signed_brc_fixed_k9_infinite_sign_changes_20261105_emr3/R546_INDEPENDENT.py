#!/usr/bin/env python3
"""Independent frozen raw-H coefficients and original Toeplitz determinants, k=9."""
from math import comb
from fractions import Fraction as Q
from sympy import Matrix
def C(k):return comb(2*k,k)//(k+1)
def raw(k,t):
 r=2*k+1
 if not 2<=t<=r:return 0
 n=r-t
 def cx(deg):
  return sum(comb(2*t,deg-2*j)*comb(n,j) for j in range(n+1) if 0<=deg-2*j<=2*t)
 return comb(r+t,2*t)*(cx(r)-cx(r-1))
def ballot(k,t):
 r=2*k+1
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(k-q) for q in range(min((t-1)//2,k)+1))
k=9;r=2*k+1
p={t:Q(raw(k,t),C(k)) for t in range(2,r+1)}
for t in range(2,r+1):assert raw(k,t)==ballot(k,t),t
A=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,2*k)]
F=[Q(1)]
for m in range(1,25):
 F.append(sum(A[j-1]*F[m-j] for j in range(1,min(m,len(A))+1)))
checks=[1,2,3,4,5,6,8,10,12,16,20,24]
for m in checks:
 det=Matrix(m,m,lambda i,j:raw(k,3+i-j)).det(method='berkowitz')
 assert det==F[m]*C(k)**m,(m,'mismatch')
 assert det!=0,m
 print('m',m,'sign','+' if det>0 else '-')
print('R546_INDEPENDENT_RAW_PASS','k',k,'H/B',r-1,'raw_matrices',len(checks))
