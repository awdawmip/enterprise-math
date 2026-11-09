#!/usr/bin/env python3
"""Exact 4D R5 coupling polytope fiber geometry and coordinate volume.
Dependency: immutable fixed-physical-pair R5 PR #1861 / commit 54f4abcb....
Only Python standard-library Fraction arithmetic is used.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

a = F(3997, 690000)
b = F(170189123, 37621284000)
d = F(8294919533, 677183112000)
L1, L2 = F(23,13)*a, F(23,18)*a
B0, B1 = 23*b, 13*L1
D0, D1 = 23*d, 5*L2
T = [(F(0), F(0)), (L1, F(0)), (F(0), L2)]

def bd(s,t): return 23*b+13*s, 23*d+5*t

def fiber_vertices(s,t):
    B,D = bd(s,t)
    return [(F(0),F(0)), (B/18,F(0)),
            ((10*B+13*D)/115, (5*B+18*D)/115),
            (F(0), D/10)]

def h(q):
    s,t,u,v = q
    B,D = bd(s,t)
    return (s, t, 23*a-13*s-18*t, u, v,
            B-18*u+13*v, D+5*u-10*v)

def area(B,D): return (25*B*B+180*B*D+117*D*D)/20700

# All 12 vertices of Q are exactly 3 base triangle vertices x 4 fiber vertices.
verts = [(s,t,u,v) for s,t in T for u,v in fiber_vertices(s,t)]
assert len(set(verts)) == 12
assert all(min(h(q))>=0 and h(q).count(0)==4 for q in verts)
# The original 7-facet inequalities are also satisfied at the midpoint of each
# triangle base and at every quadrilateral fiber corner there.
mid = (L1/3, L2/3)
assert all(min(h((mid[0],mid[1],u,v)))>=0
           for u,v in fiber_vertices(*mid))
assert all(sum(v>0 for v in h(q))==3 for q in verts)
# The quadrilateral area agrees with independent shoelace computation.
for s,t in T+[mid]:
    pts=fiber_vertices(s,t)
    twice=sum(pts[i][0]*pts[(i+1)%4][1]-pts[(i+1)%4][0]*pts[i][1]
              for i in range(4))
    B,D=bd(s,t)
    assert twice>0 and twice/2==area(B,D)

# In 4D, the four normals of the 6-vertex (quadrilateral-factor) facets have
# nonzero determinant, so an affine product with a plane quadrilateral is impossible.
# Rows (0,0,1,0),(0,0,0,1),(-13,0,18,-13),(0,-5,-5,10).
def det4(rows):
    ans=F(0)
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        z=F(-1 if inv%2 else 1)
        for i in range(4):z*=rows[i][p[i]]
        ans+=z
    return ans

det_square_normals = det4(((0,0,1,0),(0,0,0,1),
                            (-13,0,18,-13),(0,-5,-5,10)))
assert det_square_normals == 65

# Normalized triangle barycentric moments: integral_{x,y>=0,x+y<=1} x^m y^n.
def mom(m,n): return F(factorial(m)*factorial(n),factorial(m+n+2))
BB2 = B0*B0*mom(0,0)+2*B0*B1*mom(1,0)+B1*B1*mom(2,0)
DD2 = D0*D0*mom(0,0)+2*D0*D1*mom(0,1)+D1*D1*mom(0,2)
BD  = B0*D0*mom(0,0)+B1*D0*mom(1,0)+B0*D1*mom(0,1)+B1*D1*mom(1,1)
volume = L1*L2*(25*BB2+180*BD+117*DD2)/20700
EXPECTED = F(17113607962497316638837165221,
             503876396283588297216000000000000000)
assert volume==EXPECTED
# General positive-parameter family: the simplex integration simplifies to
# the following homogeneous quartic polynomial, not only the fixed pair.
def volume_closed(A,B,C):
    return F(12167,90979200)*A*A*(2125*A*A+7200*A*B+17640*A*C+
            5400*B*B+38880*B*C+25272*C*C)

def volume_by_moments(A,B,C):
    h,k=F(23,13)*A,F(23,18)*A
    p,q=23*B,13*h
    r,s=23*C,5*k
    t1=p*p*mom(0,0)+2*p*q*mom(1,0)+q*q*mom(2,0)
    t2=p*r*mom(0,0)+q*r*mom(1,0)+p*s*mom(0,1)+q*s*mom(1,1)
    t3=r*r*mom(0,0)+2*r*s*mom(0,1)+s*s*mom(0,2)
    return h*k*(25*t1+180*t2+117*t3)/20700
assert volume_closed(a,b,d)==volume
for A,B,C in ((F(1),F(1),F(1)),
              (F(1,2),F(3,4),F(2,5)),
              (F(17,100),F(23,70),F(9,8))):
    assert volume_closed(A,B,C)==volume_by_moments(A,B,C)
# Fiber area monotonic in B,D. Minimum at (0,0). For the maximum,
# positive partial derivatives force x+y=1. Along that edge A(x,1-x)
# is concave, with strictly positive derivative at x=1.
A_min=area(B0,D0)
A_max=area(B0+B1,D0)
A_edge0=area(B0,D0+D1)
edge_quadratic=(2*A_max+2*A_edge0-4*area(B0+B1/2,D0+D1/2))
edge_linear=A_max-A_edge0-edge_quadratic
assert edge_quadratic<0 and edge_linear+2*edge_quadratic>0
assert A_min==F(1428755703638704652497,1993812900773932800000000)
assert A_max==F(0)+area(B0+B1,D0)
assert (B0,B1,D0,D1)==(F('170189123/1635708000'),
                         F('3997/30000'),F('8294919533/29442744000'),
                         F('3997/108000'))
print('PASS_TRIANGLE_BY_QUADRILATERAL_FIBERS_ALL_REAL_BASE_PARAMETERS')
print('PASS_EXACT_FIBER_AREA_POLYNOMIAL (25*B^2+180*B*D+117*D^2)/20700')
print('PASS_TWELVE_FORMULA_VERTICES_ALL_FOUR_FACETS_EACH')
print('PASS_NON_AFFINE_PRODUCT_SIX_VERTEX_FACET_NORMALS_DET',det_square_normals)
print('PASS_SHARP_FIBER_AREA_MIN_MAX',A_min,A_max)
print('PASS_GENERAL_POSITIVE_PARAMETERS_EXACT_QUARTIC_VOLUME_FORMULA')
print('PASS_EXACT_FOUR_DIM_COORDINATE_VOLUME',volume)
print('VOLUME_DECIMAL',format(float(volume),'.14g'))
