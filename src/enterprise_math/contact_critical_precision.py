"""Critical-group denominator for exact contact cut/cycle decomposition.

For a connected contact graph with signed incidence ``B`` and integer edge
history ``j``, the coarse body change is ``b=Bj``.  Over the rationals one may
split the edge history into a potential/cut part plus a cycle part by solving

    L phi = b,             L = B B^T,

and writing

    j = B^T phi + z,       B z = 0.

Over the integer lattice an integral potential need not exist.  Fix one root
vertex and delete its Laplacian row/column.  The reduced Laplacian ``L_r`` is
invertible over Q.  The least common denominator ``s`` of the unique rational
solution

    L_r phi_r = b_r

is exactly the order of the physical body-delta class in the graph critical
group

    im_Z(B) / im_Z(L).

Indeed ``s phi_r`` is integral, so ``s b`` lies in the integer Laplacian image;
conversely any ``t`` with ``t b`` in that image forces ``t phi_r`` integral by
uniqueness, hence ``s|t``.

Thus ``s`` is the minimum precision denominator required by this particular
potential/cycle representation.  It is one exactly when an integer
potential-derived representative exists modulo an integer cycle.

The module returns the exact common-denominator decomposition

    s*j = cut_numerator + cycle_numerator,

with

    cut_numerator = B^T potential_numerator,
    B*cycle_numerator = 0.

The denominator divides the spanning-tree count ``det(L_r)``.  For the cycle
graph ``C_n`` and a unit impulse on one edge, ``s=n`` and

    e_0 = (1/n) * ((n-1,-1,...,-1) + (1,1,...,1)).

Graph critical groups, the matrix-tree theorem and rational Hodge decomposition
are standard prior mathematics.  The Enterprise Math value is the exact
precision interpretation and its separation from cycle-history ambiguity.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Sequence

from .contact_cycle_witness_repair import (
    apply_integer_matrix,
    fundamental_cycle_lattice,
)


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _incidence(
    values: Sequence[Sequence[int]],
) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    lattice = fundamental_cycle_lattice(rows)
    if lattice.component_count != 1:
        raise ValueError("critical precision currently requires a connected graph")
    return rows


def _vector(
    values: Sequence[int],
    length: int,
    *,
    name: str,
) -> Vector:
    result = tuple(values)
    if len(result) != length:
        raise ValueError(f"{name} must have length {length}")
    for value in result:
        _require_int(name, value)
    return result


def _lcm(left: int, right: int) -> int:
    if left <= 0 or right <= 0:
        raise ValueError("lcm inputs must be positive")
    return abs(left * right) // gcd(left, right)


def contact_graph_laplacian(
    incidence: Sequence[Sequence[int]],
) -> Matrix:
    """Return the integer vertex Laplacian ``B B^T``."""
    matrix = _incidence(incidence)
    body_count = len(matrix)
    edge_count = len(matrix[0])
    return tuple(
        tuple(
            sum(
                matrix[left][edge] * matrix[right][edge]
                for edge in range(edge_count)
            )
            for right in range(body_count)
        )
        for left in range(body_count)
    )


def _reduced_matrix(
    matrix: Matrix,
    root: int,
) -> tuple[Matrix, tuple[int, ...]]:
    size = len(matrix)
    _require_int("root", root)
    if not 0 <= root < size:
        raise ValueError("root is outside the vertex set")
    keep = tuple(index for index in range(size) if index != root)
    reduced = tuple(
        tuple(matrix[row][column] for column in keep)
        for row in keep
    )
    return reduced, keep


def _bareiss_determinant(matrix: Matrix) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    previous = 1

    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            replacement = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if work[row][pivot_index] != 0
                ),
                None,
            )
            if replacement is None:
                return 0
            work[pivot_index], work[replacement] = (
                work[replacement],
                work[pivot_index],
            )
            sign *= -1

        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index]
                    * work[pivot_index][column]
                )
                if numerator % previous != 0:
                    raise AssertionError("Bareiss division lost exactness")
                work[row][column] = numerator // previous
            work[row][pivot_index] = 0
        previous = pivot

    return sign * work[-1][-1]


def _solve_fraction(
    matrix: Matrix,
    right_hand_side: Vector,
) -> tuple[Fraction, ...]:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("linear solve requires a square matrix")
    if len(right_hand_side) != size:
        raise ValueError("right-hand side dimension mismatch")
    augmented = [
        [Fraction(value) for value in row]
        + [Fraction(right_hand_side[index])]
        for index, row in enumerate(matrix)
    ]

    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if augmented[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            raise ValueError("reduced Laplacian is singular")
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        pivot_value = augmented[column][column]
        augmented[column] = [
            value / pivot_value
            for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor == 0:
                continue
            augmented[row] = [
                left - factor * right
                for left, right in zip(
                    augmented[row],
                    augmented[column],
                    strict=True,
                )
            ]

    return tuple(augmented[row][-1] for row in range(size))


def _transpose_times_vector(
    incidence: Matrix,
    vertex_vector: Vector,
) -> Vector:
    edge_count = len(incidence[0])
    return tuple(
        sum(
            incidence[body][edge] * vertex_vector[body]
            for body in range(len(incidence))
        )
        for edge in range(edge_count)
    )


@dataclass(frozen=True)
class ContactCriticalPrecisionReport:
    root: int
    spanning_tree_count: int
    critical_class_order: int
    body_delta: Vector
    potential_numerators: Vector
    potential_denominator: int
    cut_numerators: Vector
    cycle_numerators: Vector

    @property
    def integer_potential_representative_exists(self) -> bool:
        return self.critical_class_order == 1

    @property
    def requires_precision_refinement(self) -> bool:
        return self.critical_class_order > 1


def contact_critical_precision_report(
    incidence: Sequence[Sequence[int]],
    impulse_history: Sequence[int],
    *,
    root: int | None = None,
) -> ContactCriticalPrecisionReport:
    """Return the minimum-denominator cut/cycle decomposition of one history."""
    matrix = _incidence(incidence)
    body_count = len(matrix)
    edge_count = len(matrix[0])
    history = _vector(
        impulse_history,
        edge_count,
        name="impulse_history",
    )
    if root is None:
        root = body_count - 1
    _require_int("root", root)
    if not 0 <= root < body_count:
        raise ValueError("root is outside the vertex set")

    body_delta = apply_integer_matrix(matrix, history)
    if sum(body_delta) != 0:
        raise AssertionError("incidence body delta must have zero total")

    laplacian = contact_graph_laplacian(matrix)
    reduced_laplacian, keep = _reduced_matrix(laplacian, root)
    spanning_tree_count = abs(_bareiss_determinant(reduced_laplacian))
    if spanning_tree_count <= 0:
        raise AssertionError("connected graph must have positive reduced determinant")

    reduced_delta = tuple(body_delta[index] for index in keep)
    reduced_potential = _solve_fraction(
        reduced_laplacian,
        reduced_delta,
    )

    denominator = 1
    for value in reduced_potential:
        denominator = _lcm(denominator, value.denominator)

    potential_numerators_list = [0] * body_count
    for index, value in zip(keep, reduced_potential, strict=True):
        scaled = value * denominator
        if scaled.denominator != 1:
            raise AssertionError("common denominator failed to integralize potential")
        potential_numerators_list[index] = scaled.numerator
    potential_numerators = tuple(potential_numerators_list)

    common = denominator
    for value in potential_numerators:
        common = gcd(common, abs(value))
    if common != 1:
        raise AssertionError("reported potential denominator was not minimal")

    cut_numerators = _transpose_times_vector(
        matrix,
        potential_numerators,
    )
    cycle_numerators = tuple(
        denominator * impulse - cut
        for impulse, cut in zip(
            history,
            cut_numerators,
            strict=True,
        )
    )

    if apply_integer_matrix(matrix, cut_numerators) != tuple(
        denominator * value
        for value in body_delta
    ):
        raise AssertionError("cut numerator failed to reproduce scaled body delta")
    if any(apply_integer_matrix(matrix, cycle_numerators)):
        raise AssertionError("cycle numerator left the incidence kernel")
    if tuple(
        cut + cycle
        for cut, cycle in zip(
            cut_numerators,
            cycle_numerators,
            strict=True,
        )
    ) != tuple(denominator * value for value in history):
        raise AssertionError("cut/cycle numerator decomposition lost the edge history")

    if spanning_tree_count % denominator != 0:
        raise AssertionError("critical class order must divide the critical group order")

    return ContactCriticalPrecisionReport(
        root=root,
        spanning_tree_count=spanning_tree_count,
        critical_class_order=denominator,
        body_delta=body_delta,
        potential_numerators=potential_numerators,
        potential_denominator=denominator,
        cut_numerators=cut_numerators,
        cycle_numerators=cycle_numerators,
    )
