#!/usr/bin/env python3
"""Exact local total-variation geometry of the BRC N=4 S23 prepared map.

Extension of PR #1765 source law/positive mixing. All arithmetic is Fraction.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from random import Random

M20 = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A = (0,0,0,1,1,1)
B = (2,2,3,2,2,4)
C = (5,6,7,8,9,10)
CUTS = (1,3,5,7,9,11,13)  # One representative of each nontrivial complementary pair.
assert len(M20)==6 and all(sum(row)==20 for row in M20)
assert all(len({A[x],B[x],C[x]})==3 for x in range(6))

def latent(a,b,c):
    return a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)

def prepared(theta):
    fs=[latent(theta[A[x]],theta[B[x]],theta[C[x]]) for x in range(6)]
    return tuple(tuple(sum((Q(M20[i][x],20)*fs[x][t] for x in range(6)),Q(0))
                       for t in range(4)) for i in range(6))

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),Q(0))/2

def box_vertices(lo,hi):
    varying=[j for j in range(11) if lo[j]!=hi[j]]
    for flags in product((0,1),repeat=len(varying)):
        theta=list(lo)
        for j,flag in zip(varying,flags):
            theta[j]=hi[j] if flag else lo[j]
        yield tuple(theta)

def subset_mass(dist,mask):
    return sum((dist[t] for t in range(4) if (mask >> t)&1),Q(0))

def exact_box_geometry(lo,hi,anchor=None):
    assert len(lo)==len(hi)==11 and all(Q(0)<=a<=b<=Q(1) for a,b in zip(lo,hi))
    vertices=tuple((v,prepared(v)) for v in box_vertices(lo,hi))
    center=prepared(anchor) if anchor is not None else None
    diameter=Q(0); diameter_witness=None
    radius=Q(0); radius_witness=None
    for i in range(6):
        for mask in CUTS:
            values=[subset_mass(rows[i],mask) for _,rows in vertices]
            hi_idx=max(range(len(values)),key=values.__getitem__)
            lo_idx=min(range(len(values)),key=values.__getitem__)
            spread=values[hi_idx]-values[lo_idx]
            if spread>diameter:
                diameter=spread
                diameter_witness=(i,mask,vertices[hi_idx][0],vertices[lo_idx][0])
            if center is not None:
                z=subset_mass(center[i],mask)
                rad=max(values[hi_idx]-z,z-values[lo_idx])
                if rad>radius:
                    radius=rad
                    radius_witness=(i,mask,z,values[hi_idx],values[lo_idx])
    return diameter,diameter_witness,radius,radius_witness,vertices

def full_tv_diameter_from_pairs(vertices):
    return max((max(tv(p[i],q[i]) for i in range(6))
                for (_,p),(_,q) in combinations(vertices,2)),default=Q(0))

zero=(Q(0),)*11
# Counterexample: all-low/all-high corners miss the diameter.
lo=list(zero);hi=list(zero)
lo[0]=Q(0);hi[0]=Q(1,4)
lo[2]=Q(1,4);hi[2]=Q(1)
lo=tuple(lo);hi=tuple(hi)
d,w,_,_,v=exact_box_geometry(lo,hi)
end=max(tv(prepared(lo)[i],prepared(hi)[i]) for i in range(6))
assert len(v)==4 and d==Q(13,16) and end==Q(3,4)
assert full_tv_diameter_from_pairs(v)==d
assert { (w[2][0],w[2][2]),(w[3][0],w[3][2]) } == { (Q(1,4),Q(1,4)),(Q(0),Q(1)) }
print('MIXED_CORNER_COUNTEREXAMPLE: exact_diameter=',d,'two_diagonal_corners=',end,
      'winning_input=',w[0],'cut_mask=',w[1])

# Saturated-stage example: local diameter / exact center radius beat global anisotropic modulus.
lo=list(zero);hi=list(zero)
lo[0]=hi[0]=Q(9,10);lo[2]=hi[2]=Q(0)
lo[5]=Q(0);hi[5]=Q(1)
lo=tuple(lo);hi=tuple(hi)
mid=tuple((a+b)/2 for a,b in zip(lo,hi))
d,w,r,rw,v=exact_box_geometry(lo,hi,mid)
assert len(v)==2 and d==Q(1,20) and r==Q(1,40)
assert full_tv_diameter_from_pairs(v)==d
assert d<Q(1,2) and r<Q(1,4)
print('SATURATED_THIRD_STAGE: exact_diameter=',d,'global_diameter_bound=',Q(1,2),
      'exact_midpoint_radius=',r,'global_halfwidth_bound=',Q(1,4))
lo_s=list(lo);hi_s=list(hi)
lo_s[0]=hi_s[0]=Q(1)
assert exact_box_geometry(tuple(lo_s),tuple(hi_s))[0]==0
print('COMPLETELY_SHADOWED_CONTROL: exact_diameter=0 at a_A=1')

# All corners, all rows, seven cuts: 11-dimensional case, exact rational arithmetic.
lo=zero;hi=(Q(1),)*11
d,w,r,rw,v=exact_box_geometry(lo,hi,tuple(Q(1,2) for _ in range(11)))
assert len(v)==2048 and d==1 and Q(0)<=r<=1
print('FULL_11D_BOX: vertices=',len(v),'cuts_per_input=',len(CUTS),'diameter=',d,
      'midpoint_radius=',r)

# Six freely varying third-stage controls: an exact closed-form source-mass formula.
lo=list(zero);hi=list(zero)
for j,exact in ((0,Q(9,10)),(1,Q(2,5)),(2,Q(3,7)),
                (3,Q(1,3)),(4,Q(5,8))):
    lo[j]=hi[j]=exact
third_lo=(Q(0),Q(1,7),Q(1,3),Q(1,5),Q(0),Q(1,8))
third_hi=(Q(1),Q(6,7),Q(3,4),Q(4,5),Q(1,2),Q(1))
for j,(a,b) in enumerate(zip(third_lo,third_hi),start=5):
    lo[j]=a;hi[j]=b
lo=tuple(lo);hi=tuple(hi)
computed=[];closed=[]
for i in range(6):
    computed.append(tv(prepared(lo)[i],prepared(hi)[i]))
    closed.append(sum((Q(M20[i][x],20)*(1-lo[A[x]])*(1-lo[B[x]])
                       *(hi[C[x]]-lo[C[x]]) for x in range(6)),Q(0)))
assert tuple(computed)==tuple(closed)
assert exact_box_geometry(lo,hi)[0]==max(closed)
print('SIX_C_STAGE_FACE: row_exact_diameters=',','.join(map(str,closed)),
      'overall=',max(closed),'full_vertices=',64)

# Independent brute-force pair checks on seeded rational boxes, small dimension only.
rng=Random(20261101)
for trial in range(32):
    lo=list(zero);hi=list(zero)
    varying=rng.sample(range(11),3)
    for j in range(11):
        l=Q(rng.randrange(5),5)
        u=l+Q(rng.randrange(6-int(l*5)),5)
        lo[j]=hi[j]=l
        if j in varying:
            hi[j]=u
    lo=tuple(lo);hi=tuple(hi)
    mid=tuple((a+b)/2 for a,b in zip(lo,hi))
    d,_,r,_,v=exact_box_geometry(lo,hi,mid)
    assert d==full_tv_diameter_from_pairs(v)
    assert r==max(max(tv(prepared(mid)[i],rows[i]) for i in range(6)) for _,rows in v)
    assert r<=d
    for _ in range(6):
        theta=tuple(a+(b-a)*Q(rng.randrange(11),10) for a,b in zip(lo,hi))
        phi=tuple(a+(b-a)*Q(rng.randrange(11),10) for a,b in zip(lo,hi))
        assert max(tv(prepared(theta)[i],prepared(phi)[i]) for i in range(6))<=d
print('RANDOM_RATIONAL_3D_BOXES: exact_pairs_and_midpoint_radii=',32,
      'interior_pairs=',32*6)
print('PASS_BRC_N4_S23_LOCAL_BOX_EXACT_TV_GEOMETRY_20261101')
