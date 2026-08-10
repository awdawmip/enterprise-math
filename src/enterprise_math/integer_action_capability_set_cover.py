"""Exact Set-Cover specialization of integer future-action capability selection.

This module gives a polynomial, 0/1-valued construction showing that generic
minimum future-action capability already contains ordinary Set Cover even when
all action matrices are pairwise commuting and idempotent and the future module
closes after one action layer.

For universe elements ``j=0,...,m-1`` use two state coordinates:

* ``e_j`` — currently observed source coordinate;
* ``f_j`` — future coordinate revealed when some selected set covers j.

The current observation rows are all ``e_j``.  For set/action ``S_a`` define
one integer matrix by

    e_j A_a = f_j   if j in S_a,
    e_j A_a = e_j   otherwise,
    f_j A_a = f_j   always.

Every action is idempotent.  Two actions commute because their joint effect on
``e_j`` is simply whether either set covers j.  For action subset T, the closed
future row module is generated exactly by all ``e_j`` plus those ``f_j`` whose
element is covered by at least one set in T.

Assuming the full set family covers the universe,

    T preserves the full STATE_KERNEL precision
      iff T covers the universe
      iff T preserves the full INTEGER_MODULE precision.

Therefore minimum-cardinality action capability contains Minimum Set Cover as a
special case.  The construction separates two complexities:

* future-word closure can be trivial (commuting, idempotent, horizon one);
* selecting a smallest capability alphabet can still have the full combinatorial
  difficulty of Set Cover.

Set Cover and its complexity are standard prior computer science.  The project
value is the exact P023 reduction and the boundary against assuming that a fast
future-module closure automatically makes capability minimization easy.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    action_subset_final_basis,
    action_subset_preserves,
)


Matrix = tuple[tuple[int, ...], ...]


def _universe_size(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("universe_size must be an integer")
    if value <= 0:
        raise ValueError("universe_size must be positive")
    return value


def _cover_sets(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> tuple[frozenset[int], ...]:
    result = tuple(frozenset(values) for values in sets)
    if not result:
        raise ValueError("at least one set/action is required")
    for subset in result:
        for element in subset:
            if isinstance(element, bool) or not isinstance(element, int):
                raise TypeError("set-cover elements must be integer indices")
            if not 0 <= element < universe_size:
                raise ValueError("set-cover element is outside the universe")
    return result


def set_cover_observation_rows(universe_size: int) -> Matrix:
    size = _universe_size(universe_size)
    dimension = 2 * size
    return tuple(
        tuple(int(column == element) for column in range(dimension))
        for element in range(size)
    )


def set_cover_action_matrices(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> tuple[Matrix, ...]:
    size = _universe_size(universe_size)
    cover_sets = _cover_sets(size, sets)
    dimension = 2 * size
    actions = []
    for subset in cover_sets:
        rows = [[0] * dimension for _ in range(dimension)]
        for element in range(size):
            source = element
            target = size + element
            if element in subset:
                rows[source][target] = 1
            else:
                rows[source][source] = 1
            rows[target][target] = 1
        actions.append(tuple(tuple(row) for row in rows))
    return tuple(actions)


def selected_sets_cover_universe(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    action_indices: Sequence[int],
) -> bool:
    size = _universe_size(universe_size)
    cover_sets = _cover_sets(size, sets)
    indices = tuple(action_indices)
    if len(set(indices)) != len(indices):
        raise ValueError("action_indices must be distinct")
    covered: set[int] = set()
    for index in indices:
        if isinstance(index, bool) or not isinstance(index, int):
            raise TypeError("action index must be an integer")
        if not 0 <= index < len(cover_sets):
            raise ValueError("action index is outside the set family")
        covered.update(cover_sets[index])
    return covered == set(range(size))


def set_cover_actions_commute_and_are_idempotent(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> bool:
    actions = set_cover_action_matrices(universe_size, sets)

    def product(left: Matrix, right: Matrix) -> Matrix:
        dimension = len(left)
        return tuple(
            tuple(
                sum(left[row][inner] * right[inner][column] for inner in range(dimension))
                for column in range(dimension)
            )
            for row in range(dimension)
        )

    for action in actions:
        if product(action, action) != action:
            raise AssertionError("compiled set-cover action was not idempotent")
    for left in actions:
        for right in actions:
            if product(left, right) != product(right, left):
                raise AssertionError("compiled set-cover actions did not commute")
    return True


@dataclass(frozen=True)
class SetCoverActionCapabilityReport:
    universe_size: int
    action_count: int
    full_family_covers_universe: bool
    compiled_actions_commute_and_are_idempotent: bool


def set_cover_action_capability_report(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> SetCoverActionCapabilityReport:
    size = _universe_size(universe_size)
    cover_sets = _cover_sets(size, sets)
    full = tuple(range(len(cover_sets)))
    return SetCoverActionCapabilityReport(
        universe_size=size,
        action_count=len(cover_sets),
        full_family_covers_universe=selected_sets_cover_universe(
            size,
            cover_sets,
            full,
        ),
        compiled_actions_commute_and_are_idempotent=(
            set_cover_actions_commute_and_are_idempotent(size, cover_sets)
        ),
    )


def verify_set_cover_capability_equivalence(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    action_indices: Sequence[int],
) -> bool:
    """Verify cover iff STATE_KERNEL iff INTEGER_MODULE preservation."""
    size = _universe_size(universe_size)
    cover_sets = _cover_sets(size, sets)
    full_indices = tuple(range(len(cover_sets)))
    if not selected_sets_cover_universe(size, cover_sets, full_indices):
        raise ValueError("the full set family must cover the universe")

    actions = set_cover_action_matrices(size, cover_sets)
    observations = set_cover_observation_rows(size)
    cover = selected_sets_cover_universe(size, cover_sets, action_indices)
    kernel = action_subset_preserves(
        actions,
        observations,
        action_indices,
        mode=STATE_KERNEL,
    )
    module = action_subset_preserves(
        actions,
        observations,
        action_indices,
        mode=INTEGER_MODULE,
    )
    if not (cover == kernel == module):
        raise AssertionError("set-cover/action-capability equivalence failed")

    # In the full module, each covered f_j is a literal unit row; no hidden
    # integer index separates STATE_KERNEL from INTEGER_MODULE here.
    basis = action_subset_final_basis(actions, observations, action_indices)
    expected_rank = size + len(
        set().union(*(cover_sets[index] for index in action_indices))
        if action_indices
        else set()
    )
    if len(basis) != expected_rank:
        raise AssertionError("compiled set-cover future module had unexpected rank")
    return True
