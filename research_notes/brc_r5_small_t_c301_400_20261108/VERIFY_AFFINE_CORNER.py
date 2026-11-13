#!/usr/bin/env python3
"""Exact affine 11-edge Blackwell transfer for p=0,q=1,theta=1,kappa=3/4 and 0<=t<=1/50.
Finite seven-node P/Q statistical observer; not native Heartbeat dynamics.
"""
from fractions import Fraction as F
from VERIFY import mass, source, tp, tq, R

T1=F(1,50)
SUPPORT={
 0:F(131317,1800000), 1:F(20647,3600000), 8:F(77,8000),
 15:F(5603,2300000),16:F(49,100),17:F(17397,2300000),
 24:F(339269,1800000),38:F(1,1600),43:F(99661,82800000),
 45:F(7261,4140000),48:F(395317,1800000),
}
def x(t):
 return source(t,F(0),F(1),F(1))
def y(t):
 return (F(1),F(0),F(1),F(23,160)*t,F(27,160)+F(9,16)*t,F(21,80)-t/32,F(0))
def mat(t):
 k=t/T1
 q0={7*i+i:m for i,m in enumerate(mass(x(F(0)))) if m}
 return {s:(1-k)*q0.get(s,F(0))+k*SUPPORT.get(s,F(0)) for s in set(q0)|set(SUPPORT)}
def verify(t):
 assert 0<=t<=T1
 X,Y=x(t),y(t); mx,my=mass(X),mass(Y)
 g,a,b,u,v,w,z=Y
 assert 0<=b<=g<=1 and 0<=a<=g and 0<=u<=F(13,40)*a+b/80
 assert 0<=w<=F(3,40)*a+F(21,80)*b
 assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
 assert 9*b*z==4*a*(v-z)
 E={divmod(s,7):w for s,w in mat(t).items()}
 assert all(w>=0 for w in E.values())
 assert all(v>=0 for v in list(mx)+list(my))
 assert sum(mx)==sum(my)==F(1)
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==F(1)
 assert tp(X)==tp(Y) and tq(X)==tq(Y)
 for i in range(7):
  assert sum(v for (ii,j),v in E.items() if i==ii)==my[i]
 for j in range(7):
  assert sum(v for (i,jj),v in E.items() if j==jj)==mx[j]
  assert sum(R[i]*v for (i,jj),v in E.items() if j==jj)==R[j]*mx[j]
 return True
if __name__=='__main__':
 verify(F(0));verify(T1)
 print('PASS_EXACT_ENDPOINTS_AFFINE_11_EDGES_T_0_TO_1_50')
 assert len(SUPPORT)==11 and all(v>0 for v in SUPPORT.values())
 assert all(x(F(0))[k]+50*t*(x(T1)[k]-x(F(0))[k])==x(t)[k]
            for t in (F(1,1000),F(1,73),F(1,50)) for k in range(7))
 assert all(y(F(0))[k]+50*t*(y(T1)[k]-y(F(0))[k])==y(t)[k]
            for t in (F(1,1000),F(1,73),F(1,50)) for k in range(7))
 for i in range(101):
  verify(T1*F(i,100))
 print('PASS_EXACT_101_AFFINE_REGRESSIONS')
 print('PROVED_ALL_REAL_T_0_TO_1_50_P0_Q1_THETA1_KAPPA3_4_EXACT_SEEDLESS')
