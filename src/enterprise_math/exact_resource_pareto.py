"""Offline exact-semantic-fibre Pareto comparator for R014.

This module deliberately does not define a universal scalar cost.  It only compares
representations after both exact semantic identity and accounting regime have been
frozen.  Positive coordinate weights rescale a coordinate identically on both sides;
zero disables that coordinate.  Therefore weighting never turns the product order
into a weighted-sum total order.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
import math
from typing import Any, Mapping

COORDINATES = ("storage", "work", "depth", "channel", "reconstruction")
ROOT_VERDICT = (
    "ROOTING_SUCCESS / METHODOLOGY_AND_TOOLING_ONLY / "
    "NO_NEW_FOUNDATION_RESOURCE_CALCULUS"
)
ROUTING = {
    "new_enterprise_specific_calculus": False,
    "methodology_and_tooling": True,
    "ordinary_implementation_pareto_only": True,
}


class SemanticMismatch(ValueError):
    """Raised when representations do not belong to the same exact semantic fibre."""


class AccountingMismatch(ValueError):
    """Raised when resource values were measured under different accounting regimes."""


class UndefinedResource(ValueError):
    """Raised when an active resource coordinate is unspecified."""


class InvalidResource(ValueError):
    """Raised when a resource value is negative, NaN, or not numeric."""


class InvalidWeights(ValueError):
    """Raised when coordinate weights are invalid or disable every coordinate."""


class Comparison(str, Enum):
    LEFT_DOMINATES = "LEFT_DOMINATES"
    RIGHT_DOMINATES = "RIGHT_DOMINATES"
    RESOURCE_EQUIVALENT = "RESOURCE_EQUIVALENT"
    INCOMPARABLE = "INCOMPARABLE"


def canonical_semantic_digest(contract: Any) -> str:
    """Return a deterministic SHA-256 commitment to a JSON semantic contract."""
    canonical = json.dumps(
        contract,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )
    return "sha256-v1:" + sha256(canonical.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ResourceVector:
    storage: int | float | None
    work: int | float | None
    depth: int | float | None
    channel: int | float | None
    reconstruction: int | float | None

    def value(self, coordinate: str) -> int | float | None:
        if coordinate not in COORDINATES:
            raise KeyError(coordinate)
        return getattr(self, coordinate)


@dataclass(frozen=True)
class Representation:
    name: str
    semantic_fibre: str
    accounting_regime: str
    resources: ResourceVector


def _validated_weights(
    weights: Mapping[str, int | float] | None,
) -> dict[str, float]:
    resolved = {coordinate: 1.0 for coordinate in COORDINATES}
    if weights is not None:
        unknown = set(weights) - set(COORDINATES)
        if unknown:
            raise InvalidWeights(f"unknown coordinates: {sorted(unknown)}")
        for coordinate, raw_weight in weights.items():
            if isinstance(raw_weight, bool) or not isinstance(raw_weight, (int, float)):
                raise InvalidWeights(f"{coordinate}: weight must be numeric")
            weight = float(raw_weight)
            if not math.isfinite(weight) or weight < 0:
                raise InvalidWeights(f"{coordinate}: weight must be finite and nonnegative")
            resolved[coordinate] = weight
    if not any(weight > 0 for weight in resolved.values()):
        raise InvalidWeights("at least one coordinate must remain active")
    return resolved


def _validated_resource(
    representation: Representation,
    coordinate: str,
    weight: float,
) -> float | None:
    raw_value = representation.resources.value(coordinate)
    if weight == 0:
        return None
    if raw_value is None:
        raise UndefinedResource(
            f"{representation.name}: active coordinate {coordinate!r} is undefined"
        )
    if isinstance(raw_value, bool) or not isinstance(raw_value, (int, float)):
        raise InvalidResource(
            f"{representation.name}: coordinate {coordinate!r} must be numeric"
        )
    value = float(raw_value)
    if math.isnan(value) or value < 0:
        raise InvalidResource(
            f"{representation.name}: coordinate {coordinate!r} must be nonnegative"
        )
    return value * weight


def compare(
    left: Representation,
    right: Representation,
    *,
    weights: Mapping[str, int | float] | None = None,
) -> Comparison:
    """Compare two exact implementations by weak coordinatewise Pareto dominance.

    Preconditions:
      * exact semantic fibre identifiers must match;
      * accounting-regime identifiers must match;
      * every active coordinate must be defined on both representations.

    Weight policy:
      * positive weights are common coordinate rescalings and do not scalarize;
      * zero disables a coordinate;
      * negative/nonfinite weights are invalid.
    """
    if left.semantic_fibre != right.semantic_fibre:
        raise SemanticMismatch(
            f"{left.semantic_fibre!r} != {right.semantic_fibre!r}"
        )
    if left.accounting_regime != right.accounting_regime:
        raise AccountingMismatch(
            f"{left.accounting_regime!r} != {right.accounting_regime!r}"
        )

    resolved = _validated_weights(weights)
    left_better = False
    right_better = False

    for coordinate, weight in resolved.items():
        if weight == 0:
            continue
        left_value = _validated_resource(left, coordinate, weight)
        right_value = _validated_resource(right, coordinate, weight)
        assert left_value is not None and right_value is not None
        if left_value < right_value:
            left_better = True
        elif left_value > right_value:
            right_better = True

    if left_better and right_better:
        return Comparison.INCOMPARABLE
    if left_better:
        return Comparison.LEFT_DOMINATES
    if right_better:
        return Comparison.RIGHT_DOMINATES
    return Comparison.RESOURCE_EQUIVALENT


def pareto_frontier(
    representations: list[Representation],
    *,
    weights: Mapping[str, int | float] | None = None,
) -> list[Representation]:
    """Return nondominated representations, preserving input order.

    All representations must belong to one exact semantic fibre and one accounting
    regime. Resource-equivalent duplicates are retained because this oracle compares
    costs rather than claiming representation identity.
    """
    if not representations:
        return []
    anchor = representations[0]
    for representation in representations[1:]:
        if representation.semantic_fibre != anchor.semantic_fibre:
            raise SemanticMismatch("pareto_frontier requires one semantic fibre")
        if representation.accounting_regime != anchor.accounting_regime:
            raise AccountingMismatch("pareto_frontier requires one accounting regime")

    frontier: list[Representation] = []
    for candidate in representations:
        dominated = False
        for challenger in representations:
            if candidate is challenger:
                continue
            relation = compare(challenger, candidate, weights=weights)
            if relation == Comparison.LEFT_DOMINATES:
                dominated = True
                break
        if not dominated:
            frontier.append(candidate)
    return frontier
