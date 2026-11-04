"""D25 finite checks: CM-24 two-isogeny Frobenius and split quadratic-form norm."""
from math import isqrt
Q=(1,-140,294,-140,1)

def mul(a,b,p):
 r=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]=(r[i+j]+x*y)%p
 while len(r)>4:
  z=r.pop(); k=len(r)-4
  for i in range(4):r[k+i]=(r[k+i]-z*Q[i])%p
 return tuple((r+[0]*4)[:4])

def powq(a,n,p):
 r=(1,0,0,0)
 while n:
  if n&1:r=mul(r,a,p)
  a=mul(a,a,p);n>>=1
 return r

def primes(n):
 s=bytearray([1])*(n+1);s[:2]=b'\0\0'
 for k in range(2,isqrt(n)+1):
  if s[k]:s[k*k:n+1:k]=bytes((n-k*k)//k+1)
 return [p for p in range(5,n+1) if s[p]]

def representation(p):
 for a in range(1,isqrt(p//2)+1,2):
  r=p-2*a*a
  if r>=0 and r%3==0:
   b=isqrt(r//3)
   if b%2 and b*b*3==r:return a,b
 return None

counts=[0,0,0]
for p in primes(20000):
 if p%8!=5:continue
 counts[0]+=1
 y=(140%p,-293%p,140%p,-1%p)
 y_frob=tuple(((140-y[i]) if i==0 else -y[i])%p for i in range(4))
 assert powq(y,p,p)==y_frob
 J=tuple((144*247*y[i]-(144*502 if i==0 else 0))%p for i in range(4))
 J2=tuple(((4834944 if i==0 else 0)-J[i])%p for i in range(4))
 assert powq(J,p,p)==J2
 assert mul(J,J2,p)==(14670139392%p,0,0,0)
 r=representation(p)
 if p%24==5:
  counts[1]+=1;assert r and 2*r[0]**2+3*r[1]**2==p
 else:
  counts[2]+=1;assert p%24==13 and r is None
assert counts==[569,281,288],counts
print('PASS primes=569 split_norm=281 inert=288')
