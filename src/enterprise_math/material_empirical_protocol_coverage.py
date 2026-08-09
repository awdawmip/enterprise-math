"""Finite measured-horizon coverage of a multi-action material protocol.

The stable P023 quotient answers which measured histories are predictively
indistinguishable for the declared action/observation language.  A separate
question is whether those predictions remain inside the actually measured
protocol graph.

For each measured state this module finds the shortest declared action word that
reaches the explicit ``UNDERRESOLVED`` sink.  ``None`` means no finite action
word can leave the measured subgraph from that state.  The corresponding states
form the maximal action-closed measured region of this finite protocol machine.

This is an experimental-coverage diagnostic.  It neither interpolates missing
successors nor interprets the action-closed region as a complete physical state
space.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass

from .material_empirical_action_protocol import (
    EmpiricalActionProtocolMachine,
    UNDERRESOLVED_STATE,
)


@dataclass(frozen=True)
class ProtocolCoverageState:
    state_id: str
    first_underresolved_depth: int | None
    shortest_underresolved_word: tuple[str, ...] | None

    @property
    def fully_measured_for_all_finite_words(self) -> bool:
        return self.first_underresolved_depth is None


@dataclass(frozen=True)
class EmpiricalProtocolCoverage:
    action_names: tuple[str, ...]
    states: tuple[ProtocolCoverageState, ...]
    fully_measured_state_ids: tuple[str, ...]
    eventually_underresolved_state_ids: tuple[str, ...]


def shortest_underresolved_action_word(
    machine: EmpiricalActionProtocolMachine,
    state_id: str,
) -> tuple[str, ...] | None:
    """Return a shortest action word reaching UNDERRESOLVED, or None if impossible."""
    if state_id not in machine.measured_state_ids:
        raise ValueError("state_id must name a measured protocol state")

    queue: deque[tuple[str, tuple[str, ...]]] = deque([(state_id, ())])
    seen = {state_id}
    while queue:
        state, word = queue.popleft()
        for action in machine.action_names:
            successor = machine.operations[action][state]
            next_word = word + (action,)
            if successor == UNDERRESOLVED_STATE:
                return next_word
            if successor not in seen:
                seen.add(successor)
                queue.append((successor, next_word))
    return None


def empirical_protocol_coverage(
    machine: EmpiricalActionProtocolMachine,
) -> EmpiricalProtocolCoverage:
    """Return exact measured-future coverage for every measured start state."""
    reports: list[ProtocolCoverageState] = []
    fully: list[str] = []
    finite: list[str] = []
    for state_id in sorted(machine.measured_state_ids):
        witness = shortest_underresolved_action_word(machine, state_id)
        if witness is None:
            fully.append(state_id)
            depth = None
        else:
            finite.append(state_id)
            depth = len(witness)
        reports.append(
            ProtocolCoverageState(
                state_id=state_id,
                first_underresolved_depth=depth,
                shortest_underresolved_word=witness,
            )
        )
    return EmpiricalProtocolCoverage(
        action_names=machine.action_names,
        states=tuple(reports),
        fully_measured_state_ids=tuple(fully),
        eventually_underresolved_state_ids=tuple(finite),
    )
