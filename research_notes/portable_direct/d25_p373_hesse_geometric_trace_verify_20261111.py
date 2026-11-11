#!/usr/bin/env python3
"""D25 author-side p=373 original Hesse CM-24 geometric q-Frobenius certificate.
Finite-field curve point counts, NOT a native divided-power H0/B0 [X]U computation.
Requires Python standard library only; all arithmetic is exact in F_373[T]/(T^2-2).
"""
from collections import Counter
import json

p = 373
q = p * p
O = (0, 0)
I = (1, 0)
T = (0, 1)

def add(x, y):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

def sub(x, y):
    return ((x[0] - y[0]) % p, (x[1] - y[1]) % p)

def scale(x, c):
    return (x[0] * c % p, x[1] * c % p)

def mul(x, y):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)

def norm(x):
    return (x[0] * x[0] - 2 * x[1] * x[1]) % p

def inv(x):
    k = pow(norm(x), -1, p)
    return (x[0] * k % p, -x[1] * k % p)

def power(x, n):
    assert n >= 0
    v = I
    while n:
        if n & 1:
            v = mul(v, x)
        x = mul(x, x)
        n >>= 1
    return v

def quadratic_character(x):
    # For F_{p^2}, chi_q(x) = chi_p(Norm(x)).
    a = norm(x)
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def pack(x):
    return x[0] + p * x[1]

def hesse_as_cubic(lam):
    # [U:V:W]=[Z:X-Y:X+Y+lambda*Z] gives y^2=f(x) on W=1.
    lam3 = power(lam, 3)
    inv3 = pow(3, -1, p)
    return (scale(sub(lam3, I), 4 * inv3),
            scale(power(lam, 2), -3),
            scale(lam, 2),
            (-inv3 % p, 0))

def polynomial(coeffs, x):
    a3, a2, a1, a0 = coeffs
    return add(mul(add(mul(add(mul(a3, x), a2), x), a1), x), a0)

def enumerate_points(coeffs, twist, square_multiplicities):
    # Two independent square tests: Legendre(Norm(y)) and enumerated y^2 fibers.
    hist = {-1: 0, 0: 0, 1: 0}
    n_by_square_list = 1  # unique point at infinity
    for x0 in range(p):
        for x1 in range(p):
            rhs = polynomial(coeffs, (x0, x1))
            if twist is not None:
                rhs = mul(twist, rhs)
            hist[quadratic_character(rhs)] += 1
            n_by_square_list += square_multiplicities[pack(rhs)]
    s = hist[1] - hist[-1]
    n_by_character = q + 1 + s
    assert n_by_square_list == n_by_character
    return n_by_character, hist


def main():
    assert pow(2, (p - 1) // 2, p) == p - 1
    # Original frozen Hesse parameter u=(2-T)/4, with lambda^(-3)=u.
    u = scale((2, -1), pow(4, -1, p))
    m = (q - 1) // 3
    assert m % 3 != 0 and power(u, m) == I
    lam = inv(power(u, pow(3, -1, m)))
    assert mul(power(lam, 3), u) == I
    assert lam == (56, 19)
    lam_conj = (lam[0], -lam[1] % p)
    assert power(lam, 3) == (4, 2)
    coeffs = hesse_as_cubic(lam)
    assert coeffs == ((4, 127), (362, 330), (112, 38), (124, 0))
    # Hesse j=27*lambda^3*(lambda^3+8)^3/(lambda^3-1)^3.
    lam3 = power(lam, 3)
    j = scale(mul(lam3, mul(power(add(lam3, (8, 0)), 3),
                              inv(power(sub(lam3, I), 3)))), 27)
    assert j == (2417472 % p, -1707264 % p) == (59, 330)
    hilbert = add(sub(mul(j, j), scale(j, 4834944)), (14670139392 % p, 0))
    assert hilbert == O
    assert lam3 != I
    # Exact projective change: a known original Hesse point [1:0:-1].
    X, Y, Z = I, O, (p - 1, 0)
    U, V, W = Z, sub(X, Y), add(add(X, Y), mul(lam, Z))
    x, y = mul(U, inv(W)), mul(V, inv(W))
    assert x == (173, 103) and y == (200, 270)
    assert mul(y, y) == polynomial(coeffs, x)
    # Full independent quadratic-residue occupancy table y -> y^2.
    squares = [0] * q
    for y0 in range(p):
        for y1 in range(p):
            squares[pack(((y0 * y0 + 2 * y1 * y1) % p,
                          (2 * y0 * y1) % p))] += 1
    assert Counter(squares) == Counter({0: (q - 1)//2, 1: 1, 2: (q - 1)//2})
    n, histogram = enumerate_points(coeffs, None, squares)
    n_conj, hist_conj = enumerate_points(hesse_as_cubic(lam_conj), None, squares)
    assert n == n_conj == (p - 1)**2 == 138384
    assert histogram == hist_conj == {-1: 69936, 0: 3, 1: 69190}
    assert q + 1 - n == 2 * p
    # Multiplying cubic RHS by nonsquare T is the quadratic twist.
    assert quadratic_character(T) == -1
    n_twist, hist_twist = enumerate_points(coeffs, T, squares)
    assert n_twist == (p + 1)**2 == 139876
    assert hist_twist == {-1: 69190, 0: 3, 1: 69936}
    assert q + 1 - n_twist == -2 * p
    print(json.dumps({
        'classification': 'AUTHOR_SIDE_EXACT_FINITE_GEOMETRIC_TRACE_NOT_NATIVE_H0B0',
        'p': p, 'field': 'F_373[T]/(T^2-2)', 'q': q,
        'u': u, 'lambda': lam, 'lambda_conjugate': lam_conj,
        'j_lambda': j,
        'cubic_rhs_coefficients_desc': coeffs,
        'point_count_original_hesse': n,
        'trace_original_hesse_q_frobenius': q + 1 - n,
        'original_histogram': histogram,
        'point_count_conjugate': n_conj,
        'point_count_quadratic_twist_by_T': n_twist,
        'trace_quadratic_twist_q_frobenius': q + 1 - n_twist,
        'twist_histogram': hist_twist,
        'independent_algorithms': ['norm-legendre-character', 'enumerated-square-fiber'],
        'native_h0b0_xu_executed': False
    }, ensure_ascii=False, sort_keys=True))

if __name__ == '__main__':
    main()
