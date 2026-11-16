#!/usr/bin/env python3
"""EC49FQU 34-node enclosure: exact rational and integer-root verification."""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal, localcontext
G0={F(1),F(13,12),F(7,6),F(5,4),F(4,3),F(17,12),F(3,2),F(13,8),F(7,4),F(15,8),F(2),F(17,8),F(9,4),F(19,8),F(5,2),F(31,12),F(8,3),F(11,4),F(17,6),F(23,8),F(3),F(47,16),F(39,16),F(35,16),F(37,16),*(F(n,16) for n in (25,27,29,31,33))}
NEW=[F(61,24),F(21,8),F(65,24),F(67,24)]
K=lambda x:F(7557)-169*x
gamma=lambda x:F(310)*(3-x)/K(x)
assert len(G0)==30 and len(G0|set(NEW))==34
assert list(map(gamma,NEW))==[F(3410,171059),F(310,18969),F(2170,170383),F(310,34009)]
G=sorted(G0|set(NEW)); pairs=list(zip(G,G[1:]))
assert len(pairs)==33
S=sum((b-a)*(gamma(a)-gamma(b)) for a,b in pairs)
assert S==F(928306751394905,174216767434670952)
certified=1-S/2
assert certified==F(347505228117946999,348433534869341904)
scale=10**12
def sqrt_interval(v):
    z=isqrt(v.numerator*scale**2//v.denominator)
    return F(z,scale),F(z+1,scale)
def upper_lower(a,b):
    l1,u1=sqrt_interval(K(a));l2,u2=sqrt_interval(K(b))
    numerator=50*(b-a)
    return numerator/(u1+u2)**2,numerator/(l1+l2)**2
scores=[(a,b,*upper_lower(a,b)) for a,b in pairs]
maxrow=next(x for x in scores if x[:2]==(F(17,12),F(3,2)))
assert all(maxrow[2]>other[3] for other in scores if other!=maxrow)
assert K(F(17,12))==F(87811,12) and K(F(3,2))==F(14607,2)
print("EC49FQU_34GRID_GEOMETRY_PASS",str(S),str(certified),"max:[17/12,3/2]")
