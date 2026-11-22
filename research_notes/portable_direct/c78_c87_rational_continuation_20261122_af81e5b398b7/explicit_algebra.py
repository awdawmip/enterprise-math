"""Exact polynomial circuits and degree-16 radical norm for the C78 spectrum.

Only arbitrary-precision integers and fractions.Fraction are used. Polynomials
are sparse maps (r exponent, s exponent) -> integer coefficient.
"""
from fractions import Fraction as Q
from math import comb, factorial, gcd
from functools import reduce


def clean(p):
    return {ij: a for ij, a in p.items() if a}


def add(*ps):
    out = {}
    for p in ps:
        for ij, a in p.items():
            out[ij] = out.get(ij, 0) + a
    return clean(out)


def scale(p, a):
    return clean({ij: a * b for ij, b in p.items()})


def mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            ij = i + k, j + l
            out[ij] = out.get(ij, 0) + a * b
    return clean(out)


def power(p, n):
    out = {(0, 0): 1}
    while n:
        if n & 1:
            out = mul(out, p)
        n >>= 1
        if n:
            p = mul(p, p)
    return out


def shift(p, i=0, j=0):
    return {(a+i, b+j): c for (a, b), c in p.items()}


def derivative(p, axis):
    out = {}
    for ij, a in p.items():
        e = ij[axis]
        if e:
            out[(ij[0]-(axis == 0), ij[1]-(axis == 1))] = a * e
    return out


def evaluate(p, r, s):
    r, s = Q(r), Q(s)
    return sum((Q(a) * r**i * s**j for (i, j), a in p.items()), Q(0))


def circuit():
    n = scale(shift(mul({(9, 0): 1, (0, 9): -4},
                        {(0, 0): 1, (15, 0): -4}), 6, 42), 50176)
    q = mul({(0, 0): 1, (51, 9): 448},
            {(0, 0): 1, (66, 9): 1792})
    nr, ns, qr, qs = (derivative(n, 0), derivative(n, 1),
                       derivative(q, 0), derivative(q, 1))
    a = add(mul(q, nr), scale(mul(n, qr), -1))
    b = add(mul(q, ns), scale(mul(n, qs), -1))
    c = add(shift(a, 1), shift(b, 0, 1))
    u = add(mul(q, derivative(c, 0)), scale(mul(c, qr), -2))
    v = add(mul(q, derivative(c, 1)), scale(mul(c, qs), -2))
    delta = add(mul(a, v), scale(mul(b, u), -1))
    hrr = add(shift(add(mul(q, derivative(a, 0)),
                        scale(mul(a, qr), -2)), 1), scale(mul(a, q), -3))
    hss = add(shift(add(mul(q, derivative(b, 1)),
                        scale(mul(b, qs), -2)), 0, 1), scale(mul(b, q), -3))
    mixed = add(mul(q, derivative(a, 1)), scale(mul(a, qs), -2))
    mixed_other = add(mul(q, derivative(b, 0)), scale(mul(b, qr), -2))
    assert mixed == mixed_other
    hessian = add(mul(hrr, hss), scale(shift(power(mixed, 2), 1, 1), -1))
    return {'N': n, 'Q': q, 'A': a, 'B': b, 'C': c, 'U': u, 'V': v,
            'Delta': delta, 'Hrr': hrr, 'Hss': hss, 'Mixed': mixed, 'Hessian': hessian}


def lowest_homogeneous_part(p):
    degree = min(i+j for i, j in p)
    return degree, {ij: a for ij, a in p.items() if sum(ij) == degree}


def primitive_part(p):
    """Divide out only an exact integer content, not any r or s factors."""
    content = reduce(gcd, (abs(a) for a in p.values()))
    return content, {ij: a // content for ij, a in p.items()}


def exact_division(p, q):
    """Exact integer-coefficient lexicographic division; None if it is not exact over Z."""
    remainder, quotient = dict(p), {}
    ij, c = max(q), q[max(q)]
    while remainder:
        kl, d = max(remainder), remainder[max(remainder)]
        if kl[0] < ij[0] or kl[1] < ij[1] or d % c:
            return None
        power_pair, coeff = (kl[0]-ij[0], kl[1]-ij[1]), d//c
        quotient[power_pair] = quotient.get(power_pair, 0) + coeff
        remainder = add(remainder, scale(shift(q, *power_pair), -coeff))
    assert mul(q, quotient) == p
    return quotient


def norm_matrix_polynomials(p):
    """16x16 multiplication matrix over Z[X,Y], basis r^i s^j, 0<=i,j<4.

    Entry polynomial exponent pairs now denote X and Y, not r and s.
    """
    out = [[{} for _ in range(16)] for _ in range(16)]
    for i in range(4):
        for j in range(4):
            col = 4*i+j
            for (a, b), c in p.items():
                u, v = (a+i) % 4, (b+j) % 4
                row = 4*u+v
                ij = (a+i)//4, (b+j)//4
                out[row][col][ij] = out[row][col].get(ij, 0) + c
    return [[clean(e) for e in row] for row in out]


def norm_matrix_at(p, x, y):
    return [[evaluate(e, x, y) for e in row] for row in norm_matrix_polynomials(p)]


def determinant(matrix):
    """Exact Gaussian determinant with nonzero pivot search."""
    a = [[Q(x) for x in row] for row in matrix]
    n, out = len(a), Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        value = a[j][j]
        out *= value
        for i in range(j+1, n):
            if not a[i][j]:
                continue
            ratio = a[i][j] / value
            for k in range(j+1, n):
                a[i][k] -= ratio * a[j][k]
            a[i][j] = Q(0)
    return out


def characteristic_coefficients(matrix):
    """Monic characteristic coefficients, descending powers, by exact traces."""
    a = [[Q(x) for x in row] for row in matrix]
    n = len(a)
    b = [[Q(i == j) for j in range(n)] for i in range(n)]
    coeffs = [Q(1)]
    for k in range(1, n+1):
        ab = [[sum((a[i][l]*b[l][j] for l in range(n)), Q(0))
               for j in range(n)] for i in range(n)]
        c = -sum((ab[i][i] for i in range(n)), Q(0))/k
        coeffs.append(c)
        for i in range(n):
            ab[i][i] += c
        b = ab
    assert all(value == 0 for row in b for value in row)
    return coeffs


def characteristic_bound(p):
    """On 0<=X,Y<=1, |a_j| <= choose(16,j)(16-j)! B^(16-j)."""
    b = sum(abs(a) for a in p.values())
    bounds = [comb(16, j)*factorial(16-j)*b**(16-j) for j in range(17)]
    return b, bounds, sum(bounds[1:])


def norm_leading_certificate(p):
    """Leading lexicographic norm monomial, proved by matrix degree bookkeeping."""
    a, b = max(p)
    coefficient = p[(a, b)]
    return {'r_degree': a, 'leading_r_coefficient_s_degree': b,
            'leading_r_s_coefficient': coefficient,
            'norm_x_degree': 4*a,
            'norm_leading_x_coefficient_y_degree': 4*b,
            'norm_leading_coefficient': coefficient**16,
            'grid_exponent_D': 4*(a+b)}


def polynomial_rows(p):
    return [[i, j, a] for (i, j), a in sorted(p.items())]


def fractions_pack(q):
    q = Q(q)
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}
