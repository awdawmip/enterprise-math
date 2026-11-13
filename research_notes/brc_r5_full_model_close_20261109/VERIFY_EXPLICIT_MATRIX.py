#!/usr/bin/env python3
"""Exact 12-edge Blackwell coupling for an explicitly nonseedless R5 source.
Only the Python standard library and sibling VERIFY_PGEQ.py are required.
Floating LP was used to suggest an edge support, but the stored rational
certificate and these checks are independent of the LP computation.
"""
from fractions import Fraction as F
from VERIFY_PGEQ import R, mass, lawful, source, target, tp, tq

PARAMS=(F(1,10),F(3,4),F(1,4),F(1),F(0))
X=(F(1),F(1,10),F(1),F(27,800),F(1,100),F(27,400),F(1,100))
Y=tuple(map(F,("4673/6400", "1311/6400", "4673/6400", "38759/512000",
                "47301/256000", "103999/512000", "1311/64000")))
EDGE_ROWS=(
(0,0,"16109/720000"),
(0,1,"9/2080"),
(0,2,"273874223/2995200000"),
(2,1,"9/1300"),
(2,2,"21277/83200"),
(3,2,"2442943/38400000"),
(3,3,"98191/360000"),
(3,5,"9/100"),
(5,2,"1/256"),
(6,2,"8134171/230400000"),
(6,5,"9/80"),
(6,6,"29609/720000"),
)
E=[[F(0) for _ in range(7)] for _ in range(7)]
for i,j,v in EDGE_ROWS:
    assert E[i][j]==0
    E[i][j]=F(v)

def main():
    assert X==source(*PARAMS)
    assert Y==target(*PARAMS)
    lawful(X);lawful(Y)
    assert 9*X[2]*X[6]-4*X[1]*(X[4]-X[6])==F(9,100)
    assert 9*Y[2]*Y[6]-4*Y[1]*(Y[4]-Y[6])==0
    assert tp(X)==tp(Y) and tq(X)==tq(Y)
    a,b=mass(X),mass(Y)
    assert all(sum(E[i])==b[i] for i in range(7))
    assert all(sum(E[i][j] for i in range(7))==a[j] for j in range(7))
    assert all(sum(R[i]*E[i][j] for i in range(7))==R[j]*a[j] for j in range(7))
    assert len(EDGE_ROWS)==12
    assert min(F(v) for i,j,v in EDGE_ROWS)==F(1,256)
    print("PASS_R5_EXACT_12_EDGE_BLACKWELL_CERTIFICATE")
    print("SOURCE_RESIDUAL_9_OVER_100_TARGET_RESIDUAL_ZERO")
    print("MARTINGALE_ROW_COLUMN_AND_WEIGHTED_COLUMN_IDENTITIES_PASS")
    print("STOP_TIMES_AND_SEEDLESS_PHYSICAL_BOUNDARIES_PASS")
if __name__=="__main__":main()
