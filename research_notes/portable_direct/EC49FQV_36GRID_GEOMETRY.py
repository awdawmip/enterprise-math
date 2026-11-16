#!/usr/bin/env python3
"""EC49FQV 36-node BRC certified area and regret; exact rational and radical bounds."""
from fractions import Fraction as F
from math import isqrt
old=sorted({F(1),F(13,12),F(7,6),F(5,4),F(4,3),F(17,12),F(3,2),F(13,8),F(7,4),F(15,8),F(2),F(17,8),F(9,4),F(19,8),F(5,2),F(31,12),F(8,3),F(11,4),F(17,6),F(23,8),F(3),F(47,16),F(39,16),F(35,16),F(37,16),*(F(n,16) for n in (25,27,29,31,33)),*(F(n,24) for n in (61,63,65,67))})
K=lambda x:F(7557)-169*x
gamma=lambda x:310*(3-x)/K(x)
assert len(old)==34
new=sorted(old+[F(11,8),F(35,24)])
assert len(new)==36
assert gamma(F(11,8))==F(4030,58597)
assert gamma(F(35,24))==F(11470,175453)
area=lambda grid:sum((b-a)*(gamma(a)-gamma(b)) for a,b in zip(grid,grid[1:]))
assert area(old)==F(928306751394905,174216767434670952)
assert area(new)==F(3866402060924905195,766379559945117517848)
assert 1-area(new)/2==F(1528892717829310130501,1532759119890235035696)
scale=10**13
def sqrt_lu(v):
 z=isqrt(v.numerator*scale**2//v.denominator)
 return F(z,scale),F(z+1,scale)
def regret_lu(a,b):
 al,au=sqrt_lu(K(a));bl,bu=sqrt_lu(K(b))
 return 50*(b-a)/(au+bu)**2,50*(b-a)/(al+bl)**2
rows=[(a,b,*regret_lu(a,b)) for a,b in zip(new,new[1:])]
maximum=next(i for i in rows if i[:2]==(F(5,4),F(4,3)))
assert all(maximum[2]>j[3] for j in rows if j!=maximum)
assert K(F(5,4))==F(29383,4) and K(F(4,3))==F(21995,3)
print('EC49FQV_36GRID_GEOMETRY_PASS',len(new),len(rows),str(area(new)),str(1-area(new)/2),'max 5/4..4/3')
