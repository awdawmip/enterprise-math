"""Finite implication-basis execution and storage/depth diagnostics.

The full rooted-circuit table from Supplement 130 closes every seed in one
parallel round, but it can contain rules redundant under iterative forward
chaining.  This module separates semantic closure from one chosen implication
basis and measures the resulting derivation depth.

All implication/Horn/forward-chaining machinery here is classical.  The P025
use is to expose relation-law storage versus execution-depth precision.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Hashable, Iterable

from .closure_implication_circuits import closure_of

Label = Hashable
State = frozenset[Label]


@dataclass(frozen=True, order=True)
class Implication:
    premise: frozenset[Label]
    root: Label


@dataclass(frozen=True)
class BasisReport:
    rule_count: int
    total_premise_literals: int
    complete: bool
    sound: bool
    worst_case_rounds: int | None


def _powerset(labels: tuple[Label, ...]):
    for size in range(len(labels) + 1):
        for subset in combinations(labels, size):
            yield frozenset(subset)


def forward_chaining_trace(seed: Iterable[Label], rules: Iterable[Implication]) -> tuple[State, ...]:
    """Apply all currently enabled single-head implications in parallel rounds."""
    current = frozenset(seed)
    rule_tuple = tuple(rules)
    trace = [current]
    while True:
        additions = {
            rule.root
            for rule in rule_tuple
            if rule.premise.issubset(current) and rule.root not in current
        }
        if not additions:
            return tuple(trace)
        current = frozenset(current.union(additions))
        trace.append(current)


def implication_closure(seed: Iterable[Label], rules: Iterable[Implication]) -> State:
    return forward_chaining_trace(seed, rules)[-1]


def basis_report(
    labels: Iterable[Label],
    states: Iterable[State],
    rules: Iterable[Implication],
) -> BasisReport:
    labels = tuple(labels)
    states = tuple(states)
    universe = frozenset(labels)
    rules = tuple(rules)
    if len(set(labels)) != len(labels):
        raise ValueError("labels must be distinct")
    if not states:
        raise ValueError("states must be nonempty")
    if any(not state.issubset(universe) for state in states):
        raise ValueError("state contains label outside universe")
    if any(not rule.premise.issubset(universe) or rule.root not in universe for rule in rules):
        raise ValueError("rule contains label outside universe")

    sound = all(rule.root in closure_of(labels, states, rule.premise) for rule in rules)
    complete = True
    worst = 0
    for seed in _powerset(labels):
        target = closure_of(labels, states, seed)
        trace = forward_chaining_trace(seed, rules)
        if trace[-1] != target:
            complete = False
        if trace[-1] == target:
            worst = max(worst, len(trace) - 1)
    return BasisReport(
        rule_count=len(rules),
        total_premise_literals=sum(len(rule.premise) for rule in rules),
        complete=complete,
        sound=sound,
        worst_case_rounds=worst if complete else None,
    )


def chain_closure_states(labels: Iterable[Label]) -> tuple[State, ...]:
    """Exact states for x_0 => x_1 => ... => x_n: empty plus suffixes."""
    labels = tuple(labels)
    if not labels:
        raise ValueError("chain must contain at least one label")
    return (frozenset(),) + tuple(frozenset(labels[index:]) for index in range(len(labels)))


def chain_adjacent_basis(labels: Iterable[Label]) -> tuple[Implication, ...]:
    labels = tuple(labels)
    return tuple(
        Implication(frozenset({labels[index]}), labels[index + 1])
        for index in range(len(labels) - 1)
    )


def chain_full_circuit_basis(labels: Iterable[Label]) -> tuple[Implication, ...]:
    labels = tuple(labels)
    return tuple(
        Implication(frozenset({labels[left]}), labels[right])
        for left in range(len(labels))
        for right in range(left + 1, len(labels))
    )
