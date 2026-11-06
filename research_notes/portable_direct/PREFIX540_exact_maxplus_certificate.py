#!/usr/bin/env python3
"""Rooted first-axis BRC max-plus exact certificate, X6 frozen f42f2906."""
from collections import Counter, defaultdict
import json
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*x for x in STARS[a] if x!=abs(c))
P=tuple((a,p,e*x) for a in range(4) for x in STARS[a] for e in (-1,1) for p in near(a,e*x))
IX={x:i for i,x in enumerate(P)}
def successors(x):
 a,p,c=x
 b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
 return tuple(IX[y] for y in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
NX=tuple(successors(x) for x in P)
def sig(i):return (1 if P[i][2]>0 else -1) if abs(P[i][2])==1 else 0
def ep(i):return int(abs(P[i][2])==1)
def tau(r,i,j):
 n=ep(i)+ep(j)-abs(sig(j)-r)+abs(sig(i)-r)
 assert n%2==0 and n//2 in (0,1)
 return n//2
def step(r,v):return [max(tau(r,i,j)+v[j] for j in NX[i]) for i in range(48)]
assert len(P)==48 and len(IX)==48 and all(len(js)==3 and len(set(js))==3 for js in NX)
assert sum(map(len,NX))==144
periods={}
for r,period,shift in ((-1,6,2),(0,3,1),(1,6,2)):
 v=[0]*48;first=[tuple(v)]
 for _ in range(6):v=step(r,v);first.append(tuple(v))
 assert first[period]==(shift,)*48
 periods[r]=(period,shift,first)
classes=[]
for i in range(48):
 r=sig(i)
 if r:
  classes.append('SIGNED')
  assert [periods[r][2][d][i] for d in range(6)]==[0,0,0,0,1,1]
 else:
  fast=any(ep(j) for j in NX[i]);classes.append('FAST' if fast else 'DELAYED')
  assert [periods[r][2][d][i] for d in range(3)]==[0,0,int(fast)]
assert Counter(classes)=={'FAST':24,'DELAYED':16,'SIGNED':8}
def formula(i,d):
 if classes[i]=='SIGNED':
  k,b=divmod(d,6);return 2*k+int(b in (4,5))
 k,b=divmod(d,3);return k+int(b==2 and classes[i]=='FAST')
for i in range(48):
 states={(i,0):1};r=sig(i)
 for d in range(37):
  m=-1;total=0
  for (last,K),count in states.items():
   x=K-abs(sig(last)-r)
   assert x>=0 and x%2==0
   m=max(m,x//2);total+=count
  assert total==6**d and m==formula(i,d)
  if d<36:
   nxt=defaultdict(int)
   for (last,K),count in states.items():
    for j in NX[last]:nxt[(j,K+ep(last)+ep(j))]+=2*count
   states=nxt
for r in (-1,0,1):
 v=[0]*48
 for d in range(241):
  for i in range(48):
   if sig(i)==r:assert v[i]==formula(i,d)
  v=step(r,v)
def slots(m,H):return sum(max(0,m-h+1) for h in range(H+1))
savings={}
for d in range(37):
 H=(d+2)//4;u=(d+1)//3
 old=48*slots(u,H);new=sum(slots(formula(i,d),H) for i in range(48))
 assert new<=old
 savings[d]=(old,new,old-new)
assert savings[20]==(1584,1440,144) and savings[23]==(2016,1848,168) and savings[24]==(2016,2016,0)
result={'status':'ALL_CHECKS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'model':{'phases':48,'edges':144,'microstep_labels_per_edge':2},
 'max_plus_period_identity':{'r0':[3,1,48],'r_plus':[6,2,48],'r_minus':[6,2,48]},
 'root_classes':dict(Counter(classes)),'raw_endpoint_checks':48*37,'maxplus_crosschecks':'all roots, 0..240',
 'root_phase_classes': [{'phase_index':i,'phase':list(P[i]),'type':classes[i]} for i in range(48)],
 'histogram_support_savings':{str(d):{'global_slots':a,'root_slots':b,'saved':c} for d,(a,b,c) in savings.items()},
 'review':'AUTHOR_PROVED / EXACT_FINITE_IDENTITY / RAW_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED'}
with open('PREFIX540_EXACT_EXECUTION_SUMMARY.json','w') as f:json.dump(result,f,indent=2)
print('ALL_CHECKS_PASS',result['root_classes'],savings[20],savings[23],savings[24])
