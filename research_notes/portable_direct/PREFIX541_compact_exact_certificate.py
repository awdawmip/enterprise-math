#!/usr/bin/env python3
"""PREFIX-541 exact BRC/gate support, scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from collections import Counter,defaultdict
import json
S=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*x for x in S[a] if x!=abs(c))
P=tuple((a,p,e*x) for a in range(4) for x in S[a] for e in (-1,1) for p in near(a,e*x))
IX={s:i for i,s in enumerate(P)}
def nxt(i):
 a,p,c=P[i];b=next(b for b in range(4) if b!=a and abs(c) in S[b]);return tuple(IX[x] for x in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(nxt(i) for i in range(48));T=IX[(0,1,-3)]
def sig(i):return (1 if P[i][2]>0 else -1) if abs(P[i][2])==1 else 0
def ep(i):return abs(sig(i))
def tau(r,i,j):
 n=ep(i)+ep(j)-abs(sig(j)-r)+abs(sig(i)-r)
 assert n%2==0 and n//2 in (0,1)
 return n//2
assert len(P)==48 and len(IX)==48 and all(len(set(js))==3 for js in N) and T not in N[T]
def G(v):return [max(int(b and bit and j==T)+v[2*j+bit] for j in N[i] for bit in (0,1)) for i in range(48) for b in (0,1)]
v=[0]*96;V=[v]
for _ in range(5):v=G(v);V.append(v)
assert all(V[5][k]==V[1][k]+1 for k in range(96))
base=[tuple(V[d][2*i] for d in range(1,5)) for i in range(48)]
assert Counter(base)=={(0,0,0,0):6,(0,0,0,1):15,(0,0,1,1):18,(0,1,1,1):9}
def H(i,d):
 if not d:return 0
 k,b=divmod(d-1,4);return k+base[i][b]
def M(i,d):
 if sig(i):
  k,b=divmod(d,6);return 2*k+int(b in (4,5))
 k,b=divmod(d,3);return k+int(b==2 and any(ep(j) for j in N[i]))
def trop(r,f):
 out=[]
 for i in range(48):
  for b in (0,1):
   row={}
   for j in N[i]:
    x=tau(r,i,j)
    for bit in (0,1):
     y=int(b and bit and j==T)
     for p,h in f[2*j+bit].items():row[p+x]=max(row.get(p+x,-1),h+y)
   out.append(row)
 return out
L=24; profiles=[[None]*(L+1) for _ in range(48)]
for r in (-1,0,1):
 f=[{0:0} for _ in range(96)]
 for d in range(L+1):
  for i in range(48):
   if sig(i)==r:
    profiles[i][d]=dict(f[2*i]);assert max(f[2*i].values())==H(i,d) and max(f[2*i])==M(i,d)
  if d<L:f=trop(r,f)
rows=[{'d':d,'old':0,'root_gate':0,'exact':0} for d in range(L+1)]
def slots(m,h):return sum(max(0,m-x+1) for x in range(h+1))
for root in range(48):
 states={(root,0,0,0):1};r=sig(root)
 for d in range(L+1):
  hist=defaultdict(int)
  for (i,b,K,h),n in states.items():
   delta=abs(sig(i)-r);assert K>=delta and (K-delta)%2==0
   hist[(K-delta)//2,h]+=n
  assert sum(hist.values())==6**d
  heights={}
  for p,h in hist:heights[p]=max(heights.get(p,-1),h)
  assert heights==profiles[root][d]
  assert set(hist)=={(p,h) for p,m in heights.items() for h in range(m+1)}
  x=rows[d];x['old']+=slots(M(root,d),(d+2)//4);x['root_gate']+=slots(M(root,d),H(root,d));x['exact']+=len(hist)
  if d==L:break
  new=defaultdict(int)
  for (i,b,K,h),n in states.items():
   for j in N[i]:
    new[j,0,K+ep(i)+ep(j),h]+=n
    new[j,1,K+ep(i)+ep(j),h+int(b and j==T)]+=n
  states=new
assert (rows[24]['old'],rows[24]['root_gate'],rows[24]['exact'])==(2016,1998,1876)
assert [(rows[k]['old'],rows[k]['root_gate'],rows[k]['exact']) for k in (20,23)]==[(1440,1426,1352),(1848,1801,1709)]
report={'status':'ALL_CHECKS_PASS','pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','maxplus_identity':'G^5(0_96)=G(0_96)+1_96','classes':{str(k):v for k,v in Counter(base).items()},'raw_endpoint_vs_tropical_48_root_25_depth':1200,'by_depth':rows,'review':'AUTHOR_PROVED/EXACT_INTEGER_CHECKED/UNREVIEWED/NOT_ADMITTED'}
with open('PREFIX541_EXACT_EXECUTION.json','w') as file:json.dump(report,file,indent=2)
print('ALL_CHECKS_PASS',report['raw_endpoint_vs_tropical_48_root_25_depth'],rows[24])
