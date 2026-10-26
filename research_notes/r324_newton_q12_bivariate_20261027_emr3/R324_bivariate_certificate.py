#!/usr/bin/env python3
"""R324 formal bivariate generating-function identity and high-tail sign witness."""
from sympy import symbols,expand,binomial,Poly
x,z,t,w=symbols('x z t w')
def C(n,k): return binomial(n,k) if 0<=k<=n else 0
def n(i):return -C(3,i-1)*z-C(6,i-1)*z**2+C(8,i-2)*z**3
def d(i):return (-C(4,i)+C(2,i-1))*z+(C(5,i-1)-C(5,i-2))*z**2+C(7,i-2)*z**3-C(9,i-3)*z**4
n_closed=1-z*w*(1+w)**3-z**2*w*(1+w)**6+z**3*w**2*(1+w)**8
delta_closed=-z*((1+w)**4-1)+z*w*(1+w)**2+z**2*w*(1-w)*(1+w)**5+z**3*w**2*(1+w)**7-z**4*w**3*(1+w)**9
assert expand(n_closed-1-sum(n(i)*w**i for i in range(1,11)))==0
assert expand(delta_closed-sum(d(i)*w**i for i in range(1,13)))==0
M=[1]
for s in range(1,5):
 M.append(expand(n(s)*(1-z)**s-sum(d(i)*M[s-i]*(1-z)**(i-1) for i in range(1,min(s,12)+1))))
s=3
B3=expand(sum(c*(1+t)**(2*s+1-j) for (j,),c in Poly(M[s],z).terms()))
assert B3.coeff(t,0)==8 and B3.coeff(t,3)==20 and B3.coeff(t,4)==-7
print('PASS GF numerator and denominator finite-binomial identity')
print('M3=',M[3])
print('B3=',B3)
