#!/usr/bin/env python3
"""Exact external ternary-IID N=14 Stage243 dual/convex-slice exploration.
Author-side candidate; no Source/Driver admission or native-X6/BRC physical claim.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json,time
N=14
PN=(3,1,20);QN=(2,2,20)
DEN=24**N
P=tuple(F(v,24) for v in PN)
LP=F(16197445464,292565255);LQ=F(17414258688,292565255)
S=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
NEXT=lambda s,j:(s[0]+1,s[1]+(j==0),s[2]+(j==1))
@lru_cache(None)
def bell(s):
 n,a,b=s
 vals={'P':LQ*F(2**(a+b),3**a),'Q':LP}
 if n<N: vals['C']=F(1)+sum(P[j]*bell(NEXT(s,j))[0] for j in range(3))
 m=min(vals.values());return m,tuple(x for x,v in vals.items() if v==m),vals
H=bell((0,0,0))[0]
ties=[s for s in S if len(bell(s)[1])>1]
gaps=[v-bell(s)[0] for s in S for v in bell(s)[2].values() if v>bell(s)[0]]
print('bellman',len(S),'ties',len(ties),'positive gaps',len(gaps),'min gap',min(gaps),'H',H)
assert len(S)==680 and len(ties)==13 and len(gaps)==1227
assert all(len(bell(s)[1])==2 for s in ties)
fixed={s:bell(s)[1][0] for s in S if s not in ties}
opt=[bell(s)[1] for s in ties]
BASE=[24**(N-n) for n in range(N+1)]
point={}
all_dom=True
node_total=0
for bits in range(1<<len(ties)):
 acts=dict(fixed)
 for i,s in enumerate(ties):acts[s]=opt[i][(bits>>i)&1]
 @lru_cache(None)
 def dp(s):
  n,_,_=s;act=acts[s];base=BASE[n]
  if act=='P':return 0,base,n*base,n*base
  if act=='Q':return base,0,n*base,n*base
  child=[dp(NEXT(s,j)) for j in range(3)]
  return (sum(PN[j]*child[j][0] for j in range(3)),
          sum(QN[j]*child[j][1] for j in range(3)),
          sum(PN[j]*child[j][2] for j in range(3)),
          sum(QN[j]*child[j][3] for j in range(3)))
 ep,eq,tp,tq=dp((0,0,0))
 assert F(tp,DEN)+LP*F(ep,DEN)+LQ*F(eq,DEN)==H,('dual',bits)
 all_dom &= tp>tq
 point[bits]=(ep-eq,ep,tp,tq)
 # Completely independent ordered-history DFS: no merging of count states.
 acc=[0,0,0,0];stack=[(0,0,0,1,1)]
 while stack:
  n,x,y,p,q=stack.pop();node_total+=1
  a=acts[(n,x,y)]
  if a=='C':
   for j in range(3):stack.append((n+1,x+(j==0),y+(j==1),p*PN[j],q*QN[j]))
  else:
   factor=BASE[n]
   if a=='Q':acc[0]+=p*factor
   if a=='P':acc[1]+=q*factor
   acc[2]+=n*p*factor;acc[3]+=n*q*factor
 assert tuple(acc)==(ep,eq,tp,tq),('INDEPENDENT_ORDERED_DFS_MISMATCH',bits)
 if bits%1024==0:print('count',bits,flush=True)
assert all_dom
print('full_history_dfs_nodes',node_total)
print('policies',len(point),'distinct xy',len({p[:2] for p in point.values()}),'time dominance',all_dom)
# Build global 2D convex hull (XY) of all points; repeated XY retain minimal mask.
seen={};
for bits,p in point.items():seen.setdefault(p[:2],bits)
seq=sorted(seen)
# Monotone chain, retaining vertices and excluding redundant collinear intermediates.
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
lower=[]
for p in seq:
 while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
 lower.append(p)
upper=[]
for p in reversed(seq):
 while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
 upper.append(p)
hull=lower[:-1]+upper[:-1]
print('hull size',len(hull),'lower',len(lower),'upper',len(upper));
# For all full hull edges crossing X=0, the balanced error is on segment.
def section(a,b):
 x1,y1=a;x2,y2=b
 if x1*x2>0 or x1==x2:return None
 if x1==0:return F(y1)
 if x2==0:return F(y2)
 return F(y1*(-x2)+y2*x1,x1-x2)
edges=[]
for a,b in zip(hull,hull[1:]+hull[:1]):
 v=section(a,b)
 if v is not None:edges.append((v,a,b))
assert len(edges)==2,edges
edges.sort(key=lambda r:r[0]);(miny,ea,eb),(maxy,ec,ed)=edges
# Set edge orientation x1<x2. Supports: miny line lower, maxy line upper.
A,B=sorted((ea,eb));C,D=sorted((ec,ed))
def margin(v,a,b):
 x,y=v;x1,y1=a;x2,y2=b
 return (y-y1)*(x2-x1)-(y2-y1)*(x-x1)
assert all(margin(k[:2],A,B)>=0 and margin(k[:2],C,D)<=0 for k in point.values())
# Pick boundary pair by mask, and mix to X=0 (works for full real arcs by convexity).
def witness(a,b):
 b1,b2=seen[a],seen[b];x1,y1=point[b1][:2];x2,y2=point[b2][:2]
 w=F(-x2,x1-x2)
 assert 0<=w<=1 and w*x1+(1-w)*x2==0
 alpha=(w*y1+(1-w)*y2)/DEN
 tp=(w*point[b1][2]+(1-w)*point[b2][2])/DEN
 tq=(w*point[b1][3]+(1-w)*point[b2][3])/DEN
 assert tp>tq and tp==H-(LP+LQ)*alpha
 return dict(alpha=str(alpha),value=str(tp),timeQ=str(tq),masks=[b1,b2],weights=[str(w),str(1-w)],XY=[list(a),list(b)])
left=witness(A,B);right=witness(C,D)
alpha242=F(1092145237285,2925595459584)
value242=F(2619507545471,365699432448)
print('LEFT',left,'RIGHT',right)
print('LEFT agrees stage242',F(left['alpha'])==alpha242,F(left['value'])==value242)
assert F(left['alpha'])==alpha242 and F(left['value'])==value242
assert F(right['alpha'])>alpha242
assert F(right['value'])<value242
# For cross-check independent forward occupancy of 2 witness pairs, sum P/Q masses (normalized by DEN).
def forward(bits):
 acts=dict(fixed)
 for i,s in enumerate(ties):acts[s]=opt[i][(bits>>i)&1]
 inflow={(0,0,0):(DEN,DEN)};out=[0,0,0,0]
 # Inflow masses store count-weighted masses with denominator 24^n factored to DEN.
 for s in S:
  p,q=inflow.get(s,(0,0));n,_,_=s
  if not p and not q:continue
  a=acts[s]
  if a=='P':out[1]+=q;out[2]+=n*p;out[3]+=n*q
  elif a=='Q':out[0]+=p;out[2]+=n*p;out[3]+=n*q
  else:
   # already denominator 24^N, exact fractions needed if path mass not divisible
   for j in range(3):
    child=NEXT(s,j);v=inflow.get(child,(F(0),F(0)))
    inflow[child]=(v[0]+F(p*PN[j],24),v[1]+F(q*QN[j],24))
 return tuple(out)
for i in set(left['masks']+right['masks']):
 o=forward(i)
 # note point=(ep-eq,ep,tp,tq)
 ep,eq,tp,tq=o
 assert (ep-eq,ep,tp,tq)==point[i],(i,'forward mismatch')
 print('forward crosscheck',i,'PASS')
result={
 'stage':243,'status':'AUTHOR_EXACT_UNREVIEWED','model':{'P':list(PN),'Q':list(QN),'N':N},
 'LP':str(LP),'LQ':str(LQ),'H':str(H),'slope':str(-LP-LQ),
 'bellman_states':len(S),'tie_states':[{'s':list(s),'actions':list(bell(s)[1])} for s in ties],
 'positive_gaps':len(gaps),'minimum_gap':str(min(gaps)),
 'ordered_dfs_nodes':node_total,'deterministic_corner_count':len(point),'distinct_xy':len(seen),'hull_vertices':len(hull),
 'all_corners_tp_gt_tq':all_dom,'left':left,'right':right,
 'delta':str(F(right['alpha'])-F(left['alpha'])),
 'supports':{'lower':{'A':list(A),'B':list(B)},'upper':{'C':list(C),'D':list(D)}},
 'identity':'At each corner tP+LP*eP+LQ*eQ=H. All corners satisfy both global integer supporting-line inequalities; endpoint mixtures have eP=eQ, tP>tQ. Markovization covers full ordered history in this IID model.',
 'forward_crosschecked_masks':sorted(set(left['masks']+right['masks']))
}
Path(__file__).with_name('CERT_STAGE243_EXACT.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('STAGE243_EXACT_AUTHOR_PASS',len(point))
