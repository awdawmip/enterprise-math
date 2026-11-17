#!/usr/bin/env python3
"""Standalone exact EC49FRG 116-node parameter-area and radical-regret checker.
Python standard library only. Checks geometric consequences of already-certified
BRC prices; scientific Bellman certificates have a separate independent verifier.
"""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal, localcontext
from functools import reduce

OLD = "1 49/48 25/24 17/16 13/12 53/48 9/8 55/48 7/6 19/16 29/24 59/48 5/4 61/48 31/24 21/16 4/3 65/48 11/8 67/48 17/12 23/16 35/24 71/48 3/2 49/32 25/16 51/32 13/8 53/32 107/64 27/16 109/64 55/32 111/64 7/4 113/64 57/32 115/64 29/16 117/64 59/32 119/64 15/8 121/64 61/32 123/64 31/16 125/64 63/32 127/64 2 129/64 65/32 131/64 33/16 133/64 67/32 135/64 17/8 137/64 69/32 139/64 35/16 141/64 71/32 143/64 9/4 145/64 73/32 147/64 37/16 149/64 75/32 151/64 19/8 153/64 77/32 155/64 39/16 157/64 79/32 159/64 5/2 121/48 61/24 41/16 31/12 125/48 21/8 127/48 8/3 43/16 65/24 131/48 11/4 133/48 67/24 45/16 17/6 137/48 23/8 185/64 93/32 187/64 47/16 189/64 95/32 191/64 3"
SEAMS = "105/64:8990/155301 103/64:27590/466241 101/64:28210/466579 99/64:9610/155639 97/64:5890/93451 275/96:4030/678997"

old = [F(x) for x in OLD.split()]
new_data = [(F(a),F(b)) for item in SEAMS.split() for a,b in [item.split(":")]]
new = [x for x,g in new_data]
assert len(old)==110 and len(set(old))==110 and old==sorted(old)
K = lambda x: F(7557)-169*x
G = lambda x: 310*(3-x)/K(x)
D = F(2185500)
U = lambda a,b: (b-a)*(G(a)-G(b))
def area(nodes):
    return sum((U(a,b) for a,b in zip(nodes,nodes[1:])), F(0))
def exact_radical_bounds(a,b):
    scale=10**40
    def sqrtbox(k):
        n=isqrt(k.numerator*scale*scale//k.denominator)
        lo,hi=F(n,scale),F(n+1,scale)
        assert lo*lo<=k<hi*hi
        return lo,hi
    la,ua=sqrtbox(K(a));lb,ub=sqrtbox(K(b))
    return (50*(b-a)/(ua+ub)**2,50*(b-a)/(la+lb)**2)
assert all(0<G(x)<F(620,3299) for x,_ in new_data)
assert all(g==G(x) for x,g in new_data)
work=old.copy()
for x,g in new_data:
    a,b=max(zip(work,work[1:]),key=lambda ab: K(ab[0])/K(ab[1]))
    assert x==(a+b)/2
    assert 2*(U(a,x)+U(x,b))==U(a,b)
    work=sorted(work+[x])
assert len(work)==116
assert area(old)==F(259924479610030238135,162277343928838082317536)
assert area(work)==F(353039202146480393615,236644210143071463572064)
assert area(old)-area(work)==F(19144978000085375,174245733138392004168)
assert 1-area(work)/2 == F(472935381083996446750513,473288420286142927144128)
def bound_rows(nodes):
    return [(a,b,*exact_radical_bounds(a,b)) for a,b in zip(nodes,nodes[1:])]
older=bound_rows(old);rows=bound_rows(work)
before=max(older,key=lambda z:z[2]);after=max(rows,key=lambda z:z[2])
assert before[:2]==(F(13,8),F(53,32))
assert after[:2]==(F(17,6),F(137,48))
assert all(before[2]>r[3] for r in older if r is not before)
assert all(after[2]>r[3] for r in rows if r is not after)
assert after[3]<before[2]
with localcontext() as ctx:
    ctx.prec=72
    q=lambda x:Decimal(x.numerator)/Decimal(x.denominator)
    radical=lambda a,b:50*q(b-a)/(q(K(a)).sqrt()+q(K(b)).sqrt())**2
    print("NODES",len(work),"BANDS",len(rows))
    print("AREA_TOTAL",area(work))
    print("CERTIFIED_PERCENT_LOWER",100*q(1-area(work)/2))
    print("STRICT_UNIQUE_LARGEST_REGRET_INTERVAL",after[0],after[1])
    print("MAX_REGRET_OVER_T",radical(*after[:2]))
    print("PREVIOUS_MAX_REGRET_OVER_T",radical(*before[:2]))
print("EC49FRG_EXACT_116_NODE_GEOMETRY_PASS")
