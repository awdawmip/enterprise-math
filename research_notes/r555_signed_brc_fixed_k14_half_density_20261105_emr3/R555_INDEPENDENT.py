#!/usr/bin/env python3
"""R555 independent original integer convolution / Berkowitz determinant cross-check."""
from math import comb
from sympy import Matrix
def raw(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 v=[comb(2*t,j) for j in range(2*t+1)]
 w=[0]*(r+1)
 for q in range(r-t+1):
  for j in range(2*t+1):
   idx=2*q+j
   if idx<=r:w[idx]+=comb(r-t,q)*v[j]
 return comb(r+t,2*t)*(w[r]-w[r-1])
def recurse(k,mx):
 den=raw(k,2);h=[raw(k,j+2) for j in range(1,2*k)]
 D=[1]
 for m in range(1,mx+1):
  D.append(sum((-1)**(j-1)*h[j-1]*den**(j-1)*D[m-j]
               for j in range(1,min(m,2*k-1)+1)))
 return D
if __name__=="__main__":
 k=14;D=recurse(k,16)
 for m in range(1,17):
  mat=Matrix(m,m,lambda i,j:raw(k,3+i-j))
  assert mat.det(method="berkowitz")==D[m],m
 print("R555_INDEPENDENT_BERKOWITZ_PASS m=1..16 signs=", [int(x>0)-int(x<0) for x in D[:17]])
