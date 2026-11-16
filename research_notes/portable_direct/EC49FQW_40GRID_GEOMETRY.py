#!/usr/bin/env python3
"""EC49FQW: self-contained exact 40-price-node geometry and strict gap comparison.
Only standard library. A prior Bellman certificate at each node is an explicit theorem hypothesis.
"""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal, localcontext

old = sorted({
    F(1), F(13,12), F(7,6), F(5,4), F(4,3), F(17,12),
    F(3,2), F(13,8), F(7,4), F(15,8), F(2), F(17,8),
    F(9,4), F(19,8), F(5,2), F(31,12), F(8,3),
    F(11,4), F(17,6), F(23,8), F(3), F(47,16),
    F(39,16), F(35,16), F(37,16),
    *(F(n,16) for n in (25,27,29,31,33)),
    *(F(n,24) for n in (61,63,65,67)),
    F(11,8), F(35,24)
})
assert len(old) == 36
added = [F(25,24), F(9,8), F(29,24), F(31,24)]
assert len(set(added)) == 4 and not any(x in old for x in added)
new = sorted(old+added)
assert len(new) == 40

K = lambda x: F(7557)-169*x
gamma = lambda x: 310*(3-x)/K(x)
beta = F(620,3299)
assert all(0<gamma(x)<beta for x in added)
assert [gamma(x) for x in added] == [
    F(310,3769),F(310,3929),F(13330,176467),F(12710,176129)
]
area = lambda grid: sum(
    (b-a)*(gamma(a)-gamma(b)) for a,b in zip(grid,grid[1:])
)
previous, current = area(old), area(new)
assert previous == F(3866402060924905195,766379559945117517848)
assert current == F(97662317051285,21777095929333869)
assert 1-current/2 == F(43456529541616453,43554191858667738)

# Exact sqrt enclosures: z^2 <= v*(10^16)^2 < (z+1)^2.
scale = 10**16
def sqrt_enclosure(v):
    z=isqrt(v.numerator*scale*scale//v.denominator)
    assert F(z*z,scale*scale)<=v<F((z+1)*(z+1),scale*scale)
    return F(z,scale),F(z+1,scale)

def regret_interval(a,b):
    al,au=sqrt_enclosure(K(a))
    bl,bu=sqrt_enclosure(K(b))
    return 50*(b-a)/(au+bu)**2,50*(b-a)/(al+bl)**2

bounds = [(a,b,*regret_interval(a,b)) for a,b in zip(new,new[1:])]
leader = next(x for x in bounds if x[:2] == (F(47,16),F(3)))
assert leader[2] > max(row[3] for row in bounds if row is not leader)
prior_max = max(regret_interval(a,b)[1] for a,b in zip(old,old[1:]))
assert leader[3] < prior_max
assert K(F(47,16)) == F(112969,16)
assert K(F(3)) == 7050
with localcontext() as c:
    c.prec=58
    d=lambda q:Decimal(q.numerator)/Decimal(q.denominator)
    m=Decimal(50)*d(F(1,16))/(d(K(F(47,16))).sqrt()+d(K(F(3))).sqrt())**2
print('EC49FQW_40GRID_GEOMETRY_PASS',len(new),
      'unresolved_area',current,'certified_fraction',1-current/2,
      'max_interval','47/16..3','max_regret',m)
