#!/usr/bin/env python3
"""Independent exact signed-BRC coefficient / direct Berkowitz matrix checks for R510.
Raw H via ballot-Catalan sum, different from JS coefficient extraction; no floating point.
"""
import json
from math import comb
from sympy import Matrix

def binom(n, j):
    return comb(n, j) if 0 <= j <= n else 0
def catalan(k):
    return comb(2*k,k)//(k+1)
def h_alt(k,t):
    r=2*k+1
    if t<2 or t>r: return 0
    b=sum(binom(t-1,2*q)*(4**q)*catalan(k-q) for q in range(min((t-1)//2,k)+1))
    return binom(r+t, 2*t)*b

points=(1,6,7,8,9,10,15,37,38,65,66,67,68)
res=[]
for k in points:
    A=Matrix(33,33, lambda i,j: h_alt(k,3+i-j))
    det=int(A.det(method='berkowitz'))
    res.append({'k':k,'r':2*k+1,'sign':'+' if det>0 else '-' if det<0 else '0','determinant_abs_digits':len(str(abs(det)))})
assert [v['sign'] for v in res]==['+','+','+','-','-','-','-','-','-','-','-','+','+']
print(json.dumps({'status':'R510_INDEPENDENT_PASS','method':'Python SymPy Berkowitz directly on original 33x33 Toeplitz matrix; H from independent ballot-Catalan sum','points':res,'scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f'},indent=2))
