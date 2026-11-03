#!/usr/bin/env python3
"""Original D25 216 finite arithmetic, exact p-adic observer check."""
import json
from math import comb
from pathlib import Path
def primes(n):
 s=bytearray(b'\x01')*(n+1);s[:2]=b'\x00\x00'
 for k in range(2,int(n**0.5)+1):
  if s[k]: s[k*k::k]=b'\x00'*((n-k*k)//k+1)
 return [k for k in range(2,n+1) if s[k]]
def coeffs(p,m):
 a=[1]
 for k in range(p-1):
  a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,m)%m)
 return a
def W(b,t,m):
 v=0;powt=1
 for k,x in enumerate(b):
  v=(v+(6*k+1)*x*powt)%m;powt=powt*t%m
 return v
def valuation(x,p):
 if x==0:return None
 v=0
 while x%p==0:x//=p;v+=1
 return v
def case(p):
 m=p**5;b=coeffs(p,m);C0=sum(b[k]*b[p-1-k] for k in range(p))%m
 assert C0%p**2==0 and C0//p**2%p==10%p
 c=C0//p**2;r=(p-1)//6
 j=sum(k*comb(r,k)*comb(2*r,k)*pow(2,-k,p) for k in range(r+1))%p
 assert j and sum(comb(r,k)*comb(2*r,k)*pow(2,-k,p) for k in range(r+1))%p==0
 D1=sum(k*(6*k+1)*x for k,x in enumerate(b))%m
 D2=sum(k*(k-1)*(6*k+1)*x for k,x in enumerate(b))%m
 assert D1%p==12*j*j%p and D2%p==8*j*j%p
 w0=W(b,1,p**3);rows=[]
 for lam,mu in ((1,0),(1,1),(1,2),(2,3),(3,1)):
  t=1+p*lam+p*p*mu;ct=C0*pow(t,p-1,m)%m
  s=(ct//p**2)*pow(c,-1,p**3)%p**3
  assert s==pow(t,p-1,p**3)
  A=(s-1)//p;L=(-A)%p;M=(L+L*L-(A+L)//p)%p
  assert (L,M)==(lam,mu)
  dw=(W(b,t,p**3)-w0)%p**3
  e=(p*lam*D1+p*p*(mu*D1+lam*lam*D2*pow(2,-1,p**3)))%p**3
  assert dw==e
  alpha=pow(p-1,-1,p**3);v=s-1
  h=(alpha*D1*v+(alpha*(alpha-1)*D1+alpha*alpha*D2)*pow(2,-1,p**3)*v*v)%p**3
  assert h==dw
  assert valuation((ct-C0)%m,p)==3 and valuation(dw,p)==1
  rows.append([lam,mu,A,dw//p])
 t=1+2*p+p*p;u=1+2*p+3*p*p
 ct=C0*pow(t,p-1,m)%m;cu=C0*pow(u,p-1,m)%m
 assert valuation((ct-cu)%m,p)==4
 assert valuation((W(b,t,p**3)-W(b,u,p**3))%p**3,p)==2
 return dict(p=p,j=j,C_div_p2=c%p**3,D1_modp2=D1%p**2,D2_modp=D2%p,lifts=rows)
if __name__=='__main__':
 rows=[case(p) for p in primes(2000) if p>=13 and p%24 in (13,19)]
 assert len(rows)==77
 print(json.dumps(dict(schema='D25_REFLECTION_ISOMETRY_FINITE_CHECK_V1',PASS=True,count=77,selected=[x for x in rows if x['p'] in (13,19,373)]),indent=2))
