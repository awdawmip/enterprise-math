#!/usr/bin/env python3
"""Independent direct frozen H coefficients and Toeplitz/Berkowitz validation, k=7 and 8."""
from math import comb
from fractions import Fraction as Q
from sympy import Matrix

def C(k): return comb(2*k,k)//(k+1)
def direct_h(k,t):
 r=2*k+1
 if not 2<=t<=r: return 0
 n=r-t
 def cx(deg):
  return sum(comb(2*t,deg-2*j)*comb(n,j) for j in range(n+1) if 0<=deg-2*j<=2*t)
 return comb(r+t,2*t)*(cx(r)-cx(r-1))
def ballot_h(k,t):
 r=2*k+1
 if not 2<=t<=r: return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*j)*4**j*C(k-j) for j in range(min((t-1)//2,k)+1))
for k in (7,8):
 r=2*k+1; p={t:Q(direct_h(k,t),C(k)) for t in range(2,r+1)}
 for t in range(2,r+1):assert direct_h(k,t)==ballot_h(k,t),('coeff',k,t)
 # unscaled X recurrence for D_m/C_k^m
 A=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,2*k)]
 F=[Q(1)]
 for m in range(1,25): F.append(sum(A[j-1]*F[m-j] for j in range(1,min(m,len(A))+1)))
 for m in [1,2,3,4,5,6,8,9,12,16,20,24]:
  det=Matrix(m,m,lambda i,j: direct_h(k,3+i-j)).det(method='berkowitz')
  assert det == F[m]*C(k)**m,('determinant',k,m)
  assert det!=0,('zero',k,m)
  print('k',k,'m',m,'sign','+' if det>0 else '-')
 print('R545_RAW_BERKOWITZ_PASS',k,'H_equals_ballot',r-1,'raw_determinants',12)
print('R545_INDEPENDENT_PASS')
