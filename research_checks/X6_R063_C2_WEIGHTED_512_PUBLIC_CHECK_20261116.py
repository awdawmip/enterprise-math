#!/usr/bin/env python3
"""512-radius exact C2 weighted BRC oracle; author-side, not frozen native runner."""
import hashlib,itertools,json,math

def d(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def roots(r):
 return {(a,b) for a in range(r+1) if (t:=r*r-a*a)>=0 and (b:=math.isqrt(t))**2==t}
def c2(r):
 s=set()
 for a in range(math.isqrt(r)+1):
  t=r-a*a
  if t>=0 and (b:=math.isqrt(t))**2==t:
   x,y=abs(a*a-b*b),2*a*b;s.update(((x,y),(y,x)))
 return s
def euclid(r):
 s={(r,0),(0,r)}
 for m in range(2,math.isqrt(r)+1):
  for n in range(1,m):
   h=m*m+n*n
   if h>r:break
   if r%h==0 and math.gcd(m,n)==1 and (m-n)%2:
    x,y=r//h*(m*m-n*n),r//h*2*m*n;s.update(((x,y),(y,x)))
 return s
def lift(s):
 v=set()
 for a,b in s:
  for i,j in itertools.combinations(range(6),2):
   for u,w in itertools.product((-1,1),repeat=2):
    z=[0]*6;z[i]=u*a;z[j]=w*b;v.add(tuple(z))
 return v
rows=[];total_missing=0
for r in range(1,513):
 full=roots(r);c=c2(r);assert full==euclid(r) and c<=full
 A=sum(math.comb(a+b,a) for a,b in full)
 C=sum(math.factorial(a+b)//(math.factorial(a)*math.factorial(b)) for a,b in c)
 delta=int((r,0) in c)
 vf,vc=lift(full),lift(c)
 F=60*A-108;K=60*C-108*delta
 assert len(vf)==60*len(full)-108 and len(vc)==60*len(c)-108*delta
 assert F==sum(math.comb(sum(map(abs,z)),max(map(abs,z))) for z in vf)
 assert K==sum(math.comb(sum(map(abs,z)),max(map(abs,z))) for z in vc)
 total_missing+=len(vf-vc)
 rows.append(dict(r=r,N=r*r,nonnegative_roots=len(full),C2_roots=len(c),missing_roots=len(full-c),
  full_chart_BRC=str(A),C2_chart_BRC=str(C),missing_chart_BRC=str(A-C),
  full_signed_pair_endpoints=len(vf),C2_signed_pair_endpoints=len(vc),missing_signed_pair_endpoints=len(vf-vc),
  full_signed_pair_BRC=str(F),C2_signed_pair_BRC=str(K),missing_signed_pair_BRC=str(F-K),
  has_C2_axis=bool(delta),classification=('COMPLETE' if c==full else 'C2_EMPTY' if not c else 'C2_NONEMPTY_INCOMPLETE')))
assert len(rows)==512 and total_missing==31608
assert d(rows)=='a6e827a5e3962b1568d6a8e26101379867e0a410d75c57089aca4f4c8655f9d3'
assert sum(x['nonnegative_roots'] for x in rows)==1820
assert sum(x['C2_roots'] for x in rows)==440
assert sum(x['missing_roots'] for x in rows)==1380
print('PASS_X6_R063_C2_512_WEIGHTED',d(rows))
