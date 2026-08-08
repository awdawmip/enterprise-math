"""Abstract finite precision systems for Enterprise Math P018 stage 5.

A finite precision system is represented here by one finite terminal state set X
and a family of observations O_l : X -> Y_l.  A finer observation refines a
coarser one when equality at the finer level implies equality at the coarser
level.  Equivalently, the partition induced by the finer observation refines the
coarser partition.

Inverse/projective systems and partition refinement are established mathematics.
P018 studies the finite proof/dynamics consequences of this structure without
requiring an inverse limit or infinite-precision terminal object.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable

Certificate = str
TRUE: Certificate = "TRUE"
FALSE: Certificate = "FALSE"
UNRESOLVED: Certificate = "UNRESOLVED"


def _unique_states(states: list[Hashable]) -> list[Hashable]:
    if not states:
        raise ValueError("terminal state set must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("terminal states must be distinct")
    return states


def observation_partition(
    states: list[Hashable], observation: Callable[[Hashable], Hashable]
) -> dict[Hashable, tuple[Hashable, ...]]:
    """Return the finite partition induced by one observation map."""
    _unique_states(states)
    blocks: dict[Hashable, list[Hashable]] = {}
    for state in states:
        key = observation(state)
        blocks.setdefault(key, []).append(state)
    return {key: tuple(block) for key, block in blocks.items()}


def observation_fiber(
    states: list[Hashable],
    observation: Callable[[Hashable], Hashable],
    state: Hashable,
) -> tuple[Hashable, ...]:
    """Return the observation fiber containing ``state``."""
    _unique_states(states)
    if state not in states:
        raise ValueError("state must belong to terminal state set")
    key = observation(state)
    return tuple(candidate for candidate in states if observation(candidate) == key)


def refinement_projection(
    states: list[Hashable],
    coarse_observation: Callable[[Hashable], Hashable],
    fine_observation: Callable[[Hashable], Hashable],
) -> dict[Hashable, Hashable]:
    """Construct the unique transition map fine-observation -> coarse-observation.

    The map exists exactly when the fine observation refines the coarse one:
    equal fine observations must always have equal coarse observations.
    """
    _unique_states(states)
    projection: dict[Hashable, Hashable] = {}
    for state in states:
        fine_key = fine_observation(state)
        coarse_key = coarse_observation(state)
        previous = projection.get(fine_key, coarse_key)
        if previous != coarse_key:
            raise ValueError("fine observation does not refine coarse observation")
        projection[fine_key] = coarse_key
    return projection


def fiber_nesting(
    states: list[Hashable],
    coarse_observation: Callable[[Hashable], Hashable],
    fine_observation: Callable[[Hashable], Hashable],
    state: Hashable,
) -> dict[str, tuple[Hashable, ...]]:
    """Verify that the fine fiber is contained in the coarse fiber."""
    refinement_projection(states, coarse_observation, fine_observation)
    coarse = observation_fiber(states, coarse_observation, state)
    fine = observation_fiber(states, fine_observation, state)
    if not set(fine).issubset(coarse):
        raise AssertionError("fine observation fiber escaped coarse fiber")
    return {"coarse": coarse, "fine": fine}


def ambiguity_multiplicity(
    states: list[Hashable],
    observation: Callable[[Hashable], Hashable],
    state: Hashable,
) -> int:
    """Return the number of terminal states still compatible with an observation."""
    return len(observation_fiber(states, observation, state))


def ambiguity_profile(
    states: list[Hashable],
    observations: list[Callable[[Hashable], Hashable]],
    state: Hashable,
) -> list[int]:
    """Return nonincreasing ambiguity along a refinement chain."""
    if not observations:
        raise ValueError("at least one observation is required")
    counts: list[int] = []
    previous = observations[0]
    last: int | None = None
    for observation in observations:
        refinement_projection(states, previous, observation)
        count = ambiguity_multiplicity(states, observation, state)
        if last is not None and count > last:
            raise AssertionError("ambiguity increased under refinement")
        counts.append(count)
        last = count
        previous = observation
    return counts


def strict_refinement_witness(
    states: list[Hashable],
    coarse_observation: Callable[[Hashable], Hashable],
    fine_observation: Callable[[Hashable], Hashable],
    state: Hashable,
) -> Hashable | None:
    """Return a terminal state removed from the target fiber by refinement.

    Such a witness exists iff ambiguity strictly decreases at ``state``.
    """
    data = fiber_nesting(states, coarse_observation, fine_observation, state)
    removed = [candidate for candidate in data["coarse"] if candidate not in data["fine"]]
    return removed[0] if removed else None


def ambiguity_gain_profile(
    states: list[Hashable],
    observations: list[Callable[[Hashable], Hashable]],
    state: Hashable,
) -> list[int]:
    """Return nonnegative ambiguity reductions between adjacent precision levels."""
    counts = ambiguity_profile(states, observations, state)
    gains = [earlier - later for earlier, later in zip(counts, counts[1:])]
    if any(gain < 0 for gain in gains):
        raise AssertionError("precision ambiguity gain must be nonnegative")
    if gains and sum(gains) != counts[0] - counts[-1]:
        raise AssertionError("ambiguity gains failed to telescope")
    return gains


def predicate_fiber_certificate(
    states: list[Hashable],
    observation: Callable[[Hashable], Hashable],
    predicate: Callable[[Hashable], bool],
    state: Hashable,
) -> Certificate:
    """Certify a Boolean predicate when it is constant on the observation fiber."""
    fiber = observation_fiber(states, observation, state)
    values = {bool(predicate(candidate)) for candidate in fiber}
    if values == {True}:
        return TRUE
    if values == {False}:
        return FALSE
    return UNRESOLVED


def predicate_certificate_profile(
    states: list[Hashable],
    observations: list[Callable[[Hashable], Hashable]],
    predicate: Callable[[Hashable], bool],
    state: Hashable,
) -> list[Certificate]:
    """Return persistent predicate certificates along a refinement chain."""
    if not observations:
        raise ValueError("at least one observation is required")
    statuses: list[Certificate] = []
    decided: Certificate | None = None
    previous = observations[0]
    for observation in observations:
        refinement_projection(states, previous, observation)
        status = predicate_fiber_certificate(states, observation, predicate, state)
        if decided is not None and status != decided:
            raise AssertionError("a predicate certificate was overturned by refinement")
        if status != UNRESOLVED:
            decided = status
        statuses.append(status)
        previous = observation
    return statuses


def first_decision_index(
    states: list[Hashable],
    observations: list[Callable[[Hashable], Hashable]],
    predicate: Callable[[Hashable], bool],
    state: Hashable,
) -> int | None:
    """Return the first precision index that certifies the predicate at state."""
    profile = predicate_certificate_profile(states, observations, predicate, state)
    for index, status in enumerate(profile):
        if status != UNRESOLVED:
            return index
    return None


def first_decision_shells(
    states: list[Hashable],
    observations: list[Callable[[Hashable], Hashable]],
    predicate: Callable[[Hashable], bool],
) -> dict[int | None, tuple[Hashable, ...]]:
    """Partition terminal states by their first predicate-certifying precision."""
    _unique_states(states)
    shells: dict[int | None, list[Hashable]] = {}
    for state in states:
        index = first_decision_index(states, observations, predicate, state)
        shells.setdefault(index, []).append(state)
    flattened = [state for block in shells.values() for state in block]
    if sorted(map(repr, flattened)) != sorted(map(repr, states)):
        raise AssertionError("first-decision shells failed to partition terminal states")
    return {index: tuple(block) for index, block in shells.items()}


def kernel_partition(
    states: list[Hashable], map_fn: Callable[[Hashable], Hashable]
) -> dict[Hashable, tuple[Hashable, ...]]:
    """Alias emphasizing the equivalence partition induced by a state map."""
    return observation_partition(states, map_fn)


def deterministic_time_partition_coarsens(
    states: list[Hashable],
    earlier_map: Callable[[Hashable], Hashable],
    transition: Callable[[Hashable], Hashable],
) -> bool:
    """Verify that one deterministic postcomposition coarsens the kernel partition.

    If F_next = transition o F_earlier, any pair already merged by F_earlier
    remains merged by F_next.  This is the time-direction counterpart of
    precision refinement, where later observation partitions refine earlier ones.
    """
    _unique_states(states)
    later_map = lambda state: transition(earlier_map(state))
    # A coarsening means equality earlier implies equality later.
    for left in states:
        for right in states:
            if earlier_map(left) == earlier_map(right):
                if later_map(left) != later_map(right):
                    return False
    return True


def product_observation(
    first: Callable[[Hashable], Hashable],
    second: Callable[[Hashable], Hashable],
) -> Callable[[Hashable], tuple[Hashable, Hashable]]:
    """Return the product of two precision observations on the same terminal set."""
    return lambda state: (first(state), second(state))


def product_fiber_identity(
    states: list[Hashable],
    first: Callable[[Hashable], Hashable],
    second: Callable[[Hashable], Hashable],
    state: Hashable,
) -> dict[str, object]:
    """Verify that a product-precision fiber is the intersection of axis fibers."""
    first_fiber = set(observation_fiber(states, first, state))
    second_fiber = set(observation_fiber(states, second, state))
    product = product_observation(first, second)
    product_fiber = set(observation_fiber(states, product, state))
    intersection = first_fiber.intersection(second_fiber)
    if product_fiber != intersection:
        raise AssertionError("product precision fiber is not the axis intersection")
    return {
        "first_fiber": tuple(first_fiber),
        "second_fiber": tuple(second_fiber),
        "product_fiber": tuple(product_fiber),
        "product_ambiguity": len(product_fiber),
        "first_ambiguity": len(first_fiber),
        "second_ambiguity": len(second_fiber),
    }
