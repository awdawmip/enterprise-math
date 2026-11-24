import itertools as it, math, numpy as np
from fractions import Fraction as F
V=[(1,0,0),(1,3,-1),(4,-4,1),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(6,-1,0),(7,-1,0),(9,-5,1)]
W=[0,3,5,6,7,9]; M=[30,51,42,21,58,51,20,7,23,30]
E=np.array([[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]],dtype=np.int64)
def gaps(v):
 x,y,z=v; h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z]; return [abs(h[j]-h[i]) for i,j in it.combinations(range(4),2)]
G=[gaps(v) for v in V]; T=sorted({(j,g) for i in W for j,g in enumerate(G[i]) if g and M[i]>>j&1}); H=sorted({(j,g) for row in G for j,g in enumerate(row) if g})
def primitive(x):
 x=tuple(int(a) for a in x); d=math.gcd(*x); return tuple(a//d for a in x) if d else x
def canonical(x):
 x=primitive(x); return tuple(-a for a in x) if next((a for a in x if a),0)<0 else x
def line(a,b,k,l): return canonical(k*a[1]*E[b[0]]-l*b[1]*E[a[0]])
L=sorted({q for a,b,k,l in [(a,b,1,1) for a,b in it.combinations(H,2)]+[(a,b,3,2) for a,b in it.product(H,repeat=2)] if min(q:=line(a,b,k,l))<0<max(q)})
assert len(L)==442
# Build exact arrangement by vertices and edges, never polygon clipping.
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def ray(a,b):
 p=canonical(cross(a,b)); return p if min(p)>=0 and any(p) else None

def points():
 lines=L+[(1,0,0),(0,1,0),(0,0,1)]; n=len(L); vertices=[set() for _ in L]
 for i in range(n):
  for j in range(i+1,len(lines)):
   p=ray(lines[i],lines[j])
   if p is not None:
    vertices[i].add(p)
    if j<n:vertices[j].add(p)
 # Integer perturbation: dot(p,m) nonzero -> abs >=1; K exceeds every |dot(l,m)|.
 K=1+max(abs(dot(a,b)) for a in lines for b in L)
 P=set(); edge=0
 for l,vs in zip(L,vertices):
  if not vs:continue
  axis=next(i for i in range(3) if len({F(p[i],sum(p)) for p in vs})>1)
  seq=sorted(vs,key=lambda p:F(p[axis],sum(p)))
  for p in seq:
   if min(p)>0:P.add(p)
  for a,b in zip(seq,seq[1:]):
   p=primitive(tuple(x+y for x,y in zip(a,b)))
   if min(p)<=0:continue
   edge+=1;P.add(p)
   for s in [-1,1]:
    q=primitive(tuple(K*x+s*y for x,y in zip(p,l)))
    assert min(q)>0; P.add(q)
 print('edge',edge,'K',K,'rays',len(P),flush=True)
 return np.array(sorted(P),dtype=np.int64)

def labels(P):
 S=P@E.T; n=len(P); g=np.array(G); fs=[]
 for row in g:
  a=np.zeros(n,dtype=np.int64);b=np.ones(n,dtype=np.int64)
  for j in range(6):
   z=row[j]*b>a*S[:,j]; a=np.where(z,row[j],a);b=np.where(z,S[:,j],b)
  fs.append((a,b))
 nr,dr=fs[W[0]]
 for i in W[1:]:
  a,b=fs[i];z=a*dr<nr*b;nr=np.where(z,a,nr);dr=np.where(z,b,dr)
 mask=np.zeros(n,dtype=np.int64);near=mask.copy()
 for i,(j,g) in enumerate(T):mask|=((g*dr==nr*S[:,j]).astype(np.int64)<<i)
 for i,(a,b) in enumerate(fs):near|=((2*a*dr<3*nr*b).astype(np.int64)<<i)
 assert np.all(mask);return np.stack([mask,near],1)
if __name__=='__main__':
 P=points();print('max',P.max(), 'maxline',np.max(np.abs(L)),flush=True); labs=labels(P)
 print('labels',len(set(map(tuple,labs))), 'singleton',len({tuple(x) for x in labs if int(x[0]).bit_count()==1}),'near',len(set(labs[:,1])),flush=True)
 Q=np.array(L,dtype=np.int64); seen={}
 for start in range(0,len(P),4096):
  dots=P[start:start+4096]@Q.T
  keys=np.packbits(np.concatenate([dots>0,dots<0],axis=1),axis=1)
  for i,k in enumerate(keys):
   key=k.tobytes();idx=start+i
   if key in seen:assert tuple(labs[idx])==tuple(labs[seen[key]])
   else:seen[key]=idx
 ix=np.array(list(seen.values()));P=P[ix];labs=labs[ix];print('unique states',len(P),flush=True)
 counts=[0,0,0]
 for i in range(0,len(P),4096):
  n=(P[i:i+4096]@Q.T==0).sum(axis=1)
  counts[0]+=int((n==0).sum());counts[1]+=int((n==1).sum());counts[2]+=int((n>=2).sum())
 print('face counts [2D,1D,0D]',counts)
 assert counts[0]==counts[1]-counts[2]+1
 np.savez('r171_states.npz',P=P,L=Q,labs=labs)
