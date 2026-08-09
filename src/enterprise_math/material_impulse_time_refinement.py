"""Finite time-refinement compatibility for material impulse projection.

Spatial precision and time cadence are independent E001 world axes.  A coarse
time tick with full-scale impulse capacity ``J`` may be explicitly refined into
subticks with capacities ``J_i``.  This module studies when such a refinement is
semantically neutral.

For a constant material response sample ``r/A`` and retained impulse detail,
any non-negative subcapacity schedule satisfying

    sum_i J_i = J

is exactly equivalent at the lifted-momentum endpoint because

    sum_i J_i*r = J*r.

The result does not depend on substep order.  In contrast, if detail is discarded
at every substep, projection cadence can change the delivered whole impulse even
when the capacities sum exactly.  Example ``A=4,r=1,J=4``: one coarse tick
delivers one whole momentum quantum, while four detail-dropping unit subticks
deliver zero.

If the material response itself changes between subticks, equality is no longer
automatic: the endpoint depends on the explicitly paired sum ``sum_i J_i*r_i``.
Thus time refinement is a declared dynamics change unless the required response
compatibility is proved; hidden substepping is not assumed.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_accumulation import retained_impulse_history_certificate
from .material_impulse_coupling import project_material_impulse


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def balanced_impulse_capacity_schedule(full_capacity: int, substeps: int) -> tuple[int, ...]:
    """Deterministically split J into q/q+1 integer capacities with exact total."""
    _require_nonnegative("full_capacity", full_capacity)
    _require_positive("substeps", substeps)
    q, remainder = divmod(full_capacity, substeps)
    schedule = (q + 1,) * remainder + (q,) * (substeps - remainder)
    if sum(schedule) != full_capacity:
        raise AssertionError("balanced impulse schedule lost total capacity")
    return schedule


@dataclass(frozen=True)
class ConstantResponseTimeRefinementReport:
    full_capacity: int
    subcapacities: tuple[int, ...]
    response_sample: int
    amplitude: int
    coarse_whole_impulse: int
    coarse_detail: int
    refined_whole_impulse_retained: int
    refined_detail_retained: int
    refined_whole_impulse_dropped: int
    retained_endpoint_exact: bool
    dropped_endpoint_exact: bool


def constant_response_time_refinement_report(
    full_capacity: int,
    subcapacities: tuple[int, ...] | list[int],
    response_sample: int,
    amplitude: int,
) -> ConstantResponseTimeRefinementReport:
    """Compare one coarse kick with explicit subticks at constant response."""
    _require_nonnegative("full_capacity", full_capacity)
    _require_nonnegative("response_sample", response_sample)
    _require_positive("amplitude", amplitude)
    if response_sample > amplitude:
        raise ValueError("response_sample must not exceed amplitude")
    schedule = tuple(subcapacities)
    if not schedule:
        raise ValueError("at least one subcapacity is required")
    for capacity in schedule:
        _require_nonnegative("subcapacity", capacity)
    if sum(schedule) != full_capacity:
        raise ValueError("subcapacities must sum exactly to full_capacity")

    coarse = project_material_impulse(
        response_sample,
        amplitude,
        full_capacity,
        1,
        0,
        True,
    )

    retained_whole = 0
    retained_detail = 0
    dropped_whole = 0
    for capacity in schedule:
        retained = project_material_impulse(
            response_sample,
            amplitude,
            capacity,
            1,
            retained_detail,
            True,
        )
        retained_whole += retained.impulse_quanta
        retained_detail = retained.next_detail_numerator

        dropped = project_material_impulse(
            response_sample,
            amplitude,
            capacity,
            1,
            0,
            False,
        )
        dropped_whole += dropped.impulse_quanta

    retained_exact = (
        retained_whole == coarse.impulse_quanta
        and retained_detail == coarse.next_detail_numerator
    )
    if not retained_exact:
        raise AssertionError("retained constant-response time refinement must be exact")
    return ConstantResponseTimeRefinementReport(
        full_capacity=full_capacity,
        subcapacities=schedule,
        response_sample=response_sample,
        amplitude=amplitude,
        coarse_whole_impulse=coarse.impulse_quanta,
        coarse_detail=coarse.next_detail_numerator,
        refined_whole_impulse_retained=retained_whole,
        refined_detail_retained=retained_detail,
        refined_whole_impulse_dropped=dropped_whole,
        retained_endpoint_exact=retained_exact,
        dropped_endpoint_exact=dropped_whole == coarse.impulse_quanta,
    )


@dataclass(frozen=True)
class VariableResponseSubstepPairingReport:
    capacities: tuple[int, ...]
    responses: tuple[int, ...]
    amplitude: int
    paired_raw_impulse_numerator: int
    reversed_response_raw_impulse_numerator: int
    order_defect_numerator: int


def variable_response_pairing_report(
    capacities: tuple[int, ...] | list[int],
    responses: tuple[int, ...] | list[int],
    amplitude: int,
) -> VariableResponseSubstepPairingReport:
    """Expose order sensitivity when capacities and material samples both vary."""
    _require_positive("amplitude", amplitude)
    js = tuple(capacities)
    rs = tuple(responses)
    if not js or len(js) != len(rs):
        raise ValueError("capacities and responses must be equal nonempty sequences")
    for capacity in js:
        _require_nonnegative("capacity", capacity)
    for response in rs:
        _require_nonnegative("response", response)
        if response > amplitude:
            raise ValueError("response must not exceed amplitude")
    paired = sum(capacity * response for capacity, response in zip(js, rs, strict=True))
    reversed_raw = sum(
        capacity * response
        for capacity, response in zip(js, reversed(rs), strict=True)
    )
    return VariableResponseSubstepPairingReport(
        capacities=js,
        responses=rs,
        amplitude=amplitude,
        paired_raw_impulse_numerator=paired,
        reversed_response_raw_impulse_numerator=reversed_raw,
        order_defect_numerator=paired - reversed_raw,
    )
