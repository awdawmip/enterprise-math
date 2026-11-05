#!/usr/bin/env python3
"""Exact S23/AV two-iid joint-kernel certificate: all calculations rational."""
from fractions import Fraction as Q
from itertools import product

CORNERS=list(product((Q(1,2),Q(7,8)),repeat=2))
LOWER,OLD,UPPER=Q(423,2468),Q(235,1144),Q(947,5000)
COUNTS=(
 (0,0,0,0,10000,0,0,0,0),
 (0,239,0,5881,0,0,2436,1111,333),
 (0,5881,2436,239,0,1111,0,0,333),
 (7534,321,912,321,0,0,912,0,0)
)
L=tuple(tuple(Q(x,10000) for x in row) for row in COUNTS)
checks=0
def chk(p,label):
 global checks
 assert p,label
 checks+=1
def av(a,c):
 z=(1-a)*c
 return (a,z,1-a-z)
def binary(a,c):
 z=(1-a)*c
 return (z,1-z)
def tensor(a,b):
 return tuple(x*y for x in a for y in b)
def recover(p):
 return tuple(sum(p[z]*L[z][k] for z in range(4)) for k in range(9))
def tv(d):return sum(abs(x) for x in d)/2
def bayes(x,y,t):return sum(min((1-t)*a,t*b) for a,b in zip(x,y))
def swap9(j):return 3*(j%3)+(j//3)
def swap4(i):return 2*(i%2)+(i//2)

for i,row in enumerate(L):
 chk(sum(row)==1 and all(v>=0 for v in row),f'row {i} stochastic')
 chk(all(L[swap4(i)][swap9(j)]==row[j] for j in range(9)),f'row {i} symmetric')
Ai=[av(*p) for p in CORNERS];Bi=[binary(*p) for p in CORNERS]
for i in range(4):
 chk(sum(Ai[i])==sum(Bi[i])==1,f'corner {i} law')
F={}
for i in range(4):
 for j in range(4):
  true=tensor(Ai[i],Ai[j]); observed=tensor(Bi[i],Bi[j])
  reconstructed=recover(observed)
  chk(sum(true)==sum(observed)==sum(reconstructed)==1,f'ordered {i},{j}')
  F[i,j]=tuple(true[k]-reconstructed[k] for k in range(9))
cert=[]
for i in range(4):
 for j in range(i,4):
  g=tuple((F[i,j][k]+F[j,i][k])/2 for k in range(9))
  z=tv(g)
  chk(z<=UPPER,f'symmetrized {i},{j}')
  cert.append((i,j,z))
chk(max(z for i,j,z in cert)==UPPER,'sharp certificate')
chk(tv(F[0,0])==UPPER,'attainment at theta0')
p=Q(256,617)
ra=bayes(tensor(Ai[0],Ai[0]),tensor(Ai[3],Ai[3]),p)
rb=bayes(tensor(Bi[0],Bi[0]),tensor(Bi[3],Bi[3]),p)
chk(ra==Q(601,2468),'full Bayes risk')
chk(rb==Q(256,617),'binary Bayes risk')
chk(rb-ra==LOWER,'lower bound')
chk(LOWER<=UPPER<OLD,'upper strictly improves')
chk(OLD-UPPER==Q(5727,357500),'exact improvement')
print('PASS_S23_AV_TWO_IID_JOINT_KERNEL_947_5000_EXACT_20261106')
print('CHECKS',checks)
print('FROZEN_INPUT','43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('KERNEL_DENOMINATOR',10000)
for i,row in enumerate(COUNTS):print('ROW',i,','.join(map(str,row)))
print('SYMMETRIZED_CORNER_CERTIFICATE')
for i,j,z in cert:print(i,j,z)
print('LOWER',LOWER,'UPPER',UPPER,'OLD_UPPER',OLD)
print('IMPROVEMENT',OLD-UPPER)
print('ATTAINMENT',CORNERS[0],tv(F[0,0]))
