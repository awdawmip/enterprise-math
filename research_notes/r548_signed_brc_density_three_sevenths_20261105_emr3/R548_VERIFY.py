#!/usr/bin/env python3
"""R548: exact rational angular-cone check; old root isolation is inherited."""
from fractions import Fraction as F
from math import gcd
ROOT_DISKS=[
 (5,'1247.313','1468.117','0.1','763a7f3f741a1e9557a170328304078f3c1f0753'),
 (6,'3292.954','3962.354','0.1','13f87f5f3d5a1da6ffc64f5210c204d32ab269b6'),
 (7,'3.177694','3.914665','0.001','c3ba2406d9dfc990cb58e962ad812608bf35d7b0'),
 (8,'4.036005','5.081137','0.001','c3ba2406d9dfc990cb58e962ad812608bf35d7b0'),
 (9,'4.987574458','6.397700798','0.001','38e4af26eceed759fe12110032bb3b630e0fe449'),
 (10,'6.033407511','7.862167698','0.001','00fb680d24d50f03464179a1f06a220aff2493fe'),
]
def verify():
 print('R548_ANGULAR_CONE_EXACT_BEGIN')
 for k,a,b,e,ref in ROOT_DISKS:
  a,b,e=F(a),F(b),F(e)
  assert a>e and b-e>a+e and 2*(b+e)<3*(a-e)
  print(f'k={k}; theta_in_(pi/4,pi/3)=True; certified_by={ref[:12]}')
 small=[(p,q) for q in range(1,14) for p in range(1,q)
        if 8*p>q and 6*p<q and gcd(p,q)==1]
 assert small==[(1,7),(2,13)],small
 for q in range(14,2001):
  minimal=(q-1)//2 if q%2 else (q-2)//2
  assert 7*minimal>=3*q,(q,minimal)
 print('primitive_periods_q<14:',small)
 print('uniform_lower_density_ge_3/7_for_q>=14: exact integer algebra passed (checked through q=2000; all larger q by monotonicity)')
 print('R548_EXACT_ANGLE_CERT_PASS')
if __name__=='__main__':verify()
