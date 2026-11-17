#!/usr/bin/env python3
"""EC49FRH 128-node rational enclosure checker (Python 3, stdlib only).
Runs with no external data. Optional raw certificates are in the evidence archive;
this checks the geometric claims, not an independent Bellman recurrence.
"""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal,localcontext
P116="""1 49/48 25/24 17/16 13/12 53/48 9/8 55/48 7/6 19/16 29/24 59/48 5/4 61/48 31/24 21/16 4/3 65/48 11/8 67/48 17/12 23/16 35/24 71/48 3/2 97/64 49/32 99/64 25/16 101/64 51/32 103/64 13/8 105/64 53/32 107/64 27/16 109/64 55/32 111/64 7/4 113/64 57/32 115/64 29/16 117/64 59/32 119/64 15/8 121/64 61/32 123/64 31/16 125/64 63/32 127/64 2 129/64 65/32 131/64 33/16 133/64 67/32 135/64 17/8 137/64 69/32 139/64 35/16 141/64 71/32 143/64 9/4 145/64 73/32 147/64 37/16 149/64 75/32 151/64 19/8 153/64 77/32 155/64 39/16 157/64 79/32 159/64 5/2 121/48 61/24 41/16 31/12 125/48 21/8 127/48 8/3 43/16 65/24 131/48 11/4 133/48 67/24 45/16 17/6 137/48 275/96 23/8 185/64 93/32 187/64 47/16 189/64 95/32 191/64 3"""
expected="""91/32 271/96 269/96 89/32 265/96 263/96 87/32 259/96 257/96 85/32 253/96 251/96"""
grid=list(map(F,P116.split()))
K=lambda x:F(7557)-169*x
G=lambda x:310*(3-x)/K(x)
U=lambda a,b:(b-a)*(G(a)-G(b))
RANK=lambda a,b:K(a)/K(b)
assert len(grid)==116 and grid==sorted(set(grid))
S=lambda gr:sum((U(a,b) for a,b in zip(gr,gr[1:])),F(0))
assert S(grid)==F(353039202146480393615,236644210143071463572064)
old=grid[:]
picked=[]
for step in range(12):
    a,b=max(zip(grid,grid[1:]),key=lambda ab:RANK(*ab))
    m=(a+b)/2
    assert U(a,m)+U(m,b)==U(a,b)/2
    picked.append(m)
    grid=sorted(grid+[m])
assert picked==list(map(F,expected.split()))
assert len(grid)==128
assert S(grid)==F(328238036058866176955,238057456560501514334688)
assert S(old)-S(grid)==F(13113000,116005288213)
assert 1-S(grid)/2==F(1)-F(328238036058866176955,238057456560501514334688)/2
# Integer-only outward rational square-root interval:
scale=10**38
def sb(v):
    q=isqrt(v.numerator*scale**2//v.denominator)
    low,high=F(q,scale),F(q+1,scale)
    assert low**2<=v<high**2
    return low,high
def bounds(a,b):
    al,ah=sb(K(a));bl,bh=sb(K(b))
    return 50*(b-a)/(ah+bh)**2,50*(b-a)/(al+bl)**2
def winner(nodes):
    bounds_list=[(a,b,*bounds(a,b)) for a,b in zip(nodes,nodes[1:])]
    best=max(bounds_list,key=lambda w:w[2])
    assert all(best[2]>x[3] for x in bounds_list if x is not best)
    return best
prev=winner(old);curr=winner(grid)
assert prev[:2]==(F(17,6),F(137,48))
assert curr[:2]==(F(31,12),F(125,48))
assert curr[3]<prev[2]
with localcontext() as c:
    c.prec=60
    d=lambda r:Decimal(r.numerator)/Decimal(r.denominator)
    gap=lambda a,b:Decimal(50)*d(b-a)/(d(K(a)).sqrt()+d(K(b)).sqrt())**2
    print("128-node certified percent >=",100*(1-d(S(grid))/2))
    print("old worst R/t",gap(*prev[:2]),"interval",prev[:2])
    print("new worst R/t",gap(*curr[:2]),"interval",curr[:2])
print("PASS: all rational identities, exact dyadic choice, all 127 radical rankings")
