#!/usr/bin/env python3
"""R555: exact k=13 signed BRC root isolation and finite recurrence checks.
Python 3 + SymPy; float nroots is only a candidate generator.
All proof predicates use Python Fraction.
"""
from fractions import Fraction as F
from decimal import Decimal
from math import comb, lcm
from time import perf_counter
import sympy as S
K=14; d=27; eps=F(1,10000)
def C(n): return comb(2*n,n)//(n+1)
def H(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(k-q) for q in range(min((t-1)//2,k)+1))
def H_raw(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 total=0
 for q in range(r-t+1):
  h=r-2*q
  if 0<=h<=2*t:total+=comb(2*t,h)*comb(r-t,q)
  if 0<=h-1<=2*t:total-=comb(2*t,h-1)*comb(r-t,q)
 return comb(r+t,2*t)*total
def polynomials():
 assert all(H(K,t)==H_raw(K,t) for t in range(2,2*K+2))
 p2=F(H(K,2),C(K))
 a=[F((-1)**(j-1)*H(K,j+2),C(K))/p2 for j in range(1,d+1)]
 co=[F(1)]+[-v for v in a]
 L=1
 for v in co:L=lcm(L,v.denominator)
 ints=[int(v*L) for v in co]
 assert ints[0]>0 and all(F(z,ints[0])==v for z,v in zip(ints,co))
 return ints,a,p2
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def n2(a):return a[0]*a[0]+a[1]*a[1]
def upper(a):return abs(a[0])+abs(a[1])
def lower(a):return max(abs(a[0]),abs(a[1]))
# Fixed rational centres (discoverable by nroots; every root assertion below is exact).
CENTERS=[
 ("11.173455980451","-15.184653065800"),
 ("11.173455980451","15.184653065800"),
 ("6.2386687855971","0"),
 ("5.1137655900491","-3.7867908468940"),
 ("5.1137655900491","3.7867908468940"),
 ("2.7146842961466","-1.7455289581489"),
 ("2.7146842961466","1.7455289581489"),
 ("1.7982289197651","-1.0496603150888"),
 ("1.7982289197651","1.0496603150888"),
 ("1.3248583355894","-0.70947477788846"),
 ("1.3248583355894","0.70947477788846"),
 ("1.0396185347224","-0.51880059016433"),
 ("1.0396185347224","0.51880059016433"),
 ("0.85130517163074","-0.39964642256488"),
 ("0.85130517163074","0.39964642256488"),
 ("0.71990091353151","-0.31760107123437"),
 ("0.71990091353151","0.31760107123437"),
 ("0.62475421689530","-0.25651074784581"),
 ("0.62475421689530","0.25651074784581"),
 ("0.55363234525618","-0.20788730157824"),
 ("0.55363234525618","0.20788730157824"),
 ("0.49863560332989","-0.16652027042382"),
 ("0.49863560332989","0.16652027042382"),
 ("0.45400927135018","-0.12851206224589"),
 ("0.45400927135018","0.12851206224589"),
 ("0.41381642848426","-0.089523066428600"),
 ("0.41381642848426","0.089523066428600")]
def Taylor_at(c,co):
 t=[]
 for a in co:
  nt=[(F(a),F(0))]+[(F(0),F(0))]*len(t)
  for j,z in enumerate(t):
   nt[j]=add(nt[j],mul(c,z));nt[j+1]=add(nt[j+1],z)
  t=nt
 return t
def certify(co):
 cc=[(F(x),F(y)) for x,y in CENTERS]; assert len(cc)==d
 ratios=[]
 for idx,c in enumerate(cc):
  b=Taylor_at(c,co)
  lhs=lower(b[1])*eps
  rhs=upper(b[0])+sum((upper(b[j])*eps**j for j in range(2,d+1)),F(0))
  assert lhs>rhs,("Rouche",idx,float(rhs/lhs))
  ratios.append(rhs/lhs)
 for i in range(d):
  for j in range(i+1,d):
   assert n2((cc[i][0]-cc[j][0],cc[i][1]-cc[j][1]))>4*eps*eps
 assert cc[0][0]==cc[1][0] and cc[0][1]==-cc[1][1] and cc[0][1]!=0
 assert n2(cc[0])>(F(18)+eps)**2
 assert all(n2(c)<(F(7)-eps)**2 for c in cc[2:])
 # Optional strict phase wedge pi/4 < theta < pi/3.
 assert cc[0][0]>eps and abs(cc[0][1])>cc[0][0]+2*eps
 assert 3*(cc[0][0]-eps)**2>(abs(cc[0][1])+eps)**2
 assert max(ratios)<F(3,500),max(ratios)
 print("R555_RATIONAL_ROUCHE_PASS roots=27 disjoint_pairs=351 radius=1/10000 max_ratio_lt=3/500")
def finite(a):
 t=[F(1)]
 for m in range(1,1025):
  t.append(sum((a[j-1]*t[m-j] for j in range(1,min(m,d)+1)),F(0)))
 result=(sum(v>0 for v in t),sum(v<0 for v in t),
         sum(v==0 for v in t),sum(t[i-1]*t[i]<0 for i in range(1,len(t))))
 assert result==(515,510,0,304),result
 print("R555_RECURRENCE_PASS m=0..1024 plus=515 minus=510 zero=0 changes=304")
if __name__=="__main__":
 t=perf_counter();co,a,p2=polynomials()
 assert C(K)==2674440 and p2==31465
 print("R555_RAW_COEFFICIENT_PASS count=28 C14=2674440 p2=31465 degree=27")
 certify(co);finite(a)
 print("R555_ROOT_AND_RECURRENCE_CERT_PASS elapsed_s=",round(perf_counter()-t,3))
