#!/usr/bin/env python3
"""R542 independent raw-H/B and original Toeplitz determinant crosscheck.
Uses SymPy Berkowitz as independent path from the rational Rouche certificate.
"""
from math import comb
from fractions import Fraction as F
import sympy as sp

def b(n,j): return comb(n,j) if 0<=j<=n else 0
def cat(k): return comb(2*k,k)//(k+1)
def raw_H(k,t):
    r=2*k+1
    if not 2<=t<=r:return 0
    return comb(r+t,2*t)*sum(
      comb(r-t,q)*(b(2*t,r-2*q)-b(2*t,r-2*q-1))
      for q in range(r-t+1))
def ballot(k,t):
    r=2*k+1
    if not 2<=t<=r:return 0
    return comb(r+t,2*t)*sum(
      comb(t-1,2*q)*4**q*cat(k-q)
      for q in range(min((t-1)//2,k)+1))
for k in (3,4):
    r=2*k+1
    for t in range(2,r+1):
        assert raw_H(k,t)==ballot(k,t),(k,t)
    p={t:sp.Rational(ballot(k,t),cat(k)) for t in range(2,r+1)}
    d=2*k-1
    a=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,d+1)]
    f=[sp.Integer(1)]
    for m in range(1,9):
        f.append(sum(a[j-1]*f[m-j] for j in range(1,min(d,m)+1)))
        M=sp.Matrix([[raw_H(k,3+i-j) for j in range(m)] for i in range(m)])
        assert M.det(method="berkowitz")==cat(k)**m*f[m],(k,m)
        assert f[m]>0
    print("k",k,"H/B equations",r-1,"raw Berkowitz determinants",8,"PASS")
print("R542_INDEPENDENT_RAW_DET_PASS")
