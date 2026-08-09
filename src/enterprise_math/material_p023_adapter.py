"""Compile finite peak-history material memory into the P023 operation quotient.

E001 should not own another generic automaton minimizer.  P023 already proves and
implements finite operation-family future refinement.  This module is only the
material adapter:

    peak-aware material states
        -> finite P023 domain,
    declared next-deformation commands
        -> deterministic endomaps,
    declared material observation
        -> initial partition,
    P023 stable_family_partition
        -> coarsest future-safe material-history classes.

The default observation retains current deformation index plus response sample,
so this adapter minimizes *history memory* rather than merging distinct geometry
states merely because their current responses coincide.  Branch and historical
peak may optionally be declared observable too.

A command family is accepted only when every command is total on the represented
material state domain.  Missing peak classes therefore remain explicit model
underresolution; they are never filled by interpolation.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import LOADING, RETURNING, MaterialBranch
from .material_peak_memory import (
    PeakConditionedMaterialFamily,
    PeakHistoryMaterialState,
    advance_peak_history_material,
    peak_history_material_state,
)
from .operation_quotient import class_count, family_descends, stable_family_partition

PeakMachineState = tuple[int, MaterialBranch, int]


@dataclass(frozen=True)
class PeakMaterialP023System:
    domain: tuple[PeakMachineState, ...]
    command_indices: tuple[int, ...]
    operations: dict[int, dict[PeakMachineState, PeakMachineState]]
    initial_partition: dict[PeakMachineState, tuple[object, ...]]
    stable_partition: dict[PeakMachineState, int]
    initial_class_count: int
    stable_class_count: int


def _represented_peaks(family: PeakConditionedMaterialFamily) -> tuple[int, ...]:
    return tuple(peak for peak, _profile in family.peak_profiles)


def _domain_states(family: PeakConditionedMaterialFamily) -> tuple[PeakMachineState, ...]:
    states: list[PeakMachineState] = []
    for peak in _represented_peaks(family):
        for index in range(peak + 1):
            for branch in (LOADING, RETURNING):
                states.append((index, branch, peak))
    return tuple(states)


def _material_state(
    family: PeakConditionedMaterialFamily,
    state: PeakMachineState,
) -> PeakHistoryMaterialState:
    index, branch, peak = state
    return peak_history_material_state(family, index, branch, peak)


def compile_peak_material_p023_system(
    family: PeakConditionedMaterialFamily,
    command_indices: tuple[int, ...] | list[int],
    include_branch_observation: bool = False,
    include_peak_observation: bool = False,
) -> PeakMaterialP023System:
    """Compile and minimize one declared finite peak-history material operation language."""
    commands = tuple(command_indices)
    if not commands:
        raise ValueError("at least one deformation command is required")
    if len(commands) != len(set(commands)):
        raise ValueError("deformation commands must be distinct")
    for command in commands:
        if (
            isinstance(command, bool)
            or not isinstance(command, int)
            or not 0 <= command < family.deformation_count
        ):
            raise ValueError("deformation command lies outside the material domain")

    domain = _domain_states(family)
    operations: dict[int, dict[PeakMachineState, PeakMachineState]] = {}
    for command in commands:
        operation: dict[PeakMachineState, PeakMachineState] = {}
        for state in domain:
            current = _material_state(family, state)
            try:
                nxt = advance_peak_history_material(family, current, command)
            except ValueError as exc:
                raise ValueError(
                    f"deformation command {command} is not total on represented peak states"
                ) from exc
            next_key = (nxt.deformation_index, nxt.branch, nxt.historical_peak)
            if next_key not in set(domain):
                raise AssertionError("peak material transition escaped represented P023 domain")
            operation[state] = next_key
        operations[command] = operation

    initial: dict[PeakMachineState, tuple[object, ...]] = {}
    for state in domain:
        material = _material_state(family, state)
        label: list[object] = [material.deformation_index, material.response_sample]
        if include_branch_observation:
            label.append(material.branch)
        if include_peak_observation:
            label.append(material.historical_peak)
        initial[state] = tuple(label)

    stable = stable_family_partition(domain, operations, initial)
    if not family_descends(domain, operations, stable):
        raise AssertionError("P023 stable material partition did not support all commands")
    return PeakMaterialP023System(
        domain=domain,
        command_indices=commands,
        operations=operations,
        initial_partition=initial,
        stable_partition=stable,
        initial_class_count=class_count(initial),
        stable_class_count=class_count(stable),
    )


def states_future_equivalent(
    system: PeakMaterialP023System,
    left: PeakMachineState,
    right: PeakMachineState,
) -> bool:
    """Whether two represented material histories occupy one P023 stable class."""
    if left not in system.stable_partition or right not in system.stable_partition:
        raise ValueError("states must belong to the compiled material system")
    return system.stable_partition[left] == system.stable_partition[right]
