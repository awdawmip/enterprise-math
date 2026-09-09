#!/usr/bin/env python3
# Exact 5/7/13/19 quotient-field experiment. Research, not Nollm runtime.
# Run with frozen predecessor scripts beside this file, or the bundled layout.
"""Task-local adapter for frozen mixed57 geometry; no Nollm runtime change."""
from pathlib import Path
import sys, math, hashlib, importlib.util, argparse
from itertools import product
from functools import lru_cache
import numpy as np
ROOT=Path(__file__).resolve().parent
OPTIONS=[ROOT/'nollm_boundary_repair'/'experiment.py',
         ROOT/'nollm_mixed57_boundary_repair_20260909_c6c82.py']
PATH=next((p for p in OPTIONS if p.exists()),None)
if PATH is None:raise FileNotFoundError('frozen boundary-repair predecessor required')
if hashlib.sha256(PATH.read_bytes()).hexdigest()!='fced7c21cc5fdd597381094531454e5b5d37711cd514b64c79b02989ced205fa':
 raise ValueError('boundary-repair source hash mismatch')
sys.path.insert(0,str(PATH.parent))
_load=importlib.util.spec_from_file_location('boundary_repair',PATH)
r=importlib.util.module_from_spec(_load);sys.modules['boundary_repair']=r;_load.loader.exec_module(r)
m=r.m;sp=r.sp
E13=np.array([[1,-3],[3,4]],dtype=np.int64)
E19=np.array([[2,-3],[3,5]],dtype=np.int64)
NEW_ANCHORS=((-3,1),(-1,3),(-1,-2),(-3,2),(-2,3),(-2,-1))

def spec(s,legacy=False):
 a,b,c,d=(tuple(s)+(0,)*(4-len(s)));j=(b+3*c+2*d)%6
 if 5**a*7**b*13**c*19**d>10**12:raise ValueError('int64 prototype bound')
 T=5**(a//2)*m.power(m.W,(a//2)%6)@m.power(m.G,b)@m.power(E13,c)@m.power(E19,d)
 return T@(m.H[j] if a%2 else m.I), (tuple(map(int,T@(r.ANCHORS[j] if legacy else NEW_ANCHORS[j]))) if a%2 else None), j

def member(points,s,legacy=False):
 arr=np.asarray(points,dtype=np.int64);shape=arr.shape[:-1];x=arr.reshape(-1,2)
 P,u,j=spec(s,legacy);vs=m.vectors(P);closed=np.ones(len(x),dtype=bool)
 for v in vs:closed &= x[:,0]*(2*v[0]+v[1])+x[:,1]*(v[0]+2*v[1])<=m.Q(v)
 keep=closed.copy()
 for v in vs:
  lhs=x[:,0]*(2*v[0]+v[1])+x[:,1]*(v[0]+2*v[1]);ids=np.flatnonzero(closed&(lhs==m.Q(v)))
  for i in ids:
   z=tuple(map(int,x[i]))
   if s[0]%2:
    y=(z[0]-v[0],z[1]-v[1]);kz,ky=r.tie_key(z,u),r.tie_key(y,u)
    assert kz!=ky
    if ky<kz:keep[i]=False
   elif v[0]*z[1]-v[1]*z[0]<=0:keep[i]=False
 return keep.reshape(shape)

def section(s):
 P,_,_=spec(s);n=m.old.det(P)
 if n>700000:raise ValueError('section enumeration limit')
 vs=m.vertices(P);lo=[math.ceil(min(v[i] for v in vs)) for i in range(2)];hi=[math.floor(max(v[i] for v in vs)) for i in range(2)]
 X=np.array(list(product(range(lo[0],hi[0]+1),range(lo[1],hi[1]+1))),dtype=np.int64)
 S=X[member(X,s)];assert len(S)==n
 return S

@lru_cache(None)
def stencil(parity,j,p):
 P=m.H[j] if parity else m.I
 if p==5:C=5*m.W if parity else m.H[j]
 else:
  T,sh={7:(m.G,1),13:(E13,3),19:(E19,2)}[p];C=T@(m.H[(j+sh)%6] if parity else m.I)
 # Reuse the exact prior polygon compiler, but extend its bounded enumeration.
 # The earlier radius<6 guard was proved only for 5/7, not for arbitrary primes.
 _,poly=sp.stencil(P,C)
 lo=[math.ceil(min(x[i] for x in poly)) for i in range(2)]
 hi=[math.floor(max(x[i] for x in poly)) for i in range(2)]
 return np.array([v for v in product(range(lo[0],hi[0]+1),range(lo[1],hi[1]+1))
                  if sp.in_poly(v,poly)],dtype=np.int64)

def child_state(s,p):
 ss=list(s)+[0]*(4-len(s));ss[[5,7,13,19].index(p)]+=1;return tuple(ss)

def children(S,s,p):
 P,_,j=spec(s);V=stencil(s[0]%2,j,p);out=[]
 for start in range(0,len(S),1000):
  ps=S[start:start+1000];X=ps[:,None,:]+(V@P.T)[None,:,:];mask=member(X,child_state(s,p))
  assert np.all(mask.sum(1)==p)
  out.append(X[mask])
 return np.concatenate(out)


from itertools import permutations, combinations
import json
f=sys.modules[__name__]
PRIMES=(5,7,13,19)
def save(o,name): (OUT/name).write_text(json.dumps(o,indent=2)+'\n')
def cvsign(w,v):
 return m.dot2(w,v)**2-3*(int(w[0])*v[1]-int(w[1])*v[0])**2

def cert():
 rows=[];N=set()
 for h in [m.I]+m.H:N.update(m.Q(v) for v in r.facet_vectors(h))
 assert N=={1,3,7,19}
 for e,j,p in product(range(2),range(6),PRIMES):
  P=m.H[j] if e else m.I
  if p==5:
   C=5*m.W if e else m.H[j]
   olda=f.NEW_ANCHORS[j] if e else None
   newa=None if e else f.NEW_ANCHORS[j]
  else:
   T,sh={7:(m.G,1),13:(f.E13,3),19:(f.E19,2)}[p]
   C=T@(m.H[(j+sh)%6] if e else m.I)
   olda=f.NEW_ANCHORS[j] if e else None
   newa=T@f.NEW_ANCHORS[(j+sh)%6] if e else None
  X=m.old.adj(P)@C;den=m.old.det(P)
  assert not np.any(X%den);assert m.old.det(X//den)==p
  common=sorted(set(r.facet_vectors(P))&set(r.facet_vectors(C)))
  signs=[]
  for v in common:
   s=cvsign(olda,v) if olda is not None else 1
   t=cvsign(newa,v) if newa is not None else 1
   assert s>0 and t>0,(e,j,p,v,s,t)
   signs.append([s,t])
  V=f.stencil(e,j,p)
  _,poly=f.sp.stencil(P,C)
  # full polygon bounding-box enumeration, no inherited radius cutoff
  rows.append(dict(parity=e,j=j,prime=p,shared_normals=common,chiral_signs=signs,
                   candidates=len(V),max_Q=max(map(m.Q,V)),stencil=V.tolist(),
                   polygon=[[str(x) for x in v] for v in poly]))
 save(dict(norms=sorted(N),phases=rows),'certificate.json')
 return rows


def run(out):
 global OUT
 OUT=Path(out);OUT.mkdir(parents=True,exist_ok=True)
 assert np.array_equal(E13%5,m.power(m.G,3)%5)
 assert np.array_equal(E19%5,m.power(m.G,2)%5)
 c=cert();print('certificate PASS',len(c),flush=True)
 states=[s for s in product(range(4),range(3),range(2),range(2)) if 5**s[0]*7**s[1]*13**s[2]*19**s[3]<=150000]
 states=sorted(set(states+[(5,1,0,0),(5,1,0,1),(4,0,1,0),(3,0,0,2),(1,0,2,1),(1,3,0,1)]))
 cache={};rows=[]
 for s in states:
  S=f.section(s);P,_,j=f.spec(s);n=len(S)
  assert len(np.unique(m.coset_keys(S,P),axis=0))==n
  assert m.same_set(S,-S)
  metric=m.old.hull_metrics(S);assert metric['hull_total_lattice_sites']==n,(s,metric)
  h=S.T@S
  if not s[0]%2:
   assert m.same_set(S,S@m.W.T)
   assert h[0,0]==h[1,1] and 2*h[0,1]==-h[0,0]
  legacy_inside=f.member(S,s,True)
  rows.append(dict(state=s,j=j,count=n,holes=0,axis_ratio=m.old.ratio(h),
                   changed_from_legacy=int((~legacy_inside).sum()),C6=not bool(s[0]%2)))
  cache[s]=S;print('section',s,n,'ok',flush=True)
 np.savez_compressed(OUT/'layers.npz',**{'s'+'_'.join(map(str,s)):a for s,a in cache.items()})
 save(rows,'sections.json')
 edges=[]
 for s,S in cache.items():
  for p in PRIMES:
   t=f.child_state(s,p)
   if t not in cache:continue
   assert np.all(f.member(S,t)),('stable',s,p)
   if len(S)>3000:continue
   C=f.children(S,s,p);assert m.same_set(C,cache[t])
   edges.append(dict(state=s,prime=p,parents=len(S),descendants=len(C)))
   print('edge',s,p,len(S),flush=True)
 save(edges,'edges.json')
 # All six orders for three factors and all 24 for four, exact fibers of their product.
 orders=[]
 for s in [(0,0,0,0),(1,0,0,0),(0,1,0,0),(1,1,0,0),(2,0,0,0)]:
  for primes in [(5,7,13),(5,7,19),(5,7,13,19)]:
   dst=s
   for p in primes:dst=f.child_state(dst,p)
   if dst not in cache:continue
   for path in permutations(primes):
    X=cache[s];cur=s
    for p in path:X=f.children(X,cur,p);cur=f.child_state(cur,p)
    assert m.same_set(X,cache[dst])
    _,cts=np.unique(m.coset_keys(X,f.spec(s)[0]),axis=0,return_counts=True)
    assert len(cts)==len(cache[s]) and np.all(cts==np.prod(primes))
   orders.append(dict(start=s,primes=primes,permutations=__import__('math').factorial(len(primes)),
                      parents=len(cache[s]),descendants=len(cache[dst]),mismatch=0))
   print('orders',orders[-1],flush=True)
 save(orders,'orders.json')
 # Concrete old-rule failure, not a mathematical no-go for all selectors.
 s=(5,1,0,0);x=np.array([[121,39]],dtype=np.int64);y=np.array([[-104,-61]],dtype=np.int64)
 assert f.member(x,s,True)[0] and not f.member(x,f.child_state(s,19),True)[0]
 assert not f.member(x,s)[0] and f.member(y,s)[0] and f.member(y,f.child_state(s,19))[0]
 assert m.Q(x[0])==m.Q(y[0])==20881
 # Finite field shift identities and inclusion/diamond identities using exact integer matrices.
 shifts={};algebra=0
 for name,T,sh in [('7',m.G,1),('13',f.E13,3),('19',f.E19,2)]:
  for j in range(6):assert not np.any((m.old.adj(m.H[j])@T@m.H[(j+sh)%6])%5)
  shifts[name]=sh
 for s in product(range(4),range(3),range(2),range(2)):
  P=f.spec(s)[0]
  for p,q in combinations(PRIMES,2):
   sp=f.child_state(s,p);sq=f.child_state(s,q);end=f.child_state(sp,q)
   def trans(a,b):
    A=f.spec(a)[0];B=f.spec(b)[0];T=m.old.adj(A)@B;d=m.old.det(A);assert not np.any(T%d)
    return T//d
   assert np.array_equal(trans(s,sp)@trans(sp,end),trans(s,sq)@trans(sq,end));algebra+=1
 result=dict(schema='NOLLM_SPLIT_PRIME_BOUNDARY_EXTENSION_V1',status='PASS_RESEARCH_NOT_PROMOTED',
             event_id='NOLLM-SPLIT-EXTENSION-20260909-C6C82',new_anchors=f.NEW_ANCHORS,
             six_state_shifts=shifts,short_facet_norms=[1,3,7,19],phase_types=len(c),
             sections=len(rows),enumerated_points_sum=sum(v['count'] for v in rows),
             largest_section=max(v['count'] for v in rows),hull_holes=0,
             refinement_edges=len(edges),parents_checked=sum(v['parents'] for v in edges),
             order_tests=orders,permutation_runs=sum(v['permutations'] for v in orders),
             descendants_across_order_runs=sum(v['permutations']*v['descendants'] for v in orders),
             exact_matrix_diamonds=algebra,
             max_candidates_by_prime={str(p):max(v['candidates'] for v in c if v['prime']==p) for p in PRIMES},
             old_rule_failure=dict(start=[5,1,0,0],prime=19,lost_point=[121,39],competitor=[-104,-61],equal_norm=20881),
             limits=['quotient/index multiplication, not scalar label multiplication',
                     'new anchor convention requires boundary migration',
                     'full split-prime extension proof is conditional on the stated primitive/ideal choices',
                     'candidate cost grows with prime and uses the current basis',
                     'physical fanout cap 7 is not implemented for primes 13 and 19'])
 save(result,'results.json');print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',type=Path,default=ROOT/'results')
 run(parser.parse_args().output)
