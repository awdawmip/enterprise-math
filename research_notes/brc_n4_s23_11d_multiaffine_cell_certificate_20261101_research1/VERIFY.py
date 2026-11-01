#!/usr/bin/env python3
"""Exact BRC N4 S23 11D multi-affine certificate and a 2D four-label cell cover.
Python standard-library Fraction; no floating-point tolerances or sampling claim.
"""
from fractions import Fraction as F
from itertools import product

M20 = ((10,10,0,0,0,0), (9,11,0,0,0,0), (0,0,20,0,0,0),
       (0,0,0,10,10,0), (0,0,0,2,18,0), (0,0,0,0,0,20))
A = (0,0,0,1,1,1)
B = (2,2,3,2,2,4)
C = (5,6,7,8,9,10)


def source_law(x, z):
    a,b,c = z[A[x]],z[B[x]],z[C[x]]
    return (a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c))


def prepared(z):
    law = tuple(source_law(x,z) for x in range(6))
    return tuple(tuple(sum((F(M20[i][x],20)*law[x][t] for x in range(6)),F(0))
                       for t in range(4)) for i in range(6))


def tv(u,v):
    return sum((abs(x-y) for x,y in zip(u,v)),F(0))/2


def loss(p, q):
    return max(tv(p[i],q[i]) for i in range(6))


def bank_loss(p, qs):
    return min(loss(p,q) for q in qs)


def theta_face(s,t):
    # c carries distinct provenance even within mixed AU/BU prepared rows.
    return (s,t,F(0),F(0),F(0), F(0),F(1),F(1),F(1),F(0),F(1))


def certify_box(box, qs):
    # Fixed same label for every vertex of the box -> all interior points.
    vertices = tuple(prepared(theta_face(F(s),F(t)))
                     for s,t in product(box[0], box[1]))
    return min(max(loss(p,q) for p in vertices) for q in qs)


def main():
    # Full eleven-coordinate, 2048-corner, exact multilinear identity.
    target = (F(1,3),F(2,5),F(3,7),F(4,9),F(5,11),
              F(1,2),F(2,3),F(3,4),F(4,5),F(5,6),F(6,7))
    actual = prepared(target)
    reconstructed = [[F(0) for _ in range(4)] for _ in range(6)]
    corners_checked = 0
    for bit in product((0,1),repeat=11):
        w = F(1)
        for j in range(11):
            w *= target[j] if bit[j] else 1-target[j]
        p = prepared(tuple(F(i) for i in bit))
        corners_checked += 1
        for i in range(6):
            for t in range(4):
                reconstructed[i][t] += w*p[i][t]
    assert corners_checked==2048
    assert tuple(map(tuple,reconstructed))==actual

    # Coefficient λ_ij = mixed mass of source x on which control j acts.
    lam = tuple(tuple(sum((F(M20[i][x],20)
                           for x in range(6) if j in (A[x],B[x],C[x])),F(0))
                      for j in range(11)) for i in range(6))
    assert all(sum(row)==3 for row in lam)
    assert lam[0][5:7]==(F(1,2),F(1,2))
    assert lam[1][5:7]==(F(9,20),F(11,20))
    assert lam[3][8:10]==(F(1,2),F(1,2))
    assert lam[4][8:10]==(F(1,10),F(9,10))

    # k=6 identity common encoder, four fixed source-decoder kernels.
    # Decoder αβ gives each source the stop-time law at (a_A,a_B)=(α,β).
    qs = tuple(prepared(theta_face(F(alpha),F(beta)))
               for alpha,beta in product((0,1),repeat=2))
    face_checks = 0
    for s,t in product((F(j,8) for j in range(9)), repeat=2):
        p=prepared(theta_face(s,t))
        individual = tuple(loss(p,q) for q in qs)
        expected_individual = tuple(max(abs(s-F(alpha)),abs(t-F(beta)))
                                    for alpha,beta in product((0,1),repeat=2))
        assert individual==expected_individual, (s,t,individual,expected_individual)
        assert bank_loss(p,qs)==max(min(s,1-s),min(t,1-t))
        face_checks+=1
    corners = tuple(prepared(theta_face(F(s),F(t)))
                    for s,t in product((0,1),repeat=2))
    corner_only_lower=max(bank_loss(p,qs) for p in corners)
    single_box_upper=min(max(loss(p,q) for p in corners) for q in qs)
    assert corner_only_lower==0 and single_box_upper==1
    halves = ((F(0),F(1,2)),(F(1,2),F(1)))
    box_bounds=tuple(certify_box((u,v),qs) for u,v in product(halves,repeat=2))
    assert box_bounds==(F(1,2),)*4
    center=bank_loss(prepared(theta_face(F(1,2),F(1,2))),qs)
    assert center==F(1,2)
    # Full-face 4-corner nearest-vertex Lipschitz gap: 1/2 is sharp.
    face_widths=(F(1),F(1))
    lip_error=max(sum(lam[i][j]*face_widths[j] for j in range(2))
                  for i in range(6))/2
    assert lip_error==F(1,2)
    print('full_11d_exact_multiaffine_vertices='+str(corners_checked))
    print('mixing_lambda_row_sums='+','.join(str(sum(row)) for row in lam))
    print('face_grid_rational_checks='+str(face_checks))
    print('face_corner_max_min='+str(corner_only_lower))
    print('full_box_fixed_label_upper='+str(single_box_upper))
    print('four_quadrant_fixed_label_uppers='+','.join(map(str,box_bounds)))
    print('interior_center_bank_loss='+str(center))
    print('face_nearest_corner_bound='+str(lip_error))
    print('PASS_BRC_N4_S23_11D_MULTIAFFINE_ADAPTIVE_CELL_CERT_20261101')


if __name__=='__main__':
    main()
