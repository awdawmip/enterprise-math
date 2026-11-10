#!/usr/bin/env python3
"""Exact model finite checks. Not a native H0/B0 run."""
from collections import Counter

def s(x,p): return x[0]%p,-x[1]%p
def add(x,y,p):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def sub(x,y,p):return ((x[0]-y[0])%p,(x[1]-y[1])%p)
def mul(x,y,m):return ((x[0]*y[0]+2*x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m)
def matmul(a,b,m):return tuple(tuple(add(mul(a[i][0],b[0][j],m),mul(a[i][1],b[1][j],m),m) for j in range(2)) for i in range(2))
def sigmamat(a,p):return tuple(tuple(s(a[i][j],p*p) for j in range(2)) for i in range(2))
def f(p,b,d):
 m=p*p;sd=s(d,p)
 return (((-p*sd[0]%m,-p*sd[1]%m),((1+p*b[0])%m,p*b[1]%m)),((p,0),(p*d[0]%m,p*d[1]%m)))
def gauge(p,u,v,w,z,inv=False):
 m=p*p;t=-1 if inv else 1
 return ((((1+t*p*u[0])%m,t*p*u[1]%m),(t*p*v[0]%m,t*p*v[1]%m)),((t*p*w[0]%m,t*p*w[1]%m),((1+t*p*z[0])%m,t*p*z[1]%m)))
def action(p,b,d,u,v,w,z):
 m=p*p
 g=gauge(p,u,v,w,z);gi=gauge(p,u,v,w,z,True)
 got=matmul(matmul(gi,f(p,b,d),m),sigmamat(g,p),m)
 newb=add(b,sub(s(z,p),u,p),p);newd=sub(d,w,p)
 assert got==f(p,newb,newd)
 return newb,newd
def full(p):
 zero=(0,0);counterL=Counter();counterSL=Counter()
 for da in range(p):
  for db in range(p):
   d=(da,db)
   for ba in range(p):
    for bb in range(p):
     b=(ba,bb);counterL[d]+=1;counterSL[(d,bb)]+=1
     z=(ba*pow(2,-1,p)%p,0);u=((-z[0])%p,0)
     assert action(p,(0,bb),d,u,zero,zero,z)==(b,d)
     assert action(p,zero,d,sub(zero,b,p),zero,zero,zero)==(b,d)
 assert len(counterL)==p*p and set(counterL.values())=={p*p}
 assert len(counterSL)==p**3 and set(counterSL.values())=={p}
 print('p',p,'fixed',p**4,'line_orbits',len(counterL),'oriented_line_orbits',len(counterSL),'PASS')
def sample(p):
 z=(pow(2,-1,p),0);zero=(0,0);t=(0,1)
 f0=f(p,zero,zero)
 assert matmul(f0,sigmamat(f0,p),p*p)==(((p,0),(0,0)),((0,0),(p,0)))
 assert action(p,zero,zero,sub(zero,z,p),zero,zero,z)==((1,0),zero)
 assert action(p,zero,zero,zero,zero,sub(zero,t,p),zero)==(zero,t)
 print('p',p,'modulus',p*p,'gauge witnesses PASS')
if __name__=='__main__':
 full(5)
 for prime in (13,19,373): sample(prime)
 print('NATIVE_H0B0_EXECUTED=False')
