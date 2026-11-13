#!/usr/bin/env python3
"""Two positive rational native X6-BRC collision points: sharp 24-state order 13."""
import sympy as S
from PREFIX601_R2_exact_certificate import P,N,g,axis,plus,minus,T,evalpoly,step96,enc,embed

def Q(w,z):
 x=[1,1,1,1,w,w];M=S.zeros(48)
 for i in range(48):
  for j in N[i]:M[i,j]=x[axis[i]]*(1 if i==g else (3+z if j==g else 2))
 return M

w=S.Integer(2)
for name,z,shared in [('A',S.Rational(109,17),T-8),('B',S.Rational(153,13),T+24)]:
 A=Q(w,z);B=A.extract(plus,minus);C=A.extract(minus,plus);M=B*C
 cp=M.charpoly(T).as_poly(T)
 F=S.Poly((T-4)*(T-8)**6*(T+24)**2*(T*T+12*T-96)**3,T)
 R=cp.exquo(F)
 H=S.Poly((T-4)*(T-8)*(T+24)*(T*T+12*T-96),T)
 assert S.gcd(H,R).monic()==S.Poly(shared,T).monic()
 mu=(H*R).exquo(S.Poly(shared,T))
 assert mu.degree()==13
 assert evalpoly(mu,M).is_zero_matrix and evalpoly(mu,C*B).is_zero_matrix
 sharp=[]
 for f,_ in S.factor_list(mu.as_expr())[1]:
  n=sum(bool(a) for a in evalpoly(mu.exquo(S.Poly(f,T)),M))
  assert n>0
  sharp.append((str(f),n))
 # Exact source-port observer preservation at both rational collision gates.
 x=[1,1,1,1,2,2]
 for case in range(8):
  r=[(i+case)%11 for i in range(96)]
  r=step96(r,x,z);v=enc(r)
  assert r[2*g]==r[2*g+1]
  for depth in range(2,8):
   r=step96(r,x,z)
   assert r==step96(embed(v),x,z)
   v=list(A*S.Matrix(v))
   assert v==enc(r)
 print('PASS',name,'w=2 z=',z,'nu_degree=13 full_Q_degree=26','factors=',len(sharp),'port_checks=',8*6)
 print('sharp_witnesses',sharp)
print('ALL_ASSERTIONS_PASS')
