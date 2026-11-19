#!/usr/bin/env python3
"""R284AX: exact unit-strength Port-star reconstruction, standard library only."""
import hashlib
import itertools
import json
import math
import random
from math import isqrt
from pathlib import Path


def det(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign, old = 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            pivot_row = next((j for j in range(k + 1, n) if a[j][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % old == 0
                a[i][j] = num // old
            a[i][k] = 0
        old = pivot
    return sign * a[-1][-1]


def poly_coeff(c, edit=None):
    """Return signed coefficient indexed by the deleted-diagonal-variable set T."""
    n = len(c)
    a = [row[:] for row in c]
    if edit is not None:
        a[0][edit] += 1
    out = []
    for mask in range(1 << n):
        t = [j for j in range(n) if mask & (1 << j)]
        out.append((-1) ** len(t) * det([[a[i][j] for j in t] for i in t]))
    return tuple(out)


def reconstruct(responses):
    """Responses v -> subset coefficient vector of det(D-C-E_0v)."""
    n = (len(next(iter(responses.values()))) - 1).bit_length()
    def mask(t):
        return sum(1 << i for i in t)
    def at(v, t):
        return responses[v][mask(t)]
    def unchanged(t):
        return next(at(v, t) for v in range(1, n) if not (0 in t and v in t))

    a = [-unchanged({i}) for i in range(n)]
    p = {(i, j): a[i] * a[j] - unchanged({i, j})
         for i in range(n) for j in range(i + 1, n)}
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        c[i][i] = a[i]
    for v in range(1, n):
        c[v][0] = unchanged({0, v}) - at(v, {0, v})
        assert c[v][0] > 0 and p[0, v] % c[v][0] == 0
        c[0][v] = p[0, v] // c[v][0]

    if n == 3:
        delta = at(1, {0, 1, 2}) - at(2, {0, 1, 2})
        s = delta - a[2] * c[1][0] + a[1] * c[2][0]
        A, B = c[2][0], c[1][0] * p[1, 2]
        root = isqrt(s * s + 4 * A * B)
        assert root * root == s * s + 4 * A * B
        assert (-s + root) % (2 * A) == 0
        x = (-s + root) // (2 * A)
        assert x > 0 and p[1, 2] % x == 0
        c[1][2], c[2][1] = x, p[1, 2] // x
    else:
        for i in range(1, n):
            for j in range(i + 1, n):
                g = at(i, {0, i, j}) - unchanged({0, i, j})
                num = a[j] * c[i][0] - g
                assert num % c[j][0] == 0
                x = num // c[j][0]
                assert x > 0 and p[i, j] % x == 0
                c[i][j], c[j][i] = x, p[i, j] // x
    return c


def weights_b3(n):
    w = []
    for t in range(n):
        forbidden = set()
        for k in (1, 2, 3):
            if k <= t:
                for a in itertools.combinations(w, k - 1):
                    for b in itertools.combinations(w, k):
                        forbidden.add(sum(b) - sum(a))
        x = w[-1] + 1 if w else 1
        while x in forbidden:
            x += 1
        w.append(x)
    for k in range(1, min(3, n) + 1):
        sums = [sum(x) for x in itertools.combinations(w, k)]
        assert len(sums) == len(set(sums))
    return w


def balanced_digits(x, base):
    digits = {}
    e = 0
    while x:
        x, rem = divmod(x, base)
        if rem >= base // 2:
            x += 1
            rem -= base
        if rem:
            digits[e] = rem
        e += 1
    return digits


def scalar_case(c, H):
    n = len(c)
    w = weights_b3(n)
    W = 1 + sum(w)
    A = (1 << (n + 1)) * math.factorial(n) * (H + 1) ** n
    base = 1 << (2 * A).bit_length()
    d = [base ** (W + wi) for wi in w]
    def exponent(mask):
        return sum((W + w[i]) for i in range(n) if not (mask & (1 << i)))
    recovered_polys = {}
    read_bits = []
    for v in range(1, n):
        m = [[(d[i] if i == j else 0) - c[i][j] - int(i == 0 and j == v)
              for j in range(n)] for i in range(n)]
        y = det(m)
        read_bits.append(abs(y).bit_length())
        digits = balanced_digits(y, base)
        recovered_polys[v] = tuple(digits.get(exponent(t), 0) for t in range(1 << n))
    assert reconstruct(recovered_polys) == c
    return {'n': n, 'H': H, 'weights': w,
            'max_diagonal_bits': max(x.bit_length() for x in d),
            'max_reading_bits': max(read_bits)}


def main():
    rng = random.Random(2842823)
    counts = {}
    for n, N in [(3, 512), (4, 250), (5, 50), (6, 12)]:
        for k in range(N):
            H = 2 if n == 3 else 2 + k % 3
            arr = list(itertools.product((1, 2), repeat=9))[k] if n == 3 else [rng.randint(1, H) for _ in range(n*n)]
            c = [list(arr[i*n:(i+1)*n]) for i in range(n)]
            assert reconstruct({v: poly_coeff(c, v) for v in range(1, n)}) == c
        counts[str(n)] = N
    scalars = []
    for n, N in [(3, 52), (4, 14), (5, 3), (6, 1)]:
        for k in range(N):
            H = 2 + k % 3
            c = [[rng.randint(1, H) for _ in range(n)] for _ in range(n)]
            scalars.append(scalar_case(c, H))
    # Same unit response at n=2, H=3: offdiagonal (1,3) vs (2,2).
    c1, c2 = [[1, 1], [3, 1]], [[1, 2], [2, 1]]
    assert poly_coeff(c1, 1) == poly_coeff(c2, 1) and c1 != c2
    report = {'research_unit': 'R284AX', 'status': 'PASS', 'seed': 2842823,
              'polynomial_coefficient_exact_cases': counts,
              'polynomial_coefficient_total': sum(counts.values()),
              'exhaustive_n3_H2': 512, 'scalar_exact_cases': len(scalars),
              'max_diagonal_bits': max(x['max_diagonal_bits'] for x in scalars),
              'max_reading_bits': max(x['max_reading_bits'] for x in scalars),
              'largest_tested_dimension': 6,
              'n2_fixed_unit_collision': {'C': c1, 'Cprime': c2, 'equal_response_coefficients': poly_coeff(c1, 1)},
              'scalar_example': scalars[-1],
              'evidence_semantics': 'exact integer coefficients and Bareiss determinants; finite coverage only',
              'independent_review': 'NOT_REVIEWED'}
    out = Path(__file__).with_name('R284AX_unit_star_scalar_verification.json')
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
