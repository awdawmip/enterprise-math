#!/usr/bin/env python3
"""EC49FQY: 45-price-grid exact rational enclosure verifier.

Inputs: inherited 43 certified prices (EC49FQX PR #2583), plus
new exact Bellman-certified prices 75/32 and 77/32.
No external Python dependencies.
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
    F(11,8), F(35,24), F(25,24), F(9,8),
    F(29,24), F(31,24),
    *(F(n,32) for n in (79,93,95))
})
assert len(old) == 43, len(old)
new = [F(75,32), F(77,32)]
assert not set(old).intersection(new)
grid = sorted(old + new)
assert len(grid) == 45 and grid[0] == 1 and grid[-1] == 3

K = lambda x: F(7557) - 169*x
gamma = lambda x: 310*(3-x)/K(x)
beta = F(620,3299)
assert [str(gamma(x)) for x in new] == ["2170/76383","190/7381"]
assert all(0 < gamma(x) < beta for x in new)

area = lambda g: sum(
    ((b-a)*(gamma(a)-gamma(b)) for a,b in zip(g,g[1:])), F(0)
)
old_area, new_area = area(old), area(grid)
assert old_area == F(56160233186339700335,13277756713266011935728)
assert new_area == F(162317745998378463895,39951040674583873370736)
certified = 1-new_area/2
assert certified == F(79739763603169368277577,79902081349167746741472)
assert new_area < old_area

for a,b in zip(grid,grid[1:]):
    delta = b-a
    # Exact derivative/integral identity for the certified strip.
    assert gamma(a)-gamma(b) == F(2185500)*delta/(K(a)*K(b))
    assert K(a) > K(b) > 0

scale = 10**18
def sqrt_bounds(q):
    n = isqrt((q.numerator*scale*scale)//q.denominator)
    low, high = F(n,scale), F(n+1,scale)
    assert low*low <= q < high*high
    return low,high

def regret_bounds(a,b):
    al,ah = sqrt_bounds(K(a)); bl,bh = sqrt_bounds(K(b))
    return F(50)*(b-a)/(ah+bh)**2, F(50)*(b-a)/(al+bl)**2

bounds = [(a,b,*regret_bounds(a,b)) for a,b in zip(grid,grid[1:])]
leader = max(bounds,key=lambda z:z[2])
assert leader[0:2] == (F(9,4),F(37,16))
assert all(leader[2] > z[3] for z in bounds if z is not leader)
assert leader[3] < max(regret_bounds(a,b)[1] for a,b in zip(old,old[1:]))

# Exact insertion gain from area strips, checked for each inserted price.
for c in new:
    k = grid.index(c); a,b = grid[k-1],grid[k+1]
    direct = (b-a)*(gamma(a)-gamma(b)) - (
        (c-a)*(gamma(a)-gamma(c)) + (b-c)*(gamma(c)-gamma(b)))
    formula = F(2185500)*(c-a)*(b-c)/K(c)*(1/K(a)+1/K(b))
    assert direct == formula > 0

with localcontext() as c:
    c.prec=55
    d=lambda z: Decimal(z.numerator)/Decimal(z.denominator)
    def regret(a,b):
        return Decimal(50)*d(b-a)/(d(K(a)).sqrt()+d(K(b)).sqrt())**2
    print("CERTIFIED_AREA_PERCENT", 100*d(certified))
    print("UNPROVED_STRIP_AREA", new_area)
    print("MAX_CERTIFIED_REGRET_OVER_t", regret(leader[0],leader[1]))
    print("PREVIOUS_MAX_REGRET_OVER_t",
          max(regret(a,b) for a,b in zip(old,old[1:])))
print("EC49FQY_45GRID_EXACT_PASS",len(grid),"leader",leader[0],leader[1])
