"""Finite work-energy turning and rebound oracle for an explicit material force law.

This E001 layer asks the constitutive question before choosing a time integrator:
given an incoming kinetic/work resource already calibrated into the same doubled
work coordinate as ``FiniteForceLaw``, how deep can the represented material be
compressed, and how much work can its declared returning branch release?

Let

    L_k = doubled loading chord work from depth 0 to k,
    R_k = doubled returning chord work from depth 0 to k.

Both are exact integers.  For an incoming resource E>=0:

* if ``E == L_k`` at the first represented depth k where the resource is fully
  consumed, the turning depth is exactly represented;
* if ``L_k < E < L_{k+1}``, the turning point lies inside a material interval and
  is explicitly ``TURN_UNDERRESOLVED`` -- no interpolation is invented;
* if ``E > L_K`` at the deepest represented material state, the material depth is
  ``MATERIAL_UNDERRESOLVED``.

At an exact turn k, a full return to zero deformation releases exactly ``R_k`` in
the same work coordinate, so

    dissipated = L_k - R_k,
    outgoing_resource = R_k.

For a passive cycle ``R_k<=L_k`` this can never exceed the incoming resource.  No
coefficient of restitution is required.  If one later wants a momentum magnitude,
that is a separate finite square/root projection problem with its own precision.

This is a static work-energy oracle, not a time evolution law.  It is useful as a
passivity/turning benchmark for explicit impulse worlds and for direct empirical
force-displacement data.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_force_work import FiniteForceLaw, force_cycle_work_report

EXACT_TURN = "EXACT_TURN"
TURN_UNDERRESOLVED = "TURN_UNDERRESOLVED"
MATERIAL_UNDERRESOLVED = "MATERIAL_UNDERRESOLVED"


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def loading_work_prefix_numerators2(law: FiniteForceLaw) -> tuple[int, ...]:
    return tuple(
        force_cycle_work_report(law, depth).loading_work_numerator2
        for depth in range(len(law.profile.loading))
    )


def returning_work_prefix_numerators2(law: FiniteForceLaw) -> tuple[int, ...]:
    return tuple(
        force_cycle_work_report(law, depth).returned_work_numerator2
        for depth in range(len(law.profile.returning))
    )


@dataclass(frozen=True)
class MaterialTurningReport:
    incoming_work_resource_numerator2: int
    status: str
    exact_turn_depth: int | None
    lower_represented_depth: int | None
    upper_represented_depth: int | None
    lower_loading_work_numerator2: int | None
    upper_loading_work_numerator2: int | None
    deepest_loading_work_numerator2: int


def material_turning_report(
    law: FiniteForceLaw,
    incoming_work_resource_numerator2: int,
) -> MaterialTurningReport:
    """Locate an exact, interval-underresolved, or depth-underresolved turn."""
    _nonnegative("incoming_work_resource_numerator2", incoming_work_resource_numerator2)
    energy = incoming_work_resource_numerator2
    prefixes = loading_work_prefix_numerators2(law)
    if any(right < left for left, right in zip(prefixes, prefixes[1:])):
        raise AssertionError("non-negative force law produced decreasing loading work")

    for depth, work in enumerate(prefixes):
        if energy == work:
            return MaterialTurningReport(
                incoming_work_resource_numerator2=energy,
                status=EXACT_TURN,
                exact_turn_depth=depth,
                lower_represented_depth=depth,
                upper_represented_depth=depth,
                lower_loading_work_numerator2=work,
                upper_loading_work_numerator2=work,
                deepest_loading_work_numerator2=prefixes[-1],
            )
        if energy < work:
            lower = depth - 1
            return MaterialTurningReport(
                incoming_work_resource_numerator2=energy,
                status=TURN_UNDERRESOLVED,
                exact_turn_depth=None,
                lower_represented_depth=lower,
                upper_represented_depth=depth,
                lower_loading_work_numerator2=prefixes[lower],
                upper_loading_work_numerator2=work,
                deepest_loading_work_numerator2=prefixes[-1],
            )

    return MaterialTurningReport(
        incoming_work_resource_numerator2=energy,
        status=MATERIAL_UNDERRESOLVED,
        exact_turn_depth=None,
        lower_represented_depth=len(prefixes) - 1,
        upper_represented_depth=None,
        lower_loading_work_numerator2=prefixes[-1],
        upper_loading_work_numerator2=None,
        deepest_loading_work_numerator2=prefixes[-1],
    )


@dataclass(frozen=True)
class StaticMaterialReboundReport:
    turning: MaterialTurningReport
    loading_work_numerator2: int | None
    returning_work_numerator2: int | None
    dissipated_work_numerator2: int | None
    outgoing_work_resource_numerator2: int | None
    passive_at_turn: bool | None
    retention_ratio_numerator: int | None
    retention_ratio_denominator: int | None


def static_material_rebound_report(
    law: FiniteForceLaw,
    incoming_work_resource_numerator2: int,
) -> StaticMaterialReboundReport:
    """Return curve-derived outgoing work only when the turning depth is represented."""
    turning = material_turning_report(law, incoming_work_resource_numerator2)
    if turning.status != EXACT_TURN:
        return StaticMaterialReboundReport(
            turning=turning,
            loading_work_numerator2=None,
            returning_work_numerator2=None,
            dissipated_work_numerator2=None,
            outgoing_work_resource_numerator2=None,
            passive_at_turn=None,
            retention_ratio_numerator=None,
            retention_ratio_denominator=None,
        )
    depth = turning.exact_turn_depth
    if depth is None:
        raise AssertionError("exact turn lost its depth")
    cycle = force_cycle_work_report(law, depth)
    load = cycle.loading_work_numerator2
    returned = cycle.returned_work_numerator2
    loss = load - returned
    if load == 0:
        ratio_num, ratio_den = (0, 1) if returned == 0 else (returned, 0)
        if ratio_den == 0:
            raise AssertionError("zero loading work cannot release positive passive work")
    else:
        common = gcd(abs(returned), load)
        ratio_num = returned // common
        ratio_den = load // common
    return StaticMaterialReboundReport(
        turning=turning,
        loading_work_numerator2=load,
        returning_work_numerator2=returned,
        dissipated_work_numerator2=loss,
        outgoing_work_resource_numerator2=returned,
        passive_at_turn=loss >= 0,
        retention_ratio_numerator=ratio_num,
        retention_ratio_denominator=ratio_den,
    )
