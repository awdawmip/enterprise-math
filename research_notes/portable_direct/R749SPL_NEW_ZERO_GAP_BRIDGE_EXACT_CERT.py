#!/usr/bin/env python3
"""R749SPL: exact all-real lower-Walsh zero-gap bridge triangle.
Independent stdlib-only certificate: 12 choose 7 rational bases plus signed BRC audit.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from math import comb

MASKS = (3, 12, 15, 1, 2, 4, 8)
WALSH = tuple(tuple(-1 if (k & m).bit_count() % 2 else 1 for m in MASKS) for k in range(16))

def law(t, s, h=0, u=0, v=0, w=0, z=0):
    return tuple((1 + sum((a*b for a,b in zip(row, (t,s,h,u,v,w,z))),F(0)))/16 for row in WALSH)

def tv(a, b):
    return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def solve(rows, rhs, subset):
    n = 7
    a = [list(rows[i]) + [rhs[i]] for i in subset]
    previous = 1
    for j in range(n-1):
        pivot_index = next((i for i in range(j,n) if a[i][j] != 0), None)
        if pivot_index is None: return None
        if pivot_index != j: a[j],a[pivot_index] = a[pivot_index],a[j]
        pivot = a[j][j]
        for i in range(j+1,n):
            leading = a[i][j]
            for k in range(j+1,n+1):
                numerator = a[i][k]*pivot - leading*a[j][k]
                assert numerator % previous == 0
                a[i][k] = numerator // previous
            a[i][j] = 0
        previous = pivot
    if a[-1][-2] == 0: return None
    x = [F(0)]*n
    for j in range(n-1,-1,-1):
        x[j] = (F(a[j][n]) - sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def block_mean(h, X, V):
    """1/4 sum_{c,d=+-1}|h+cX+dV|, for h,X,V >= 0."""
    return max(h,X,V,(h+X+V)/2)

def b_risk(h, X, Y, Z, Q):
    return sum((block_mean(abs(h),u,v) for u in (X,Y) for v in (Z,Q)),F(0))/8

def run():
    # Variables (t,s,h,X=|u+v|,Y=|u-v|,Z=|w+z|,Q=|w-z|).
    # Four exact block inequalities, four signed-magnitude gauges,
    # and Q = conv{(0,0),(1/5,1/5),(1/5,2/5)}.
    rows = [
        (1,1,1,-1,0,-1,0),
        (1,-1,-1,-1,0,0,-1),
        (-1,1,-1,0,-1,-1,0),
        (-1,-1,1,0,-1,0,-1),
        (0,0,0,1,0,0,0), (0,0,0,0,1,0,0),
        (0,0,0,0,0,1,0), (0,0,0,0,0,0,1),
        (1,0,0,0,0,0,0), (-1,1,0,0,0,0,0),
        (2,-1,0,0,0,0,0), (-5,0,0,0,0,0,0)
    ]
    rhs = [-1]*4 + [0]*7 + [-1]
    assert len(rows)==12 and len(rhs)==12
    vertices = set(); nonsingular = feasible = 0
    for ids in combinations(range(12),7):
        x = solve(rows,rhs,ids)
        if x is None: continue
        nonsingular += 1
        if all(sum((a*b for a,b in zip(row,x)),F(0)) >= bound for row,bound in zip(rows,rhs)):
            feasible += 1
            vertices.add(x)
    assert len(vertices)>0 and comb(12,7)==792
    maximum = None; tight = 0
    projections={}
    for t,s,h,X,Y,Z,Q in vertices:
        assert 0 <= t <= F(1,5) and t <= s <= 2*t
        u,v,w,z=(X+Y)/2,(X-Y)/2,(Z+Q)/2,(Z-Q)/2
        p=law(t,s,h,u,v,w,z)
        center=law(t,s,2*t-s)
        assert min(p)>=0 and min(center)>=0
        assert sum(p)==1 and sum(center)==1
        exact_tv=tv(p,center)
        reduced=b_risk(h-(2*t-s),X,Y,Z,Q)
        assert exact_tv==reduced
        excess=exact_tv-(1-t)/2
        maximum=excess if maximum is None else max(maximum,excess)
        tight += (excess==0)
        projections[(t,s)]=projections.get((t,s),0)+1
        # Explicit lower-bound laws remain valid on entire triangle.
        plus=law(t,s,0,-t,-t,s,1-t)
        minus=law(t,s,0,-t,-t,-s,t-1)
        assert min(plus)>=0 and min(minus)>=0
        assert tv(plus,minus)==1-t
    assert maximum==0
    for k in range(16):
        swap=((k&3)<<2)|((k&12)>>2)
        assert WALSH[swap]==(WALSH[k][1],WALSH[k][0],WALSH[k][2],WALSH[k][5],WALSH[k][6],WALSH[k][3],WALSH[k][4])
    out={
        'status':'PASS',
        'theorem':'R749SPL exact zero-gap diagonal bridge triangle and reflected copy',
        'scientific_input_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'domain_Q':'conv{(0,0),(1/5,1/5),(1/5,2/5)}',
        'domain_Q_reflected':'conv{(0,0),(1/5,1/5),(2/5,1/5)}',
        'exact_radius':'(1-t)/2 on Q; (1-s)/2 on reflected Q',
        'calibrated_center':'p(t,s,h=2t-s,u=v=w=z=0) on Q',
        'source_pair_tv':'1-t',
        'calibration_gap':'0 on Q and reflected Q',
        'additional_two_triangle_area':'1/25',
        'union_with_R749SPK_lower_wedges_area':'6/25',
        'full_sign_gauge_proof':'Risk invariant under independent signs of U+, U-, V+, V- for q with no U/V components',
        'candidate_bases':comb(12,7),
        'nonsingular_bases':nonsingular,
        'feasible_bases_with_repetitions':feasible,
        'distinct_rational_vertices':len(vertices),
        'tight_vertices':tight,
        'vertex_parameter_projection':{f'{a},{b}':v for (a,b),v in sorted(projections.items())},
        'maximum_excess':str(maximum),
        'bit_pair_exchange_checked_16_atoms':True,
        'arithmetic':'Python Fraction and integer Bareiss; no floating-point tolerances',
        'scope':'All real parameters by convexity of joint affine TV upper envelope',
        'mathematical_status':'AUTHOR_EXACT_NOT_REVIEWED',
    }
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__': run()
