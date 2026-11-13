#!/usr/bin/env python3
"""Exact native X6-BRC 24+24 phase-parity certificate (frozen f42f2906)."""
from itertools import product
import sympy as S
T=S.Symbol('u')
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c): return [-k if c>0 else k for k in STAR[a] if k!=abs(c)]
P=[(a,p,t*k) for a in range(4) for k in STAR[a] for t in (-1,1) for p in near(a,t*k)]
ID={p:i for i,p in enumerate(P)}
def nxt(i):
 a,p,c=P[i];b=next(b for b in range(4) if b!=a and abs(c) in STAR[b]);return [ID[v] for v in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]]
N=[nxt(i) for i in range(48)];g=ID[(0,1,-3)];axis=[abs(q[2])-1 for q in P]
plus=[i for i,p in enumerate(P) if p[2]>0];minus=[i for i,p in enumerate(P) if p[2]<0]
assert g==4 and len(plus)==len(minus)==24
assert all(P[i][2]*P[j][2]<0 for i in range(48) for j in N[i])
A0=S.zeros(48)
for i in range(48):
 for j in N[i]:A0[i,j]=1
D=A0.extract(plus,minus);E=A0.extract(minus,plus)
assert D.det()==E.det()==729
assert all(sum(axis[i]==a for i in ids)==4 for ids in (plus,minus) for a in range(6))

def Q(w,z):
 x=[1,1,1,1,w,w];M=S.zeros(48)
 for i in range(48):
  for j in N[i]:M[i,j]=x[axis[i]]*(1 if i==g else (3+z if j==g else 2))
 return M

def evalpoly(p,M):
 Z=S.zeros(24);I=S.eye(24)
 for c in S.Poly(p,T).all_coeffs():Z=Z*M+c*I
 return Z

for w,z in [(1,1),(1,2),(2,1),(2,2),(3,0),(3,2)]:
 A=Q(w,z);B=A.extract(plus,minus);C=A.extract(minus,plus)
 prod=w**8
 assert B.det()==2**23*3**6*(z+3)*prod
 assert C.det()==2**23*3**6*prod
 M=B*C;V=C*B
 assert M.charpoly(T)==V.charpoly(T)
 cp=M.charpoly(T).as_poly(T)
 F=S.Poly((T-4)*(T-4*w)**6*(T+12*w)**2*(T*T+4*(w+1)*T-48*w)**3,T)
 R=cp.exquo(F)
 if z==1: p=S.Poly(S.prod(f for f,_ in S.factor_list(cp.as_expr())[1]),T)
 elif w==1:
  h=S.Poly((T-4)*(T+12)*(T*T+8*T+144),T)
  p=h*S.Poly((T-36)*h.as_expr()-(z-1)*4*(T-12)*(5*T*T+72*T+1296),T)
 else:p=S.Poly((T-4)*(T-4*w)*(T+12*w)*(T*T+4*(w+1)*T-48*w),T)*R
 assert evalpoly(p,M).is_zero_matrix and evalpoly(p,V).is_zero_matrix
 for f,_ in S.factor_list(p.as_expr())[1]:
  assert not evalpoly(p.exquo(S.Poly(f,T)),M).is_zero_matrix
 print('PASS',w,z,'degree half',p.degree(),'full',2*p.degree())
# Typed 96-port adapter and nonstationary two-step identity.
E=[[] for _ in range(7)]
for i in range(48):
 for j in N[i]:
  for u,v in product((0,1),repeat=2):
   E[6 if j==g and u==v==1 else axis[i]].append((2*i+u,2*j+v))
assert list(map(len,E))==[93,96,96,96,96,96,3]
def step96(v,x,z):
 out=[0]*96
 for k,es in enumerate(E):
  for i,j in es:out[i]+=(x[k] if k<6 else x[0]*z)*v[j]
 return out
def enc(r):return [r[2*i] if i==g else r[2*i]+r[2*i+1] for i in range(48)]
def embed(v):
 r=[0]*96
 for i in range(48):
  r[2*i]=v[i]
  if i==g:r[2*i+1]=v[i]
 return r
def step48(M,v):return list(M*S.Matrix(v))
import random
rng=random.Random(601);full_cases=0;paired_cases=0
for case in range(9):
 r=[rng.randrange(11) for _ in range(96)]; matrices=[]
 for depth in range(1,11):
  x=[rng.randrange(6) for _ in range(6)];z=[0,1,2,5][(depth+case)%4]
  if depth%4==0:x=[1,1,1,1,0,0]
  old=r;r=step96(r,x,z);Qk=S.zeros(48)
  for i in range(48):
   for j in N[i]:Qk[i,j]=x[axis[i]]*(1 if i==g else (3+z if j==g else 2))
  if depth==1:v=enc(r)
  else:
   assert r==step96(embed(v),x,z)
   v=step48(Qk,v);assert v==enc(r)
  assert r[2*g]==r[2*g+1]
  matrices.append(Qk);full_cases+=1
 if case<4:
  # Explicitly factor the whole 10-step nonstationary Q product into 24-lane pairs.
  v0=[rng.randrange(11) for _ in range(48)]
  direct=v0[:]
  for A in matrices:direct=step48(A,direct)
  p=S.Matrix([v0[i] for i in plus]);m=S.Matrix([v0[i] for i in minus])
  for j in range(0,10,2):
   A1,A2=matrices[j],matrices[j+1]
   B1,C1=A1.extract(plus,minus),A1.extract(minus,plus)
   B2,C2=A2.extract(plus,minus),A2.extract(minus,plus)
   p,m=B2*C1*p,C2*B1*m
  got={i:int(v) for i,v in zip(plus,p)}
  got.update({i:int(v) for i,v in zip(minus,m)})
  assert direct==[got[i] for i in range(48)]
  paired_cases+=1
print('96_PORT_TESTS',full_cases,'NONSTATIONARY_PAIR_TESTS',paired_cases)
print('ALL_ASSERTIONS_PASS')
