# Independent exact replay, R172. Uses no inherited candidate coverage theorem.
import itertools as it, json, math
from fractions import Fraction as F
from pathlib import Path
V=[(1,0,0),(1,3,-1),(4,-4,1),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(6,-1,0),(7,-1,0),(9,-5,1)]
W=[0,3,5,6,7,9]; M=[30,51,42,21,58,51,20,7,23,30]
E=[(17,1,0),(39,0,0),(17,0,1),(22,1,0),(0,1,1),(22,0,1)]
def gaps(v):
 x,y,z=v; h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z]; return [abs(h[j]-h[i]) for i,j in it.combinations(range(4),2)]
G=[gaps(v) for v in V]; T=sorted({(j,g) for i in W for j,g in enumerate(G[i]) if g and M[i]>>j&1}); H=sorted({(j,g) for row in G for j,g in enumerate(row) if g})
full=[v for v in it.product(range(-10,11),repeat=3) if next((x for x in v if x),0)>0 and max(sum(max(x,0) for x in v),sum(max(-x,0) for x in v))<=10]; GG=[gaps(v) for v in full]
assert len(full)==1935
rows=json.loads(Path(__file__).with_name('x6_r172_strict_convex_witnesses.json').read_text()); count=0
# use exact fractions for all 1935 directions

def label(p):
 global count
 count+=1;t,b,d=p;s=[17*t+b,39*t,17*t+d,22*t+b,b+d,22*t+d]
 f=[max(F(g,sj) for g,sj in zip(row,s)) for row in GG];eta=min(f);N={v for v,val in zip(full,f) if 2*val<3*eta};assert N<=set(V)
 return sum(1<<i for i,(j,g) in enumerate(T) if F(g,s[j])==eta),sum(1<<i for i,v in enumerate(V) if v in N)
assert len({(m,n) for m,n,_ in rows})==len(rows)==35
P=[];pairs=0;weights=[(1,1),(1,2),(2,1),(1,4),(4,1),(1,9),(9,1)]
for m,n,ps in rows:
 assert m.bit_count()==1
 for p in ps:assert label(p)==(m,n);P.append(p)
 for p,q in it.combinations(ps,2):
  for a,b in weights:
   if (lambda z: not (z[0]&m) or z[1]!=n)(label([a*x+b*y for x,y in zip(p,q)])):break
  else:raise AssertionError((p,q))
  pairs+=1
print('FULL DIRECTION CONVEX PASS',len(P),'pairs',pairs,'inputs',count,'scores',count*len(full))
def canonical(x):
 d=math.gcd(*x);x=tuple(a//d for a in x) if d else x
 return tuple(-a for a in x) if next((a for a in x if a),0)<0 else x
def line(a,b,k,l):return canonical(tuple(k*a[1]*x-l*b[1]*y for x,y in zip(E[b[0]],E[a[0]])))
L=sorted({q for a,b,k,l in [(a,b,1,1) for a,b in it.combinations(H,2)]+[(a,b,3,2) for a,b in it.product(H,repeat=2)] if min(q:=line(a,b,k,l))<0<max(q)})
assert len(L)==442
Q=L+[tuple(-x for x in l) for l in L]; survive=[]
for i,l in enumerate(Q):
 a=sum(sum(x*y for x,y in zip(l,p))>0 for p in P)
 if a<=32 and len(P)-a<=32:survive.append(i)
print('ROOT WITNESS FILTER',len(Q),'remain',len(survive),'excluded',len(Q)-len(survive))
