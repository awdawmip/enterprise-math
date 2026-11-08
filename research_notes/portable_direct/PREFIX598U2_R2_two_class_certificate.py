#!/usr/bin/env python3
"""PREFIX598U2: exact two-class X6-BRC 48-tail minimal-polynomial certificate.
Run from same directory as PREFIX598U_R2_uniform_gate_certificate.py.
Requires sympy. No floating-point computation used for theorem checks.
"""
import json
import sympy as s
from PREFIX598U_R2_uniform_gate_certificate import N,G,AX
t=s.Symbol('t')
X=(1,1,1,1,2,2)
def Q(z,axes=X):
 A=s.zeros(48)
 for i in range(48):
  for j in N[i]:
   A[i,j]=axes[AX[i]]*(1 if i==G else (3+z if j==G else 2))
 return A
A=Q(1);A2=Q(2)
c1=s.Poly(A.charpoly(t).as_expr(),t)
c2=s.Poly(A2.charpoly(t).as_expr(),t)
F=s.gcd(c1,c2-c1)
P=c1.quo(F)
B=-(c2-c1).quo(F)
h=s.Poly(s.prod(p for p,m in s.factor_list(F.as_expr())[1]),t)
rad=s.Poly(s.prod(p for p,m in s.factor_list(c1.as_expr())[1]),t)
assert F.degree()==30 and P.degree()==18 and B.degree()==14
assert h.degree()==10 and rad.degree()==22
assert s.gcd(P,B).degree()==0 and s.gcd(h,B).degree()==0
u=s.Matrix([X[AX[i]]*int(G in N[i]) for i in range(48)])
e=s.zeros(48,1);e[G]=1
assert A2==A+u*e.T
assert s.Matrix.hstack(*(A**k*u for k in range(18))).rank()==18
identity=s.eye(48)
def zero(poly,mat):
 v=s.zeros(48)
 for a in poly.all_coeffs():v=v*mat+a*identity
 return v.is_zero_matrix
assert zero(rad,A)
case=[]
for z in (0,1,2,3):
 m=rad if z==1 else h*s.Poly(P.as_expr()-(z-1)*B.as_expr(),t)
 assert zero(m,Q(z))
 case.append({'z':z,'exact_annihilator_degree':m.degree()})
assert s.factor(F.as_expr())==(t-2)*(t+2)*(t*t-8)**6*(t*t+24)**2*(t**4+12*t*t-96)**3
assert s.factor(B.as_expr())==4*(9*t**14+160*t**12+5200*t**10-111488*t**8+104448*t**6-37601280*t**4+429981696*t*t-1146617856)
print(json.dumps({'status':'ALL_ASSERTIONS_PASS','weights':X,'charpoly_fixed_degree':F.degree(),'moving_degree':P.degree(),
'B_degree':B.degree(),'Krylov_rank':18,'minimal_polynomial_cases':case,'P18':str(s.factor(P.as_expr())),
'F30':str(s.factor(F.as_expr()))},ensure_ascii=False))
