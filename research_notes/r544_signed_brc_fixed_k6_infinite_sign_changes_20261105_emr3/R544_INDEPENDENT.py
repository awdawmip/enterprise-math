#!/usr/bin/env python3
"""Independent direct original coefficient and raw Toeplitz determinant checks, k=6."""
from math import comb
from fractions import Fraction
from sympy import Matrix
def coef_direct(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 n=r-t
 def coefficient(degree):
  return sum(comb(2*t,degree-2*j)*comb(n,j)
             for j in range(n+1) if 0<=degree-2*j<=2*t)
 return comb(r+t,2*t)*(coefficient(r)-coefficient(r-1))
def cat(k):return comb(2*k,k)//(k+1)
def ballot(k,t):
 r=2*k+1
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*j)*4**j*cat(k-j)
              for j in range(min((t-1)//2,k)+1))
k=6;r=2*k+1;d=2*k-1;C=cat(k)
for t in range(2,r+1):
 assert coef_direct(k,t)==ballot(k,t),(t,coef_direct(k,t),ballot(k,t))
p={t:Fraction(coef_direct(k,t),C) for t in range(2,r+1)}
a=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,d+1)]
f=[Fraction(1)]
for m in range(1,24):
 f.append(sum(a[j-1]*f[m-j] for j in range(1,min(m,d)+1)))
orders=[1,2,3,4,5,6,7,8,10,12,13,16,20,23]
for m in orders:
 D=Matrix(m,m,lambda i,j:coef_direct(k,3+i-j)).det(method='berkowitz')
 expected=f[m]*C**m
 assert expected.denominator==1 and D==expected,(m,D,expected)
 print(m,'+' if D>0 else '-' if D<0 else '0','digits',len(str(abs(D))))
print('R544_INDEPENDENT_RAW_DET_PASS','H=B checked',r-1,'determinants',len(orders))
