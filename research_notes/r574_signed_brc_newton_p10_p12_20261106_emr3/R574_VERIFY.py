#!/usr/bin/env python3
"""R574: exact p10/p12 signed BRC auxiliary scalar certificate.
Frozen R462 source: 18783e01e3646c72b7aab3b16d3f565e83e6446f.
Proof conditions: exact SymPy QQ polynomial identities/shift-coefficient signs;
independent literal Catalan/binomial evaluation via Fraction for 2<=k<=1000.
Run: python R574_VERIFY.py > R574_EVIDENCE.txt
"""
from math import comb, factorial
from fractions import Fraction
import sympy as S

k,u = S.symbols('k u', integer=True)

def catalan(n):
    return comb(2*n,n)//(n+1)

def H(n,j):
    r=2*n+1
    if j<2 or j>r: return 0
    return comb(r+j,2*j)*sum(comb(j-1,2*q)*4**q*catalan(n-q)
                 for q in range(min(n,(j-1)//2)+1))

def Aj(j):
    bq = (S.Rational(24,factorial(2*j+4))
          * S.prod(2*k+a for a in range(4,j+4))
          * S.prod(2*k-1-b for b in range(j)))
    def cq(q):
        return S.prod((k-v+1)/(2*(2*(k-v)-1)) for v in range(q))
    branch=sum(comb(j+1,2*q)*4**q*cq(q)
               for q in range((j+1)//2+1))
    return S.Poly(S.cancel(bq*branch),k)

A={}
p={}
for m in range(1,13):
    A[m]=Aj(m)
    p[m]=-sum(((-1)**j*A[j]*p[m-j] for j in range(1,m)),S.Poly(0,k)) - m*(-1)**m*A[m]
    assert p[m].degree() == 2*m

def shift_coeffs(m, origin):
    return list(reversed(S.Poly(p[m].as_expr().subs(k,u+origin),u).all_coeffs()))

neg10=shift_coeffs(10,5)
pos12=shift_coeffs(12,11)
assert len(neg10)==21 and all(x<0 for x in neg10)
assert len(pos12)==25 and all(x>0 for x in pos12)
assert all(p[10].eval(n)>0 for n in (2,3,4))
assert all(p[12].eval(n)>0 for n in (2,3,4))
assert all(p[12].eval(n)<0 for n in range(5,11))

# Cross-check symbolic formulas against original literal model independently.
for n in range(2,1001):
    h=H(n,2)
    c={j:Fraction(H(n,j+2),h) for j in range(1,13)}
    for j in range(1,13):
        assert c[j] == Fraction(A[j].eval(n))
    powers={}
    for m in range(1,13):
        powers[m]=-sum((-1)**j*c[j]*powers[m-j] for j in range(1,m))-m*(-1)**m*c[m]
        assert powers[m] == Fraction(p[m].eval(n))

const10=S.factor(abs(p[10].LC())/2)
const12=S.factor(p[12].LC()/2)
print('R574 FROZEN_SOURCE R462@18783e01e3646c72b7aab3b16d3f565e83e6446f')
print('MODEL d=2k-1, Q_k(z)=z^d+sum_{j=1}^d (-1)^j H_k(j+2)/H_k(2) z^(d-j)')
print('P10_DEGREE',p[10].degree())
print('P10_LEADING',p[10].LC())
print('P10_SHIFT_K5_COEFF_COUNT',len(neg10),'ALL_NEGATIVE',all(x<0 for x in neg10))
print('P12_DEGREE',p[12].degree())
print('P12_LEADING',p[12].LC())
print('P12_SHIFT_K11_COEFF_COUNT',len(pos12),'ALL_POSITIVE',all(x>0 for x in pos12))
print('P10_SIGNS',[(n,'+' if p[10].eval(n)>0 else '-') for n in (2,3,4,5,10,11)])
print('P12_SIGNS',[(n,'+' if p[12].eval(n)>0 else '-') for n in range(2,12)])
print('RHO10_LIMINF_FACTOR_POWER10',const10)
print('RHO12_LIMINF_FACTOR_POWER12',const12)
print('RHO12_FACTOR',S.N(const12**S.Rational(1,12),16))
print('P10_2_P12_2',p[10].eval(2),p[12].eval(2))
print('P10_5_P12_5',p[10].eval(5),p[12].eval(5))
print('P10_11_P12_11',p[10].eval(11),p[12].eval(11))
print('R574_NEWTON_P10_P12_EXACT_PASS k=2..1000 n=999')
