#!/usr/bin/env python3
"""Exact checker for Newton coordinate-observer and frozen-horizon lattices."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb

from enterprise_math.brc_newton_fiber_quotient import (
    NewtonFiberPosition,
    newton_fiber_coordinate,
    newton_fiber_quotient_analysis,
    newton_fiber_sum_signature,
)
from enterprise_math.brc_newton_recursion import RationalValuationScale

Q = Fraction
Scale = RationalValuationScale
ONE = Scale.one()


def s(value: Fraction | int) -> Scale:
    return Scale.from_rational(Q(value))


def rank(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row or work[r][col] == 0:
                continue
            factor = work[r][col]
            work[r] = [a - factor * b for a, b in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def source_layout():
    # Five residual coordinates with two duplicate provenance directions:
    # (1,0), (1,1), (1,2), (1/2,0), (1/2,1).
    return (
        NewtonFiberPosition(s(Q(1, 4)), 0, "edge-const-a"),
        NewtonFiberPosition(s(Q(1, 4)), 0, "edge-const-b"),
        NewtonFiberPosition(s(Q(1, 2)), 1, "edge-linear-a"),
        NewtonFiberPosition(s(Q(1, 2)), 1, "edge-linear-b"),
        NewtonFiberPosition(ONE, 2, "edge-quadratic"),
        NewtonFiberPosition(s(Q(1, 8)), 0, "strict-const"),
        NewtonFiberPosition(s(Q(1, 4)), 1, "strict-linear"),
    )


def coordinate_observer_matrix(positions, theta, multiplicity, observed):
    rows = []
    for coordinate in observed:
        rows.append([
            Q(1) if newton_fiber_coordinate(position, theta, multiplicity) == coordinate else Q(0)
            for position in positions
        ])
    return rows


def coordinate_signature(positions, coefficients, theta, multiplicity, observed):
    full = dict(newton_fiber_sum_signature(positions, coefficients, theta, multiplicity))
    return tuple((coordinate, full.get(coordinate, Q(0))) for coordinate in observed)


def coordinate_observer_lattice_checks():
    positions = source_layout()
    theta = s(Q(1, 2))
    r = 2
    analysis = newton_fiber_quotient_analysis(positions, theta, r)
    coordinates = tuple(fiber.coordinate for fiber in analysis.fibers)
    assert len(positions) == 7
    assert len(coordinates) == 5

    subsets = []
    subset_checks = 0
    for mask in range(1 << len(coordinates)):
        observer = tuple(coordinates[i] for i in range(len(coordinates)) if mask & (1 << i))
        matrix = coordinate_observer_matrix(positions, theta, r, observer)
        observed_rank = rank(matrix)
        assert observed_rank == len(observer)
        kernel_dim = len(positions) - observed_rank
        assert kernel_dim == len(positions) - len(observer)
        subsets.append(set(observer))
        subset_checks += 3

    pair_checks = 0
    for left in subsets:
        for right in subsets:
            union = left | right
            intersection = left & right
            left_matrix = coordinate_observer_matrix(positions, theta, r, tuple(left))
            right_matrix = coordinate_observer_matrix(positions, theta, r, tuple(right))
            stacked = left_matrix + right_matrix
            intersection_kernel_dim = len(positions) - rank(stacked)
            assert intersection_kernel_dim == len(positions) - len(union)

            left_kernel_dim = len(positions) - len(left)
            right_kernel_dim = len(positions) - len(right)
            sum_kernel_dim = left_kernel_dim + right_kernel_dim - intersection_kernel_dim
            assert sum_kernel_dim == len(positions) - len(intersection)

            if left <= right:
                # K_right subset K_left; dimensions reverse observer inclusion.
                assert len(positions) - len(right) <= len(positions) - len(left)
            pair_checks += 3

    # Every proper coordinate addition is genuinely observable by a unit probe.
    probe_checks = 0
    zero = tuple(Q(0) for _ in positions)
    for coordinate in coordinates:
        representative = next(
            i for i, position in enumerate(positions)
            if newton_fiber_coordinate(position, theta, r) == coordinate
        )
        unit = [Q(0) for _ in positions]
        unit[representative] = Q(1)
        without = tuple(c for c in coordinates if c != coordinate)
        assert coordinate_signature(positions, zero, theta, r, without) == coordinate_signature(
            positions, unit, theta, r, without
        )
        assert coordinate_signature(positions, zero, theta, r, (coordinate,)) != coordinate_signature(
            positions, unit, theta, r, (coordinate,)
        )
        probe_checks += 2

    edge = tuple(coordinate for coordinate in coordinates if coordinate.residual_scale == ONE)
    assert len(edge) == 3
    full_kernel_dim = len(positions) - len(coordinates)
    edge_kernel_dim = len(positions) - len(edge)
    assert full_kernel_dim == 2
    assert edge_kernel_dim == 4
    assert full_kernel_dim < edge_kernel_dim
    return len(subsets), pair_checks, subset_checks, probe_checks, full_kernel_dim, edge_kernel_dim


# A formal scheduled Newton substitution.  It is linear for fixed root,
# multiplicity and scale; it does not autonomously select them.
def scheduled_step(state, root: Fraction, multiplicity: int, theta: Scale):
    output = {}
    for (scale, degree), coefficient in state.items():
        for new_degree in range(degree + 1):
            value = coefficient * Q(comb(degree, new_degree)) * root ** (degree - new_degree)
            if value == 0:
                continue
            coordinate = (
                scale.multiply(theta.power(new_degree - multiplicity)),
                new_degree,
            )
            output[coordinate] = output.get(coordinate, Q(0)) + value
    return {coordinate: value for coordinate, value in output.items() if value}


def edge_observation(state):
    return {
        degree: value
        for (scale, degree), value in state.items()
        if scale == ONE and value
    }


def horizon_signature(state, horizon: int, root: Fraction, multiplicity: int, theta: Scale):
    signature = {}
    current = dict(state)
    for time in range(horizon + 1):
        for degree, value in edge_observation(current).items():
            signature[(time, degree)] = value
        if time < horizon:
            current = scheduled_step(current, root, multiplicity, theta)
    return signature


def observability_matrix(initial_coordinates, horizon, root, multiplicity, theta):
    columns = []
    output_keys = set()
    for coordinate in initial_coordinates:
        signature = horizon_signature({coordinate: Q(1)}, horizon, root, multiplicity, theta)
        columns.append(signature)
        output_keys.update(signature)
    rows = tuple(sorted(output_keys))
    matrix = [
        [columns[column].get(row, Q(0)) for column in range(len(initial_coordinates))]
        for row in rows
    ]
    return rows, matrix


def matrix_apply(matrix, vector):
    return tuple(sum((a * b for a, b in zip(row, vector)), Q(0)) for row in matrix)


def frozen_horizon_checks():
    theta = s(Q(1, 2))
    root = Q(-1)
    r = 2
    coordinates = (
        (ONE, 0),
        (ONE, 1),
        (ONE, 2),
        (s(Q(1, 2)), 1),
        (s(Q(1, 4)), 0),
        (s(Q(1, 16)), 0),
    )

    ranks = []
    matrices = []
    rowsets = []
    for horizon in range(3):
        rows, matrix = observability_matrix(coordinates, horizon, root, r, theta)
        observed_rank = rank(matrix)
        ranks.append(observed_rank)
        matrices.append(matrix)
        rowsets.append(rows)
    assert ranks == [3, 5, 6]
    kernel_dims = [len(coordinates) - value for value in ranks]
    assert kernel_dims == [3, 1, 0]

    # Strict future witnesses.
    now_invisible = [Q(0)] * len(coordinates)
    now_invisible[3] = Q(1)  # (1/2,1): visible after one scheduled step.
    assert matrix_apply(matrices[0], now_invisible) == tuple(Q(0) for _ in matrices[0])
    assert any(matrix_apply(matrices[1], now_invisible))

    two_step_only = [Q(0)] * len(coordinates)
    two_step_only[5] = Q(1)  # (1/16,0): first visible at horizon two.
    assert matrix_apply(matrices[1], two_step_only) == tuple(Q(0) for _ in matrices[1])
    assert any(matrix_apply(matrices[2], two_step_only))

    # Exhaust a finite rational coefficient catalog and compare stacked matrix
    # evaluation with direct scheduled substitution.
    catalog_checks = 0
    rows2 = rowsets[2]
    matrix2 = matrices[2]
    for values in product((Q(-1), Q(0), Q(1)), repeat=len(coordinates)):
        state = {
            coordinate: value
            for coordinate, value in zip(coordinates, values)
            if value
        }
        direct = horizon_signature(state, 2, root, r, theta)
        expected = tuple(direct.get(row, Q(0)) for row in rows2)
        assert matrix_apply(matrix2, values) == expected
        catalog_checks += 1

    # Exact linearity of each scheduled substitution on a small pair catalog.
    linearity_checks = 0
    basis_states = [
        {coordinate: Q(1)} for coordinate in coordinates
    ]
    for left, right in product(basis_states, repeat=2):
        combined = dict(left)
        for coordinate, value in right.items():
            combined[coordinate] = combined.get(coordinate, Q(0)) + value
        lhs = scheduled_step(combined, root, r, theta)
        l = scheduled_step(left, root, r, theta)
        rr = scheduled_step(right, root, r, theta)
        rhs = dict(l)
        for coordinate, value in rr.items():
            rhs[coordinate] = rhs.get(coordinate, Q(0)) + value
        rhs = {coordinate: value for coordinate, value in rhs.items() if value}
        assert lhs == rhs
        linearity_checks += 1

    return tuple(ranks), tuple(kernel_dims), catalog_checks, linearity_checks


def main() -> int:
    subsets, pair_checks, subset_checks, probes, full_dim, edge_dim = coordinate_observer_lattice_checks()
    ranks, kernel_dims, catalog, linearity = frozen_horizon_checks()
    print("BRC Newton observer lattice checker: PASS")
    print(f"coordinate_observer_subsets={subsets}")
    print(f"coordinate_subset_rank_checks={subset_checks}")
    print(f"observer_pair_lattice_checks={pair_checks}")
    print(f"coordinate_probe_strictness_checks={probes}")
    print(f"full_residual_kernel_dimension={full_dim}")
    print(f"edge_only_kernel_dimension={edge_dim}")
    print(f"frozen_horizon_ranks={ranks}")
    print(f"frozen_horizon_kernel_dimensions={kernel_dims}")
    print(f"frozen_horizon_catalog_checks={catalog}")
    print(f"scheduled_step_linearity_checks={linearity}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
