"""Finite quotient calculus for composition-safe collapse (P023 research branch).

The core question is whether a coarse state map may safely forget distinctions
without changing any future observable that matters to the chosen dynamics.

For a fine domain X, a coarse projection q:X->Q, a transformation F:X->Y, and
an observable r:Y->R, the observable r∘F descends through q exactly when it is
constant on every q-fiber.  When it does not, the coarsest one-step repair is
the refinement x |-> (q(x), r(F(x))).

For a finite deterministic self-map F:X->X and an initial observation partition
q_0, repeated refinement by q_{t+1}(x)=(q_t(x),q_t(F(x))) stabilizes finitely.
The stable partition is the coarsest F-compatible refinement of q_0 and records
exactly the distinctions needed to preserve all future q_0-observations.

This module is deliberately finite and exact.  It uses only equality, integer
class identifiers, and finite iteration; no real-valued error metric is used.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from typing import TypeVar

State = TypeVar("State", bound=Hashable)
Label = TypeVar("Label", bound=Hashable)
Output = TypeVar("Output", bound=Hashable)


def _domain(domain: Iterable[State]) -> tuple[State, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _total_map(states: tuple[State, ...], mapping: Mapping[State, Output], name: str) -> None:
    if set(mapping) != set(states):
        raise ValueError(f"{name} must be total on the domain and have no extra keys")


def canonical_class_ids(
    domain: Iterable[State], labels: Mapping[State, Hashable]
) -> dict[State, int]:
    """Replace arbitrary hashable labels by deterministic first-seen integer ids."""
    states = _domain(domain)
    _total_map(states, labels, "labels")
    class_id: dict[Hashable, int] = {}
    result: dict[State, int] = {}
    for state in states:
        label = labels[state]
        if label not in class_id:
            class_id[label] = len(class_id)
        result[state] = class_id[label]
    return result


def fiber_constancy_witness(
    domain: Iterable[State],
    coarse: Mapping[State, Hashable],
    observed: Mapping[State, Hashable],
) -> tuple[State, State] | None:
    """Return two states in one coarse fiber with different observed outputs."""
    states = _domain(domain)
    _total_map(states, coarse, "coarse map")
    _total_map(states, observed, "observed map")
    first: dict[Hashable, State] = {}
    for state in states:
        key = coarse[state]
        if key not in first:
            first[key] = state
            continue
        representative = first[key]
        if observed[representative] != observed[state]:
            return representative, state
    return None


def descends_through(
    domain: Iterable[State],
    coarse: Mapping[State, Hashable],
    observed: Mapping[State, Hashable],
) -> bool:
    """Whether ``observed`` factors through the coarse-state map."""
    return fiber_constancy_witness(domain, coarse, observed) is None


def induced_map(
    domain: Iterable[State],
    coarse: Mapping[State, Hashable],
    observed: Mapping[State, Hashable],
) -> dict[Hashable, Hashable]:
    """Construct the unique induced coarse map when fiber constancy holds."""
    states = _domain(domain)
    _total_map(states, coarse, "coarse map")
    _total_map(states, observed, "observed map")
    witness = fiber_constancy_witness(states, coarse, observed)
    if witness is not None:
        raise ValueError(f"observed map does not descend through coarse fibers: {witness!r}")
    result: dict[Hashable, Hashable] = {}
    for state in states:
        result[coarse[state]] = observed[state]
    return result


def coarsest_one_step_repair(
    domain: Iterable[State],
    coarse: Mapping[State, Hashable],
    observed: Mapping[State, Hashable],
) -> dict[State, int]:
    """Coarsest refinement of ``coarse`` through which ``observed`` descends.

    The repaired class of x is determined by the pair
    ``(coarse[x], observed[x])``.  Integer class ids are returned only as a
    canonical finite representation of that pair partition.
    """
    states = _domain(domain)
    _total_map(states, coarse, "coarse map")
    _total_map(states, observed, "observed map")
    signatures = {state: (coarse[state], observed[state]) for state in states}
    return canonical_class_ids(states, signatures)


def refines(
    domain: Iterable[State],
    finer: Mapping[State, Hashable],
    coarser: Mapping[State, Hashable],
) -> bool:
    """Whether equality in ``finer`` implies equality in ``coarser``."""
    states = _domain(domain)
    _total_map(states, finer, "finer partition")
    _total_map(states, coarser, "coarser partition")
    seen: dict[Hashable, Hashable] = {}
    for state in states:
        fine = finer[state]
        coarse = coarser[state]
        if fine in seen and seen[fine] != coarse:
            return False
        seen[fine] = coarse
    return True


def one_step_transition_refinement(
    domain: Iterable[State],
    transition: Mapping[State, State],
    partition: Mapping[State, Hashable],
) -> dict[State, int]:
    """Refine by current class and the next-state class."""
    states = _domain(domain)
    _total_map(states, transition, "transition")
    _total_map(states, partition, "partition")
    state_set = set(states)
    if any(transition[state] not in state_set for state in states):
        raise ValueError("transition must map the domain into itself")
    signatures = {
        state: (partition[state], partition[transition[state]]) for state in states
    }
    return canonical_class_ids(states, signatures)


def transition_compatible(
    domain: Iterable[State],
    transition: Mapping[State, State],
    partition: Mapping[State, Hashable],
) -> bool:
    """Whether transition descends to a deterministic map on partition classes."""
    states = _domain(domain)
    _total_map(states, transition, "transition")
    _total_map(states, partition, "partition")
    next_labels = {state: partition[transition[state]] for state in states}
    return descends_through(states, partition, next_labels)


def future_partition_sequence(
    domain: Iterable[State],
    transition: Mapping[State, State],
    initial_partition: Mapping[State, Hashable],
) -> tuple[dict[State, int], ...]:
    """Return all distinct refinement stages through the first stable stage."""
    states = _domain(domain)
    _total_map(states, transition, "transition")
    current = canonical_class_ids(states, initial_partition)
    stages = [current]
    while True:
        nxt = one_step_transition_refinement(states, transition, current)
        if nxt == current:
            return tuple(stages)
        if not refines(states, nxt, current):
            raise AssertionError("future refinement must never merge current classes")
        stages.append(nxt)
        current = nxt
        if len(stages) > len(states):
            raise AssertionError("finite partition refinement exceeded the state bound")


def stable_future_partition(
    domain: Iterable[State],
    transition: Mapping[State, State],
    initial_partition: Mapping[State, Hashable],
) -> dict[State, int]:
    """Return the coarsest transition-compatible refinement of the initial partition."""
    return dict(future_partition_sequence(domain, transition, initial_partition)[-1])


def future_signature(
    state: State,
    transition: Mapping[State, State],
    observation: Mapping[State, Hashable],
    depth: int,
) -> tuple[Hashable, ...]:
    """Observation labels along ``state, F(state), ..., F^depth(state)``."""
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    result: list[Hashable] = []
    current = state
    for _ in range(depth + 1):
        if current not in transition or current not in observation:
            raise ValueError("transition and observation must cover the visited state")
        result.append(observation[current])
        current = transition[current]
    return tuple(result)


def same_future_observations(
    left: State,
    right: State,
    transition: Mapping[State, State],
    observation: Mapping[State, Hashable],
    steps: int,
) -> bool:
    """Whether two states agree on observation labels for ``steps+1`` positions."""
    return future_signature(left, transition, observation, steps) == future_signature(
        right, transition, observation, steps
    )


def class_count(partition: Mapping[State, Hashable]) -> int:
    """Number of represented coarse classes."""
    return len(set(partition.values()))
