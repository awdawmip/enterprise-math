"""Combinatorial branch-pattern bounds from hidden guard rank.

If a hidden guard-image lattice has rational rank d, choose any exact integer
basis of that lattice. Every guard that varies on the hidden lattice becomes one
affine hyperplane in R^d. A binary threshold pattern is constant on each
relative-open face of that hyperplane arrangement.

For q affine hyperplanes in R^d, the total number of faces is bounded by the
simple/general-position arrangement value

    F_d(q) = sum_{j=0}^{min(d,q)} 2^j * C(q,j).

Integer lattice sampling can only remove faces, and q binary guards have at most
2^q truth patterns. Therefore the reachable-pattern count is bounded by
min(2^q, F_d(q)).

This module records that standard arrangement bound as an A3 complexity tool;
it is not an originality claim about hyperplane arrangements.
"""

from __future__ import annotations

from math import comb

from .guard_image_lattice import IntMatrix, integer_matrix_rank


def arrangement_total_face_bound(hyperplane_count: int, dimension: int) -> int:
    """Maximum total face count of q affine hyperplanes in R^d.

    The formula satisfies F_d(q)=F_d(q-1)+2 F_(d-1)(q-1), with F_0(q)=1.
    """
    if (
        isinstance(hyperplane_count, bool)
        or not isinstance(hyperplane_count, int)
        or hyperplane_count < 0
    ):
        raise ValueError("hyperplane_count must be a non-negative integer")
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 0:
        raise ValueError("dimension must be a non-negative integer")
    return sum(
        (2**order) * comb(hyperplane_count, order)
        for order in range(min(dimension, hyperplane_count) + 1)
    )


def arrangement_total_face_recurrence(
    hyperplane_count: int, dimension: int
) -> tuple[int, int]:
    """Return the closed form and deletion-restriction recurrence value."""
    closed = arrangement_total_face_bound(hyperplane_count, dimension)
    if hyperplane_count == 0 or dimension == 0:
        return closed, 1
    recurrence = arrangement_total_face_bound(
        hyperplane_count - 1, dimension
    ) + 2 * arrangement_total_face_bound(
        hyperplane_count - 1, dimension - 1
    )
    return closed, recurrence


def _require_generators(generators: IntMatrix) -> int:
    if not isinstance(generators, tuple):
        raise ValueError("generators must be a tuple")
    if not generators:
        return 0
    width = len(generators[0])
    if any(not isinstance(row, tuple) or len(row) != width for row in generators):
        raise ValueError("generators must have a common width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in generators
        for value in row
    ):
        raise ValueError("generator entries must be integers")
    return width


def nonconstant_guard_count(generators: IntMatrix, guard_count: int | None = None) -> int:
    """Number of guard coordinates that actually vary on the hidden lattice."""
    width = _require_generators(generators)
    if generators:
        if guard_count is not None and guard_count != width:
            raise ValueError("guard_count does not match generator width")
        count = width
    else:
        if guard_count is None:
            raise ValueError("guard_count is required for an empty generator family")
        if isinstance(guard_count, bool) or not isinstance(guard_count, int) or guard_count < 0:
            raise ValueError("guard_count must be a non-negative integer")
        count = guard_count
    return sum(
        any(generator[index] != 0 for generator in generators)
        for index in range(count)
    )


def hidden_guard_pattern_bound(
    generators: IntMatrix, guard_count: int | None = None
) -> tuple[int, int, int, int]:
    """Return `(hidden_rank, varying_guards, face_bound, binary_bound)`.

    `face_bound` is F_d(q); `binary_bound` is the sharper min(2^q,F_d(q)).
    Constant guards contribute no branch multiplicity inside one coarse fiber.
    """
    width = _require_generators(generators)
    if generators:
        count = width
        if guard_count is not None and guard_count != width:
            raise ValueError("guard_count does not match generator width")
    else:
        if guard_count is None:
            raise ValueError("guard_count is required for an empty generator family")
        if isinstance(guard_count, bool) or not isinstance(guard_count, int) or guard_count < 0:
            raise ValueError("guard_count must be a non-negative integer")
        count = guard_count

    hidden_rank = integer_matrix_rank(generators, column_count=count)
    varying = nonconstant_guard_count(generators, guard_count=count)
    face_bound = arrangement_total_face_bound(varying, hidden_rank)
    binary_bound = min(2**varying, face_bound)
    return hidden_rank, varying, face_bound, binary_bound
