#!/usr/bin/env python3
# Adaptation of frozen prior replay 949c4114b1882b37b60e4e7de05d7ce9933fb33b.
from fractions import Fraction as F
from math import floor, comb, lcm
from itertools import product, combinations_with_replacement, groupby
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
from collections import Counter
import hashlib,json,time,sys
P,CAP,N=13,2331,12
W=[P*r-1 for r in range(1,P)]
H=[[pow(r,-k,P**k) for r in range(1,P)] for k in range(1,7)]
def solve(target):
    x=[0]*N; A=[[int(i==j) for j in range(N)] for i in range(N)]
    for k,h in enumerate(H,1):
        mod=P**k;t=(target[k-1]-sum(a*b for a,b in zip(x,h)))%mod
        v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
        piv=next(i for i,y in enumerate(v) if y%P);inv=pow(v[piv],-1,mod);old=A[piv]
        x=[a+(t*inv%mod)*b for a,b in zip(x,old)]
        A=[[mod*a for a in row] if i==piv else [a-(v[i]*inv%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
    assert all((sum(a*b for a,b in zip(x,h))-target[k-1])%P**k==0 for k,h in enumerate(H,1))
    return x,A
_,A=solve([0]*6);M=Matrix(A);assert abs(M.det())==P**21
Rw=(hermite_normal_form(M.T).T*Matrix.diag(*W)).lll(delta=F(3,4))
U=Rw*Matrix.diag(*(F(1,w) for w in W));assert all(x.q==1 for x in U)
assert abs(U.det())==P**21
assert all(sum(int(U[j,t])*h[t] for t in range(N))%P**k==0 for j in range(N) for k,h in enumerate(H,1))
UI=U.inv();G=Rw*Rw.T
mu=[[F(0)]*N for _ in range(N)];D=[]
for i in range(N):
    for j in range(i):mu[i][j]=(F(int(G[i,j]))-sum(mu[i][t]*mu[j][t]*D[t] for t in range(j)))/D[j]
    D.append(F(int(G[i,i]))-sum(mu[i][j]**2*D[j] for j in range(i)))
dmin=min(D);assert dmin>2*CAP**2
Urows=[[int(U[j,t]) for t in range(N)] for j in range(N)]
# Positive target corresponds to subtracting the negative vertical roster.
C0={(q,r):[F(x) for x in Matrix(1,N,solve([pow(P*q+r,-k,P**k) for k in range(1,7)])[0])*UI] for q in range(1,13) for r in range(1,13)}
C0={k:[x-floor(x) for x in v] for k,v in C0.items()}
B=lcm(*(x.denominator for v in C0.values() for x in v)); C={a:[int(x*B) for x in v] for a,v in C0.items()}
# Exact scaling: center = (L_i*c_i + sum_j M_ji*z_j)/(B*L_i)
L=[lcm(*(mu[j][i].denominator for j in range(i+1,N))) for i in range(N)]
MM=[[int(mu[j][i]*L[i]) for j in range(i+1,N)] for i in range(N)]
K=[D[i]/(B*L[i])**2 for i in range(N)];Q=lcm(*(x.denominator for x in K));T=[int(x*Q) for x in K]
def patterns(total,length,low=1):
    if length==0:
        if total==0:yield ()
        return
    for q in range(low,total+1):
        for t in patterns(total-q,length-1,q):yield (q,)+t
def rosters(pat):
    groups=[len(tuple(g)) for _,g in groupby(pat)]
    for blocks in product(*(combinations_with_replacement(range(1,P),k) for k in groups)):
        yield tuple(zip(pat,(r for b in blocks for r in b)))
