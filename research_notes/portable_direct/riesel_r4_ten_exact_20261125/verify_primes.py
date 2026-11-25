"""Deterministic exact-order and prime certificate verification (stdlib only)."""
import json
from math import gcd,isqrt,prod
from functools import cache
G=json.load(open('inventory.json'))
D=json.load(open('lucas.json'))
P={int(d):list(map(int,qs)) for d,qs in D['factors'].items()}
C={int(q):r for q,r in D['certificates'].items()}
@cache
def pf(d):
 z=[]
 for i in range(2,isqrt(d)+1):
  if d%i==0:
   z.append(i)
   while d%i==0:d//=i
 return z+([d] if d>1 else [])
def quad_pow(x,k,t,q):
 a,b=1,0;u,v=x
 while k:
  if k&1:a,b=(a*u+t*b*v)%q,(a*v+b*u)%q
  u,v=(u*u+t*v*v)%q,2*u*v%q;k//=2
 return a,b
@cache
def prime(q):
 assert q>=2
 if q<=10**7:return all(q%j for j in range(2,isqrt(q)+1))
 cert=C[q];mode=cert['mode'];assert mode in (-1,1)
 fs={int(p):e for p,e in cert['factors'].items()}
 F=prod(p**e for p,e in fs.items())
 assert all(p<q and e>=1 and prime(p) for p,e in fs.items())
 assert (q+mode)%F==0 and F>isqrt(q)+1
 ws=cert['witness']
 if mode==1:
  t=next(iter(ws.values()))[0]
  assert gcd(t,q)==1 and all(w[0]==t for w in ws.values())
 for p in fs:
  w=ws[str(p)]
  if mode==-1:
   assert pow(w,q-1,q)==1 and gcd(pow(w,(q-1)//p,q)-1,q)==1
  else:
   t,a,b=w
   assert (a*a-t*b*b)%q==1
   assert quad_pow((a,b),q+1,t,q)==(1,0)
   x,y=quad_pow((a,b),(q+1)//p,t,q)
   assert gcd(gcd(x-1,y),q)==1
 return True
for hs in G.values():
 for d,c in hs:
  primes=P[d]; assert prod(primes)==int(c)
  for p in primes:
   assert prime(p)
   assert pow(2,d,p)==1 and all(pow(2,d//q,p)!=1 for q in pf(d))
print(f'{len({p for qs in P.values() for p in qs})} distinct primes, {prime.cache_info().currsize} verification nodes; {sum(c["mode"]==1 for c in C.values())} plus-one certificates')
