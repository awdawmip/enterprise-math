#!/usr/bin/env python3
"""Exact rational-GF certificate and integer DP for the R4-EC7 auxiliary BRC."""
from collections import defaultdict
from itertools import product
import sympy as s
E={0:((2,-1,-1),(2,1,-1)),1:((0,-1,-1),(0,1,-1)),2:((1,1,1),(2,1,-1))}
R=((1,0),(2,0),(2,2))
S=[(q,r,e) for q in range(3) for r in (0,1) for e in (1,-1)]
I={state:i for i,state in enumerate(S)}
x=s.symbols('x')
e0=s.zeros(12,1);e0[I[(0,0,1)]]=1

def mats(sign):
    A=s.zeros(12);B=s.zeros(12)
    for j,(q,r,e) in enumerate(S):
        for a,(qp,eta,b) in enumerate(E[q]):
            rp=R[r][a]
            if rp==2:continue
            assert e*eta*b==e*(1-2*a)
            i=I[(qp,rp,e*eta)]
            if e*eta*b==sign:A[i,j]+=1
            else:B[i,j]+=1
    return A,B

for sign in (1,-1):
    A,B=mats(sign)
    M=s.eye(12)-x*A
    assert s.factor(M.det())==1-x
    J=M.inv()
    v=J*e0
    for _ in range(3):
        v=J*(x*B*v)
    if sign==1:
        formulas=(x**3*(x**3-x**2+1)/(1-x),x**8/(1-x)**2)
    else:
        formulas=(x**3*(x**2-x+1)/(1-x),x**7/(1-x)**2)
    for r,expected in enumerate(formulas):
        assert s.cancel(v[I[(2,r,sign)]]-expected)==0,(sign,r)
print('PASS: exact rational generating functions')

def move(state,a):
    q,r,e,k=state
    qp,eta,b=E[q][a]
    return (qp,R[r][a],e*eta,k*eta+b)

D={(0,0,1,0):1}
for n in range(151):
    assert sum(D.values())==2**n
    if n<=13:
        brute=defaultdict(int)
        for word in product((0,1),repeat=n):
            z=(0,0,1,0)
            for a in word:z=move(z,a)
            brute[z]+=1
        assert dict(brute)==dict(D)
    if n>=7:
        k=n-6
        assert (D.get((2,0,1,k),0),D.get((2,1,1,k),0))==(1,n-7),n
        assert (D.get((2,0,-1,k),0),D.get((2,1,-1,k),0))==(1,n-6),n
    if n!=150:
        ND=defaultdict(int)
        for z,count in D.items():
            for a in (0,1):ND[move(z,a)]+=count
        D=ND
print('PASS: brute 0..13, exact DP 0..150')
