"""Exact finite word checks for the circulation limit. Python standard library only."""

from fractions import Fraction as F
from functools import cache
from itertools import combinations, permutations
from math import comb, lcm, prod


def circulation(size, cycles):
    matrix = [[0] * size for _ in range(size)]
    for coefficient, vertices in cycles:
        for i, j in zip(vertices, vertices[1:] + vertices[:1]):
            matrix[i][j] += coefficient
            matrix[j][i] -= coefficient
    assert all(sum(row) == 0 for row in matrix)
    return matrix


def spectral_invariants(weights, matrix):
    pairs = combinations(range(len(weights)), 2)
    s = sum(F(matrix[i][j] ** 2, weights[i] * weights[j]) for i, j in pairs)
    p = F(0)
    for i, j, k, l in combinations(range(len(weights)), 4):
        pf = (matrix[i][j] * matrix[k][l] - matrix[i][k] * matrix[j][l]
              + matrix[i][l] * matrix[j][k])
        p += F(pf**2, weights[i] * weights[j] * weights[k] * weights[l])
    return s, p


def finite_moments(n, weights, matrix):
    """Append the final letter and combine raw moment sums over all words."""
    d = len(weights)
    coeff = [[F(matrix[i][j], weights[i] * weights[j]) for j in range(d)]
             for i in range(d)]
    common = lcm(*(v.denominator for row in coeff for v in row))
    edge = [[int(common * v) for v in row] for row in coeff]
    choose = [[comb(k, j) for j in range(k + 1)] for k in range(5)]

    @cache
    def moments(inventory):
        if not any(inventory):
            return (1, 0, 0, 0, 0)
        total = [0] * 5
        for last, count in enumerate(inventory):
            if count == 0:
                continue
            prev = list(inventory)
            prev[last] -= 1
            old = moments(tuple(prev))
            step = sum(prev[i] * edge[i][last] for i in range(d))
            powers = [1, step, step**2, step**3, step**4]
            for k in range(5):
                total[k] += sum(choose[k][j] * old[j] * powers[k - j]
                                for j in range(k + 1))
        return tuple(total)

    sums = moments(tuple(n * w for w in weights))
    moments.cache_clear()
    return tuple(F(v, sums[0] * (2 * n * common)**k) for k, v in enumerate(sums))


def interpolate(nodes, values, x):
    return sum(y * prod((x - z) / (u - z) for z in nodes if z != u)
               for u, y in zip(nodes, values))


def check_example(label, weights, cycles, expected_blocks):
    matrix = circulation(len(weights), cycles)
    s, p = spectral_invariants(weights, matrix)
    assert (0 if s == 0 else 2 if p else 1) == expected_blocks
    variance = s / 12
    fourth = 3 * variance**2 + (s**2 - 2 * p) / 120
    finite = [finite_moments(n, weights, matrix) for n in range(1, 5)]
    for m0, m1, m2, m3, _ in finite:
        assert (m0, m1, m2, m3) == (1, 0, variance, 0)
    nodes = [F(1, n) for n in (1, 2, 3)]
    fourths = [m[4] for m in finite[:3]]
    assert interpolate(nodes, fourths, F(0)) == fourth
    assert interpolate(nodes, fourths, F(1, 4)) == finite[3][4]
    print(f'{label}: blocks={expected_blocks} S={s} P={p} '
          f'variance={variance} limiting fourth={fourth}')


def check_gepner_orientation():
    plus = {(2, 1, 0), (1, 0, 2), (0, 2, 1)}
    for triple in permutations(range(3)):
        a, b, c = (triple.index(i) for i in range(3))
        cycle = (a < b) + (b < c) + (c < a)
        g = 1 if triple in plus else -1
        assert g == 3 - 2 * cycle
    print('Gepner orientation verified on all six triple orders.')


if __name__ == '__main__':
    check_gepner_orientation()
    tri = [(1, (0, 1, 2))]
    check_example('zero', (1, 1, 1), [], 0)
    check_example('unit triangle', (1, 1, 1), tri, 1)
    check_example('unequal triangle', (1, 2, 3), tri, 1)
    check_example('disjoint triangles', (1,) * 6, tri + [(2, (3, 4, 5))], 2)
    check_example('overlapping weighted six-axis', (1, 2, 1, 1, 2, 1),
                  tri + [(-2, (0, 3, 4)), (1, (1, 4, 5, 3))], 2)
