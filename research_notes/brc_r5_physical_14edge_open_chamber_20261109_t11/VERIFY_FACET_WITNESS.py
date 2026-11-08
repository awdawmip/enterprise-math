#!/usr/bin/env python3
"""Exact witness that the fixed 14-edge chart requires support changes."""
from fractions import Fraction as F
import VERIFY_14_CHAMBER as Q

R=Q.R
EDGES=getattr(Q,"EDGES",getattr(Q,"EDGE_NAMES",None))
entries=getattr(Q,"entries",getattr(Q,"coupling",None))
model=Q.model;mass=Q.mass;tp=Q.tp;tq=Q.tq
residual=getattr(Q,"residual",getattr(Q,"equality_residual",None))

x=tuple(map(F,'1 1/10 1 27/800 1/100 27/400 1/100'.split()))
y=tuple(map(F,'4673/6400 1311/6400 4673/6400 38759/512000 47301/256000 103999/512000 1311/64000'.split()))
p=(x[0],x[1],x[3],x[4],x[5],x[6],y[0],y[1],y[2])
assert model(p)==(x,y)
assert tp(x)==tp(y) and tq(x)==tq(y)
assert residual(p)==(F(0),)*21

chart=dict(zip(EDGES,entries(x,y)))
assert chart[4,2]==F(-2109829,147200000)
assert sum(v<0 for v in chart.values())==1
print('EXACT_FIXED_CHART_NEGATIVE_E_4_2',chart[4,2])

SOURCE_EDGES=[
(0,0,'16109/720000'),(0,1,'9/2080'),(0,2,'273874223/2995200000'),
(2,1,'9/1300'),(2,2,'21277/83200'),(3,2,'2442943/38400000'),
(3,3,'98191/360000'),(3,5,'9/100'),(5,2,'1/256'),
(6,2,'8134171/230400000'),(6,5,'9/80'),(6,6,'29609/720000')
]
E={(i,j):F(v) for i,j,v in SOURCE_EDGES}
mu,nu=mass(y),mass(x)
assert len(E)==12 and all(v>0 for v in E.values())
assert all(sum(E.get((i,j),F(0)) for j in range(7))==mu[i] for i in range(7))
assert all(sum(E.get((i,j),F(0)) for i in range(7))==nu[j] for j in range(7))
assert all(sum(R[i]*E.get((i,j),F(0)) for i in range(7))==R[j]*nu[j] for j in range(7))
print('EXACT_ALTERNATIVE_12_EDGE_TRANSPORT_PASS',min(E.values()))
