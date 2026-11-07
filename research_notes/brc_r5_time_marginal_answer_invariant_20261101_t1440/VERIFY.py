#!/usr/bin/env python3
"""Exact time-marginal obstruction for R5 coupled real LR keys; Python stdlib only."""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm

P = (F(1,8), F(1,8), F(1,4), F(1,2))
Q = (F(1,8), F(1,8), F(1,8), F(5,8))
assert sum(P)==sum(Q)==1

def time_vector(policy):
    p1,p2,q1,q2,qB,r=map(F,policy)
    def ta(p,q,low):
        return p+(1-p)*(2+low*(1-q))
    p=(P[0]*ta(p1,q1,F(1,2)) + P[1]*ta(p2,q2,F(3,4))
       +P[2]*(3-qB)+P[3]*(3-2*r))
    q=(Q[0]*ta(p1,q1,F(1,4)) + Q[1]*ta(p2,q2,F(3,8))
       +Q[2]*(3-qB)+Q[3]*(3-2*r))
    return (p,q)

def lr_policy(p,q,r):return (p,p,q,q,q,r)

def H(v):return 21*v[0]-26*v[1]

def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def polygon(points):
    pts=sorted(set(points))
    def chain(seq):
        out=[]
        for p in seq:
            while len(out)>1 and cross(out[-2],out[-1],p)<=0:out.pop()
            out.append(p)
        return out
    return chain(pts)[:-1]+chain(pts[::-1])[:-1]

def integer_edge(a,b):
    dx=b[0]-a[0];dy=b[1]-a[1]
    coeff=(-dy,dx,dy*a[0]-dx*a[1]); scale=lcm(*(x.denominator for x in coeff))
    nums=tuple(int(x*scale) for x in coeff); div=gcd(*nums)
    return tuple(x//div for x in nums)

def slack(edge,point):
    a,b,c=edge;return a*point[0]+b*point[1]+c

lrs=[(x,time_vector(lr_policy(*x))) for x in product((0,1),repeat=3)]
fulls=[(x,time_vector(x)) for x in product((0,1),repeat=6)]
assert len(lrs)==8 and len(fulls)==64
assert max(H(v) for _,v in lrs)==-1
assert max(H(v) for _,v in fulls)==-F(7,8)

# Exact all-real Bellman expression, checked on all vertices and an interior grid.
def H_formula(policy):
    p1,p2,q1,q2,qB,r=map(F,policy)
    return (-F(25,2)+F(1,8)*p1-F(1,8)*p2
            -F(1,2)*(1-p1)*q1-F(3,4)*(1-p2)*q2
            -2*qB+F(23,2)*r)
for bits,v in fulls:assert H(v)==H_formula(bits)
vals=(F(0),F(1,3),F(1,2),F(2,3),F(1))
for p,q,r in product(vals,repeat=3):
    t=time_vector(lr_policy(p,q,r))
    assert H(t)==-1-F(23,2)*(1-r)-(2+F(5,4)*(1-p))*q

lh=polygon([v for _,v in lrs]); fh=polygon([v for _,v in fulls])
W=(F(55,32),F(91,64))
assert len(lh)==6 and len(fh)==7
assert set(fh)==set(lh)|{W}
edges=[integer_edge(lh[i],lh[(i+1)%len(lh)]) for i in range(len(lh))]
assert edges==[(-1,2,-1),(-21,26,-1),(-160,128,103),(4,-8,11),(8,-8,1),(20,-16,-7)]
counts=[sum(slack(e,v)<0 for _,v in fulls) for e in edges]
assert counts==[0,2,0,0,0,0]
assert min(slack(edges[1],v) for _,v in fulls)==-F(1,8)
violators=[b for b,v in fulls if slack(edges[1],v)<0]
assert violators==[(1,0,0,0,0,1),(1,0,1,0,0,1)]

# Exact closest point of LR time hull in L_infty.
y=tuple(F(22,47)*time_vector(lr_policy(1,0,1))[j]
       +F(25,47)*time_vector(lr_policy(0,0,1))[j] for j in (0,1))
assert max(abs(W[j]-y[j]) for j in (0,1))==F(1,376)
assert H(W)-H(y)==F(1,8)
assert 47*F(1,376)==F(1,8)

# Independent end-of-path perturbation: O_theta - O_0 = (1-p1)(1-q1)*(-alpha/16,beta/32,0,0).
# Rank-one determinant lemma from last round's exact 4x4 chart.
def det(alpha,beta):return (F(233)+530*alpha-170*beta)/163840
box=(F(-1,100),F(0),F(1,100))
for alpha,beta in product(box,repeat=2):
    assert F(0)<F(3,5)+alpha<1 and F(0)<F(1,2)+beta<1
    assert det(alpha,beta)>=F(113,81920)
    # Time marginal independent of alpha,beta; likelihood-ratio signatures remain separated.
    x_ratio=2*(F(3,5)+alpha)/(F(1,2)+beta)
    y_ratio=2*(F(2,5)-alpha)/(F(1,2)-beta)
    assert x_ratio>2 and F(4,5)<y_ratio<2 and x_ratio!=y_ratio

# Previous fixed-model six outward facet gaps persist with old dual normals.
gaps=(F(2793,1864),F(90,233),F(3737,1864),F(205,233),F(1,932),F(1,932))
normals=((-14100,-9608),(-8480,-5440),(13620,8456),(8960,6592),(80,192),(-80,-192))
expected=(F(65099,46600),F(76,233),F(88963,46600),F(4742,5825),F(3,23300),F(3,23300))
for i,((a,b),g) in enumerate(zip(normals,gaps)):
    loss=2*(F(abs(a),233*16)+F(abs(b),233*32))*F(1,100)
    assert g-loss==expected[i] and expected[i]>0

print('FROZEN_TIME_LR_HULL_VERTICES',lh)
print('FROZEN_TIME_FULL_EXTRA_VERTEX',W)
print('EXACT_LR_TIME_EDGES',edges)
print('FULL_VIOLATION_COUNTS',counts,'WITNESSES',violators)
print('ALL_REAL_SUPPORT_MAX_LR',-1,'FULL',-F(7,8),'GAP',F(1,8))
print('EXACT_TIME_LINFTY_DISTANCE',F(1,376),'PRIMAL_CLOSEST_LR',y)
print('PERTURBATION_BOX', 'alpha,beta in [-1/100,1/100]', 'DETERMINANT_MIN',F(113,81920))
print('SIX_FACET_OLD_DIRECTION_MIN_GAPS',expected)
print('PASS_EXACT_R5_COUPLED_KEYS_TIME_MARGINAL_GLOBAL_ANSWER_NO_GO')
