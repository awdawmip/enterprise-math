from itertools import combinations
from math import gcd
from functools import reduce,lru_cache
from fractions import Fraction as Q
V=[(1,0,0),(1,3,-1),(4,-4,1),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(6,-1,0),(7,-1,0),(9,-5,1)]
M=[30,51,10,21,58,51,20,3,23,30]; W=[0,3,5,6,7,9]
E=[(17,1,0),(39,0,0),(17,0,1),(22,1,0),(0,1,1),(22,0,1)]
J=list(combinations(range(4),2))
def gaps(v):
 x,y,z=v;h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z);return tuple(abs(h[i]-h[j]) for i,j in J)
G=list(map(gaps,V)); MASK=[30,51,42,21,58,51,20,7,23,30]
T=sorted({(j,g) for i in W for j,g in enumerate(G[i]) if g and MASK[i]>>j&1})
H=sorted({(j,g) for i in range(10) for j,g in enumerate(G[i]) if g and M[i]>>j&1})
def line(a,b,k=1,l=1):
 j,g=a;h,f=b;return tuple(k*g*E[h][i]-l*f*E[j][i] for i in range(3))
def norm(v):
 d=reduce(gcd,v);return tuple(x//d for x in v) if d else v
def canon(v):
 v=norm(v);return tuple(-x for x in v) if next((x for x in v if x),1)<0 else v
def dot(a,b):return sum(x*y for x,y in zip(a,b))
L=sorted({canon(line(a,b)) for a,b in combinations(T,2)}|{canon(line(a,h,3,2)) for a in T for h in H})
L=[l for l in L if min(l)<0<max(l)]
print('lines',len(L),flush=True)
def split(c,l):
 vv=[dot(p,l) for p in c]
 if not min(vv)<0<max(vv):return [c]
 out=[[],[]]
 for i,p in enumerate(c):
  q=c[(i+1)%len(c)];v,w=vv[i],vv[(i+1)%len(c)]
  if v>=0:out[0].append(p)
  if v<=0:out[1].append(p)
  if v*w<0:
   r=norm(tuple(abs(w)*a+abs(v)*b for a,b in zip(p,q)))
   out[0].append(r);out[1].append(r)
 return [tuple(x) for x in out]
polys=[((1,0,0),(0,1,0),(0,0,1))]
for l in L:polys=[z for c in polys for z in split(c,l)]
pts=set()
for c in polys:
 pts.update(c);pts.add(norm(tuple(map(sum,zip(*c)))))
 for a,b in zip(c,c[1:]+c[:1]):pts.add(norm(tuple(x+y for x,y in zip(a,b))))
pts=sorted(p for p in pts if min(p)>0)
print('cells',len(polys),'points',len(pts),flush=True)
P=L+[tuple(-x for x in l) for l in L]
allowed={norm(line(a,b)) for a,b in combinations(T,2)}|{norm(line(b,a)) for a,b in combinations(T,2)}|{norm(line(a,h,3,2)) for a in T for h in H}
P=[l for l in P if l in allowed]
S=[];labels=[]
for p in pts:
 s=[dot(e,p) for e in E];z=[Q(g,s[j]) for j,g in T];fs=[max(Q(g,s[j]) for j,g in enumerate(row)) for row in G];eta=min(fs[i] for i in W);mask=sum(1<<i for i,v in enumerate(z) if v==eta);near=sum(1<<i for i,v in enumerate(fs) if 2*v<3*eta)
 assert mask
 S.append(tuple(dot(l,p)>0 for l in P));labels.append((mask,near))
print('predicates',len(P),'near outputs',len(set(n for _,n in labels)),'joint label sets',len(set(labels)), 'singleton joint labels',len(set((m,n) for m,n in labels if m.bit_count()==1)),flush=True)
N=len(S);ALL=(1<<N)-1
qm=[0]*len(P);om={};single={};nm={}
for i,(sig,(a,b)) in enumerate(zip(S,labels)):
 bit=1<<i
 for j,t in enumerate(sig):
  if t:qm[j]|=bit
 nm[b]=nm.get(b,0)|bit
 for j in range(len(T)):
  if a>>j&1:om[j,b]=om.get((j,b),0)|bit
 if a.bit_count()==1:single[a,b]=single.get((a,b),0)|bit
sm_by_n={b:[m for (a,c),m in single.items() if c==b] for b in nm}
@lru_cache(None)
def lb(s):return sum(max(1,sum(bool(s&m) for m in sm_by_n[b])) for b,u in nm.items() if s&u)
@lru_cache(None)
def leaf(s):return next((k for k,m in om.items() if s&m==s),None)
print('root lower leaf count',lb(ALL),flush=True)
import sys
budget=int(sys.argv[1]) if len(sys.argv)>1 else 2000
calls=0
class Budget(Exception):pass
@lru_cache(None)
def solve(s,d):
 global calls
 calls+=1
 if calls>budget:raise Budget()
 k=leaf(s)
 if k is not None:return ('leaf',k)
 if d==0 or lb(s)>2**d:return None
 opts=[];seen=set()
 for j,m in enumerate(qm):
  a=s&m;b=s^a
  if not a or not b or min(a,b) in seen:continue
  seen.add(min(a,b));x=lb(a);y=lb(b)
  if max(x,y)>2**(d-1):continue
  opts.append((max(x,y),x+y,max(a.bit_count(),b.bit_count()),j,a,b))
 for _,_,_,j,a,b in sorted(opts):
  if lb(a)>=lb(b):
   t=solve(a,d-1)
   if t is None:continue
   u=solve(b,d-1)
  else:
   u=solve(b,d-1)
   if u is None:continue
   t=solve(a,d-1)
  if t is not None and u is not None:return (j,t,u)
 return None
for d in [6,7,8]:
 calls=0
 try:tr=solve(ALL,d)
 except Budget: print('budget',d,calls,flush=True);continue
 print('depth',d,'found',tr is not None,'calls',calls,flush=True)
 if tr is not None:
  def walk(s):
   t=tr
   while t[0]!='leaf':t=t[1 if s[t[0]] else 2]
   return t[1]
  assert all((a>>j&1) and n==b for sig,(a,b) in zip(S,labels) for j,n in [walk(sig)])
  def dep(t):return 0 if t[0]=='leaf' else 1+max(dep(t[1]),dep(t[2]))
  print('verified depth',dep(tr),'PASS',flush=True)
  print('tree',tr,flush=True);break
