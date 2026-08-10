"""Endpoint-cache versus runtime-memory boundary for legal auxiliary states.

Under legal raw initialization, a deterministic acyclic helper compiler has two
very different semantics depending on the future language:

* at saturated endpoint, helper coordinates are a deterministic section over
  the raw closed state and add no new semantic distinctions;
* during stepwise execution, the same raw projection can occur at different
  helper-progress states with different next-step behavior, so helper state is
  genuine runtime memory.

This module instantiates the boundary on the sequential k-way synergy compiler.
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_helper_state_boundary import pure_synergy_states
from .closure_implication_bases import forward_chaining_trace
from .closure_synergy_depth import synergy_chain


@dataclass(frozen=True)
class HelperCacheMemoryReport:
    arity: int
    raw_closed_state_count: int
    saturated_internal_state_count: int
    saturated_section_injective: bool
    saturated_projection_identity: bool
    transient_seed: frozenset[str]
    transient_left: frozenset[str]
    transient_right: frozenset[str]
    common_raw_projection: frozenset[str]
    left_has_future_update: bool
    right_has_future_update: bool
    runtime_future_separated: bool


def _project_raw(state: frozenset[str], raw_labels: frozenset[str]) -> frozenset[str]:
    return frozenset(label for label in state if label in raw_labels)


def _one_parallel_step(state: frozenset[str], rules) -> frozenset[str]:
    additions = {
        rule.root
        for rule in rules
        if rule.premise.issubset(state) and rule.root not in state
    }
    return frozenset(state.union(additions))


def saturated_helper_section(arity: int) -> dict[frozenset[str], frozenset[str]]:
    """Map each raw closed state to its legally saturated internal cache state."""
    raw_labels_tuple, raw_states = pure_synergy_states(arity)
    raw_labels = frozenset(raw_labels_tuple)
    compiled = synergy_chain(arity)
    section: dict[frozenset[str], frozenset[str]] = {}
    for raw_state in raw_states:
        internal = forward_chaining_trace(raw_state, compiled.rules)[-1]
        if _project_raw(internal, raw_labels) != raw_state:
            raise AssertionError("a raw closed state must project identically after legal saturation")
        section[raw_state] = internal
    return section


def helper_cache_memory_report(arity: int = 4) -> HelperCacheMemoryReport:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4 for the transient fixture")

    raw_labels_tuple, raw_states = pure_synergy_states(arity)
    raw_labels = frozenset(raw_labels_tuple)
    compiled = synergy_chain(arity)
    section = saturated_helper_section(arity)
    image = set(section.values())
    injective = len(image) == len(section)
    projection_identity = all(
        _project_raw(internal, raw_labels) == raw
        for raw, internal in section.items()
    )

    # Keep the final antecedent absent. The sequential compiler can still make
    # progress through e2,e3,... while the raw projection remains unchanged.
    transient_seed = frozenset(f"a{i}" for i in range(1, arity))
    trace = forward_chaining_trace(transient_seed, compiled.rules)
    if len(trace) < 3:
        raise AssertionError("transient fixture must expose at least two helper-progress states")
    left = trace[-2]
    right = trace[-1]
    left_projection = _project_raw(left, raw_labels)
    right_projection = _project_raw(right, raw_labels)
    if left_projection != right_projection:
        raise AssertionError("transient helper states must share the same raw projection")

    left_next = _one_parallel_step(left, compiled.rules)
    right_next = _one_parallel_step(right, compiled.rules)
    left_updates = left_next != left
    right_updates = right_next != right

    return HelperCacheMemoryReport(
        arity=arity,
        raw_closed_state_count=len(raw_states),
        saturated_internal_state_count=len(image),
        saturated_section_injective=injective,
        saturated_projection_identity=projection_identity,
        transient_seed=transient_seed,
        transient_left=left,
        transient_right=right,
        common_raw_projection=left_projection,
        left_has_future_update=left_updates,
        right_has_future_update=right_updates,
        runtime_future_separated=(left_updates != right_updates),
    )
