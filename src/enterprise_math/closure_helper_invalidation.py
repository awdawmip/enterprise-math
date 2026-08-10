"""Cross-job invalidation boundary for sequential helper caches.

A helper value that was legally derived in one raw job can become stale after
raw inputs are replaced.  Retaining a stale helper can bypass missing raw
antecedents in the next job and spuriously derive the output.

For the sequential k-way compiler, every helper e_j is individually unsafe to
retain across arbitrary job replacement.  Therefore a fixed deletion-only reset
policy that must be correct for all prior/next raw jobs must clear all k-2
helpers (unless some stronger versioning/validation mechanism is introduced).
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_helper_state_boundary import pure_synergy_states
from .closure_implication_bases import forward_chaining_trace
from .closure_implication_circuits import closure_of
from .closure_synergy_depth import synergy_chain


@dataclass(frozen=True)
class StaleHelperCounterexample:
    arity: int
    helper: str
    prior_raw_seed: frozenset[str]
    prior_saturated_state: frozenset[str]
    next_raw_seed: frozenset[str]
    stale_internal_seed: frozenset[str]
    stale_compiled_raw_projection: frozenset[str]
    expected_next_raw_closure: frozenset[str]
    corrupts_raw_semantics: bool


def stale_helper_counterexample(arity: int, helper_index: int) -> StaleHelperCounterexample:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 3:
        raise ValueError("arity must be an integer >= 3")
    if isinstance(helper_index, bool) or not isinstance(helper_index, int) or not 2 <= helper_index <= arity - 1:
        raise ValueError("helper_index must lie in 2..arity-1")

    compiled = synergy_chain(arity)
    helper = f"e{helper_index}"
    prior_raw_seed = frozenset(f"a{i}" for i in range(1, helper_index + 1))
    prior_saturated = forward_chaining_trace(prior_raw_seed, compiled.rules)[-1]
    if helper not in prior_saturated:
        raise AssertionError("chosen prior job must legally generate the helper")

    next_raw_seed = frozenset(f"a{i}" for i in range(helper_index + 1, arity + 1))
    stale_internal_seed = frozenset(set(next_raw_seed) | {helper})
    stale_final = forward_chaining_trace(stale_internal_seed, compiled.rules)[-1]

    raw_labels_tuple, raw_states = pure_synergy_states(arity)
    raw_labels = frozenset(raw_labels_tuple)
    stale_projection = frozenset(label for label in stale_final if label in raw_labels)
    expected = closure_of(raw_labels_tuple, raw_states, next_raw_seed)

    return StaleHelperCounterexample(
        arity=arity,
        helper=helper,
        prior_raw_seed=prior_raw_seed,
        prior_saturated_state=prior_saturated,
        next_raw_seed=next_raw_seed,
        stale_internal_seed=stale_internal_seed,
        stale_compiled_raw_projection=stale_projection,
        expected_next_raw_closure=expected,
        corrupts_raw_semantics=stale_projection != expected,
    )


def required_fixed_helper_reset_count(arity: int) -> int:
    """Every helper has its own stale-cache counterexample, so all must clear."""
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 3:
        raise ValueError("arity must be an integer >= 3")
    for helper_index in range(2, arity):
        if not stale_helper_counterexample(arity, helper_index).corrupts_raw_semantics:
            raise AssertionError("every sequential helper must be unsafe under some job replacement")
    return arity - 2
