#!/usr/bin/env python3
"""Exact checks for the prime-valuation universal BRC histogram transfer."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product

from enterprise_math.brc_rational_holonomy import (
    rational_from_prime_valuations,
    rational_prime_valuations,
)

Histogram = dict[Q, int]
SignedHistogram = dict[Q, int]
HMatrix = list[list[Histogram]]
QMatrix = list[list[Q]]
Edge = tuple[int, int, Q]


def hclean(hist: dict[Q, int]) -> dict[Q, int]:
    return {q: c for q, c in hist.items() if c != 0}


def hzero() -> Histogram:
    return {}


def hone() -> Histogram:
    return {Q(1): 1}


def hfrom_weights(weights: tuple[Q, ...]) -> Histogram:
    out: Histogram = {}
    for weight in weights:
        assert weight > 0
        out[weight] = out.get(weight, 0) + 1
    return out


def hadd(left: Histogram, right: Histogram) -> Histogram:
    out = dict(left)
    for q, c in right.items():
        out[q] = out.get(q, 0) + c
    return hclean(out)


def hmul(left: Histogram, right: Histogram) -> Histogram:
    if not left or not right:
        return {}
    out: Histogram = {}
    for q, c in left.items():
        for r, d in right.items():
            qr = q * r
            out[qr] = out.get(qr, 0) + c * d
    return hclean(out)


def hcount(hist: Histogram) -> int:
    return sum(hist.values())


def hmass(hist: Histogram) -> Q:
    return sum((q * c for q, c in hist.items()), Q(0))


def hmax(hist: Histogram) -> Q:
    return max(hist) if hist else Q(0)


def hmoment(hist: Histogram, moment: int) -> Q:
    return sum((c * q**moment for q, c in hist.items()), Q(0))


def hbool(hist: Histogram) -> bool:
    return bool(hist)


def hscale_weight(hist: Histogram, factor: Q) -> Histogram:
    assert factor > 0
    return {q * factor: c for q, c in hist.items()}


def hmat_zero(rows: int, cols: int) -> HMatrix:
    return [[{} for _ in range(cols)] for _ in range(rows)]


def hmat_eye(n: int) -> HMatrix:
    out = hmat_zero(n, n)
    for i in range(n):
        out[i][i] = hone()
    return out


def hmat_add(left: HMatrix, right: HMatrix) -> HMatrix:
    return [[hadd(left[i][j], right[i][j]) for j in range(len(left[0]))] for i in range(len(left))]


def hmat_mul(left: HMatrix, right: HMatrix) -> HMatrix:
    if not left or not right:
        return []
    out = hmat_zero(len(left), len(right[0]))
    for i in range(len(left)):
        for j in range(len(right[0])):
            value: Histogram = {}
            for k in range(len(right)):
                value = hadd(value, hmul(left[i][k], right[k][j]))
            out[i][j] = value
    return out


def hmat_pow(matrix: HMatrix, exponent: int) -> HMatrix:
    result = hmat_eye(len(matrix))
    base = [[dict(value) for value in row] for row in matrix]
    power = exponent
    while power:
        if power & 1:
            result = hmat_mul(result, base)
        base = hmat_mul(base, base)
        power >>= 1
    return result


def hsubmatrix(matrix: HMatrix, rows: list[int], cols: list[int]) -> HMatrix:
    return [[dict(matrix[i][j]) for j in cols] for i in rows]


def hboundary_block(matrix: HMatrix, boundary: list[int]) -> HMatrix:
    return hsubmatrix(matrix, boundary, boundary)


def universal_matrix(vertex_count: int, edges: list[Edge]) -> HMatrix:
    matrix = hmat_zero(vertex_count, vertex_count)
    for source, target, weight in edges:
        matrix[source][target] = hadd(matrix[source][target], {weight: 1})
    return matrix


def explicit_walk_histograms(vertex_count: int, edges: list[Edge], length: int) -> HMatrix:
    outgoing: list[list[tuple[int, Q]]] = [[] for _ in range(vertex_count)]
    for source, target, weight in edges:
        outgoing[source].append((target, weight))
    result = hmat_zero(vertex_count, vertex_count)
    for source in range(vertex_count):
        def walk(state: int, depth: int, weight: Q) -> None:
            if depth == length:
                result[source][state] = hadd(result[source][state], {weight: 1})
                return
            for target, edge_weight in outgoing[state]:
                walk(target, depth + 1, weight * edge_weight)
        walk(source, 0, Q(1))
    return result


def eval_hmatrix(matrix: HMatrix, moment: int) -> QMatrix:
    return [[hmoment(value, moment) for value in row] for row in matrix]


def qmat_mul(left: QMatrix, right: QMatrix) -> QMatrix:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0)) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def qmat_pow(matrix: QMatrix, exponent: int) -> QMatrix:
    result = [[Q(int(i == j)) for j in range(len(matrix))] for i in range(len(matrix))]
    base = [row[:] for row in matrix]
    power = exponent
    while power:
        if power & 1:
            result = qmat_mul(result, base)
        base = qmat_mul(base, base)
        power >>= 1
    return result


def check_histogram_semiring() -> int:
    values = [Q(1, 3), Q(1, 2), Q(2, 3), Q(1), Q(3, 2)]
    families = [()] + [(value,) for value in values] + [pair for pair in product(values, repeat=2)]
    histograms = [hfrom_weights(tuple(family)) for family in families]
    checks = 0
    for left in histograms:
        for right in histograms:
            added = hadd(left, right)
            multiplied = hmul(left, right)
            assert hcount(added) == hcount(left) + hcount(right)
            assert hcount(multiplied) == hcount(left) * hcount(right)
            assert hmass(added) == hmass(left) + hmass(right)
            assert hmass(multiplied) == hmass(left) * hmass(right)
            assert hmax(added) == max(hmax(left), hmax(right))
            assert hmax(multiplied) == hmax(left) * hmax(right)
            assert hbool(added) == (hbool(left) or hbool(right))
            assert hbool(multiplied) == (hbool(left) and hbool(right))
            for moment in range(7):
                assert hmoment(added, moment) == hmoment(left, moment) + hmoment(right, moment)
                assert hmoment(multiplied, moment) == hmoment(left, moment) * hmoment(right, moment)
                checks += 2
    return checks


def check_universal_path_histograms() -> tuple[int, int]:
    edges: list[Edge] = [
        (0, 0, Q(1, 2)),
        (0, 0, Q(1, 3)),
        (0, 1, Q(2, 3)),
        (1, 1, Q(1, 6)),
        (1, 2, Q(3, 4)),
        (1, 2, Q(1, 4)),
        (2, 0, Q(1, 5)),
    ]
    matrix = universal_matrix(3, edges)
    path_checks = 0
    readout_checks = 0
    numeric_matrices = {moment: eval_hmatrix(matrix, moment) for moment in range(7)}
    for length in range(6):
        powered = hmat_pow(matrix, length)
        explicit = explicit_walk_histograms(3, edges, length)
        assert powered == explicit
        path_checks += 9
        for i in range(3):
            for j in range(3):
                hist = powered[i][j]
                if hist:
                    count = hcount(hist)
                    mass = hmass(hist)
                    dominant = hmax(hist)
                    assert count >= 1 and mass >= dominant > 0
                for moment in range(7):
                    assert hmoment(hist, moment) == qmat_pow(numeric_matrices[moment], length)[i][j]
                    readout_checks += 1
    return path_checks, readout_checks


def valuation_eval(valuations: tuple[tuple[int, int], ...], moment: int) -> Q:
    out = Q(1)
    for prime, exponent in valuations:
        power = exponent * moment
        if power >= 0:
            out *= prime**power
        else:
            out /= prime ** (-power)
    return out


def check_prime_valuation_specialization() -> int:
    values = [Q(1, 12), Q(2, 3), Q(9, 10), Q(25, 14), Q(81, 50)]
    checks = 0
    for value in values:
        valuations = rational_prime_valuations(value)
        assert rational_from_prime_valuations(valuations) == value
        for moment in range(7):
            assert valuation_eval(valuations, moment) == value**moment
            checks += 1
    # Explicit example x_3^-1 + x_2 x_3^-1 for {1/3,2/3}.
    hist = hfrom_weights((Q(1, 3), Q(2, 3)))
    assert hmoment(hist, 0) == 2
    assert hmoment(hist, 1) == 1
    assert hmoment(hist, 2) == Q(5, 9)
    return checks


# Signed group-ring polynomial completion used only for finite adjugate/determinant compression.
# A coefficient is a signed finite dictionary rational-weight -> integer coefficient.
def gr_add(left: SignedHistogram, right: SignedHistogram) -> SignedHistogram:
    out = dict(left)
    for q, c in right.items():
        out[q] = out.get(q, 0) + c
    return hclean(out)


def gr_neg(value: SignedHistogram) -> SignedHistogram:
    return {q: -c for q, c in value.items()}


def gr_mul(left: SignedHistogram, right: SignedHistogram) -> SignedHistogram:
    if not left or not right:
        return {}
    out: SignedHistogram = {}
    for q, c in left.items():
        for r, d in right.items():
            qr = q * r
            out[qr] = out.get(qr, 0) + c * d
    return hclean(out)


Polynomial = list[SignedHistogram]


def ptrim(poly: Polynomial) -> Polynomial:
    out = [hclean(coef) for coef in poly]
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def padd(left: Polynomial, right: Polynomial) -> Polynomial:
    size = max(len(left), len(right))
    out: Polynomial = []
    for i in range(size):
        a = left[i] if i < len(left) else {}
        b = right[i] if i < len(right) else {}
        out.append(gr_add(a, b))
    return ptrim(out)


def pneg(value: Polynomial) -> Polynomial:
    return ptrim([gr_neg(coef) for coef in value])


def pmul(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = [{} for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = gr_add(out[i + j], gr_mul(a, b))
    return ptrim(out)


def identity_poly() -> Polynomial:
    return [{Q(1): 1}]


def zero_poly() -> Polynomial:
    return [{}]


def i_minus_z_hist(diagonal: bool, hist: Histogram) -> Polynomial:
    constant = {Q(1): 1} if diagonal else {}
    return ptrim([constant, gr_neg(hist)])


def pmat_mul(left: list[list[Polynomial]], right: list[list[Polynomial]]) -> list[list[Polynomial]]:
    out = [[zero_poly() for _ in range(len(right[0]))] for _ in range(len(left))]
    for i in range(len(left)):
        for j in range(len(right[0])):
            value = zero_poly()
            for k in range(len(right)):
                value = padd(value, pmul(left[i][k], right[k][j]))
            out[i][j] = value
    return out


def check_finite_rational_compression() -> None:
    edges: list[Edge] = [
        (0, 0, Q(1, 2)),
        (0, 1, Q(1, 3)),
        (0, 1, Q(2, 3)),
        (1, 0, Q(3, 5)),
        (1, 1, Q(1, 4)),
    ]
    w = universal_matrix(2, edges)
    m00 = i_minus_z_hist(True, w[0][0])
    m01 = i_minus_z_hist(False, w[0][1])
    m10 = i_minus_z_hist(False, w[1][0])
    m11 = i_minus_z_hist(True, w[1][1])
    matrix = [[m00, m01], [m10, m11]]
    det = padd(pmul(m00, m11), pneg(pmul(m01, m10)))
    adj = [[m11, pneg(m01)], [pneg(m10), m00]]
    product_matrix = pmat_mul(matrix, adj)
    assert product_matrix[0][0] == det
    assert product_matrix[1][1] == det
    assert product_matrix[0][1] == zero_poly()
    assert product_matrix[1][0] == zero_poly()
    assert det[0] == {Q(1): 1}
    # Finite signed compression is distinct from the non-negative path coefficients.
    assert any(c < 0 for coefficient in det for c in coefficient.values())
    for length in range(5):
        powered = hmat_pow(w, length)
        assert all(c >= 0 for row in powered for hist in row for c in hist.values())


def universal_segment_coefficients(matrix: HMatrix, internal: list[int], max_length: int) -> tuple[list[int], list[HMatrix]]:
    n = len(matrix)
    internal_set = set(internal)
    boundary = [i for i in range(n) if i not in internal_set]
    a = hsubmatrix(matrix, internal, internal)
    x = hsubmatrix(matrix, internal, boundary)
    y = hsubmatrix(matrix, boundary, internal)
    b = hsubmatrix(matrix, boundary, boundary)
    coeffs = [hmat_zero(len(boundary), len(boundary)) for _ in range(max_length + 1)]
    if max_length >= 1:
        coeffs[1] = b
    for length in range(2, max_length + 1):
        coeffs[length] = hmat_mul(hmat_mul(y, hmat_pow(a, length - 2)), x)
    return boundary, coeffs


def universal_port_star_coefficients(segment_coeffs: list[HMatrix], max_length: int) -> list[HMatrix]:
    size = len(segment_coeffs[0])
    result = [hmat_zero(size, size) for _ in range(max_length + 1)]
    result[0] = hmat_eye(size)
    for n in range(1, max_length + 1):
        total = hmat_zero(size, size)
        for length in range(1, n + 1):
            total = hmat_add(total, hmat_mul(segment_coeffs[length], result[n - length]))
        result[n] = total
    return result


def qsegment_coefficients(matrix: QMatrix, internal: list[int], max_length: int) -> tuple[list[int], list[QMatrix]]:
    n = len(matrix)
    internal_set = set(internal)
    boundary = [i for i in range(n) if i not in internal_set]
    a = [[matrix[i][j] for j in internal] for i in internal]
    x = [[matrix[i][j] for j in boundary] for i in internal]
    y = [[matrix[i][j] for j in internal] for i in boundary]
    b = [[matrix[i][j] for j in boundary] for i in boundary]
    coeffs = [[[Q(0) for _ in boundary] for _ in boundary] for _ in range(max_length + 1)]
    if max_length >= 1:
        coeffs[1] = b
    for length in range(2, max_length + 1):
        coeffs[length] = qmat_mul(qmat_mul(y, qmat_pow(a, length - 2)), x)
    return boundary, coeffs


def check_universal_port_transfer() -> tuple[int, int]:
    edges: list[Edge] = [
        (0, 0, Q(1, 5)),
        (0, 1, Q(1, 7)),
        (1, 0, Q(1, 11)),
        (1, 1, Q(1, 6)),
        (0, 2, Q(1, 3)),
        (0, 2, Q(1, 4)),
        (1, 3, Q(2, 5)),
        (2, 0, Q(1, 8)),
        (2, 1, Q(1, 9)),
        (2, 3, Q(1, 10)),
        (3, 0, Q(1, 12)),
        (3, 2, Q(1, 13)),
    ]
    universal = universal_matrix(4, edges)
    boundary, segments = universal_segment_coefficients(universal, [0, 1], 7)
    assert boundary == [2, 3]
    port_star = universal_port_star_coefficients(segments, 7)
    coefficient_checks = 0
    specialization_checks = 0
    for length in range(8):
        full = hboundary_block(hmat_pow(universal, length), boundary)
        assert port_star[length] == full
        coefficient_checks += 4
    for moment in range(6):
        numeric = eval_hmatrix(universal, moment)
        boundary_q, segments_q = qsegment_coefficients(numeric, [0, 1], 7)
        assert boundary_q == boundary
        for length in range(1, 8):
            assert eval_hmatrix(segments[length], moment) == segments_q[length]
            specialization_checks += 4
    return coefficient_checks, specialization_checks


def gauge_universal_edges(edges: list[Edge], potentials: list[Q]) -> list[Edge]:
    return [(s, t, w * potentials[t] / potentials[s]) for s, t, w in edges]


def gauge_hmatrix(matrix: HMatrix, potentials: list[Q]) -> HMatrix:
    return [
        [hscale_weight(matrix[i][j], potentials[j] / potentials[i]) for j in range(len(matrix))]
        for i in range(len(matrix))
    ]


def check_universal_gauge() -> None:
    edges: list[Edge] = [
        (0, 0, Q(1, 5)), (0, 1, Q(1, 7)), (1, 0, Q(1, 11)),
        (0, 2, Q(1, 3)), (1, 3, Q(2, 5)), (2, 0, Q(1, 8)),
        (3, 1, Q(1, 12)), (2, 3, Q(1, 10)),
    ]
    h = [Q(2), Q(3), Q(5), Q(7)]
    w = universal_matrix(4, edges)
    wg = universal_matrix(4, gauge_universal_edges(edges, h))
    assert wg == gauge_hmatrix(w, h)
    boundary, segments = universal_segment_coefficients(w, [0, 1], 6)
    boundary_g, segments_g = universal_segment_coefficients(wg, [0, 1], 6)
    assert boundary_g == boundary == [2, 3]
    h_boundary = [h[i] for i in boundary]
    for length in range(1, 7):
        assert segments_g[length] == gauge_hmatrix(segments[length], h_boundary)
        # Moment specializations recover the H_m gauge law.
        for moment in range(5):
            numeric = eval_hmatrix(segments[length], moment)
            numeric_g = eval_hmatrix(segments_g[length], moment)
            h_m = [value**moment for value in h_boundary]
            expected = [
                [numeric[i][j] * h_m[j] / h_m[i] for j in range(2)]
                for i in range(2)
            ]
            assert numeric_g == expected
            if moment == 0:
                assert numeric_g == numeric


def two_route_universal(weights: tuple[Q, Q]) -> HMatrix:
    # order [i1,i2,u,v], hidden [0,1].
    edges: list[Edge] = [
        (2, 0, weights[0]), (0, 3, Q(1)),
        (2, 1, weights[1]), (1, 3, Q(1)),
    ]
    universal = universal_matrix(4, edges)
    _, segments = universal_segment_coefficients(universal, [0, 1], 2)
    return segments[2]


def check_port_prefix_resolution() -> None:
    a = two_route_universal((Q(1, 3), Q(2, 3)))
    b = two_route_universal((Q(1, 4), Q(3, 4)))
    assert a != b
    assert a[0][1] == {Q(1, 3): 1, Q(2, 3): 1}
    assert b[0][1] == {Q(1, 4): 1, Q(3, 4): 1}
    assert hmoment(a[0][1], 0) == hmoment(b[0][1], 0) == 2
    assert hmoment(a[0][1], 1) == hmoment(b[0][1], 1) == 1
    assert hmoment(a[0][1], 2) == Q(5, 9)
    assert hmoment(b[0][1], 2) == Q(5, 8)


def main() -> int:
    semiring_checks = check_histogram_semiring()
    path_checks, readout_checks = check_universal_path_histograms()
    valuation_checks = check_prime_valuation_specialization()
    check_finite_rational_compression()
    port_checks, specialization_checks = check_universal_port_transfer()
    check_universal_gauge()
    check_port_prefix_resolution()
    print("BRC prime-valuation universal transfer checker: PASS")
    print(f"semiring_character_checks={semiring_checks}")
    print(f"path_histogram_checks={path_checks}")
    print(f"histogram_readout_checks={readout_checks}")
    print(f"prime_valuation_specializations={valuation_checks}")
    print(f"universal_port_coefficient_checks={port_checks}")
    print(f"universal_port_moment_specializations={specialization_checks}")
    print("finite_adjugate_compression=PASS")
    print("universal_gauge_naturality=PASS")
    print("port_prefix_resolution=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
