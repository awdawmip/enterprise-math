"""Cayley-Hamilton horizon bound for commuting integer future actions.

Let ``A_1,...,A_k`` be pairwise commuting ``n x n`` integer matrices.  Any
literal action word can be reordered to one monomial

    A_1^e1 ... A_k^ek.

For each action, Cayley-Hamilton expresses every power ``A_i^e`` with ``e>=n``
as an integer linear combination of lower powers ``1,A_i,...,A_i^(n-1)``.  Since
the matrices commute, these reductions can be performed independently in each
exponent without changing the other factors.

Therefore every action-word matrix is an integer linear combination of bounded
monomials

    A_1^e1 ... A_k^ek,       0<=e_i<n.

Every such monomial has word length at most

    k*(n-1).

Consequently the complete integer future-observation row lattice for any
observation matrix ``C`` is already attained by horizon ``k*(n-1)``.

For ``k=1`` this is the ordinary ``n-1`` Cayley-Hamilton bound.  The general
multi-action closure may stabilize much earlier, but cannot require a longer
word when the action family is pairwise commuting.

This is a standard commutative matrix-algebra consequence of Cayley-Hamilton.
The project use is as a sharp comparator for the noncommuting multi-action
integer-observability line: delayed Smith refinement from longer words requires
structure not captured by this commuting bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_action_language_observability import action_language_smith_profile
from .integer_future_observability import integer_matrix_product


Matrix = tuple[tuple[int, ...], ...]


def _matrix(values: Sequence[Sequence[int]]) -> Matrix:
    matrix = tuple(tuple(row) for row in values)
    if not matrix:
        raise ValueError("matrix must contain at least one row")
    width = len(matrix[0])
    if width == 0 or any(len(row) != width for row in matrix):
        raise ValueError("matrix rows must have one common positive width")
    for row in matrix:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
    return matrix


def commuting_action_family(
    action_matrices: Sequence[Sequence[Sequence[int]]],
) -> bool:
    actions = tuple(_matrix(matrix) for matrix in action_matrices)
    if not actions:
        raise ValueError("at least one action matrix is required")
    dimension = len(actions[0])
    if any(len(action) != dimension or len(action[0]) != dimension for action in actions):
        raise ValueError("all actions must be square on one common dimension")
    for left_index, left in enumerate(actions):
        for right in actions[left_index + 1 :]:
            if integer_matrix_product(left, right) != integer_matrix_product(right, left):
                return False
    return True


def commuting_cayley_hamilton_horizon_bound(
    action_matrices: Sequence[Sequence[Sequence[int]]],
) -> int:
    actions = tuple(_matrix(matrix) for matrix in action_matrices)
    if not actions:
        raise ValueError("at least one action matrix is required")
    dimension = len(actions[0])
    if any(len(action) != dimension or len(action[0]) != dimension for action in actions):
        raise ValueError("all actions must be square on one common dimension")
    if not commuting_action_family(actions):
        raise ValueError("Cayley-Hamilton multi-action bound requires pairwise commuting actions")
    return len(actions) * (dimension - 1)


@dataclass(frozen=True)
class CommutingActionObservabilityBoundReport:
    action_count: int
    state_dimension: int
    horizon_bound: int
    smith_factors_at_bound: tuple[int, ...]
    saturation_index_at_bound: int


def commuting_action_observability_bound_report(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
) -> CommutingActionObservabilityBoundReport:
    actions = tuple(_matrix(matrix) for matrix in action_matrices)
    bound = commuting_cayley_hamilton_horizon_bound(actions)
    profile = action_language_smith_profile(
        actions,
        observation_rows,
        bound,
    )
    return CommutingActionObservabilityBoundReport(
        action_count=len(actions),
        state_dimension=len(actions[0]),
        horizon_bound=bound,
        smith_factors_at_bound=profile.smith_invariant_factors,
        saturation_index_at_bound=profile.maximal_nonzero_determinantal_divisor,
    )
