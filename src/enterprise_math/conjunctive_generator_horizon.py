"""Minimum generators and exact conjunction-arity horizon of a closure system.

For the conjunctive closure cl_Omega induced by a finite exact-state family,
define g(C) as the minimum size of a raw label set S with cl(S)=C, and let
g(Omega) be the maximum over closed sets.  This is the exact worst-case number
of raw labels needed to represent every conjunction-future equivalence class.

Every inclusion-minimal / minimum-cardinality generator can be chosen as an
antichain in the semantic implication quotient, so g(Omega) is at most the
semantic implication width.  The inequality can be strict under higher-order
closure dependencies.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .conjunctive_state_closure import conjunctive_closure, enumerate_closed_sets
from .semantic_implication_poset import analyze_semantic_implication

Element = object
State = frozenset[object]


@dataclass(frozen=True)
class ClosureGeneratorInfo:
    closed_set: frozenset[object]
    minimum_size: int
    minimum_generators: tuple[frozenset[object], ...]


@dataclass(frozen=True)
class ConjunctiveGeneratorHorizon:
    semantic_width: int
    generator_horizon: int
    strict_below_width: bool
    closure_generators: tuple[ClosureGeneratorInfo, ...]


def minimum_generators_for_closed_set(
    elements: tuple[object, ...],
    states: frozenset[State],
    closed_set: frozenset[object],
) -> ClosureGeneratorInfo:
    closed_sets = enumerate_closed_sets(elements, states)
    if closed_set not in closed_sets:
        raise ValueError("closed_set must be fixed by the conjunctive closure")

    for size in range(len(elements) + 1):
        matches: list[frozenset[object]] = []
        for subset in combinations(elements, size):
            candidate = frozenset(subset)
            if conjunctive_closure(elements, states, candidate) == closed_set:
                matches.append(candidate)
        if matches:
            return ClosureGeneratorInfo(
                closed_set=closed_set,
                minimum_size=size,
                minimum_generators=tuple(matches),
            )
    raise AssertionError("every finite closed set must have at least one generator")


def analyze_generator_horizon(
    elements: tuple[object, ...], states: frozenset[State]
) -> ConjunctiveGeneratorHorizon:
    semantic = analyze_semantic_implication(elements, states)
    closed_sets = enumerate_closed_sets(elements, states)
    infos = tuple(
        minimum_generators_for_closed_set(elements, states, closed_set)
        for closed_set in sorted(closed_sets, key=lambda item: (len(item), tuple(x in item for x in elements)))
    )
    horizon = max(info.minimum_size for info in infos)
    if horizon > semantic.semantic_width:
        raise AssertionError("minimum conjunction generators cannot exceed semantic implication width")

    class_of = {
        label: index
        for index, cls in enumerate(semantic.equivalence_classes)
        for label in cls
    }
    for info in infos:
        for generator in info.minimum_generators:
            classes = [class_of[label] for label in generator]
            if len(classes) != len(set(classes)):
                raise AssertionError("minimum generator cannot contain semantically equivalent labels")
            for i in classes:
                for j in classes:
                    if i != j and ((i, j) in semantic.class_relation or (j, i) in semantic.class_relation):
                        raise AssertionError("minimum generator cannot contain unary-comparable labels")

    return ConjunctiveGeneratorHorizon(
        semantic_width=semantic.semantic_width,
        generator_horizon=horizon,
        strict_below_width=horizon < semantic.semantic_width,
        closure_generators=infos,
    )
