# EC49AC exact certificate; Python 3 standard library only.
# Run: python3 VERIFY_REMOTE.py
from fractions import Fraction as F
from itertools import product
import json
z=F(0)
slopes=[F(3),F(12369,2341),F(1359,251),F(567,13),F(5097,83)]
knots=[(z,z),(F(17,288),F(17,96)),(F(3047,38400),F(3641,12800)),(F(19,192),F(25,64)),(F(1939,19200),F(3067,6400)),(F(59,576),F(109,192))]
facets=[(F(297,2341),F(5049,37456),72,48,F(297,2341)),(F(101,753),F(583,4016),72,24,F(133,753)),(F(4841,1248),F(1633,416),72,24,F(29,39)),(F(45431,7968),F(15199,2656),72,48,F(1,3))]
def t(w,u):return F(1,2)+F((2*u-1)*(1-w),200)
def masses(x,c,u,j):
 p=sum((x[w][c]*t(w,u)*(F(1,6) if w==j else F(1,12)) for w in range(3)),z)
 q=sum((x[w][c]*t(w,u)/9 for w in range(3)),z)
 return p,q,p-q
def vertex(i,j,tags,bt,b):
 x=[[z for c in range(4)] for w in range(3)];h=F(5,16)+b
 for w in range(3):
  H=h if w==i else z;B=b if w==j else z
  assert H+B<=1
  x[w][tags[w]]+=1-H-B;x[w][bt]+=B
 return x
def obs(x):return [masses(x,c,u,j) for c,u,j in product(range(4),range(2),range(3))]
def env(a,lam):return sum((max(z,lam*d-p) for p,q,d in a),z)
def fmt(v):return str(v)
for source in ('P','Q'):
 leaves=[t(w,u)*(F(1,6) if source=='P' and w==j else F(1,12) if source=='P' else F(1,9)) for w,u,j in product(range(3),range(2),range(3))]
 assert len(leaves)==18 and all(x>0 for x in leaves) and sum(leaves)==1
assert all(slopes[k]<slopes[k+1] for k in range(4))
checked=0; groups=[]
for idx,(e0,e1,n0,n1,gamma) in enumerate(facets):
 lam=slopes[idx+1];assert 16*(e1-e0)==gamma>0
 for p in (idx+1,idx+2):assert lam*knots[p][0]-e1==knots[p][1]
 for b,expected,nexpected in [(z,e0,n0),(F(1,16),e1,n1)]:
  vals=[];dmax=z
  for i,j,tags,bt in product(range(3),range(3),product((0,1),repeat=3),(2,3)):
   a=obs(vertex(i,j,tags,bt,b));v=env(a,lam);vals.append(v)
   dmax=max(dmax,sum((max(z,d) for p,q,d in a),z))
  assert len(vals)==144 and max(vals)==expected and vals.count(expected)==nexpected
  assert dmax==knots[-1][0];checked+=144
 groups.append((fmt(lam),fmt(e0),fmt(e1),fmt(gamma)))
x=[[F(1),z,z,z],[z,F(1),z,z],[F(9,16),z,F(1,16),z]]
a={(c,u,j):masses(x,c,u,j) for c,u,j in product(range(4),range(2),range(3))}
pure=[(1,0,1),(1,1,1),(2,0,2),(2,1,2)]
extra=[(0,1,0),(0,0,0),(0,0,2),(0,1,2)]
assert sum((a[k][0] for k in pure),z)==knots[1][1]
assert sum((a[k][2] for k in pure),z)==knots[1][0]
for idx,k in enumerate(extra):
 p,q,d=a[k];assert p/d==slopes[idx+1]
 assert d==knots[idx+2][0]-knots[idx+1][0]
 assert p==knots[idx+2][1]-knots[idx+1][1]
def witness(delta):
 y={k:z for k in a}
 if delta<=knots[1][0]:
  for k in pure:y[k]=delta/knots[1][0]
 else:
  for k in pure:y[k]=F(1)
  for idx,k in enumerate(extra):
   lo=knots[idx+1][0];hi=knots[idx+2][0]
   y[k]=max(z,min(F(1),(delta-lo)/(hi-lo)))
 assert all(0<=v<=1 for v in y.values())
 p=sum((y[k]*v[0] for k,v in a.items()),z)
 q=sum((y[k]*v[1] for k,v in a.items()),z)
 assert p-q==delta
 return p,q
samples=[]
for idx in range(5):
 d0,p0=knots[idx];d1,p1=knots[idx+1]
 assert p1-p0==slopes[idx]*(d1-d0)
 for d in (d0,(d0+d1)/2,d1):
  p,q=witness(d);assert p==p0+slopes[idx]*(d-d0)
  samples.append((fmt(d),fmt(p),fmt(q)))
assert witness(F(1,12))==(F(1229,4016),F(2683,12048))
assert witness(knots[-1][0])==(F(109,192),F(67,144))
T=sum((x[w][c] for w,c in product(range(3),range(4))),z);b=sum((x[w][c] for w,c in product(range(3),(2,3))),z)
assert (T+b)/3==F(43,48) and T/3==F(7,8)
print(json.dumps({'schema':'EC49AC_288_VERTEX_COMPLETE_BOUNDARY_V1','checks':checked,'groups':groups,'knots':[(fmt(d),fmt(p)) for d,p in knots],'samples':samples,'costs':['43/48','7/8'],'status':'AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED'},indent=2))
