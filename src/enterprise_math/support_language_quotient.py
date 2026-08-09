"""Exact support-language quotient through the A3-generated integer metric.

The labeled zero-relation quotient state set plus its integer metric ``rho``
determines every primitive radius relation and every finite relation word built
from them.  Conversely the complete primitive radius family reconstructs rho.

This module intentionally does not claim that rho supports richer A3 operations
such as signed weighted partition aggregation; a regression counterexample is
kept in the test suite.
"""

from __future__ import annotations

from collections.abc import Mapping

from .relation_support_bridge import DistanceMatrix

Relation = frozenset[tuple[int, int]]


def _require_metric(metric: DistanceMatrix) -> None:
    size = len(metric)
    if size == 0 or any(len(row) != size for row in metric):
        raise ValueError("metric must be a non-empty square matrix")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for row in metric
        for value in row
    ):
        raise ValueError("metric entries must be non-negative integers")


def support_relation_from_metric(metric: DistanceMatrix, radius: int) -> Relation:
    """Generate R_r={(x,y):rho(x,y)<=r}."""
    _require_metric(metric)
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return frozenset(
        (i, j)
        for i in range(len(metric))
        for j in range(len(metric))
        if metric[i][j] <= radius
    )


def compose_relations(left: Relation, right: Relation) -> Relation:
    """Finite relational composition."""
    right_by_source: dict[int, set[int]] = {}
    for source, target in right:
        right_by_source.setdefault(source, set()).add(target)
    return frozenset(
        (source, target)
        for source, middle in left
        for target in right_by_source.get(middle, ())
    )


def support_word_relation(metric: DistanceMatrix, radii: tuple[int, ...]) -> Relation:
    """Evaluate R_r1 ; ... ; R_rk using only the metric quotient."""
    _require_metric(metric)
    if not radii:
        raise ValueError("support word must contain at least one radius")
    if any(isinstance(radius, bool) or not isinstance(radius, int) or radius < 0 for radius in radii):
        raise ValueError("word radii must be non-negative integers")
    result = support_relation_from_metric(metric, radii[0])
    for radius in radii[1:]:
        result = compose_relations(result, support_relation_from_metric(metric, radius))
    return result


def primitive_support_family(metric: DistanceMatrix) -> tuple[Relation, ...]:
    """Return R_0,...,R_D where D=max rho; R_D is universal."""
    _require_metric(metric)
    diameter = max(max(row) for row in metric)
    return tuple(support_relation_from_metric(metric, radius) for radius in range(diameter + 1))


def recover_metric_from_support_family(
    class_count: int, family: Mapping[int, Relation] | tuple[Relation, ...]
) -> DistanceMatrix:
    """Recover rho as the first radius where each labeled pair appears.

    A tuple is interpreted as consecutive radii 0,1,... . A mapping must contain
    consecutive integer keys from zero through its maximum key.
    """
    if isinstance(class_count, bool) or not isinstance(class_count, int) or class_count <= 0:
        raise ValueError("class_count must be a positive integer")
    if isinstance(family, tuple):
        relations = {radius: relation for radius, relation in enumerate(family)}
    else:
        relations = dict(family)
    if not relations:
        raise ValueError("support family must be nonempty")
    radii = sorted(relations)
    if radii != list(range(radii[-1] + 1)):
        raise ValueError("support family radii must be consecutive from zero")

    valid_pairs = {(i, j) for i in range(class_count) for j in range(class_count)}
    for relation in relations.values():
        if not set(relation).issubset(valid_pairs):
            raise ValueError("support relation contains an out-of-range class")

    rows: list[tuple[int, ...]] = []
    for i in range(class_count):
        row: list[int] = []
        for j in range(class_count):
            first = next(
                (radius for radius in radii if (i, j) in relations[radius]),
                None,
            )
            if first is None:
                raise ValueError("family does not reach a universal radius")
            row.append(first)
        rows.append(tuple(row))
    return tuple(rows)
