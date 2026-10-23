#!/usr/bin/env python3
"""Exact author-side checks, stdlib only. No formal/independent review."""
from fractions import Fraction as F
from itertools import product
from math import prod
Q={'0':(1,665,1,333),'2':(333,333,1,333),'3':(1,1,1,997)}
E=((0,1),(1,2),(1,3),(2,3))
DEG=tuple(sum(i in e for e in E) for i in range(4))
MASKS=tuple((1<<i)|(1<<j) for i,j in E)
assert DEG==(1,3,2,2)
assert all(min(v)>0 and sum(v)==1000 for v in Q.values())

def dp_num(w):
    states=[0]*16
    states[0]=1
    for a in w:
        nxt=[0]*16
        for mask,x in enumerate(states):
            if x:
                for i,q in enumerate(Q[a]):
                    nxt[mask|(1<<i)]+=x*q
        states=nxt
    return sum(states[mask] for mask in MASKS)

def product_num(w):
    A=[prod(Q[a][i] for a in w) for i in range(4)]
    B=[prod(Q[a][i]+Q[a][j] for a in w) for i,j in E]
    return sum(B)-sum(d*x for d,x in zip(DEG,A))+(4 if not w else 0)

checked=0
for length in range(7):
    for chars in product(Q,repeat=length):
        w=''.join(chars)
        assert dp_num(w)==product_num(w),(w,dp_num(w),product_num(w))
        checked+=1
assert checked==1093

W='032020'
n=[dp_num(W[:t]) for t in range(7)]
assert n==[0,0,666000,554226216,626011982376,429146205098784,436231737917062944]
assert n[-1]-436231737917062900==44
d=[F(v,1000**t) for t,v in enumerate(n)]
delta=[F(0)]+[d[t]-d[t-1] for t in range(1,7)]
R=[F(0)]*7
for t in range(2,7):
    R[t]=sum((max(F(0),x) for x in delta[2:t+1]),F(0))-max(d[:t+1])
assert [t for t in range(2,7) if R[t]>R[t-1]]==[4,6]

nodes=[0]+[prod(Q[a][i] for a in '02') for i in range(4)]+[
    prod(Q[a][i]+Q[a][j] for a in '02') for i,j in E]
coeff=[4]+[-v for v in DEG]+[1]*4
assert nodes==[0,333,221445,1,110889,443556,222444,664668,111556]
assert len(set(nodes))==9 and prod(coeff)==48
for k in range(9):
    assert sum(c*m**k for c,m in zip(coeff,nodes))==dp_num('02'*k)

prime=1000003
hs=[sum(c*pow(m,k,prime) for c,m in zip(coeff,nodes))%prime for k in range(17)]
matrix=[[hs[i+j] for j in range(9)] for i in range(9)]
det=1
for j in range(9):
    pivot=next((i for i in range(j,9) if matrix[i][j]%prime),None)
    assert pivot is not None
    if pivot!=j:
        matrix[j],matrix[pivot]=matrix[pivot],matrix[j]
        det=-det
    a=matrix[j][j]%prime
    det=det*a%prime
    inv=pow(a,-1,prime)
    for i in range(j+1,9):
        x=matrix[i][j]*inv%prime
        for k in range(j,9):
            matrix[i][k]=(matrix[i][k]-x*matrix[j][k])%prime
vand=prod(nodes[j]-nodes[i] for i in range(9) for j in range(i+1,9))%prime
assert det%prime==48*vand*vand%prime==139775

def horizon_ok(s):
    return 998**s > 2001*997**s+1
assert not horizon_ok(7582) and horizon_ok(7583)
q=[F(3,16),F(4,16),F(4,16),F(5,16)]
assert max(q)<min(q[i]+q[j] for i,j in E)
values=[F(0)]
for t in range(1,61):
    values.append(sum(((q[i]+q[j])**t for i,j in E),F(0))-
                  sum((DEG[i]*q[i]**t for i in range(4)),F(0)))
assert values[1]==0 and values[2]>values[1]
assert all(values[t]<values[t-1] for t in range(3,61))
print('PASS 1093 words, exact 16-mask vs product observer')
print('PASS N6 436231737917062944; prior evidence typo differs by 44')
print('PASS residual-growth rounds {4,6}')
print('PASS nine-node Hankel determinant mod 1000003 = 139775')
print('PASS minimal strict uniform-decline threshold s*=7583, all t>=7584')
print('PASS fixed-law Fraction example through 60 rounds')
