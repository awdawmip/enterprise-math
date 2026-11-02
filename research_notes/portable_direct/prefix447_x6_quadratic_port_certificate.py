#!/usr/bin/env python3
"""PREFIX-447: exact X6 quadratic moment unisolvency and typed affine BRC transport.

Pure standard-library certificate. This checks the mathematical port law; it
is not an import/execution of the frozen enterprise_math package.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations

D = 6
QDIM = D + 1


def base_paths():
    """28 signed native-X6 length-4 words, one per interpolation endpoint."""
    words = [[(2, 1), (2, -1), (2, 1), (2, -1)]]
    for i in range(1, D + 1):
        for s in (1, -1):
            words.append([(i, s), (i, s), (2, 1), (2, -1)])
    for i, j in combinations(range(1, D + 1), 2):
        words.append([(i, 1), (i, 1), (j, 1), (j, 1)])
    return words


def endpoint(word):
    v = [0] * D
    for axis, sign in word:
        assert 1 <= axis <= D and sign in (-1, 1)
        v[axis - 1] += sign
    return tuple(v)


def history(word):
    return sum(1 for axis, sign in word if axis == 1 and sign == -1)


def sector_pad(word, r, q):
    t = (r - history(word)) % q
    out = list(word)
    out.extend([(1, -1), (1, 1)] * t)
    out.extend([(2, 1), (2, -1)] * (q - 1 - t))
    return out


def features(p):
    return (1,) + tuple(v for x in p for v in (x, x * x)) + tuple(p[i] * p[j] for i, j in combinations(range(D), 2))


def exact_det(matrix):
    """Fraction-free Bareiss determinant, with row pivoting."""
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    assert n > 0 and all(len(row) == n for row in a)
    sign = 1
    denominator = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % denominator == 0
                a[i][j] = num // denominator
            a[i][k] = 0
        denominator = pivot
    return sign * a[-1][-1]


def matsum(a, b):
    return [[x + y for x, y in zip(rowa, rowb)] for rowa, rowb in zip(a, b)]


def zeros():
    return [[Q(0) for _ in range(QDIM)] for _ in range(QDIM)]


def moment(paths, q):
    out = [zeros() for _ in range(q)]
    for r, v, weight in paths:
        z = list(map(Q, v)) + [Q(1)]
        assert 0 <= r < q and isinstance(weight, Q) and weight > 0
        for i in range(QDIM):
            for j in range(QDIM):
                out[r][i][j] += weight * z[i] * z[j]
    return out


def identity():
    return [[Q(i == j) for j in range(QDIM)] for i in range(QDIM)]


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return list(map(list, zip(*a)))


def apply(h, p):
    z = list(map(Q, p)) + [Q(1)]
    return tuple(sum((x * y for x, y in zip(row, z)), Q(0)) for row in h[:-1])


def kernel(q):
    out = []
    for r in range(q):
        hp = identity()
        hp[0][-1] = Q(1)
        hs = identity()
        hs[0][1] = Q(1)
        hs[1][-1] = Q(-1)
        out.append((r, r, Q(r + 2, r + 3), hp))
        out.append((r, (r + 1) % q, Q(2 * r + 1, 2 * r + 3), hs))
    return out


def step_direct(paths, edges):
    out = []
    for r, v, w in paths:
        for src, dst, factor, h in edges:
            if r == src:
                out.append((dst, apply(h, v), w * factor))
    return out


def step_moment(states, edges):
    out = [zeros() for _ in states]
    for src, dst, factor, h in edges:
        term = matmul(matmul(h, states[src]), transpose(h))
        for i in range(QDIM):
            for j in range(QDIM):
                out[dst][i][j] += factor * term[i][j]
    return out


def small_witness(q=3, r=0):
    # 2 point sources: same complete six one-axis marginals; different x1*x2.
    pairs_a = ((2, 2), (-2, -2))
    pairs_b = ((2, -2), (-2, 2))
    def source(pairs):
        out = []
        for x, y in pairs:
            w = [(1, 1 if x > 0 else -1)] * 2 + [(2, 1 if y > 0 else -1)] * 2
            word = sector_pad(w, r, q)
            assert len(word) == 2 * q + 2 and history(word) % q == r
            out.append((r, endpoint(word), Q(1)))
        return out
    return source(pairs_a), source(pairs_b)


def main():
    base = base_paths()
    assert len(base) == 28 and all(len(w) == 4 for w in base)
    points = [endpoint(w) for w in base]
    assert len(set(points)) == 28 and len(features(points[0])) == 28
    det = exact_det([features(p) for p in points])
    assert det == 2 ** 54, det
    witness_counts = {}
    for q in (2, 3, 4, 5):
        rows = []
        for r in range(q):
            for w in base:
                ww = sector_pad(w, r, q)
                assert len(ww) == 2 * q + 2
                assert history(ww) % q == r
                assert endpoint(ww) == endpoint(w)
                rows.append((r, ww))
        assert len(rows) == 28 * q and len({(r,tuple(w)) for r,w in rows}) == 28*q
        # The sector-labeled quadratic observation matrix has q diagonal
        # copies of the unimodular-over-Q block with determinant 2**54.
        witness_counts[q] = len(rows)
    a, b = small_witness()
    for j in range(D):
        assert Counter(p[j] for _, p, _ in a) == Counter(p[j] for _, p, _ in b)
    cross_a = sum((w * p[0] * p[1] for _, p, w in a), Q(0))
    cross_b = sum((w * p[0] * p[1] for _, p, w in b), Q(0))
    shear_a = sum((w * (p[0] + p[1]) ** 2 for _, p, w in a), Q(0))
    shear_b = sum((w * (p[0] + p[1]) ** 2 for _, p, w in b), Q(0))
    assert (cross_a,cross_b,shear_a,shear_b) == (8,-8,32,0)
    ncontrol = 3
    source = []
    for r in range(ncontrol):
        for idx, word in enumerate(base):
            ww = sector_pad(word, r, ncontrol)
            source.append((r,endpoint(ww),Q(idx+1, idx%7+1)))
    state = moment(source,ncontrol)
    edges = kernel(ncontrol)
    for step_no in (1,2,3):
        source = step_direct(source,edges)
        state = step_moment(state,edges)
        assert moment(source,ncontrol) == state, f'typed affine moment mismatch at step {step_no}'
    print(f'PASS: 28 interpolation points; determinant=2^54={det}')
    print(f'PASS: native-X6 same-duration sector-labeled words counts={witness_counts}')
    print(f'PASS: two-word marginal fiber: cross=({cross_a},{cross_b}); shear_square=({shear_a},{shear_b})')
    print(f'PASS: typed affine BRC moment transport, 3 serial updates, 3 sectors, 168 initial weighted branches after first kernel')
    print('VERIFICATION_SCOPE: exact Fraction/int and native signed-path word construction; independent port algebra, not upstream class import')


if __name__ == '__main__':
    main()
