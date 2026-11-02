"""Exact finite positive-rational branch-weight histogram BRC carrier.

This module is the production extraction of WBRC-T36/T38.  It intentionally
keeps the positive semantic carrier finite and exact.  Laurent/group-ring
fraction-field compression remains a theorem-level representation, not a
runtime-complexity claim of this reference implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Mapping, Sequence

from .brc_rational_holonomy import rational_prime_valuations

RationalInput = int | Fraction


def _positive_fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    result = Fraction(value)
    if result <= 0:
        raise ValueError(f"{name} must be positive")
    return result


def _nonnegative_int(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be non-negative")
    return value


@dataclass(frozen=True)
class LeadingPair:
    """Exact dominant weight together with its tie multiplicity."""

    mass: Fraction
    multiplicity: int

    def __post_init__(self) -> None:
        if self.mass < 0:
            raise ValueError("leading mass must be non-negative")
        _nonnegative_int("multiplicity", self.multiplicity)
        if (self.mass == 0) != (self.multiplicity == 0):
            raise ValueError("zero leading pair must be exactly (0,0)")


@dataclass(frozen=True)
class WeightHistogram:
    """Finite exact histogram ``sum_q c_q [q]`` with positive rational q."""

    entries: tuple[tuple[Fraction, int], ...]

    def __post_init__(self) -> None:
        seen: set[Fraction] = set()
        previous: Fraction | None = None
        for weight, count in self.entries:
            if not isinstance(weight, Fraction) or weight <= 0:
                raise ValueError("histogram weights must be positive Fractions")
            if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
                raise ValueError("histogram counts must be positive integers")
            if weight in seen:
                raise ValueError("histogram entries must be coalesced")
            if previous is not None and weight <= previous:
                raise ValueError("histogram entries must be strictly weight-sorted")
            seen.add(weight)
            previous = weight

    @classmethod
    def from_counts(cls, counts: Mapping[RationalInput, int]) -> "WeightHistogram":
        combined: dict[Fraction, int] = {}
        for raw_weight, raw_count in counts.items():
            weight = _positive_fraction("weight", raw_weight)
            count = _nonnegative_int("count", raw_count)
            if count:
                combined[weight] = combined.get(weight, 0) + count
        return cls(tuple(sorted(combined.items())))

    @classmethod
    def from_weights(cls, weights: Iterable[RationalInput]) -> "WeightHistogram":
        combined: dict[Fraction, int] = {}
        for raw in weights:
            weight = _positive_fraction("weight", raw)
            combined[weight] = combined.get(weight, 0) + 1
        return cls(tuple(sorted(combined.items())))

    @property
    def is_zero(self) -> bool:
        return not self.entries

    @property
    def count(self) -> int:
        return sum(count for _, count in self.entries)

    @property
    def total_mass(self) -> Fraction:
        return sum((weight * count for weight, count in self.entries), Fraction(0, 1))

    @property
    def dominant_mass(self) -> Fraction:
        return self.entries[-1][0] if self.entries else Fraction(0, 1)

    @property
    def dominant_degeneracy(self) -> int:
        return self.entries[-1][1] if self.entries else 0

    @property
    def leading_pair(self) -> LeadingPair:
        return LeadingPair(self.dominant_mass, self.dominant_degeneracy)

    def moment(self, order: int) -> Fraction:
        _nonnegative_int("order", order)
        return sum(
            (count * (weight**order) for weight, count in self.entries),
            Fraction(0, 1),
        )

    def prime_valuation_terms(self) -> tuple[tuple[tuple[tuple[int, int], ...], int], ...]:
        """Finite Laurent/group-semiring terms in exact prime-valuation coordinates."""
        return tuple((rational_prime_valuations(weight), count) for weight, count in self.entries)


def weight_histogram(weights: Iterable[RationalInput]) -> WeightHistogram:
    return WeightHistogram.from_weights(weights)


def histogram_recoalesce(left: WeightHistogram, right: WeightHistogram) -> WeightHistogram:
    counts: dict[Fraction, int] = dict(left.entries)
    for weight, count in right.entries:
        counts[weight] = counts.get(weight, 0) + count
    return WeightHistogram(tuple(sorted(counts.items())))


def histogram_serial(left: WeightHistogram, right: WeightHistogram) -> WeightHistogram:
    if left.is_zero or right.is_zero:
        return WeightHistogram(())
    counts: dict[Fraction, int] = {}
    for left_weight, left_count in left.entries:
        for right_weight, right_count in right.entries:
            weight = left_weight * right_weight
            counts[weight] = counts.get(weight, 0) + left_count * right_count
    return WeightHistogram(tuple(sorted(counts.items())))


def leading_recoalesce(left: LeadingPair, right: LeadingPair) -> LeadingPair:
    if left.mass > right.mass:
        return left
    if right.mass > left.mass:
        return right
    if left.mass == 0:
        return LeadingPair(Fraction(0, 1), 0)
    return LeadingPair(left.mass, left.multiplicity + right.multiplicity)


def leading_serial(left: LeadingPair, right: LeadingPair) -> LeadingPair:
    if left.mass == 0 or right.mass == 0:
        return LeadingPair(Fraction(0, 1), 0)
    return LeadingPair(left.mass * right.mass, left.multiplicity * right.multiplicity)


def dominant_degeneracy_error_bound(histogram: WeightHistogram, order: int) -> tuple[Fraction, Fraction]:
    """Return exact normalized excess and WBRC-T38 upper bound.

    The result is ``(Phi_m/M^m-d, (C-d) r^m)``.  For an all-dominant or zero
    histogram both entries are zero.
    """
    _nonnegative_int("order", order)
    if histogram.is_zero or len(histogram.entries) == 1:
        return Fraction(0, 1), Fraction(0, 1)
    maximum = histogram.dominant_mass
    degeneracy = histogram.dominant_degeneracy
    normalized = histogram.moment(order) / (maximum**order)
    excess = normalized - degeneracy
    sub_weight = histogram.entries[-2][0]
    ratio = sub_weight / maximum
    bound = (histogram.count - degeneracy) * (ratio**order)
    return excess, bound


def power_sum_root_polynomial(count: int, moments: Sequence[RationalInput]) -> tuple[Fraction, ...]:
    """Recover the monic root polynomial coefficients from P_1..P_count.

    Returns ``(1,-e1,e2,...,(-1)^r e_r)``.  The roots, as an unordered
    multiset, are the branch weights when the supplied moments come from an
    r-element weight multiset.  This avoids requiring a general rational-root
    factorization routine in the production interface.
    """
    count = _nonnegative_int("count", count)
    if len(moments) < count:
        raise ValueError("moments must contain P_1 through P_count")
    if count == 0:
        return (Fraction(1, 1),)
    power = [Fraction(0, 1)]
    for raw in moments[:count]:
        if isinstance(raw, bool) or not isinstance(raw, (int, Fraction)):
            raise TypeError("moments must be int or Fraction")
        power.append(Fraction(raw))
    elementary = [Fraction(1, 1)]
    for k in range(1, count + 1):
        numerator = sum(
            (((-1) ** (i - 1)) * elementary[k - i] * power[i] for i in range(1, k + 1)),
            Fraction(0, 1),
        )
        elementary.append(numerator / k)
    return tuple(
        Fraction(1, 1) if k == 0 else ((-1) ** k) * elementary[k]
        for k in range(count + 1)
    )
