#!/usr/bin/env python3
"""Exact six-label moment recurrence / distributional ODE / Frobenius certificate.
Scalar observer only; does not simulate native X6 BRC propagation.
Requires sympy. Assertion arithmetic is integral and rational.
"""
from math import comb
import sympy as sp
from sympy.functions.combinatorial.numbers import stirling
x,n,D = sp.symbols('x n D')
A=[1,6,66]
for r in range(2,25):
    num=(2*(2*r+1)*(14*r**4+28*r**3+28*r**2+14*r+3)*A[r]
         -4*r**3*(196*r**2+59)*A[r-1]
         +1152*(2*r-1)*r*r*(r-1)**2*A[r-2])
    assert num % (r+1)**5 == 0
    A.append(num // (r+1)**5)

def collision(R):
    a=[1]*(R+1)
    for d in range(2,7):
        a=[sum(comb(i,k)**2*a[i-k] for k in range(i+1)) for i in range(R+1)]
    return a
assert A[:13]==collision(12)
R={
    3:(n+3)**5,
    2:-2*(2*n+5)*(14*(n+2)**4+28*(n+2)**3+28*(n+2)**2+14*(n+2)+3),
    1:4*(n+2)**3*(196*(n+2)**2+59),
    0:-1152*(2*n+3)*(n+2)**2*(n+1)**2
}
for m in range(13):
    assert sum(int(R[j].subs(n,m))*A[m+j] for j in R)==0
# < y^m, y^j Q_j(theta) rho> = Q_j(-m-j-1)*A[m+j].
Q={j:sp.expand(R[j].subs(n,-D-j-1)) for j in R}
highest=sp.factor(sum(x**j*sp.Poly(Q[j],D).coeff_monomial(D**5) for j in R))
assert sp.expand(highest+(x-4)*(x-16)*(x-36))==0
deriv={
    h:sp.factor(x**h*sum(x**j*sum(
        sp.Poly(Q[j],D).coeff_monomial(D**k)*stirling(k,h,kind=2)
        for k in range(h,6)) for j in R)) for h in range(6)
}
assert sp.expand(deriv[5]+x**5*(x-4)*(x-16)*(x-36))==0
assert sp.factor(deriv[4]+5*x**4*(3*x**3-140*x**2+1568*x-3456))==0
for c in (4,16,36):
    a5p=sp.diff(deriv[5],x).subs(x,c)
    a4=deriv[4].subs(x,c)
    assert 4-a4/a5p==sp.Rational(3,2)
    print('critical',c,'exponents 0,1,2,3,3/2','leading derivative',a5p,'a4',a4)
assert sp.factor(Q[3]+(D+1)**5)==0
print('PASS: independent collision moments r=0..12; all tested recurrence identities')
print('PASS: fifth-order distribution ODE; singularities 0,4,16,36; Frobenius exponents')
print('Q:',{j:str(sp.factor(Q[j])) for j in sorted(Q,reverse=True)})
print('a5:',sp.factor(deriv[5]))
print('a4:',sp.factor(deriv[4]))
