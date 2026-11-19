#!/usr/bin/env python3
"""EC49FUF: first endpoint-saddle failure at n=17 for fixed width x=5/123.
Exact Fraction and integer polynomial certificate, Python standard library only.
Frozen BRC16943: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab
Predecessor EC49FUE-S: 191fb5ec2276c7caa28f6c42c6b6c9699d660e0b
"""
from fractions import Fraction as F
from math import comb, lcm

E=F(1048576,18958647);m=F(1469,64);L=F(951,1280);U=F(3,4);W=U-L;X=F(5,123)
A_MEAN=m*(L+U)/2;C_MEAN=m*(U-X*W/2)

def p(e):
 return X*C_MEAN/A_MEAN if e is None else X*(1-e*C_MEAN)/(1-e*A_MEAN)
def q(e):
 return F(575*41217719,45529434409) if e is None else F(575)*(41217719*e-2359296)/(45529434409*e-2630615040)
def r(e):return p(e)+q(e)*(1-p(e))
def tail(n,y,j):return sum((F(comb(n,k))*y**k*(1-y)**(n-k) for k in range(j,n+1)),F(0))
def delta(n,e,j):return tail(n,r(e),j)-tail(n,p(e),j)
def mass(n,e,k):return F(comb(n,k))*(r(e)**k*(1-r(e))**(n-k)-p(e)**k*(1-p(e))**(n-k))

def add(v,w):
 out=[0]*max(len(v),len(w))
 for i,z in enumerate(v):out[i]+=z
 for i,z in enumerate(w):out[i]+=z
 return out
def sub(v,w):return add(v,[-z for z in w])
def scale(v,z):return [z*x for x in v]
def mul(v,w):
 a=[0]*(len(v)+len(w)-1)
 for i,x in enumerate(v):
  if x:
   for j,y in enumerate(w):a[i+j]+=x*y
 return a
def pw(v,n):
 a=[1]
 for _ in range(n):a=mul(a,v)
 return a
def clear(v,w):
 t=lcm(*(z.denominator for z in v+w));return [int(z*t) for z in v],[int(z*t) for z in w]
def tailpoly(num,den,n,j):
 out=[0];oth=sub(den,num)
 # precompute powers
 X=[pw(num,k) for k in range(n+1)];Y=[pw(oth,k) for k in range(n+1)]
 for k in range(j,n+1):out=add(out,scale(mul(X[k],Y[n-k]),comb(n,k)))
 return out

AD,PN=clear([1-E*A_MEAN,A_MEAN],[X*(1-E*C_MEAN),X*C_MEAN])
BD,QN=clear([F(2630615040)-45529434409*E,F(45529434409)],[F(575)*(2359296-41217719*E),F(575*41217719)])
VV=mul(AD,BD);RR=sub(add(mul(PN,BD),mul(QN,AD)),mul(PN,QN))

def verify():
 assert W==F(9,1280) and X*W==F(3,10496)
 assert p(E)==F(311263325,8339351907)
 assert r(E)==F(5867068998425,13670371100129)
 assert all(z>0 for z in AD+BD)
 print('width=',X,'pE=',p(E),'rE=',r(E))
 bands={**{n:1 for n in range(1,6)},**{n:2 for n in range(6,12)},**{n:3 for n in range(12,18)}}
 cumulative=0
 for n in range(1,18):
  js=[j for j in range(1,n+1) if all(mass(n,E,k)<0 for k in range(j)) and all(mass(n,E,k)>0 for k in range(j,n+1))]
  assert len(js)==1, (n,js)
  j=js[0];assert j==bands[n],(n,j);d0=delta(n,E,j)
  Dnum=sub(tailpoly(RR,VV,n,j),mul(tailpoly(PN,AD,n,j),pw(BD,n)))
  H=sub(scale(Dnum,d0.denominator),scale(pw(VV,n),d0.numerator))
  while H[-1]==0:H.pop()
  nonzero=H[1:]
  neg=sum(1 for a in nonzero if a<0);pos=sum(1 for a in nonzero if a>0);zeros=sum(1 for a in nonzero if a==0)
  assert H[0]==0 and len(H)==2*n+1
  if n<=16:
   assert neg==0 and zeros==0 and pos==2*n
   assert delta(n,None,j)>d0
   cumulative+=pos
  else:
   assert neg==1 and H[-1]<0 and pos==33 and zeros==0
   assert delta(n,-1,j)<d0
  # Cross-check the polynomial identity at independent exact rational parameters.
  for sv in (F(0),F(1),F(7,3)):
   poly_value=sum(F(v)*sv**k for k,v in enumerate(H))
   denom=d0.denominator*sum(F(v)*sv**k for k,v in enumerate(pw(VV,n)))
   assert poly_value/denom==delta(n,E-sv,j)-d0
  print('n',n,'j',j,'positive',pos,'negative',neg,'Hdegree',len(H)-1,flush=True)
 assert cumulative==sum(2*n for n in range(1,17))==272
 print('PASS 272/272 strictly positive coefficients for n<=16; n17 highest-degree coefficient negative')

if __name__=='__main__': verify()
