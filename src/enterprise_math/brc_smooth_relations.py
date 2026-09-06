"""BRC multi-strip smooth-relation carrier and GF(2) dependency facade.

This module is deliberately prior-art-safe.  Smooth factor-base relations,
parity linear algebra, congruences of squares, Dixon, QS, MPQS and SIQS are
classical mathematics.  The BRC-specific surface here is typed composition:
relations generated on different retained multiplier/vertical strips can share
one dependency algebra because

    x^2 - D = m*N  ->  x^2 == D (mod N).

The multiplier is therefore a relation-generator coordinate, not a dependency
coordinate.  Exact exponent parity, full exponents and x provenance are kept
until a square congruence is reconstructed.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Iterable

from .brc_multiplier_factor_scan import (
    AdmissibleMultiplierRootState,
    admissible_root_state_sequence,
)
from .brc_multiplier_vertical_wheel import (
    vertical_gap_at,
    vertical_state_from_multiplier_state,
)
from .legendre import primes_up_to


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def factor_base(bound: int) -> tuple[int, ...]:
    """Classical reference factor base containing every prime <= bound."""
    _require_positive("bound", bound)
    return tuple(primes_up_to(bound))


def factor_over_base(value: int, base: tuple[int, ...]) -> tuple[int, ...] | None:
    """Return aligned prime exponents iff positive value is fully base-smooth."""
    _require_positive("value", value)
    if not base:
        raise ValueError("factor base must be nonempty")
    remaining = value
    exponents: list[int] = []
    for prime in base:
        _require_positive("factor-base prime", prime)
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        exponents.append(exponent)
    return tuple(exponents) if remaining == 1 else None


@dataclass(frozen=True)
class BRCSmoothRelation:
    """One exact smooth relation with dependency and reconstruction data."""

    n: int
    multiplier: int
    vertical_offset: int
    x: int
    gap: int
    factor_base: tuple[int, ...]
    exponents: tuple[int, ...]

    def __post_init__(self) -> None:
        _require_positive("n", self.n)
        _require_positive("multiplier", self.multiplier)
        if self.vertical_offset < 0:
            raise ValueError("vertical_offset must be nonnegative")
        _require_positive("x", self.x)
        _require_positive("gap", self.gap)
        if len(self.factor_base) != len(self.exponents):
            raise ValueError("factor base/exponent lengths disagree")
        if any(e < 0 for e in self.exponents):
            raise ValueError("exponents must be nonnegative")
        reconstructed = 1
        for prime, exponent in zip(self.factor_base, self.exponents):
            reconstructed *= prime**exponent
        if reconstructed != self.gap:
            raise ValueError("smooth relation factorization failed reconstruction")
        if self.x * self.x - self.gap != self.multiplier * self.n:
            raise ValueError("BRC relation failed x^2-D=mN reconstruction")

    @property
    def parity_mask(self) -> int:
        mask = 0
        for index, exponent in enumerate(self.exponents):
            if exponent & 1:
                mask |= 1 << index
        return mask


@dataclass(frozen=True)
class RelationDependency:
    relation_indices: tuple[int, ...]
    parity_xor: int


@dataclass(frozen=True)
class SquareCongruence:
    n: int
    relation_indices: tuple[int, ...]
    x_mod_n: int
    y_mod_n: int
    gcd_minus: int
    gcd_plus: int

    @property
    def nontrivial_factor(self) -> int | None:
        for value in (self.gcd_minus, self.gcd_plus):
            if 1 < value < self.n:
                return value
        return None


@dataclass(frozen=True)
class SmoothRelationFactorWitness:
    factor: int
    points_examined: int
    smooth_relations: int
    dependencies_tested: int
    dependency_size: int
    multipliers_used: tuple[int, ...]


class GF2RelationAccumulator:
    """Incremental parity elimination retaining exact relation provenance."""

    def __init__(self, base: tuple[int, ...]):
        if not base:
            raise ValueError("factor base must be nonempty")
        self.factor_base = base
        self.relations: list[BRCSmoothRelation] = []
        self._pivots: dict[int, tuple[int, int]] = {}
        self.dependencies: list[RelationDependency] = []

    def add(self, relation: BRCSmoothRelation) -> RelationDependency | None:
        if relation.factor_base != self.factor_base:
            raise ValueError("relation factor base differs from accumulator")
        index = len(self.relations)
        self.relations.append(relation)
        vector = relation.parity_mask
        provenance = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            prior = self._pivots.get(pivot)
            if prior is None:
                self._pivots[pivot] = (vector, provenance)
                return None
            vector ^= prior[0]
            provenance ^= prior[1]
        indices = tuple(
            i for i in range(len(self.relations)) if (provenance >> i) & 1
        )
        dependency = RelationDependency(indices, 0)
        self.dependencies.append(dependency)
        return dependency


def relation_from_multiplier_state(
    state: AdmissibleMultiplierRootState,
    vertical_offset: int,
    base: tuple[int, ...],
) -> BRCSmoothRelation | None:
    """Extract one smooth relation from a retained horizontal BRC state."""
    if isinstance(vertical_offset, bool) or not isinstance(vertical_offset, int) or vertical_offset < 0:
        raise ValueError("vertical_offset must be a nonnegative integer")
    vertical = vertical_state_from_multiplier_state(state)
    gap = vertical_gap_at(vertical, vertical_offset)
    # D=0 is an exact-square point, not a factor-base smooth relation carrier.
    if gap == 0:
        return None
    exponents = factor_over_base(gap, base)
    if exponents is None:
        return None
    return BRCSmoothRelation(
        n=state.n,
        multiplier=state.multiplier,
        vertical_offset=vertical_offset,
        x=vertical.base_x + vertical_offset,
        gap=gap,
        factor_base=base,
        exponents=exponents,
    )


def congruence_from_dependency(
    relations: tuple[BRCSmoothRelation, ...],
    dependency: RelationDependency,
) -> SquareCongruence:
    """Reconstruct the classical square congruence from one GF(2) dependency."""
    if not dependency.relation_indices:
        raise ValueError("dependency must contain at least one relation")
    selected = tuple(relations[i] for i in dependency.relation_indices)
    n = selected[0].n
    base = selected[0].factor_base
    if any(relation.n != n or relation.factor_base != base for relation in selected):
        raise ValueError("dependency relations must share n and factor base")

    x_mod_n = 1
    exponent_totals = [0] * len(base)
    parity = 0
    for relation in selected:
        x_mod_n = (x_mod_n * (relation.x % n)) % n
        parity ^= relation.parity_mask
        for index, exponent in enumerate(relation.exponents):
            exponent_totals[index] += exponent
    if parity != 0 or any(exponent & 1 for exponent in exponent_totals):
        raise ValueError("relation subset is not a GF(2) parity dependency")

    y_mod_n = 1
    for prime, exponent in zip(base, exponent_totals):
        if exponent:
            y_mod_n = (y_mod_n * pow(prime, exponent // 2, n)) % n
    if (x_mod_n * x_mod_n - y_mod_n * y_mod_n) % n != 0:
        raise AssertionError("dependency did not reconstruct a congruence of squares")
    return SquareCongruence(
        n=n,
        relation_indices=dependency.relation_indices,
        x_mod_n=x_mod_n,
        y_mod_n=y_mod_n,
        gcd_minus=gcd((x_mod_n - y_mod_n) % n, n),
        gcd_plus=gcd((x_mod_n + y_mod_n) % n, n),
    )


def layered_relation_points(
    states: tuple[AdmissibleMultiplierRootState, ...],
    point_limit: int,
) -> Iterable[tuple[AdmissibleMultiplierRootState, int]]:
    """Round-robin shallow vertical sampling over all retained multiplier strips."""
    _require_positive("point_limit", point_limit)
    if not states:
        return
    emitted = 0
    offset = 0
    while emitted < point_limit:
        for state in states:
            if emitted >= point_limit:
                return
            yield state, offset
            emitted += 1
        offset += 1


def first_layered_smooth_factor_witness(
    n: int,
    smooth_bound: int,
    point_limit: int,
    *,
    max_multiplier: int = 100,
) -> SmoothRelationFactorWitness | None:
    """Reference multi-strip relation collector with incremental GF(2) elimination.

    This is not a production quadratic-sieve implementation: smoothness is
    detected by trial division and dependency basis vectors are tested as they
    appear.  It exists to verify the exact cross-strip relation semantics.
    """
    _require_positive("n", n)
    _require_positive("smooth_bound", smooth_bound)
    _require_positive("point_limit", point_limit)
    base = factor_base(smooth_bound)
    states = admissible_root_state_sequence(n, max_multiplier)
    accumulator = GF2RelationAccumulator(base)
    dependencies_tested = 0

    for points_examined, (state, offset) in enumerate(
        layered_relation_points(states, point_limit), 1
    ):
        relation = relation_from_multiplier_state(state, offset, base)
        if relation is None:
            continue
        dependency = accumulator.add(relation)
        if dependency is None:
            continue
        dependencies_tested += 1
        congruence = congruence_from_dependency(tuple(accumulator.relations), dependency)
        factor = congruence.nontrivial_factor
        if factor is not None:
            multipliers = tuple(
                sorted({accumulator.relations[i].multiplier for i in dependency.relation_indices})
            )
            return SmoothRelationFactorWitness(
                factor=factor,
                points_examined=points_examined,
                smooth_relations=len(accumulator.relations),
                dependencies_tested=dependencies_tested,
                dependency_size=len(dependency.relation_indices),
                multipliers_used=multipliers,
            )
    return None


__all__ = [
    "BRCSmoothRelation",
    "RelationDependency",
    "SquareCongruence",
    "SmoothRelationFactorWitness",
    "GF2RelationAccumulator",
    "factor_base",
    "factor_over_base",
    "relation_from_multiplier_state",
    "congruence_from_dependency",
    "layered_relation_points",
    "first_layered_smooth_factor_witness",
]
