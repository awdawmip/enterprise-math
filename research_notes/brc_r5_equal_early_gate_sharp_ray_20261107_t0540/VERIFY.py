#!/usr/bin/env python3
"""Exact R5 equal-early-gate critical-ray certificate (Python stdlib Fraction)."""
from fractions import Fraction as F
q2=(F(1,2),F(1,2));r2=(F(3,4),F(5,4))
q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
r3=(F(1,2),F(1),F(3,2));r4=(F(1,10),F(1),F(19,10))
q4={(i,0):(F(509,900),F(382,900),F(9,900)) for i in range(2)}
q4.update({(i,2):(F(9,900),F(382,900),F(509,900)) for i in range(2)})
q4[0,1]=(F(47,180),F(43,90),F(47,180))
q4[1,1]=(F(67,162),F(14,81),F(67,162))
assert sum(q2)==sum(q2[i]*r2[i] for i in range(2))==1
for i in range(2):
 assert sum(q3[i])==1
 assert sum(q3[i][j]*r3[j] for j in range(3))==r2[i]
 for j in range(3):
  assert all(p>0 for p in q4[i,j]) and sum(q4[i,j])==1
  assert sum(q4[i,j][k]*r4[k] for k in range(3))==r3[j]
row1=tuple((4*q4[0,1][k]+9*q4[1,1][k])/13 for k in range(3))
assert row1==(F(11,30),F(4,15),F(11,30))
V=(F(27,80),F(13,40),F(27,80))
W0=(F(161801,180000),F(6499,18000),F(267,80),F(137,40))
H=F(16917,4642820); OLD=F(9,2500);r=(F(1,10),F(1,2),F(1),F(3,2),F(19,10))
assert H>OLD
def masses(t,x):
 a,b,c=x
 return (F(509,900)*a+F(11,30)*b+F(1,100)*c,
         V[0]*t-a,
         1-t+V[1]*t-b+F(191,450)*(a+c)+F(4,15)*b,
         V[2]*t-c,
         F(1,100)*a+F(11,30)*b+F(509,900)*c)
def check(t,x,E,h):
 m=masses(t,x)
 assert 0<=t<=1 and all(0<=x[j]<=V[j]*t for j in range(3))
 assert all(0<=E[j]<=m[j] for j in range(5))
 assert sum(m)==sum(m[j]*r[j] for j in range(5))==1
 w=(1-sum(r[j]*E[j] for j in range(5)),sum(E),
    1+2*t+x[0]/2+x[1]+3*x[2]/2,1+2*t+sum(x))
 assert w==tuple(W0[j]+h*(1,1,1,-1)[j] for j in range(4))
 return m
center=(F(77,80),(F(3,16),F(3,10),F(1,80)),
        (F(1297,6000),F(879,6400),F(563,144000),F(0),F(349,96000)),F(0))
t=F(31911,33163)
x=(F(3199433,18571280),F(31911,102040),F(220131,18571280))
E=(F(886766809,4178538000),F(1415873,9285640),F(0),F(0),F(0))
end=(t,x,E,H)
m0=check(*center);m1=check(*end)
assert x[1]==V[1]*t and E[0]==m1[0] and E[1]==m1[1]
for s in (F(0),F(1,7),F(1,4),F(1,2),F(2,3),F(1)):
 ts=(1-s)*center[0]+s*t
 xs=tuple((1-s)*center[1][j]+s*x[j] for j in range(3))
 Es=tuple((1-s)*center[2][j]+s*E[j] for j in range(5))
 check(ts,xs,Es,s*H)
# Exact 10-coordinate dual coefficient identity.
N=10
def row(terms):
 arr=[F(0)]*N
 for i,v in terms.items():arr[i]=F(v)
 return tuple(arr)
A=[row({0:2,1:1,2:1,3:1,9:1}),
   row({0:2,1:F(1,2),2:1,3:F(3,2),9:-1}),
   row({4:1,5:1,6:1,7:1,8:1,9:-1}),
   row({4:r[0],5:r[1],6:r[2],7:r[3],8:r[4],9:1})]
B=(F(97,40),F(187,80),F(6499,18000),F(18199,180000))
C=[row({0:-V[1],2:1}),
   row({1:-F(509,900),2:-F(11,30),3:-F(1,100),4:1}),
   row({0:-V[0],1:1,5:1}),
   row({6:-1}),row({7:-1}),row({8:-1})]
lam=(21126,-13604,-83401,114010)
mu=(18878,72000,26396,30609,87614,133218)
assert all(sum(lam[i]*A[i][j] for i in range(4))+
           sum(mu[i]*C[i][j] for i in range(6)) == (232141 if j==9 else 0)
           for j in range(N))
assert sum(lam[i]*B[i] for i in range(4))==232141*H
assert all(c>=0 for c in mu)
print("center_histogram=",tuple(map(str,m0)))
print("endpoint_histogram=",tuple(map(str,m1)))
print("endpoint_t=",t,"X=",tuple(map(str,x)))
print("endpoint_E=",tuple(map(str,E)))
print("sharp_upper_h=",H,"approx=",float(H))
print("improvement_over_9/2500=",H/OLD,"percent=",100*(H/OLD-1))
print("exact_dual_multipliers=",lam,mu,"denominator=232141")
print("all_real_interval= [0, 16917/4642820] by affine feasibility")
print("PASS_EXACT_R5_EQUAL_EARLY_GATE_SHARP_RAY")
