#!/usr/bin/env python3
"""R749SOB: Exact 5D base-fiber vertex certificate and analytic diamond constants.

Scope: auxiliary finite Walsh source model, frozen inputs of PR #2361.
Only Python standard library. Every nontrivial value is Fraction-exact.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from math import comb
import json

MASKS = (15, 1, 2, 4, 8)

def chi(mask, x):
    return 1 - 2 * ((mask & x).bit_count() & 1)

# At (t,s)=(1/2,1/2), y=(2h,2u,2v,2w,2z).
ROWS = [tuple(chi(m,x) for m in MASKS) for x in range(16)]
RHS = [-2-chi(3,x)-chi(12,x) for x in range(16)]


def solve_exact(indices):
    """Gauss-Jordan rational solve of five equalities (no floating point)."""
    a = [[Q(v) for v in ROWS[i]] + [Q(RHS[i])] for i in indices]
    for j in range(5):
        pivot = next((k for k in range(j,5) if a[k][j] != 0), None)
        if pivot is None:
            return None
        a[j],a[pivot] = a[pivot],a[j]
        factor = a[j][j]
        a[j] = [z / factor for z in a[j]]
        for k in range(5):
            if k != j:
                factor = a[k][j]
                if factor:
                    a[k] = [v - factor*w for v,w in zip(a[k],a[j])]
    return tuple(a[i][-1] for i in range(5))


def tv_to_reference(y):
    # mu_y - r_* = [sum_j (y_j - yref_j) chi_j]/32, yref=(1,0,0,0,0).
    return sum((abs(sum((Q(y[j] - int(j == 0)) * ROWS[x][j] for j in range(5)), Q(0))) for x in range(16)), Q(0)) / 64


def main():
    verts=set()
    nonsing=0
    feasible=0
    for indices in combinations(range(16),5):
        y=solve_exact(indices)
        if y is None:
            continue
        nonsing += 1
        if all(sum((a*b for a,b in zip(row,y)),Q(0)) >= bound for row,bound in zip(ROWS,RHS)):
            feasible += 1
            verts.add(y)
    assert comb(16,5)==4368
    assert len(verts)==17, ('unexpected vertex count',len(verts))
    risks=Counter(str(tv_to_reference(y)) for y in verts)
    exact_max=max(tv_to_reference(y) for y in verts)
    assert exact_max == Q(15,32)
    witness=(Q(0),Q(1),Q(1),Q(1),Q(1))
    assert witness in verts and tv_to_reference(witness)==exact_max
    # Source nonnegativity: rational margins of the 16 atoms.
    assert all(2+chi(3,x)+chi(12,x)+sum((ROWS[x][j]*witness[j] for j in range(5)),Q(0))>=0 for x in range(16))

    d=Q(1,481)
    C=d/(Q(1,2)-d)
    oldH=C+d/2
    K=Q(15,32)+oldH+d
    H_new=C*K+d/2
    lower=Q(1,110)-3*H_new
    assert K<Q(1,2)
    assert lower==Q(916283,97117786480)>0
    assert Q(15,32)+oldH+d <= Q(1,2)
    assert 3*H_new < Q(1,110)

    res={
       'result':'PASS',
       'model':'auxiliary Walsh source fiber on F_2^4, retained masks 3,12,15,1,2,4,8',
       'frozen_source':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
       'base_reference':{'t':'1/2','s':'1/2','h':'1/2','u':'0','v':'0','w':'0','z':'0'},
       'exact_vertex_certificate':{
          'active_sets':comb(16,5),
          'nonsingular_bases':nonsing,
          'feasible_bases':feasible,
          'unique_vertices':len(verts),
          'TV_to_reference_distribution':dict(sorted(risks.items(),key=lambda kv:Q(kv[0]))),
          'maximum_TV':'15/32',
          'sharp_witness_y':list(map(str,witness)),
          'sharp_witness_h_u_v_w_z':['0','1/2','1/2','1/2','1/2']
       },
       'diamond':{
           'L1_radius':'1/481',
           'area':'2/231361',
           'area_ratio_to_R749SOA':'683929/231361',
           'old_transport_H_at_radius':str(oldH),
           'local_reference_bound_K':str(K),
           'new_transport_H_at_radius':str(H_new),
           'uniform_strict_gap_lower_bound':str(lower)
       },
       'inference':'Finite exact base certificate + analytic transport inequality covers all real t,s in the closed diamond; NOT_REVIEWED'
    }
    return res

if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,ensure_ascii=False,indent=2))
