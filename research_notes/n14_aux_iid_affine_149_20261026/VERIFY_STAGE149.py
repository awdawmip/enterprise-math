#!/usr/bin/env python3
"""Exact author stage149 proof checker, external N14 ternary iid, 4-observer.
Independent Bellman backward Fraction plus literal ordered-prefix integer-weight DFS.
No floating point, no BRC native/physical transfer.
"""
from fractions import Fraction as F
from collections import defaultdict
import json
from pathlib import Path
N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(100164600,266527)
L=F(98815768,266527)
B=(11,0,1)
G=(11,7,3)
STATES=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def LR(s):return F(2**(s[1]+s[2]),3**s[1])
value={}; optimal={}; ties=[]; gaps=[]
for s in reversed(STATES):
 opts={'P':K*LR(s),'Q':L}
 if s[0]<N:opts['C']=1+sum((P[j]*value[c] for j,c in enumerate(child(s))),F())
 v=min(opts.values());value[s]=v
 optimal[s]=tuple(k for k,x in opts.items() if x==v)
 if len(optimal[s])>1: ties.append((s,optimal[s]))
 gaps.extend(x-v for x in opts.values() if x>v)
assert len(STATES)==680 and len(gaps)==1238
assert set(ties)=={(B,('Q','C')),(G,('P','C'))}
assert len(gaps)==1238 and min(gaps)==F(2016649859,176854523904)
H=value[(0,0,0)]
assert H==F(2645762825003325844206337,9733658641089851031552)
STRICT={s:acts[0] for s,acts in optimal.items()}
def action(s,b,g):
 if s==B:return 'Q' if b else 'C'
 if s==G:return 'P' if g else 'C'
 return STRICT[s]
def backward(b,g):
 D={}
 for s in reversed(STATES):
  a=action(s,b,g)
  if a=='P':m=(F(),F(1),F(),F())
  elif a=='Q':m=(F(1),F(),F(),F())
  else:
   cs=[D[t] for t in child(s)]
   m=tuple((F(1) if j>=2 else F())+sum(((P if j%2==0 else Q)[i]*cs[i][j] for i in range(3)),F()) for j in range(4))
  D[s]=m
 return D[0,0,0]
def literal_dfs(b,g):
 stack=[(0,0,0,1,1)]
 total=[0]*4;hits=defaultdict(lambda:[0,F(),F()]);visited=0
 while stack:
  n,a,c,x,y=stack.pop();s=(n,a,c);visited+=1
  if s in (B,G):
   hits[s][0]+=1;hits[s][1]+=F(x,24**n);hits[s][2]+=F(y,12**n)
  act=action(s,b,g)
  if act=='C':
   assert n<14
   stack.extend(((n+1,a+1,c,x*3,y),(n+1,a,c+1,x,y),(n+1,a,c,x*20,y*10)))
  else:
   X=x*24**(N-n);Y=y*12**(N-n)
   if act=='Q':total[0]+=X
   else:total[1]+=Y
   total[2]+=n*X;total[3]+=n*Y
 return tuple(F(total[j],(24 if j%2==0 else 12)**N) for j in range(4)),visited,hits
C={};vis=[];hs={}
for b,g in ((0,0),(1,0),(0,1),(1,1)):
 m=backward(b,g);m2,count,hits=literal_dfs(b,g)
 assert m==m2,(b,g)
 C[b,g]=m;vis.append(count)
 hs[f'b{b}_g{g}']={str(s):[str(x) for x in hits[s]] for s in (B,G)}

def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def plus(*vec):return tuple(map(sum,zip(*vec)))
M00=C[0,0];dB=sub(C[1,0],M00);dG=sub(C[0,1],M00)
assert sub(sub(C[1,1],C[1,0]),dG)==(F(),)*4
alpha148=F(6124245463802993075,17602807464179269632)
V148=F(35426720708566621357,2933801244029878272)
bstar=F(7957468313073991,8143872000000000)
# balanced g=c0+c1*b, with g(bstar)=0. Express from eP=eQ.
g0=(M00[1]-M00[0])/(dG[0]-dG[1])
gb=(dB[1]-dB[0])/(dG[0]-dG[1])
assert g0+gb*bstar==0,(g0,gb,bstar)
assert gb>0
# balance allowed b in [bstar,min(1,(1-g0)/gb)]
b_g1=(1-g0)/gb
b_end=min(F(1),b_g1)
assert b_end>bstar
g_end=g0+gb*b_end
assert 0<=g_end<=1

def observe(b):
 g=g0+gb*b
 return tuple(M00[i]+b*dB[i]+g*dG[i] for i in range(4))
start=observe(bstar);end=observe(b_end)
assert start[0]==start[1]==alpha148
assert start[2]==V148
assert start[2]>start[3] and end[2]>end[3]
assert end[0]==end[1]>start[0]
assert start[2]>end[2]
assert all(x[2]+L*x[0]+K*x[1]==H for x in (start,end))
assert (start[2]-end[2])==(K+L)*(end[0]-start[0])
# saturation right sharpness: any equality in universal support line must choose only tied actions,
# may average history-dependent mixing at each count state by P-probability mass;
# cones disjoint (same depth, differing counts). Equality errors fixes g(b).
# Max common error on the box section is at b_end; strict for alpha>alpha_end.
res={
 'schema':'EM_STAGE149_AUTHOR_EXACT_V1',
 'scope':'external ternary iid N14 arbitrary ordered-history randomized policies; no native X6 transfer',
 'source_stage148':'aafcfc3ca6e2f8325311848ccc2a5193a074209f',
 'bellman':{'states':680,'ties':[{'state':list(s),'actions':list(a)} for s,a in ties], 'positive_gaps':len(gaps),'min_positive_gap':str(min(gaps)),'negative_gaps':0,'K':str(K),'L':str(L),'Hroot':str(H)},
 'observer_order':['eP','eQ','tP','tQ'],
 'corners':{f'b{b}_g{g}':[str(x) for x in C[b,g]] for b,g in ((0,0),(1,0),(0,1),(1,1))},
 'M00':[str(x) for x in M00], 'dB':[str(x) for x in dB], 'dG':[str(x) for x in dG],
 'corner_cross_term':['0']*4,'visited_dfs':vis,'first_hit':hs,
 'balance':{'g0':str(g0),'dg_db':str(gb),'b_start':str(bstar),'b_g1':str(b_g1),'b_end':str(b_end),'g_end':str(g_end)},
 'affine':{'alpha148':str(alpha148),'V148':str(V148),'alpha149':str(end[0]),'V149':str(end[2]),'eta149':str(end[0]-alpha148),'slope149':str(K+L),'t_gap_start':str(start[2]-start[3]),'t_gap_end':str(end[2]-end[3]),'endpoint':'B_Q_STOP_SATURATION' if b_end==1 else 'G_P_STOP_SATURATION'},
 'verification':{'bellman':'PASS','two_distinct_algorithms_4_corners':'PASS','universal_ordered_history_lower_bound':'BELLMAN_FINITE_680','full_real_affine':'ANALYTIC_AFFINE','support_right_sharpness':'ARGUMENT_PLUS_EXACT_BOUNDS','native_claim':'NOT_VERIFIED','driver_review':'NOT_VERIFIED'}
}
p=Path(__file__).parent/'certificate149.json';p.write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print('PASS_STAGE149',res['affine'])
print('DFS',vis, 'FirstHit',hs['b0_g0'])
print('dB',dB, 'dG',dG)
print('g0',g0,'gb',gb,'b_g1',b_g1)
