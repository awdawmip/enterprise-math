#!/usr/bin/env python3
"""Exact 16-corner R5 theta-prism; needs sibling VERIFY.py and VERIFY_Q1_PRISM.py."""
from fractions import Fraction as F
from itertools import product
from VERIFY import mass
from VERIFY_Q1_PRISM import validate
# At t=1/5, theta=0; keys are (p,q) in {0,1}^2.
C = {
(0,0): ((F(159007,160125),F(301981,1921500),F(159007,160125),F(154999,10248000),F(5411,878400)),
 {(0,0):F(67,960),(0,1):F(68903,6148800),(1,1):F(1486921,30744000),
  (2,1):F(68903,3843000),(2,2):F(2,5),(3,3):F(253,2400),
  (3,5):F(68903,13834800),(5,5):F(1637389,6148800),
  (6,5):F(68903,11067840),(6,6):F(67,960)}),
(0,1): ((F(15730927,15778375),F(2901518,15778375),F(15730927,15778375),F(161283,126227000),F(13910343,50490800)),
 {(0,0):F(2177,30000),(0,1):F(206709,50490800),(1,1):F(1054873,15778375),
  (1,3):F(206709,50490800),(2,1):F(206709,31556750),(2,2):F(2,5),
  (3,3):F(410549971,1893405000),(6,3):F(68903,30294480),(6,6):F(3401,15000)}),
(1,0): ((F(17173202,17230325),F(3388942,17230325),F(16966493,17230325),F(21015797,275685200),F(47703,27568520)),
 {(0,0):F(5113,45000),(0,3):F(68903,33082224),(2,2):F(2,5),
  (3,3):F(586970191,4430655000),(4,5):F(206709,34460650),
  (5,3):F(206709,55137040),(5,5):F(36907713,137842600),
  (6,5):F(206709,55137040),(6,6):F(2117,30000)}),
(1,1): ((F(1),F(78140024,408062125),F(405810541,408062125),F(487490233,6528994000),F(357681153,1305798800)),
 {(0,0):F(41903,360000),(0,2):F(281727,163224850),(2,2):F(161910124,408062125),
  (2,3):F(6101853,816124250),(3,3):F(143698989769,587609460000),
  (4,3):F(1125792,408062125),(5,2):F(1220817,816124250),
  (6,3):F(1283423,979349100),(6,6):F(27301,120000)})
}

def source(t,p,q,theta):
 return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
         t*theta/10+F(27,160),(F(3,40)*t+F(21,80))*q,t*theta/10)

def corner(t,p,q,theta):
 x=source(t,p,q,theta)
 if t==0 or theta==F(3,4):
  yv=(x[0],x[1],x[2],x[3],x[5])
  return x,yv,{(i,i):v for i,v in enumerate(mass(x)) if v>0}
 assert t==F(1,5) and theta==0
 yv,Q=C[(int(p),int(q))]
 return x,yv,Q

if __name__=='__main__':
 vertices={}
 for t,p,q,theta in product((F(0),F(1,5)),(F(0),F(1)),(F(0),F(1)),(F(0),F(3,4))):
  x,yv,Q=corner(t,p,q,theta)
  validate(x,yv,Q)
  vertices[t,p,q,theta]=(x,yv,Q)
 assert len(vertices)==16
 for j in range(601):
  t=F(1,5)*F(j,600)
  p=F((7*j+13)%601,601)
  q=F((11*j+29)%601,601)
  theta=F(3,4)*F((17*j+23)%601,601)
  weights={v:(t/F(1,5) if v[0] else 1-t/F(1,5))*(p if v[1] else 1-p)*
             (q if v[2] else 1-q)*(theta/F(3,4) if v[3] else 1-theta/F(3,4)) for v in vertices}
  assert sum(weights.values())==1 and min(weights.values())>=0
  x=source(t,p,q,theta)
  assert all(sum(weights[v]*vertices[v][0][k] for v in vertices)==x[k] for k in range(7))
  yv=tuple(sum(weights[v]*vertices[v][1][k] for v in vertices) for k in range(5))
  Q={ij:sum(weights[v]*vertices[v][2].get(ij,F(0)) for v in vertices)
     for ij in set().union(*(set(item[2]) for item in vertices.values()))}
  validate(x,yv,Q)
 print('PASS_16_EXACT_CORNERS_THETA_0_TO_3_4_Q_0_TO_1',sum(len(C[k][1]) for k in C))
 print('PASS_601_EXACT_FOUR_PARAMETER_INTERPOLATION_CASES')
 print('PROVED_ALL_REAL_T_P_Q_THETA_FULL_PRISM_T_0_TO_1_5_P_Q_0_TO_1_THETA_0_TO_3_4_KAPPA_3_4')
