"""Exact integer scale transport for E001 material curves and oscillators.

Both material transforms have explicit finite refinement carries:

* quotient/power hardening gets a carry from its Euclidean remainder;
* root softening gets a carry from the unresolved remainder inside the coarse
  integer-root basin.

For ``N=s*A^(p-1)=q^p+delta`` and integer refinement ``lambda``:

    R_p(lambda^p*N) = lambda*q + kappa,

where ``0 <= kappa < lambda`` and ``kappa`` is the largest integer in that range
whose p-th-power increment over ``(lambda*q)^p`` fits inside the refined
remainder budget ``lambda^p*delta``.  Exact homogeneity is therefore a special
zero-carry case, not the generic law.

The projected Pythagorean oscillator has a related coordinatewise law: scaling
the input state by ``lambda`` transports the projected output by ``lambda`` plus
one signed carry determined completely by the original projection detail.

These are arithmetic scale identities, not physical similarity laws.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    projected_rotation_step,
)
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
    """Exact bounded root-carry report for the softening transform."""

    base_value: int
    scaled_value: int
    transported_base: int
    defect: int
    base_argument: int
    base_root_remainder: int
    refined_remainder_budget: int
    expected_defect_from_remainder: int


@dataclass(frozen=True)
class RotationScaleReport:
    """Exact coordinatewise refinement defect of one projected rotation step."""

    base_state: tuple[int, int]
    refined_state: tuple[int, int]
    base_after: tuple[int, int]
    refined_after: tuple[int, int]
    transported_base_after: tuple[int, int]
    base_details: tuple[int, int]
    defects: tuple[int, int]
    expected_defects_from_details: tuple[int, int]


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


def _expected_root_refinement_carry(
    base_root: int,
    base_remainder: int,
    power: int,
    refinement: int,
) -> int:
    """Largest ``k<lambda`` supported by the refined root-basin remainder."""
    transported = refinement * base_root
    budget = refinement**power * base_remainder
    expected = 0
    for carry in range(1, refinement):
        increment = (transported + carry) ** power - transported**power
        if increment <= budget:
            expected = carry
        else:
            break
    return expected


def softening_scale_report(
    sample: int,
    amplitude: int,
    power: int,
    refinement: int,
) -> SofteningScaleReport:
    """Return the exact root-refinement carry of ``G_p``.

    If ``N=s*A^(p-1)=q^p+delta`` then the refined argument is
    ``lambda^p*N`` and the refined root has the form ``lambda*q+kappa`` with
    ``0<=kappa<lambda``.  The carry is exactly determined by ``delta``.
    """
    _validate_sample(sample, amplitude)
    _require_positive("power", power)
    _require_positive("refinement", refinement)

    base_argument = sample * amplitude ** (power - 1)
    base = softening_sample(sample, amplitude, power)
    base_remainder = base_argument - base**power
    if base_remainder < 0:
        raise AssertionError("integer root exceeded its argument")

    scaled = softening_sample(
        refinement * sample,
        refinement * amplitude,
        power,
    )
    transported = refinement * base
    defect = scaled - transported
    expected = _expected_root_refinement_carry(
        base,
        base_remainder,
        power,
        refinement,
    )
    if defect != expected:
        raise AssertionError("root refinement carry disagrees with basin remainder")
    if not 0 <= defect < refinement:
        raise AssertionError("root refinement carry escaped its finite shell")

    return SofteningScaleReport(
        base_value=base,
        scaled_value=scaled,
        transported_base=transported,
        defect=defect,
        base_argument=base_argument,
        base_root_remainder=base_remainder,
        refined_remainder_budget=refinement**power * base_remainder,
        expected_defect_from_remainder=expected,
    )


def _scaled_signed_detail_defect(detail: int, divisor: int, refinement: int) -> int:
    if detail == 0:
        return 0
    sign = 1 if detail > 0 else -1
    return sign * (refinement * abs(detail) // divisor)


def rotation_scale_report(
    state: tuple[int, int],
    rotation: PythagoreanRotation,
    refinement: int,
) -> RotationScaleReport:
    """Verify projected rotation transport under integer state refinement.

    If one base lifted coordinate is ``c*q+delta`` under toward-zero projection,
    then the same coordinate from the ``lambda``-scaled input projects to

        lambda*q + sign(delta)*floor(lambda*|delta|/c).

    The coordinate defect therefore has absolute value strictly below lambda.
    """
    _require_positive("refinement", refinement)
    x, y = state
    if isinstance(x, bool) or not isinstance(x, int):
        raise ValueError("state x must be an integer")
    if isinstance(y, bool) or not isinstance(y, int):
        raise ValueError("state y must be an integer")

    base = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
    refined_state = (refinement * x, refinement * y)
    refined = projected_rotation_step(*refined_state, rotation, TOWARD_ZERO)
    transported = (
        refinement * base.after[0],
        refinement * base.after[1],
    )
    defects = (
        refined.after[0] - transported[0],
        refined.after[1] - transported[1],
    )
    expected = tuple(
        _scaled_signed_detail_defect(detail, rotation.c, refinement)
        for detail in base.details
    )
    if defects != expected:
        raise AssertionError("rotation refinement defect disagrees with base detail")
    if any(abs(defect) >= refinement for defect in defects):
        raise AssertionError("rotation refinement defect escaped its carry range")

    return RotationScaleReport(
        base_state=state,
        refined_state=refined_state,
        base_after=base.after,
        refined_after=refined.after,
        transported_base_after=transported,
        base_details=base.details,
        defects=defects,
        expected_defects_from_details=expected,
    )
