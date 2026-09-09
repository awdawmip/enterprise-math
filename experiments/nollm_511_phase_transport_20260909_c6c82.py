#!/usr/bin/env python3
"""Exact two-chart transport tests; parent computations are hash-pinned."""
from pathlib import Path
from itertools import product,permutations
from collections import deque,Counter
import importlib.util,hashlib,sys,json,math
import numpy as np
ROOT=Path(__file__).resolve().parent
import argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--data',type=Path,default=ROOT/'results')
DATA=parser.parse_args().data;DATA.mkdir(parents=True,exist_ok=True)
path=next((p for p in [ROOT/'prior/nollm_two_inert_511/experiment.py',ROOT/'nollm_two_inert_511_20260909_c6c82.py'] if p.exists()),None)
if path is None:raise FileNotFoundError('hash-pinned two-inert predecessor required')
assert hashlib.sha256(path.read_bytes()).hexdigest()=='db00742a81241d10883299253307fb1ee7831b7703bf710f88288606998f53b4'
spec=importlib.util.spec_from_file_location('parent',path);f=importlib.util.module_from_spec(spec);sys.modules['parent']=f;spec.loader.exec_module(f)
m=f.m;G=f.ES[7];SCORES=np.load(DATA/'allcost.npy')
C5=[3,4,2,0,1,5];C11=[8,9,4,11,6,1,2,0,3,5,7,10]
CYCLES=(C5,C11);DELTA=(1,11)

def shift(s):
 e,g,l,k=s
 return e,g,f.act(G,l,5,True),f.act(G,k,11,False)

def score(s):
 e,g,l,k=s;return int(SCORES[e+2*g,C5.index(l),C11.index(k)])

def choose(s):return int(score(shift(s))<score(s))

def shifted_key(k):
 e,g,l,h=k
 return e,g,f.act(G,l,5,True) if e else -1,f.act(G,h,11,False) if g else -1

def crt_matrix(ex,reverse=False):
 n=math.prod(p**a for p,a in zip(f.ACTIVE,ex));D=np.zeros((2,2),dtype=np.int64)
 if n==1:return np.eye(2,dtype=np.int64)
 for p,a in zip(f.ACTIVE,ex):
  if not a:continue
  mod=p**a
  if p==5:C=G if reverse else (pow(7,-1,mod)*m.old.adj(G))%mod
  elif p==11:C=(pow(7,-1,mod)*m.old.adj(G))%mod if reverse else G
  else:C=f.I
  w=n//mod*pow(n//mod,-1,mod)
  D=(D+w*C)%n
 assert math.gcd(m.old.det(D),n)==1
 return D

def world(ex,chart):
 P,u,s,T=f.world(ex)
 if not chart:return P,u,s,T
 ns=shift(s);H=f.H(*ns);v=None if f.key(ns)==f.REG else tuple(map(int,T@f.ANCHORS[f.key(ns)]))
 return T@H,v,ns,T

CANONICAL_BOUND_CASES=set()
def canonical_points(Y,P,u):
 """Exact nearest section representative via <=9 candidates after Gauss reduction."""
 from fractions import Fraction as F
 B=m.reduced(P);n=abs(m.old.det(B));adj=m.old.adj(B)
 if m.old.det(B)<0:B=B.copy();B[:,1]*=-1;adj=m.old.adj(B)
 token=f.pkey(B)
 if token not in CANONICAL_BOUND_CASES:
  vv=m.vertices(B)
  coeff=[tuple((adj[i,0]*x+adj[i,1]*y)/n for i in (0,1)) for x,y in vv]
  assert all(abs(x)<=1 and abs(y)<=1 for x,y in coeff)
  CANONICAL_BOUND_CASES.add(token)
 offsets=np.array(list(product((-1,0,1),repeat=2)),dtype=np.int64)
 ans=[]
 for start in range(0,len(Y),1000):
  ys=np.asarray(Y[start:start+1000],dtype=np.int64);flo=(ys@adj.T)//n
  trial=ys[:,None,:]-(flo[:,None,:]+offsets[None,:,:])@B.T
  mask=f.member(trial,P,u)
  assert np.all(mask.sum(axis=1)==1)
  ans.append(trial[mask])
 return np.concatenate(ans)

CACHE={}
def section(ex,c):
 key=(tuple(ex),c)
 if key not in CACHE:
  P,u,s,T=world(ex,c);pts=f.section(P,u,700000)
  CACHE[key]=(pts,P,{tuple(k):i for i,k in enumerate(m.coset_keys(pts,P))})
 return CACHE[key]

def convert(pts,ex,src,dst):
 if src==dst:return pts.copy()
 n=math.prod(p**a for p,a in zip(f.ACTIVE,ex));D=crt_matrix(ex,reverse=src==1)
 S,P,lookup=section(ex,dst)
 Y=(pts@D.T)%n
 keys=m.coset_keys(Y,P)
 expected=S[[lookup[tuple(k)] for k in keys]]
 _,u,_,_=world(ex,dst)
 actual=canonical_points(Y,P,u)
 assert np.array_equal(actual,expected)
 return actual

def refine(pts,ex,p):
 _,_,s,_=f.world(ex);src=choose(s)
 # Use parent fiber routine unchanged on canonical source-chart residue coordinates.
 a=convert(pts,ex,src,0);res=f.children(a,ex,p)
 dst_ex=f.next_exp(ex,p);dst=choose(f.world(dst_ex)[2])
 return convert(res,dst_ex,0,dst),dst_ex

# All 72 initial choices, generator 7 and 19 ONLY.
gen=[(1,1),(2,9)];bad={(3,7),(1,11),(5,3)}
q=deque([(0,0)]);seen={(0,0)}
while q:
 x=q.popleft()
 for a,b in gen:
  y=((x[0]+a)%6,(x[1]+b)%12)
  if y not in seen:seen.add(y);q.append(y)
assert len(seen)==72
reach=[]
for start in product(range(6),range(12)):
 q=deque([start]);prev={start:None};hit=None
 while q:
  x=q.popleft()
  if x in bad:hit=x;break
  for p,(a,b) in zip((7,19),gen):
   y=((x[0]+a)%6,(x[1]+b)%12)
   if y not in prev:prev[y]=(x,p);q.append(y)
 route=[];x=hit
 while prev[x] is not None:x,p=prev[x];route.append(p)
 reach.append(dict(start=start,thin=hit,path=route[::-1],distance=len(route)))
print('all starts reach thin; distances',Counter(x['distance'] for x in reach),flush=True)
# Commutation of chart translation with EVERY finite transition in frozen family.
commutation=0
for s in f.STATES:
 for p in [5,11]+f.EXCEPT:
  ns,E=f.trans(s,p);ns1,E1=f.trans(shift(s),p)
  assert shift(ns)==ns1 and np.array_equal(E,E1);commutation+=1
print('chart / transition commutation',commutation,flush=True)
# Complete quotient bijections across the entire base atlas, scales 1 and 5.
rows=[];roundtrips=0;cloud_max=0
for k in f.KEYS:
 for t in (0,1):
  scale=5**t;dst=shifted_key(k)
  P0=scale*f.H(*k);P1=scale*f.H(*dst)
  u0=None if k==f.REG else tuple(scale*x for x in f.ANCHORS[k])
  u1=None if dst==f.REG else tuple(scale*x for x in f.ANCHORS[dst])
  S0=f.section(P0,u0);S1=f.section(P1,u1);ex=(2*t+k[0],k[1],0,0,0)
  n=len(S0);D=crt_matrix(ex);inv=crt_matrix(ex,True)
  lookup1={tuple(z):i for i,z in enumerate(m.coset_keys(S1,P1))}
  Z=S1[[lookup1[tuple(z)] for z in m.coset_keys((S0@D.T)%n,P1)]]
  assert len(np.unique(Z,axis=0))==n
  assert np.array_equal(canonical_points((S0@D.T)%n,P1,u1),Z)
  assert np.array_equal(m.coset_keys((Z@inv.T)%n,P0),m.coset_keys(S0,P0))
  # lattice compatibility is checked on both basis columns, not just sample residues
  assert not np.any((m.old.adj(P1)@D@P0)%n)
  assert not np.any((m.old.adj(P0)@inv@P1)%n)
  # inactive line values do not affect either cost or actual lattice
  s=(k[0],k[1],k[2] if k[0] else C5[0],k[3] if k[1] else C11[0]);c=choose(s)
  S=S0 if not c else S1;P=P0 if not c else P1
  info=f.section_info(S,P,k==f.REG)
  cloud_max=max(cloud_max,info['axis_ratio'] if info['axis_ratio'] is not None and math.isfinite(info['axis_ratio']) else 0)
  rows.append(dict(key=k,scale=scale,chart=c,score0=score(s),score1=score(shift(s)),**info))
  roundtrips+=n
print('transport sections',len(rows),'residues',roundtrips,'max cloud',cloud_max,flush=True)
# Finite actual state test including all five prime factors.
states=sorted(ex for ex in product(range(3),range(3),range(2),range(2),range(2)) if math.prod(p**a for p,a in zip(f.ACTIVE,ex))<=20000)
actual=[];naturality=0;parents_checked=0;witness=None;identity_witness=None
for ex in states:
 P0,u,s,T=world(ex,0);c=choose(s);S=section(ex,c)[0]
 img=convert(S,ex,c,1-c);back=convert(img,ex,1-c,c)
 assert np.array_equal(back,S)
 actual.append(dict(exponents=ex,index=len(S),chart=c,score=score(shift(s) if c else s)))
 for p in f.ACTIVE:
  child=f.next_exp(ex,p)
  if child not in states or len(S)>1000:continue
  cc=choose(f.world(child)[2]);C=section(child,cc)[0]
  Y,_=refine(S,ex,p);assert m.same_set(Y,C)
  parents_checked+=len(S);naturality+=1
  if identity_witness is None and cc!=c:
   baseparents=convert(S,ex,c,0)
   zero_children=convert(baseparents,child,0,cc)
   ids=np.flatnonzero(np.any(zero_children!=S,axis=1))
   if len(ids):
    ii=int(ids[0]);identity_witness=dict(exponents=ex,prime=p,from_chart=c,to_chart=cc,old_point=S[ii].tolist(),new_point=zero_children[ii].tolist(),moved_zero_children=len(ids),parents=len(S))
  if witness is None and cc!=c:
   missing=set(map(tuple,S))-set(map(tuple,C))
   if missing:witness=dict(exponents=ex,prime=p,from_chart=c,to_chart=cc,lost_visible_point=min(missing),lost_count=len(missing),parent_count=len(S))
print('actual',len(actual),'edges',naturality,'parents',parents_checked,'support failure',witness,'identity move',identity_witness,flush=True)
# Per-parent 5*11*7 fibers, dynamic chart choice on every step.
orders=[]
for start in [(0,0,0,0,0),(1,0,0,0,0),(0,1,0,0,0)]:
 for primes in [(5,11,7),(5,11,13),(5,11,7,13)]:
  end=start
  for p in primes:end=f.next_exp(end,p)
  if math.prod(p**a for p,a in zip(f.ACTIVE,end))>20000:continue
  S=section(start,choose(f.world(start)[2]))[0]
  expected=section(end,choose(f.world(end)[2]))[0]
  ref=None
  for path in permutations(primes):
   X=S;cur=start
   for p in path:X,cur=refine(X,cur,p)
   assert m.same_set(X,expected)
   # group sequential descendants in source parent order
   groups=[set(map(tuple,a)) for a in X.reshape(len(S),math.prod(primes),2)]
   if ref is None:ref=groups
   else:assert ref==groups
  orders.append(dict(start=start,primes=primes,runs=math.factorial(len(primes)),parents=len(S),descendants=len(expected)))
print('order runs',sum(r['runs'] for r in orders),flush=True)
# A tiny fully labelled witness: horizontal unit-thin 55 lattice -> compact second chart.
k=(1,1,0,0);dst=shifted_key(k)
S0=f.section(f.H(*k),f.ANCHORS[k]);S1=f.section(f.H(*dst),f.ANCHORS[dst]);n=55
lookup={tuple(z):i for i,z in enumerate(m.coset_keys(S1,f.H(*dst)))}
Y=S1[[lookup[tuple(z)] for z in m.coset_keys((S0@crt_matrix((1,1,0,0,0)).T)%55,f.H(*dst))]]
unit=[(q,r) for q,r in product(range(-1,2),repeat=2) if f.Q((q,r))==1];idx={tuple(x):i for i,x in enumerate(S0)}
edges=kept=0;displacement=[]
for i,x in enumerate(S0):
 displacement.append(f.Q(Y[i]-x))
 for d in unit:
  j=idx.get((x[0]+d[0],x[1]+d[1]))
  if j is not None and j>i:
   edges+=1;kept+=int(f.Q(Y[j]-Y[i])==1)
np.savez_compressed(DATA/'transport_example.npz',source=S0,target_by_source_label=Y,target_section=S1)
example=dict(source_key=k,target_key=dst,source_axis=m.old.ratio(S0.T@S0),target_axis=m.old.ratio(S1.T@S1),source_neighbors=edges,preserved_neighbors=kept,moved=int(np.sum(np.any(S0!=Y,axis=1))),max_move_squared=max(displacement),mean_move_squared=sum(displacement)/55)
print('labelled thin -> compact',example,flush=True)
result=dict(status='PASS_RESEARCH_NOT_PROMOTED',event_id='NOLLM-511-PHASE-CONTROL-20260909-C6C82',source_pin='db00742a81241d10883299253307fb1ee7831b7703bf710f88288606998f53b4',shift=[1,11],reachable_from_every_initial=72,reachability=reach,transition_commutation_checks=commutation,transport_sections=len(rows),transport_roundtrip_residues=roundtrips,atlas=rows,max_selected_sample_cloud_ratio=cloud_max,actual_sections=actual,actual_refinement_edges=naturality,actual_parent_checks=parents_checked,permutation_groups=orders,permutation_runs=sum(r['runs'] for r in orders),support_inclusion_counterexample=witness,logical_zero_child_movement=identity_witness,canonical_candidate_bound=9,canonical_basis_bound_cases=len(CANONICAL_BOUND_CASES),labelled_example=example,limits=['two distinct quotient embeddings, not rigid rotations of one point cloud','fixed addresses and neighborhood distances not preserved across chart switches','basis condition ratio is not cloud covariance','not ordinary scalar label multiplication','minimax optimality only among declared phase translations','exact integer bit cost grows; no physical fanout implementation'])
(DATA/'control_results.json').write_text(json.dumps(result,indent=2,default=lambda x:int(x) if isinstance(x,np.integer) else x)+'\n')
