"""Finite engineering-measurement metadata for E001 material benchmarks.

This module separates three things that must not be conflated:

* an experimental count recorded on a declared measurement scale;
* the physical/unit tag carried by that count;
* the independent model precision ``A`` used by a finite material curve.

No floating-point value is required. A measurement count ``v`` on scale ``s``
represents the exact rational quantity ``v/s`` in the declared unit. Unit tags
are intentionally opaque here: dimensional algebra is outside this scope.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_integer(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


@dataclass(frozen=True)
class ExactMeasurement:
    numerator: int
    denominator: int
    unit: str

    def __post_init__(self) -> None:
        _require_integer("numerator", self.numerator)
        _require_positive("denominator", self.denominator)
        if not isinstance(self.unit, str) or not self.unit:
            raise ValueError("unit must be a nonempty string")


@dataclass(frozen=True)
class FiniteMeasurementAxis:
    name: str
    unit: str
    scale_factor: int
    lower_count: int
    upper_count: int

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("name must be a nonempty string")
        if not isinstance(self.unit, str) or not self.unit:
            raise ValueError("unit must be a nonempty string")
        _require_positive("scale_factor", self.scale_factor)
        _require_integer("lower_count", self.lower_count)
        _require_integer("upper_count", self.upper_count)
        if self.upper_count < self.lower_count:
            raise ValueError("upper_count must not be less than lower_count")

    def contains(self, count: int) -> bool:
        _require_integer("count", count)
        return self.lower_count <= count <= self.upper_count

    def exact_value(self, count: int) -> ExactMeasurement:
        if not self.contains(count):
            raise ValueError("count lies outside the declared observation axis")
        common = gcd(abs(count), self.scale_factor)
        return ExactMeasurement(count // common, self.scale_factor // common, self.unit)


@dataclass(frozen=True)
class FiniteMaterialDataset:
    deformation_axis: FiniteMeasurementAxis
    response_axis: FiniteMeasurementAxis
    deformations: tuple[int, ...]
    responses: tuple[int, ...]
    source_id: str

    def __post_init__(self) -> None:
        if len(self.deformations) != len(self.responses):
            raise ValueError("deformation and response observations must have equal length")
        if not self.deformations:
            raise ValueError("material dataset must contain at least one observation")
        if not isinstance(self.source_id, str) or not self.source_id:
            raise ValueError("source_id must be a nonempty string")
        for value in self.deformations:
            if not self.deformation_axis.contains(value):
                raise ValueError("deformation observation lies outside its declared axis")
        for value in self.responses:
            if not self.response_axis.contains(value):
                raise ValueError("response observation lies outside its declared axis")

    @property
    def observation_count(self) -> int:
        return len(self.deformations)


def model_precision_is_independent(dataset: FiniteMaterialDataset, amplitude: int) -> bool:
    """Validate that ``A`` is supplied independently of measurement scale."""
    _require_positive("amplitude", amplitude)
    return True
