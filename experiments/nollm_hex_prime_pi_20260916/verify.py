"""Independent standard-library verification of strict-hex prime/pi observations.
Run: python verify.py
Counts use only integer arithmetic. No network or production source changes.
"""
from collections import Counter
from math import gcd,isqrt,prod,sqrt
import json,random

def height(q,r):return max(abs(2*q+r),abs(q+2*r),abs(q-r))
def norm(q,r):return q*q+q*r+r*r
def row(q,s):return max(-s-2*q,-((s+q)//2),q-s),min(s-2*q,(s-q)//2,q+s)
def count(s):return s*s+s+1-2*(s%3==1)
def points(s):
 for q in range(-s,s+1):
  lo,hi=row(q,s)
  for r in range(lo,hi+1):yield q,r

def mu_sieve(n):
 mu=[0]*(n+1);mu[1]=1;ps=[];bad=bytearray(n+1)
 for x in range(2,n+1):
  if not bad[x]:ps.append(x);mu[x]=-1
  for p in ps:
   y=x*p
   if y>n:break
   bad[y]=1
   if x%p==0:mu[y]=0;break
   mu[y]=-mu[x]
 return mu

def visible(s,mu):return sum(mu[d]*(count(s//d)-1) for d in range(1,s//2+1))
def disk(s):
 total=0
 lim=isqrt(s*s//3)
 for q in range(-lim,lim+1):
  j=isqrt(s*s-3*q*q)
  total+=max(0,(j-q)//2+(q+j)//2+1)
 return total

def primes_to(n):
 flags=bytearray(b'\1')*(n+1);flags[:2]=b'\0\0'
 for p in range(2,isqrt(n)+1):
  if flags[p]:flags[p*p::p]=b'\0'*((n-p*p)//p+1)
 return [p for p in range(2,n+1) if flags[p]]
def factors(n,ps):
 out=[]
 for p in ps:
  if p*p>n:break
  e=0
  while n%p==0:n//=p;e+=1
  if e:out.append([p,e])
 if n>1:out.append([n,1])
 return out

def decode(q,r,k):
 n=0
 for j in range(k):
  a,b=q%2,r%2;n+=(a+2*b)*4**j
  u,v=(q-a)//2,(r-b)//2;q,r=u+v,-u
 return n

def boundary(k):
 m=1<<k;bins={}
 for q0 in range((m+2)//3,2*m//3+1):
  q,r=q0,m-2*q0
  for _ in range(6):
   bins.setdefault(decode(q,r,k),set()).add((q,r));q,r=-r,q+r
 assert len(bins)==m-1 and all(len(v)==2 for v in bins.values())
 return bins

def main():
 mu=mu_sieve(65535);ps=primes_to(65536);capacity=[];pi_rows=[];boundary_rows=[];rings=[]
 for s in range(256):assert sum(hi-lo+1 for q in range(-s,s+1) for lo,hi in [row(q,s)] if hi>=lo)==count(s)
 for s in range(65):
  p=list(points(s));assert sum(gcd(q,r)==1 for q,r in p)==visible(s,mu)
  assert sum(4*norm(q,r)<=s*s for q,r in p)==disk(s)
 for t in range(1,9):
  m=4**t;K=m*m-m+1;fs=factors(K,ps);assert prod(p**e for p,e in fs)==K
  for p,e in fs:
   assert p%12==1 and factors(p,ps)==[[p,1]]
   x=pow(2,t,p);assert pow(x,12,p)==1 and all(pow(x,d,p)!=1 for d in (1,2,3,4,6))
  capacity.append([m,K,fs])
 for m in (256,1024,4096,16384,65536):
  s=m-1;K=count(s);V=visible(s,mu);D=disk(s)
  pi_rows.append([m,K,V,D,sqrt(6*(K-1)/V)])
  b=boundary(m.bit_length()-1);primitive=odd=prime_labels=0;mods=Counter()
  for n,pair in b.items():
   a,c=sorted(pair);da,dc=gcd(*a),gcd(*c);Qa,Qc=norm(*a),norm(*c)
   assert da==dc and Qa==Qc and da&(da-1)==0 and m%da==0 and Qa%3==1
   assert height(*a)==height(*c)==m
   primitive+=da==1;odd+=n%2
   if factors(n,ps)==[[n,1]]:prime_labels+=1;mods[n%12]+=1
   if m<=4096:
    fs=factors(Qa,ps);assert all(p==2 or p%3==1 for p,e in fs)
    if fs==[[Qa,1]]:assert Qa%12==7
  assert primitive==(m-4)//2 and odd==(m-4)//3
  boundary_rows.append([m,len(b),primitive,odd,prime_labels,dict(sorted(mods.items()))])
 for m in (4,16,64,256,1024):
  K=m*m-m+1;s=m-1;inv=[None]*K;V=D=0
  for q,r in points(s):
   z=(q+m*r)%K;assert inv[z] is None;inv[z]=(q,r)
   V+=gcd(q,r)==1;D+=4*norm(q,r)<=s*s
  assert all(x is not None for x in inv)
  assert V==visible(s,mu) and D==disk(s)
  rng=random.Random(m)
  pairs=((i,j) for i in range(K) for j in range(K)) if m<=16 else ((rng.randrange(K),rng.randrange(K)) for _ in range(10000))
  tests=0
  for i,j in pairs:
   q,r=inv[i];u,v=inv[j];aq,ar=q*u-r*v,q*v+r*u+r*v
   assert (aq+m*ar)%K==i*j%K
   tq,tr=inv[i*j%K];dq,dr=aq-tq,ar-tr
   assert ((m-1)*dq-dr)%K==0 and (dq+m*dr)%K==0
   tests+=1
  rings.append([m,K,tests])
 result={'schema':'NOLLM_HEX_PRIME_PI_INDEPENDENT_V1','capacity':capacity,'pi_counts_m_K_V_D_pi_estimate':pi_rows,
         'boundary_m_count_primitive_odd_prime_residues':boundary_rows,'ring_m_K_pairs':rings,
         'assertions':'PASS','pi_used_in_point_selection':False,'ring_readout_changes_original_n_labels':True,'Actions_used':False}
 print(json.dumps(result,ensure_ascii=False,indent=2))
 return result
if __name__=='__main__':main()
