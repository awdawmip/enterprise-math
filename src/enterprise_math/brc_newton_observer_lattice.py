"""Exact observer-lattice and frozen-horizon tools for Weighted-BRC Newton jets.

Implements WBRC-T57/T58 only.  Coordinate observers are defined on the T56
residual-coordinate quotient.  Frozen Newton schedules are declared operation
sequences; this module does not autonomously select roots, multiplicities or
scales for perturbed states.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Sequence, TypeAlias

from .brc_newton_fiber_quotient import (
    NewtonFiberCoordinate,
    NewtonFiberPosition,
    newton_fiber_quotient_analysis,
    newton_fiber_sum_signature,
)
from .brc_newton_recursion import RationalValuationScale

RationalInput: TypeAlias = int | Fraction
ResidualState = tuple[tuple[NewtonFiberCoordinate, Fraction], ...]


def _fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    return Fraction(value)


def _coordinate_key(coordinate: NewtonFiberCoordinate):
    return (coordinate.residual_scale.valuations, coordinate.taylor_degree)


def _normalize_coordinates(
    coordinates: Sequence[NewtonFiberCoordinate],
) -> tuple[NewtonFiberCoordinate, ...]:
    output: list[NewtonFiberCoordinate] = []
    seen: set[NewtonFiberCoordinate] = set()
    for coordinate in coordinates:
        if not isinstance(coordinate, NewtonFiberCoordinate):
            raise TypeError("observer coordinates must be NewtonFiberCoordinate")
        if coordinate not in seen:
            output.append(coordinate)
            seen.add(coordinate)
    return tuple(sorted(output, key=_coordinate_key))


@dataclass(frozen=True)
class NewtonCoordinateObserver:
    """A declared coordinate-projection observer on residual Newton state."""

    coordinates: tuple[NewtonFiberCoordinate, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "coordinates", _normalize_coordinates(self.coordinates))

    @property
    def rank(self) -> int:
        return len(self.coordinates)

    def join(self, other: "NewtonCoordinateObserver") -> "NewtonCoordinateObserver":
        if not isinstance(other, NewtonCoordinateObserver):
            raise TypeError("other must be NewtonCoordinateObserver")
        return NewtonCoordinateObserver(self.coordinates + other.coordinates)

    def meet(self, other: "NewtonCoordinateObserver") -> "NewtonCoordinateObserver":
        if not isinstance(other, NewtonCoordinateObserver):
            raise TypeError("other must be NewtonCoordinateObserver")
        right = set(other.coordinates)
        return NewtonCoordinateObserver(tuple(c for c in self.coordinates if c in right))

    def refines(self, other: "NewtonCoordinateObserver") -> bool:
        """Whether this observer is at least as informative as ``other``."""
        if not isinstance(other, NewtonCoordinateObserver):
            raise TypeError("other must be NewtonCoordinateObserver")
        return set(other.coordinates) <= set(self.coordinates)


def full_coordinate_observer(
    positions: Sequence[NewtonFiberPosition],
    theta: RationalValuationScale,
    multiplicity: int,
) -> NewtonCoordinateObserver:
    analysis = newton_fiber_quotient_analysis(positions, theta, multiplicity)
    return NewtonCoordinateObserver(tuple(fiber.coordinate for fiber in analysis.fibers))


def edge_coordinate_observer(
    positions: Sequence[NewtonFiberPosition],
    theta: RationalValuationScale,
    multiplicity: int,
) -> NewtonCoordinateObserver:
    one = RationalValuationScale.one()
    full = full_coordinate_observer(positions, theta, multiplicity)
    return NewtonCoordinateObserver(tuple(c for c in full.coordinates if c.residual_scale == one))


def _validate_observer_within(
    observer: NewtonCoordinateObserver,
    universe: NewtonCoordinateObserver,
) -> None:
    if not isinstance(observer, NewtonCoordinateObserver):
        raise TypeError("observer must be NewtonCoordinateObserver")
    unknown = set(observer.coordinates) - set(universe.coordinates)
    if unknown:
        raise ValueError("observer contains coordinates outside the residual universe")


def coordinate_observer_signature(
    positions: Sequence[NewtonFiberPosition],
    coefficients: Sequence[RationalInput],
    theta: RationalValuationScale,
    multiplicity: int,
    observer: NewtonCoordinateObserver,
) -> tuple[tuple[NewtonFiberCoordinate, Fraction], ...]:
    universe = full_coordinate_observer(positions, theta, multiplicity)
    _validate_observer_within(observer, universe)
    full = dict(newton_fiber_sum_signature(positions, coefficients, theta, multiplicity))
    return tuple((coordinate, full.get(coordinate, Fraction(0))) for coordinate in observer.coordinates)


def coordinate_observer_equivalent(
    positions: Sequence[NewtonFiberPosition],
    left: Sequence[RationalInput],
    right: Sequence[RationalInput],
    theta: RationalValuationScale,
    multiplicity: int,
    observer: NewtonCoordinateObserver,
) -> bool:
    return coordinate_observer_signature(positions, left, theta, multiplicity, observer) == coordinate_observer_signature(
        positions, right, theta, multiplicity, observer
    )


def coordinate_observer_kernel_dimension(
    positions: Sequence[NewtonFiberPosition],
    theta: RationalValuationScale,
    multiplicity: int,
    observer: NewtonCoordinateObserver,
) -> int:
    normalized = tuple(positions)
    universe = full_coordinate_observer(normalized, theta, multiplicity)
    _validate_observer_within(observer, universe)
    return len(normalized) - observer.rank


@dataclass(frozen=True)
class FrozenNewtonScheduleStep:
    root: Fraction
    multiplicity: int
    theta: RationalValuationScale

    def __post_init__(self) -> None:
        object.__setattr__(self, "root", _fraction("root", self.root))
        if isinstance(self.multiplicity, bool) or not isinstance(self.multiplicity, int):
            raise TypeError("multiplicity must be an integer")
        if self.multiplicity < 1:
            raise ValueError("multiplicity must be positive")
        if not isinstance(self.theta, RationalValuationScale):
            raise TypeError("theta must be RationalValuationScale")


def _normalize_state(
    state: Sequence[tuple[NewtonFiberCoordinate, RationalInput]],
) -> ResidualState:
    accumulated: dict[NewtonFiberCoordinate, Fraction] = {}
    for coordinate, raw_value in state:
        if not isinstance(coordinate, NewtonFiberCoordinate):
            raise TypeError("state coordinates must be NewtonFiberCoordinate")
        value = _fraction("state coefficient", raw_value)
        accumulated[coordinate] = accumulated.get(coordinate, Fraction(0)) + value
    return tuple(
        (coordinate, accumulated[coordinate])
        for coordinate in sorted(accumulated, key=_coordinate_key)
        if accumulated[coordinate]
    )


def frozen_newton_substitution(
    state: Sequence[tuple[NewtonFiberCoordinate, RationalInput]],
    step: FrozenNewtonScheduleStep,
) -> ResidualState:
    if not isinstance(step, FrozenNewtonScheduleStep):
        raise TypeError("step must be FrozenNewtonScheduleStep")
    output: list[tuple[NewtonFiberCoordinate, Fraction]] = []
    for coordinate, coefficient in _normalize_state(state):
        degree = coordinate.taylor_degree
        for new_degree in range(degree + 1):
            value = coefficient * Fraction(comb(degree, new_degree)) * step.root ** (degree - new_degree)
            if value == 0:
                continue
            new_coordinate = NewtonFiberCoordinate(
                coordinate.residual_scale.multiply(step.theta.power(new_degree - step.multiplicity)),
                new_degree,
            )
            output.append((new_coordinate, value))
    return _normalize_state(output)


def residual_edge_signature(
    state: Sequence[tuple[NewtonFiberCoordinate, RationalInput]],
) -> tuple[tuple[int, Fraction], ...]:
    one = RationalValuationScale.one()
    return tuple(
        (coordinate.taylor_degree, value)
        for coordinate, value in _normalize_state(state)
        if coordinate.residual_scale == one
    )


def frozen_horizon_edge_signature(
    state: Sequence[tuple[NewtonFiberCoordinate, RationalInput]],
    schedule: Sequence[FrozenNewtonScheduleStep],
) -> tuple[tuple[tuple[int, Fraction], ...], ...]:
    current = _normalize_state(state)
    output = [residual_edge_signature(current)]
    for step in schedule:
        if not isinstance(step, FrozenNewtonScheduleStep):
            raise TypeError("schedule entries must be FrozenNewtonScheduleStep")
        current = frozen_newton_substitution(current, step)
        output.append(residual_edge_signature(current))
    return tuple(output)


def _matrix_rank(matrix: Sequence[Sequence[Fraction]]) -> int:
    work = [list(row) for row in matrix]
    if not work:
        return 0
    columns = len(work[0])
    if any(len(row) != columns for row in work):
        raise ValueError("matrix rows must have equal length")
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        leading = work[pivot_row][column]
        work[pivot_row] = [value / leading for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


@dataclass(frozen=True)
class FrozenNewtonObservabilityAnalysis:
    initial_coordinates: tuple[NewtonFiberCoordinate, ...]
    schedule: tuple[FrozenNewtonScheduleStep, ...]
    output_coordinates: tuple[tuple[int, int], ...]
    matrix: tuple[tuple[Fraction, ...], ...]
    rank: int

    @property
    def kernel_dimension(self) -> int:
        return len(self.initial_coordinates) - self.rank


def frozen_horizon_observability_analysis(
    initial_coordinates: Sequence[NewtonFiberCoordinate],
    schedule: Sequence[FrozenNewtonScheduleStep],
) -> FrozenNewtonObservabilityAnalysis:
    coordinates = _normalize_coordinates(initial_coordinates)
    if not coordinates:
        raise ValueError("initial_coordinates must be nonempty")
    steps = tuple(schedule)
    if any(not isinstance(step, FrozenNewtonScheduleStep) for step in steps):
        raise TypeError("schedule entries must be FrozenNewtonScheduleStep")

    column_signatures: list[dict[tuple[int, int], Fraction]] = []
    output_keys: set[tuple[int, int]] = set()
    for coordinate in coordinates:
        horizon = frozen_horizon_edge_signature(((coordinate, Fraction(1)),), steps)
        signature: dict[tuple[int, int], Fraction] = {}
        for time, edge in enumerate(horizon):
            for degree, value in edge:
                signature[(time, degree)] = value
                output_keys.add((time, degree))
        column_signatures.append(signature)

    outputs = tuple(sorted(output_keys))
    matrix = tuple(
        tuple(column.get(output, Fraction(0)) for column in column_signatures)
        for output in outputs
    )
    observed_rank = _matrix_rank(matrix)
    return FrozenNewtonObservabilityAnalysis(coordinates, steps, outputs, matrix, observed_rank)


def frozen_horizon_rank_profile(
    initial_coordinates: Sequence[NewtonFiberCoordinate],
    schedule: Sequence[FrozenNewtonScheduleStep],
) -> tuple[int, ...]:
    steps = tuple(schedule)
    return tuple(
        frozen_horizon_observability_analysis(initial_coordinates, steps[:horizon]).rank
        for horizon in range(len(steps) + 1)
    )


def frozen_horizon_kernel_profile(
    initial_coordinates: Sequence[NewtonFiberCoordinate],
    schedule: Sequence[FrozenNewtonScheduleStep],
) -> tuple[int, ...]:
    steps = tuple(schedule)
    return tuple(
        frozen_horizon_observability_analysis(initial_coordinates, steps[:horizon]).kernel_dimension
        for horizon in range(len(steps) + 1)
    )


__all__ = [
    "NewtonCoordinateObserver",
    "FrozenNewtonScheduleStep",
    "FrozenNewtonObservabilityAnalysis",
    "full_coordinate_observer",
    "edge_coordinate_observer",
    "coordinate_observer_signature",
    "coordinate_observer_equivalent",
    "coordinate_observer_kernel_dimension",
    "frozen_newton_substitution",
    "residual_edge_signature",
    "frozen_horizon_edge_signature",
    "frozen_horizon_observability_analysis",
    "frozen_horizon_rank_profile",
    "frozen_horizon_kernel_profile",
]
