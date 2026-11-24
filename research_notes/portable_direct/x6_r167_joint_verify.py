from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd
from functools import reduce, lru_cache
V=[(1,0,0),(1,3,-1),(4,-4,1),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(6,-1,0),(7,-1,0),(9,-5,1)]
M=[30,51,10,21,58,51,20,3,23,30]
# R164 full masks, verified from R164 previous table, use full six instead for optimizer (only nonzero)
W=[0,3,5,6,7,9]
E=[(17,1,0),(39,0,0),(17,0,1),(22,1,0),(0,1,1),(22,0,1)]
J=list(combinations(range(4),2))
def gaps(v):
 x,y,z=v;h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z);return tuple(abs(h[i]-h[j]) for i,j in J)
G=list(map(gaps,V))
# exact original R164 score masks (read source to confirm), else using full terms
MASK=[30,51,42,21,58,51,20,7,23,30]
T=sorted({(j,g) for i in W for j,g in enumerate(G[i]) if g and MASK[i]>>j&1})
print('terms',T,len(T),flush=True)
# positive weights normalized (t,b,d)=(1-x-y,x,y). linear form coordinates (constant,x,y)
def line(a,b,k=1,l=1):
 j,g=a;h,f=b
 # sign of k*g/s_j - l*f/s_h
 v=[k*g*E[h][i]-l*f*E[j][i] for i in range(3)]
 return (v[0],v[1]-v[0],v[2]-v[0])
def norm(v):
 d=reduce(gcd,v);return tuple(x//d for x in v) if d else v
def canonical(v):
 v=norm(v);return tuple(-x for x in v) if next((x for x in v if x),1)<0 else v
def val(l,p):return l[0]+l[1]*p[0]+l[2]*p[1]
S=tuple((Q(x),Q(y)) for x,y in [(0,0),(1,0),(0,1)])
def splits(poly,l):
 vv=[val(l,p) for p in poly]
 if not min(vv)<0<max(vv):return [poly]
 def half(s):
  out=[]
  for i,p in enumerate(poly):
   q=poly[(i+1)%len(poly)];v,w=vv[i],vv[(i+1)%len(poly)]
   if s*v>=0:out.append(p)
   if v*w<0:
    a=v/(v-w);out.append(tuple(p[j]+a*(q[j]-p[j]) for j in range(2)))
  return tuple(out)
 return [half(1),half(-1)]
def samples(polys):
 p=set()
 for c in polys:
  p.update(c);p.add(tuple(sum(x[j] for x in c)/len(c) for j in range(2)))
  for a,b in zip(c,c[1:]+c[:1]):p.add(tuple((a[j]+b[j])/2 for j in range(2)))
 return {x for x in p if min(x)>0 and sum(x)<1}
L=sorted({canonical(line(a,b)) for a,b in combinations(T,2)}-{(0,0,0)})
L=[l for l in L if min(map(lambda p:val(l,p),S))<0<max(map(lambda p:val(l,p),S))]
# every strict sign query and reverse sign, allowing explicit equality differentiation
P=L+[tuple(-x for x in l) for l in L]
polys=[S]
for l in L:polys=[z for c in polys for z in splits(c,l)]
pts=samples(polys)
print('optimizer lines,cells,points',len(L),len(polys),len(pts),flush=True)
def cap(p):
 t,b,d=1-sum(p),*p;return [a*t+e*b+f*d for a,e,f in E]
def result(p):
 s=cap(p);z=[Q(g,s[j]) for j,g in T];eta=min(max(Q(g,s[j]) for j,g in enumerate(G[i])) for i in W);return sum(1<<i for i,v in enumerate(z) if v==eta)
# greedily split by exact multi-output label; constant signs removed, intersection permits any optimum term
states={tuple(val(l,p)>0 for l in P):result(p) for p in pts}
print('states',len(states),'output sets',len(set(states.values())),flush=True)
items=sorted(states.items());n=len(items);ALL=(1<<n)-1
Qm=[sum(1<<i for i,(v,o) in enumerate(items) if v[j]) for j in range(len(P))]
Om=[sum(1<<i for i,(v,o) in enumerate(items) if o>>j&1) for j in range(len(T))]
# greedy split, with prefer larger common-output leaves and balance, exact worst depth by replay
@lru_cache(None)
def common(s):return next((i for i,m in enumerate(Om) if s&m==s),None)
def depth(t):return 0 if t[0]=='leaf' else 1+max(depth(t[1]),depth(t[2]))
def route(t,p):
 path=[]
 while t[0]!='leaf':
  j=t[0];yes=val(P[j],p)>0;path.append((j,yes));t=t[1 if yes else 2]
 return t[1],tuple(path)
print('unique active anchors', [(T[j],sum(o==(1<<j) for _,o in items)) for j in range(len(T))],flush=True)
# prefer split that reduces count of compulsory different anchors, not raw geometric rank states
single=[sum(1<<i for i,(_,o) in enumerate(items) if o==1<<j) for j in range(len(T))]
@lru_cache(None)
def distinct(s):return sum(bool(s&m) for m in single)
calls=0
@lru_cache(None)
def bounded(s,d):
 global calls
 calls+=1
 k=common(s)
 if k is not None:return ('leaf',k)
 if not d or distinct(s)>2**d:return None
 opts=[];seen=set()
 for j,m in enumerate(Qm):
  a=s&m;b=s^a
  if not a or not b or min(a,b) in seen:continue
  seen.add(min(a,b))
  x=0 if common(a) is not None else max(2,distinct(a));y=0 if common(b) is not None else max(2,distinct(b))
  if max(x,y)>2**(d-1):continue
  opts.append((max(x,y),x+y,max(a.bit_count(),b.bit_count()),j,a,b))
 for _,_,_,j,a,b in sorted(opts):
  if distinct(a)>=distinct(b):
   t=bounded(a,d-1)
   if t is None:continue
   u=bounded(b,d-1)
  else:
   u=bounded(b,d-1)
   if u is None:continue
   t=bounded(a,d-1)
  if t is not None and u is not None:return (j,t,u)
 return None
for d in (4,5,6):
 tr=bounded(ALL,d);print('bounded',d,'calls',calls,'found',tr is not None,flush=True)
 if tr is not None:break
assert depth(tr)==6
assert all(result(p)>>route(tr,p)[0]&1 for p in pts)
print('tree',tr,flush=True)
# all optimizer cells including edges and vertices: refine each closed 2D polygon with near threshold lines using anchor chosen at interior. Anchor remains optimal on closure by continuity. At any sample actual tree may route to another leaf, but true threshold output is anchor invariant.
near_pred=sorted({(j,g) for i in range(len(V)) for j,g in enumerate(G[i]) if g and M[i]>>j&1})
# near predicate 2*g/s_j < 3*anchor_g/s_anchor -> line(anchor,term,3,2)>0
# split per optimizer polygon; use all vertices, edge midpoints, interior as representatives; if optimizer lines cross boundary only at existing vertices, sign constant per face.
from collections import defaultdict
bucket=defaultdict(dict)
count=0
allpoints=set()
for c in polys:
 p=tuple(sum(x[j] for x in c)/len(c) for j in range(2));k,_=route(tr,p);a=T[k]
 cs=[c]
 for h in near_pred:
  l=canonical(line(a,h,3,2));cs=[z for c0 in cs for z in splits(c0,l)]
 count+=len(cs)
 for p in samples(cs):
  allpoints.add(p)
  k,path=route(tr,p);a=T[k];s=cap(p);eta=Q(a[1],s[a[0]])
  assert result(p)>>k&1
  sig=tuple(val(line(a,h,3,2),p)>0 for h in near_pred)
  output=sum(1<<i for i,g in enumerate(G) if max(Q(v,s[j]) for j,v in enumerate(g))<Q(3,2)*eta)
  assert output==sum(1<<i for i,g in enumerate(G) if all(not v or not(M[i]>>j&1) or 2*v<3*eta*s[j] for j,v in enumerate(g)))
  assert sig not in bucket[path] or bucket[path][sig]==output
  bucket[path][sig]=output
print('refined cells',count,'leaves',len(bucket),'joint states',sum(map(len,bucket.values())),flush=True)
# exact per-leaf minimax decision depth, compare against R166 universal worst six
rows=[]
trees={}
for path,bd in bucket.items():
 li=list(bd.items());n=len(li);full=(1<<n)-1
 qs=[sum(1<<i for i,(s,o) in enumerate(li) if s[j]) for j in range(len(near_pred))]
 outs=[sum(1<<i for i,(s,o) in enumerate(li) if o==v) for v in set(bd.values())]
 @lru_cache(None)
 def dp(S):
  if any(S&m==S for m in outs):return 0
  return 1+min(max(dp(a),dp(S^a)) for m in qs if (a:=S&m) and a!=S)
 def build(S):
  if dp(S)==0:return ('leaf',next(o for i,(_,o) in enumerate(li) if S>>i&1))
  _,j,a=min((max(dp(a),dp(S^a)),j,a) for j,m in enumerate(qs) if (a:=S&m) and a!=S)
  return (j,build(a),build(S^a))
 d=dp(full);tree=build(full);trees[path]=tree
 for sig,o in li:
  t=tree
  while t[0]!='leaf':t=t[1 if sig[t[0]] else 2]
  assert t[1]==o
 rows.append((len(path),d,n,len(outs),path))
print('per-leaf',[(a,b,c,d) for a,b,c,d,_ in sorted(rows)],flush=True)
print('joint worst',max(a+b for a,b,*_ in rows),'near worst',max(b for a,b,*_ in rows),flush=True)

# Additional exact full-population replay at a deterministic subset of refined points.
U=[v for v in product(range(-10,11),repeat=3) if any(v) and next(x for x in v if x)>0 and max(sum(max(x,0) for x in v),sum(max(-x,0) for x in v))<=10]
UG=[gaps(v) for v in U];assert len(U)==1935
from math import lcm
pp=sorted(allpoints);checks=0
for p in pp[::max(1,len(pp)//120)]:
 s=cap(p);scale=lcm(*(x.denominator for x in s));ss=[int(x*scale) for x in s]
 k,path=route(tr,p);j,g=T[k];a,b=g,ss[j]
 t=trees[path]
 while t[0]!='leaf':
  i,v=near_pred[t[0]];t=t[1 if 2*v*b<3*a*ss[i] else 2]
 N=set()
 for u,h in zip(U,UG):
  assert any(v*b>=a*ss[i] for i,v in enumerate(h))
  if all(2*v*b<3*a*ss[i] for i,v in enumerate(h)):N.add(u)
 assert N=={v for i,v in enumerate(V) if t[1]>>i&1}
 checks+=len(U)
print('full population checks',checks,'weights',checks//1935,'PASS',flush=True)
