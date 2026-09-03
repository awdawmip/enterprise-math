#!/usr/bin/env python3
"""Exact checker for the critical-degeneracy-matrix large-moment asymptotic.

The checker reuses the exact cycle/characteristic-expansion primitives from the
merged unique-critical experiment.  No floating eigensolver is used.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import brc_unique_critical_cycle_moment_asymptotic_check as uc

Q = Fraction


def critical_structure(n: int, edges: uc.EdgeMap):
    cycles = uc.simple_cycles(n, edges)
    critical = uc.critical_cycles(n, edges)
    if not critical:
        return None
    reference = critical[0]
    r0 = len(reference)
    q0, _ = uc.cycle_data(reference, edges)

    # Reclassify directly from the root-free rational equality.
    exact_critical = tuple(
        cycle
        for cycle in cycles
        if uc.cycle_data(cycle, edges)[0] ** r0 == q0 ** len(cycle)
    )
    assert set(exact_critical) == set(critical)

    critical_edges: set[tuple[int, int]] = set()
    for cycle in critical:
        for idx, source in enumerate(cycle):
            critical_edges.add((source, cycle[(idx + 1) % len(cycle)]))

    k_matrix = [[0 for _ in range(n)] for _ in range(n)]
    k_support: uc.EdgeMap = {}
    for source, target in sorted(critical_edges):
        cell = uc.dominant_cell(edges, source, target)
        assert cell is not None
        _, degeneracy = cell
        k_matrix[source][target] = degeneracy
        k_support[(source, target)] = (Q(1),)

    # Classical critical-graph closure property, rechecked exactly here:
    # every directed cycle using only critical edges is itself critical.
    for cycle in uc.simple_cycles(n, k_support):
        q_cycle, _ = uc.cycle_data(cycle, edges)
        assert q_cycle**r0 == q0 ** len(cycle)

    return critical, r0, q0, tuple(tuple(row) for row in k_matrix), critical_edges


def characteristic_coefficients_of_numeric_matrix(matrix: tuple[tuple[int, ...], ...]) -> dict[int, Fraction]:
    n = len(matrix)
    edges: uc.EdgeMap = {
        (i, j): (Q(matrix[i][j]),)
        for i in range(n)
        for j in range(n)
        if matrix[i][j]
    }
    exp = uc.characteristic_exponential_coefficients(n, edges)
    return {
        degree: sum((Q(coeff) * base for base, coeff in bases.items()), Q(0))
        for degree, bases in exp.items()
    }


def verify_sample(n: int, edges: uc.EdgeMap) -> tuple[int, int] | None:
    structure = critical_structure(n, edges)
    if structure is None:
        return None
    _, r0, q0, k_matrix, _ = structure
    exp = uc.characteristic_exponential_coefficients(n, edges)
    target = characteristic_coefficients_of_numeric_matrix(k_matrix)

    equality_checks = 0
    strict_ratios: list[Fraction] = []
    strict_coeff_abs_by_degree: dict[int, int] = {}

    for degree in range(n + 1):
        k = n - degree
        bases = exp.get(degree, {})
        equality_sum = 0
        for base, coeff in bases.items():
            lhs = base**r0
            rhs = q0**k
            assert lhs <= rhs
            if lhs == rhs:
                equality_sum += coeff
            else:
                if k > 0:
                    ratio = lhs / rhs
                    assert Q(0) < ratio < 1
                    strict_ratios.append(ratio)
                    strict_coeff_abs_by_degree[degree] = strict_coeff_abs_by_degree.get(degree, 0) + abs(coeff)
            equality_checks += 1
        assert Q(equality_sum) == target.get(degree, Q(0))

    eta = max(strict_ratios, default=Q(0))
    assert Q(0) <= eta < 1

    # Exact coefficient-rate bound along moment orders m=r0*s, where all
    # normalizing powers are rational and no root evaluation is needed.
    rate_checks = 0
    for s in range(1, 5):
        m = r0 * s
        for degree in range(n + 1):
            k = n - degree
            raw_coeff = sum(
                (Q(coeff) * (base**m) for base, coeff in exp.get(degree, {}).items()),
                Q(0),
            )
            normalized = raw_coeff / (q0 ** (s * k)) if k else raw_coeff
            limit = target.get(degree, Q(0))
            error = abs(normalized - limit)
            constant = strict_coeff_abs_by_degree.get(degree, 0)
            bound = Q(constant) * (eta**s)
            assert error <= bound
            rate_checks += 1

    # Direct ordinary characteristic evaluation is still reproduced exactly.
    for m in (0, 1, 2, 4):
        matrix = uc.moment_matrix(n, edges, m)
        for lam in (Q(0), Q(1, 5), Q(3, 4)):
            assert uc.evaluate_characteristic(exp, m, lam) == uc.direct_char_value(matrix, lam)
            equality_checks += 1

    return equality_checks, rate_checks


def exhaustive_regression() -> tuple[int, int, int]:
    samples = 0
    equality_checks = 0
    rate_checks = 0

    catalog2 = [(), (Q(1, 4),), (Q(1, 2),), (Q(1, 2), Q(1, 2))]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for assignment in product(catalog2, repeat=len(cells2)):
        edges = uc.normalize_edges(
            2,
            {cell: weights for cell, weights in zip(cells2, assignment) if weights},
        )
        result = verify_sample(2, edges)
        if result is not None:
            samples += 1
            equality_checks += result[0]
            rate_checks += result[1]

    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for assignment in product(catalog3, repeat=len(cells3)):
        edges = uc.normalize_edges(
            3,
            {cell: weights for cell, weights in zip(cells3, assignment) if weights},
        )
        result = verify_sample(3, edges)
        if result is not None:
            samples += 1
            equality_checks += result[0]
            rate_checks += result[1]

    return samples, equality_checks, rate_checks


def exact_perron_brackets() -> int:
    examples = [
        # Branching critical graph with unit cell degeneracy.  Correction comes
        # from critical route growth: K=ones(2x2), rho(K)=2.
        (
            2,
            uc.normalize_edges(
                2,
                {
                    (0, 0): (Q(1, 2), Q(1, 5)),
                    (0, 1): (Q(1, 2), Q(1, 4)),
                    (1, 0): (Q(1, 2), Q(1, 6)),
                    (1, 1): (Q(1, 2), Q(1, 7)),
                },
            ),
            Q(1, 2),
            Q(2),
        ),
        # Disjoint critical classes: multiplicities 1 and 3, so rho(K)=3.
        (
            2,
            uc.normalize_edges(
                2,
                {
                    (0, 0): (Q(1, 2), Q(1, 4)),
                    (1, 1): (Q(1, 2), Q(1, 2), Q(1, 2), Q(1, 5)),
                },
            ),
            Q(1, 2),
            Q(3),
        ),
        # Nonuniform critical edge weights.  Entrywise normalization does not
        # converge, but all three simple cycles are critical and K=ones(2x2).
        (
            2,
            uc.normalize_edges(
                2,
                {
                    (0, 0): (Q(1, 2),),
                    (1, 1): (Q(1, 2),),
                    (0, 1): (Q(2, 3),),
                    (1, 0): (Q(3, 8),),
                },
            ),
            Q(1, 2),
            Q(2),
        ),
    ]

    checks = 0
    for n, edges, mu, target in examples:
        structure = critical_structure(n, edges)
        assert structure is not None
        _, _, _, k_matrix, _ = structure
        k_coeff = characteristic_coefficients_of_numeric_matrix(k_matrix)
        # Check the claimed rational rho(K) by exact sign of det(tI-K).
        def k_char(value: Fraction) -> Fraction:
            return sum(coeff * (value**degree) for degree, coeff in k_coeff.items())

        assert k_char(target) == 0
        exp = uc.characteristic_exponential_coefficients(n, edges)
        for m in range(5, 13):
            scale = mu**m
            lower = scale * (target - Q(1, 10))
            upper = scale * (target + Q(1, 10))
            assert uc.evaluate_characteristic(exp, m, lower) < 0
            assert uc.evaluate_characteristic(exp, m, upper) > 0
            checks += 2
    return checks


def branching_entropy_witness() -> None:
    edges = uc.normalize_edges(
        2,
        {(i, j): (Q(1, 2),) for i in range(2) for j in range(2)},
    )
    structure = critical_structure(2, edges)
    assert structure is not None
    critical, _, _, k_matrix, _ = structure
    assert len(critical) == 3  # two self-loops and the two-state cycle
    assert k_matrix == ((1, 1), (1, 1))
    # Every individual critical state cycle has edge-degeneracy product 1,
    # while the critical multiplicity matrix has Perron correction 2.
    assert all(uc.cycle_data(cycle, edges)[1] == 1 for cycle in critical)
    k_coeff = characteristic_coefficients_of_numeric_matrix(k_matrix)
    assert sum(coeff * (Q(2) ** degree) for degree, coeff in k_coeff.items()) == 0


def main() -> int:
    samples, equality_checks, rate_checks = exhaustive_regression()
    perron_checks = exact_perron_brackets()
    branching_entropy_witness()

    assert samples > 10000
    print("BRC critical-degeneracy matrix asymptotic checker: PASS")
    print(f"cyclic_samples={samples}")
    print(f"exact_characteristic_checks={equality_checks}")
    print(f"exact_gap_rate_checks={rate_checks}")
    print(f"exact_perron_bracket_checks={perron_checks}")
    print("critical_branching_entropy=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
