"""Synergy-chain closures separating direct premise arity from iterative arity.

A k-way conjunction a_1&...&a_k can be a rooted direct implication for z while
an equivalent iterative Horn basis uses only binary premises, provided helper
labels encode partial conjunctions.  The price is k-1 parallel derivation
rounds from the raw antecedent seed.

This is classical Horn-circuit compilation.  P025 uses it only as an exact
relation-law precision boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .closure_implication_bases import Implication, basis_report, forward_chaining_trace
from .closure_implication_circuits import RootedCircuit, rooted_circuits


@dataclass(frozen=True)
class SynergyChain:
    antecedents: tuple[str, ...]
    helpers: tuple[str, ...]
    root: str
    labels: tuple[str, ...]
    rules: tuple[Implication, ...]
    exact_states: tuple[frozenset[str], ...]


def _powerset(items: tuple[str, ...]):
    for size in range(len(items) + 1):
        for subset in combinations(items, size):
            yield frozenset(subset)


def closed_states_for_rules(labels: tuple[str, ...], rules: tuple[Implication, ...]) -> tuple[frozenset[str], ...]:
    """Enumerate all subsets already fixed by forward chaining under rules."""
    return tuple(
        state
        for state in _powerset(labels)
        if forward_chaining_trace(state, rules)[-1] == state
    )


def synergy_chain(arity: int) -> SynergyChain:
    """Build a k-way raw conjunction compiled through binary helper rules."""
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 2:
        raise ValueError("arity must be an integer >= 2")
    antecedents = tuple(f"a{i}" for i in range(1, arity + 1))
    root = "z"
    helpers = tuple(f"e{i}" for i in range(2, arity))
    rules: list[Implication] = []
    if arity == 2:
        rules.append(Implication(frozenset(antecedents), root))
    else:
        rules.append(Implication(frozenset({antecedents[0], antecedents[1]}), "e2"))
        for index in range(3, arity):
            rules.append(
                Implication(frozenset({f"e{index-1}", antecedents[index-1]}), f"e{index}")
            )
        rules.append(Implication(frozenset({f"e{arity-1}", antecedents[-1]}), root))
    labels = antecedents + helpers + (root,)
    rule_tuple = tuple(rules)
    exact_states = closed_states_for_rules(labels, rule_tuple)
    return SynergyChain(
        antecedents=antecedents,
        helpers=helpers,
        root=root,
        labels=labels,
        rules=rule_tuple,
        exact_states=exact_states,
    )


def synergy_chain_report(arity: int) -> dict[str, int | bool]:
    chain = synergy_chain(arity)
    report = basis_report(chain.labels, chain.exact_states, chain.rules)
    raw_circuit = RootedCircuit(frozenset(chain.antecedents), chain.root)
    circuits = set(rooted_circuits(chain.labels, chain.exact_states))
    trace = forward_chaining_trace(frozenset(chain.antecedents), chain.rules)
    return {
        "raw_arity": arity,
        "raw_rooted_circuit_present": raw_circuit in circuits,
        "iterative_rule_count": len(chain.rules),
        "iterative_max_premise_arity": max(len(rule.premise) for rule in chain.rules),
        "raw_seed_derivation_rounds": len(trace) - 1,
        "basis_sound": report.sound,
        "basis_complete": report.complete,
    }
