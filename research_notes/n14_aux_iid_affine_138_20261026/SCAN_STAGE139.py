#!/usr/bin/env python3
"""Independent exact rational dual-ray candidate scan Stage138 -> Stage139.
This gives dual candidate only and does not assert primal attainment.
"""
from fractions import Fraction as F
import json
N=14;P=(F(1,8),F(1,24),F(5,6));B=(11,0,1);H=(11,4,1)
K=F(3709800,6941);L=F(3529544,6941);dK=-F(1);dL=-F(112,129)
def states(n): return ((n,a,b) for a in range(n+1) for b in range(n-a+1))
def children(s):
 n,a,b=s; return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
base={};dbase={};close=[];at0=[]
for n in range(N,-1,-1):
 for s in states(n):
  n,a,b=s;r=F(2**(a+b),3**a)
  cost={'P':K*r,'Q':L};der={'P':dK*r,'Q':dL}
  if n<N:
   cost['C']=1+sum((P[j]*base[c] for j,c in enumerate(children(s))),F(0))
   der['C']=sum((P[j]*dbase[c] for j,c in enumerate(children(s))),F(0))
  m=min(cost.values());actions=[a for a,x in cost.items() if x==m]
  dm=min(der[a] for a in actions)
  base[s]=m;dbase[s]=dm
  if len(actions)>1:at0.append((s,actions,[(a,str(der[a])) for a in actions]))
  for a,v in cost.items():
   gap=v-m;gap_der=der[a]-dm
   if gap==0 and gap_der<0: raise RuntimeError(('invalid direction',s,a))
   if gap>0 and gap_der<0:close.append((gap/-gap_der,s,a))
close.sort()
print('ties_at_start',at0)
print('closures',len(close),'minfirst',close[:6])
t,critical,action=close[0];k1=K+t*dK;l1=L+t*dL
nextH={};nextties=[];gaps=[]
for n in range(N,-1,-1):
 for s in states(n):
  n,a,b=s;r=F(2**(a+b),3**a)
  c={'P':k1*r,'Q':l1}
  if n<N:c['C']=1+sum((P[j]*nextH[x] for j,x in enumerate(children(s))),F(0))
  m=min(c.values());nextH[s]=m
  sel=[k for k,v in c.items() if v==m]
  if len(sel)>1:nextties.append((s,sel))
  gaps.extend((v-m for v in c.values() if v>m))
result={'t':str(t),'K139':str(k1),'L139':str(l1),'next_critical':str(critical),'closing_action':action,'positive_ray_closing_candidates':len(close),'min_gap':str(min(gaps)),'num_positive_gaps':len(gaps),'ties':[[str(s),a] for s,a in nextties],'Hroot':str(nextH[(0,0,0)]),'status':'DUAL_CANDIDATE_ONLY'}
with open('/mnt/data/scan139.json','w') as f:json.dump(result,f,indent=2)
print('STAGE139_DUAL_CANDIDATE',json.dumps(result,indent=2))
