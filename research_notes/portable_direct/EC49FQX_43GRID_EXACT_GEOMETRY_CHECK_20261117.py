#!/usr/bin/env python3
"""EC49FQX: 43-node exact rational BRC enclosure and strict integer-root bounds.

Scientific input: EC49FQW's 40 certified price slices and EC49FQX's
12 new complete Bellman anchors (see accompanying theorem/index).
Only the Python standard library is used.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import isqrt

old = sorted({
    F(1), F(13,12), F(7,6), F(5,4), F(4,3), F(17,12),
    F(3,2), F(13,8), F(7,4), F(15,8), F(2), F(17,8),
    F(9,4), F(19,8), F(5,2), F(31,12), F(8,3), F(11,4),
    F(17,6), F(23,8), F(3), F(47,16), F(39,16),
    F(35,16), F(37,16),
    *(F(n,16) for n in (25,27,29,31,33)),
    *(F(n,24) for n in (61,63,65,67)),
    F(11,8), F(35,24), F(25,24), F(9,8), F(29,24), F(31,24)
})
assert len(old)==40
added=[F(79,32),F(93,32),F(95,32)]
assert len(set(added))==3 and not set(old).intersection(added)
grid=sorted(old+added)
assert len(grid)==43 and grid[0]==1 and grid[-1]==3

K=lambda x:F(7557)-169*x
gamma=lambda x:310*(3-x)/K(x)
beta=F(620,3299)
assert [str(gamma(x)) for x in added]==[
    "5270/228473","310/75369","310/225769"
]
assert all(0<gamma(x)<beta for x in added)
area=lambda q:sum((b-a)*(gamma(a)-gamma(b)) for a,b in zip(q,q[1:]))
old_area, new_area=area(old),area(grid)
assert old_area==F(97662317051285,21777095929333869)
assert new_area==F(56160233186339700335,13277756713266011935728)
assert 1-new_area/2==F(26499353193345684171121,26555513426532023871456)
assert new_area<old_area
scale=10**18
def sqrt_bds(q):
    n=isqrt((q.numerator*scale*scale)//q.denominator)
    low,high=F(n,scale),F(n+1,scale)
    assert low*low<=q<high*high
    return low,high
def regret_bds(a,b):
    al,ah=sqrt_bds(K(a));bl,bh=sqrt_bds(K(b))
    return F(50)*(b-a)/(ah+bh)**2,F(50)*(b-a)/(al+bl)**2
bounds=[(a,b,*regret_bds(a,b)) for a,b in zip(grid,grid[1:])]
leader=max(bounds,key=lambda z:z[2])
assert (leader[0],leader[1])==(F(19,8),F(39,16))
assert all(leader[2]>z[3] for z in bounds if z is not leader)
assert leader[3]<max(regret_bds(a,b)[1] for a,b in zip(old,old[1:]))
with localcontext() as context:
    context.prec=60
    d=lambda f:Decimal(f.numerator)/Decimal(f.denominator)
    regret=lambda a,b:Decimal(50)*d(b-a)/(d(K(a)).sqrt()+d(K(b)).sqrt())**2
    print("CERTIFIED_AREA_PERCENT",100*(1-d(new_area)/2))
    print("NEW_MAX_REGRET_OVER_t",regret(leader[0],leader[1]))
    print("OLD_MAX_REGRET_OVER_t",max(regret(a,b) for a,b in zip(old,old[1:])))
print("EC49FQX_43_GRID_EXACT_PASS",len(grid),"leader",leader[0],leader[1])
