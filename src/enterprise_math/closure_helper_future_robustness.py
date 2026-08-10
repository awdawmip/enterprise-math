"""Future-operation-relative validity of sequential helper caches.

For helper e_j in the sequential k-way conjunction compiler, the semantic
meaning is the raw prefix a_1&...&a_j.  A present helper is prefix-valid when
all of those raw antecedents are currently present.

If raw output z is not already true, prefix-validity of every retained helper is
exactly the invariant needed to preserve the pure raw closure under *all future
monotone additions of raw antecedents*.  A stale helper can be harmless for the
current endpoint yet unsafe for a richer future that may add the missing suffix.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .closure_helper_state_boundary import pure_synergy_states
from .closure_implication_bases import forward_chaining_trace
from .closure_implication_circuits import closure_of
from .closure_synergy_depth import synergy_chain


@dataclass(frozen=True)
class HelperRobustnessReport:
    arity: int
    internal_state: frozenset[str]
    raw_projection: frozenset[str]
    current_projection_correct: bool
    prefix_validity: bool
    future_robust_under_raw_additions: bool
    violating_addition: frozenset[str] | None


def _raw_projection(state: frozenset[str], raw_labels: frozenset[str]) -> frozenset[str]:
    return frozenset(label for label in state if label in raw_labels)


def prefix_validity_holds(arity: int, state: frozenset[str]) -> bool:
    """Every present e_j has its intended raw prefix currently present."""
    for j in range(2, arity):
        helper = f"e{j}"
        if helper in state:
            prefix = {f"a{i}" for i in range(1, j + 1)}
            if not prefix.issubset(state):
                return False
    return True


def helper_robustness_report(arity: int, state: frozenset[str]) -> HelperRobustnessReport:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 3:
        raise ValueError("arity must be an integer >= 3")
    compiled = synergy_chain(arity)
    universe = frozenset(compiled.labels)
    if not state.issubset(universe):
        raise ValueError("state contains labels outside the compiled universe")

    raw_labels_tuple, raw_states = pure_synergy_states(arity)
    raw_labels = frozenset(raw_labels_tuple)
    raw = _raw_projection(state, raw_labels)

    current_final = forward_chaining_trace(state, compiled.rules)[-1]
    current_projection = _raw_projection(current_final, raw_labels)
    expected_current = closure_of(raw_labels_tuple, raw_states, raw)
    current_ok = current_projection == expected_current

    # Test all monotone future additions of raw antecedents only.  z is an
    # output/raw state coordinate, not an exogenous antecedent action here.
    antecedents = tuple(f"a{i}" for i in range(1, arity + 1))
    missing = tuple(label for label in antecedents if label not in raw)
    violating = None
    robust = True
    for size in range(len(missing) + 1):
        for addition_tuple in combinations(missing, size):
            addition = frozenset(addition_tuple)
            extended_internal = frozenset(set(state) | set(addition))
            final = forward_chaining_trace(extended_internal, compiled.rules)[-1]
            projected = _raw_projection(final, raw_labels)
            expected = closure_of(raw_labels_tuple, raw_states, frozenset(set(raw) | set(addition)))
            if projected != expected:
                robust = False
                violating = addition
                break
        if not robust:
            break

    valid = prefix_validity_holds(arity, state)
    # If z is already raw-true, helpers cannot change any further raw label.
    expected_robust = ("z" in raw) or valid
    if robust != expected_robust:
        raise AssertionError("future robustness must equal output-true OR prefix-validity")

    return HelperRobustnessReport(
        arity=arity,
        internal_state=state,
        raw_projection=raw,
        current_projection_correct=current_ok,
        prefix_validity=valid,
        future_robust_under_raw_additions=robust,
        violating_addition=violating,
    )
