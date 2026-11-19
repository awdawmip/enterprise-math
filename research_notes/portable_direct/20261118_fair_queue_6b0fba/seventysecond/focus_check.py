"""Integer certificates for oriented port matchings. Uses only the Python standard library."""
from collections import Counter
from itertools import combinations, permutations, product
from math import factorial, gcd, prod
import json


def parity(p):
    return sum(a > b for i, a in enumerate(p) for b in p[i + 1:]) % 2


def dot_matching(u, v, p):
    return sum(u[i] * v[j] for i, j in enumerate(p))


def spread(values):
    return gcd(*(value - values[0] for value in values))


def gf4_product(a, b):
    poly = (a if b & 1 else 0) ^ ((a << 1) if b & 2 else 0)
    return poly ^ (7 if poly & 4 else 0)


def checksum(p):
    result = 0
    for x, y in enumerate(p):
        result ^= gf4_product(x, y)
    return result


def determinant(rows):
    """Fraction-free Gaussian elimination."""
    a = [row[:] for row in rows]
    n = len(a)
    sign, previous = 1, 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if k != pivot:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        d = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = a[i][j] * d - a[i][k] * a[k][j]
                assert v % previous == 0
                a[i][j] = v // previous
        previous = d
    return sign * a[-1][-1]


def four_ports():
    perms = list(permutations(range(4)))
    permitted = [p for p in perms if not parity(p)]
    counts = Counter(map(checksum, perms))
    assert all((checksum(p) != 0) == bool(parity(p)) for p in perms)
    choices = ['0231', '0312', '1032', '1203', '1320', '2013', '2130', '2301', '3021']
    rows = []
    for s in choices:
        p = tuple(map(int, s))
        assert p in permitted
        rows.append([int(p[i] == j) - int(i == j) for i in range(3) for j in range(3)])
    assert determinant(rows) == 4
    for v in product(range(2), repeat=4):
        orbit = lambda group: {tuple(v[j] for j in p) for p in group}
        assert orbit(permitted) == orbit(perms)
    return dict(minor_rows=choices, determinant=4, checksum_histogram=dict(sorted(counts.items())))


def eisenstein_spread(u, v):
    x, y = u[0] - u[2], u[1] - u[2]
    z, t = v[0] - v[2], v[1] - v[2]
    # conjugate(x+y*w) * (z+t*w), with w*w=-w-1.
    return gcd((x - y) * z + y * t, x * t - y * z)


def three_ports():
    evens = [p for p in permutations(range(3)) if not parity(p)]
    trials = 0
    for x, y, z, t in product(range(-5, 6), repeat=4):
        u, v = (x, y, 0), (z, t, 0)
        actual = spread([dot_matching(u, v, p) for p in evens])
        assert actual == eisenstein_spread(u, v)
        trials += 1
    norms = {}
    for n in (1, 3, 7, 13, 21, 49, 91, 147):
        a, b = next((x, y) for x in range(n + 1) for y in range(x + 1)
                    if gcd(x, y) == 1 and x*x - x*y + y*y == n)
        u = (a, b, 0)
        full = [dot_matching(u, u, p) for p in permutations(range(3))]
        oriented = [dot_matching(u, u, p) for p in evens]
        assert spread(full) == 1 and spread(oriented) == n
        norms[n] = dict(primitive=[a, b], even_values=oriented)
    return dict(exact_integer_trials=trials, norm_witnesses=norms)


def rectangle_check(n):
    basis = []
    for a in range(1, n):
        for out in range(1, n):
            c = 0
            b = next(i for i in range(n) if i not in (a, c))
            u, v = out, 0
            w, db, dc = [i for i in range(n) if i not in (u, v)][:3]
            p = next(p for p in permutations(range(n)) if not parity(p)
                     and (p[a], p[b], p[c]) == (u, db, dc))
            tau = {u:v, v:w, w:u}
            other = tuple(tau.get(i, i) for i in p)
            g = {a:b, b:c, c:a}
            pg = tuple(p[g.get(i, i)] for i in range(n))
            og = tuple(other[g.get(i, i)] for i in range(n))
            assert not any(parity(z) for z in (p, other, pg, og))
            for y, x in product(range(n), repeat=2):
                entry = int(pg[x] == y) - int(p[x] == y) - int(og[x] == y) + int(other[x] == y)
                assert entry == (int(y == u) - int(y == v)) * (int(x == c) - int(x == a))
            basis.append([a, out])
    return len(basis)


def moments(n):
    u, v = list(range(n)), [i * i + 1 for i in range(n)]
    N = n * (n - 1) // 2
    pairs = [(1 - 2 * parity(p), dot_matching(u, v, p)) for p in permutations(range(n))]
    signed = [sum(sign * x**k for sign, x in pairs) for k in range(N + 1)]
    vand = lambda a: prod(y - x for x, y in combinations(a, 2))
    denom = prod(factorial(j) for j in range(n))
    expected = factorial(N) * vand(u) * vand(v) // denom
    assert signed[:-1] == [0] * N and signed[-1] == expected
    return dict(ports=n, first_differing_order=N,
                signed_moment_sum=expected, normalization_per_coset=factorial(n)//2)


if __name__ == '__main__':
    print(json.dumps(dict(three=three_ports(), four=four_ports(),
                          rectangle_bases={n:rectangle_check(n) for n in (5, 6)},
                          moment_tests=[moments(n) for n in range(2, 7)]), indent=2))
