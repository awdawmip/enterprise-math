"""Exact rational Minkowski certificates for all phasewise local stencils."""
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
try:
 import mixed57 as m
except ModuleNotFoundError:
 import nollm_mixed57_20260909_c6c82 as m

def hull(points):
 pts=sorted(set(points))
 def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 lo=[];hi=[]
 for p in pts:
  while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
  lo.append(p)
 for p in reversed(pts):
  while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
  hi.append(p)
 return lo[:-1]+hi[:-1]

def in_poly(x,poly):
 return all((b[0]-a[0])*(x[1]-a[1])-(b[1]-a[1])*(x[0]-a[0])>=0 for a,b in zip(poly,poly[1:]+poly[:1]))

def stencil(P,Q):
 a=m.old.adj(P);d=m.old.det(P)
 cloud=[]
 for y in m.vertices(Q):
  for x in m.vertices(P):
   diff=(y[0]-x[0],y[1]-x[1]);cloud.append(tuple(F(int(a[i,0])*diff[0]+int(a[i,1])*diff[1],d) for i in range(2)))
 poly=hull(cloud)
 # The separately proved radius<6 bound makes this enumeration complete.
 return [tuple(map(int,v)) for v in m.STENCIL if in_poly(tuple(v),poly)],poly

if __name__=='__main__':
 allvs=set();rows=[]
 for j in range(6):
  for a,b,q in [(m.I,m.H[j],5),(m.H[j],5*m.W,5),(m.I,m.G,7),(m.H[j],m.G@m.H[(j+1)%6],7)]:
   vs,poly=stencil(a,b);allvs.update(vs)
   rows.append(dict(j=j,prime=q,from_shape=a.tolist(),to_shape=b.tolist(),count=len(vs),max_Q=max(map(m.Q,vs)),
                    stencil=vs,poly=[[str(c) for c in v] for v in poly]))
 print('counts',[(r['j'],r['prime'],r['count'],r['max_Q']) for r in rows])
 print('union',len(allvs),'maxnorm',max(map(m.Q,allvs)))
 # All inequalities are rational certificates; no numeric hull tolerance.
 (Path(__file__).parent/'results'/'stencil_certificate.json').write_text(json.dumps(dict(rows=rows,union=sorted(allvs),union_count=len(allvs)),indent=2)+'\n')
 # Execute the compact stencils independently on every saved finite edge.
 root=Path(__file__).parent/'results';result=json.loads((root/'results.json').read_text())
 layers=np.load(root/'layers.npz');verified=[]
 for e in result['edges']:
  a,b,q=e['a'],e['b'],e['prime'];offset=(0 if a%2==0 else 1) if q==5 else (2 if a%2==0 else 3)
  record=rows[4*(b%6)+offset]
  target=(a+(q==5),b+(q==7));points=layers[f'a{a}b{b}']
  child,maxq=m.descendants(points,a,b,q,record['stencil'])
  assert m.same_set(child,layers[f'a{target[0]}b{target[1]}'])
  verified.append(dict(a=a,b=b,prime=q,candidates=record['count'],parents=len(points)))
 print('compact stencil verification:',len(verified),'edges,',sum(v['parents'] for v in verified),'parents; max candidates',max(v['candidates'] for v in verified))
 (root/'compact_stencil_checks.json').write_text(json.dumps(dict(status='PASS',verified=verified),indent=2)+'\n')
