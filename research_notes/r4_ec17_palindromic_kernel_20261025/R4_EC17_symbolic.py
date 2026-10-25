#!/usr/bin/env python3
"""Exact independent SymPy audit of EC17's algebraic coefficient certificates."""
import json
import sympy as s

x,u,n = s.symbols('x u n')
Delta = 1-(1+u)*x+2*u**2*x**4-u**3*x**6
Nleft = (1-u*x**2)*(1-u*x**3)
Nright = (1-u*x**2)*(1-u**2*x**3)
E = (1-u*x**2)/Delta
assert s.cancel(E.subs({x:u*x,u:1/u}, simultaneous=True)-E) == 0
assert s.cancel((Nright-Nleft)/Delta - u*(1-u)*x**3*E)==0

A = [1/(1-x)]
for k in range(1,6):
    term = x*A[k-1]
    if k>=2: term -= 2*x**4*A[k-2]
    if k>=3: term += x**6*A[k-3]
    A.append(s.cancel(term/(1-x)))

out={}
for k in (4,5):
    q = x**3*(A[k-1]-(1+x**2)*A[k-2]+x**2*A[k-3])
    P = s.Poly(s.cancel(q*(1-x)**k),x)
    polynomial = s.factor(sum(value*s.prod(n-degree+i for i in range(1,k))/s.factorial(k-1)
                              for (degree,),value in P.terms()))
    expected = ((n-13)*(n-9)*(n-8)/6 if k==4
                else (n-15)*(n-10)*(n**2-25*n+148)/24)
    assert s.simplify(polynomial-expected)==0
    out[f'k{k}']={'numerator':str(s.factor(P.as_expr())),
                  'polynomial_n':str(polynomial),'degree_P':P.degree()}

print(json.dumps({'result':'PASS','palindromicity':'EXACT',
                  'reflection_defect':'EXACT','fixed_edge':out},ensure_ascii=False))
