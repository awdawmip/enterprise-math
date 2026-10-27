#!/usr/bin/env python3
"""Exact standalone Fraction checker: N4 post-switch flat TV phase."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import json
O,Z=F(1),F(0)
P,Q,C=(O,Z,Z),(Z,O,Z),(Z,Z,O)
LO,HI=F(26911,39215),F(27483,39215)
N={1:{'A':(F(1,2),F(1,2),None),'B':(F(1,2),F(3,2),None)},2:{
 'AU':(F(1,6),O,'A'),'AV':(F(1,3),F(1,4),'A'),
 'BU':(F(1,4),O,'B'),'BV':(F(1,4),F(2),'B')}}
for t in (3,4):
 N[t]={}
 for pa,(q,r,_) in N[t-1].items():
  e=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[pa] if t==3 else
     Z if pa=='AV0' else F(3,50) if pa=='AV1' else F(1,20))
  for i,s in enumerate((-1,1)):N[t][pa+str(i)]=(q/2,r*(1+s*e),pa)
for t in N:
 assert len(N[t])==2**t and all(q>0 and r>0 for q,r,_ in N[t].values())
 assert sum(q for q,r,_ in N[t].values())==sum(q*r for q,r,_ in N[t].values())==1
 if t<4:
  for h,(q,r,_) in N[t].items():
   ch=[(qc,rc) for qc,rc,parent in N[t+1].values() if parent==h]
   assert len(ch)==2 and sum(qc for qc,rc in ch)==q and sum(qc*rc for qc,rc in ch)==q*r

def coeff(lam):
 return ((7843*lam+22989)/72358,(39215*lam+44303)/72358,
         (39215*lam+44303)/72358,307*(181-253*lam)/289432,
         3*(8198-1265*lam)/36179)
def full(lam,t,h,r):
 if t==1:return C
 if t==2:return {'AU':P,'AV':C,'BU':C,'BV':P}[h]
 if t==3:
  if h=='AV0':return (Z,1-lam,lam)
  return {'AV1':C,'BU0':C,'BU1':Q}.get(h,P)
 return Q if 100*r<F(2501,100) else P
def joint(lam,t,h,r):
 a,s,z,k,m=coeff(lam)
 if t==1:return C
 if t==2:
  if h in ('AU','BU'):return (a,Z,1-a)
  return (1-s,Z,s) if h=='AV' else P
 if t==3:
  if h in ('AU0','AU1'):return Q
  if h in ('AV0','AV1'):return (Z,(s-z)/s,z/s)
  if h=='BU0':return C
  if h=='BU1':return (Z,m/(1-a),1-m/(1-a))
  return P
 if r==F(1,4):return (k/z,1-k/z,Z)
 return Q if 100*r<F(2501,100) else P
def outcome(policy):
 ans=[Z]*16
 for leaf,(q,r4,_) in N[4].items():
  alive=O
  for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
   act=policy(t,h,N[t][h][1])
   assert all(v>=0 for v in act) and sum(act)==1 and (t<4 or act[2]==0)
   for j in (0,1):
    i=2*(t-1)+j;ans[i]+=q*alive*act[j];ans[8+i]+=q*r4*alive*act[j]
   alive*=act[2]
  assert alive==0
 assert sum(ans[:8])==sum(ans[8:])==1
 return ans
def tv(u,v,offset):return sum(abs(u[i]-v[i]) for i in range(offset,offset+8))/2
wq=tuple(map(F,('0','0','25/253','0','3/2024','25/253','25/253','-25/253')))
wp=tuple(map(F,('0','0','-203/506','0','0','-197/506','-197/506','203/506')))
def cost(t,r,j):
 i=2*(t-1)+j
 return wq[i]+r*wp[i]
def bellman2():
 stage3={}
 for h,(q,r,_) in N[3].items():
  cont=sum(q4*min(cost(4,r4,0),cost(4,r4,1))/q for ch,(q4,r4,pa) in N[4].items() if pa==h)
  stage3[h]=(cost(3,r,0),cost(3,r,1),cont)
 best=None;count=0
 for v1 in product(range(3),repeat=2):
  r1=dict(zip(('A','B'),v1))
  for v2 in product(range(3),repeat=3):
   count+=1;r2=dict(zip(('U','AV','BV'),v2));groups=defaultdict(list);s=Z
   for h,(q,r,_) in N[1].items():
    if r1[h]!=2:s+=q*cost(1,r,r1[h])
   for h,(q,r,parent) in N[2].items():
    if r1[parent]!=2:continue
    act=r2['U' if h in ('AU','BU') else h]
    if act!=2:s+=q*cost(2,r,act)
    else:
     for ch,(q3,r3,pa) in N[3].items():
      if pa==h:groups[ch].append(ch)
   for hs in groups.values():
    s+=min(sum(N[3][h][0]*stage3[h][d] for h in hs) for d in range(3))
   if best is None or s<best:best=s
 assert count==243
 return best,count
low,cases=bellman2()
assert low==-F(153,506)
assert max(wq)-min(wq)+max(wp)-min(wp)==1
score=lambda v:sum(wq[i]*v[i]+wp[i]*v[8+i] for i in range(8))
records={}
for lam in (LO,F(7,10),HI):
 a,s,z,k,m=coeff(lam)
 assert 0<a<1 and 0<z<=s<=1 and 0<=k<=z and 0<=m<=1-a
 f=outcome(lambda t,h,r:full(lam,t,h,r))
 v=outcome(lambda t,h,r:joint(lam,t,h,r))
 seen={}
 for t in (2,3,4):
  for h,(q,r,_) in N[t].items():
   act=joint(lam,t,h,r)
   if (t,r) in seen:assert seen[(t,r)]==act
   seen[t,r]=act
 A=(27483-39215*lam)/289432
 B=(39215*lam-26911)/289432
 assert A>=0 and B>=0 and A+B==F(1,506)
 assert tuple(v[i]-f[i] for i in range(8))==(Z,Z,A,Z,Z,B,Z,-F(1,506))
 assert tuple(v[8+i]-f[8+i] for i in range(8))==(Z,Z,-F(1,506),Z,Z,Z,Z,F(1,506))
 assert tv(f,v,0)==tv(f,v,8)==F(1,506)
 assert score(f)==-F(7,23) and low-score(f)==F(1,506)
 records[str(lam)]={'a_s_z_k_m':list(map(str,(a,s,z,k,m))),
  'Q_residual_A_B':list(map(str,(A,B))),'TV_Q':'1/506','TV_P':'1/506'}
# All displayed feasibility inequalities and observation identities are affine
# in lam; checking both rational endpoints proves them on the FULL real interval.
assert LO<F(7,10)<HI
result={'status':'PASS_EXACT_FRACTION_N4_POST_SWITCH_FLAT_PHASE',
 'interval':[str(LO),str(HI)],'phase_width':str(HI-LO),
 'd2':'1/506','d23':'1/506','d3':'(1-lambda)/2000 (previous result)',
 'strict_gap_lower':str((1-HI)/2000),'dual_min':str(low),
 'dual_oscillation':'1','bellman_prefix_cases':cases,'checked':records,
 'scope':'positive N4 external two-law tree; all real behavioral policies',
 'admission':'AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED'}
print(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2))
