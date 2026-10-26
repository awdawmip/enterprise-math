#!/usr/bin/env python3
"""Exact forward tangent scan along B-tie preserving ray after Stage151."""
from fractions import Fraction as F
from collections import defaultdict
import json
from pathlib import Path
P=(F(1,8),F(1,24),F(5,6))
K=F(45154992,127757); L=F(6412152,18251)
dK=F(-1);dL=F(-112,129)
N=14;B=(11,0,1);U=(9,4,1)
H={};D={};OPTIONS={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);ratio=F(2**(a+b),3**a)
   choices={'P':(K*ratio,dK*ratio),'Q':(L,dL)}
   if n<N:choices['C']=(F(1)+sum(P[i]*H[n+1,a+(i==0),b+(i==1)] for i in range(3)),sum(P[i]*D[n+1,a+(i==0),b+(i==1)] for i in range(3)))
   h=min(p[0] for p in choices.values())
   deriv=min(p[1] for p in choices.values() if p[0]==h)
   H[s]=h;D[s]=deriv;OPTIONS[s]=choices

assert OPTIONS[B]['Q'][0]==OPTIONS[B]['C'][0] and OPTIONS[B]['Q'][1]==OPTIONS[B]['C'][1]
assert OPTIONS[U]['P'][0]==OPTIONS[U]['C'][0]
print('U derivatives',OPTIONS[U], 'best dH',D[U])

positive=[];ties=[];bad_ties=[]
for s,o in OPTIONS.items():
 for act,(cost,deriv) in o.items():
  gap=cost-H[s];dg=deriv-D[s]
  if gap==0:
   ties.append((s,act,dg))
   if dg<0:bad_ties.append((s,act,dg))
  elif dg<0:
   positive.append((gap/(-dg),s,act,gap,dg))
assert not bad_ties,bad_ties
near=min(q[0] for q in positive)
winners=[q for q in positive if q[0]==near]
print('t*=',near,'closest closures',winners)
Knew=K+near*dK;Lnew=L+near*dL
print('Knew',Knew,'Lnew',Lnew,'slope',Knew+Lnew)
# independent exact reevaluation at candidate
from functools import lru_cache
@lru_cache(None)
def h2(s):
 n,a,b=s
 choices={'P':Knew*F(2**(a+b),3**a),'Q':Lnew}
 if n<N:choices['C']=F(1)+sum(P[i]*h2((n+1,a+(i==0),b+(i==1))) for i in range(3))
 return min(choices.values())
positive_gaps=[];exact_ties=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);opts={'P':Knew*F(2**(a+b),3**a),'Q':Lnew}
   if n<N:opts['C']=F(1)+sum(P[i]*h2((n+1,a+(i==0),b+(i==1))) for i in range(3))
   best=min(opts.values());zero=[act for act,v in opts.items() if v==best]
   if len(zero)>1:exact_ties.append((s,zero))
   positive_gaps.extend(v-best for v in opts.values() if v>best)
print('root H',h2((0,0,0)))
print('ties',exact_ties,'positive gaps',len(positive_gaps),'min gap',min(positive_gaps))
res={'start_K':str(K),'start_L':str(L),'ray_dK':str(dK),'ray_dL':str(dL),'t_star':str(near),'new_K':str(Knew),'new_L':str(Lnew),'H_root':str(h2((0,0,0))),'ties':[str(x) for x in exact_ties],'positive_gap_count':len(positive_gaps),'minimum_positive_gap':str(min(positive_gaps))}
with open(Path(__file__).resolve().parent / 'dual_stage152_candidate.json','w') as f:json.dump(res,f,indent=2)
