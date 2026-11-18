"""Exact integral exterior-algebra certificates for the marked Gaussian sixfold."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import json


def wedge_sign(left, right):
    if left & right:
        return 0
    inversions = 0
    while left:
        lowest = left & -left
        inversions += (right & (lowest - 1)).bit_count()
        left ^= lowest
    return (-1) ** inversions


def wedge(left, right):
    result = defaultdict(int)
    for i, a in left.items():
        for j, b in right.items():
            sign = wedge_sign(i, j)
            if sign:
                result[i | j] += sign * a * b
    return {k: v for k, v in result.items() if v}


def linear(terms):
    result = defaultdict(int)
    for scale, value in terms:
        for k, v in value.items():
            result[k] += scale * v
    return {k: v for k, v in result.items() if v}


def gaussian_volume(axes):
    real, imag = {0: 1}, {}
    for j in axes:
        x, y = {1 << (2 * j): 1}, {1 << (2 * j + 1): 1}
        real, imag = (linear([(1, wedge(real, x)), (-1, wedge(imag, y))]),
                      linear([(1, wedge(imag, x)), (1, wedge(real, y))]))
    return real, imag


def graph_pullback(monomial, a, b):
    result = {0: 1}
    for j in range(12):
        if monomial & (1 << j):
            step = {1 << j: a, 1 << (j ^ 1): (-b if j % 2 else b)}
            result = wedge(result, step)
    return result


def cup(left, right):
    # In signature (3,3), the complex orientation has sign - on this top form.
    return -wedge(left, right).get(2 ** 12 - 1, 0)


def coefficients(a, b):
    return [a ** (6 - j) * b ** j for j in range(7)]


def lower_certificate(a, b):
    return a * b * (a - 2*b) * (a - b) * (a + b) * (2*a - b)


def main():
    alpha, beta = gaussian_volume(range(6))
    assert (cup(alpha, alpha), cup(alpha, beta), cup(beta, beta)) == (-32, 0, -32)
    assert not alpha.keys() & beta.keys()
    assert all(abs(x) == 1 for x in [*alpha.values(), *beta.values()])
    graphs = [(30, 1, 0), (-120, 0, 1), (-10, 1, 1), (-10, 1, -1),
              (1, 1, 2), (1, 1, -2)]
    w = [1, 0, -1, 0, 1, 0, -1]
    assert [sum(t * coefficients(a, b)[j] for t, a, b in graphs)
            for j in range(7)] == [12*i for i in w]
    dual = [0, 2, -5, 0, 5, -2, 0]
    assert Fraction(sum(v * z for v, z in zip(dual, w)), 120) == Fraction(1, 12)
    for a, b in product(range(120), repeat=2):
        cert = lower_certificate(a, b)
        assert cert == sum(u*v for u, v in zip(dual, coefficients(a, b)))
        assert cert % 120 == 0

    checked = 0
    eta = sum(1 << (2 * j) for j in range(6))
    for axes in combinations(range(12), 6):
        mask = sum(1 << a for a in axes)
        a, b = -cup({mask: 1}, alpha), -cup({mask: 1}, beta)
        times32 = linear([(a, alpha), (b, beta)])
        if mask == eta:
            assert times32 == alpha
        graph = linear([(t, graph_pullback(mask, u, v)) for t, u, v in graphs])
        assert graph == linear([(12, times32)])
        checked += 1
    assert checked == 924

    pairs = [(0, 3), (1, 4), (2, 5)]
    volumes = [gaussian_volume(pair) for pair in pairs]
    for pair, (c, s) in zip(pairs, volumes):
        top = sum(3 << (2*j) for j in pair)
        assert wedge(c, c) == wedge(s, s) == {top: 2}
        assert not wedge(c, s)
    parts = [[], []]
    for choices in product(range(2), repeat=3):
        term = {0: 1}
        for vol, choice in zip(volumes, choices):
            term = wedge(term, vol[choice])
        degree = sum(choices)
        parts[degree % 2].append(((-1) ** (degree // 2), term))
    # Paired determinant order (0,3,1,4,2,5) has odd sign.
    assert linear(parts[0]) == linear([(-1, alpha)])
    assert linear(parts[1]) == linear([(-1, beta)])
    # At the split reference point take the positive plane span(u_1,u_2,u_3);
    # c_j has sigma-component u_j^* wedge v_j^*.  Its restriction to the
    # deformed plane gives the entries Xi_{j,l} with l != j.
    tangent_rows = []
    for j in range(3):
        for k, l in combinations(range(3), 2):
            row = [0]*9
            if k == j:
                row[3*j+l] += 1
            if l == j:
                row[3*j+k] -= 1
            if any(row):
                tangent_rows.append(row)
    off_diagonal = sorted(next(i for i,x in enumerate(row) if x)
                          for row in tangent_rows)
    assert off_diagonal == [1, 2, 3, 5, 6, 7]
    print(json.dumps({"integral_gram": [[-32, 0], [0, -32]],
                      "primitive_volume_support": [len(alpha), len(beta)],
                      "cohomological_minimum": 32, "gaussian_graph_minimum": 384,
                      "graph_expression_weight_a_b": graphs, "dual_numerator": dual,
                      "dual_value_on_32_projector": "1/12",
                      "integer_valued_residues_checked": 120**2,
                      "degree_six_columns_checked": checked,
                      "surface_gram": [[-2, 0], [0, -2]], "terms_per_pure_class": [4, 4],
                      "tangent_rows_at_reference_point": tangent_rows,
                      "tangent_kernel_dimension": 3}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
