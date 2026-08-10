"""Auxiliary-state boundary for reducing implication premise arity.

A pure k-way closure on raw labels a_1,...,a_k,z has only the nontrivial law
{a_1,...,a_k} -> z.  If the rule/state alphabet is fixed, iterative depth alone
cannot lower this premise arity: there is no intermediate semantic consequence
to derive.

Adding k-2 helper labels permits the binary synergy-chain compilation from
Supplement 135, preserving the closure observed on the raw labels while paying
auxiliary state and derivation depth.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .closure_implication_bases import Implication, forward_chaining_trace
from .closure_implication_circuits import RootedCircuit, closure_of, rooted_circuits
from .closure_synergy_depth import synergy_chain


@dataclass(frozen=True)
class HelperStateTradeoff:
    raw_arity: int
    raw_label_count: int
    raw_nontrivial_circuit_count: int
    fixed_alphabet_required_premise_arity: int
    helper_label_count: int
    compiled_max_premise_arity: int
    compiled_depth: int
    raw_projection_verified: bool


def _powerset(items: tuple[str, ...]):
    for size in range(len(items) + 1):
        for subset in combinations(items, size):
            yield frozenset(subset)


def pure_synergy_states(arity: int) -> tuple[tuple[str, ...], tuple[frozenset[str], ...]]:
    """All states closed under the sole raw law A_k -> z."""
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 2:
        raise ValueError("arity must be an integer >= 2")
    antecedents = tuple(f"a{i}" for i in range(1, arity + 1))
    root = "z"
    labels = antecedents + (root,)
    antecedent_set = frozenset(antecedents)
    states = tuple(
        state
        for state in _powerset(labels)
        if not antecedent_set.issubset(state) or root in state
    )
    return labels, states


def pure_nontrivial_circuits(arity: int) -> tuple[RootedCircuit, ...]:
    labels, states = pure_synergy_states(arity)
    return rooted_circuits(labels, states)


def helper_state_tradeoff(arity: int) -> HelperStateTradeoff:
    raw_labels, raw_states = pure_synergy_states(arity)
    raw_antecedents = frozenset(raw_labels[:-1])
    root = raw_labels[-1]
    circuits = pure_nontrivial_circuits(arity)
    expected = RootedCircuit(raw_antecedents, root)
    if set(circuits) != {expected}:
        raise AssertionError("pure synergy closure must have exactly one nontrivial rooted circuit")

    compiled = synergy_chain(arity)
    raw_projection_verified = True
    for seed in _powerset(raw_labels):
        raw_target = closure_of(raw_labels, raw_states, seed)
        compiled_final = forward_chaining_trace(seed, compiled.rules)[-1]
        projected = frozenset(label for label in compiled_final if label in raw_labels)
        if projected != raw_target:
            raw_projection_verified = False
            break

    return HelperStateTradeoff(
        raw_arity=arity,
        raw_label_count=len(raw_labels),
        raw_nontrivial_circuit_count=len(circuits),
        fixed_alphabet_required_premise_arity=arity,
        helper_label_count=max(0, arity - 2),
        compiled_max_premise_arity=max(len(rule.premise) for rule in compiled.rules),
        compiled_depth=arity - 1,
        raw_projection_verified=raw_projection_verified,
    )
