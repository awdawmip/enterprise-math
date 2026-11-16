#!/usr/bin/env python3
"""Independent reconstruction from raw signed-BRC coefficients and Toeplitz determinants."""
from math import comb
from fractions import Fraction as F
from sympy import Matrix
def C(k):return comb(2*k,k)//(k+1)
def raw(k,t):
 r=2*k+1
 if not 2<=t<=r:return 0
 n=r-t
 def cf(deg):return sum(comb(2*t,deg-2*j)*comb(n,j) for j in range(n+1) if 0<=deg-2*j<=2*t)
 return comb(r+t,2*t)*(cf(r)-cf(r-1))
def ballot(k,t):
 r=2*k+1
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(k-q) for q in range(min((t-1)//2,k)+1))
k=10;r=2*k+1
for t in range(2,r+1):assert raw(k,t)==ballot(k,t),t
p={t:F(raw(k,t),C(k)) for t in range(2,r+1)}
A=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,2*k)]
f=[F(1)]
for m in range(1,25): f.append(sum(A[j-1]*f[m-j] for j in range(1,min(m,len(A))+1)))
checks=[1,2,3,4,5,6,8,10,12,16,20,24]
for m in checks:
 det=Matrix(m,m,lambda i,j:raw(k,3+i-j)).det(method='berkowitz')
 assert det==f[m]*C(k)**m,(m,'RAW_DET_MISMATCH')
 print(m,'+' if det>0 else '-' if det<0 else '0')
print('R547_INDEPENDENT_RAW_PASS','k',k,'raw_H_matches',r-1,'matrices',len(checks))
