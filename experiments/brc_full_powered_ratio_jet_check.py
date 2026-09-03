#!/usr/bin/env python3
"""Exact checker for the full powered branch-ratio jet on irreducible critical graphs."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product, permutations

import brc_critical_degeneracy_matrix_moment_asymptotic_check as crit
import brc_critical_powered_rational_gauge_check as pg
import brc_critical_ratio_spectral_response_check as rsp
import brc_unique_critical_cycle_moment_asymptotic_check as uc
from enterprise_math.brc_rational_holonomy import (
    rational_from_prime_valuations,
    rational_prime_valuations,
)

Q = Fraction
Branch = tuple[int, int, Fraction]
IntMatrix = tuple[tuple[int, ...], ...]
RatMatrix = tuple[tuple[Fraction, ...], ...]


def cell_map(branches: tuple[Branch, ...]):
    out: dict[tuple[int, int], list[Fraction]] = defaultdict(list)
    for u, v, q in branches:
        out[(u, v)].append(q)
    return {cell: tuple(values) for cell, values in out.items()}


def moment_matrix(n: int, branches: tuple[Branch, ...], m: int) -> RatMatrix:
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for u, v, q in branches:
        out[u][v] += q**m
    return tuple(tuple(row) for row in out)


def mat_jet(levels: tuple[Fraction, ...], layers: tuple[IntMatrix, ...], s: int) -> RatMatrix:
    n = len(layers[0])
    return tuple(
        tuple(
            sum(
                ((ratio**s) * layers[index][i][j] for index, ratio in enumerate(levels)),
                Q(0),
            )
            for j in range(n)
        )
        for i in range(n)
    )


def det_t_minus(matrix: RatMatrix, t: Fraction) -> Fraction:
    n = len(matrix)
    total = Q(0)
    for perm in permutations(range(n)):
        sign = rsp.sign_of_permutation(tuple(perm))
        term = Q(sign)
        for i, j in enumerate(perm):
            term *= (t - matrix[i][j]) if i == j else (-matrix[i][j])
        total += term
    return total


def full_ratio_jet(n: int, branches: tuple[Branch, ...]):
    analysis, components, roots, h = pg.powered_potentials(n, branches)
    K = analysis.critical_matrix
    if not rsp.irreducible(K):
        raise ValueError("critical matrix is not irreducible")
    assert components == (tuple(range(n)),)
    assert set(h) == set(range(n))

    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product
    critical = set(analysis.critical_edges)
    cells = cell_map(branches)
    ratios: list[tuple[int, int, Fraction, Fraction, bool]] = []
    for u, v, q in branches:
        lam = (q**r0) * h[v] / (q0 * h[u])
        assert Q(0) < lam <= 1
        is_dom_critical = (u, v) in critical and q == max(cells[(u, v)])
        assert (lam == 1) == is_dom_critical
        ratios.append((u, v, q, lam, is_dom_critical))

    levels = tuple(sorted({item[3] for item in ratios}, reverse=True))
    assert levels and levels[0] == 1
    layers: list[IntMatrix] = []
    for level in levels:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for u, v, _, lam, _ in ratios:
            if lam == level:
                matrix[u][v] += 1
        layers.append(tuple(tuple(row) for row in matrix))
    assert layers[0] == K
    return analysis, roots, h, tuple(ratios), levels, tuple(layers)


def direct_similarity_check(n: int, branches: tuple[Branch, ...], analysis, h, levels, layers) -> int:
    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product
    checks = 0
    for s in range(0, 5):
        m = r0 * s
        Wm = moment_matrix(n, branches, m)
        transformed = tuple(
            tuple((h[j] / h[i]) ** s * Wm[i][j] / (q0**s) for j in range(n))
            for i in range(n)
        )
        expected = mat_jet(levels, layers, s)
        assert transformed == expected
        checks += n * n

        # Exact characteristic similarity/scalar check at rational test points.
        if s > 0:
            for t in (Q(0), Q(1), Q(3, 2)):
                left = det_t_minus(Wm, (q0**s) * t) / (q0 ** (s * n))
                right = det_t_minus(transformed, t)
                assert left == right
                checks += 1
    return checks


def t40_gap(branches: tuple[Branch, ...], analysis) -> Fraction | None:
    n = analysis.state_count
    edges: uc.EdgeMap = {}
    for u, v, q in branches:
        edges.setdefault((u, v), tuple())
        edges[(u, v)] = (*edges[(u, v)], q)
    edges = uc.normalize_edges(n, edges)
    exp = uc.characteristic_exponential_coefficients(n, edges)
    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product
    strict: list[Fraction] = []
    for degree, bases in exp.items():
        k = n - degree
        if k == 0:
            continue
        for base, coeff in bases.items():
            if coeff == 0:
                continue
            lhs = base**r0
            rhs = q0**k
            assert lhs <= rhs
            if lhs < rhs:
                strict.append(lhs / rhs)
    return max(strict) if strict else None


def validate_sample(n: int, branches: tuple[Branch, ...], response_check: bool) -> tuple[int, int, int, int] | None:
    try:
        analysis, _, h, ratios, levels, layers = full_ratio_jet(n, branches)
    except ValueError:
        return None

    branch_checks = len(ratios) * 2 + len(levels)
    for _, _, _, lam, _ in ratios:
        coords = rational_prime_valuations(lam)
        assert rational_from_prime_valuations(coords) == lam
        branch_checks += 1

    matrix_checks = direct_similarity_check(n, branches, analysis, h, levels, layers)

    gap_checks = 0
    gap = t40_gap(branches, analysis)
    if len(levels) == 1:
        assert gap is None
        gap_checks += 1
    else:
        assert gap == levels[1]
        gap_checks += 1

    response_checks = 0
    if response_check and len(levels) > 1:
        K = layers[0]
        M1 = layers[1]
        p0 = tuple(Q(value) for value in cd_criticality(K))
        p1 = rsp.determinant_first_derivative(K, M1)
        response_checks += rsp.response_sign_certificate(p0, p1)
    return branch_checks, matrix_checks, gap_checks, response_checks


def cd_criticality(matrix: IntMatrix) -> tuple[int, ...]:
    from enterprise_math.brc_critical_degeneracy import criticality_polynomial
    return criticality_polynomial(matrix)


def branches_from_assignment(cells, assignment) -> tuple[Branch, ...]:
    return tuple(
        (u, v, weight)
        for (u, v), weights in zip(cells, assignment)
        for weight in weights
    )


def exhaustive_regression() -> tuple[int, int, int, int, int, int]:
    samples = branch_checks = matrix_checks = gap_checks = response_checks = strict_samples = 0

    catalog2 = [(), (Q(1, 4),), (Q(1, 2),), (Q(1, 2), Q(1, 2))]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for index, assignment in enumerate(product(catalog2, repeat=4)):
        branches = branches_from_assignment(cells2, assignment)
        result = validate_sample(2, branches, response_check=True)
        if result is None:
            continue
        samples += 1
        branch_checks += result[0]
        matrix_checks += result[1]
        gap_checks += result[2]
        response_checks += result[3]
        analysis = full_ratio_jet(2, branches)
        if len(analysis[4]) > 1:
            strict_samples += 1

    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for index, assignment in enumerate(product(catalog3, repeat=9)):
        branches = branches_from_assignment(cells3, assignment)
        # Sturm response on every 3-state sample would duplicate PR #1179's
        # 11k-core gate.  Sample it deterministically while checking the full
        # branch/matrix/T40 identities exhaustively.
        result = validate_sample(3, branches, response_check=(index % 29 == 0))
        if result is None:
            continue
        samples += 1
        branch_checks += result[0]
        matrix_checks += result[1]
        gap_checks += result[2]
        response_checks += result[3]
        analysis = full_ratio_jet(3, branches)
        if len(analysis[4]) > 1:
            strict_samples += 1

    return samples, branch_checks, matrix_checks, gap_checks, response_checks, strict_samples


def gauge_transform(branches: tuple[Branch, ...], gauge: tuple[Fraction, ...]) -> tuple[Branch, ...]:
    return tuple((u, v, q * gauge[v] / gauge[u]) for u, v, q in branches)


def special_examples() -> tuple[int, int]:
    checks = gauge_checks = 0

    # Algebraic critical mean, but a wholly rational full jet.
    algebraic = (
        (0, 1, Q(1, 2)),
        (0, 1, Q(1, 4)),
        (1, 0, Q(1, 3)),
        (0, 0, Q(1, 10)),
    )
    analysis, _, h, ratios, levels, layers = full_ratio_jet(2, algebraic)
    assert analysis.reference_cycle_length == 2
    assert analysis.reference_cycle_product == Q(1, 6)
    assert h == {0: Q(1), 1: Q(2, 3)}
    assert levels == (Q(1), Q(1, 4), Q(3, 50))
    assert layers[0] == ((0, 1), (1, 0))
    checks += 5

    # On a critical edge, full powered lambda is the r0-th power of the local
    # PR #1178 within-cell ratio.
    cells = cell_map(algebraic)
    for u, v, q, lam, _ in ratios:
        if (u, v) in set(analysis.critical_edges):
            a = max(cells[(u, v)])
            assert lam == (q / a) ** analysis.reference_cycle_length
            checks += 1

    base = full_ratio_jet(2, algebraic)
    for gauge in ((Q(2), Q(3)), (Q(5, 7), Q(11, 3))):
        transformed = full_ratio_jet(2, gauge_transform(algebraic, gauge))
        assert transformed[0].critical_matrix == base[0].critical_matrix
        assert tuple(item[3] for item in transformed[3]) == tuple(item[3] for item in base[3])
        assert transformed[4] == base[4]
        assert transformed[5] == base[5]
        gauge_checks += 4

    # No strict branch: normalized matrix is exactly K for all powered moments.
    pure = ((0, 1, Q(1, 2)), (1, 0, Q(1, 3)))
    analysis2, _, h2, _, levels2, layers2 = full_ratio_jet(2, pure)
    assert levels2 == (Q(1),)
    assert direct_similarity_check(2, pure, analysis2, h2, levels2, layers2) > 0
    checks += 2
    return checks, gauge_checks


def main() -> int:
    samples, branch_checks, matrix_checks, gap_checks, response_checks, strict_samples = exhaustive_regression()
    special, gauge = special_examples()
    assert samples > 1000
    assert strict_samples > 100
    print("BRC full powered branch-ratio jet checker: PASS")
    print(f"irreducible_critical_samples={samples}")
    print(f"branch_ratio_and_valuation_checks={branch_checks}")
    print(f"full_similarity_and_matrix_jet_checks={matrix_checks}")
    print(f"t40_gap_identification_checks={gap_checks}")
    print(f"sampled_first_response_checks={response_checks}")
    print(f"strict_ratio_samples={strict_samples}")
    print(f"special_checks={special}")
    print(f"rational_gauge_invariance_checks={gauge}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
