#!/usr/bin/env python3
"""R284T reproducible exact-rational determinant/cofactor certificate.

Standalone: Python standard library only. The program checks small explicitly
specified auxiliary Port systems, not native X6 dynamics.
"""
from fractions import Fraction as Q
import json
from itertools import product


def det(A):
    n = len(A)
    a = [[Q(z) for z in row] for row in A]
    assert all(len(row) == n for row in a)
    sign, out = 1, Q(1)
    for k in range(n):
        p = next((j for j in range(k, n) if a[j][k]), None)
        if p is None:
            return Q(0)
        if p != k:
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        out *= pivot
        for i in range(k + 1, n):
            fac = a[i][k] / pivot
            for j in range(k + 1, n):
                a[i][j] -= fac * a[k][j]
            a[i][k] = Q(0)
    return out * sign


def inverse(A):
    n = len(A)
    a = [[Q(v) for v in row] + [Q(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for k in range(n):
        p = next((j for j in range(k, n) if a[j][k]), None)
        assert p is not None, 'singular input in declared stable case'
        a[k], a[p] = a[p], a[k]
        v = a[k][k]
        a[k] = [u / v for u in a[k]]
        for i in range(n):
            if i != k:
                v = a[i][k]
                a[i] = [u - v * w for u, w in zip(a[i], a[k])]
    return [row[n:] for row in a]


def matrix(t, a, b, gamma, x=Q(0), y=Q(0)):
    # W_00=t+y, W_01=a, W_12=x, W_20=b, W_21=gamma.
    W = [[t + y, a, Q(0)], [Q(0), Q(0), x], [b, gamma, Q(0)]]
    assert all(all(v >= 0 for v in row) and sum(row) < 1 for row in W)
    return [[Q(int(i == j)) - W[i][j] for j in range(3)] for i in range(3)]


def bordered(M1, M2):
    n1, n2 = len(M1), len(M2)
    K = [[Q(0) for j in range(n1+n2+1)] for i in range(n1+n2+1)]
    for i in range(n1):
        for j in range(n1): K[i][j] = M1[i][j]
    for i in range(n2):
        for j in range(n2): K[n1+i][n1+j] = M2[i][j]
    K[0][-1] = Q(1)
    K[n1][-1] = Q(-1)
    K[-1][0] = Q(1)
    K[-1][n1] = Q(1)
    return K


def replace_two(K, r1, u1, r2, u2):
    out = [row[:] for row in K]
    for i in range(len(out)):
        out[i][r1] = Q(int(i == u1))
        out[i][r2] = Q(int(i == u2))
    return out


def f(M): return inverse(M)[0][0]


def normalized_p(M1, M2):
    d1, d2 = det(M1), det(M2)
    return (f(M1)-f(M2))*d1*d2


def second_coeff_det(model1, model2, which, other):
    """S_i=[x_i^2]P by one 7x7 column-replacement determinant.
    For x: the column v=2 of each block is edited, with u=1.
    For y: the column v=0 of each block is edited, with u=0.
    """
    x,y = (Q(0), other) if which=='x' else (other, Q(0))
    M1 = matrix(*model1,x,y)
    M2 = matrix(*model2,x,y)
    K = bordered(M1,M2)
    col, row = (2,1) if which=='x' else (0,0)
    return -det(replace_two(K, col,row,3+col,3+row))


def second_coeff_interpolation(model1, model2, which, other):
    t = Q(1,20)
    def P(v):
        x,y=(v,other) if which=='x' else (other,v)
        return normalized_p(matrix(*model1,x,y),matrix(*model2,x,y))
    return (P(Q(2)*t)-Q(2)*P(t)+P(Q(0)))/(Q(2)*t*t)


def s(v): return str(v)


# Two relevant, genuinely cyclic named edits x and y in both systems.
m1=(Q(1,4),Q(1,4),Q(3,8),Q(0))
m2=(Q(0),Q(1,4),Q(3,8),Q(0))
main_grid=[Q(0),Q(1,20),Q(1,10)]
for x,y in product(main_grid,repeat=2):
    A,B=matrix(*m1,x,y),matrix(*m2,x,y)
    D1,D2=det(A),det(B)
    assert D1 == Q(3,4)-y-Q(3,32)*x
    assert D2 == Q(1)-y-Q(3,32)*x
    assert f(A)==1/D1 and f(B)==1/D2
    assert normalized_p(A,B) == Q(1,4)
    assert -det(bordered(A,B)) == Q(1,4)

coefficient_checks=0
for which in ('x','y'):
    for other in main_grid:
        A=second_coeff_det(m1,m2,which,other)
        B=second_coeff_interpolation(m1,m2,which,other)
        assert A==B==0,(which,other,A,B)
        coefficient_checks+=1

# Nonzero quadratic obstruction inherited from R284S; the same determinant
# detects the true x^2 coefficient at one y=0 point, with no inverses.
c1=(Q(0),Q(1,4),Q(1,4),Q(0))
c2=(Q(0),Q(1,4),Q(15,64),Q(1,4))
assert second_coeff_det(c1,c2,'x',Q(0))==Q(-1,64)
assert second_coeff_interpolation(c1,c2,'x',Q(0))==Q(-1,64)
for x in (Q(0),Q(1,16),Q(1,4),Q(1,2)):
    assert normalized_p(matrix(*c1,x),matrix(*c2,x)) == x/Q(256)-x*x/Q(64)

print(json.dumps({
 'status':'PASS',
 'arithmetic':'exact Fraction; integer-only rational Gaussian elimination',
 'two_edit_grid_nodes_checked':9,
 'two_edit_cross_product':'1/4',
 'bordered_determinant_identity_nodes_checked':9,
 'two_coordinate_quadratic_coefficient_sites':coefficient_checks,
 'quadratic_certificate_values_all_zero':True,
 'independent_second_finite_difference_matches':coefficient_checks+1,
 'nonzero_control_coefficient_x2':'-1/64',
 'nonzero_control_grid_nodes_checked':4,
 'proof_scope':'two finite explicit examples only; global certificate theorem is algebraic'
},ensure_ascii=False,indent=2))
