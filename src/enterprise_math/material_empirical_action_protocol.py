"""Multi-action empirical material protocol compiled through canonical P023.

This module is an E001 application adapter, not a new automaton-minimization
algorithm.  It turns one explicitly measured finite protocol graph into a
finite deterministic operation family and delegates future-state minimization
to ``operation_quotient.stable_family_partition``.

Each measured state carries only the currently observed deformation/response
pair plus one explicit successor for every declared protocol action.  ``None``
means that successor was not measured.  Such an edge goes to one explicit
``UNDERRESOLVED`` sink; it is never interpolated, wrapped around, or inferred
from a different protocol branch.

The stable quotient therefore answers a deliberately narrow question:

    what is the minimum finite memory needed to reproduce every future measured
    response under every finite word in this declared action alphabet?

It does not assert that two physical histories merged by this measured protocol
are physically identical outside the declared observations/actions.  Missing
transition diagnostics are retained separately so provenance is not smuggled
into the coarsest predictive state.
"""

from __future__ import annotations

from dataclasses import dataclass

from .operation_quotient import class_count, family_descends, stable_family_partition

UNDERRESOLVED_STATE = "__MATERIAL_ACTION_PROTOCOL_UNDERRESOLVED__"


@dataclass(frozen=True)
class EmpiricalActionProtocolSample:
    """One measured material state with an explicit successor per action."""

    state_id: str
    deformation_index: int
    response_sample: int
    action_successors: tuple[tuple[str, str | None], ...]

    def __post_init__(self) -> None:
        if not isinstance(self.state_id, str) or not self.state_id:
            raise ValueError("state_id must be a nonempty string")
        if self.state_id == UNDERRESOLVED_STATE:
            raise ValueError("state_id uses the reserved underresolved state")
        for name, value in (
            ("deformation_index", self.deformation_index),
            ("response_sample", self.response_sample),
        ):
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"{name} must be a non-negative integer")

        actions: set[str] = set()
        for action, successor in self.action_successors:
            if not isinstance(action, str) or not action:
                raise ValueError("action names must be nonempty strings")
            if action in actions:
                raise ValueError("action names must be unique within one sample")
            actions.add(action)
            if successor is not None:
                if not isinstance(successor, str) or not successor:
                    raise ValueError("successor ids must be None or nonempty strings")
                if successor == UNDERRESOLVED_STATE:
                    raise ValueError("measured samples must not name the reserved sink")


def _successor_map(sample: EmpiricalActionProtocolSample) -> dict[str, str | None]:
    return dict(sample.action_successors)


@dataclass(frozen=True)
class EmpiricalActionProtocolMachine:
    """Finite measured action machine plus its P023 stable predictive quotient."""

    action_names: tuple[str, ...]
    measured_state_ids: tuple[str, ...]
    domain: tuple[str, ...]
    operations: dict[str, dict[str, str]]
    current_observation: dict[str, tuple[object, ...]]
    stable_partition: dict[str, int]
    current_class_count: int
    stable_class_count: int
    missing_transitions: tuple[tuple[str, str], ...]


def compile_empirical_action_protocol(
    samples: tuple[EmpiricalActionProtocolSample, ...]
    | list[EmpiricalActionProtocolSample],
) -> EmpiricalActionProtocolMachine:
    """Compile an explicit multi-action measured graph and minimize future memory.

    Every measured state must declare the same nonempty action alphabet.  A
    successor may be another measured state or ``None``.  ``None`` is completed
    by the distinguished underresolved sink so every action is total, as
    required by the canonical P023 operation-family compiler.
    """
    records = tuple(samples)
    if not records:
        raise ValueError("at least one empirical action-protocol sample is required")

    ids = tuple(record.state_id for record in records)
    if len(ids) != len(set(ids)):
        raise ValueError("empirical protocol state ids must be unique")
    id_set = set(ids)

    successor_maps = tuple(_successor_map(record) for record in records)
    first_actions = set(successor_maps[0])
    if not first_actions:
        raise ValueError("protocol action alphabet must be nonempty")
    for successors in successor_maps[1:]:
        if set(successors) != first_actions:
            raise ValueError("every measured state must declare the same action alphabet")
    action_names = tuple(sorted(first_actions))

    missing: list[tuple[str, str]] = []
    for record, successors in zip(records, successor_maps, strict=True):
        for action in action_names:
            target = successors[action]
            if target is None:
                missing.append((record.state_id, action))
            elif target not in id_set:
                raise ValueError("explicit action successor must name a measured state")

    domain = ids + (UNDERRESOLVED_STATE,)
    operations: dict[str, dict[str, str]] = {}
    for action in action_names:
        operation = {
            record.state_id: (
                UNDERRESOLVED_STATE
                if successors[action] is None
                else successors[action]
            )
            for record, successors in zip(records, successor_maps, strict=True)
        }
        operation[UNDERRESOLVED_STATE] = UNDERRESOLVED_STATE
        operations[action] = operation

    observation = {
        record.state_id: (
            "MEASURED",
            record.deformation_index,
            record.response_sample,
        )
        for record in records
    }
    observation[UNDERRESOLVED_STATE] = ("UNDERRESOLVED",)

    stable = stable_family_partition(domain, operations, observation)
    if not family_descends(domain, operations, stable):
        raise AssertionError("P023 stable empirical partition did not support all actions")

    return EmpiricalActionProtocolMachine(
        action_names=action_names,
        measured_state_ids=ids,
        domain=domain,
        operations=operations,
        current_observation=observation,
        stable_partition=stable,
        current_class_count=class_count(observation),
        stable_class_count=class_count(stable),
        missing_transitions=tuple(sorted(missing)),
    )


def protocol_states_future_equivalent(
    machine: EmpiricalActionProtocolMachine,
    left: str,
    right: str,
) -> bool:
    """Whether two measured histories occupy one stable P023 future class."""
    if left not in machine.stable_partition or right not in machine.stable_partition:
        raise ValueError("states must belong to the compiled empirical protocol")
    return machine.stable_partition[left] == machine.stable_partition[right]


def action_word_observation_trace(
    machine: EmpiricalActionProtocolMachine,
    state: str,
    word: tuple[str, ...] | list[str],
) -> tuple[tuple[object, ...], ...]:
    """Return current and successive observations along one declared action word."""
    if state not in machine.current_observation:
        raise ValueError("state must belong to the compiled empirical protocol")
    current = state
    observations = [machine.current_observation[current]]
    for action in word:
        if action not in machine.operations:
            raise ValueError("action word contains an undeclared protocol action")
        current = machine.operations[action][current]
        observations.append(machine.current_observation[current])
    return tuple(observations)
