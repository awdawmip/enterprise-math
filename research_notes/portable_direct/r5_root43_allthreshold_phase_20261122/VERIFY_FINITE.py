#!/usr/bin/env python3
"""R5 global exact first jets using 3 disjoint failure blocks, integer cyclic rings."""
import sys,time
from math import lcm
import sympy as sp

PRICES=list(range(214,315))
S=[set(range(214,219)),set([214,216,217,218,219,220,221]),set(range(215,222)),set(range(223,291)),set(range(296,313))]
DSET=[7,9,11,13,17,19,23,25,27,29,31,32,37,43]
L=229746052653717600
CAP=int(sys.argv[1]) if len(sys.argv)>1 else 4
x=sp.symbols('x')

class J:
 def __init__(self,d):
  self.d=d; self.z=(0,)*d; self.o=(1,)+(0,)*(d-1)
  phi=sp.Poly(sp.cyclotomic_poly(d,x),x,domain=sp.ZZ)
  self.phi=phi; self.phideg=phi.degree()
 def shift(self,a,k):
  d=self.d;k%=d
  return a[-k:]+a[:-k] if k else a
 def add(self,a,b):return tuple(u+v for u,v in zip(a,b))
 def sub(self,a,b):return tuple(u-v for u,v in zip(a,b))
 def mul(self,a,b):
  z=[0]*self.d
  for i,u in enumerate(a):
   if u:
    for j,v in enumerate(b):
     if v:z[(i+j)%self.d]+=u*v
  return tuple(z)
 def jadd(self,A,B):return (self.add(A[0],B[0]), self.add(A[1],B[1]))
 def jsub(self,A,B):return (self.sub(A[0],B[0]), self.sub(A[1],B[1]))
 def jmul(self,A,B):return (self.mul(A[0],B[0]),self.add(self.mul(A[1],B[0]),self.mul(A[0],B[1])))
 def jmonomial(self,A,k):
  u=self.shift(A[0],k); v=self.shift(A[1],k)
  return (u,self.add(v,tuple(k*t for t in u)))
 def jfactor(self,p):
  u=self.shift(self.o,p);return (self.sub(self.o,u),tuple(-p*t for t in u))
 def jprod(self,prices):
  a=self.jone()
  for p in prices:a=self.jmul(a,self.jfactor(p))
  return a
 def jone(self):return self.o,self.z
 def jzero(self):return self.z,self.z
 def jreduce(self,a):
  p=sp.Poly.from_list(list(a[::-1]),gens=x,domain=sp.ZZ)
  rem=p.rem(self.phi)
  vals=[0]*self.phideg
  for (e,),coef in rem.terms():vals[e]=int(coef)
  return tuple(vals)
 def jetreduce(self,A):return self.jreduce(A[0]),self.jreduce(A[1])
 def q_single(self,prices):
  h=[self.jone()]+[self.jzero() for _ in range(CAP)]
  for p in prices:
   for r in range(1,CAP+1):h[r]=self.jadd(h[r],self.jmonomial(h[r-1],p))
  q=self.jzero()
  for a in h:q=self.jadd(q,a)
  return q
 def event_single(self,prices):return self.jmul(self.q_single(prices),self.jprod(prices))
 def q_intersection(self,I):
  events=list(I)
  union=sorted(set().union(*(S[i] for i in events)))
  zero_key=(0,)*len(events)
  dp={zero_key:self.jone()}
  for p in union:
   affected=[j for j,i in enumerate(events) if p in S[i]]
   nextdp={}
   for counts,V in dp.items():
    limit=min(CAP-counts[j] for j in affected)
    for r in range(limit+1):
     newkey=tuple(c+(r if j in affected else 0) for j,c in enumerate(counts))
     m=self.jmonomial(V,p*r) if r else V
     if newkey in nextdp:nextdp[newkey]=self.jadd(nextdp[newkey],m)
     else:nextdp[newkey]=m
   dp=nextdp
  q=self.jzero()
  for v in dp.values():q=self.jadd(q,v)
  return q,union
 def event_core(self):
  a=self.jzero()
  for mask in range(1,8):
   I=[i for i in range(3) if mask>>i&1]
   q,union=self.q_intersection(I)
   term=self.jmul(q,self.jprod(union))
   a=self.jadd(a,term) if len(I)%2 else self.jsub(a,term)
  return a
 def numerator(self):
  a=self.event_core();b=self.event_single(sorted(S[3]));c=self.event_single(sorted(S[4]));one=self.jone()
  return self.jsub(one, self.jmul(self.jmul(self.jsub(one,a),self.jsub(one,b)),self.jsub(one,c)))

def verify():
 rows=[]; start=time.time()
 for d in DSET:
  r=J(d).jetreduce(J(d).numerator())
  v0,v1=r
  j=0 if any(v0) else 1 if any(v1) else 2
  nd=sum(p%d==0 for p in PRICES)
  coeff=next(((i,x) for i,x in enumerate(r[j]) if x),None) if j<=1 else None
  row=[d,nd,j,nd-j,coeff]
  rows.append(row)
  print('CAP',CAP,'root',d,'row',row,'elapsed',round(time.time()-start,2),flush=True)
 survive=[r[0] for r in rows if r[3]>=3]
 observed=lcm(*survive)
 print('SURVIVE',survive,'LCM',observed)
 assert len(survive)==len(DSET) and observed==L
 print('ALL CHECKS PASS')
 return rows

if __name__=='__main__':verify()
