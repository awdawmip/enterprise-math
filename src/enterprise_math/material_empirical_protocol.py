"""Finite empirical material protocol machine backed by the canonical P023 quotient.

This module is deliberately narrower than a constitutive law.  It turns an
*explicitly observed finite protocol graph* into a deterministic finite
input/output system and delegates future-state minimization to P023.

The intended cyclic-material workflow is:

    measured protocol states
        -> explicit NEXT transitions
        -> current (deformation,response) observation
        -> P023 stable future partition.

A missing measured successor is never interpolated.  It enters one explicit
``UNDERRESOLVED`` sink whose observation stays distinguishable from every
measured material sample.  Consequently the resulting quotient describes the
minimum memory needed by the *declared empirical prediction interface*; it does
not prove that two physical histories behind an underresolved boundary are truly
equivalent.

This is useful for Mullins/cyclic data because candidate labels such as
``historical_peak`` or ``cycle_count`` need not be declared permanent state
coordinates.  If two measured histories have identical current response but
different measured futures, P023 splits them.  If later histories have identical
current and future protocol behaviour, P023 merges them automatically.
"""

from __future__ import annotations

from dataclasses import dataclass

from .operation_quotient import class_count, family_descends, stable_family_partition

UNDERRESOLVED_STATE = "__MATERIAL_PROTOCOL_UNDERRESOLVED__"
NEXT_PROTOCOL_STEP = "NEXT_PROTOCOL_STEP"


@dataclass(frozen=True)
class EmpiricalProtocolSample:
    state_id: str
    deformation_index: int
    response_sample: int
    next_state_id: str | None

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
        if self.next_state_id is not None and (
            not isinstance(self.next_state_id, str) or not self.next_state_id
        ):
            raise ValueError("next_state_id must be None or a nonempty string")


@dataclass(frozen=True)
class EmpiricalMaterialProtocolMachine:
    measured_state_ids: tuple[str, ...]
    domain: tuple[str, ...]
    next_operation: dict[str, str]
    current_observation: dict[str, tuple[object, ...]]
    stable_partition: dict[str, int]
    current_class_count: int
    stable_class_count: int


def compile_empirical_material_protocol(
    samples: tuple[EmpiricalProtocolSample, ...] | list[EmpiricalProtocolSample],
) -> EmpiricalMaterialProtocolMachine:
    """Compile one finite measured protocol graph and minimize its future memory.

    Every explicit successor must name another measured state.  ``None`` means
    that the experiment stops at that point; the transition is completed by the
    explicit UNDERRESOLVED sink rather than by extrapolation or wraparound.
    """
    records = tuple(samples)
    if not records:
        raise ValueError("at least one empirical protocol sample is required")
    ids = tuple(record.state_id for record in records)
    if len(ids) != len(set(ids)):
        raise ValueError("empirical protocol state ids must be unique")
    id_set = set(ids)
    for record in records:
        if record.next_state_id is not None and record.next_state_id not in id_set:
            raise ValueError("explicit next_state_id must name a measured state")

    domain = ids + (UNDERRESOLVED_STATE,)
    next_operation = {
        record.state_id: (
            UNDERRESOLVED_STATE
            if record.next_state_id is None
            else record.next_state_id
        )
        for record in records
    }
    next_operation[UNDERRESOLVED_STATE] = UNDERRESOLVED_STATE

    current_observation = {
        record.state_id: (
            "MEASURED",
            record.deformation_index,
            record.response_sample,
        )
        for record in records
    }
    current_observation[UNDERRESOLVED_STATE] = ("UNDERRESOLVED",)

    operations = {NEXT_PROTOCOL_STEP: next_operation}
    stable = stable_family_partition(domain, operations, current_observation)
    if not family_descends(domain, operations, stable):
        raise AssertionError("P023 empirical protocol partition did not support NEXT")
    return EmpiricalMaterialProtocolMachine(
        measured_state_ids=ids,
        domain=domain,
        next_operation=next_operation,
        current_observation=current_observation,
        stable_partition=stable,
        current_class_count=class_count(current_observation),
        stable_class_count=class_count(stable),
    )


def protocol_states_future_equivalent(
    machine: EmpiricalMaterialProtocolMachine,
    left: str,
    right: str,
) -> bool:
    """Whether two protocol states occupy the same P023 stable future class."""
    if left not in machine.stable_partition or right not in machine.stable_partition:
        raise ValueError("states must belong to the compiled empirical protocol")
    return machine.stable_partition[left] == machine.stable_partition[right]


def first_future_observation_difference(
    machine: EmpiricalMaterialProtocolMachine,
    left: str,
    right: str,
) -> int | None:
    """Return the first NEXT depth at which two observations differ, if any.

    ``0`` means the current measured observations already differ.  Because the
    compiled protocol is finite and deterministic, if no difference appears
    within one pair-state repetition horizon then the two infinite NEXT traces
    are identical and ``None`` is returned.
    """
    if left not in machine.current_observation or right not in machine.current_observation:
        raise ValueError("states must belong to the compiled empirical protocol")
    a = left
    b = right
    seen: set[tuple[str, str]] = set()
    depth = 0
    while (a, b) not in seen:
        if machine.current_observation[a] != machine.current_observation[b]:
            return depth
        seen.add((a, b))
        a = machine.next_operation[a]
        b = machine.next_operation[b]
        depth += 1
    return None
