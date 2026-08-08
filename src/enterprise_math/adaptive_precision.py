"""Adaptive finite precision selection for Enterprise Math P018 stage 6.

The module works on one finite terminal state set and a family of finite
observations.  It distinguishes raw ambiguity reduction from predicate-specific
conflict reduction, then solves finite target-state and worst-case decision
problems with integer costs.

Decision-tree optimization and dynamic programming are established ideas.  P018
uses them here only on finite precision observations/fibers; no probability,
expected value, real-valued information measure, or infinite precision limit is
required.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable
from functools import lru_cache

from .precision_system import (
    ambiguity_multiplicity,
    observation_fiber,
    predicate_fiber_certificate,
    refinement_projection,
    TRUE,
    FALSE,
    UNRESOLVED,
)

Observation = Callable[[Hashable], Hashable]
Predicate = Callable[[Hashable], bool]


def _validate_states(states: list[Hashable], state: Hashable | None = None) -> None:
    if not states:
        raise ValueError("terminal state set must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("terminal states must be distinct")
    if state is not None and state not in states:
        raise ValueError("state must belong to terminal state set")


def _validate_costs(observations: dict[str, Observation], costs: dict[str, int]) -> None:
    if set(observations) != set(costs):
        raise ValueError("costs must be supplied for exactly the observation names")
    for name, cost in costs.items():
        if isinstance(cost, bool) or not isinstance(cost, int) or cost <= 0:
            raise ValueError(f"cost for {name} must be a positive integer")


def predicate_conflict_fiber(
    states: list[Hashable],
    observation: Observation,
    predicate: Predicate,
    state: Hashable,
) -> tuple[Hashable, ...]:
    """Return compatible terminal states with predicate truth opposite to state."""
    _validate_states(states, state)
    truth = bool(predicate(state))
    return tuple(
        candidate
        for candidate in observation_fiber(states, observation, state)
        if bool(predicate(candidate)) != truth
    )


def conflict_multiplicity(
    states: list[Hashable],
    observation: Observation,
    predicate: Predicate,
    state: Hashable,
) -> int:
    """Number of currently compatible states that could overturn the predicate."""
    return len(predicate_conflict_fiber(states, observation, predicate, state))


def conflict_profile(
    states: list[Hashable],
    observations: list[Observation],
    predicate: Predicate,
    state: Hashable,
) -> list[int]:
    """Return nonincreasing predicate-conflict multiplicity along a refinement chain."""
    _validate_states(states, state)
    if not observations:
        raise ValueError("at least one observation is required")
    counts: list[int] = []
    previous = observations[0]
    last: int | None = None
    for observation in observations:
        refinement_projection(states, previous, observation)
        count = conflict_multiplicity(states, observation, predicate, state)
        if last is not None and count > last:
            raise AssertionError("predicate conflict increased under refinement")
        counts.append(count)
        last = count
        previous = observation
    return counts


def refinement_proof_gain(
    states: list[Hashable],
    coarse: Observation,
    fine: Observation,
    predicate: Predicate,
    state: Hashable,
) -> dict[str, int | bool | str]:
    """Compare raw ambiguity gain with predicate-specific conflict gain."""
    _validate_states(states, state)
    refinement_projection(states, coarse, fine)
    ambiguity_before = ambiguity_multiplicity(states, coarse, state)
    ambiguity_after = ambiguity_multiplicity(states, fine, state)
    conflict_before = conflict_multiplicity(states, coarse, predicate, state)
    conflict_after = conflict_multiplicity(states, fine, predicate, state)
    if ambiguity_after > ambiguity_before or conflict_after > conflict_before:
        raise AssertionError("refinement increased an uncertainty count")
    certificate = predicate_fiber_certificate(states, fine, predicate, state)
    return {
        "ambiguity_before": ambiguity_before,
        "ambiguity_after": ambiguity_after,
        "ambiguity_gain": ambiguity_before - ambiguity_after,
        "conflict_before": conflict_before,
        "conflict_after": conflict_after,
        "conflict_gain": conflict_before - conflict_after,
        "decides": certificate != UNRESOLVED,
        "certificate": certificate,
    }


def product_observations(observations: list[Observation]) -> Observation:
    """Combine finitely many precision axes into one tuple-valued observation."""
    if not observations:
        return lambda _state: ()
    return lambda state: tuple(observation(state) for observation in observations)


def product_conflict_bound(
    states: list[Hashable],
    observations: list[Observation],
    predicate: Predicate,
    state: Hashable,
) -> dict[str, object]:
    """Verify that joint precision cannot have more predicate conflict than any axis."""
    _validate_states(states, state)
    if not observations:
        raise ValueError("at least one observation is required")
    joint = product_observations(observations)
    joint_conflict = conflict_multiplicity(states, joint, predicate, state)
    axis_conflicts = [
        conflict_multiplicity(states, observation, predicate, state)
        for observation in observations
    ]
    if any(joint_conflict > count for count in axis_conflicts):
        raise AssertionError("product precision increased predicate conflict")
    return {"joint_conflict": joint_conflict, "axis_conflicts": axis_conflicts}


def joint_predicate_complete(
    states: list[Hashable],
    observations: dict[str, Observation],
    predicate: Predicate,
) -> bool:
    """Whether all supplied observations together determine the predicate."""
    _validate_states(states)
    joint = product_observations(list(observations.values()))
    truth_by_key: dict[Hashable, bool] = {}
    for state in states:
        key = joint(state)
        truth = bool(predicate(state))
        previous = truth_by_key.get(key, truth)
        if previous != truth:
            return False
        truth_by_key[key] = truth
    return True


def _restricted_block(
    block: frozenset[Hashable], observation: Observation, state: Hashable
) -> frozenset[Hashable]:
    key = observation(state)
    return frozenset(candidate for candidate in block if observation(candidate) == key)


def _predicate_constant(block: frozenset[Hashable], predicate: Predicate) -> bool:
    return len({bool(predicate(state)) for state in block}) <= 1


def optimal_target_decision_cost(
    states: list[Hashable],
    observations: dict[str, Observation],
    costs: dict[str, int],
    predicate: Predicate,
    state: Hashable,
) -> int | None:
    """Minimum integer observation cost needed to decide the predicate for one state.

    The actual state is fixed.  Choosing an observation reveals the observation
    value of that state and therefore replaces the current block by the matching
    sub-block.  ``None`` means the available observations cannot decide the
    predicate at this state.
    """
    _validate_states(states, state)
    _validate_costs(observations, costs)
    names = tuple(sorted(observations))

    @lru_cache(maxsize=None)
    def solve(block: frozenset[Hashable], remaining: tuple[str, ...]) -> int | None:
        if _predicate_constant(block, predicate):
            return 0
        best: int | None = None
        for index, name in enumerate(remaining):
            next_block = _restricted_block(block, observations[name], state)
            if next_block == block:
                continue
            next_remaining = remaining[:index] + remaining[index + 1 :]
            tail = solve(next_block, next_remaining)
            if tail is None:
                continue
            candidate = costs[name] + tail
            if best is None or candidate < best:
                best = candidate
        return best

    return solve(frozenset(states), names)


def optimal_target_first_observation(
    states: list[Hashable],
    observations: dict[str, Observation],
    costs: dict[str, int],
    predicate: Predicate,
    state: Hashable,
) -> tuple[str, int] | None:
    """Return one cost-optimal first observation for the fixed target state."""
    _validate_states(states, state)
    _validate_costs(observations, costs)
    names = tuple(sorted(observations))

    @lru_cache(maxsize=None)
    def solve(block: frozenset[Hashable], remaining: tuple[str, ...]) -> int | None:
        if _predicate_constant(block, predicate):
            return 0
        best: int | None = None
        for index, name in enumerate(remaining):
            next_block = _restricted_block(block, observations[name], state)
            if next_block == block:
                continue
            next_remaining = remaining[:index] + remaining[index + 1 :]
            tail = solve(next_block, next_remaining)
            if tail is None:
                continue
            candidate = costs[name] + tail
            if best is None or candidate < best:
                best = candidate
        return best

    initial = frozenset(states)
    if _predicate_constant(initial, predicate):
        return None
    best_pair: tuple[str, int] | None = None
    for index, name in enumerate(names):
        next_block = _restricted_block(initial, observations[name], state)
        if next_block == initial:
            continue
        tail = solve(next_block, names[:index] + names[index + 1 :])
        if tail is None:
            continue
        total = costs[name] + tail
        if best_pair is None or total < best_pair[1] or (
            total == best_pair[1] and name < best_pair[0]
        ):
            best_pair = (name, total)
    return best_pair


def _observation_blocks(
    block: frozenset[Hashable], observation: Observation
) -> tuple[frozenset[Hashable], ...]:
    groups: dict[Hashable, set[Hashable]] = {}
    for state in block:
        groups.setdefault(observation(state), set()).add(state)
    return tuple(frozenset(group) for group in groups.values())


def optimal_worst_case_decision_cost(
    states: list[Hashable],
    observations: dict[str, Observation],
    costs: dict[str, int],
    predicate: Predicate,
) -> int | None:
    """Minimum worst-case integer cost of a finite predicate decision tree.

    No probability distribution is assumed.  At each node an observation is
    chosen; its possible finite values branch the current terminal-state block.
    The recurrence minimizes observation cost plus the maximum unresolved child
    cost.  ``None`` means the supplied observations are not predicate-complete.
    """
    _validate_states(states)
    _validate_costs(observations, costs)
    names = tuple(sorted(observations))

    @lru_cache(maxsize=None)
    def solve(block: frozenset[Hashable], remaining: tuple[str, ...]) -> int | None:
        if _predicate_constant(block, predicate):
            return 0
        best: int | None = None
        for index, name in enumerate(remaining):
            children = _observation_blocks(block, observations[name])
            if len(children) <= 1:
                continue
            next_remaining = remaining[:index] + remaining[index + 1 :]
            child_costs: list[int] = []
            feasible = True
            for child in children:
                tail = solve(child, next_remaining)
                if tail is None:
                    feasible = False
                    break
                child_costs.append(tail)
            if not feasible:
                continue
            candidate = costs[name] + max(child_costs, default=0)
            if best is None or candidate < best:
                best = candidate
        return best

    return solve(frozenset(states), names)


def complete_observation_cost_bound(
    states: list[Hashable],
    observations: dict[str, Observation],
    costs: dict[str, int],
    predicate: Predicate,
) -> dict[str, int | bool | None]:
    """Verify the finite sum-of-costs bound when the joint observation is complete."""
    _validate_states(states)
    _validate_costs(observations, costs)
    complete = joint_predicate_complete(states, observations, predicate)
    optimal = optimal_worst_case_decision_cost(states, observations, costs, predicate)
    total = sum(costs.values())
    if complete:
        if optimal is None or optimal > total:
            raise AssertionError("complete finite observation family violated cost bound")
    elif optimal is not None:
        raise AssertionError("incomplete joint observation unexpectedly decided predicate")
    return {"joint_complete": complete, "optimal_cost": optimal, "sum_cost_bound": total}
