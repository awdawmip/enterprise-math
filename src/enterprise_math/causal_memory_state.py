"""Causal memory as unresolved continuation-type multiplicity.

A declared current state label r is future-sufficient exactly when all raw
histories/witnesses mapped to r share one continuation-signature type.  Thus a
Markov-like state is derived from future distinguishability rather than assumed.

The minimal finite memory refinement is the pair (r, tau), not raw history.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable

State = Hashable
Current = Hashable
ContinuationType = Hashable


def continuation_types_per_current(
    state_to_current: dict[State, Current],
    state_to_type: dict[State, ContinuationType],
) -> dict[Current, frozenset[ContinuationType]]:
    if not isinstance(state_to_current, dict) or not state_to_current:
        raise ValueError("state_to_current must be a non-empty dict")
    if set(state_to_type) != set(state_to_current):
        raise ValueError("state_to_type must define exactly the same raw states")
    result: dict[Current, set[ContinuationType]] = defaultdict(set)
    for state, current in state_to_current.items():
        result[current].add(state_to_type[state])
    return {current: frozenset(types) for current, types in result.items()}


def current_state_is_future_sufficient(
    state_to_current: dict[State, Current],
    state_to_type: dict[State, ContinuationType],
) -> bool:
    """Whether the declared current-state label is already causally Markov."""
    return all(
        len(types) == 1
        for types in continuation_types_per_current(state_to_current, state_to_type).values()
    )


def minimal_memory_refinement(
    state_to_current: dict[State, Current],
    state_to_type: dict[State, ContinuationType],
) -> dict[State, tuple[Current, ContinuationType]]:
    """Refine current labels only by future-distinguishable continuation type."""
    continuation_types_per_current(state_to_current, state_to_type)
    return {
        state: (state_to_current[state], state_to_type[state])
        for state in state_to_current
    }


def hidden_memory_excess(
    state_to_current: dict[State, Current],
    state_to_type: dict[State, ContinuationType],
) -> int:
    """Count extra continuation classes hidden inside current labels.

    Sum_r (number_of_types_in_r - 1).  This is a typed finite diagnostic, not a
    universal scalar ontology.
    """
    return sum(
        len(types) - 1
        for types in continuation_types_per_current(state_to_current, state_to_type).values()
    )
