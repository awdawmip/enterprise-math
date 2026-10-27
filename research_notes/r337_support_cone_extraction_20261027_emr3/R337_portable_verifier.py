#!/usr/bin/env python3
"""Standalone exact R337 checker: original signed K/J, no prior R-series imports."""
import json,sys
from math import comb
from fractions import Fraction as F

def C(n,k): return comb(n,k) if 0<=k<=n else 0
def plus(a,b):
 c=[0]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return trim(c)
def trim(a):
 while len(a)>1 and not a[-1]:a.pop()
 return a
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def get(a,i):return a[i] if i<len(a) else 0
def K(i,m):
 d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
 return -sum(d[j-1]*C(i+1-j,m-i+1) for j in range(1,5))
def J(s,m):
 n=m-s
 return -C(3,s-1)*C(s,n)-C(6,s-1)*C(s-1,n)+C(8,s-2)*C(s-2,n)
def run(Q=32):
 d=[];a=[]
 for m in range(Q+1):
  d.append(trim([int(m==0)]+[-K(i,m) for i in range(1,13)]))
  a.append(trim([int(m<=1)]+[J(s,m) for s in range(1,11)]))
  assert len(a[-1])-1<=m and (m==0 or len(d[-1])-1<=m+1)
 assert d[0]==[1,-2] and d[1]==[0,-3,1]
 z=[[1]]
 for _ in range(Q):z.append(mul(z[-1],d[0]))
 P=[]
 for q in range(Q+1):
  p=mul(z[q],a[q])
  for m in range(1,q+1):p=plus(p,[-v for v in mul(mul(d[m],z[m-1]),P[q-m])])
  assert len(p)-1<=2*q
  assert sum((F(v,2**i) for i,v in enumerate(p)),F(0))==F(5,4)**q
  P.append(p)
 kpol=[trim([K(i,m) for m in range(2*i+1)]) for i in range(1,13)]
 B=[[1,1]]
 for s in range(1,2*Q+1):
  row=trim([J(s,m) for m in range(2*s+3)])
  for i in range(1,min(s,12)+1):row=plus(row,mul(kpol[i-1],B[s-i]))
  B.append(row)
 n_b=n_d=0
 for q in range(Q+1):
  p=P[q]
  for s in range(2*Q+1):
   value=sum(p[i]*2**(s-i)*C(q+s-i,q) for i in range(min(s,len(p)-1)+1))
   assert value==get(B[s],q),(s,q)
   n_b+=1
  for r in range(q+1):
   k=q-r
   lhs=sum((-1)**(k-v)*C(k,v)*2**(q-v)*get(B[q+v],q) for v in range(k+1))
   rhs=F(0)
   for j in range(r+1):
    gy=(-1)**j*sum((F(p[i]*C(i,j),2**i) for i in range(j,len(p))),F(0))
    rhs+=4**q*gy*C(2*q-j,r-j)
   assert rhs==lhs,(q,r,lhs,rhs)
   n_d+=1
 n_top=0
 for r in range(min(Q//2,16)+1):
  h=[]
  for u in range(r+1):
   q=r+u
   h.append(F(sum((-1)**(u-v)*C(u,v)*2**(q-v)*get(B[q+v],q) for v in range(u+1)),5**u))
  assert sum((-1)**(r-u)*C(r,u)*h[u] for u in range(r+1))==6**r
  n_top+=1
 negatives=sum(v<0 for s,row in enumerate(B) for v in row[s+1:])
 return {'status':'PASS','q_max':Q,'B_rows':2*Q+1,'rational_recursion_degree_checks':Q+1,
   'P_at_half_checks':Q+1,'B_coefficient_crosschecks':n_b,
   'D_extraction_crosschecks':n_d,'top_difference_checks':n_top,
   'outside_triangle_negative_terms_preserved':negatives,'arithmetic':'integer/Fraction exact',
   'scope':'finite crosscheck; universal proof in R337_PROOF.zh-CN.md'}
if __name__=='__main__':
 Q=int(sys.argv[1]) if len(sys.argv)>1 else 32
 assert 0<=Q<=80
 print(json.dumps(run(Q),sort_keys=True,indent=2))
