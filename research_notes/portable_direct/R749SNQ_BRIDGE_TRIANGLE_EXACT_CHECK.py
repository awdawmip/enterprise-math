#!/usr/bin/env python3
"""R749SNQ: exact zero-calibration bridge triangle, source-frozen Walsh model."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json

PIN = 'a72226e2430ffa4786321ac86e7f0c599d5f0389'
MASKS = (3, 12, 15, 1, 2, 4, 8)
ROWS = [tuple(1 if (mask & x).bit_count() % 2 == 0 else -1
              for mask in MASKS) for x in range(16)]
EVENT = (3, 5, 7, 9, 11, 13, 14, 15)
TRIANGLE = ((Q(7, 10), Q(3, 20)), (Q(7, 10), Q(1, 5)), (Q(4, 5), Q(1, 5)))


def law(t, s, h=0, u=0, v=0, w=0, z=0):
    coefs = (t, s, h, u, v, w, z)
    return tuple((1 + sum((c * r for c, r in zip(coefs, row)), Q(0))) / 16
                 for row in ROWS)


def radius(t, s):
    return (3 + t - s) / 8


def eta(t, s):
    return Q(3, 2) * (s - Q(1, 5))


def solve_integer(M, rhs, selected, n=7):
    """Exact Bareiss determinant-preserving elimination with row pivots."""
    a = [list(M[i]) + [rhs[i]] for i in selected]
    prev = 1
    for j in range(n - 1):
        piv = next((i for i in range(j, n) if a[i][j]), None)
        if piv is None:
            return None
        if piv != j:
            a[j], a[piv] = a[piv], a[j]
        leading = a[j][j]
        for i in range(j + 1, n):
            old = a[i][j]
            for k in range(j + 1, n + 1):
                num = a[i][k] * leading - old * a[j][k]
                assert num % prev == 0
                a[i][k] = num // prev
            a[i][j] = 0
        prev = leading
    if not a[n - 1][n - 1]:
        return None
    result = [Q(0)] * n
    for j in range(n - 1, -1, -1):
        result[j] = (Q(a[j][-1]) - sum((a[j][k] * result[k] for k in range(j + 1, n)), Q(0))) / a[j][j]
    return tuple(result)


def certify():
    # Let y = 20*(t,s,h,u,v,w,z). The 16 atom inequalities are 20+ROW*y >= 0.
    M = list(ROWS)
    rhs = [-20] * 16
    # t>=7/10; s<=1/5; 2s-t >= -2/5
    M.extend(((1,0,0,0,0,0,0),(0,-1,0,0,0,0,0),(-1,2,0,0,0,0,0)))
    rhs.extend((14,-4,-8))
    vertices = set()
    stats = {'active_bases': 0, 'nonsingular_bases': 0, 'feasible_bases': 0,
             'unique_vertices': 0, 'tight_vertices': 0, 'violating_vertices': 0}
    for selected in combinations(range(19), 7):
        stats['active_bases'] += 1
        y = solve_integer(M, rhs, selected)
        if y is None:
            continue
        stats['nonsingular_bases'] += 1
        if any(sum((a * b for a,b in zip(row,y)),Q(0)) < bound
               for row,bound in zip(M,rhs)):
            continue
        stats['feasible_bases'] += 1
        vertices.add(tuple(z / 20 for z in y))
    assert stats['active_bases'] == comb(19,7) == 50388
    stats['unique_vertices'] = len(vertices)
    assert len(vertices) > 0
    largest_excess = None
    for t,s,h,u,v,w,z in vertices:
        mu = law(t,s,h,u,v,w,z)
        q = law(t,s,eta(t,s))
        assert all(x>=0 for x in mu) and all(x>=0 for x in q)
        assert sum(mu)==sum(q)==1
        tv = sum((abs(a-b) for a,b in zip(mu,q)), Q(0))/2
        excess = tv-radius(t,s)
        largest_excess = excess if largest_excess is None else max(largest_excess,excess)
        stats['tight_vertices'] += (excess==0)
        stats['violating_vertices'] += (excess>0)
    stats['max_excess'] = str(largest_excess)
    assert largest_excess == 0 and stats['violating_vertices'] == 0
    for t,s in TRIANGLE:
        center=law(t,s,eta(t,s))
        W=law(t,s,0,s-1,-t,-s,-s)
        assert min(center)>=0 and min(W)>=0 and sum(W)==1
        assert all(sum(ROWS[x][i] for x in EVENT)==0 for i in range(3))
        assert sum((W[x] for x in EVENT),Q(0))-Q(1,2)==radius(t,s)
    assert eta(Q(7,10),Q(3,20)) == -Q(3,40)
    assert eta(Q(7,10),Q(1,5)) == eta(Q(4,5),Q(1,5)) == 0
    stats['triangle_vertices'] = [[str(t),str(s)] for t,s in TRIANGLE]
    return {'unit':'R749SNQ', 'status':'PASS', 'frozen_scientific_pin':PIN,
            'scope':'all real (t,s) in conv((7/10,3/20),(7/10,1/5),(4/5,1/5)); auxiliary 16-state Walsh source, author proof, independent review pending',
            'theorem':'rho(t,s)=rho_cal(t,s)=(3+t-s)/8',
            'center':'q(x)=(1+t*A+s*D+(3/2)*(s-1/5)*AD)/16',
            'lower_witness':'W=(h,u,v,w,z)=(0,s-1,-t,-s,-s), E={3,5,7,9,11,13,14,15}',
            'certificate':stats}


if __name__=='__main__':
    print(json.dumps(certify(), indent=2, sort_keys=True))
