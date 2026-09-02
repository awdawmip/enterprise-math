"""Exact finite determinant cycle-interaction polynomial for Weighted-BRC.

The explicit-edge polynomial is the finite inclusion-exclusion certificate proved
in PR #1134.  Its signs are determinant/cycle-system coefficients, not signed
BRC branch weights.  Enumeration is exact but exponential in explicit edge
count; use it as a certificate/calculus surface rather than a large-graph oracle.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

RationalInput = int | Fraction
EdgeShape = tuple[int, int]


def _fraction(value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("weight must be int or Fraction")
    return Fraction(value)


def _add_term(terms: dict[int, int], mask: int, coefficient: int) -> None:
    if coefficient == 0:
        return
    terms[mask] = terms.get(mask, 0) + coefficient
    if terms[mask] == 0:
        del terms[mask]


@dataclass(frozen=True)
class CyclePolynomial:
    """Sparse multiaffine polynomial indexed by explicit-edge bitmasks."""

    variable_count: int
    terms: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        if isinstance(self.variable_count, bool) or not isinstance(self.variable_count, int) or self.variable_count < 0:
            raise ValueError("variable_count must be a non-negative integer")
        seen: set[int] = set()
        for mask, coefficient in self.terms:
            if mask < 0 or mask >= (1 << self.variable_count):
                raise ValueError("term mask exceeds variable count")
            if coefficient == 0:
                raise ValueError("zero coefficients must be omitted")
            if mask in seen:
                raise ValueError("term masks must be unique")
            seen.add(mask)

    def as_dict(self) -> dict[int, int]:
        return dict(self.terms)


def explicit_cycle_interaction_polynomial(
    vertex_count: int, edge_shapes: Sequence[EdgeShape]
) -> CyclePolynomial:
    """Enumerate ``det(I-W(x))`` by vertex-disjoint explicit cycle systems.

    The implementation is intentionally literal: it enumerates edge subsets and
    accepts exactly those whose selected directed edges form a disjoint union of
    directed cycles.  Complexity is exponential in explicit edge count.
    """
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count <= 0:
        raise ValueError("vertex_count must be a positive integer")
    shapes: tuple[EdgeShape, ...] = tuple(edge_shapes)
    for source, target in shapes:
        if (
            isinstance(source, bool)
            or isinstance(target, bool)
            or not isinstance(source, int)
            or not isinstance(target, int)
            or not 0 <= source < vertex_count
            or not 0 <= target < vertex_count
        ):
            raise ValueError("edge endpoints must be valid vertex indices")

    terms: dict[int, int] = {0: 1}
    for mask in range(1, 1 << len(shapes)):
        indegree = [0] * vertex_count
        outdegree = [0] * vertex_count
        successor: dict[int, int] = {}
        valid = True
        for index, (source, target) in enumerate(shapes):
            if not ((mask >> index) & 1):
                continue
            outdegree[source] += 1
            indegree[target] += 1
            if outdegree[source] > 1 or indegree[target] > 1:
                valid = False
                break
            successor[source] = target
        if not valid or any(indegree[v] != outdegree[v] for v in range(vertex_count)):
            continue

        involved = {v for v in range(vertex_count) if outdegree[v] == 1}
        if not involved:
            continue
        seen: set[int] = set()
        cycle_count = 0
        for start in involved:
            if start in seen:
                continue
            cycle_count += 1
            vertex = start
            local: set[int] = set()
            while vertex not in local:
                if vertex not in successor:
                    valid = False
                    break
                local.add(vertex)
                seen.add(vertex)
                vertex = successor[vertex]
            if not valid or vertex != start:
                valid = False
                break
        if valid:
            _add_term(terms, mask, -1 if cycle_count & 1 else 1)

    if any(coefficient not in {-1, 1} for coefficient in terms.values()):
        raise AssertionError("explicit-edge determinant coefficient escaped +/-1")
    return CyclePolynomial(len(shapes), tuple(sorted(terms.items())))


def evaluate_cycle_interaction_polynomial(
    polynomial: CyclePolynomial,
    weights: Sequence[RationalInput],
) -> Fraction:
    """Evaluate a sparse cycle polynomial at exact rational weights."""
    values = tuple(_fraction(weight) for weight in weights)
    if len(values) != polynomial.variable_count:
        raise ValueError("weight count must match polynomial variable count")
    total = Fraction(0, 1)
    for mask, coefficient in polynomial.terms:
        term = Fraction(coefficient, 1)
        for index, weight in enumerate(values):
            if (mask >> index) & 1:
                term *= weight
        total += term
    return total


def partial_cycle_interaction_polynomial(
    polynomial: CyclePolynomial,
    edge_index: int,
) -> CyclePolynomial:
    """Differentiate with respect to one explicit branch variable."""
    if (
        isinstance(edge_index, bool)
        or not isinstance(edge_index, int)
        or not 0 <= edge_index < polynomial.variable_count
    ):
        raise ValueError("edge_index out of range")
    bit = 1 << edge_index
    terms: dict[int, int] = {}
    for mask, coefficient in polynomial.terms:
        if mask & bit:
            _add_term(terms, mask ^ bit, coefficient)
    return CyclePolynomial(polynomial.variable_count, tuple(sorted(terms.items())))


def tree_reduce_cycle_interaction_polynomial(
    polynomial: CyclePolynomial,
    tree_indices: Sequence[int],
) -> CyclePolynomial:
    """Set tree variables to one and reindex the remaining gauge coordinates.

    Distinct explicit-edge monomials may collapse, so the resulting integer
    coefficients are not restricted to +/-1.
    """
    tree = tuple(tree_indices)
    if len(set(tree)) != len(tree) or any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or not 0 <= index < polynomial.variable_count
        for index in tree
    ):
        raise ValueError("tree_indices must be distinct valid variable indices")
    tree_set = set(tree)
    non_tree = tuple(
        index for index in range(polynomial.variable_count) if index not in tree_set
    )
    position = {edge_index: coordinate for coordinate, edge_index in enumerate(non_tree)}
    terms: dict[int, int] = {}
    for mask, coefficient in polynomial.terms:
        reduced_mask = 0
        for edge_index in non_tree:
            if (mask >> edge_index) & 1:
                reduced_mask |= 1 << position[edge_index]
        _add_term(terms, reduced_mask, coefficient)
    return CyclePolynomial(len(non_tree), tuple(sorted(terms.items())))
