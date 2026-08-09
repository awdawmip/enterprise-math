"""Bulk-dependent continuation states instead of a fixed Cartesian product.

A convenient causal runtime schema often looks like `(bulk, tau)`, but the
minimum structural continuation quotient can depend on the current bulk.  Once
bulk saturation or another causal effect makes some relation distinctions
forever irrelevant, those tau labels should collapse only in that bulk context.

Thus a fixed product `B x T` is generally an upper-bound representation, not the
ontology.  The exact finite state is obtained by future refinement of the full
reachable `(bulk,raw_relation)` states; when bulk is part of the current
observation, the stable classes decompose contextually as a disjoint family
`T_b` whose cardinality may vary with b.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable

from .causal_continuation_refinement import stable_continuation_types

State = Hashable
Bulk = Hashable


def stable_dependent_types(
    bulk_of_state: dict[State, Bulk],
    extra_observation: dict[State, Hashable],
    actions: dict[Hashable, dict[State, State]],
) -> tuple[dict[State, int], int]:
    """Future-minimize full states while keeping current bulk explicitly observable."""
    if set(bulk_of_state) != set(extra_observation):
        raise ValueError("bulk and extra observation must cover the same states")
    observations = {
        state: (bulk_of_state[state], extra_observation[state])
        for state in bulk_of_state
    }
    return stable_continuation_types(observations, actions)


def continuation_classes_by_bulk(
    bulk_of_state: dict[State, Bulk],
    stable_classes: dict[State, int],
) -> dict[Bulk, frozenset[int]]:
    if set(bulk_of_state) != set(stable_classes):
        raise ValueError("bulk labels and stable classes must cover the same states")
    result: dict[Bulk, set[int]] = defaultdict(set)
    for state, bulk in bulk_of_state.items():
        result[bulk].add(stable_classes[state])
    return {bulk: frozenset(classes) for bulk, classes in result.items()}


def dependent_state_count(
    bulk_of_state: dict[State, Bulk],
    stable_classes: dict[State, int],
) -> int:
    """Number of exact future classes across all represented bulk contexts."""
    return len(set(stable_classes.values()))


def rectangular_upper_bound(
    bulk_of_state: dict[State, Bulk],
    raw_relation_of_state: dict[State, Hashable],
) -> int:
    """Naive `#bulks * #raw_relation_labels` product-state size."""
    if set(bulk_of_state) != set(raw_relation_of_state):
        raise ValueError("bulk and relation labels must cover the same states")
    return len(set(bulk_of_state.values())) * len(set(raw_relation_of_state.values()))


def bulk_dependent_compression(
    bulk_of_state: dict[State, Bulk],
    raw_relation_of_state: dict[State, Hashable],
    stable_classes: dict[State, int],
) -> int:
    """How many states the global future quotient removes from a fixed B x T rectangle."""
    return rectangular_upper_bound(bulk_of_state, raw_relation_of_state) - dependent_state_count(
        bulk_of_state, stable_classes
    )
