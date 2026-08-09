"""Exact quotient criteria for binary threshold-controlled affine dynamics.

This is an A3 specialization of future-compatible quotient semantics.

Fine state is the full integer lattice Z^k. A coordinate partition A observes
block sums. A binary program uses the guard

    w^T c + b >= 0

and chooses one of two affine branches c' = B_r c + u_r.

Two regimes are exact:

1. The guard descends to the partition. If it is nonconstant on coarse Z^l,
   both branch affine maps must descend; the coarse program keeps the guard.
   If the guard is globally constant, only the active branch matters.
2. The guard does not descend. Then every coarse fiber contains both guard
   outcomes. Exact descent is possible iff both affine branches descend and
   induce the same coarse affine map. In that case branch identity is erased.

Although exactness is not monotone under arbitrary partition refinement, the
coarsest exact refinement of a declared initial partition still has a two-stage
construction: first stabilize the branch dynamics; only if a hidden guard then
sees different coarse branch effects must the guard be exposed and stability
recomputed.

No floating point values or state-box enumeration are used.
"""

from __future__ import annotations

from dataclasses import dataclass

from .linear_observation_quotient import (
    descended_linear_observable,
    refine_partition_for_linear_observations,
)
from .linear_relation_quotient import (
    Matrix,
    Partition,
    descended_linear_matrix,
    partition_matrix,
    refine_partition_for_linear_family,
)


Vector = tuple[int, ...]
AffineBranch = tuple[Matrix, Vector]


@dataclass(frozen=True)
class BinaryThresholdFactor:
    """Exact coarse factorization of a binary threshold affine program."""

    mode: str
    coarse_guard_weights: Vector | None
    guard_bias: int
    true_branch: AffineBranch | None
    false_branch: AffineBranch | None
    common_branch: AffineBranch | None


def _require_vector(name: str, vector: Vector, size: int) -> None:
    if not isinstance(vector, tuple) or len(vector) != size:
        raise ValueError(f"{name} must have length {size}")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError(f"{name} entries must be integers")


def _require_square_matrix(name: str, matrix: Matrix, size: int | None = None) -> int:
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError(f"{name} must be a non-empty square tuple")
    matrix_size = len(matrix)
    if size is not None and matrix_size != size:
        raise ValueError(f"{name} has incompatible dimension")
    if any(not isinstance(row, tuple) or len(row) != matrix_size for row in matrix):
        raise ValueError(f"{name} must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in matrix
        for value in row
    ):
        raise ValueError(f"{name} entries must be integers")
    return matrix_size


def _require_partition(size: int, partition: Partition) -> None:
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be non-empty")
    flattened = [index for group in partition for index in group]
    if any(not isinstance(group, tuple) or not group for group in partition):
        raise ValueError("partition groups must be non-empty tuples")
    if any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or index < 0
        or index >= size
        for index in flattened
    ):
        raise ValueError("partition index out of range")
    if sorted(flattened) != list(range(size)):
        raise ValueError("partition must cover every coordinate exactly once")


def _coarse_offset(offset: Vector, partition: Partition) -> Vector:
    aggregation = partition_matrix(len(offset), partition)
    return tuple(
        sum(aggregation[row][column] * offset[column] for column in range(len(offset)))
        for row in range(len(partition))
    )


def descended_affine_branch(branch: AffineBranch, partition: Partition) -> AffineBranch:
    """Return the exact coarse affine branch, or raise if its linear part cannot descend."""
    matrix, offset = branch
    size = _require_square_matrix("matrix", matrix)
    _require_vector("offset", offset, size)
    coarse_matrix = descended_linear_matrix(matrix, partition)
    return coarse_matrix, _coarse_offset(offset, partition)


def _guard_factor(weights: Vector, bias: int, partition: Partition) -> tuple[str, Vector | None]:
    if isinstance(bias, bool) or not isinstance(bias, int):
        raise ValueError("bias must be an integer")
    size = len(weights)
    _require_vector("weights", weights, size)
    try:
        coarse_weights = descended_linear_observable(weights, partition)
    except ValueError as error:
        if str(error) == "observable reads distinctions erased by the partition":
            return "hidden", None
        raise

    if all(weight == 0 for weight in coarse_weights):
        return ("constant_true" if bias >= 0 else "constant_false"), coarse_weights
    return "coarse_guard", coarse_weights


def factor_binary_threshold_piecewise(
    weights: Vector,
    bias: int,
    true_branch: AffineBranch,
    false_branch: AffineBranch,
    partition: Partition,
) -> BinaryThresholdFactor:
    """Return the exact coarse program, or raise if the partition is not exact.

    The theorem is complete for a single affine threshold guard on the full
    integer lattice Z^k.
    """
    true_matrix, true_offset = true_branch
    size = _require_square_matrix("true matrix", true_matrix)
    _require_vector("true offset", true_offset, size)
    false_matrix, false_offset = false_branch
    _require_square_matrix("false matrix", false_matrix, size)
    _require_vector("false offset", false_offset, size)
    _require_vector("weights", weights, size)
    _require_partition(size, partition)

    mode, coarse_guard = _guard_factor(weights, bias, partition)

    if mode == "constant_true":
        coarse_true = descended_affine_branch(true_branch, partition)
        return BinaryThresholdFactor(
            mode=mode,
            coarse_guard_weights=coarse_guard,
            guard_bias=bias,
            true_branch=coarse_true,
            false_branch=None,
            common_branch=coarse_true,
        )

    if mode == "constant_false":
        coarse_false = descended_affine_branch(false_branch, partition)
        return BinaryThresholdFactor(
            mode=mode,
            coarse_guard_weights=coarse_guard,
            guard_bias=bias,
            true_branch=None,
            false_branch=coarse_false,
            common_branch=coarse_false,
        )

    try:
        coarse_true = descended_affine_branch(true_branch, partition)
        coarse_false = descended_affine_branch(false_branch, partition)
    except ValueError as error:
        if str(error) == "linear dynamics reads distinctions erased by the partition":
            raise ValueError("piecewise program reads distinctions erased by the partition") from error
        raise

    if mode == "coarse_guard":
        return BinaryThresholdFactor(
            mode=mode,
            coarse_guard_weights=coarse_guard,
            guard_bias=bias,
            true_branch=coarse_true,
            false_branch=coarse_false,
            common_branch=coarse_true if coarse_true == coarse_false else None,
        )

    if coarse_true != coarse_false:
        raise ValueError(
            "hidden guard varies inside every coarse fiber but branch coarse effects differ"
        )

    return BinaryThresholdFactor(
        mode="hidden_guard_erased",
        coarse_guard_weights=None,
        guard_bias=bias,
        true_branch=coarse_true,
        false_branch=coarse_false,
        common_branch=coarse_true,
    )


def binary_threshold_piecewise_descends(
    weights: Vector,
    bias: int,
    true_branch: AffineBranch,
    false_branch: AffineBranch,
    partition: Partition,
) -> bool:
    """Whether the binary threshold affine program factors exactly through the partition."""
    try:
        factor_binary_threshold_piecewise(
            weights, bias, true_branch, false_branch, partition
        )
    except ValueError as error:
        if str(error) in {
            "piecewise program reads distinctions erased by the partition",
            "hidden guard varies inside every coarse fiber but branch coarse effects differ",
        }:
            return False
        raise
    return True


def minimum_exact_partition_for_binary_threshold_piecewise(
    weights: Vector,
    bias: int,
    true_branch: AffineBranch,
    false_branch: AffineBranch,
    initial_partition: Partition | None = None,
) -> Partition:
    """Coarsest exact refinement for one binary integer-threshold affine program.

    Construction:

    1. If the fine guard is globally constant, stabilize only the active branch.
    2. Otherwise compute the coarsest partition on which both branch linear
       parts descend.
    3. If that partition is already exact, return it. This includes hidden
       guards whose two coarse branch effects coincide.
    4. If a hidden guard still sees different coarse branch effects, no further
       refinement that keeps the guard hidden can restore equality: every child
       target block would have to have zero branch-difference sum, whose sum
       would force the parent block difference to be zero already. Therefore
       every exact refinement must expose the guard. Split by guard coefficients
       and restabilize both branches.

    This bypasses the fact that exactness itself is not monotone along arbitrary
    intermediate refinements.
    """
    true_matrix, true_offset = true_branch
    size = _require_square_matrix("true matrix", true_matrix)
    _require_vector("true offset", true_offset, size)
    false_matrix, false_offset = false_branch
    _require_square_matrix("false matrix", false_matrix, size)
    _require_vector("false offset", false_offset, size)
    _require_vector("weights", weights, size)
    if isinstance(bias, bool) or not isinstance(bias, int):
        raise ValueError("bias must be an integer")

    if initial_partition is None:
        initial = (tuple(range(size)),)
    else:
        _require_partition(size, initial_partition)
        initial = initial_partition

    if all(weight == 0 for weight in weights):
        active_matrix = true_matrix if bias >= 0 else false_matrix
        return refine_partition_for_linear_family((active_matrix,), initial)

    branch_stable = refine_partition_for_linear_family(
        (true_matrix, false_matrix), initial
    )

    try:
        factor_binary_threshold_piecewise(
            weights, bias, true_branch, false_branch, branch_stable
        )
        return branch_stable
    except ValueError as error:
        if str(error) != (
            "hidden guard varies inside every coarse fiber but branch coarse effects differ"
        ):
            raise

    guard_visible = refine_partition_for_linear_observations(
        (weights,), branch_stable
    )
    result = refine_partition_for_linear_family(
        (true_matrix, false_matrix), guard_visible
    )
    factor_binary_threshold_piecewise(
        weights, bias, true_branch, false_branch, result
    )
    return result
