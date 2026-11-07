#!/usr/bin/env python3
"""R372: exact signed BRC r=4 PF2 phase; original R346 K/J, no R363 assumption.
Run: python research_notes/r372_signed_k3_corank4_phase_20261029_emr3/R372_reproduce.py
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
 S,P=24,14
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
 for v in range(9):
  k=v+1;q=4+k
  m=add(mul(D(q,k),D(q+1,k+1)),scale(mul(D(q,k+1),D(q+1,k)),-1))
  a.append(scale(m,Fraction(5)**(7-2*k)))
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
 c=coeffs();assert len(c)==9
 assert [Poly(z,x).degree() for z in c]==[4,6,7,8,8,8,8,8,8]
 T=[expand(c[j]**2-c[j-1]*c[j+1]) for j in range(1,8)]
 U=expand(7*c[1]**2-16*c[0]*c[2]); a,b=Rational(1469,1000),Rational(1470,1000)
 lo,hi=Rational(1710,1000),Rational(1711,1000); end=Rational(9,4)
 for z in c:pos(z,-1,b)
 for z in T[1:]:pos(z,-1,b)
 pos(-U,-1,b)
 pos(T[0],-1,a);pos(-T[0],b,hi);pos(-diff(T[0],x),a,b)
 pos(c[1],-1,lo);pos(-c[1],hi,end);pos(-diff(c[1],x),lo,hi)
 tail=list(reversed(Poly(-c[0],x,domain='QQ').shift(end).all_coeffs()))
 assert tail==[1351200000,368160000000,1224192000000,1398784000000,3276800000]
 assert expand(c[8]-14*(30-16*x)**8)==0
 assert [int(z.subs(x,0)) for z in c]==[10478580000000,74179222880000,250257279520000,494571650400000,618103193760000,497471220000000,251096760000000,72564660000000,9185400000000]
 print('R372_EXACT_PASS: 9 raw-D polynomials, 22 positive Bernstein interval certificates, 5 tail coefficients')
 print('PF2 iff -1 < theta <= sigma4, sigma4 uniquely in (1469/1000,1470/1000). PF-infinity never for theta>-1.')
if __name__=='__main__':main()
