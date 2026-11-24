"""Deterministic Lucas/trial-division proof; standard library only."""
from math import gcd, isqrt, prod
from pathlib import Path
import json

data=json.loads(Path(__file__).with_name("order_primes_lucas.json").read_text())
roots={int(d):ps for d,ps in data["roots"].items()}
cert={int(n):x for n,x in data["certificates"].items()}

def distinct_factors(n):
 result=[]
 for p in range(2,isqrt(n)+1):
  if n%p: continue
  result.append(p)
  while n%p==0: n//=p
  if n==1: break
 if n>1: result.append(n)
 return result

def prime(n):
 if n <= 2**32:
  return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
 item=cert[n]
 a=item["witness"]
 fs={int(q):k for q,k in item["factorization"].items()}
 return (all(1<q<n and k>0 and prime(q) for q,k in fs.items()) and
         prod(q**k for q,k in fs.items())==n-1 and pow(a,n-1,n)==1 and
         all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q in fs))

phi={315:25435999094089869005186806358949569337458761,
     630:19862216791445343941138167955238148374298681,
     1260:489673978102803602494885320443690671105166192206511931497551144959435000420664929685441}
for d,ps in roots.items():
 fs=distinct_factors(d)
 assert all(prime(p) and pow(2,d,p)==1 and all(pow(2,d//q,p)!=1 for q in fs) for p in ps)
 assert phi[d]%prod(ps)==0
 assert (2**d-1)%phi[d]==0 and all(gcd(2**(d//q)-1,phi[d])==1 for q in fs)
 assert all(d//gcd(d,36)==35 for p in ps)
 print(d,ps, "verified", "cofactor",phi[d]//prod(ps))

def kth_root_floor(n,k):
 lo,hi=1,1<<((n.bit_length()+k-1)//k)
 while lo<hi:
  mid=(lo+hi+1)//2
  if mid**k<=n: lo=mid
  else: hi=mid-1
 return lo

C=phi[1260]//prod(roots[1260])
assert gcd(3,C)==1 and pow(3,C-1,C)!=1
assert all(kth_root_floor(C,k)**k!=C for k in range(2,C.bit_length()))
assert gcd(C,prod(roots[1260]))==1
print("Order-1260 cofactor is composite and not a perfect power; at least two new distinct prime factors.")
