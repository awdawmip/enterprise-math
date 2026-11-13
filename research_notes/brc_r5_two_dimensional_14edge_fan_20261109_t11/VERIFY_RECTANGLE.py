#!/usr/bin/env python3
"""Exact sharp full-width 2D physical 14-edge Blackwell rectangle via observer-kernel lift."""
from pathlib import Path
from fractions import Fraction as F
from runpy import run_path
c=run_path(str(Path(__file__).with_name('VERIFY_2D.py')))
Q=c['Q'];X0=c['X0'];X1=c['X1'];Y0=c['Y0'];Y1=c['Y1'];XH=c['XH'];YH=c['YH']
SA=c['SA'];SB=c['SB'];A0=c['A0'];AH=c['AH'];BH=c['BH'];B1=c['B1']
D=c['D'];DX=c['DX'];DY=c['DY']; add=c['add']; shifted=c['shifted'];slack=c['slack']
masses=c['masses'];times=c['times'];lawful=c['lawful'];verify=c['verify'];R=c['R']
K=Q('-49400/295513 -49400/295513 -49400/295513 -33345/591026 132145/295513 -33345/591026 1')
assert K[0]==K[2]
assert tuple(a-b for a,b in zip(masses(add(X0,K,1)),masses(X0)))==(F(0),)*7
assert tuple(a-b for a,b in zip(times(add(X0,K,1)),times(X0)))==(F(0),)*2
print('EXACT_OBSERVER_KERNEL_DIRECTION_NONZERO',K)
DX2=tuple(a-b for a,b in zip(DX,K))
assert DX2[-1]==-1
assert tuple(a-b for a,b in zip(masses(add(X0,DX2,1)),masses(X0)))==Q('-1/2 0 0 1 0 0 -1/2')
assert tuple(a-b for a,b in zip(times(add(X0,DX2,1)),times(X0)))==tuple(a-b for a,b in zip(times(add(Y0,DY,1)),times(Y0)))
EPS=F(1,120)
for name,S,W,x,y in [('A0',SA,A0,X0,Y0),('AH',SA,AH,XH,YH),('BH',SB,BH,XH,YH),('B1',SB,B1,X1,Y1)]:
 xx=add(x,DX2,EPS); yy=add(y,DY,EPS)
 ww=shifted(S,W,EPS)
 assert lawful(xx) and lawful(yy)
 assert xx[0]==xx[2] and yy[6]==yy[1]/10 and yy[4]-yy[6]==F(9,40)*yy[2]
 assert all(z>=0 for z in slack(xx)+slack(yy))
 assert times(xx)==times(yy)
 assert sum(masses(xx))==sum(masses(yy))==1
 assert sum(R[i]*m for i,m in enumerate(masses(xx)))==sum(R[i]*m for i,m in enumerate(masses(yy)))==1
 n,m=verify(S,ww,xx,yy)
 print('RECTANGLE_TOP_EXACT_21',name,'positive_edges',n,'min_edge',m)
assert masses(Y1)[1]-masses(Y0)[1]==-F(367,24000)
assert (-F(1,2))*(-(masses(Y1)[1]-masses(Y0)[1]))==-F(367,48000)
assert slack(add(X0,DX2,EPS))[9]==0
assert slack(add(X0,DX2,EPS+F(1,1000000)))[9]<0
print('SHARP_WIDTH_FIXED_KERNEL_LIFT',EPS,'SOURCE_Z_AT_LAMBDA_0',0)
print('THEOREM_ALL_REAL_FULL_RECTANGLE_14_EDGE', '0<=lambda<=1', '0<=delta<=1/120')
