#!/usr/bin/env python3
"""Exact F7 A6 noninvertible witness regressions; universal argument in PROOF.md."""
from fractions import Fraction
from itertools import product, permutations
import json

C=((1,1),(1,-1))
D=[[0]*4 for _ in range(4)]
for k in (0,2):
 for i in range(2):
  for j in range(2): D[k+i][k+j]=C[i][j]
per=(0,2,3,1)
Pi=[[int(j==per[i]) for j in range(4)] for i in range(4)]
def mm(X,Y): return [[sum(a*b for a,b in zip(r,c)) for c in zip(*Y)] for r in X]
def mv(X,y): return [sum(a*b for a,b in zip(r,y)) for r in X]
def det(X):
 return sum((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*
            X[0][p[0]]*X[1][p[1]]*X[2][p[2]]*X[3][p[3]]
            for p in permutations(range(4)))
A=mm(mm(D,Pi),D)
assert A==[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[-1,1,1,-1]]
assert det(A)==16
assert mm(D,A)==[[2*z for z in row] for row in mm(Pi,D)]
assert all(any(A[2*i+r][2*j+c] for r in range(2) for c in range(2))
           for i in range(2) for j in range(2))
def q(n,m,t=0):
 assert 0<=t<3
 return Fraction(int(n+m!=0)+int(n-m!=0),2)
unary=0
for n,m,t in product(range(-6,7),range(-6,7),range(3)):
 v=q(n,m,t)
 assert q(n,m,(t+n)%3)==v # R
 assert q(-n,m,(-t)%3)==v # J
 assert q(n,m,(-t)%3)==v # S
 assert not n or v>=Fraction(1,2)
 unary+=1
assert q(0,0)==0 and q(1,0)==1
free=0
for w in product(range(-4,5),repeat=4):
 x=mv(A,w)
 assert q(x[0],x[1])+q(x[2],x[3])==q(w[0],w[1])+q(w[2],w[3])
 free+=1
out=mv(A,(1,0,0,0))
assert out==[1,1,1,-1] and q(out[0],out[1])==q(out[2],out[3])==Fraction(1,2)
assert mv(D,(1,0,0,0))==[1,1,0,0] # not in image: every D*A*w is even
for ta,tb in product(range(3),repeat=2):
 assert q(1,2,ta)+q(-3,4,tb)==q(1,2)+q(-3,4)
print(json.dumps({"result":"EXACT_REGRESSION_PASS","A":A,"det":det(A),
                  "channel_identity":"D*A=2*Pi*D","pair_cases":free,
                  "unary_cases":unary,"marked_output":out,"marked_q_each":"1/2",
                  "torsion":"identity; 9 labels symbolically",
                  "native_review":False},indent=2))
