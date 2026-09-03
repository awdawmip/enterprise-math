#!/usr/bin/env python3
"""Exact checker for rational powered critical gauges and valuation flattening."""

from __future__ import annotations

from fractions import Fraction
from itertools import product

from enterprise_math.brc_critical_degeneracy import critical_degeneracy_analysis
from enterprise_math.brc_rational_holonomy import (
    rational_from_prime_valuations,
    rational_prime_valuations,
)

Q = Fraction
Branch = tuple[int, int, Fraction]


def branches_from_cells(n: int, cells: dict[tuple[int, int], tuple[Fraction, ...]]) -> tuple[Branch, ...]:
    return tuple(
        (source, target, weight)
        for (source, target), weights in cells.items()
        for weight in weights
    )


def cell_map(branches: tuple[Branch, ...]) -> dict[tuple[int, int], tuple[Fraction, ...]]:
    out: dict[tuple[int, int], list[Fraction]] = {}
    for source, target, weight in branches:
        out.setdefault((source, target), []).append(weight)
    return {cell: tuple(weights) for cell, weights in out.items()}


def critical_components(n: int, critical_edges: tuple[tuple[int, int], ...]) -> tuple[tuple[int, ...], ...]:
    states = sorted({v for edge in critical_edges for v in edge})
    edge_set = set(critical_edges)
    reach = [[False for _ in range(n)] for _ in range(n)]
    for state in range(n):
        reach[state][state] = True
    for source, target in edge_set:
        reach[source][target] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    remaining = set(states)
    components: list[tuple[int, ...]] = []
    while remaining:
        root = min(remaining)
        component = tuple(sorted(v for v in remaining if reach[root][v] and reach[v][root]))
        assert component
        components.append(component)
        remaining.difference_update(component)
    return tuple(components)


def powered_potentials(n: int, branches: tuple[Branch, ...]):
    analysis = critical_degeneracy_analysis(n, branches)
    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product
    dominant = analysis.dominant_mass_matrix
    critical = set(analysis.critical_edges)
    components = critical_components(n, analysis.critical_edges)

    h: dict[int, Fraction] = {}
    roots: dict[int, int] = {}
    for component in components:
        root = min(component)
        h[root] = Q(1)
        for vertex in component:
            roots[vertex] = root
        changed = True
        while changed:
            changed = False
            for source, target in sorted(critical):
                if source not in component or target not in component or source not in h:
                    continue
                candidate = q0 * h[source] / (dominant[source][target] ** r0)
                if target not in h:
                    h[target] = candidate
                    changed = True
                else:
                    assert h[target] == candidate
        assert all(vertex in h for vertex in component)

    for source, target in critical:
        assert dominant[source][target] ** r0 * h[target] == q0 * h[source]

    return analysis, components, roots, h


def valuation_dict(value: Fraction) -> dict[int, int]:
    coords = dict(rational_prime_valuations(value))
    assert rational_from_prime_valuations(coords) == value
    return coords


def valuation_checks(analysis, h: dict[int, Fraction]) -> int:
    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product
    q0v = valuation_dict(q0)
    checks = 0
    for source, target in analysis.critical_edges:
        av = valuation_dict(analysis.dominant_mass_matrix[source][target])
        huv = valuation_dict(h[source])
        hvv = valuation_dict(h[target])
        primes = set(q0v) | set(av) | set(huv) | set(hvv)
        for prime in primes:
            lam = Q(q0v.get(prime, 0), r0)
            gu = Q(huv.get(prime, 0), r0)
            gv = Q(hvv.get(prime, 0), r0)
            assert Q(av.get(prime, 0)) + gv - gu == lam
            checks += 1
    return checks


def moment_residual_checks(n: int, branches: tuple[Branch, ...]) -> tuple[int, int]:
    analysis, _, _, h = powered_potentials(n, branches)
    cells = cell_map(branches)
    r0 = analysis.reference_cycle_length
    q0 = analysis.reference_cycle_product
    residual_checks = 0
    bound_checks = 0

    for source, target in analysis.critical_edges:
        weights = cells[(source, target)]
        a = max(weights)
        d = sum(weight == a for weight in weights)
        lower = tuple(weight for weight in weights if weight < a)
        theta = max((weight / a for weight in lower), default=Q(0))
        c = len(lower)
        previous_error: Fraction | None = None
        for s in (1, 2, 3):
            m = r0 * s
            wm = sum((weight**m for weight in weights), Q(0))
            direct = wm / (a**m)
            powered = (h[target] / h[source]) ** s * wm / (q0**s)
            assert direct == powered
            expected = Q(d) + sum(((weight / a) ** m for weight in lower), Q(0))
            assert direct == expected
            error = direct - d
            assert Q(0) <= error <= Q(c) * (theta**m)
            if previous_error is not None:
                assert error <= previous_error
            previous_error = error
            residual_checks += 2
            bound_checks += 2
    return residual_checks, bound_checks


def gauge_transform(branches: tuple[Branch, ...], gauge: tuple[Fraction, ...]) -> tuple[Branch, ...]:
    return tuple(
        (source, target, weight * gauge[target] / gauge[source])
        for source, target, weight in branches
    )


def gauge_covariance_checks(n: int, branches: tuple[Branch, ...]) -> int:
    analysis, _, roots, h = powered_potentials(n, branches)
    gauges = tuple(
        tuple(values[:n])
        for values in (
            (Q(2), Q(3), Q(5)),
            (Q(5, 7), Q(11, 3), Q(13, 5)),
        )
    )
    base_cells = cell_map(branches)
    checks = 0
    for gauge in gauges:
        transformed_branches = gauge_transform(branches, gauge)
        transformed, _, transformed_roots, hp = powered_potentials(n, transformed_branches)
        assert transformed.critical_edges == analysis.critical_edges
        assert transformed.critical_matrix == analysis.critical_matrix
        assert transformed.reference_cycle == analysis.reference_cycle
        assert transformed.reference_cycle_product == analysis.reference_cycle_product
        assert transformed_roots == roots
        r0 = analysis.reference_cycle_length
        for vertex, value in h.items():
            root = roots[vertex]
            assert hp[vertex] == value * (gauge[root] / gauge[vertex]) ** r0
            checks += 1

        new_cells = cell_map(transformed_branches)
        for source, target in analysis.critical_edges:
            a = max(base_cells[(source, target)])
            ap = max(new_cells[(source, target)])
            for m in (r0, 2 * r0, 3 * r0):
                old_residual = sum((q**m for q in base_cells[(source, target)]), Q(0)) / (a**m)
                new_residual = sum((q**m for q in new_cells[(source, target)]), Q(0)) / (ap**m)
                assert old_residual == new_residual
                checks += 1
    return checks


def verify_sample(n: int, branches: tuple[Branch, ...], gauge: bool = False) -> tuple[int, int, int] | None:
    try:
        analysis, _, _, h = powered_potentials(n, branches)
    except ValueError:
        return None
    edge_checks = len(analysis.critical_edges)
    valuation = valuation_checks(analysis, h)
    residual, bound = moment_residual_checks(n, branches)
    covariance = gauge_covariance_checks(n, branches) if gauge else 0
    return edge_checks + valuation, residual + bound, covariance


def exhaustive_regression() -> tuple[int, int, int]:
    samples = certificate_checks = residual_checks = 0

    catalog2 = [(), (Q(1, 4),), (Q(1, 2),), (Q(1, 2), Q(1, 2))]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for assignment in product(catalog2, repeat=4):
        branches = branches_from_cells(2, {cell: weights for cell, weights in zip(cells2, assignment) if weights})
        result = verify_sample(2, branches)
        if result is not None:
            samples += 1
            certificate_checks += result[0]
            residual_checks += result[1]

    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for assignment in product(catalog3, repeat=9):
        branches = branches_from_cells(3, {cell: weights for cell, weights in zip(cells3, assignment) if weights})
        result = verify_sample(3, branches)
        if result is not None:
            samples += 1
            certificate_checks += result[0]
            residual_checks += result[1]

    return samples, certificate_checks, residual_checks


def special_examples() -> tuple[int, int]:
    checks = covariance = 0

    # Irrational critical mean mu=1/sqrt(6), rational powered certificate.
    algebraic_mean = (
        (0, 1, Q(1, 2)),
        (1, 0, Q(1, 3)),
    )
    analysis, components, roots, h = powered_potentials(2, algebraic_mean)
    assert analysis.reference_cycle_length == 2
    assert analysis.reference_cycle_product == Q(1, 6)
    assert components == ((0, 1),)
    assert roots == {0: 0, 1: 0}
    assert h == {0: Q(1), 1: Q(2, 3)}
    checks += 5

    # Mixed critical cell gives a nonzero exact local branch gap.
    mixed = (
        (0, 0, Q(1, 2)), (0, 0, Q(1, 4)),
        (0, 1, Q(1, 2)), (0, 1, Q(1, 5)),
        (1, 0, Q(1, 2)),
        (1, 1, Q(1, 2)), (1, 1, Q(1, 7)),
    )
    result = verify_sample(2, mixed, gauge=True)
    assert result is not None
    checks += sum(result[:2])
    covariance += result[2]

    # Two disjoint critical self-loop classes share the same global mean.
    classes = (
        (0, 0, Q(1, 2)), (0, 0, Q(1, 4)),
        (1, 1, Q(1, 2)),
        (2, 2, Q(1, 2)), (2, 2, Q(1, 5)),
    )
    analysis, components, _, h = powered_potentials(3, classes)
    assert len(components) == 3
    assert all(value == 1 for value in h.values())
    assert analysis.reference_cycle_product == Q(1, 2)
    checks += 3

    return checks, covariance


def main() -> int:
    samples, certificate_checks, residual_checks = exhaustive_regression()
    special, covariance = special_examples()

    assert samples == 19823
    print("BRC critical powered rational gauge checker: PASS")
    print(f"cyclic_samples={samples}")
    print(f"powered_and_valuation_certificate_checks={certificate_checks}")
    print(f"critical_residual_and_gap_checks={residual_checks}")
    print(f"rational_gauge_covariance_checks={covariance}")
    print(f"special_checks={special}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
