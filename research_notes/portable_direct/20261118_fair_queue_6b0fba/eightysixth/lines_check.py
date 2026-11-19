"""Exact checks for the degree-two blocks, in the frozen six coefficient coordinates."""
import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path


def multiply(a, b):
    """Elements of Z[s], s^3=-s^2+2s+1."""
    tmp = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            tmp[i+j] += x*y
    for d in (4, 3):
        tmp[d-3] += tmp[d]
        tmp[d-2] += 2*tmp[d]
        tmp[d-1] -= tmp[d]
    return tuple(tmp[:3])


ONE = (1, 0, 0)
ZERO = (0, 0, 0)
S = (0, 1, 0)
U = (-2, 0, 1)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def neg(x):
    return tuple(-i for i in x)


def scale(t, x):
    return tuple(t*i for i in x)


def field_norm(a):
    b = multiply(a, S)
    c = multiply(b, S)
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - b[0]*(a[1]*c[2]-a[2]*c[1])
            + c[0]*(a[1]*b[2]-a[2]*b[1]))


def adj(a):
    trace = 3*a[0]-a[1]+5*a[2]
    square = multiply(a, a)
    trace_sq = 3*square[0]-square[1]+5*square[2]
    assert (trace*trace-trace_sq) % 2 == 0
    return add(add(square, neg(scale(trace, a))), scale((trace*trace-trace_sq)//2, ONE))


def powers_unit(a, max_power):
    assert field_norm(a) == 1
    p = {0: ONE}
    for j in range(1, max_power+1):
        p[j] = multiply(p[j-1], a)
        p[-j] = multiply(p[1-j], adj(a))
    return p


def unit_check():
    gens = [powers_unit(t, 5) for t in (S, U)]
    elements = {scale(sign, multiply(v, w)): (i, j)
                for i, v in gens[0].items() for j, w in gens[1].items()
                for sign in (-1, 1)}
    seen = Counter()
    for a, b, c in itertools.product(range(-3, 4), range(-2, 3), range(-2, 3)):
        elt = a, b, c
        sq = multiply(elt, elt)
        trace = 3*sq[0]-sq[1]+5*sq[2]
        if trace <= 15 and abs(field_norm(elt)) == 1:
            assert elt in elements
            seen[trace] += 1
    return dict(sorted(seen.items()))


def det(a):
    m = [list(row) for row in a]
    sign = 1
    previous = 1
    for j in range(len(m)-1):
        k = next(i for i in range(j, len(m)) if m[i][j])
        if j != k:
            m[j], m[k] = m[k], m[j]
            sign = -sign
        pivot = m[j][j]
        for i in range(j+1, len(m)):
            for l in range(j+1, len(m)):
                numerator = pivot*m[i][l]-m[i][j]*m[j][l]
                assert numerator % previous == 0
                m[i][l] = numerator//previous
        previous = pivot
    return sign*m[-1][-1]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matprod(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def matrix_power(a, e):
    r = ident(len(a))
    for _ in range(e):
        r = matprod(r, a)
    return r


def sumat(*matrices):
    return [[sum(items) for items in zip(*rows)] for rows in zip(*matrices)]


def norm_label(pair):
    a, b = pair
    if b == ZERO:
        return ()
    numer = multiply(a, adj(b))
    den = field_norm(b)
    common = gcd(abs(den), *numer)
    if den < 0:
        common = -common
    return tuple(x//common for x in (den, *numer))


def pair_powers():
    result = [(ONE, ZERO)]
    for _ in range(5):
        a, b = result[-1]
        result.append((neg(b), add(a, multiply(S, b))))
    return result


PAIR = pair_powers()


def relative_pair(v):
    return tuple(tuple(sum(v[i]*PAIR[i][k][j] for i in range(6)) for j in range(3))
                 for k in (0, 1))


def reduced_pair(v, root, p):
    # Evaluate the six original coefficients directly modulo z^2-root*z+1.
    a = b = 0
    for t in reversed(v):
        a, b = (t-b) % p, (a+root*b) % p
    assert a or b
    return -1 if b == 0 else a*pow(b, -1, p) % p


def isprime(p):
    return p >= 2 and all(p % j for j in range(2, isqrt(p)+1))


def trace_poly(i, t):
    a, b = 2, t
    for _ in range(i):
        a, b = b, t*b-a
    return a


def inspect_block(n, p, conjugate, depth, operators, root):
    assert (root**3+root**2-2*root-1) % p == 0
    assert pow((root*root-4) % p, (p-1)//2, p) == p-1
    shifts = [sumat([[n*z for z in row] for row in ident(6)], t) for t in operators]
    forward = matrix_power(shifts[conjugate], depth)
    other = [M for i, M in enumerate(shifts) if i != conjugate]
    inverse_scaled = matrix_power(matprod(*other), depth)
    assert matprod(forward, inverse_scaled) == [[p**depth*z for z in row] for row in ident(6)]
    # If x=g^r v is short, p^r v_i = row_i(inverse_scaled) dot x.
    bounds = []
    for row in inverse_scaled:
        height_squared = sum(z*z for z in row)
        b = 0
        while 42**3*(b+1)**6*p**(4*depth) < height_squared**3*p:
            b += 1
        bounds.append(b)
    g2 = matprod(list(zip(*forward)), forward)
    ratio_labels, field_labels = {}, Counter()
    npoints = 0
    for v in itertools.product(*(range(-b,b+1) for b in bounds)):
        if next((i for i in v if i), 0) <= 0:  # one representative per sign
            continue
        q = sum(g2[i][i]*v[i]**2+2*sum(g2[i][j]*v[i]*v[j] for j in range(i))
                for i in range(6))
        if 42**3*q**3 >= p**(2*depth+1):
            continue
        tag = norm_label(relative_pair(v))
        local = reduced_pair(v, root, p)
        assert ratio_labels.setdefault(tag, local) == local
        field_labels[tag] += 1
        npoints += 1
    assert len(set(ratio_labels.values())) == len(ratio_labels)
    # The dual projective line has p finite slopes plus one pole.
    assert len(ratio_labels) <= p+1
    return dict(prime=p, level=depth, conjugate=conjugate+1, trace_root=root,
                coefficient_box=bounds, nonzero_pairs_mod_sign=npoints, bad_seeds=len(ratio_labels),
                denominator=p+1, line_fiber_histogram=dict(sorted(Counter(field_labels.values()).items())))


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('--out', type=Path)
    args = parse.parse_args()
    ident6 = ident(6)
    shift = [[int(i == j+1) if j < 5 else -1 for j in range(6)] for i in range(6)]
    assert matrix_power(shift, 7) == ident6
    operators = [sumat(matrix_power(shift,i), matrix_power(shift,7-i)) for i in (1,2,3)]
    S0 = operators[0]
    determinant = det(sumat(ident6, matprod(list(zip(*S0)), S0)))
    assert determinant == 377
    # Bernoulli values weight pairs (1,6),(2,5),(3,4), with chi(3)=omega.
    chi = Fraction((37-29)**2-(37-29)*(25-29)+(25-29)**2,49)
    assert chi == Fraction(16,7)
    zeta_over_pi6 = chi*Fraction(1, 6*7**3)
    assert zeta_over_pi6 == Fraction(8,7203)
    rows = []
    for n, levels in ((43,(0,1,7,16)), (85,(0,1,3)), (129,(0,1,3)), (220,(0,1,3))):
        p = n**3-n*n-2*n+1
        assert p % 7 == 6 and isprime(p)
        for depth in levels:
            for i, inv in enumerate((1,3,2)):
                root = trace_poly(inv,-n) % p
                rows.append(inspect_block(n,p,i,depth,operators,root))
    first = next(p for p in range(42**3+1, 42**3+200) if p%7==6 and isprime(p))
    assert all(not isprime(p) for p in range(42**3+1, first) if p%7 == 6)
    roots = [t for t in range(first) if (t**3+t*t-2*t-1) % first == 0]
    assert len(roots) == 3 and 42**3 < first <= 8*42**3
    first_hits = [len({reduced_pair(v,t,first) for v in ident6}) for t in roots]
    assert first_hits == [6,6,6]
    assert 13 < 42**3
    out = dict(unit_ball_trace_histogram=unit_check(), ellipsoid_determinant=determinant,
               zeta_F_2_over_pi6=str(zeta_over_pi6),
               first_nonempty_base_prime=first, first_trace_roots=roots, first_bad_seeds=first_hits,
               locked_p13_base=dict(all_seeds=14,bad=0), blocks=rows)
    data = json.dumps(out, indent=2, sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(data)
    else:
        print(data, end='')


if __name__ == '__main__':
    main()
