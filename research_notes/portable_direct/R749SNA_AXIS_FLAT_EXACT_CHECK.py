#!/usr/bin/env python3
"""Exact polytope-vertex certificate for a full Walsh minimax axis."""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
import json

C = (1, 2, 4, 8, 15)
B = tuple(k for k in range(1,16) if k not in C)
VARIABLE_MASKS = (3,) + C  # coordinates (t,u,v,w,z,h)

def chi(k,x):
    return 1 if (k & x).bit_count() % 2 == 0 else -1

def solve(A,b):
    n=len(b)
    m=[[Q(v) for v in row]+[Q(v)] for row,v in zip(A,b)]
    for j in range(n):
        k=next((i for i in range(j,n) if m[i][j]),None)
        if k is None: return None
        m[k],m[j]=m[j],m[k]
        factor=m[j][j]
        m[j]=[x/factor for x in m[j]]
        for i in range(n):
            if i!=j and m[i][j]:
                factor=m[i][j]
                m[i]=[a-factor*b for a,b in zip(m[i],m[j])]
    return tuple(row[-1] for row in m)

ROW=tuple(tuple(chi(k,x) for k in VARIABLE_MASKS) for x in range(16))
count_nonsingular=count_feasible=0
vertices=set()
for inds in combinations(range(16),6):
    z=solve([ROW[x] for x in inds], [-1]*6)
    if z is None: continue
    count_nonsingular += 1
    if any(1+sum(a*v for a,v in zip(ROW[x],z))<0 for x in range(16)):
        continue
    count_feasible += 1
    vertices.add(z)

assert (count_nonsingular,count_feasible,len(vertices)) == (3520,1920,18)
assert all(-1<=z[0]<=1 for z in vertices)

def tv_to_calibrated(z):
    return sum(abs(sum(z[j+1]*chi(C[j],x) for j in range(5))) for x in range(16))/32

expected = Counter({Q(-1):2, Q(-1,2):4,Q(0):6,Q(1,2):4,Q(1):2})
assert Counter(z[0] for z in vertices) == expected
TV=Counter(str(tv_to_calibrated(z)) for z in vertices)
assert TV == Counter({'1/2':10,'3/8':8}),TV
assert max(tv_to_calibrated(z) for z in vertices)==Q(1,2)

# Every admissible law is a convex combination of the exact vertices;
# total variation from affine q_t is jointly convex in the 6 variables.
# The disjoint witnesses (1+t chi_3)(1 +/- chi_1)/16 provide sharpness.
for t in (Q(-1),Q(-3,4),Q(-1,3),Q(0),Q(1,3),Q(3,4),Q(1)):
    pair=[]
    for sig in (-1,1):
        p=tuple((1+t*chi(3,x))*(1+sig*chi(1,x))/16 for x in range(16))
        assert min(p)>=0 and sum(p)==1
        assert all(sum(p[x]*chi(k,x) for x in range(16)) == (t if k==3 else 0) for k in B)
        pair.append(p)
    assert sum(abs(a-b) for a,b in zip(*pair))/2 == 1

result={
 'schema':'R749SNA_AXIS_FLAT_WALSH_MINIMAX_CERTIFICATE_V1',
 'status':'PASS',
 'frozen_science_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'domain':'G=F2^4; all real t in [-1,1], s=0; other B moments zero',
 'nonnegativity_facets':16,
 'joint_polytope_dimension':6,
 'six_facet_subsets':8008,
 'nonsingular_subsets':count_nonsingular,
 'feasible_subsets':count_feasible,
 'unique_vertices':len(vertices),
 'vertex_t_counts':{str(t):n for t,n in sorted(expected.items())},
 'tv_histogram':dict(sorted(TV.items())),
 'sharp_uniform_upper':'1/2',
 'disjoint_lower':'1/2',
 'unrestricted_minimax_axis':'rho_B(t,0)=1/2 for all real t in [-1,1]',
 'calibrated_minimax_axis':'rho_cal(t,0)=1/2 for all real t in [-1,1]',
 'symmetric_axis':'rho_B(0,s)=rho_cal(0,s)=1/2 for all real s in [-1,1]',
 'arithmetic':'standard library fractions.Fraction exact elimination and full finite vertex enumeration',
 'native_status':'abstract Walsh observer only; V29/V39 mapping not asserted',
}
print(json.dumps(result,ensure_ascii=False,indent=2))
