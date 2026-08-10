"""Local provenance laws for sequential helper states.

The global prefix-validity invariant e_j -> (a_1 & ... & a_j) is equivalent to
local recursive constraints:

    e2 -> a1, a2
    e_j -> e_(j-1), a_j   (j>=3)

Every state reachable from legal raw initialization satisfies these one-sided
provenance laws.  At saturation, helpers additionally satisfy the reverse
forward-rule implications, so each helper is locally equivalent to its
prerequisites.  During transient execution the reverse direction can fail.
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_helper_future_robustness import prefix_validity_holds
from .closure_helper_state_boundary import pure_synergy_states
from .closure_implication_bases import forward_chaining_trace
from .closure_synergy_depth import synergy_chain


@dataclass(frozen=True)
class HelperProvenanceReport:
    arity: int
    reachable_states_checked: int
    all_reachable_locally_sound: bool
    local_global_validity_equivalent: bool
    all_saturated_locally_complete: bool
    transient_reverse_failure_state: frozenset[str]
    transient_reverse_failure_helper: str


def local_provenance_holds(arity: int, state: frozenset[str]) -> bool:
    if "e2" in state and not {"a1", "a2"}.issubset(state):
        return False
    for j in range(3, arity):
        helper = f"e{j}"
        if helper in state and not {f"e{j-1}", f"a{j}"}.issubset(state):
            return False
    return True


def local_cache_complete(arity: int, state: frozenset[str]) -> bool:
    """Reverse direction of every helper rule: prerequisites imply helper."""
    if {"a1", "a2"}.issubset(state) and "e2" not in state:
        return False
    for j in range(3, arity):
        if {f"e{j-1}", f"a{j}"}.issubset(state) and f"e{j}" not in state:
            return False
    return True


def helper_provenance_report(arity: int) -> HelperProvenanceReport:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4")
    compiled = synergy_chain(arity)
    raw_labels, raw_states = pure_synergy_states(arity)

    reachable = []
    for raw_state in raw_states:
        # raw closed seeds are enough to sample every legal helper progress
        # prefix; also include nonclosed raw seeds via arbitrary subsets below.
        reachable.extend(forward_chaining_trace(raw_state, compiled.rules))

    from itertools import combinations

    raw_tuple = tuple(raw_labels)
    for size in range(len(raw_tuple) + 1):
        for subset in combinations(raw_tuple, size):
            reachable.extend(forward_chaining_trace(frozenset(subset), compiled.rules))

    reachable_set = set(reachable)
    all_sound = all(local_provenance_holds(arity, state) for state in reachable_set)

    # Exhaust the full compiled Boolean state space to verify that recursive
    # local provenance is exactly the global prefix-validity condition.
    all_states = []
    labels = tuple(compiled.labels)
    for size in range(len(labels) + 1):
        for subset in combinations(labels, size):
            all_states.append(frozenset(subset))
    equivalent = all(
        local_provenance_holds(arity, state) == prefix_validity_holds(arity, state)
        for state in all_states
    )

    saturated = {
        forward_chaining_trace(raw_state, compiled.rules)[-1]
        for raw_state in raw_states
    }
    saturated_complete = all(
        local_provenance_holds(arity, state) and local_cache_complete(arity, state)
        for state in saturated
    )

    transient_seed = frozenset({"a1", "a2", "a3"})
    trace = forward_chaining_trace(transient_seed, compiled.rules)
    failure_state = trace[1]
    if "e2" not in failure_state or "a3" not in failure_state or "e3" in failure_state:
        raise AssertionError("transient fixture must have prerequisites for e3 before e3 appears")
    if not local_provenance_holds(arity, failure_state) or local_cache_complete(arity, failure_state):
        raise AssertionError("transient state must be provenance-sound but cache-incomplete")

    return HelperProvenanceReport(
        arity=arity,
        reachable_states_checked=len(reachable_set),
        all_reachable_locally_sound=all_sound,
        local_global_validity_equivalent=equivalent,
        all_saturated_locally_complete=saturated_complete,
        transient_reverse_failure_state=failure_state,
        transient_reverse_failure_helper="e3",
    )
