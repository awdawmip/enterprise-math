#!/usr/bin/env python3
"""Exact 2-anchor fixed-face Blackwell bridge, a/b in [1/50,1/5].
Imports the parent exact seven-node model and verifies both rational anchors.
Whole real interval follows by convex interpolation on a common seedless face.
"""
from fractions import Fraction as F
from VERIFY import source, mass, tp, tq, R

C = [
    {
      't':'1/50',
      'y':['914/919','0','914/919','327/459500','4113/183800','9597/36760','0'],
      'Q':[
        [0,0,'1423/450000'],[0,1,'7531487/827100000'],[1,1,'1199013/459500000'],
        [1,2,'4186487/459500000'],[2,2,'1265335841/2642125000'],
        [2,3,'48539159/2642125000'],[3,1,'7531487/1033875000'],
        [3,3,'216792907/689250000'],[6,2,'4186487/2113700000'],
        [6,3,'48539159/9511650000'],[6,6,'67423/450000']
      ]
    },
    {
      't':'1/5',
      'y':['16304/16325','6407/32650','16304/16325','0','3191/130600','72321/261200','6407/3265000'],
      'Q':[
        [0,0,'2879/360000'],[0,1,'63/65300'],[0,2,'265403/73462500'],
        [1,1,'19919/261200'],[2,2,'7897097/20406250'],
        [2,3,'581431/40812500'],[3,2,'3450239/367312500'],
        [3,3,'327285391/979500000'],[6,1,'9/32650'],
        [6,3,'581431/146925000'],[6,6,'58379/360000']
      ]
    }
]
def target_legal(y):
    g,a,b,u,v,w,z=y
    return 0<=g<=1 and 0<=a<=g and 0<=b<=g and 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b and 0<=z<=a/10 and 0<=v-z<=F(9,40)*b

def check(x,y,Q):
    assert target_legal(y)
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    assert y[6]==y[1]/100 # fixed tau=1/10 -> tau*a/10 = a/100
    assert y[4]-y[6]==F(9,400)*y[2]
    mx,my=mass(x),mass(y)
    assert all(v>=0 for row in Q for v in row)
    assert sum(mx)==sum(my)==1
    assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
    assert all(sum(Q[i])==my[i] for i in range(7))
    assert all(sum(Q[i][j] for i in range(7))==mx[j] for j in range(7))
    assert all(sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j] for j in range(7))
    assert tp(x)==tp(y) and tq(x)==tq(y)

def recover(rec):
    t=F(rec['t']); y=tuple(F(v) for v in rec['y'])
    Q=[[F(0) for j in range(7)] for i in range(7)]
    for i,j,val in rec['Q']:
        assert Q[i][j]==0
        Q[i][j]=F(val)
    x=source(t)
    check(x,y,Q)
    return (x,y,Q)

ends=list(map(recover,C))
print('PASS_TWO_EXACT_FIXED_FACE_RATIONAL_ANCHORS')

def lift(t):
    lo,hi=F(1,50),F(1,5)
    assert lo<=t<=hi
    lam=(t-lo)/(hi-lo)
    x=tuple((1-lam)*ends[0][0][k]+lam*ends[1][0][k] for k in range(7))
    y=tuple((1-lam)*ends[0][1][k]+lam*ends[1][1][k] for k in range(7))
    Q=[[(1-lam)*ends[0][2][i][j]+lam*ends[1][2][i][j] for j in range(7)] for i in range(7)]
    assert x==source(t)
    check(x,y,Q)

for i in range(201):
    lift(F(1,50)+(F(1,5)-F(1,50))*F(i,200))
print('PASS_201_EXACT_RATIONAL_BRIDGE_REGRESSIONS')
print('PASS_ALL_REAL_LOW_RATIO_DIFFICULT_CORNER_0_TO_1_OVER_5_BY_TWO_CHARTS')
