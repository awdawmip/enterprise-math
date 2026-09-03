"""Exact full-residual Newton fiber-sum quotient for Weighted-BRC.

Implements WBRC-T56 only.  The quotient assumes a fixed Newton multiplicity
and fixed Newton scale.  It does not choose the Newton scale or selected root;
those remain responsibilities of the parent Newton tools.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence, TypeAlias

from .brc_newton_recursion import RationalValuationScale

RationalInput: TypeAlias = int | Fraction


def _fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    return Fraction(value)


@dataclass(frozen=True)
class NewtonFiberPosition:
    """One labeled source Taylor coefficient position."""

    source_scale: RationalValuationScale
    taylor_degree: int
    label: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.source_scale, RationalValuationScale):
            raise TypeError("source_scale must be RationalValuationScale")
        if isinstance(self.taylor_degree, bool) or not isinstance(self.taylor_degree, int):
            raise TypeError("taylor_degree must be an integer")
        if self.taylor_degree < 0:
            raise ValueError("taylor_degree must be non-negative")
        if self.label is not None and not isinstance(self.label, str):
            raise TypeError("label must be str or None")


@dataclass(frozen=True)
class NewtonFiberCoordinate:
    residual_scale: RationalValuationScale
    taylor_degree: int


@dataclass(frozen=True)
class NewtonFiberClass:
    coordinate: NewtonFiberCoordinate
    position_indices: tuple[int, ...]


@dataclass(frozen=True)
class NewtonFiberQuotientAnalysis:
    positions: tuple[NewtonFiberPosition, ...]
    theta: RationalValuationScale
    multiplicity: int
    fibers: tuple[NewtonFiberClass, ...]

    @property
    def observer_rank(self) -> int:
        return len(self.fibers)

    @property
    def kernel_dimension(self) -> int:
        return len(self.positions) - len(self.fibers)

    @property
    def transfer_basis(self) -> tuple[tuple[int, int], ...]:
        """Return (anchor, moved-index) generators e_j-e_anchor."""
        output: list[tuple[int, int]] = []
        for fiber in self.fibers:
            anchor = fiber.position_indices[0]
            output.extend((anchor, index) for index in fiber.position_indices[1:])
        return tuple(output)


def newton_fiber_coordinate(
    position: NewtonFiberPosition,
    theta: RationalValuationScale,
    multiplicity: int,
) -> NewtonFiberCoordinate:
    if not isinstance(position, NewtonFiberPosition):
        raise TypeError("position must be NewtonFiberPosition")
    if not isinstance(theta, RationalValuationScale):
        raise TypeError("theta must be RationalValuationScale")
    if isinstance(multiplicity, bool) or not isinstance(multiplicity, int):
        raise TypeError("multiplicity must be an integer")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    return NewtonFiberCoordinate(
        position.source_scale.multiply(theta.power(position.taylor_degree - multiplicity)),
        position.taylor_degree,
    )


def newton_fiber_quotient_analysis(
    positions: Sequence[NewtonFiberPosition],
    theta: RationalValuationScale,
    multiplicity: int,
) -> NewtonFiberQuotientAnalysis:
    normalized = tuple(positions)
    if not normalized:
        raise ValueError("positions must be nonempty")
    grouped: dict[NewtonFiberCoordinate, list[int]] = {}
    for index, position in enumerate(normalized):
        coordinate = newton_fiber_coordinate(position, theta, multiplicity)
        grouped.setdefault(coordinate, []).append(index)
    fibers = tuple(
        NewtonFiberClass(coordinate, tuple(indices))
        for coordinate, indices in grouped.items()
    )
    return NewtonFiberQuotientAnalysis(normalized, theta, multiplicity, fibers)


def newton_fiber_sum_signature(
    positions: Sequence[NewtonFiberPosition],
    coefficients: Sequence[RationalInput],
    theta: RationalValuationScale,
    multiplicity: int,
) -> tuple[tuple[NewtonFiberCoordinate, Fraction], ...]:
    normalized = tuple(positions)
    values = tuple(_fraction("coefficient", value) for value in coefficients)
    if len(normalized) != len(values):
        raise ValueError("positions and coefficients must have equal length")
    analysis = newton_fiber_quotient_analysis(normalized, theta, multiplicity)
    output: list[tuple[NewtonFiberCoordinate, Fraction]] = []
    for fiber in analysis.fibers:
        total = sum((values[index] for index in fiber.position_indices), Fraction(0))
        if total:
            output.append((fiber.coordinate, total))
    return tuple(output)


def newton_fiber_equivalent(
    positions: Sequence[NewtonFiberPosition],
    left: Sequence[RationalInput],
    right: Sequence[RationalInput],
    theta: RationalValuationScale,
    multiplicity: int,
) -> bool:
    return newton_fiber_sum_signature(positions, left, theta, multiplicity) == newton_fiber_sum_signature(
        positions, right, theta, multiplicity
    )


def newton_fiber_edge_signature(
    positions: Sequence[NewtonFiberPosition],
    coefficients: Sequence[RationalInput],
    theta: RationalValuationScale,
    multiplicity: int,
) -> tuple[tuple[int, Fraction], ...]:
    """Weaker observer: current residual scale-one polynomial coefficients."""
    one = RationalValuationScale.one()
    output = []
    for coordinate, value in newton_fiber_sum_signature(positions, coefficients, theta, multiplicity):
        if coordinate.residual_scale == one:
            output.append((coordinate.taylor_degree, value))
    return tuple(output)


def apply_newton_fiber_transfer(
    coefficients: Sequence[RationalInput],
    anchor_index: int,
    moved_index: int,
    amount: RationalInput,
) -> tuple[Fraction, ...]:
    """Apply amount*(e_moved-e_anchor) to one coefficient state."""
    values = [_fraction("coefficient", value) for value in coefficients]
    if isinstance(anchor_index, bool) or isinstance(moved_index, bool):
        raise TypeError("indices must be integers")
    if not (
        isinstance(anchor_index, int)
        and isinstance(moved_index, int)
        and 0 <= anchor_index < len(values)
        and 0 <= moved_index < len(values)
    ):
        raise ValueError("transfer index out of range")
    if anchor_index == moved_index:
        raise ValueError("transfer endpoints must be distinct")
    delta = _fraction("amount", amount)
    values[anchor_index] -= delta
    values[moved_index] += delta
    return tuple(values)


__all__ = [
    "NewtonFiberPosition",
    "NewtonFiberCoordinate",
    "NewtonFiberClass",
    "NewtonFiberQuotientAnalysis",
    "newton_fiber_coordinate",
    "newton_fiber_quotient_analysis",
    "newton_fiber_sum_signature",
    "newton_fiber_equivalent",
    "newton_fiber_edge_signature",
    "apply_newton_fiber_transfer",
]
