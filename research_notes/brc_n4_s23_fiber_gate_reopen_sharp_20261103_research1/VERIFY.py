#!/usr/bin/env python3
"""Source-labeled BRC S23 exact Fraction reproduction; no floating arithmetic."""
from fractions import Fraction as Q
from itertools import product
import json
A=(0,0,0,1,1,1);B=(2,2,3,2,2,4);C=(5,6,7,8,9,10)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
def obs(t,h):
 z=(Q(1,3),Q(5,6),t,Q(1,2),Q(1,2),h[0],h[1],Q(1),h[2],h[3],Q(1,3))
 r=[(a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)) for a,b,c in ((z[A[i]],z[B[i]],z[C[i]]) for i in range(6))]
 return tuple(tuple(sum((Q(M[i][j],20)*r[j][k] for j in range(6)),Q(0)) for k in range(4)) for i in range(6))
def tv(u,v):return sum(map(abs,(x-y for x,y in zip(u,v))),Q(0))/2
def dd(p,q):return max(tv(p[i],q[i]) for i in range(6))
def inv(t,p,q):
 u=[(p[i][2]-q[i][2])/(1-t) for i in (0,1,3,4)]
 return (Q(33,2)*u[0]-15*u[1],-Q(27,2)*u[0]+15*u[1],Q(27,2)*u[2]-Q(15,2)*u[3],-Q(3,2)*u[2]+Q(15,2)*u[3])
T=((Q(1,3),Q(1,3),0,0),(Q(3,10),Q(11,30),0,0),
   (0,0,Q(1,12),Q(1,12)),(0,0,Q(1,60),Q(3,20)))
assert max(sum(map(abs,row)) for row in T)==Q(2,3)
pts=list(product((Q(0),Q(1,2),Q(1)),repeat=4))
corner=list(product((Q(0),Q(1)),repeat=4))
betas=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
for h in pts: assert obs(Q(1),h)==obs(Q(1),pts[0])
count=0
for t in betas:
 for h in pts: assert all(sum(row)==1 for row in obs(t,h))
 for h in corner:
  p=obs(t,h)
  for g in corner:
   q=obs(t,g);d=tuple(a-b for a,b in zip(h,g));n=max(map(abs,d))
   y=tuple(sum(a*b for a,b in zip(row,d)) for row in T)
   err=dd(p,q)
   assert err==(1-t)*max(map(abs,y))
   assert Q(2,63)*(1-t)*n<=err<=Q(2,3)*(1-t)*n
   if t<1:assert inv(t,p,q)==d
   count+=1
 for a,b,expected in (((Q(1),Q(1),Q(0),Q(0)),(Q(0),)*4,Q(2,3)),):
  assert dd(obs(t,a),obs(t,b))==(1-t)*expected
 assert dd(obs(t,(Q(1),Q(0),Q(0),Q(0))),obs(t,(Q(0),Q(19,21),Q(0),Q(0))))==Q(2,63)*(1-t)
for t in betas[:-1]:
 for h in pts: assert inv(t,obs(t,h),obs(t,(Q(0),)*4))==h
print(json.dumps({'marker':'PASS_BRC_S23_FIBER_GATE_SHARP_20261103','frozen_science':'43ec6098b1330ae86d0a7863be336c5d97f6ef34','beta_values':['0','1/4','1/2','3/4','1'],'fiber_points':81,'corner_pairs':count,'bounds':'2(1-beta)/63 and 2(1-beta)/3; both sharp','arithmetic':'Python Fraction; full source labeled model','scope':'finite exact checks; real-domain algebra proved in PROOF.md'},indent=2))
