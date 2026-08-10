"""Initialization/reachability boundary for auxiliary implication state.

Helper-state compilation preserves a raw closure only under a declared embedding
of raw states into legal internal states (helpers initially absent) and a raw
projection after internal forward chaining.  It need not preserve raw semantics
from arbitrary internal helper valuations.

This is a finite simulation/refinement boundary, not a claim of new generic
transition-system theory.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .closure_helper_state_boundary import pure_synergy_states
from .closure_implication_bases import forward_chaining_trace
from .closure_implication_circuits import closure_of
from .closure_synergy_depth import synergy_chain


@dataclass(frozen=True)
class AuxiliarySimulationReport:
    arity: int
    raw_embedding_verified: bool
    arbitrary_internal_state_counterexample: frozenset[str] | None
    counterexample_raw_projection: frozenset[str] | None
    counterexample_compiled_projection: frozenset[str] | None
    counterexample_expected_raw_closure: frozenset[str] | None


def _powerset(items: tuple[str, ...]):
    for size in range(len(items) + 1):
        for subset in combinations(items, size):
            yield frozenset(subset)


def auxiliary_simulation_report(arity: int) -> AuxiliarySimulationReport:
    """Verify raw-initialized simulation and exhibit unsafe helper initialization."""
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 3:
        raise ValueError("arity must be an integer >= 3")

    raw_labels, raw_states = pure_synergy_states(arity)
    raw_label_set = frozenset(raw_labels)
    compiled = synergy_chain(arity)

    raw_ok = True
    for seed in _powerset(raw_labels):
        expected = closure_of(raw_labels, raw_states, seed)
        final = forward_chaining_trace(seed, compiled.rules)[-1]
        projected = frozenset(label for label in final if label in raw_label_set)
        if projected != expected:
            raw_ok = False
            break

    # In the sequential compiler, final rule is {e_(k-1), a_k} -> z.
    last_helper = f"e{arity-1}"
    last_raw = f"a{arity}"
    internal_seed = frozenset({last_helper, last_raw})
    internal_final = forward_chaining_trace(internal_seed, compiled.rules)[-1]
    raw_projection = frozenset(label for label in internal_seed if label in raw_label_set)
    compiled_projection = frozenset(label for label in internal_final if label in raw_label_set)
    expected_raw = closure_of(raw_labels, raw_states, raw_projection)

    counterexample = internal_seed if compiled_projection != expected_raw else None
    if counterexample is None:
        raise AssertionError("arbitrary helper initialization should violate pure raw simulation")

    return AuxiliarySimulationReport(
        arity=arity,
        raw_embedding_verified=raw_ok,
        arbitrary_internal_state_counterexample=counterexample,
        counterexample_raw_projection=raw_projection,
        counterexample_compiled_projection=compiled_projection,
        counterexample_expected_raw_closure=expected_raw,
    )
