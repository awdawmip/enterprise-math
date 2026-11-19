"""Exact finite checks for marked polarizations on the frozen Gaussian lattice."""
from fractions import Fraction as Q
from functools import lru_cache
from math import gcd, isqrt
import json


def vp(n, p):
    j = 0
    while n % p == 0:
        n //= p
        j += 1
    return j


def least_scale(h):
    return 2 ** max(0, vp(h, 2) - 1) * 3 ** max(0, vp(h, 3) - 1)


@lru_cache(None)
def sum_square_residues(m):
    # Cyclic convolution of supports by shifts of an integer bitset.
    squares = {a * a % m for a in range(m)}
    bits = sum(1 << a for a in squares)
    mask = (1 << m) - 1
    all_sums = 0
    for a in squares:
        all_sums |= ((bits << a) & mask) | (bits >> (m - a))
    return all_sums


def local_factor(p, b):
    if b == 0:
        return Q(1)
    if p == 2:
        return Q(1, 2 * 2 ** (6 * (b - 1)))
    if p == 3:
        return Q(41, 365 * 3 ** (6 * (b - 1)))
    if p % 4 == 1:
        return Q(1, p**b)
    w = (1 + Q(1, p)) * (1 + Q(1, p**5)) / (1 + Q(1, p**6))
    return Q(1, p ** (6 * b)) + w * (Q(1, p**b) - Q(1, p ** (6 * b)))


def local_weight(p, b, j):
    if p in (2, 3) and j < b - 1:
        return Q(0)
    l = min(b, j + int(p == 3))
    z = ((j + l) % 2) if p % 4 == 3 else 0
    f = Q(1, p ** (5 * j + l + z))
    d = b - l
    if d:
        omit_p = 1 - Q(1, p**(2 if p % 4 == 3 else 1))
        f *= omit_p / ((p - 1) * p ** (d - 1))
    return f


def local_sum(p, b):
    # At j>=b the next two valuations always scale by p^-10.
    return (sum(local_weight(p, b, j) for j in range(b))
            + (local_weight(p, b, b) + local_weight(p, b, b + 1))
            / (1 - Q(1, p**10)))


def integral_test(v):
    signs = (1, 1, 1, -1, -1, -3)
    s = sum(h * (x*x + y*y) for h, (x, y) in zip(signs, v))
    assert s
    b = [(h*x, h*y) for h, (x, y) in zip(signs, v)]
    # Each chosen vector is primitive; at the only possible Gaussian
    # divisor, the rational prime 3 is inert.
    delta = 3 if all(x % 3 == y % 3 == 0 for x, y in b) else 1
    h = 3 * abs(s) // (delta * delta)
    triples = []
    for i, (x, y) in enumerate(b):
        for j, (z, w) in enumerate(b):
            triples.append((s * signs[i] if i == j else 0, x*z+y*w, y*z-x*w))
    total = good = 0
    for d in (1, 2, 3, 4, 5, 6, 9):
        for a in range(1, 2*d+4):
            for c in range(1, 2*d+4):
                # line multiplier a/d, orthogonal-complement multiplier c/d.
                denom = abs(d * s)
                matrix_accepts = all((c * base + (a-c)*real) % denom == 0
                                     and (a-c)*imag % denom == 0
                                     for base, real, imag in triples)
                criterion = c % d == 0 and (3*a) % d == 0 and (3*(a-c)) % (d*h) == 0
                assert criterion == matrix_accepts
                total += 1
                good += matrix_accepts
    return dict(s=s, delta=delta, h=h, matrix_tests=total, integral=good)


def square_norms(bound):
    flags = bytearray(bound + 1)
    for x in range(isqrt(bound) + 1):
        xsq = x*x
        for y in range(x, isqrt(bound - xsq) + 1):
            flags[xsq + y*y] = 1
    return flags


def count_pairs(h, bound, norms):
    by_scale = {}
    n = 1
    while n**5 <= bound:
        stop = bound // n**5
        first = (3*n - 1) % h + 1
        count = sum(norms[n*r] for r in range(first, stop + 1, h))
        if count:
            assert n % least_scale(h) == 0
            by_scale[n] = count
        n += 1
    return by_scale


def main():
    local_tests = 0
    for h in range(1, 65):
        for n in range(1, 49):
            m = h*n
            contains = (sum_square_residues(m) >> (3*n*n % m)) & 1
            assert bool(contains) == (n % least_scale(h) == 0)
            local_tests += 1

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    factor_tests = 0
    for p in primes:
        for b in range(7):
            assert local_sum(p, b) / local_sum(p, 0) == local_factor(p, b)
            j0 = b-1 if p in (2, 3) and b > 0 else 0
            a = local_weight(p, b, j0) / local_sum(p, b)
            lower = ((1-Q(1, 3**10)) / (1+Q(1, 3**4)) if p == 3
                     else 1-Q(1, p**5))
            assert a >= lower
            factor_tests += 1

    vectors = [
        [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(0,0),(0,0),(1,0)],
        [(3,0),(0,0),(0,0),(0,0),(0,0),(1,1)],
        [(3,0),(0,0),(0,0),(0,0),(0,0),(1,2)],
        [(1,0),(3,2),(0,0),(2,1),(0,0),(1,0)],
        [(1,0),(4,1),(1,1),(1,3),(0,0),(0,0)],
        [(3,0),(3,3),(0,0),(0,3),(3,0),(2,1)],
    ]
    bound = 1000000
    ns = square_norms(bound)
    counts = {}
    for h in [1, 2, 3, 4, 5, 6, 7, 9, 12, 21, 33, 35, 49]:
        table = count_pairs(h, bound, ns)
        j0 = least_scale(h)
        small = count_pairs(h//j0, bound//j0**6, ns)
        assert table == {n*j0: c for n, c in small.items()}
        counts[h] = dict(total=sum(table.values()), by_complement=table)
    # Independent relation for the two standard axes: on e1 the split
    # forms are exactly (x,n) positive integral with 3*x*n a norm;
    # on e6 they are all (r,n) with r*n a norm.
    for h, rstep in [(1, 1), (3, 3)]:
        total = 0
        for n in range(1, 17):
            if n**5 > bound:
                break
            total += sum(ns[rstep*x*n] for x in range(1, bound//(rstep*n**5)+1))
        assert total == counts[h]['total']
    print(json.dumps(dict(square_congruences=local_tests,
                          rational_euler_factor_tests=factor_tests,
                          integral_matrix_tests=[integral_test(v) for v in vectors],
                          local_C_over_C1={p: [str(local_factor(p,b)) for b in (1,2)]
                                           for p in [2,3,5,7,11]},
                          chi_cutoff=bound, marked_form_counts=counts),
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
