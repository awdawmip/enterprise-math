#!/usr/bin/env python3
"""Exact N=4 two-law (T,D) TV minimax witness and Bellman certificate."""
import json
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

N={1:{'A':(F(1,2),F(1,2),None),'B':(F(1,2),F(3,2),None)},
   2:{'AU':(F(1,6),F(1),'A'),'AV':(F(1,3),F(1,4),'A'),
      'BU':(F(1,4),F(1),'B'),'BV':(F(1,4),F(2),'B')}}
N[3]={}
for par,(q,r,_) in N[2].items():
 e={'AU':F(1,10),'AV':F(0),'BU':F(4,5),'BV':F(0)}[par]
 for i,s in enumerate((-1,1)):N[3][f'{par}{i}']=(q/2,r*(1+s*e),par)
N[4]={}
for par,(q,r,_) in N[3].items():
 e=F(0) if par=='AV0' else F(3,50) if par=='AV1' else F(1,20)
 for i,s in enumerate((-1,1)):N[4][f'{par}{i}']=(q/2,r*(1+s*e),par)
for t in N:
 assert len(N[t])==2**t
 assert all(q>0 and r>0 for q,r,_ in N[t].values())
 assert sum(q for q,r,_ in N[t].values())==sum(q*r for q,r,_ in N[t].values())==1
 if t<4:
  for n,(q,r,_) in N[t].items():
   ch=[(cq,cr) for cq,cr,pa in N[t+1].values() if pa==n]
   assert len(ch)==2 and sum(cq for cq,cr in ch)==q and sum(cq*cr for cq,cr in ch)==q*r
assert N[2]['AU'][1]==N[2]['BU'][1]==1
assert N[3]['AV0'][1]==N[3]['AV1'][1]==F(1,4)
P,Q,C=(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))
def full(t,n,r):
 if t==1:return C
 if t==2:return {'AU':P,'AV':C,'BU':C,'BV':P}[n]
 if t==3:return {'AV0':Q,'AV1':C,'BU0':Q,'BU1':P}.get(n,P)
 return Q if 100*r<F(2501,100) else P

def compressed(t,n,r):
 if t==1:return C
 if t==2:return {F(1):(F(2,5),F(0),F(3,5)),F(1,4):C,F(2):P}[r]
 if t==3:return {F(9,10):(F(7,19),F(0),F(12,19)),F(11,10):P,
                  F(1,4):(F(0),F(13,20),F(7,20)),F(1,5):Q,F(9,5):P,F(2):P}[r]
 return {F(171,200):P,F(189,200):Q,F(1,4):Q,F(47,200):P,F(53,200):P}.get(r,P)

def vector(action):
 out=[F(0)]*16
 for leaf,(q,r4,_) in N[4].items():
  alive=F(1)
  for t,h in enumerate((leaf[0],leaf[:2],leaf[:3],leaf),start=1):
   a=action(t,h,N[t][h][1]);assert all(x>=0 for x in a) and sum(a)==1
   for j in (0,1):
    ix=2*(t-1)+j;out[ix]+=q*alive*a[j];out[ix+8]+=q*r4*alive*a[j]
   alive*=a[2]
  assert alive==0
 assert sum(out[:8])==sum(out[8:])==1
 return tuple(out)
for t in N:
 d={}
 for n,(q,r,_) in N[t].items():
  a=compressed(t,n,r)
  if r in d:assert d[r]==a
  d[r]=a
f,s=vector(full),vector(compressed)
WQ=(0,0,3,45,45,-45,-45,-45)
WP=(0,0,-29,50,-50,50,50,50)
def L(v):return sum(WQ[i]*v[i]+WP[i]*v[8+i] for i in range(8))
def TV(offset):return sum(abs(s[i]-f[i]) for i in range(offset,offset+8))/2
assert TV(0)==TV(8)==F(7,380)
assert L(f)==-F(467,12) and L(s)==-F(425,12)
assert max(WQ)-min(WQ)==90 and max(WP)-min(WP)==100

def c(t,r,a):
 i=2*(t-1)+(a=='Q')
 return F(WQ[i])+r*WP[i]
term={n:min('PQ',key=lambda a:c(4,r,a)) for n,(q,r,pa) in N[4].items()}
c3={}
for n,(q,r,pa) in N[3].items():
 c3[n]={a:c(3,r,a) for a in 'PQ'}
 c3[n]['C']=sum(q4*c(4,r4,term[m])/q for m,(q4,r4,parent) in N[4].items() if parent==n)
rootmin={};count=0
for a1 in product('PQC',repeat=2):
 first=dict(zip(('A','B'),a1));best=None
 for a2 in product('PQC',repeat=3):
  count+=1;second=dict(zip(('U','AV','BV'),a2));v=F(0);groups=defaultdict(list)
  for n,(q,r,_) in N[1].items():
   if first[n]!='C':v+=q*c(1,r,first[n])
  for n,(q,r,par) in N[2].items():
   if first[par]!='C':continue
   act=second['U' if n in ('AU','BU') else n]
   if act!='C':v+=q*c(2,r,act)
   else:
    for child,(qc,rc,parent) in N[3].items():
     if parent==n:groups[rc].append(child)
  for names in groups.values():
   v+=min(sum(N[3][n][0]*c3[n][act] for n in names) for act in 'PQC')
  if best is None or v<best:best=v
 rootmin[''.join(a1)]=best
assert count==243
assert rootmin=={'PP':0,'PQ':0,'QP':0,'QQ':0,'PC':-F(95,4),
                 'QC':-F(95,4),'CP':-F(91,6),'CQ':-F(91,6),'CC':-F(425,12)}
assert min(rootmin.values())-L(f)==F(7,2)
fs=lambda x:str(x)
print(json.dumps({'status':'PASS_EXACT_FRACTION_N4_TV_7_OVER_380',
 'n_by_time':{str(t):len(N[t]) for t in N},'root_t2_cases':count,
 'outcome_order':'Q: each t(P,Q), then P: each t(P,Q)',
 'F':list(map(fs,f)),'S':list(map(fs,s)),
 'tv_q':fs(TV(0)),'tv_p':fs(TV(8)),
 'dual_q':WQ,'dual_p':WP,'dual_full':fs(L(f)),
 'dual_min':fs(min(rootmin.values())),'dual_gap':fs(F(7,2)),
 'dual_root_table':{k:fs(v) for k,v in sorted(rootmin.items())},
 'exact_common_tv_minimax':fs(F(7,380))},indent=2,sort_keys=True))

