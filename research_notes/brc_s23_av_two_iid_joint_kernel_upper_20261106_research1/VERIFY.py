#!/usr/bin/env python3
"""Exact S23/AV two-iid universal joint reconstruction certificate."""
from fractions import Fraction as Q
from itertools import product
CORNERS = tuple(product((Q(1, 2), Q(7, 8)), repeat=2))
LOWER, OLD_UPPER, NEW_UPPER = Q(423,2468), Q(18549,78400), Q(235,1144)
V,T,U,W=Q(8,11),Q(10,13),Q(9,80),Q(3,520)
checks=0
def check(ok,label):
 global checks
 assert ok,label
 checks+=1
def av(a,c):
 z=(1-a)*c
 return (a,z,1-a-z)
def compressed(a,c):
 z=(1-a)*c
 return (z,1-z)
def tensor(p,q): return tuple(x*y for x in p for y in q)
def tv_signed(d): return sum(abs(v) for v in d)/2
def bayes(p,q,prior_hi):
 return sum(min((1-prior_hi)*x,prior_hi*y) for x,y in zip(p,q))
L=[[Q(0) for j in range(9)] for i in range(4)]
L[0][4]=Q(1)
L[1][3],L[1][5]=V,1-V
L[2][1],L[2][7]=V,1-V
L[3][0],L[3][2],L[3][6],L[3][8]=T,U,U,W
for i,row in enumerate(L):
 check(sum(row)==1 and all(x>=0 for x in row),f'stochastic row {i}')
def swap_out(j): return 3*(j%3)+(j//3)
def swap_bin(i): return 2*(i%2)+(i//2)
for i in range(4):
 check(all(L[swap_bin(i)][swap_out(j)]==L[i][j] for j in range(9)),f'exchange covariance {i}')
F=[]
for h,(a,c) in enumerate(CORNERS):
 check(sum(av(a,c))==1 and sum(compressed(a,c))==1,f'corner law {h}')
for i in range(4):
 row=[]
 for j in range(4):
  b2=tensor(compressed(*CORNERS[i]),compressed(*CORNERS[j]))
  a2=tensor(av(*CORNERS[i]),av(*CORNERS[j]))
  recon=tuple(sum(b2[k]*L[k][p] for k in range(4)) for p in range(9))
  check(sum(recon)==1,f'joint reconstructed law {i},{j}')
  row.append(tuple(a2[p]-recon[p] for p in range(9)))
 F.append(row)
certificate=[]
for i in range(4):
 for j in range(i,4):
  d=tuple((F[i][j][k]+F[j][i][k])/2 for k in range(9))
  value=tv_signed(d)
  check(value<=NEW_UPPER,f'symmetrized corner {i},{j}')
  certificate.append((i,j,value))
check(max(x[2] for x in certificate)==NEW_UPPER,'symmetrized maximum')
check(tv_signed(F[0][0])==NEW_UPPER,'attainment')
p=Q(256,617)
a0=tensor(av(*CORNERS[0]),av(*CORNERS[0]))
a1=tensor(av(*CORNERS[3]),av(*CORNERS[3]))
b0=tensor(compressed(*CORNERS[0]),compressed(*CORNERS[0]))
b1=tensor(compressed(*CORNERS[3]),compressed(*CORNERS[3]))
check(bayes(a0,a1,p)==Q(601,2468),'full Bayes risk')
check(bayes(b0,b1,p)==Q(256,617),'binary Bayes risk')
check(bayes(b0,b1,p)-bayes(a0,a1,p)==LOWER,'lower bound')
check(LOWER<=NEW_UPPER<OLD_UPPER,'strict improvement')
check(OLD_UPPER-NEW_UPPER==Q(349507,11211200),'exact difference')
print('PASS_S23_AV_TWO_IID_SYMMETRIZED_JOINT_KERNEL_EXACT_20261106')
print('CHECKS',checks)
print('FROZEN_INPUT','43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('KERNEL_PARAMS','v='+str(V),'t='+str(T),'u='+str(U),'w='+str(W))
print('LOWER',LOWER,'OLD_UPPER',OLD_UPPER,'NEW_UPPER',NEW_UPPER)
print('EXACT_UPPER_IMPROVEMENT',OLD_UPPER-NEW_UPPER)
print('SYMMETRIZED_CORNER_CERTIFICATE')
for i,j,value in certificate: print(f'{i},{j}',value)
print('ATTAINMENT',CORNERS[0],tv_signed(F[0][0]))
