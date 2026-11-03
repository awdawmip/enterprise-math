#!/usr/bin/env python3
"""Exact K3 common-label physical source-flow and signed-hull verification."""
from fractions import Fraction as F
from itertools import product

alpha=(F(1,2),F(2,3),F(1,2),F(3,4))
VF=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
VL=((0,0,0),(0,1,1),(1,0,0),(1,1,0))
stages=((0,0,0),(1,0,0),(1,1,0),(1,1,1))
base=dict(p=(F(1,4),F(1,2),F(3,4),F(1,2)),
          q=(F(3,4),F(1,2),F(1,4),F(1,2)),r=(F(3,4),)*4,v=(F(3,4),)*4)
mixed=dict(p=(F(1,5),F(2,3),F(3,5),F(4,7)),
           q=(F(3,5),F(2,7),F(7,8),F(1,3)),
           r=(F(1,3),F(2,5),F(3,7),F(4,9)),
           v=(F(2,7),F(3,8),F(5,9),F(4,5)))
nP=(F(8),F(0),F(-8,9),F(88,9));nQ=(F(0),F(-32),F(0),F(8))
normals=(nP,nQ,(F(0),F(0),F(-1),F(4)),(F(7),F(-3),F(5),F(-2)),(F(-1),F(2),F(-3),F(4)))
checks=0
def ok(x):
 global checks
 checks+=1; assert x

def obs(t,x,y,i,rows):
 x,y,i=F(x),F(y),F(i)
 d=y/16+3*i/32
 w=(F(1,4),(1-x)/4,y/8,i/8)
 m=[w[s]*alpha[s]*rows[s][0] for s in range(4)]
 S=[F(2,3)*m[s]*rows[s][1] for s in range(4)]
 U=[S[s]*rows[s][2] for s in range(4)]
 return (F(107,128)-21*x/128+d/4-sum(S)/2+sum((t['p'][s]*S[s]/8 for s in range(4)),F(0)),
         F(13,64)+3*x/64-d/2+sum(S)/8+sum((t['q'][s]*S[s]/32 for s in range(4)),F(0)),
         3+sum(m)+F(3,2)*sum(S)+sum((t['r'][s]*U[s] for s in range(4)),F(0)),
         3+sum(m)/2+F(3,8)*sum(S)+sum((t['v'][s]*U[s]/4 for s in range(4)),F(0)))

def dot(n,v):return sum((a*b for a,b in zip(n,v)),F(0))

def envelope(t,n,full):
 A,B,C,D=n;K=C+D/2;L=-A/2+B/8+3*C/2+3*D/8
 H=[A*t['p'][s]/8+B*t['q'][s]/32 for s in range(4)]
 T=[C*t['r'][s]+D*t['v'][s]/4 for s in range(4)]
 best=None
 for x0,y0,i0 in (VF if full else VL):
  x,y,i=F(x0),F(y0),F(i0);d=y/16+3*i/32
  c=[w*a for w,a in zip((F(1,4),(1-x)/4,y/8,i/8),alpha)]
  b=A*(F(107,128)-21*x/128+d/4)+B*(F(13,64)+3*x/64-d/2)+3*(C+D)
  vals=[(F(0),K,K+F(2,3)*(L+H[s]),K+F(2,3)*(L+H[s]+T[s])) for s in range(4)]
  z=b+(sum((c[s]*max(vals[s]) for s in range(4)),F(0)) if full else
       max(sum((c[s]*vals[s][j] for s in range(4)),F(0)) for j in range(4)))
  best=z if best is None else max(best,z)
 return best

def exhaustive(t,n,full):
 best=None
 for x,y,i in (VF if full else VL):
  choices=product(range(4),repeat=4) if full else ((j,)*4 for j in range(4))
  for js in choices:
   z=dot(n,obs(t,x,y,i,tuple(stages[j] for j in js)))
   best=z if best is None else max(best,z)
 return best

def rows(t,s,law,action):
 h=F(1,2)+t['p'][s]/8 if law=='P' else F(1,2)-t['q'][s]/8
 d=t['r'][s] if law=='P' else t['v'][s]
 for B,D,L in product((0,1),repeat=3):
  prob=F(1,2)*(d if D else 1-d)*(h if L else 1-h)
  yield prob,5+B+action*D,L

for t in (base,mixed):
 for k in ('p','q','r','v'):ok(all(0<z<1 for z in t[k]))
 for s in range(4):
  for law in ('P','Q'):
   for action in (0,1):
    R=tuple(rows(t,s,law,action))
    ok(len(R)==8 and all(prob>0 for prob,_,_ in R))
    ok(sum((prob for prob,_,_ in R),F(0))==1)
    ok(sum((prob for prob,_,L in R if L==(law=='P')),F(0))==
       F(1,2)+(t['p'][s] if law=='P' else t['q'][s])/8)
    ok(sum((prob*time for prob,time,_ in R),F(0))==
       F(11,2)+action*(t['r'][s] if law=='P' else t['v'][s]))
 for n in normals:
  for full in (True,False):ok(envelope(t,n,full)==exhaustive(t,n,full))
 # Nonbinary policy: changing only u affects clocks, never common-label errors.
 x,y,i=F(1,5),F(2,3),F(1,10)
 zs=(F(1,3),F(2,5),F(3,7),F(4,9));ts=(F(3,8),F(4,7),F(1,2),F(5,9))
 us=(F(1,11),F(2,9),F(3,5),F(4,7))
 aa=obs(t,x,y,i,tuple(zip(zs,ts,us)))
 bb=obs(t,x,y,i,tuple(zip(zs,ts,(F(0),)*4)))
 ok(aa[:2]==bb[:2]);ok(aa[2]>bb[2]);ok(aa[3]>bb[3])

W=obs(base,0,1,1,(stages[1],stages[1],stages[3],stages[1]))
ok(W==(F(659,768),F(401,3072),F(85,24),F(1247,384)))
pf,pl=envelope(base,nP,True),envelope(base,nP,False)
qf,ql=envelope(base,nQ,True),envelope(base,nQ,False)
ok((pf,pl,qf,ql)==(F(1135,32),F(851,24),F(2093,96),F(523,24)))
ok(dot(nP,W)==pf and dot(nQ,W)==qf)
ok(pf-pl==qf-ql==F(1,96))
ok((pf-pl)/sum(map(abs,nP))==F(1,1792))
print('EXACT_K3_COMMON_LABEL_PHYSICAL_OBSERVER')
print('FULL_deterministic_vertices=1536 LR_deterministic_vertices=16')
print('tested_kernels=2 directions=5 full_and_lr_envelopes=20')
print('full_supports',pf,qf)
print('lr_supports',pl,ql)
print('gaps',pf-pl,qf-ql)
print('FULL_witness',*W)
print('distance_infty_at_least',F(1,1792))
print('exact_assertions',checks)
print('PASS_EXACT_R5_K3_COMMON_LABEL_STRICT_PHYSICAL_BRIDGE')
