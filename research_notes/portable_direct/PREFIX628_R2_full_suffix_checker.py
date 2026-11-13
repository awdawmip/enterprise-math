#!/usr/bin/env python3
"""Original 48 STAR phase / 96 port / 576 labelled BRC edges; exact suffix test.
Research reference frozen at f42f2906d77f24085c123f3ccfe9667d41caa96d.
No non-native propagation surrogate.
"""
from fractions import Fraction as F
from itertools import product
from collections import deque
from pathlib import Path
import json
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c): return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in (-1,1) for p in near(a,s*k))
IX={p:i for i,p in enumerate(P)}
def neigh(i):
 a,p,c=P[i];b=next(j for j in range(4) if j!=a and abs(c) in STARS[j]);return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
N=tuple(neigh(i) for i in range(48));G=IX[(0,1,-3)]
W=(1,1,1,1,0,0)
A=[]
for i in range(48):
 for j in N[i]:
  for u,v in product((0,1),repeat=2):
   gated=(j==G and u==v==1)
   A.append((2*i+u,2*j+v,F(0) if gated else F(W[abs(P[i][2])-1]),gated))
assert len(P)==48 and len(A)==576 and G==4
ARCS={}
for dst,src,w,gated in A: ARCS.setdefault(src,[]).append((dst,w,gated))
def embed(lam):
 r=[F(0)]*96
 for i in (4,11,14,32):
  r[2*i]=lam
  if i==G:r[2*i+1]=lam
 return r
def step(r,g):
 v=[F(0)]*96
 for dst,src,w,isgate in A:v[dst]+=(g if isgate else w)*r[src]
 return v
def evolve(gs,lam):
 states=[embed(lam)]
 for g in gs:states.append(step(states[-1],g))
 return states
def endpoint_six(r,n):
 assert n>=5
 v=[r[2*i] if i==G else r[2*i]+r[2*i+1] for i in range(48)]
 t=n-2;lam=v[(2,28,38,16)[(t+2)%4]]/F(4*2**t)
 w=(v[14],v[40]/2,v[26]/4,v[4]/4)
 j0=(2,1,0,3);b=(F(1),F(1),F(1),F(1,2))
 pi=[]
 for residue in range(4):
  h=sum(k%4==residue for k in range(3,n+1))
  pi.append(w[(j0[residue]+t)%4]/(lam*b[residue]*4**h))
 ell=v[3]+v[14]+v[15]-2*v[2];delta=r[29]-r[28]
 assert ell>0 and ell-3*delta>0
 last=(ell+9*delta)/(ell-3*delta)
 return lam,tuple(pi),last

def reconstruct_entrance(endpoint,n,L,previous):
 # previous: observed g_t,...,g_(n-1) for t>=5;
 #           observed g_5,...,g_(n-1) for t=4.
 t=n-L
 lam,pi,last=endpoint_six(endpoint,n)
 indices=list(range(t,n)) if t>=5 else list(range(5,n))
 assert len(previous)==len(indices)
 observed=dict(zip(indices,previous));observed[n]=last
 # Earlier four residue products are exact native endpoint invariants.
 pre=[pi[r] for r in range(4)]
 for k in range(t+1,n+1):pre[k%4]/=(observed[k]+3)
 h=[F(0)]*(t+1)
 if t>=5:h[t]=observed[t]
 for residue in range(4):
  ks=[i for i in range(1,t+1) if i%4==residue]
  flex=next((k for k in ks if k!=t),ks[0])
  other=F(1)
  for k in ks:
   if k!=flex:other*=h[k]+3
  h[flex]=pre[residue]/other-3
  assert h[flex]>=0
 if t>=5:assert h[t]==observed[t]
 assert all(F(1)==pre[r]/__import__('functools').reduce(lambda x,k:x*(h[k]+3),[k for k in range(1,t+1) if k%4==r],F(1)) for r in range(4))
 r=embed(lam)
 for g in h[1:]:r=step(r,g)
 return r,tuple(observed[k] for k in range(t+1,n+1)),lam

def suffix_signature(state,tail):
 # Exhaust full source-and-ordered-action-labelled positive tensor, including zero-gate branches.
 paths=[((src,),mass) for src,mass in enumerate(state) if mass]
 for gate in tail:
  new=[]
  for path,mass in paths:
   for dst,w,gated in ARCS.get(path[-1],[]):
    new.append((path+(dst,),mass*(gate if gated else w)))
  paths=new
 return dict(paths)

cases=[];total_coords=0;port_checks=0
for n,L in ((5,1),(6,1),(6,2),(7,1),(7,2),(7,3),(8,1),(8,2),(9,2),(9,3),(10,1),(10,2),(10,3),(12,2),(12,3)):
 for seed in range(2):
  lam=F(3+seed,2+seed)
  gates=tuple(F((3*k+2*seed)%7+1,(k+seed)%3+1) for k in range(1,n+1))
  states=evolve(gates,lam);t=n-L
  pi_seen=endpoint_six(states[n],n)
  assert pi_seen[0]==lam and pi_seen[2]==gates[-1]
  assert pi_seen[1]==tuple(__import__('functools').reduce(lambda x,k:x*(gates[k-1]+3),[k for k in range(1,n+1) if k%4==r],F(1)) for r in range(4))
  indices=list(range(t,n)) if t>=5 else list(range(5,n))
  history=tuple(gates[k-1] for k in indices)
  ancestor,tail,decoded_lam=reconstruct_entrance(states[-1],n,L,history)
  assert ancestor==states[t] and tail==gates[t:] and decoded_lam==lam
  direct=suffix_signature(states[t],gates[t:]);rebuilt=suffix_signature(ancestor,tail)
  assert direct==rebuilt
  total_coords+=len(direct);port_checks+=96
  cases.append({'n':n,'L':L,'extra_registers':len(history),'paths_checked':len(direct),'positive_paths':sum(x!=0 for x in direct.values())})
# Exact same-endpoint witness inherited from 627, and check all one-step labelled suffix differs.
lam=F(3,2);a=(F(1),)*10;b=list(a);b[8]=F(4,3);b[0]=F(9,13);b=tuple(b)
sa=evolve(a,lam);sb=evolve(b,lam)
assert sa[-1]==sb[-1] and sa[9]!=sb[9]
assert suffix_signature(sa[9],a[9:])!=suffix_signature(sb[9],b[9:])
res={'schema':'PREFIX628_R2_FULL_SUFFIX_NATIVE_BRC_CHECK_V1','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','case_count':len(cases),'compared_labelled_paths':total_coords,'compared_entrance_port_coordinates':port_checks,'collision_same_terminal_different_one_step_suffix':True,'cases':cases,'status':'ALL_ASSERTIONS_PASS','scope':'finite rational tests, original 48/96/576 native operator; general lower/upper bounds rely on accompanying mathematical proof and earlier author-side results'}
Path(__file__).with_name('PREFIX628_R2_full_suffix_results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:res[k] for k in ('status','case_count','compared_labelled_paths','compared_entrance_port_coordinates','collision_same_terminal_different_one_step_suffix')}))
