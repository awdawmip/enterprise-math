"""One-round necessity of the full rooted-circuit table.

For single-head implications, a sound basis that reconstructs the exact closure
of every seed in one parallel round must contain every rooted minimal
implication.  Conversely the full rooted-circuit table is one-round complete.

Thus rooted circuits are globally redundant only when iterative derivation is
allowed; under one-round semantics every circuit is mandatory.
"""

from __future__ import annotations

from typing import Hashable, Iterable

from .closure_implication_bases import Implication, basis_report
from .closure_implication_circuits import RootedCircuit, rooted_circuits

Label = Hashable
State = frozenset[Label]


def rooted_circuit_basis(labels: Iterable[Label], states: Iterable[State]) -> tuple[Implication, ...]:
    """Convert the complete rooted-circuit table to single-head implications."""
    return tuple(
        Implication(circuit.premise, circuit.root)
        for circuit in rooted_circuits(tuple(labels), tuple(states))
    )


def missing_rooted_circuits(
    labels: Iterable[Label],
    states: Iterable[State],
    rules: Iterable[Implication],
) -> tuple[RootedCircuit, ...]:
    """Return direct rooted circuits absent from the proposed rule set."""
    rules = tuple(rules)
    rule_pairs = {(rule.premise, rule.root) for rule in rules}
    return tuple(
        circuit
        for circuit in rooted_circuits(tuple(labels), tuple(states))
        if (circuit.premise, circuit.root) not in rule_pairs
    )


def full_circuit_one_round_report(labels: Iterable[Label], states: Iterable[State]):
    labels = tuple(labels)
    states = tuple(states)
    rules = rooted_circuit_basis(labels, states)
    report = basis_report(labels, states, rules)
    if not report.sound or not report.complete or report.worst_case_rounds > 1:
        raise AssertionError("full rooted-circuit table must be sound and one-round complete")
    return report
