#!/usr/bin/env python3
"""Independent exact rational coherent-source witness from the original A.
Uses only Python stdlib Fraction and explicit Gaussian elimination.
It is a strict interior witness near the new sharp corner, not the sharp point.
"""
from fractions import Fraction as F
from functools import reduce

def c(a,b=0): return (F(a),F(b))
def add(z,w):return (z[0]+w[0],z[1]+w[1])
def neg(z):return (-z[0],-z[1])
def sub(z,w):return add(z,neg(w))
def mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def div(z,w):
    den=w[0]**2+w[1]**2
    assert den>0
    return ((z[0]*w[0]+z[1]*w[1])/den,(z[1]*w[0]-z[0]*w[1])/den)
def mag2(z):return z[0]*z[0]+z[1]*z[1]

def solve(M,rhs):
    T=[[M[i][j] for j in range(3)]+[rhs[i]] for i in range(3)]
    for k in range(3):
        m=next(i for i in range(k,3) if mag2(T[i][k])>0)
        T[k],T[m]=T[m],T[k]
        inv=div(c(1),T[k][k]);T[k]=[mul(z,inv) for z in T[k]]
        for i in range(3):
            if i==k:continue
            z=T[i][k];T[i]=[sub(T[i][j],mul(z,T[k][j])) for j in range(4)]
    return [T[i][3] for i in range(3)]

A=[
[c(4),c(4),c(0)],
[c(0),c(-4),c(4)],
[c(-5,3),c(0),c(-3,1)],
[c(-2,-2),c(4,4),c(2,2)],
[c(-2),c(0),c(5,2)],
]
scale=10**18
u=c(F(9999,10**10), F(999999500049375125,scale))
v=c(F(49989020038846,scale),F(-139143883029119,scale))
Y=solve(A[:3],[c(1),u,v])
W=[reduce(add,(mul(z,y) for z,y in zip(row,Y)),c(0)) for row in A]
assert W[0]==c(1) and W[1]==u and W[2]==v
I1,I2,I3,I4,I5=[mag2(z) for z in W]
Cu=mag2(add(W[0],W[1]));Cv=mag2(add(W[0],W[2]))
eps=F(1,1000000);eta=F(1,10000);beta=F(1,1000000)
assert I1==1
assert 1-eps<I2<1+eps
assert 2-eps<Cu<2+eps
assert 0<I3<beta
assert 1-eta<Cv<1+eta
assert F(709,32)-eta<I5<F(709,32)+eta
kappa=41-I4
assert 0<kappa<F('3.99868683')
print('PASS_PREFIX411_INDEPENDENT_FRACTION_ORIGINAL_A_STRICT_WITNESS')
print('kappa_witness=',kappa)
print('kappa_witness_float=',format(float(kappa),'.17f'))
print('distances_to_limits=',[(str(name),float(margin)) for name,margin in [('I2_low',I2-(1-eps)),('Cu_high',2+eps-Cu),('Cv_high',1+eta-Cv),('I5_high',F(709,32)+eta-I5)]])
