#!/usr/bin/env python3
"""PREFIX598U: exact uniform-gate 48-tail native BRC spectrum and jump certificate.
Run: python PREFIX598U_R2_uniform_gate_certificate.py (requires sympy).
Scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
import json
from itertools import product
import sympy as s
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
P=tuple((a,p,t*k) for a in range(4) for k in STAR[a] for t in (-1,1) for p in near(a,t*k))
IX={p:i for i,p in enumerate(P)}
def nxt(i):
 a,p,c=P[i];b=next(b for b in range(4) if b!=a and abs(c) in STAR[b])
 return tuple(IX[z] for z in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(nxt(i) for i in range(48))
G=IX[(0,1,-3)]
AX=tuple(abs(p[2])-1 for p in P)
assert G==4 and len(P)==48 and all(len(ns)==3 for ns in N)
E=[[] for _ in range(7)]
for i in range(48):
 for j in N[i]:
  for u,v in product((0,1),repeat=2):
   E[6 if j==G and u==v==1 else AX[i]].append((2*i+u,2*j+v))
assert list(map(len,E))==[93,96,96,96,96,96,3]
def qmat(z):
 A=s.zeros(48)
 for i in range(48):
  for j in N[i]:A[i,j]=1 if i==G else (3+z if j==G else 2)
 return A
def qstep(v,z):
 return [sum((1 if i==G else (3+z if j==G else 2))*v[j] for j in N[i]) for i in range(48)]
def astep(r,z):
 out=[0]*96
 for k,arcs in enumerate(E):
  for i,j in arcs:out[i]+=(z if k==6 else 1)*r[j]
 return out
def c48(r):return [r[2*j] if j==G else r[2*j]+r[2*j+1] for j in range(48)]
t=s.Symbol('t')
H=s.Poly((t*t-4)*(t*t+12)*(t*t-4*t+12)*(t*t+4*t+12),t)
P10=s.Poly((t*t-36)*H.as_expr(),t)
B=s.Poly(4*(t*t-12)*(5*t**4+72*t*t+1296),t)
F=(t-2)**12*(t+2)**12*(t*t+12)**5*(t*t-4*t+12)*(t*t+4*t+12)
def evalpoly(poly,M):
 out=s.zeros(48);I=s.eye(48)
 for a in poly.all_coeffs():out=out*M+a*I
 return out
def mul_mod(a,b,mod):
 k=len(mod)-1;c=[0]*(2*k-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:c[i+j]+=x*y
 for j in range(2*k-2,k-1,-1):
  q=c[j]
  if q:
   for i in range(k):c[j-k+i]-=q*mod[i]
 return c[:k]
def power_mod(n,poly):
 k=poly.degree()
 mod=list(reversed([int(c) for c in poly.all_coeffs()]))
 v=[1]+[0]*(k-1);b=[0,1]+[0]*(k-2)
 while n:
  if n&1:v=mul_mod(v,b,mod)
  b=mul_mod(b,b,mod);n>>=1
 return v
def jump(v,n,z):
 m=P10 if z==1 else H*s.Poly(P10.as_expr()-(z-1)*B.as_expr(),t)
 coeff=power_mod(n,m);ans=[0]*48;cur=v[:]
 for a in coeff:
  if a:ans=[u+a*w for u,w in zip(ans,cur)]
  cur=qstep(cur,z)
 return ans
def main():
 A=qmat(1);A2=qmat(2)
 assert s.expand(A.charpoly(t).as_expr()-F*P10.as_expr())==0
 assert s.expand(A2.charpoly(t).as_expr()-F*(P10.as_expr()-B.as_expr()))==0
 assert evalpoly(P10,A).is_zero_matrix
 assert s.gcd(P10,B).degree()==0
 u=s.Matrix([int(G in ns) for ns in N]);e=s.zeros(48,1);e[G]=1
 assert A2==A+u*e.T
 assert s.Matrix.hstack(*(A**i*u for i in range(10))).rank()==10
 r=[(7*i*i+11*i+3)%29 for i in range(96)]
 details=[]
 for z in (0,1,2,3,5):
  M=qmat(z);m=P10 if z==1 else H*s.Poly(P10.as_expr()-(z-1)*B.as_expr(),t)
  assert evalpoly(m,M).is_zero_matrix
  assert M==A+(z-1)*u*e.T
  seed=c48(astep(r,z))
  assert qstep(seed,z)==list(M*s.Matrix(seed))
  for n in (0,1,2,8,32,128,512):
   v=seed[:]
   for _ in range(n):v=qstep(v,z)
   assert jump(seed,n,z)==v
  details.append({'z':z,'degree':m.degree(),'bits_at_512':max(abs(x).bit_length() for x in v)})
 return {'status':'ALL_ASSERTIONS_PASS','phases':48,'ports':96,'typed_arcs':sum(map(len,E)),
         'krylov_rank':10,'test_gates':details,'jump_depths':[0,1,2,8,32,128,512],
         'P10':str(P10.as_expr().expand()),'H8':str(H.as_expr().expand()),
         'B6':str(B.as_expr().expand())}
if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False))
