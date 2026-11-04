#!/usr/bin/env python3
"""R543 independent raw-signed H and Toeplitz determinant check."""
from math import comb
import sympy as sp
def b(n,j):return comb(n,j) if 0<=j<=n else 0
def cat(k):return comb(2*k,k)//(k+1)
def raw(k,t):
    r=2*k+1
    if not 2<=t<=r:return 0
    return comb(r+t,2*t)*sum(comb(r-t,q)*(b(2*t,r-2*q)-b(2*t,r-2*q-1)) for q in range(r-t+1))
def ballot(k,t):
    r=2*k+1
    if not 2<=t<=r:return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*cat(k-q) for q in range(min((t-1)//2,k)+1))
k=5;d=2*k-1;r=2*k+1
assert all(raw(k,t)==ballot(k,t) for t in range(2,r+1))
p={t:sp.Rational(raw(k,t),cat(k)) for t in range(2,r+1)}
a=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,d+1)]
f=[sp.Integer(1)]
for m in range(1,45):
    f.append(sum(a[j-1]*f[m-j] for j in range(1,min(d,m)+1)))
for m in [1,2,3,4,5,6,7,8,43]:
    M=sp.Matrix([[raw(k,3+i-j) for j in range(m)] for i in range(m)])
    v=M.det(method='berkowitz')
    assert v==cat(k)**m*f[m],(m,v)
    assert (v>0 if m<=8 else v<0),(m,v)
print('R543_INDEPENDENT_RAW_PASS H/B=10, raw matrices=9 (incl m43), negative43=True')
