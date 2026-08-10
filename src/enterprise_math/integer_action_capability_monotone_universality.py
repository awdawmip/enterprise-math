"""Universality of monotone future-action capability predicates.

Any finite nonempty upward-closed family ``P`` of action subsets can be realized
exactly as the full-precision preserving subsets of a 0/1, pairwise-commuting,
idempotent integer action family.

Let ``E`` be the action set and let ``F_1,...,F_t`` be the inclusion-maximal
subsets outside ``P``.  Create one Set-Cover universe element for each ``F_i``.
Action ``a`` covers element ``i`` exactly when ``a notin F_i``.

For any action subset ``S``:

    S covers every F_i
      iff S is not contained in any maximal false F_i
      iff S belongs to P.

Composing with the exact Set-Cover action compiler therefore realizes ``P`` at
both STATE_KERNEL and INTEGER_MODULE levels.  The trivial family in which every
subset preserves is realized by a fully observed one-dimensional state and
identity actions.

Consequences:

* monotonicity is essentially the only generic set-system structure guaranteed
  for full-precision action preservation;
* minimal preserving action families can be an arbitrary antichain;
* their count can reach the Sperner bound ``binom(k,floor(k/2))``;
* exact enumeration can therefore require exponential output even though the
  compiled actions commute, are idempotent, and close after one action layer.

Monotone Boolean functions, maximal false sets, hypergraph transversals and
Sperner's theorem are standard prior combinatorics.  The project value is the
exact P023 action-capability universality boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import comb
from typing import Iterable, Sequence

from .integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    action_subset_preserves,
    inclusion_minimal_action_subsets,
)
from .integer_action_capability_set_cover import (
    set_cover_action_matrices,
    set_cover_observation_rows,
)


Matrix = tuple[tuple[int, ...], ...]


def _action_count(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("action_count must be an integer")
    if value <= 0:
        raise ValueError("action_count must be positive")
    return value


def _subset(value: Iterable[int], action_count: int) -> frozenset[int]:
    result = frozenset(value)
    for action in result:
        if isinstance(action, bool) or not isinstance(action, int):
            raise TypeError("action subset entries must be integer indices")
        if not 0 <= action < action_count:
            raise ValueError("action subset entry is outside the action set")
    return result


def all_action_subsets(action_count: int) -> tuple[frozenset[int], ...]:
    count = _action_count(action_count)
    actions = tuple(range(count))
    return tuple(
        frozenset(subset)
        for size in range(count + 1)
        for subset in combinations(actions, size)
    )


def normalize_upward_closed_family(
    action_count: int,
    preserving_subsets: Sequence[Iterable[int]],
) -> frozenset[frozenset[int]]:
    count = _action_count(action_count)
    family = frozenset(
        _subset(subset, count) for subset in preserving_subsets
    )
    if not family:
        raise ValueError("preserving family must be nonempty")
    full = frozenset(range(count))
    if full not in family:
        raise ValueError("upward-closed preserving family must contain full action set")
    all_subsets = all_action_subsets(count)
    for subset in family:
        for candidate in all_subsets:
            if subset.issubset(candidate) and candidate not in family:
                raise ValueError("preserving family is not upward closed")
    return family


def maximal_nonpreserving_subsets(
    action_count: int,
    preserving_subsets: Sequence[Iterable[int]],
) -> tuple[frozenset[int], ...]:
    count = _action_count(action_count)
    family = normalize_upward_closed_family(count, preserving_subsets)
    false_sets = tuple(
        subset for subset in all_action_subsets(count) if subset not in family
    )
    return tuple(
        subset
        for subset in false_sets
        if not any(subset < other for other in false_sets)
    )


def upward_closure_of_antichain(
    action_count: int,
    minimal_subsets: Sequence[Iterable[int]],
) -> frozenset[frozenset[int]]:
    count = _action_count(action_count)
    minimal = tuple(_subset(subset, count) for subset in minimal_subsets)
    if not minimal:
        raise ValueError("minimal_subsets must be nonempty")
    for left in minimal:
        for right in minimal:
            if left != right and left.issubset(right):
                raise ValueError("minimal_subsets must form an antichain")
    return frozenset(
        candidate
        for candidate in all_action_subsets(count)
        if any(base.issubset(candidate) for base in minimal)
    )


@dataclass(frozen=True)
class MonotoneCapabilityCompilation:
    action_count: int
    preserving_family: frozenset[frozenset[int]]
    maximal_false_subsets: tuple[frozenset[int], ...]
    observation_rows: Matrix
    action_matrices: tuple[Matrix, ...]
    trivial_all_preserving: bool


def compile_monotone_capability_family(
    action_count: int,
    preserving_subsets: Sequence[Iterable[int]],
) -> MonotoneCapabilityCompilation:
    count = _action_count(action_count)
    family = normalize_upward_closed_family(count, preserving_subsets)
    false_maximal = maximal_nonpreserving_subsets(count, tuple(family))

    if not false_maximal:
        identity = ((1,),)
        return MonotoneCapabilityCompilation(
            action_count=count,
            preserving_family=family,
            maximal_false_subsets=(),
            observation_rows=((1,),),
            action_matrices=tuple(identity for _ in range(count)),
            trivial_all_preserving=True,
        )

    cover_sets = tuple(
        frozenset(
            false_index
            for false_index, false_subset in enumerate(false_maximal)
            if action not in false_subset
        )
        for action in range(count)
    )
    universe_size = len(false_maximal)
    return MonotoneCapabilityCompilation(
        action_count=count,
        preserving_family=family,
        maximal_false_subsets=false_maximal,
        observation_rows=set_cover_observation_rows(universe_size),
        action_matrices=set_cover_action_matrices(universe_size, cover_sets),
        trivial_all_preserving=False,
    )


def verify_monotone_capability_compilation(
    compilation: MonotoneCapabilityCompilation,
) -> bool:
    for subset in all_action_subsets(compilation.action_count):
        indices = tuple(sorted(subset))
        expected = subset in compilation.preserving_family
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            actual = action_subset_preserves(
                compilation.action_matrices,
                compilation.observation_rows,
                indices,
                mode=mode,
            )
            if actual != expected:
                raise AssertionError(
                    "compiled action family disagreed with monotone predicate"
                )
    return True


def verify_antichain_minimal_family_realization(
    action_count: int,
    minimal_subsets: Sequence[Iterable[int]],
) -> bool:
    family = upward_closure_of_antichain(action_count, minimal_subsets)
    compilation = compile_monotone_capability_family(
        action_count,
        tuple(family),
    )
    verify_monotone_capability_compilation(compilation)
    expected = tuple(
        sorted(
            (tuple(sorted(_subset(subset, action_count))) for subset in minimal_subsets),
            key=lambda subset: (len(subset), subset),
        )
    )
    for mode in (STATE_KERNEL, INTEGER_MODULE):
        actual = inclusion_minimal_action_subsets(
            compilation.action_matrices,
            compilation.observation_rows,
            mode=mode,
        )
        if actual != expected:
            raise AssertionError("compiled minimal action family missed target antichain")
    return True


def sperner_maximal_minimal_family_count(action_count: int) -> int:
    count = _action_count(action_count)
    return comb(count, count // 2)
