#!/usr/bin/env python3
"""Exact three-real-parameter negative-residual Blackwell rectangle regression.
Analytic proof is in SIDE_RECTANGLE.md, which reuses the source Q from VERIFY_SIDE.py.
"""
from fractions import Fraction as F
from pathlib import Path
import runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
    base=runpy.run_path(str(Path(__file__).with_name('VERIFY_SIDE.py')))
Z=F(0); ONE=F(1)
r=base['r']; Q0=base['Q']; x0=base['x']; y0=base['y']
legal=base['legal']; times=base['times']; masses=base['masses']; residual=base['residual']
U=F(503,1600); W=F(32383,175840)
assert U < F(53,160) and W < F(33,160) and W < F(303,1600)

def flows(u,w):
    x=list(x0);y=list(y0);x[3]=y[3]=u;x[5]=y[5]=w
    return tuple(x),tuple(y)

def qmass(u,w):
    delta=(F(509,900)*u+w/100,-u,Z,F(191,450)*(u+w),Z,-w,u/100+F(509,900)*w)
    return tuple(tuple(Q0[i][j]+(delta[i] if i==j else Z) for j in range(7)) for i in range(7))

assert qmass(Z,Z)==Q0
count=0
for ru in (Z,F(1,4),F(1,2),F(3,4),ONE):
 for rw in (Z,F(1,4),F(1,2),F(3,4),ONE):
    u,w=U*ru,W*rw
    x,y=flows(u,w)
    Q=qmass(u,w)
    assert legal(x) and legal(y) and residual(x)==-F(9,20) and residual(y)==0
    assert times(x)==times(y)
    mx,my=masses(x),masses(y)
    assert all(a>=0 for row in Q for a in row)
    for i in range(7):assert sum(Q[i])==my[i]
    for j in range(7):
     assert sum(Q[i][j] for i in range(7))==mx[j]
     assert sum(r[i]*Q[i][j] for i in range(7))==r[j]*mx[j]
    for t in (Z,F(1,7),F(1,3),F(1,2),ONE):
     xt=tuple((1-t)*a+t*b for a,b in zip(x,y))
     Qt=tuple(tuple((1-t)*Q[i][j]+(t*my[i] if i==j else Z) for j in range(7)) for i in range(7))
     assert legal(xt) and times(xt)==times(y)
     assert residual(xt)==-F(9)*(t-1)*(307*t-3140)/62800
     assert all(a>=0 for row in Qt for a in row)
     mt=masses(xt)
     for i in range(7):assert sum(Qt[i])==my[i]
     for j in range(7):
      assert sum(Qt[i][j] for i in range(7))==mt[j]
      assert sum(r[i]*Qt[i][j] for i in range(7))==r[j]*mt[j]
     for d in ((Z,)*7,(ONE,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),ONE)):
      mapped=tuple(sum(Qt[i][j]*d[j] for j in range(7))/my[i] if my[i]>0 else Z for i in range(7))
      assert all(Z<=di<=ONE for di in mapped)
      assert sum(my[i]*mapped[i] for i in range(7))==sum(mt[j]*d[j] for j in range(7))
      assert sum(r[i]*my[i]*mapped[i] for i in range(7))==sum(r[j]*mt[j]*d[j] for j in range(7))
     count+=1
print('PASS_SIDE_RECTANGLE_EXACT_COEFFICIENT_BOUNDS',str(U),str(W))
print('PASS_SIDE_RECTANGLE_25_UW_GRID_AND_125_T_GRID',count)
print('EXTREME_SOURCE',','.join(map(str,flows(U,W)[0])))
print('EXTREME_TARGET',','.join(map(str,flows(U,W)[1])))
print('PASS_ALL_REAL_THREE_PARAMETER_LOW_SLACK_BLACKWELL_FAMILY')
