"""Boundary between unary implication geometry and higher-order closure.

Let cl be the conjunctive closure induced by a finite exact-state family Omega,
and M=cl(empty) its mandatory core.  Define the unary-generated closure

    cl_1(S) = M union union_{s in S} cl({s}).

The full conjunction semantics is captured by the semantic implication preorder
exactly when cl=cl_1 for every S.  Failure is witnessed by a higher-order defect
cl(S)\cl_1(S).

When the closure is unary-generated, the exact generator horizon equals the
width of the optional semantic implication quotient obtained after deleting the
(always-active) mandatory equivalence class.  This recovers ordinary poset width
for all-ideal state universes and gives horizon zero when all semantic labels are
mandatory.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .conjunctive_generator_horizon import analyze_generator_horizon
from .conjunctive_state_closure import conjunctive_closure
from .poset_boundary_width import poset_width
from .semantic_implication_poset import analyze_semantic_implication

State = frozenset[object]


@dataclass(frozen=True)
class UnaryGeneratedClosureReport:
    unary_generated: bool
    mandatory_core: frozenset[object]
    optional_semantic_width: int
    generator_horizon: int
    first_defect_query: frozenset[object] | None
    first_defect_labels: frozenset[object] | None


def unary_generated_value(
    elements: tuple[object, ...],
    states: frozenset[State],
    required: frozenset[object],
) -> frozenset[object]:
    mandatory = conjunctive_closure(elements, states, frozenset())
    result = set(mandatory)
    for label in required:
        result.update(conjunctive_closure(elements, states, frozenset({label})))
    return frozenset(result)


def optional_semantic_width(
    elements: tuple[object, ...], states: frozenset[State]
) -> int:
    semantic = analyze_semantic_implication(elements, states)
    mandatory = conjunctive_closure(elements, states, frozenset())
    optional_indices = tuple(
        index
        for index, cls in enumerate(semantic.equivalence_classes)
        if cls.isdisjoint(mandatory)
    )
    if not optional_indices:
        return 0
    optional_set = set(optional_indices)
    relation = frozenset(
        (i, j)
        for i, j in semantic.class_relation
        if i in optional_set and j in optional_set
    )
    return poset_width(optional_indices, relation)


def analyze_unary_generated_closure(
    elements: tuple[object, ...], states: frozenset[State]
) -> UnaryGeneratedClosureReport:
    mandatory = conjunctive_closure(elements, states, frozenset())
    first_query = None
    first_labels = None
    for size in range(len(elements) + 1):
        for subset in combinations(elements, size):
            required = frozenset(subset)
            exact = conjunctive_closure(elements, states, required)
            unary = unary_generated_value(elements, states, required)
            if exact != unary and first_query is None:
                defect = exact.difference(unary)
                if not defect:
                    raise AssertionError("unary-generated closure must be contained in exact closure")
                first_query = required
                first_labels = frozenset(defect)

    unary_generated = first_query is None
    optional_width = optional_semantic_width(elements, states)
    generator = analyze_generator_horizon(elements, states).generator_horizon
    if unary_generated and generator != optional_width:
        raise AssertionError(
            "unary-generated closure must have generator horizon equal optional semantic width"
        )

    return UnaryGeneratedClosureReport(
        unary_generated=unary_generated,
        mandatory_core=mandatory,
        optional_semantic_width=optional_width,
        generator_horizon=generator,
        first_defect_query=first_query,
        first_defect_labels=first_labels,
    )
