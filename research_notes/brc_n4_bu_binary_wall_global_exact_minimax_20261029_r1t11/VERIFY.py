#!/usr/bin/env python3
"""Exact rational N4 BU wall witness/dual; full 16-leaf tree checked separately."""
from fractions import Fraction as Q
from random import Random
O=Q(1); z=Q(0)
FQ=[Q(19,40),Q(43,120),Q(1,6),z]
FP=[Q(57,80),Q(29,240),Q(1,6),z]
GQ=[Q(19,40),Q(67,192),Q(1,6),Q(3,320)]
GP=[Q(57,80),Q(29,240),Q(151,960),Q(3,320)]
def tv(x,y):return sum((abs(a-b) for a,b in zip(x,y)),z)/2
assert sum(FQ,z)==sum(FP,z)==sum(GQ,z)==sum(GP,z)==O
assert tv(FQ,GQ)==tv(FP,GP)==Q(3,320)
def cert(A,B,c,U,V):
 s=(A-1+B-Q(1,20))/2;t=(A-1+3*(B-Q(1,20)))/4;H=B*c/4
 rQ=Q(1,6)-A*c/6-U/3-V/4;rP=Q(1,6)-A*c/6-U/12-V/2
 dQ=(s,H-s-rQ,rQ,-H);dP=(t,H-t-rP,rP,-H)
 e=max(sum(map(abs,dQ),z)/2,sum(map(abs,dP),z)/2)
 assert 0<=U<=A<=1 and 0<=V<=B<=1 and 0<=c<=1
 assert sum(dQ,z)==sum(dP,z)==0
 assert 2*A*c+7*B+16*rP-4*rQ==2+7*(B-V)
 w=(7*(1-c)/20,(7*c-3)/20,(3*c+1)/10,(7-3*c)/10)
 assert sum(w,z)==1
 assert w[0]*dQ[1]+w[1]*(dQ[0]+dQ[1])+w[2]*dP[2]+w[3]*(dP[0]+dP[2])+Q(7,20)*(V-B)==(33-39*c)/400
 if c<Q(3,7):assert e>Q(3,320) and e>=(Q(33,20)-2*c)/41
 elif c<=Q(3,4):assert min(w)>=0 and e>=(33-39*c)/400>=Q(3,320)
 else:assert e>=c/80>=Q(3,320)
 return e
assert cert(O,Q(1,20),Q(3,4),Q(7,80),Q(1,20))==Q(3,320)
rng=Random(20261029)
for _ in range(5000):
 A=Q(rng.randrange(101),100);B=Q(rng.randrange(101),100)
 c=Q(rng.randrange(101),100)
 U=A*Q(rng.randrange(101),100);V=B*Q(rng.randrange(101),100)
 cert(A,B,c,U,V)
print('PASS_N4_BU_WALL_EXACT_RATIONAL_DUAL_5000')
