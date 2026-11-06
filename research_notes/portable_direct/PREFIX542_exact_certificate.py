#!/usr/bin/env python3
"""PREFIX-542 self-contained exact integer certificate, pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from collections import Counter,defaultdict
from math import comb
S=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*x for x in S[a] if x!=abs(c))
P=tuple((a,p,e*x) for a in range(4) for x in S[a] for e in (-1,1) for p in near(a,e*x))
I={v:i for i,v in enumerate(P)}
def successors(i):
 a,p,c=P[i];b=next(b for b in range(4) if b!=a and abs(c) in S[b]);return tuple(I[v] for v in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NX=tuple(successors(i) for i in range(48));T=I[(0,1,-3)]
def sig(i):return (1 if P[i][2]>0 else -1) if abs(P[i][2])==1 else 0
def ep(i):return abs(sig(i))
def tau(r,i,j):
 x=ep(i)+ep(j)-abs(sig(j)-r)+abs(sig(i)-r)
 assert x%2==0 and x//2 in (0,1)
 return x//2
assert len(P)==len(I)==48 and T not in NX[T] and all(len(set(row))==3 for row in NX)

def transform(hist,d):
 out=defaultdict(int)
 for (p,k),n in hist.items():
  assert k<=d//2 and n>0
  for h in range(k+1):out[p,h]+=n*(2**(d-2*k))*comb(k,h)*(3**(k-h))
 return dict(out)

def phase_all(D):
 res=[[None]*(D+1) for _ in range(48)]
 for r in (-1,0,1):
  roots=[i for i in range(48) if sig(i)==r];U=[{(0,0):1} for _ in P]
  for d in range(D+1):
   for i in roots:
    if d==0:res[i][d]={(0,0):1};continue
    row=defaultdict(int)
    for j in NX[i]:
     for (p,k),v in U[j].items():row[p+tau(r,i,j),k]+=v
    assert sum(row.values())==3**d
    res[i][d]=dict(row)
   if d==0 or d==D:continue
   W=[]
   for i in range(48):
    row=defaultdict(int)
    for j in NX[i]:
     for (p,k),v in U[j].items():row[p+tau(r,i,j),k+int(j==T)]+=v
    W.append(dict(row))
   U=W
 return res

BACK=tuple(Counter(ep(i)+2*ep(m)+ep(T) for m in NX[i] if T in NX[m]) for i in range(48))
assert sum(sum(row.values()) for row in BACK)==9
def add(dst,src,dp=0,dh=0,m=1):
 for (p,h),v in src.items():dst[p+dp,h+dh]+=m*v

def rank49_all(D):
 res=[[None]*(D+1) for _ in range(48)]
 for r in (-1,0,1):
  roots=[i for i in range(48) if sig(i)==r]
  F=[{(2-abs(sig(i)-r),0):1} for i in range(48)];G={}
  for d in range(D+1):
   for i in roots:
    z={}
    for (e,h),v in F[i].items():
     assert e>=2 and e%2==0 and v>0
     z[(e-2)//2,h]=v
    res[i][d]=z
   if d==D:break
   W=[]
   for i in range(48):
    out=defaultdict(int)
    for j in NX[i]:add(out,F[j],ep(i)+ep(j),0,2)
    for k,v in BACK[i].items():add(out,G,k,0,v)
    W.append({k:v for k,v in out.items() if v})
   q=defaultdict(int);add(q,F[T],0,1);add(q,F[T],0,0,-1)
   F,G=W,{k:v for k,v in q.items() if v}
 return res

def raw(root,D):
 states={(root,0,0,0):1};res=[];r=sig(root)
 for d in range(D+1):
  hist=defaultdict(int)
  for (i,b,K,h),v in states.items():
   delta=abs(sig(i)-r);assert K>=delta and (K-delta)%2==0
   hist[(K-delta)//2,h]+=v
  assert sum(hist.values())==6**d
  res.append(dict(hist))
  if d==D:break
  W=defaultdict(int)
  for (i,b,K,h),v in states.items():
   for j in NX[i]:
    for bit in (0,1):W[j,bit,K+ep(i)+ep(j),h+int(b and bit and j==T)]+=v
  states=W
 return res

if __name__=='__main__':
 D=24;phase=phase_all(D);ref=rank49_all(D)
 for i in range(48):
  obs=raw(i,D)
  for d in range(D+1):
   expected=transform(phase[i][d],d)
   assert expected==ref[i][d]==obs[d]
   heights={}
   for (p,k),v in phase[i][d].items():heights[p]=max(heights.get(p,-1),k)
   assert set(expected)=={(p,h) for p,k in heights.items() for h in range(k+1)}
 assert sum(len(ref[i][24]) for i in range(48))==1876
 assert len({tuple(sorted(ref[i][24].items())) for i in range(48)})==26
 assert ref[0][6]=={(0,0):14592,(1,0):28800,(1,1):960,(2,0):2176,(2,1):128}
 print('ALL_CHECKS_PASS; 1200 three-way exact integer equalities; d24 terms=1876; classes=26')
