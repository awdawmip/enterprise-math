"""Exact finite trapezoid coordinates for measured stress-strain hysteresis.

This E001 empirical helper works directly on declared integer measurement axes.
It does not fit a polynomial, interpolate missing samples, or assume that loading
and unloading share the same interior deformation grid.

For one strictly monotone measured branch, observations are re-oriented to
increasing deformation count and the exact doubled area coordinate is

    area2 = sum_i (s_i+s_{i+1}) * (e_{i+1}-e_i).

A caller supplies ``response_sign`` (+1 or -1) to make the intended stress sign
convention explicit; no absolute-value convention is hidden.

If deformation counts represent ``1/E_s`` of a declared strain/deformation unit
and response counts represent ``1/S_s`` of a declared stress unit, the exact
product coordinate is

    area = area2 / (2*E_s*S_s).

When the deformation axis is engineering strain (dimensionless), this product is
an engineering stress-strain work-density coordinate.  The unit interpretation is
still caller-declared; this module does not infer dimensional physics from a unit
string.

Two branches form a closed-deformation hysteresis comparison only when their
oriented lower and upper deformation endpoints agree.  Interior sample grids may
differ.  The relative loss coordinate is then

    (A_load-A_return)/A_load

provided the normalized loading area is strictly positive.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_measurement import FiniteMaterialDataset


@dataclass(frozen=True)
class ExactFiniteRatio:
    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        if isinstance(self.numerator, bool) or not isinstance(self.numerator, int):
            raise ValueError("numerator must be an integer")
        if isinstance(self.denominator, bool) or not isinstance(self.denominator, int) or self.denominator <= 0:
            raise ValueError("denominator must be a positive integer")


@dataclass(frozen=True)
class MeasuredBranchArea:
    source_id: str
    deformation_lower_count: int
    deformation_upper_count: int
    observation_count: int
    response_sign: int
    doubled_area_numerator: int
    exact_area: ExactFiniteRatio
    product_unit: str
    input_was_increasing: bool


def _strict_orientation(values: tuple[int, ...]) -> int:
    if len(values) < 2:
        raise ValueError("measured branch requires at least two observations")
    if all(a < b for a, b in zip(values, values[1:])):
        return 1
    if all(a > b for a, b in zip(values, values[1:])):
        return -1
    raise ValueError("deformation observations must be strictly monotone within one branch")


def measured_branch_trapezoid_area(
    dataset: FiniteMaterialDataset,
    response_sign: int = 1,
) -> MeasuredBranchArea:
    """Integrate one measured branch exactly after explicit orientation normalization."""
    if response_sign not in (-1, 1):
        raise ValueError("response_sign must be -1 or +1")
    deformations = tuple(dataset.deformations)
    responses = tuple(dataset.responses)
    orientation = _strict_orientation(deformations)
    if orientation < 0:
        deformations = tuple(reversed(deformations))
        responses = tuple(reversed(responses))
    responses = tuple(response_sign * value for value in responses)

    area2 = 0
    for left_e, right_e, left_s, right_s in zip(
        deformations,
        deformations[1:],
        responses,
        responses[1:],
        strict=True,
    ):
        area2 += (left_s + right_s) * (right_e - left_e)

    denominator = 2 * dataset.deformation_axis.scale_factor * dataset.response_axis.scale_factor
    common = gcd(abs(area2), denominator)
    exact = ExactFiniteRatio(area2 // common, denominator // common)
    return MeasuredBranchArea(
        source_id=dataset.source_id,
        deformation_lower_count=deformations[0],
        deformation_upper_count=deformations[-1],
        observation_count=len(deformations),
        response_sign=response_sign,
        doubled_area_numerator=area2,
        exact_area=exact,
        product_unit=f"{dataset.response_axis.unit}*{dataset.deformation_axis.unit}",
        input_was_increasing=orientation > 0,
    )


@dataclass(frozen=True)
class MeasuredHysteresisReport:
    loading: MeasuredBranchArea
    returning: MeasuredBranchArea
    doubled_loss_numerator: int
    exact_loss: ExactFiniteRatio
    relative_loss: ExactFiniteRatio
    closed_deformation_interval: bool


def measured_hysteresis_report(
    loading: FiniteMaterialDataset,
    returning: FiniteMaterialDataset,
    response_sign: int = 1,
    require_closed_deformation_interval: bool = True,
) -> MeasuredHysteresisReport:
    """Compare exact measured branch areas without interpolating interior samples."""
    if loading.deformation_axis != returning.deformation_axis:
        raise ValueError("loading and returning deformation axes must match exactly")
    if loading.response_axis != returning.response_axis:
        raise ValueError("loading and returning response axes must match exactly")

    load_area = measured_branch_trapezoid_area(loading, response_sign)
    return_area = measured_branch_trapezoid_area(returning, response_sign)
    closed = (
        load_area.deformation_lower_count == return_area.deformation_lower_count
        and load_area.deformation_upper_count == return_area.deformation_upper_count
    )
    if require_closed_deformation_interval and not closed:
        raise ValueError("loading and returning branches do not share one closed deformation interval")
    if load_area.doubled_area_numerator <= 0:
        raise ValueError("normalized loading area must be positive for relative hysteresis loss")

    loss2 = load_area.doubled_area_numerator - return_area.doubled_area_numerator
    physical_denominator = (
        2 * loading.deformation_axis.scale_factor * loading.response_axis.scale_factor
    )
    common_loss = gcd(abs(loss2), physical_denominator)
    exact_loss = ExactFiniteRatio(
        loss2 // common_loss,
        physical_denominator // common_loss,
    )
    common_relative = gcd(abs(loss2), load_area.doubled_area_numerator)
    relative = ExactFiniteRatio(
        loss2 // common_relative,
        load_area.doubled_area_numerator // common_relative,
    )
    return MeasuredHysteresisReport(
        loading=load_area,
        returning=return_area,
        doubled_loss_numerator=loss2,
        exact_loss=exact_loss,
        relative_loss=relative,
        closed_deformation_interval=closed,
    )
