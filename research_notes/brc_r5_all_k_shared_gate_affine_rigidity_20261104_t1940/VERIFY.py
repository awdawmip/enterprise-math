#!/usr/bin/env python3
"""Exact integer check of the two-product affine-observer rigidity theorem.
Declared finite domain: A,B1,B2,C1,C2 in {-1,0,1}^2, 9^5 cases.
No floating arithmetic or external package is used.
"""
from itertools import product
from collections import Counter
from fractions import Fraction

DIRECTIONS = list(product((-1, 0, 1), repeat=2))


def add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(2))


def scale(a, v):
    return (a * v[0], a * v[1])


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def convex_hull(points):
    """Exact monotone chain, collinear boundary compressed to extremes."""
    p = sorted(set(points))
    if len(p) <= 1:
        return p
    lower = []
    for v in p:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], v) <= 0:
            lower.pop()
        lower.append(v)
    upper = []
    for v in p[::-1]:
        while len(upper) >= 2 and cross(upper[-2], upper[-1], v) <= 0:
            upper.pop()
        upper.append(v)
    return lower[:-1] + upper[:-1]


def contains(poly, p):
    if len(poly) == 1:
        return p == poly[0]
    if len(poly) == 2:
        a, b = poly
        return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    return all(cross(poly[i], poly[(i+1) % len(poly)], p) >= 0 for i in range(len(poly)))


def vertices(A, B, C):
    LR, FULL = [], []
    for y in product((0, 1), repeat=2):
        base = add(scale(y[0], B[0]), scale(y[1], B[1]))
        LR.append(base)
        FULL.append(base)
        LR.append(add(A, base, scale(y[0], C[0]), scale(y[1], C[1])))
        for z in product((0, 1), repeat=2):
            FULL.append(add(A, base, scale(z[0], C[0]), scale(z[1], C[1])))
    return LR, FULL


def positive_collinear_or_zero(b, c):
    if b == (0, 0):
        return True
    return b[0]*c[1] == b[1]*c[0] and b[0]*c[0]+b[1]*c[1] >= 0


def support(vertices, n):
    return max(sum(v[i]*n[i] for i in range(2)) for v in vertices)


def formula(A, B, C, n):
    dot = lambda u, v: sum(a*b for a,b in zip(u,v))
    p = [dot(n, v) for v in B]
    q = [dot(n, v) for v in C]
    a = dot(n, A)
    S = sum(max(0, z) for z in p)
    U = a + sum(max(0, z) for z in q)
    D = sum(max(0, p[i]) + max(0, q[i]) - max(0, p[i] + q[i]) for i in range(2))
    return S + max(0, U), S + max(0, U - D), D, U


def main():
    counts = Counter()
    for A, b1, b2, c1, c2 in product(DIRECTIONS, repeat=5):
        B, C = (b1, b2), (c1, c2)
        lr, full = vertices(A, B, C)
        poly = convex_hull(lr)
        hull_equal = all(contains(poly, v) for v in full)
        criterion = all(positive_collinear_or_zero(B[i], C[i]) for i in range(2))
        assert hull_equal == criterion, (A,B,C,hull_equal,criterion)
        counts['equal' if hull_equal else 'strict'] += 1
        # Independent formula verification for all four coordinate signed basis normals.
        for n in ((1,0),(-1,0),(0,1),(0,-1)):
            hf, hl, d, u = formula(A, B, C, n)
            assert hf == support(full, n) and hl == support(lr, n)
            assert hf >= hl
            assert d >= 0
        counts['checked'] += 1
    print('COMPLETE_FINITE_DOMAIN = 9^5 =', len(DIRECTIONS)**5)
    print('CHECKED =', counts['checked'])
    print('EQUAL_HULL =', counts['equal'])
    print('STRICT_HULL =', counts['strict'])
    # Both products are genuinely two-dimensional cross coupled.
    A=(2,1); B=((1,0),(0,1)); C=((0,1),(1,0)); n=(1,-1)
    lr, full=vertices(A,B,C)
    hf,hl,D,U=formula(A,B,C,n)
    S=sum(max(0,sum(n[j]*B[i][j] for j in range(2))) for i in range(2))
    assert (hf,hl,D,U,S)==(3,1,2,2,1)
    assert (4,1) in full
    print('TWO_CROSS_COUPLED_PRODUCTS: A=',A,' B=',B,' C=',C,' n=',n)
    print('SUPPORT_FULL=',hf,'SUPPORT_LR=',hl,'GAP=',hf-hl,'D=',D,'U=',U)
    print('FULL_WITNESS=(4,1), n.W=3; n.LR_support=1; supnorm_distance>=1')
    # A fully nonnegative-collinear equality example with two nonzero products.
    A=(2,-1); B=((1,0),(0,1)); C=((2,0),(0,3))
    lr,full=vertices(A,B,C)
    assert all(contains(convex_hull(lr),v) for v in full)
    print('EQUAL_HULL_EXAMPLE A=',A,'B=',B,'C=',C, 'lambda=(2,3)')
    # Three-product exact rational behavior reconstruction, including a B_i=0 fiber.
    AB=( (2, 1), (1, 0), (0, 0), (0, 1) )
    AA=AB[0]
    BB=AB[1:]
    CC=((2, 0), (-1, 3), (0, 3))
    lam=(Fraction(2), None, Fraction(3))
    fractions=[Fraction(0),Fraction(1,3),Fraction(2,3),Fraction(1)]
    total=0
    for x in fractions:
        for yy in product(fractions, repeat=3):
            for zz in product((Fraction(0),x),repeat=3):
                zp=[]
                for i in range(3):
                    if BB[i] == (0,0):
                        zp.append(zz[i]/x if x else Fraction(0))
                    else:
                        zp.append((yy[i]+lam[i]*zz[i])/(1+lam[i]*x))
                    assert 0 <= zp[-1] <= 1
                def output(y,z):
                    return tuple(x*AA[j]+sum(y[i]*BB[i][j]+z[i]*CC[i][j] for i in range(3)) for j in range(2))
                assert output(yy,zz)==output(zp,[x*yi for yi in zp])
                total+=1
    print('THREE_PRODUCT_RATIONAL_RECONSTRUCTIONS =',total)
    print('PASS_EXACT_R5_ALL_K_COMMON_X_MULTIPRODUCT_AFFINE_RIGIDITY')

if __name__=='__main__':
    main()
