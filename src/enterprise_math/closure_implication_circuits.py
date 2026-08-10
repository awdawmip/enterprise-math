"""Rooted minimal implications for finite exact-state closure systems.

Given a nonempty exact-state family Omega subseteq 2^P, define

    cl(S) = intersection {X in Omega : S subseteq X},

with empty extent interpreted as the full label universe P.  A rooted circuit
(A,b) has b not in A, b in cl(A), and no proper subset of A already forces b.

The full rooted-circuit table is a direct one-round presentation of closure:
for every seed S, cl(S) is S together with all roots b whose minimal premise A
is already contained in S.

This is classical finite closure/Horn-implication mathematics.  The module is a
P025 executable pressure-test interface; it makes no generic novelty claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Hashable, Iterable

Label = Hashable
State = frozenset[Label]


@dataclass(frozen=True, order=True)
class RootedCircuit:
    premise: frozenset[Label]
    root: Label


def _normalize(labels: Iterable[Label], states: Iterable[State]) -> tuple[tuple[Label, ...], tuple[State, ...]]:
    label_tuple = tuple(labels)
    if len(set(label_tuple)) != len(label_tuple):
        raise ValueError("labels must be distinct")
    label_set = frozenset(label_tuple)
    state_tuple = tuple(states)
    if not state_tuple:
        raise ValueError("exact-state family must be nonempty")
    if any(not isinstance(state, frozenset) for state in state_tuple):
        raise ValueError("states must be frozensets")
    if any(not state.issubset(label_set) for state in state_tuple):
        raise ValueError("state contains a label outside the universe")
    return label_tuple, state_tuple


def closure_of(labels: Iterable[Label], states: Iterable[State], seed: Iterable[Label]) -> State:
    """Return the exact conjunction closure of ``seed`` under the state family."""
    label_tuple, state_tuple = _normalize(labels, states)
    universe = frozenset(label_tuple)
    seed_set = frozenset(seed)
    if not seed_set.issubset(universe):
        raise ValueError("seed contains a label outside the universe")
    extent = tuple(state for state in state_tuple if seed_set.issubset(state))
    if not extent:
        return universe
    result = universe
    for state in extent:
        result = result.intersection(state)
    return frozenset(result)


def _proper_subsets(items: tuple[Label, ...]):
    for size in range(len(items)):
        for subset in combinations(items, size):
            yield frozenset(subset)


def rooted_circuits(labels: Iterable[Label], states: Iterable[State]) -> tuple[RootedCircuit, ...]:
    """Enumerate every inclusion-minimal single-root valid implication."""
    label_tuple, state_tuple = _normalize(labels, states)
    universe = frozenset(label_tuple)
    circuits: list[RootedCircuit] = []
    for root in label_tuple:
        others = tuple(label for label in label_tuple if label != root)
        for size in range(len(others) + 1):
            for premise_tuple in combinations(others, size):
                premise = frozenset(premise_tuple)
                if root not in closure_of(label_tuple, state_tuple, premise):
                    continue
                if any(root in closure_of(label_tuple, state_tuple, sub) for sub in _proper_subsets(premise_tuple)):
                    continue
                circuits.append(RootedCircuit(premise=premise, root=root))
    # deterministic repr across heterogeneous but printable labels
    circuits.sort(key=lambda item: (len(item.premise), tuple(sorted(map(repr, item.premise))), repr(item.root)))
    return tuple(circuits)


def one_round_circuit_closure(
    labels: Iterable[Label],
    states: Iterable[State],
    seed: Iterable[Label],
) -> State:
    """Recover closure by firing every rooted circuit whose premise lies in seed."""
    label_tuple, state_tuple = _normalize(labels, states)
    seed_set = frozenset(seed)
    universe = frozenset(label_tuple)
    if not seed_set.issubset(universe):
        raise ValueError("seed contains a label outside the universe")
    added = {
        circuit.root
        for circuit in rooted_circuits(label_tuple, state_tuple)
        if circuit.premise.issubset(seed_set)
    }
    return frozenset(seed_set.union(added))


def circuit_arity_spectrum(labels: Iterable[Label], states: Iterable[State]) -> dict[int, int]:
    """Return the number of rooted circuits at each premise arity."""
    spectrum: dict[int, int] = {}
    for circuit in rooted_circuits(labels, states):
        spectrum[len(circuit.premise)] = spectrum.get(len(circuit.premise), 0) + 1
    return dict(sorted(spectrum.items()))


def maximum_circuit_arity(labels: Iterable[Label], states: Iterable[State]) -> int:
    circuits = rooted_circuits(labels, states)
    return max((len(circuit.premise) for circuit in circuits), default=0)


def closure_is_unary_generated(labels: Iterable[Label], states: Iterable[State]) -> bool:
    """Exact finite test for Stage129's mandatory-core + singleton condition."""
    return maximum_circuit_arity(labels, states) <= 1
