"""Action redundancy can switch in both directions as future context grows.

For a fixed action ``a`` and context subset ``S`` not containing it, compare the
closed future modules ``M(S)`` and ``M(S union {a})``.

At STATE_KERNEL level, ``a`` is locally redundant when the two modules have the
same rational row space.  At INTEGER_MODULE level, it is redundant only when the
embedded integer row lattices are equal.

This local redundancy predicate is not monotone in ``S``.

* activation: an action can preserve the current small module but become useful
  after another action creates an intermediate state direction that it moves;
* suppression: an action can be useful in a small context but become redundant
  after another action supplies the same future information.

Hence ``S -> redundant actions over S`` is not a closure operator and action
redundancy is not a context-free capability label.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

from .integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    action_subset_final_basis,
)
from .integer_future_observability import integer_matrix_rank


def _mode(value: str) -> str:
    if value not in (STATE_KERNEL, INTEGER_MODULE):
        raise ValueError("mode must be STATE_KERNEL or INTEGER_MODULE")
    return value


def action_redundant_over_context(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
    context_indices: Sequence[int],
    action_index: int,
    *,
    mode: str = INTEGER_MODULE,
) -> bool:
    actions = tuple(action_matrices)
    if not actions:
        raise ValueError("at least one action is required")
    context = tuple(context_indices)
    if len(set(context)) != len(context):
        raise ValueError("context_indices must be distinct")
    if isinstance(action_index, bool) or not isinstance(action_index, int):
        raise TypeError("action_index must be an integer")
    if not 0 <= action_index < len(actions):
        raise ValueError("action_index is outside the action family")
    if action_index in context:
        raise ValueError("context must not already contain the tested action")
    selected_mode = _mode(mode)

    before = action_subset_final_basis(actions, observation_rows, context)
    after = action_subset_final_basis(
        actions,
        observation_rows,
        tuple((*context, action_index)),
    )
    if selected_mode == STATE_KERNEL:
        return integer_matrix_rank(before) == integer_matrix_rank(after)
    return before == after


def action_redundancy_contexts(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
    action_index: int,
    *,
    mode: str = INTEGER_MODULE,
) -> tuple[tuple[int, ...], ...]:
    actions = tuple(action_matrices)
    if isinstance(action_index, bool) or not isinstance(action_index, int):
        raise TypeError("action_index must be an integer")
    if not 0 <= action_index < len(actions):
        raise ValueError("action_index is outside the action family")
    others = tuple(index for index in range(len(actions)) if index != action_index)
    return tuple(
        context
        for size in range(len(others) + 1)
        for context in combinations(others, size)
        if action_redundant_over_context(
            actions,
            observation_rows,
            context,
            action_index,
            mode=mode,
        )
    )


@dataclass(frozen=True)
class RedundancyContextSwitch:
    action_index: int
    smaller_context: tuple[int, ...]
    larger_context: tuple[int, ...]
    redundant_on_smaller: bool
    redundant_on_larger: bool

    @property
    def activation(self) -> bool:
        return self.redundant_on_smaller and not self.redundant_on_larger

    @property
    def suppression(self) -> bool:
        return not self.redundant_on_smaller and self.redundant_on_larger


def first_redundancy_context_switch(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
    action_index: int,
    *,
    mode: str = INTEGER_MODULE,
) -> RedundancyContextSwitch | None:
    actions = tuple(action_matrices)
    if not actions:
        raise ValueError("at least one action is required")
    if isinstance(action_index, bool) or not isinstance(action_index, int):
        raise TypeError("action_index must be an integer")
    if not 0 <= action_index < len(actions):
        raise ValueError("action_index is outside the action family")
    others = tuple(index for index in range(len(actions)) if index != action_index)
    contexts = tuple(
        context
        for size in range(len(others) + 1)
        for context in combinations(others, size)
    )
    values = {
        context: action_redundant_over_context(
            actions,
            observation_rows,
            context,
            action_index,
            mode=mode,
        )
        for context in contexts
    }
    for smaller in contexts:
        smaller_set = set(smaller)
        for larger in contexts:
            if smaller == larger or not smaller_set.issubset(larger):
                continue
            if values[smaller] != values[larger]:
                return RedundancyContextSwitch(
                    action_index=action_index,
                    smaller_context=smaller,
                    larger_context=larger,
                    redundant_on_smaller=values[smaller],
                    redundant_on_larger=values[larger],
                )
    return None
