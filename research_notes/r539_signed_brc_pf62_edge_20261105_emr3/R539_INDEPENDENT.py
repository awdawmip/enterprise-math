"""R539 independent Python/Sympy exact verification (author-side)."""
import json, math, functools
from sympy import Matrix
m=62
@functools.lru_cache(None)
def c(n,j): return math.comb(n,j) if 0<=j<=n else 0
@functools.lru_cache(None)
def cat(k): return c(2*k,k)//(k+1)
@functools.lru_cache(None)
def H(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 return c(r+t,2*t)*sum(c(r-t,q)*(c(2*t,r-2*q)-c(2*t,r-2*q-1)) for q in range(r-t+1))
@functools.lru_cache(None)
def B(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 return c(r+t,2*t)*sum(c(t-1,2*q)*4**q*cat(k-q) for q in range(min((t-1)//2,k)+1))
def D(k):
 p=H(k,2); d=[1]
 for n in range(1,m+1):
  s=0;pow=1
  for a in range(1,n+1):
   s+=(-1 if a%2==0 else 1)*H(k,a+2)*pow*d[n-a];pow*=p
  d.append(s)
 return d[-1]
def differences(a):
 out=[];v=list(a)
 while v:
  out.append(v[0]);v=[v[i+1]-v[i] for i in range(len(v)-1)]
 return out
def N(d,k,b):return sum(x*c(k-b,j) for j,x in enumerate(d))
e=json.load(open("R539_EVIDENCE.json"))
delta=list(map(int,e['delta_at_k1']));eps=list(map(int,e['tail_newton']));L=int(e['L']);o=e['tail_shift_origin_k']
assert len(delta)==len(eps)==124 and o==74 and all(x<0 for x in eps)
assert differences([N(delta,o+j,1) for j in range(124)])==eps
ks=[1,5,6,7,10,11,12,13,72,73,74,75,100,180,374]
for k in ks:
 G=(k*(k+1)*(2*k+1)*(2*k+3))**m*(k+2)
 assert L*D(k)==cat(k)**m*G*N(delta,k,1)
 for t in range(2,m+3):assert H(k,t)==B(k,t)
for k in [6,7,11,12]:
 raw=Matrix(m,m,lambda i,j:H(k,3+i-j)).det(method='berkowitz')
 assert int(raw)==D(k)
print("R539_INDEPENDENT_PASS: 4 exact Berkowitz, 15 recurrence/certificate, 945 coefficient, 124 shifted Newton checks")
