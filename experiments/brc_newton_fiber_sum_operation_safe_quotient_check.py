#!/usr/bin/env python3
"""Exact checker for the Newton residual fiber-sum quotient."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb

from enterprise_math.brc_newton_handoff import rational_newton_pushforward
from enterprise_math.brc_newton_recursion import RationalValuationScale, rational_newton_step

Q = Fraction
Scale = RationalValuationScale
Coordinate = tuple[Scale, int]
ONE = Scale.one()


@dataclass(frozen=True)
class AtomPosition:
    label: str
    source_scale: Scale
    degree: int


@dataclass(frozen=True)
class SourceAtom:
    position: AtomPosition
    coefficient: Fraction


def source_scale(value) -> Scale:
    return Scale.from_rational(Q(value))


def residual_coordinate(position: AtomPosition, theta: Scale, multiplicity: int) -> Coordinate:
    return (
        position.source_scale.multiply(theta.power(position.degree - multiplicity)),
        position.degree,
    )


def fiber_partition(positions: tuple[AtomPosition, ...], theta: Scale, multiplicity: int):
    fibers: dict[Coordinate, list[int]] = {}
    for index, position in enumerate(positions):
        fibers.setdefault(residual_coordinate(position, theta, multiplicity), []).append(index)
    return {coordinate: tuple(indices) for coordinate, indices in fibers.items()}


def fiber_sum(
    positions: tuple[AtomPosition, ...],
    coefficients: tuple[Fraction, ...],
    theta: Scale,
    multiplicity: int,
):
    if len(positions) != len(coefficients):
        raise ValueError("position/coefficient length mismatch")
    out: dict[Coordinate, Fraction] = {}
    for position, coefficient in zip(positions, coefficients):
        coordinate = residual_coordinate(position, theta, multiplicity)
        out[coordinate] = out.get(coordinate, Q(0)) + coefficient
    return {coordinate: value for coordinate, value in out.items() if value != 0}


def polynomial_from_taylor_atom(root: Fraction, degree: int, coefficient: Fraction):
    # coefficient * (x-root)^degree, so its only nonzero Taylor coefficient
    # at x=root is exactly the requested coefficient in the requested degree.
    values = [Q(0) for _ in range(degree + 1)]
    for k in range(degree + 1):
        values[k] = coefficient * Q(comb(degree, k)) * ((-root) ** (degree - k))
    return tuple(values)


def production_source_jet(
    positions: tuple[AtomPosition, ...],
    coefficients: tuple[Fraction, ...],
    root: Fraction,
    multiplicity: int,
):
    # Keep the scale-one base polynomial unique.  Every provenance atom is a
    # separate strict jet entry, which lets T55 diagnostics retain its source
    # label while the transformed step aggregates by residual coordinate.
    base = polynomial_from_taylor_atom(root, multiplicity, Q(1))
    jet = [(ONE, base)]
    for position, coefficient in zip(positions, coefficients):
        if coefficient == 0:
            continue
        jet.append(
            (
                position.source_scale,
                polynomial_from_taylor_atom(root, position.degree, coefficient),
            )
        )
    return tuple(jet)


def residual_from_production(analysis):
    out = {}
    for fiber in analysis.fibers:
        for degree, coefficient in enumerate(fiber.polynomial):
            if coefficient:
                out[(fiber.residual_scale, degree)] = coefficient
    return out


def layout():
    # Duplicate A/B positions create two nontrivial provenance fibers.  C/D
    # have the same residual scale but different Taylor degree, while B/C have
    # the same Taylor degree but different residual scale.
    return (
        AtomPosition("A1", source_scale(Q(1, 2)), 1),
        AtomPosition("A2", source_scale(Q(1, 2)), 1),
        AtomPosition("B1", source_scale(Q(1, 4)), 0),
        AtomPosition("B2", source_scale(Q(1, 4)), 0),
        AtomPosition("C", source_scale(Q(1, 8)), 0),
        AtomPosition("D", source_scale(Q(1, 4)), 1),
        AtomPosition("E", source_scale(Q(1, 16)), 0),
    )


def matrix_rank(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
    m, n = len(rows), len(rows[0])
    rank = column = 0
    while rank < m and column < n:
        pivot = next((row for row in range(rank, m) if rows[row][column] != 0), None)
        if pivot is None:
            column += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        p = rows[rank][column]
        rows[rank] = [value / p for value in rows[rank]]
        for row in range(m):
            if row == rank or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [a - factor * b for a, b in zip(rows[row], rows[rank])]
        rank += 1
        column += 1
    return rank


def quotient_matrix(positions, theta, multiplicity):
    fibers = fiber_partition(positions, theta, multiplicity)
    coordinates = tuple(fibers)
    index = {coordinate: row for row, coordinate in enumerate(coordinates)}
    matrix = [[Q(0) for _ in positions] for _ in coordinates]
    for column, position in enumerate(positions):
        matrix[index[residual_coordinate(position, theta, multiplicity)]][column] = Q(1)
    return coordinates, matrix


def exact_rank_and_kernel_checks():
    positions = layout()
    theta = source_scale(Q(1, 2))
    r = 2
    fibers = fiber_partition(positions, theta, r)
    coordinates, matrix = quotient_matrix(positions, theta, r)
    rank = matrix_rank(matrix)
    assert rank == len(coordinates) == len(fibers)
    assert len(positions) - rank == sum(len(indices) - 1 for indices in fibers.values())

    # Exhaust zero-fiber-sum differences on every nontrivial fiber and verify
    # the anchor-transfer decomposition exactly.
    decomposition_checks = 0
    for coordinate, indices in fibers.items():
        if len(indices) <= 1:
            continue
        anchor = indices[0]
        others = indices[1:]
        for values in product((Q(-2), Q(-1), Q(0), Q(1), Q(2)), repeat=len(others)):
            vector = [Q(0) for _ in positions]
            for index, value in zip(others, values):
                vector[index] = value
            vector[anchor] = -sum(values, Q(0))
            assert fiber_sum(positions, tuple(vector), theta, r) == {}

            reconstructed = [Q(0) for _ in positions]
            for index in others:
                value = vector[index]
                reconstructed[index] += value
                reconstructed[anchor] -= value
            assert reconstructed == vector
            decomposition_checks += 1
    return rank, len(positions) - rank, decomposition_checks


def transfer_invariance_regression():
    positions = layout()
    theta = source_scale(Q(1, 2))
    root, r = Q(1), 2
    # Permanent B sum=1 ensures the selected Newton scale stays 1/2 even when
    # A provenance is redistributed.
    base_coefficients = (Q(1), Q(1), Q(2), Q(-1), Q(3), Q(4), Q(-2))
    expected = fiber_sum(positions, base_coefficients, theta, r)
    checks = future_checks = 0

    # Move rational coefficient between duplicate A and B provenance labels.
    for delta_a, delta_b in product((Q(-3), Q(-1), Q(0), Q(2), Q(5)), repeat=2):
        coefficients = list(base_coefficients)
        coefficients[0] += delta_a
        coefficients[1] -= delta_a
        coefficients[2] += delta_b
        coefficients[3] -= delta_b
        current = tuple(coefficients)
        assert fiber_sum(positions, current, theta, r) == expected

        analysis = rational_newton_pushforward(production_source_jet(positions, current, root, r), root, r)
        assert analysis.step.scale == theta
        production = residual_from_production(analysis)
        # Add the scale-one base contribution y^2 to the independent Pi table.
        independent = dict(expected)
        independent[(ONE, r)] = independent.get((ONE, r), Q(0)) + Q(1)
        assert production == independent
        checks += len(production) + 2

        # The downstream edge is y^2+2y+1=(y+1)^2 for every redistribution.
        self_edge = {key: value for key, value in production.items() if key[0] == ONE}
        assert self_edge[(ONE, 0)] == 1 and self_edge[(ONE, 1)] == 2 and self_edge[(ONE, 2)] == 1
        next_step = rational_newton_step(analysis.step.jet, Q(-1), 2)
        if delta_a == 0 and delta_b == 0:
            reference_next = next_step
        else:
            assert next_step.scale == reference_next.scale
            assert next_step.jet == reference_next.jet
            assert next_step.edge_polynomial == reference_next.edge_polynomial
        future_checks += 3
    return checks, future_checks


def coordinate_probe_and_no_merge_checks():
    positions = layout()
    theta = source_scale(Q(1, 2))
    r = 2
    zero = tuple(Q(0) for _ in positions)
    base = fiber_sum(positions, zero, theta, r)
    assert base == {}
    probes = 0
    for index in range(len(positions)):
        vector = [Q(0) for _ in positions]
        vector[index] = Q(1)
        observed = fiber_sum(positions, tuple(vector), theta, r)
        coordinate = residual_coordinate(positions[index], theta, r)
        assert observed == {coordinate: Q(1)}
        probes += 1

    # Same residual scale rho=1/2, but degrees 0 and 1.  They must not merge:
    # y^0 changes the edge/contact polynomial differently from y^1.
    c = residual_coordinate(positions[4], theta, r)
    d = residual_coordinate(positions[5], theta, r)
    assert c[0] == d[0] and c[1] != d[1]

    # Same degree 0 but different residual scales 1 and 1/2.
    b = residual_coordinate(positions[2], theta, r)
    assert b[1] == c[1] and b[0] != c[0]
    return probes + 4


def splitting_relabeling_checks():
    theta = source_scale(Q(1, 2))
    r = 2
    one = (AtomPosition("X", source_scale(Q(1, 8)), 0),)
    split = (
        AtomPosition("X1", source_scale(Q(1, 8)), 0),
        AtomPosition("X2", source_scale(Q(1, 8)), 0),
    )
    original = fiber_sum(one, (Q(7),), theta, r)
    for left in (Q(-4), Q(0), Q(2), Q(10)):
        right = Q(7) - left
        assert fiber_sum(split, (left, right), theta, r) == original
    reversed_split = tuple(reversed(split))
    assert fiber_sum(reversed_split, (Q(3), Q(4)), theta, r) == original
    return 5


def edge_only_is_coarser_witness():
    positions = layout()
    theta = source_scale(Q(1, 2))
    r = 2
    a = (Q(1), Q(1), Q(2), Q(-1), Q(3), Q(4), Q(0))
    b = list(a)
    b[6] = Q(9)  # only rho=1/4, degree 0 changes
    full_a = fiber_sum(positions, a, theta, r)
    full_b = fiber_sum(positions, tuple(b), theta, r)
    assert full_a != full_b
    edge_a = {coordinate: value for coordinate, value in full_a.items() if coordinate[0] == ONE}
    edge_b = {coordinate: value for coordinate, value in full_b.items() if coordinate[0] == ONE}
    assert edge_a == edge_b
    return 2


def production_source_split_checks():
    # Directly compare two different provenance splittings through T55.
    root, r = Q(1), 2
    positions_a = (
        AtomPosition("A", source_scale(Q(1, 2)), 1),
        AtomPosition("B", source_scale(Q(1, 4)), 0),
        AtomPosition("C", source_scale(Q(1, 8)), 0),
    )
    coeffs_a = (Q(2), Q(1), Q(3))
    positions_b = (
        AtomPosition("A1", source_scale(Q(1, 2)), 1),
        AtomPosition("A2", source_scale(Q(1, 2)), 1),
        AtomPosition("B1", source_scale(Q(1, 4)), 0),
        AtomPosition("B2", source_scale(Q(1, 4)), 0),
        AtomPosition("C", source_scale(Q(1, 8)), 0),
    )
    coeffs_b = (Q(5), Q(-3), Q(7), Q(-6), Q(3))
    theta = source_scale(Q(1, 2))
    assert fiber_sum(positions_a, coeffs_a, theta, r) == fiber_sum(positions_b, coeffs_b, theta, r)
    result_a = rational_newton_pushforward(production_source_jet(positions_a, coeffs_a, root, r), root, r)
    result_b = rational_newton_pushforward(production_source_jet(positions_b, coeffs_b, root, r), root, r)
    assert result_a.step.jet == result_b.step.jet
    assert result_a.step.edge_polynomial == result_b.step.edge_polynomial
    # Diagnostic source atoms differ: quotient preserves semantics, not provenance.
    assert tuple(len(fiber.atoms) for fiber in result_a.fibers) != tuple(len(fiber.atoms) for fiber in result_b.fibers)
    return 4


def main() -> int:
    rank, kernel_dim, decomposition = exact_rank_and_kernel_checks()
    transfer, future = transfer_invariance_regression()
    probes = coordinate_probe_and_no_merge_checks()
    splitting = splitting_relabeling_checks()
    edge_only = edge_only_is_coarser_witness()
    production_split = production_source_split_checks()
    print("BRC Newton fiber-sum operation-safe quotient checker: PASS")
    print(f"observer_rank={rank}")
    print(f"kernel_dimension={kernel_dim}")
    print(f"kernel_transfer_decomposition_checks={decomposition}")
    print(f"transfer_invariance_checks={transfer}")
    print(f"downstream_newton_future_checks={future}")
    print(f"coordinate_probe_no_merge_checks={probes}")
    print(f"splitting_relabeling_checks={splitting}")
    print(f"edge_only_coarser_witness_checks={edge_only}")
    print(f"production_provenance_split_checks={production_split}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
