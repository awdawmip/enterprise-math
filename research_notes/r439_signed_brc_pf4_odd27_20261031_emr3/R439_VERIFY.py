"""R439 exact independent input and lower-minor verifier; 4x4 exhaust by C++.
Uses only Python standard-library integer arithmetic."""
from math import comb,gcd
from functools import reduce
from itertools import permutations
from pathlib import Path
import json,re
R=27; N=25
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def signed(r,s):
 if s<2 or s>r:return 0
 return comb(r+s,2*s)*sum(comb(r-s,j)*(C(2*s,r-2*j)-C(2*s,r-2*j-1)) for j in range(r-s+1))
def polynomial(r,s):
 p=[1]
 for e,count in [(1,2*s),(2,r-s)]:
  for _ in range(count):
   t=[0]*(len(p)+e)
   for i,v in enumerate(p):t[i]+=v;t[i+e]+=v
   p=t
 return comb(r+s,2*s)*(p[r]-p[r-1])
def catalan(r,s):
 k=(r-1)//2
 return comb(r+s,2*s)*sum(C(s-1,2*j)*4**j*comb(2*(k-j),k-j)//(k-j+1) for j in range(k+1))
raw=[signed(R,R-h) for h in range(N+1)]
assert raw==[polynomial(R,R-h) for h in range(N+1)]
assert raw==[catalan(R,R-h) for h in range(N+1)]
G=reduce(gcd,raw); A=[v//G for v in raw]
assert G==116 and all(v>0 for v in A) and max(A)<2**60
def val(h):return A[h] if 0<=h<=N else 0
def det(m):
 a=[list(x) for x in m];den=1;sgn=1;n=len(a)
 for k in range(n-1):
  if a[k][k]==0:
   j=next((t for t in range(k+1,n) if a[t][k]),None)
   if j is None:return 0
   a[k],a[j]=a[j],a[k];sgn=-sgn
  p=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=a[i][j]*p-a[i][k]*a[k][j]
    assert num%den==0
    a[i][j]=num//den
   a[i][k]=0
  den=p
 return sgn*a[-1][-1]
def d3(u1,u2,v0,v1,v2):
 a,b,c=val(v0),val(v1),val(v2)
 d,e,f=val(v0-u1),val(v1-u1),val(v2-u1)
 g,h,i=val(v0-u2),val(v1-u2),val(v2-u2)
 return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
counts={1:len(A),2:0,3:0}
for u1 in range(1,N+1):
 for v0 in range(N+1):
  for v1 in range(max(v0+1,u1),u1+N+1):
   assert val(v0)*val(v1-u1)-val(v1)*val(v0-u1)>0
   counts[2]+=1
for u1 in range(1,N+1):
 for u2 in range(u1+1,u1+N+1):
  for v0 in range(N+1):
   for v1 in range(max(v0+1,u1),u1+N+1):
    for v2 in range(max(v1+1,u2),u2+N+1):
     assert d3(u1,u2,v0,v1,v2)>0
     counts[3]+=1
assert counts=={1:26,2:13975,3:7280780}
rows=range(5);cols=range(24,29)
m5=[[signed(R,R-(v-u)) for v in cols] for u in rows]
E=det(m5)
control=0
for p in permutations(range(5)):
 term=(-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
 for i,j in enumerate(p):term*=m5[i][j]
 control+=term
assert E==control==-4879066184369172962162267144222813070669793907904000000000
assert det([[signed(6,6-(v-u)) for v in (1,4,5,6)] for u in range(4)])==-4117994496
def ncols(u1,u2,u3):
 m=u3+N; ways=[int(j<=N) for j in range(m+1)]
 for lower in [u1,u2,u3]:
  prefix=[];run=0
  for z in ways:run+=z;prefix.append(run)
  nxt=[0]*(m+1)
  for j in range(lower,lower+N+1):nxt[j]=prefix[j-1] if j>0 else 0
  ways=nxt
 return sum(ways)
dp={}
for u1 in range(1,N+1):
 dp[u1]=sum(ncols(u1,u2,u3) for u2 in range(u1+1,u1+N+1) for u3 in range(u2+1,u2+N+1))
parts=[(1,5,503412499),(6,7,247320000),(8,10,414725834),(11,13,461076642),(14,16,499802641),(17,19,530250269),(20,22,551907471),(23,25,564410989)]
assert all(sum(dp[i] for i in range(a,b+1))==count for a,b,count in parts)
assert sum(z[2] for z in parts)==3772906345
spot=0
for u1 in (1,2,3,5,8,13,19,25):
 for u2 in (u1+1,u1+3,u1+7,u1+N):
  for u3 in (u2+1,u2+2,u2+N):
   u=(0,u1,u2,u3)
   for v0 in (0,1,6,13,N):
    for g1 in (0,1,3,7,N):
     v1=max(v0+1,u1)+g1
     if v1>u1+N:continue
     for g2 in (0,1,3,7,N):
      v2=max(v1+1,u2)+g2
      if v2>u2+N:continue
      for g3 in (0,1,3,7,N):
       v3=max(v2+1,u3)+g3
       if v3>u3+N:continue
       assert det([[val(v-r) for v in (v0,v1,v2,v3)]for r in u])>0
       spot+=1
assert spot==36188
for a,b,count in parts:
 f=Path(__file__).parent / f"R439_FAST_{a}_{b}.txt"
 if f.is_file():
  t=f.read_text()
  exp=f"R439_PF4_R27_CERTIFIED u1={a}..{b} pos={count} zero=0 neg=0 total={count} exact_fallback=0 cutoff=1e-15 mant=64"
  assert t.strip()==exp
print("R439_EXACT_PASS", "three_way",len(raw),"lower",counts,"full_four",3772906345,"spot",spot,"E27",E)
