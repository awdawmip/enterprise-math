#!/usr/bin/env python3
"""R373: signed BRC r=5 exact finite PF2 phase; original R346 K/J, no R363 assumption.
Run: python research_notes/r373_signed_k3_corank5_phase_20261029_emr3/R372_reproduce.py
Requires sympy. Sign checks use exact Bernstein coefficients, not sample points.
"""
import sys
from fractions import Fraction
from math import comb
from pathlib import Path
from sympy import Symbol, Poly, Rational, binomial, expand, diff
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J
x=Symbol('theta')
def clean(p):
 p=list(p)
 while p and p[-1]==0:p.pop()
 return tuple(p)
def add(a,b):return clean((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))))
def scale(a,z):return clean(v*z for v in a)
def mul(a,b):
 if not a or not b:return ()
 c=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]+=u*v
 return clean(c)
def coeffs():
 S,P=29,17
 kk=[None]+[[((int(v),) if v else ()) for v in K(i)[:P+1]] for i in range(1,13)]
 assert kk[3][2]==(-8,)
 kk[3][2]=(-8,-8)
 B=[[() for _ in range(P+1)] for _ in range(S+1)]
 B[0][0]=B[0][1]=(1,)
 for s in range(1,S+1):
  for j,z in enumerate(J(s)[:P+1]):
   if z:B[s][j]=(int(z),)
  for i in range(1,min(12,s)+1):
   for j,z in enumerate(kk[i]):
    if not z:continue
    for p in range(j,P+1):
     if B[s-i][p-j]:B[s][p]=add(B[s][p],mul(z,B[s-i][p-j]))
 def D(q,k):
  z=()
  for w in range(k+1):z=add(z,scale(B[q+w][q],(-1)**(k-w)*comb(k,w)*2**(q-w)))
  return z
 a=[]
 for v in range(11):
  k=v+1;q=5+k
  m=add(mul(D(q,k),D(q+1,k+1)),scale(mul(D(q,k+1),D(q+1,k)),-1))
  a.append(scale(m,Fraction(5)**(9-2*k)))
 c=[]
 while a:
  c.append(expand(sum(Rational(z)*x**i for i,z in enumerate(a[0]))))
  a=[add(a[i+1],scale(a[i],-1)) for i in range(len(a)-1)]
 return c
def pos(p,lo,hi):
 lo,hi=Rational(lo),Rational(hi)
 P=Poly(p,x,domain='QQ').shift(lo);n=P.degree()
 a=[z*(hi-lo)**i for i,z in enumerate(reversed(P.all_coeffs()))]
 b=[sum(a[i]*Rational(binomial(k,i),binomial(n,i)) for i in range(k+1)) for k in range(n+1)]
 assert all(z>0 for z in b),(lo,hi)
def main():
 c=coeffs()
 assert len(c)==11
 assert [Poly(z,x).degree() for z in c]==[5,6,8,9,10,10,10,10,10,10,10]
 assert expand(c[10]-42*(30-16*x)**10)==0
 expected0=[-20971520000000,234291200000000,-3015884800000000,14308556800000000,-25150360960000000,13924994720000000]
 assert [int(a) for a in Poly(c[0],x,domain='ZZ').all_coeffs()]==expected0
 T=[expand(c[j]**2-c[j-1]*c[j+1]) for j in range(1,10)]
 a,b=Rational(133,125),Rational(213,200)
 for z in c[1:]+T:pos(z,-1,b)
 pos(c[0],-1,a);pos(-diff(c[0],x),a,b)
 assert c[0].subs(x,a)>0>c[0].subs(x,b)
 pos(-c[0],b,Rational(211,100))
 intervals=[Rational(211,100),Rational(9,4),Rational(5,2),Rational(11,4),Rational(3)]
 for lo,hi in zip(intervals,intervals[1:]):pos(-c[2],lo,hi)
 tail=list(reversed(Poly(-c[0],x,domain='QQ').shift(3).all_coeffs()))
 assert tail==[296458720000000,3917925760000000,5844992000000000,2091827200000000,80281600000000,20971520000000]
 u=Rational(15,8)
 for j in range(6,11):
  zz=Poly(c[j],x,domain='QQ')
  count=0;factor=Poly(x-u,x,domain='QQ')
  while zz.eval(u)==0:
   zz=zz.exquo(factor);count+=1
  assert count==2*(j-5),(j,count)
 assert all(c[j].subs(x,u)!=0 for j in range(6))
 sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
 from R369_check import compute_rows
 rows,_=compute_rows(x,5)
 assert len(rows[5])==11
 assert all(expand(rows[5][j]-c[j])==0 for j in range(11))
 print('R373_EXACT_PASS: 11 signed raw-D polynomials, 26 rational Bernstein strict-positivity interval certificates, 6 positive tail coefficients, 11/11 independent-route symbolic equalities.')
 print('PF2 exactly for -1 < theta <= rho5 where c0(rho5)=0 and 133/125<rho5<213/200.')
 print('For theta=15/8, c6..c10 have zero orders 2,4,6,8,10; finite F5 degree drops to 5.')
if __name__=='__main__':main()
