"""Integral Gaussian matrices and independent small-modulus minimization."""
import json
from fractions import Fraction
from functools import cache, lru_cache
from itertools import product
from math import gcd, isqrt

DIAGONAL = (1, 1, 1, -1, -1, -3)


def positive_line(M):
    m, odd = divmod(M, 2)
    return [(1, 0), (m, 0), (odd, 0), (m-1, 0), (0, 0), (0, 0)]


def negative_line(h):
    x, y = 1, 0
    for _ in range(h):
        x, y = x-y, x+y
    return [(3, 0), (0, 0), (0, 0), (3, 0), (0, 0), (x, y)]


def gram_data(u):
    b = [(c*x, c*y) for c, (x, y) in zip(DIAGONAL, u)]
    n = sum(c*(x*x+y*y) for c, (x, y) in zip(DIAGONAL, u))
    entries = []
    for i, (x, y) in enumerate(b):
        for j, (X, Y) in enumerate(b):
            entries.append((DIAGONAL[i] if i == j else 0, x*X+y*Y, y*X-x*Y))
    content = gcd(*(integer for _, real, imag in entries for integer in (real, imag)))
    assert content in (1, 9)
    return n, isqrt(content), entries


def direct_integrality(n, entries, x, y):
    # x and y have positive rational denominators. Test the 36 complex entries.
    p, q, r, s = x.numerator, x.denominator, y.numerator, y.denominator
    factor = p*s-r*q
    denominator = n*s*q
    return all((r*n*q*d+factor*real) % denominator == 0
               and factor*imag % denominator == 0 for d, real, imag in entries)


@lru_cache(maxsize=20000)
def norm_integer(z):
    """Trial division using the two-squares theorem for positive integers."""
    m = z
    while m % 2 == 0:
        m //= 2
    p = 3
    while p*p <= m:
        exponent = 0
        while m % p == 0:
            exponent += 1
            m //= p
        if p % 4 == 3 and exponent % 2:
            return False
        p += 2
    return m % 4 == 1


@cache
def pair_residues(m):
    squares = {x*x % m for x in range(m)}
    return {(x+y) % m for x in squares for y in squares}


def residue_possible(start, step):
    for p in (2, 3):
        m = 1
        while m*p <= 729 and step % (m*p) == 0:
            m *= p
        if start % m not in pair_residues(m):
            return False
    return True


def minimum(t, a):
    # Enumerate B and admissible positive A in increasing order; get a finite
    # bound from (3a,a) at t=1 and (a,a) at t=3, both split and integral.
    c = 3//t
    best = (c*c*a**6, c*a, a)
    B = 1
    while c*B**5 <= best[0]:
        first = (t*B-1) % a+1
        if not residue_possible(c*first*B, c*a*B):
            B += 1
            continue
        for A in range(first, best[0]//(c*B**5)+1, a):
            if norm_integer(c*A*B):
                best = min(best, (c*A*B**5, A, B))
                break
        B += 1
    return best


def local_scale(a):
    s = 1
    while a % 4 == 0:
        a //= 2
        s *= 2
    while a % 3 == 0:
        a //= 3
        s *= 3
    return s, a


def run():
    lines = [positive_line(M) for M in range(1, 33)] + [negative_line(h) for h in range(11)]
    # Nonreal first-five coordinates and a nonreal last coordinate.
    lines += [[(1, 1), (1, 0), (2, -1), (u, 1), (0, 1), (v, -1)]
              for u, v in product(range(4), range(3))]
    values = sorted({Fraction(j, k) for k in (1, 2, 3, 4, 5, 6) for j in range(1, 25)})
    tests = accepts = 0
    for u in lines:
        n, t, matrix = gram_data(u)
        if n == 0:
            continue
        a = abs(n)//t
        for x, y in product(values, repeat=2):
            expected = (y.denominator == (t*x).denominator == 1
                        and (t*x-t*y) % a == 0)
            assert direct_integrality(n, matrix, x, y) == expected
            tests += 1
            accepts += expected
    norms = {r*r+s*s for r in range(101) for s in range(101)}
    assert all(norm_integer(v) == (v in norms) for v in range(1,10001))
    rows = []
    for t, moduli in ((1, range(1, 27)), (3, [v for v in range(1, 36) if v % 3])):
        for a in moduli:
            s, reduced = local_scale(a)
            chi, A, B = minimum(t, a)
            base = minimum(t, reduced)
            assert chi == s**6*base[0] and A % s == B % s == 0
            if reduced <= 2:
                assert chi == (9 if t == 1 else 1)*s**6
            if t == 1:
                assert 3*(a+1) <= chi <= 9*a**6
                assert (chi == 3*(a+1)) == norm_integer(3*(a+1))
            if t == 3 and a >= 4:
                assert chi >= a+3 and (chi == a+3) == norm_integer(a+3)
            rows.append([t, a, s, reduced, A, B, chi, chi*chi])
    pure = []
    for k in range(9):
        M = 3**k
        n, t, matrix = gram_data(positive_line(M))
        assert n == M and t == 1 and direct_integrality(n, matrix, Fraction(3*M), Fraction(M))
        pure.append([M,9*M**6])
    same_norm = []
    for h in range(11):
        n, t, matrix = gram_data(negative_line(h))
        assert n == -3*2**h and t == 3
        s, _ = local_scale(abs(n)//t)
        assert direct_integrality(n, matrix, Fraction(s,3), Fraction(s))
        n1, t1, duplicate = gram_data(positive_line(n))
        assert n1 == n and t1 == 1
        assert direct_integrality(n1, duplicate, Fraction(9*s), Fraction(3*s))
        ratio = 9*(3*s)**6//(s**6)
        assert ratio == 6561
        same_norm.append([n, 9*(3*s)**6, s**6])
    for a in range(1, 100):
        if a % 3:
            z = (1, 0 if a % 3 == 1 else 1)
            m = (sum(c*c for c in z)-a)//3
            line = [(3*x, 3*y) for x,y in positive_line(m)[:5]]+[z]
            assert gram_data(line)[:2] == (-3*a, 3)
    return dict(
        entries=DIAGONAL, rational_block_pairs_checked=tests,
        integral_cases=accepts, independent_sum_of_two_squares_checks=10000,
        minima_columns=['type', 'modulus', 'scale', 'reduced', 'A', 'B', 'chi', 'degree'],
        minima=rows, same_signed_norm_and_two_minima=same_norm, optimal_uniform_upper_bound_witnesses_M_and_chi=pure,
        primitive_content_three_examples_exponents=list(range(11)))


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
