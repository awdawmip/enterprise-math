#!/usr/bin/env python3
"""Independent small-field exact check of GH-118/GH-119 CM group predictions.

The author-side theorem is a CM/endomorphism argument; these computations verify
selected finite fields using only the cubic group law in F_p[r]/(r^2-2).
"""
from math import gcd, isqrt


def add(a, b, p):
    return ((a[0] + b[0]) % p, (a[1] + b[1]) % p)


def neg(a, p):
    return ((-a[0]) % p, (-a[1]) % p)


def sub(a, b, p):
    return add(a, neg(b, p), p)


def mul(a, b, p):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % p,
            (a[0] * b[1] + a[1] * b[0]) % p)


def inv(a, p):
    norm = (a[0] * a[0] - 2 * a[1] * a[1]) % p
    assert norm != 0, (p, a)
    inverse = pow(norm, -1, p)
    return (a[0] * inverse % p, -a[1] * inverse % p)


def divide(a, b, p):
    return mul(a, inv(b, p), p)


def point_add(P, Q, p, B):
    # Infinity is None.  y^2 = x^3 + x^2 + B*x.
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u and add(y, v, p) == (0, 0):
        return None
    if x != u:
        slope = divide(sub(v, y, p), sub(u, x, p), p)
    else:
        numerator = add(add(mul((3, 0), mul(x, x, p), p),
                            mul((2, 0), x, p), p), B, p)
        slope = divide(numerator, mul((2, 0), y, p), p)
    x3 = sub(sub(mul(slope, slope, p), (1, 0), p), add(x, u, p), p)
    y3 = sub(mul(slope, sub(x, x3, p), p), y, p)
    return (x3, y3)


def scalar(P, n, p, B):
    result = None
    while n:
        if n & 1:
            result = point_add(result, P, p, B)
        n >>= 1
        if n:
            P = point_add(P, P, p, B)
    return result


def find_xy(p):
    for x in range(1, isqrt(p // 2) + 1):
        rem = p - 2 * x * x
        if rem > 0 and rem % 3 == 0:
            y = isqrt(rem // 3)
            if y > 0 and 3 * y * y == rem:
                return x, y
    raise ValueError(f"no 2*x^2+3*y^2 representation for p={p}")


def predicted(p):
    assert p >= 11 and p % 8 == 3
    if p % 24 == 19:
        return (p - 1) ** 2, p - 1, p - 1, None
    assert p % 24 == 11
    x, y = find_xy(p)
    A = 2 * x * x - 3 * y * y
    B = 2 * x * y
    n1 = gcd(abs(A + 1), B)
    n = (A + 1) ** 2 + 6 * B ** 2
    assert n == p * p + 1 + 4 * x * x - 6 * y * y
    assert n % n1 == 0 and (n // n1) % n1 == 0
    return n, n1, n // n1, (x, y)


def all_points(p):
    assert pow(2, (p - 1) // 2, p) == p - 1
    elements = [(a, b) for b in range(p) for a in range(p)]
    B = (pow(8, -1, p), pow(12, -1, p))
    root_map = {}
    for y in elements:
        root_map.setdefault(mul(y, y, p), []).append(y)
    points = [None]
    for x in elements:
        x2 = mul(x, x, p)
        f = add(add(mul(x2, x, p), x2, p), mul(B, x, p), p)
        points.extend((x, y) for y in root_map.get(f, ()))
    return points, B


def check(p):
    n, n1, n2, rep = predicted(p)
    points, B = all_points(p)
    assert len(points) == n, (p, len(points), n)
    assert n % 8 == 4
    # Direct group-law checks, not a repeat of the CM-formula derivation.
    exp_fail = sum(scalar(P, n2, p, B) is not None for P in points)
    n1_torsion = sum(scalar(P, n1, p, B) is None for P in points)
    four_torsion = sum(scalar(P, 4, p, B) is None for P in points)
    assert exp_fail == 0, (p, exp_fail)
    assert n1_torsion == n1 * n1, (p, n1_torsion, n1)
    assert four_torsion == 4, (p, four_torsion)
    return dict(p=p, representation=rep, order=n, n1=n1,
                n2=n2, n1_torsion=n1_torsion, four_torsion=four_torsion)


if __name__ == '__main__':
    for p in (11, 19, 43, 59, 83):
        print('PASS', check(p))
    n, n1, n2, rep = predicted(3347)
    assert (n, n1, n2, rep) == (11208516, 2, 5604258, (40, 7))
    print('PASS_P3347_CM_GROUP_FORMULA', dict(p=3347, order=n, n1=n1,
                                             n2=n2, representation=rep))
    print('PASS_GH118_GH119_CM_GROUPS')
