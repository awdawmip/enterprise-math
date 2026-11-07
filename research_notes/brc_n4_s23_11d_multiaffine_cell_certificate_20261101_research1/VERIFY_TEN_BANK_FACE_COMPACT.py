#!/usr/bin/env python3
"""Exact four-rectangle certificate for the frozen BRC N4/S23 ten-bank face."""
from fractions import Fraction as F
from itertools import product
from VERIFY import prepared,theta_face,loss,bank_loss
SPEC=('34 24 34 24','34 23 34 34','34 34 34 23','24 24 12 12',
'12 12 24 34','12 13 23 24','23 34 12 13','24 34 12 14','13 12 13 13')
GROUP=(0,0,1,2,2,3)
def decode(s):
 rows=[]
 for pair in s.split():
  q=[F(0)]*4
  for c in pair:q[int(c)-1]+=F(1,2)
  rows.append(tuple(q))
 return tuple(rows[g] for g in GROUP)
Q10=((F(1,2),F(0),F(1,4),F(1,4)),(F(1,2),F(0),F(1,2),F(0)),
 (F(1,2),F(0),F(0),F(1,2)),(F(1,2),F(1,2),F(0),F(0)))
D=tuple(map(decode,SPEC))+(tuple(Q10[g] for g in GROUP),)
assert len(D)==10 and all(sum(row)==1 and min(row)>=0 for d in D for row in d)
P0,P1=(prepared(theta_face(F(z),F(z))) for z in (0,1))
def interval(d,indices,r):
 lo,hi=F(0),F(1)
 for i in indices:
  for sigma in product((-1,1),repeat=4):
   c=sum((sg*(x-y) for sg,x,y in zip(sigma,P0[i],d[i])),F(0))
   b=sum((sg*(y-x) for sg,x,y in zip(sigma,P0[i],P1[i])),F(0))
   if b>0:hi=min(hi,(2*r-c)/b)
   elif b<0:lo=max(lo,(2*r-c)/b)
   elif c>2*r:return None
   if lo>hi:return None
 return (lo,hi)
r=F(9,14)
R={2:((F(0),r),(F(0),r)),5:((F(5,14),F(1)),(F(0),F(2,7))),
 9:((F(5,14),F(1)),(F(2,7),F(1))),
 10:((F(0),F(1)),(F(5,14),F(1)))}
for label,(a,b) in R.items():
 assert interval(D[label-1],range(3),r)==a
 assert interval(D[label-1],range(3,6),r)==b
 print(f'label_{label}: A={a}, B={b}')
# These four fixed-label rectangles cover [0,1]^2: s>=5/14 -> (5|9)
# and s<=5/14 -> (2|10). The two alternatives overlap in t.
S=(F(0),F(5,14),F(1));T=(F(0),F(2,7),F(5,14),r,F(1));cells=0
for (s0,s1),(t0,t1) in product(zip(S,S[1:]),zip(T,T[1:])):
 s,t=(s0+s1)/2,(t0+t1)/2
 assert any(a[0]<=s<=a[1] and b[0]<=t<=b[1] for a,b in R.values())
 cells+=1
assert cells==8
s,t=F(2,3),F(2,7)
v=tuple(loss(prepared(theta_face(s,t)),d) for d in D)
assert v==(F(1),F(2,3),F(2,3),F(1),r,F(1),F(5,6),F(17,20),r,F(5,7))
print('witness=',s,t,'all_ten_losses=',','.join(map(str,v)))
print('four_closed_rectangles_cover_full_real_square; exact_supremum=9/14')
print('PASS_BRC_N4_S23_FROZEN_TEN_BANK_2D_EXACT_9_14_20261101')
