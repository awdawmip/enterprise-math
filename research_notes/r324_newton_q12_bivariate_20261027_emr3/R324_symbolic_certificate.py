#!/usr/bin/env python3
"""R324 exact recurrence certificate: fully symbolic P_0..P_12 and q=12 Newton polynomial.
Uses original coefficient recurrence for base jets (integer arithmetic) and Q[s] induction,
not point interpolation. Does not assume a physical BRC-to-Cell correspondence.
"""
from math import comb, factorial
from sympy import S, symbols, Poly, diff, expand, binomial, cancel, expand_func
s,z,u = symbols('s z u')
TOP=12
C=lambda n,k: S(comb(n,k)) if 0<=k<=n else S.Zero
n=lambda i: -C(3,i-1)*z-C(6,i-1)*z**2+C(8,i-2)*z**3
delta=lambda i: (-C(4,i)+C(2,i-1))*z+(C(5,i-1)-C(5,i-2))*z**2+C(7,i-2)*z**3-C(9,i-3)*z**4
def add(a,b,scale=1):
 c=[0]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=scale*v
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,ai in enumerate(a):
  if ai:
   for j,bj in enumerate(b):
    if bj:c[i+j]+=ai*bj
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def B(k):return [(-1)**i*comb(k,i) for i in range(k+1)]
def npc(i):return [0,-int(C(3,i-1)),-int(C(6,i-1)),int(C(8,i-2))]
def dpc(i):return [0,int(-C(4,i)+C(2,i-1)),int(C(5,i-1)-C(5,i-2)),int(C(7,i-2)),-int(C(9,i-3))]
M=[[1]]
for k in range(1,TOP+1):
 out=mul(npc(k),B(k))
 for i in range(1,min(k,12)+1):out=add(out,mul(mul(dpc(i),M[k-i]),B(i-1)),scale=-1)
 M.append(out)
def moment(p,r):return sum(c*factorial(j)//factorial(j-r) for j,c in enumerate(p) if j>=r)
P=[S.One]
assert sum(M[0])==1
for r in range(1,TOP+1):
 D=S.Zero
 for i in range(1,r+2):
  for a in range(r+2-i):
   if (i,a)==(1,0):continue
   h=r+1-i-a
   ddi=diff(delta(i),z,a).subs(z,1)
   if ddi==0:continue
   D+=(-1)**i * S(factorial(r))/factorial(r+1-i)*binomial(r+1-i,a)*ddi*P[h].subs(s,s-i)/S(2)**i
 D=expand(D)
 assert Poly(D,s).degree()==r-1,('D degree',r)
 A=S.Zero;R=D
 for d in reversed(range(r)):
  c=Poly(R,s).coeff_monomial(s**d)
  term=c*s**(d+1)/(d+1)
  A+=term;R=expand(R-(term-term.subs(s,s-1)))
 assert R==0,('antidifference remainder',r,R)
 base=moment(M[r],r)
 A=expand(A+(S(base)/S(2)**r-A.subs(s,r)))
 assert expand(A-A.subs(s,s-1)-D)==0,('delta identity',r)
 assert A.subs(s,r)==S(base)/S(2)**r,('base',r)
 P.append(A)
 if r in (10,11,12):
  den,num=Poly(A,s).clear_denoms(convert=True)
  print('P',r,'m_base',base,'P_den',den,'P_num',list(map(int,num.all_coeffs())),flush=True)
  dd,nn=Poly(D,s).clear_denoms(convert=True)
  print('D',r,'D_den',dd,'D_num',list(map(int,nn.all_coeffs())),flush=True)
q=12
recovered=cancel(expand(expand_func(sum((-1)**r*binomial(2*s+1-r,q-r)*P[r]/factorial(r) for r in range(q+1)))))
qden,qnum=Poly(recovered,s).clear_denoms(convert=True)
shift=Poly(expand(qnum.as_expr().subs(s,q+u)),u)
print('Q12 denominator',qden)
print('Q12 numerator descending',list(map(int,qnum.all_coeffs())))
print('Q12 shift descending',list(map(int,shift.all_coeffs())))
print('ALL SHIFT POSITIVE',all(x>0 for x in shift.all_coeffs()))
print('BORDER normalized',recovered.subs(s,q),'a_12_0',int(S(2)**q*recovered.subs(s,q)))
assert int(S(2)**q*recovered.subs(s,q))==sum(c*int(C(2*q+1-j,q)) for j,c in enumerate(M[q]))
assert all(x>0 for x in shift.all_coeffs()),'Shift positivity fails'
print('PASS: algebraic r=0..12 induction, q=12 exact recovery and positivity')
