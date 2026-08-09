"""Independent product construction for integer causal future systems.

For two integer-linear causal subsystems, the independent product uses block
separation: operations act within their own state blocks and observations read
one subsystem at a time.  Future distinguishability then factorizes, so the
causal-visible rank is additive.

This module is a concrete integer specialization of the more general signature
law Sigma_(A x B) = (Sigma_A, Sigma_B).
"""

from __future__ import annotations

from .causal_future_module import Matrix, RowFamily, causal_future_closure


Vector = tuple[int, ...]


def _require_square(matrix: Matrix) -> int:
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError("matrix must be a non-empty tuple")
    size = len(matrix)
    if any(not isinstance(row, tuple) or len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in matrix
        for value in row
    ):
        raise ValueError("matrix entries must be integers")
    return size


def block_diagonal(left: Matrix, right: Matrix) -> Matrix:
    """Independent product of two integer operations."""
    left_size = _require_square(left)
    right_size = _require_square(right)
    rows = []
    for row in left:
        rows.append(tuple(row) + tuple(0 for _ in range(right_size)))
    for row in right:
        rows.append(tuple(0 for _ in range(left_size)) + tuple(row))
    return tuple(rows)


def lift_left_observations(observations: RowFamily, right_size: int) -> RowFamily:
    if not isinstance(right_size, int) or isinstance(right_size, bool) or right_size <= 0:
        raise ValueError("right_size must be a positive integer")
    if not isinstance(observations, tuple) or not observations:
        raise ValueError("observations must be a non-empty tuple")
    return tuple(tuple(row) + tuple(0 for _ in range(right_size)) for row in observations)


def lift_right_observations(observations: RowFamily, left_size: int) -> RowFamily:
    if not isinstance(left_size, int) or isinstance(left_size, bool) or left_size <= 0:
        raise ValueError("left_size must be a positive integer")
    if not isinstance(observations, tuple) or not observations:
        raise ValueError("observations must be a non-empty tuple")
    return tuple(tuple(0 for _ in range(left_size)) + tuple(row) for row in observations)


def independent_product_operations(
    left_operations: tuple[Matrix, ...],
    right_operations: tuple[Matrix, ...],
) -> tuple[Matrix, ...]:
    """Synchronous independent product operation family.

    Every declared left operation is paired with every declared right operation.
    If one side needs an idle step, include the identity operation explicitly in
    that subsystem's operation family.
    """
    if not left_operations or not right_operations:
        raise ValueError("both operation families must be non-empty")
    return tuple(
        block_diagonal(left, right)
        for left in left_operations
        for right in right_operations
    )


def independent_product_observations(
    left_observations: RowFamily,
    right_observations: RowFamily,
) -> RowFamily:
    """Read each component without introducing cross-system observations."""
    left_size = len(left_observations[0])
    right_size = len(right_observations[0])
    return (
        lift_left_observations(left_observations, right_size)
        + lift_right_observations(right_observations, left_size)
    )


def independent_product_causal_rank(
    left_operations: tuple[Matrix, ...],
    left_observations: RowFamily,
    right_operations: tuple[Matrix, ...],
    right_observations: RowFamily,
) -> tuple[int, int, int]:
    """Return `(left_rank, right_rank, product_rank)` for the causal closures."""
    left = causal_future_closure(left_operations, left_observations)
    right = causal_future_closure(right_operations, right_observations)
    product = causal_future_closure(
        independent_product_operations(left_operations, right_operations),
        independent_product_observations(left_observations, right_observations),
    )
    return (
        left.causal_visible_rank,
        right.causal_visible_rank,
        product.causal_visible_rank,
    )
