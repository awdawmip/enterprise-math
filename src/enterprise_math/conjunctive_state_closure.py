"""Exact conjunctive query closure induced by a finite Boolean state family.

For a nonempty exact-state family Omega subseteq 2^P and required labels S,
let Ext(S) be the exact states containing S and define

    cl_Omega(S) = intersection Ext(S),

with the empty intersection interpreted as the full label universe P.  This is
a closure operator and Ext(S)=Ext(cl(S)).  Hence two conjunction queries have
the same truth vector on every exact state iff their closures agree.

The semantic unary implication preorder is the singleton fragment:

    x <=_Omega y  iff  x in cl({y}).

Higher-order closure can strictly compress beyond that preorder.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .semantic_implication_poset import semantic_implication_preorder

Element = object
State = frozenset[object]


@dataclass(frozen=True)
class ConjunctiveClosureReport:
    elements: tuple[object, ...]
    exact_states: frozenset[State]
    closed_sets: frozenset[frozenset[object]]
    closure_count: int
    raw_query_count: int


def _validate(elements: tuple[object, ...], states: frozenset[State]) -> None:
    if not elements or len(set(elements)) != len(elements):
        raise ValueError("elements must be a non-empty tuple of distinct labels")
    if not states:
        raise ValueError("exact state family must be non-empty")
    universe = set(elements)
    if any(not set(state).issubset(universe) for state in states):
        raise ValueError("exact state contains a label outside the universe")


def extent(
    elements: tuple[object, ...],
    states: frozenset[State],
    required: frozenset[object],
) -> frozenset[State]:
    _validate(elements, states)
    if not set(required).issubset(set(elements)):
        raise ValueError("required labels must lie in the universe")
    return frozenset(state for state in states if required.issubset(state))


def conjunctive_closure(
    elements: tuple[object, ...],
    states: frozenset[State],
    required: frozenset[object],
) -> frozenset[object]:
    ext = extent(elements, states, required)
    if not ext:
        return frozenset(elements)
    return frozenset.intersection(*tuple(ext))


def same_conjunctive_future(
    elements: tuple[object, ...],
    states: frozenset[State],
    left: frozenset[object],
    right: frozenset[object],
) -> bool:
    left_closure = conjunctive_closure(elements, states, left)
    right_closure = conjunctive_closure(elements, states, right)
    same_closure = left_closure == right_closure
    same_extent = extent(elements, states, left) == extent(elements, states, right)
    if same_closure != same_extent:
        raise AssertionError("query extents agree iff conjunctive closures agree")
    return same_closure


def enumerate_closed_sets(
    elements: tuple[object, ...], states: frozenset[State]
) -> frozenset[frozenset[object]]:
    _validate(elements, states)
    closures: set[frozenset[object]] = set()
    for size in range(len(elements) + 1):
        for subset in combinations(elements, size):
            closures.add(conjunctive_closure(elements, states, frozenset(subset)))
    return frozenset(closures)


def analyze_conjunctive_closure(
    elements: tuple[object, ...], states: frozenset[State]
) -> ConjunctiveClosureReport:
    closed = enumerate_closed_sets(elements, states)
    universe = frozenset(elements)

    # Verify closure-operator laws on all subsets.
    subsets: list[frozenset[object]] = []
    for size in range(len(elements) + 1):
        for subset in combinations(elements, size):
            subsets.append(frozenset(subset))
    for required in subsets:
        closure = conjunctive_closure(elements, states, required)
        if not required.issubset(closure):
            raise AssertionError("closure must be extensive")
        if conjunctive_closure(elements, states, closure) != closure:
            raise AssertionError("closure must be idempotent")
        if extent(elements, states, required) != extent(elements, states, closure):
            raise AssertionError("closure must preserve the query extent")
    for left in subsets:
        for right in subsets:
            if left.issubset(right):
                if not conjunctive_closure(elements, states, left).issubset(
                    conjunctive_closure(elements, states, right)
                ):
                    raise AssertionError("closure must be monotone")

    # Every exact state is itself closed because it occurs among states containing itself.
    for state in states:
        if conjunctive_closure(elements, states, state) != state:
            raise AssertionError("every exact state must be closed")

    # Singleton closure recovers exactly the semantic implication preorder.
    preorder = semantic_implication_preorder(elements, states)
    unary = frozenset(
        (lower, upper)
        for upper in elements
        for lower in conjunctive_closure(elements, states, frozenset({upper}))
    )
    if unary != preorder:
        raise AssertionError("semantic implication preorder must equal singleton closure")

    if universe not in closed:
        raise AssertionError("the full universe must be closed")

    return ConjunctiveClosureReport(
        elements=elements,
        exact_states=states,
        closed_sets=closed,
        closure_count=len(closed),
        raw_query_count=1 << len(elements),
    )
