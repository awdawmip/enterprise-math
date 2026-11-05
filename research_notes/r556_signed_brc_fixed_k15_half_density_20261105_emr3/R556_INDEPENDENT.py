#!/usr/bin/env python3
"""R556: independent original-integer H convolution and 16 Berkowitz determinants."""
from fractions import Fraction as F
from sympy import Matrix
from R556_VERIFY import M, polynomials
K=15;d=29
co,a,p2=polynomials()
assert all(M.H(K,t)==M.H_raw(K,t) for t in range(2,2*K+2))
s=[F(1)]
for m in range(1,17):
 s.append(sum((a[j-1]*s[m-j] for j in range(1,min(m,d)+1)),F(0)))
 matrix=Matrix([[M.H_raw(K,3+i-j) for j in range(m)] for i in range(m)])
 assert matrix.det(method="berkowitz")==s[m]*(M.C(K)*p2)**m,m
print("R556_RAW_H_AND_BERKOWITZ_PASS H=30 determinants=16")
