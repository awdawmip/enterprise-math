#!/usr/bin/env python3
"""R541 reproducibility: fixed-k rational Toeplitz generating function and k=1,2 all-order positivity."""
from math import comb
import sympy as sp

def b(n, j): return comb(n,j) if 0 <= j <= n else 0
def catalan(k): return comb(2*k, k) // (k + 1)

def ballot(k, t):
    r = 2*k+1
    if not 2 <= t <= r: return 0
    return comb(r+t, 2*t)*sum(comb(t-1, 2*q)*4**q*catalan(k-q)
                                 for q in range(min((t-1)//2, k)+1))

def raw_H(k,t):
    r=2*k+1
    if not 2 <= t <= r: return 0
    return comb(r+t, 2*t)*sum(comb(r-t,q)*(b(2*t,r-2*q)-b(2*t,r-2*q-1)) for q in range(r-t+1))

def f_seq(k, N):
    C=catalan(k)
    p={t:sp.Rational(ballot(k,t),C) for t in range(2,2*k+2)}
    a=[(-1)**(n-1)*p[n+2]*p[2]**(n-1) for n in range(1,2*k)]
    f=[sp.Integer(1)]
    for n in range(1,N+1): f.append(sum(a[j-1]*f[n-j] for j in range(1,min(n,len(a))+1)))
    return p,a,f

for k in [1,2]:
    p,a,f=f_seq(k,500)
    assert all(raw_H(k,t)==ballot(k,t) for t in range(2,2*k+2))
    for n in range(1,10):
        A=sp.Matrix([[raw_H(k,3+i-j) for j in range(n)] for i in range(n)])
        assert A.det(method='berkowitz')==catalan(k)**n*f[n],(k,n)
    assert all(z>0 for z in f)
    print('k=',k,'C=',catalan(k),'p=',{x:str(y) for x,y in p.items()},'coeff=',list(map(str,a)),
          'raw_Berkowitz_orders=1..9','first_500_positive=True')

x=sp.symbols('x')
P=x**3-84*x**2+2205*x-25725
assert P.subs(x,50)==-475 and P.subs(x,51)==897
assert sp.discriminant(P,x)==-1667674575
assert sp.diff(P,x).subs(x,51)==1440
assert sp.Rational(2500,1440)>2*sp.Rational(515,924)
assert sp.Rational(25725,51)>504
print('R541_EXACT_PY_PASS raw_determinant=18 root_certificate=PASS all_order_proof=RESIDUE_BOUND')
