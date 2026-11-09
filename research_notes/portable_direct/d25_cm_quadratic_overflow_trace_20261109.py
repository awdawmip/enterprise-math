#!/usr/bin/env python3
"""D25 uniform Legendre reflection and exact CM finite quadratic overflow."""
from math import comb
import json

def add(a,b,m):return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def mul(a,b,m):return ((a[0]*b[0]+2*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def power(a,n,m):
 z=(1,0)
 while n:
  if n&1:z=mul(z,a,m)
  a=mul(a,a,m);n//=2
 return z
def evaluate(poly,x,m):
 z=(0,0)
 for c in poly[::-1]:z=add(mul(z,x,m),(c,0),m)
 return z
def run(p):
 mod=p*p
 f=[1];g=[1]
 for k in range(p-1):
  f.append(f[-1]*(8*k+1)*(8*k+3)*pow(64*(k+1)**2,-1,mod)%mod)
  g.append(g[-1]*(4*k+1)*(4*k+3)*pow(16*(k+1)**2,-1,mod)%mod)
 q=(p-1)//4 if p%4==1 else (p-3)//4
 N=3*q if p%4==1 else 3*q+2
 def leg(n):return [(-1)**k*comb(n,k)*comb(n+k,k)%mod for k in range(n+1)]
 A,B=leg(q),leg(N)
 assert all((4*g[k]-3*(A[k] if k<len(A) else 0)-(B[k] if k<len(B) else 0))%mod==0 for k in range(p))
 sign=(-1)**q
 assert all(((-1)**k*sum(g[j]*comb(j,k) for j in range(k,p))-sign*g[k])%mod==0 for k in range(p))
 if p%24!=13:return {"p":p,"reflection_sign":sign,"PASS":True}
 s=(3*pow(6,-1,mod)%mod,-2*pow(6,-1,mod)%mod)
 z=pow(9,-1,mod)
 F=sum(c*pow(z,k,mod) for k,c in enumerate(f))%mod
 raw=0;v=1
 for k in range(p):
  if k:
   v=v*(8*k-7)*(8*k-5)*pow(64*k*k,-1,mod)%mod
  raw=(raw+v*pow(z,k,mod))%mod
 assert raw==F
 G=evaluate(g,s,mod)
 edge=[0]*(p-1)
 for k in range(1,p):
  t=f[k]*pow(4,k,mod)%mod
  for j in range(max(0,p-k),k+1):
   n=k+j-p
   if n<p-1:edge[n]=(edge[n]+t*(-1 if j%2 else 1)*comb(k,j))%mod
 E=evaluate(edge,s,mod)
 V=mul(power(s,p,mod),E,mod)
 assert add(G,V,mod)==(F,0)
 assert G[0]==0 and all(x%p==0 for x in (*G,*E,*V))
 u,w=E[0]//p,E[1]//p
 assert (F//p-(3*u+4*w)*pow(6,-1,p))%p==0
 return {"p":p,"G":G,"E":E,"s_p_E":V,"u_v":[u,w],"F":F,"PASS":True}
if __name__=="__main__":
 print(json.dumps([run(p) for p in [5,7,11,13,17,19,29,37,41,43,61,73,109,157,181,373]],indent=2))
