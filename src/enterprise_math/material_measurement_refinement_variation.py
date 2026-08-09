"""Variation and sharp bounds for exact measurement-area refinement shells.

This E001 empirical layer consumes the exact local shell from
``material_measurement_area_refinement``.  It adds diagnostics only; it does not
interpolate missing samples or identify the finite polyline coordinate with an
unknown continuum curve.

For three measured points with deformation gaps

    a = e1-e0 > 0,   b = e2-e1 > 0,

the local doubled-area shell is

    delta = b*(s1-s0) - a*(s2-s1).

Thus ``delta`` is a division-free numerator for the change between the two
adjacent secant slopes.  Its sign is meaningful only relative to the declared
axis orientation/sign convention; the module therefore reports the signed
integer rather than silently naming physical convexity.

If every response count lies in one declared integer interval ``[L,U]``, with
range width ``R=U-L``, linear extremality gives the sharp bound

    |delta| <= (e2-e0)*R.

Equality is attained by putting the inserted response at one endpoint of the
range and both coarse endpoints at the other.

For a refinement history with local shells ``delta_t`` define

    V = sum_t |delta_t|,
    Delta = sum_t delta_t,
    C = (V-|Delta|)/2.

``V`` is witness activity, while ``Delta`` is the endpoint area defect already
known to telescope.  The exact non-negative integer ``C`` equals the smaller of
total positive and total negative shell mass, so it is precisely the amount of
local refinement activity cancelled in the final scalar.  Two insertion orders
can have the same final measured polyline and ``Delta`` but different ``V`` and
``C``.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_measurement_area_refinement import (
    MeasurementPoint,
    MeasurementRefinementTrace,
    trace_measurement_refinement,
    trapezoid_refinement_shell,
)

SHELL_NEGATIVE = "SHELL_NEGATIVE"
SHELL_ZERO = "SHELL_ZERO"
SHELL_POSITIVE = "SHELL_POSITIVE"


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def secant_slope_change_numerator(
    left: MeasurementPoint,
    inserted: MeasurementPoint,
    right: MeasurementPoint,
) -> int:
    """Return ``b*(s1-s0)-a*(s2-s1)``, exactly the local area shell."""
    e0, s0 = left
    e1, s1 = inserted
    e2, s2 = right
    # Delegate complete point/increasing-order validation to the canonical shell.
    shell = trapezoid_refinement_shell(left, inserted, right)
    a = e1 - e0
    b = e2 - e1
    numerator = b * (s1 - s0) - a * (s2 - s1)
    if numerator != shell:
        raise AssertionError("secant-slope numerator disagrees with trapezoid shell")
    return numerator


def refinement_shell_sign(
    left: MeasurementPoint,
    inserted: MeasurementPoint,
    right: MeasurementPoint,
) -> str:
    value = secant_slope_change_numerator(left, inserted, right)
    if value < 0:
        return SHELL_NEGATIVE
    if value == 0:
        return SHELL_ZERO
    return SHELL_POSITIVE


@dataclass(frozen=True)
class RefinementShellRangeBound:
    response_lower: int
    response_upper: int
    response_range_width: int
    deformation_span: int
    shell: int
    absolute_shell: int
    sharp_absolute_bound: int
    attains_bound: bool


def refinement_shell_range_bound(
    left: MeasurementPoint,
    inserted: MeasurementPoint,
    right: MeasurementPoint,
    response_lower: int,
    response_upper: int,
) -> RefinementShellRangeBound:
    """Verify the sharp response-range bound ``|delta| <= span*(U-L)``."""
    _require_integer("response_lower", response_lower)
    _require_integer("response_upper", response_upper)
    if response_lower > response_upper:
        raise ValueError("response_lower must not exceed response_upper")
    for point in (left, inserted, right):
        if not response_lower <= point[1] <= response_upper:
            raise ValueError("every response count must lie in the declared range")

    shell = trapezoid_refinement_shell(left, inserted, right)
    span = right[0] - left[0]
    width = response_upper - response_lower
    bound = span * width
    if abs(shell) > bound:
        raise AssertionError("measurement refinement shell escaped the sharp range bound")
    return RefinementShellRangeBound(
        response_lower=response_lower,
        response_upper=response_upper,
        response_range_width=width,
        deformation_span=span,
        shell=shell,
        absolute_shell=abs(shell),
        sharp_absolute_bound=bound,
        attains_bound=(abs(shell) == bound),
    )


@dataclass(frozen=True)
class RefinementWitnessVariation:
    local_shells: tuple[int, ...]
    total_shell: int
    positive_shell_mass: int
    negative_shell_mass: int
    witness_activity: int
    cancelled_shell_mass: int


def refinement_witness_variation_from_shells(
    local_shells: tuple[int, ...] | list[int],
) -> RefinementWitnessVariation:
    """Return exact total/variation/cancellation accounting for local shells."""
    shells = tuple(local_shells)
    if any(isinstance(value, bool) or not isinstance(value, int) for value in shells):
        raise ValueError("local shells must be integers")
    positive = sum(value for value in shells if value > 0)
    negative = sum(-value for value in shells if value < 0)
    total = positive - negative
    activity = positive + negative
    defect = activity - abs(total)
    if defect < 0 or defect % 2:
        raise AssertionError("shell variation/cancellation parity identity failed")
    cancelled = defect // 2
    if cancelled != min(positive, negative):
        raise AssertionError("cancelled shell mass disagrees with signed decomposition")
    return RefinementWitnessVariation(
        local_shells=shells,
        total_shell=total,
        positive_shell_mass=positive,
        negative_shell_mass=negative,
        witness_activity=activity,
        cancelled_shell_mass=cancelled,
    )


def refinement_witness_variation(
    trace: MeasurementRefinementTrace,
) -> RefinementWitnessVariation:
    """Apply variation accounting to one exact measurement-refinement trace."""
    report = refinement_witness_variation_from_shells(trace.local_area_shells)
    if report.total_shell != trace.total_area_shell:
        raise AssertionError("variation total disagrees with refinement telescope")
    return report


@dataclass(frozen=True)
class RefinementOrderVariationComparison:
    first_trace: MeasurementRefinementTrace
    second_trace: MeasurementRefinementTrace
    first_variation: RefinementWitnessVariation
    second_variation: RefinementWitnessVariation
    same_final_polyline: bool
    same_total_shell: bool
    same_witness_activity: bool
    same_cancelled_shell_mass: bool


def compare_refinement_order_variation(
    initial: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
    first_order: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
    second_order: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
) -> RefinementOrderVariationComparison:
    """Compare endpoint shell and witness activity for two measurement histories."""
    first = trace_measurement_refinement(initial, first_order)
    second = trace_measurement_refinement(initial, second_order)
    first_variation = refinement_witness_variation(first)
    second_variation = refinement_witness_variation(second)
    same_final = first.final == second.final
    same_total = first.total_area_shell == second.total_area_shell
    if same_final and not same_total:
        raise AssertionError("same final polyline changed total refinement shell")
    return RefinementOrderVariationComparison(
        first_trace=first,
        second_trace=second,
        first_variation=first_variation,
        second_variation=second_variation,
        same_final_polyline=same_final,
        same_total_shell=same_total,
        same_witness_activity=(
            first_variation.witness_activity == second_variation.witness_activity
        ),
        same_cancelled_shell_mass=(
            first_variation.cancelled_shell_mass
            == second_variation.cancelled_shell_mass
        ),
    )
