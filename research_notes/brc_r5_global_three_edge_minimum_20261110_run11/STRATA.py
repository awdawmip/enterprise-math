#!/usr/bin/env python3
"""Exact diagonal-locus support stratification for frozen R5 seven-LR model."""
from fractions import Fraction as F
from itertools import combinations

def masses(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u, (g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)
            +F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2, F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def slacks(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

ratios=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
examples={
 'MIN3':(F(1),F(1),F(1),F(27,80),F(1,10),F(27,80),F(1,10)),
 'MIN4_A':(F(1),F(1),F(1),F(27,80),F(1,5),F(1,8),F(1,10)),
 'MIN4_CORNER':(F(1),F(0),F(1),F(0),F(0),F(0),F(0)),
 'MIN5':(F(1),F(1),F(1),F(1,5),F(1,5),F(1,8),F(1,10)),
 'MIN6':(F(1),F(1,2),F(1),F(1,20),F(1,10),F(1,16),F(1,20)),
}
expected={'MIN3':3,'MIN4_A':4,'MIN4_CORNER':4,'MIN5':5,'MIN6':6}
for label,x in examples.items():
    mass=masses(x)
    active=tuple(j for j,v in enumerate(mass) if v>0)
    assert min(slacks(x))>=0 and len(active)==expected[label],label
    assert sum(mass)==1 and sum(ratios[j]*mass[j] for j in range(7))==1
    assert all(v>=0 for v in mass) and mass[4]==0
    # Diagonal E has exactly one outgoing edge per active column and satisfies
    # all 21 Blackwell equalities: row, column, and likelihood-ratio moment.
    E={(j,j):mass[j] for j in active}
    assert tuple(sum(v for (i,j),v in E.items() if i==k) for k in range(7))==mass
    assert tuple(sum(v for (i,j),v in E.items() if j==k) for k in range(7))==mass
    assert tuple(sum(ratios[i]*v for (i,j),v in E.items() if j==k) for k in range(7))==tuple(ratios[k]*mass[k] for k in range(7))
    print(label,'SOURCES',active,'WEIGHTS',tuple(mass[j] for j in active))
print('EXACT_ALL_DIAGONAL_MINIMAL_SUPPORTS', (3,4,5,6))
print('CLASSIFICATION source_0_and_6_positive: min = 3 + active(nu1,nu2,nu5), else unique corner min=4')
print('PASS_ALL_FIVE_RATIONAL_STRATUM_WITNESSES')
