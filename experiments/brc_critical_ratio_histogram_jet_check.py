#!/usr/bin/env python3
"""Exact checker for gauge-invariant critical ratio histograms and finite jets."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product

from enterprise_math.brc_critical_degeneracy import critical_degeneracy_analysis
from enterprise_math.brc_rational_holonomy import rational_from_prime_valuations, rational_prime_valuations

Q = Fraction
Branch = tuple[int, int, Fraction]
Matrix = tuple[tuple[int, ...], ...]


def branches_from_assignment(n, cells, assignment):
    return tuple(
        (source, target, weight)
        for (source, target), weights in zip(cells, assignment)
        for weight in weights
    )


def grouped(branches):
    out = {}
    for source, target, weight in branches:
        out.setdefault((source, target), []).append(weight)
    return {cell: tuple(values) for cell, values in out.items()}


def ratio_jet(n: int, branches: tuple[Branch, ...]):
    analysis = critical_degeneracy_analysis(n, branches)
    cells = grouped(branches)
    histograms: dict[tuple[int, int], Counter[Fraction]] = {}
    ratios: set[Fraction] = set()
    for edge in analysis.critical_edges:
        weights = cells[edge]
        maximum = max(weights)
        hist = Counter(weight / maximum for weight in weights)
        assert max(hist) == 1
        histograms[edge] = hist
        ratios.update(hist)
    theta = tuple(sorted(ratios, reverse=True))
    assert theta and theta[0] == 1
    layers = []
    for ratio in theta:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for (source, target), hist in histograms.items():
            matrix[source][target] = hist.get(ratio, 0)
        layers.append(tuple(tuple(row) for row in matrix))
    assert layers[0] == analysis.critical_matrix
    return analysis, histograms, theta, tuple(layers)


def moment_residual(n: int, branches: tuple[Branch, ...], critical_edges, m: int):
    cells = grouped(branches)
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for source, target in critical_edges:
        weights = cells[(source, target)]
        maximum = max(weights)
        out[source][target] = sum((weight ** m for weight in weights), Q(0)) / (maximum ** m)
    return tuple(tuple(row) for row in out)


def jet_moment(theta, layers, m: int):
    n = len(layers[0])
    return tuple(
        tuple(sum((ratio**m) * layers[k][i][j] for k, ratio in enumerate(theta)) for j in range(n))
        for i in range(n)
    )


def denominator(theta):
    coeffs = [Q(1)]
    for ratio in theta:
        new = [Q(0)] * (len(coeffs) + 1)
        for i, value in enumerate(coeffs):
            new[i] += value
            new[i + 1] -= value * ratio
        coeffs = new
    return tuple(coeffs)


def recurrence_checks(theta, layers, upto_extra=6):
    degree = len(theta)
    denom = denominator(theta)
    sequence = [jet_moment(theta, layers, m) for m in range(degree + upto_extra + 1)]
    n = len(layers[0])
    checks = 0
    for m in range(degree, len(sequence)):
        for i in range(n):
            for j in range(n):
                value = sum(denom[k] * sequence[m-k][i][j] for k in range(degree + 1))
                assert value == 0
                checks += 1
    return checks


def validate_sample(n: int, branches: tuple[Branch, ...]):
    try:
        analysis, histograms, theta, layers = ratio_jet(n, branches)
    except ValueError:
        return None
    exact = tail = valuation = 0

    # Exact histogram reconstruction from the finite ratio jet.
    for (source, target), hist in histograms.items():
        reconstructed = Counter({ratio: layers[k][source][target] for k, ratio in enumerate(theta) if layers[k][source][target]})
        assert reconstructed == hist
        exact += len(hist)

    # Every integer moment is an exact finite exponential sum.
    for m in range(0, 9):
        direct = moment_residual(n, branches, analysis.critical_edges, m)
        via_jet = jet_moment(theta, layers, m)
        assert direct == via_jet
        exact += n * n

        # All truncation levels have exact entrywise nonnegative tail bounds.
        for t in range(len(theta) - 1):
            partial = jet_moment(theta[: t + 1], layers[: t + 1], m)
            next_ratio = theta[t + 1]
            for i in range(n):
                for j in range(n):
                    error = direct[i][j] - partial[i][j]
                    tail_count = sum(layers[k][i][j] for k in range(t + 1, len(theta)))
                    assert Q(0) <= error <= (next_ratio**m) * tail_count
                    tail += 1

    # Prime-valuation exact round trips for every ratio.
    for ratio in theta:
        coords = rational_prime_valuations(ratio)
        assert rational_from_prime_valuations(coords) == ratio
        valuation += 1

    recurrence = recurrence_checks(theta, layers)
    return exact, tail, valuation, recurrence, len(theta)


def exhaustive_regression():
    samples = exact = tail = valuation = recurrence = multilayer = 0

    # Structural 3-state catalog from PR #1167.
    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for assignment in product(catalog3, repeat=9):
        result = validate_sample(3, branches_from_assignment(3, cells3, assignment))
        if result is None:
            continue
        samples += 1
        exact += result[0]
        tail += result[1]
        valuation += result[2]
        recurrence += result[3]

    # Enriched 2-state catalog with genuine multiple subdominant ratio layers.
    catalog2 = [
        (),
        (Q(1, 4),),
        (Q(1, 2),),
        (Q(1, 2), Q(1, 4)),
        (Q(1, 2), Q(1, 3), Q(1, 4)),
    ]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for assignment in product(catalog2, repeat=4):
        result = validate_sample(2, branches_from_assignment(2, cells2, assignment))
        if result is None:
            continue
        samples += 1
        exact += result[0]
        tail += result[1]
        valuation += result[2]
        recurrence += result[3]
        if result[4] >= 3:
            multilayer += 1

    return samples, exact, tail, valuation, recurrence, multilayer


def gauge_transform(branches, gauge):
    return tuple((u, v, q * gauge[v] / gauge[u]) for u, v, q in branches)


def gauge_examples():
    examples = (
        (
            2,
            (
                (0, 0, Q(1, 2)), (0, 0, Q(1, 3)), (0, 0, Q(1, 4)),
                (0, 1, Q(1, 2)), (0, 1, Q(1, 4)),
                (1, 0, Q(1, 2)),
                (1, 1, Q(1, 2)), (1, 1, Q(1, 5)),
            ),
        ),
        (
            3,
            (
                (0, 1, Q(2, 3)), (0, 1, Q(1, 3)), (0, 1, Q(1, 6)),
                (1, 2, Q(3, 5)), (1, 2, Q(1, 5)),
                (2, 0, Q(5, 8)), (2, 0, Q(5, 16)),
            ),
        ),
    )
    gauges = ((Q(2), Q(3), Q(5)), (Q(5, 7), Q(11, 3), Q(13, 5)))
    checks = 0
    for n, branches in examples:
        base = ratio_jet(n, branches)
        for gauge in gauges:
            transformed = ratio_jet(n, gauge_transform(branches, gauge[:n]))
            assert transformed[0].critical_edges == base[0].critical_edges
            assert transformed[0].critical_matrix == base[0].critical_matrix
            assert transformed[1] == base[1]
            assert transformed[2] == base[2]
            assert transformed[3] == base[3]
            checks += 5
    return checks


def strict_boundaries():
    # Same leading K=1, different subdominant ratio shape.
    a = ((0, 0, Q(1, 2)), (0, 0, Q(1, 4)))
    b = ((0, 0, Q(1, 2)), (0, 0, Q(1, 6)))
    ja = ratio_jet(1, a)
    jb = ratio_jet(1, b)
    assert ja[0].critical_matrix == jb[0].critical_matrix == ((1,),)
    assert ja[2:] != jb[2:]
    assert moment_residual(1, a, ja[0].critical_edges, 2) != moment_residual(1, b, jb[0].critical_edges, 2)

    # Three genuine layers in one critical cell: 1, 2/3, 1/2.
    c = ((0, 0, Q(1, 2)), (0, 0, Q(1, 3)), (0, 0, Q(1, 4)))
    jc = ratio_jet(1, c)
    assert jc[2] == (Q(1), Q(2, 3), Q(1, 2))
    assert tuple(layer[0][0] for layer in jc[3]) == (1, 1, 1)
    return 5


def main():
    samples, exact, tail, valuation, recurrence, multilayer = exhaustive_regression()
    gauge = gauge_examples()
    boundaries = strict_boundaries()

    assert samples > 19000
    assert multilayer > 0
    print("BRC critical ratio histogram finite-jet checker: PASS")
    print(f"cyclic_samples={samples}")
    print(f"exact_histogram_and_moment_checks={exact}")
    print(f"finite_tail_bound_checks={tail}")
    print(f"prime_valuation_ratio_checks={valuation}")
    print(f"moment_order_recurrence_checks={recurrence}")
    print(f"genuine_multilayer_samples={multilayer}")
    print(f"rational_gauge_invariance_checks={gauge}")
    print(f"strict_boundary_checks={boundaries}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
