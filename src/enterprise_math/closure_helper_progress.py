"""Exact runtime progress precision inside one raw-projection fiber.

For the sequential k-way helper compiler, start with the first k-1 raw
antecedents and omit the last.  The raw projection never changes, while helpers
e2,...,e_(k-1) appear one per round and then stabilize.  Hence one raw state
fiber contains k-1 legal internal progress states with distinct remaining
rounds to stability.
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_implication_bases import forward_chaining_trace
from .closure_synergy_depth import synergy_chain


@dataclass(frozen=True)
class HelperProgressState:
    round_index: int
    internal_state: frozenset[str]
    raw_projection: frozenset[str]
    remaining_rounds: int


@dataclass(frozen=True)
class HelperProgressReport:
    arity: int
    raw_seed: frozenset[str]
    progress_states: tuple[HelperProgressState, ...]
    raw_projection_constant: bool
    progress_state_count: int
    distinct_remaining_rounds: bool


def helper_progress_report(arity: int) -> HelperProgressReport:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 3:
        raise ValueError("arity must be an integer >= 3")
    compiled = synergy_chain(arity)
    raw_labels = frozenset(compiled.antecedents + (compiled.root,))
    seed = frozenset(compiled.antecedents[:-1])
    trace = forward_chaining_trace(seed, compiled.rules)
    total_updates = len(trace) - 1
    states = tuple(
        HelperProgressState(
            round_index=index,
            internal_state=state,
            raw_projection=frozenset(label for label in state if label in raw_labels),
            remaining_rounds=total_updates - index,
        )
        for index, state in enumerate(trace)
    )
    projections = {item.raw_projection for item in states}
    remaining = {item.remaining_rounds for item in states}
    if len(states) != arity - 1:
        raise AssertionError("sequential missing-last-antecedent trace must have k-1 progress states")
    return HelperProgressReport(
        arity=arity,
        raw_seed=seed,
        progress_states=states,
        raw_projection_constant=len(projections) == 1,
        progress_state_count=len(states),
        distinct_remaining_rounds=len(remaining) == len(states),
    )
