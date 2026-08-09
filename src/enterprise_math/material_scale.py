"""Exact integer scale transport for E001 material curve transforms.

The root-based softening transform is exactly homogeneous under an integer
refinement ``(s,A)->(lambda*s,lambda*A)``.  The quotient-based hardening
transform instead acquires one explicit bounded remainder/carry defect.

These are arithmetic scale identities, not physical similarity laws.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import hardening_sample, softening_sample


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _validate_sample(sample: int, amplitude: int) -> None:
    if isinstance(sample, bool) or not isinstance(sample, int) or sample < 0:
        raise ValueError("sample must be a non-negative integer")
    _require_positive("amplitude", amplitude)
    if sample > amplitude:
        raise ValueError("sample must not exceed amplitude")


@dataclass(frozen=True)
class HardeningScaleReport:
    """Exact scale defect of the quotient/power hardening transform."""

    base_value: int
    scaled_value: int
    transported_base: int
    defect: int
    denominator: int
    base_remainder: int
    expected_defect_from_remainder: int


@dataclass(frozen=True)
class SofteningScaleReport:
    """Exact integer homogeneity report for the root softening transform."""

    base_value: int
    scaled_value: int
    transported_base: int
    defect: int


def hardening_scale_report(
    sample: int,
    amplitude: int,
    power: int,
    refinement: int,
) -> HardeningScaleReport:
    """Return H_p(lambda*s;lambda*A)-lambda*H_p(s;A) exactly."""
    _validate_sample(sample, amplitude)
    _require_positive("power", power)
    _require_positive("refinement", refinement)

    base = hardening_sample(sample, amplitude, power)
    scaled = hardening_sample(
        refinement * sample,
        refinement * amplitude,
        power,
    )
    transported = refinement * base
    defect = scaled - transported

    denominator = amplitude ** (power - 1)
    remainder = sample**power % denominator
    expected = refinement * remainder // denominator
    if defect != expected:
        raise AssertionError("hardening scale defect disagrees with quotient remainder")
    if not 0 <= defect < refinement:
        raise AssertionError("hardening scale defect escaped its carry range")

    return HardeningScaleReport(
        base_value=base,
        scaled_value=scaled,
        transported_base=transported,
        defect=defect,
        denominator=denominator,
        base_remainder=remainder,
        expected_defect_from_remainder=expected,
    )


def softening_scale_report(
    sample: int,
    amplitude: int,
    power: int,
    refinement: int,
) -> SofteningScaleReport:
    """Verify G_p(lambda*s;lambda*A)=lambda*G_p(s;A)."""
    _validate_sample(sample, amplitude)
    _require_positive("power", power)
    _require_positive("refinement", refinement)

    base = softening_sample(sample, amplitude, power)
    scaled = softening_sample(
        refinement * sample,
        refinement * amplitude,
        power,
    )
    transported = refinement * base
    defect = scaled - transported
    if defect != 0:
        raise AssertionError("root softening lost exact integer scale homogeneity")

    return SofteningScaleReport(
        base_value=base,
        scaled_value=scaled,
        transported_base=transported,
        defect=defect,
    )
