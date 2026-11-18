#!/usr/bin/env python3
"""Exact rational node/slope optimization for the Collins Yukawa regulator.
Output reports leading dimensionless coefficients; no measured UV data are used.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def solve(A,b):
    n = len(b)
    rows = [[F(x) for x in row]+[F(y)] for row,y in zip(A,b)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if rows[i][j]),None)
        if pivot is None:
            return None
        rows[j],rows[pivot] = rows[pivot],rows[j]
        den = rows[j][j]
        rows[j] = [v/den for v in rows[j]]
        for i in range(n):
            if i != j and rows[i][j]:
                t = rows[i][j]
                rows[i] = [x-t*y for x,y in zip(rows[i],rows[j])]
    return [row[-1] for row in rows]


def feasible(y,constraints):
    return all(dot(a,y) <= b for a,b in constraints)


def profile_problem(h,bands,floors,caps):
    # End values are 1 and 0, with all interior heights in closed intervals.
    n = len(bands)
    cmat = [[int(i == j+1)-int(i == j) for j in range(n)] for i in range(n+1)]
    offsets = [1]+[0]*n
    cons = []
    for j,(a,b) in enumerate(bands):
        v = [int(i==j) for i in range(n)]
        cons.extend([(v,b),([-x for x in v],-a)])
    for i,c in enumerate(cmat):
        cons.extend([(c,h[i]*caps[i]-offsets[i]),
                     ([-x for x in c],offsets[i]-h[i]*floors[i])])
    hess = [[2*sum(F(c[i]*c[j],w) for c,w in zip(cmat,h))
             for j in range(n)] for i in range(n)]
    linear = [2*sum(F(c[j]*t,w) for c,t,w in zip(cmat,offsets,h)) for j in range(n)]
    def energies(y):
        d = [v+dot(c,y) for v,c in zip(offsets,cmat)]
        return (sum(x*x/w for x,w in zip(d,h)),
                sum((a+b)*x-a*b*w for a,b,x,w in zip(floors,caps,d,h)))
    minima,vertices = [],[]
    for k in range(n+1):
        for active in combinations(range(len(cons)),k):
            lhs = [row+[cons[i][0][j] for i in active] for j,row in enumerate(hess)]
            lhs.extend([cons[i][0]+[0]*k for i in active])
            rhs = [-x for x in linear]+[cons[i][1] for i in active]
            result = solve(lhs,rhs)
            if result is None or not feasible(result[:n],cons):
                continue
            y = result[:n]
            if all(l >= 0 for l in result[n:]):
                minima.append((energies(y)[0],y))
            if k == n:
                vertices.append((energies(y)[1],y))
    assert minima and vertices
    return min(minima),max(vertices),energies


def exact_energy(times,heights):
    return sum(F((y-v)**2,b-a) for a,b,y,v in zip(times,times[1:],heights,heights[1:]))


def encode(obj):
    if isinstance(obj,F):
        return str(obj)
    raise TypeError(obj)


def main():
    h = [F(1),F(2),F(1)]
    bands = [(F(4,5),F(9,10)),(F(1,10),F(1,5))]
    floor = [F(0)]*3
    cap = [F(1,2),F(1),F(1,2)]
    minimum,maximum,energy = profile_problem(h,bands,floor,cap)
    assert minimum == (F(13,50),[F(4,5),F(1,5)])
    assert maximum == (F(9,10),[F(9,10),F(1,10)])
    for u,v in product(range(80,91),range(10,21)):
        lo,hi = energy([F(u,100),F(v,100)])
        assert minimum[0] <= lo <= hi <= maximum[0]
    # Holding the same exact nodes in both species gives a specific true cancellation.
    low,high = energy(minimum[1])
    assert high == F(4,5)
    energies = [F(1,3),F(3,4)]
    theta2 = [(e-low)/(high-low) for e in energies]
    assert all(0 < u < 1 for u in theta2)
    assert [low+x*(high-low) for x in theta2] == energies
    assert 3*(1+2*energies[0]) == 2*(1+2*energies[1]) == 5
    independent_gap = 4*(1+2*minimum[0])-(1+2*maximum[0])
    shared_gap = 3*(1+2*minimum[0])
    assert independent_gap == F(82,25) and shared_gap == F(114,25)
    # Each inserted measurement supplies the exact squared-slope residual.
    base_t = [F(0),F(1),F(3),F(4)]
    base_y = [F(1),*minimum[1],F(0)]
    extra = exact_energy([0,1,2,3,4],[1,*[base_y[1],F(3,5),base_y[2]],0])-exact_energy(base_t,base_y)
    assert extra == F(1,50)
    orthogonal_cases = 0
    for t in (F(3,2),F(2),F(5,2)):
        for z in (F(2,5),F(1,2),F(3,5)):
            linear = ((3-t)*base_y[1]+(t-1)*base_y[2])/2
            new = exact_energy([0,1,t,3,4],[1,base_y[1],z,base_y[2],0])
            assert new-exact_energy(base_t,base_y) == 2*(z-linear)**2/((t-1)*(3-t))
            orthogonal_cases += 1
    # A second obstacle with nonzero lower slope exercises both local bound terms.
    lower = [F(1,8),F(1,4),F(1,8)]
    other_min,other_max,_ = profile_problem(h,bands,lower,cap)
    assert other_min[0] == F(13,50) and other_min[0] <= other_max[0] < maximum[0]
    # f_n(x)=(1+x**n)^(-1); u=1-f_n maps its energy to n*int_0^1 u(1-u)du.
    simpson = (0+4*F(1,2)*(1-F(1,2))+0)/6
    assert simpson == F(1,6)
    assert 7*(1+2*2*simpson) == 5*(1+2*4*simpson)
    print(json.dumps(dict(
        coefficient_units='speed contrast multiplied by 24*pi^2/g^2, one-loop term only',
        log_widths=h,node_intervals=bands,upper_slopes=cap,
        obstacle_minimum=minimum,obstacle_maximum=maximum,grid_checks=121,
        exact_nodes=minimum[1],exact_node_energy_range=[low,high],interior_energy_pair=energies,
        slope_interpolation_theta_squared=theta2,
        common_value_for_squared_coupling_ratio_3_to_2=5,
        minimum_difference_ratio_4_to_1_independent=independent_gap,
        minimum_difference_ratio_4_to_1_common_shape=shared_gap,
        inserted_node_energy_gain=extra,orthogonality_checks=orthogonal_cases,
        positive_lower_slope_example=dict(slope_floor=lower,minimum=other_min,maximum=other_max),
        smooth_rational_profiles=dict(exponents=[2,4],energies=[2*simpson,4*simpson],
                                     cancelling_squared_couplings=[7,5])),
        default=encode,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
