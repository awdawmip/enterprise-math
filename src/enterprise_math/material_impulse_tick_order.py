"""Explicit tick-order comparator for finite material impulse and mass drift.

Once material response is represented as a signed integer impulse, a world still
has to declare *when* that impulse acts relative to the tick's position drift.
This is not an implementation detail in a discrete state machine.

Two explicit policies are compared:

* ``IMPULSE_THEN_DRIFT``: quantize/apply the material impulse, then drift using
  the updated momentum;
* ``DRIFT_THEN_IMPULSE``: drift using the old momentum, then apply the same
  material impulse at the end of the tick.

Both policies produce the same final momentum and the same impulse detail.  They
need not produce the same position or drift detail.  If their integer
displacements are ``dx_I`` and ``dx_D`` with resulting mass-fiber details
``rho_I`` and ``rho_D``, exact subtraction of the two drift decompositions gives

    m * (dx_I - dx_D) + (rho_I - rho_D) = j,

where ``j`` is the integer impulse quantum applied during the tick.

Thus even when the immediate displacement agrees, the retained drift detail can
remember tick ordering and alter later motion.  Choosing an order is an explicit
E001 world policy; no claim is made here that either ordering is physically
preferred without an external temporal/measurement contract.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_world_1d import (
    MassDriftState1D,
    MaterialImpulseQuantization,
    mass_drift_step,
    material_impulse_quantization,
    momentum_contact_status,
)

IMPULSE_THEN_DRIFT = "IMPULSE_THEN_DRIFT"
DRIFT_THEN_IMPULSE = "DRIFT_THEN_IMPULSE"
TickOrder = str


@dataclass(frozen=True)
class ImpulseDriftTickState1D:
    motion: MassDriftState1D
    impulse_detail: int = 0


@dataclass(frozen=True)
class ImpulseDriftTickOutcome1D:
    order: TickOrder
    before: ImpulseDriftTickState1D
    impulse: MaterialImpulseQuantization
    displacement: int
    after: ImpulseDriftTickState1D
    contact_status_after: str


def material_impulse_drift_tick(
    state: ImpulseDriftTickState1D,
    outward_normal: int,
    response_sample: int,
    amplitude: int,
    impulse_scale_magnitude: int,
    order: TickOrder,
) -> ImpulseDriftTickOutcome1D:
    """Execute one tick under one explicitly declared impulse/drift ordering."""
    if outward_normal not in (-1, 1):
        raise ValueError("outward_normal must be -1 or +1")
    if (
        isinstance(impulse_scale_magnitude, bool)
        or not isinstance(impulse_scale_magnitude, int)
        or impulse_scale_magnitude <= 0
    ):
        raise ValueError("impulse_scale_magnitude must be a positive integer")

    impulse = material_impulse_quantization(
        response_sample,
        amplitude,
        outward_normal * impulse_scale_magnitude,
        state.impulse_detail,
    )
    momentum_after = state.motion.momentum + impulse.impulse_quanta

    if order == IMPULSE_THEN_DRIFT:
        drift_input = MassDriftState1D(
            position=state.motion.position,
            momentum=momentum_after,
            mass=state.motion.mass,
            drift_detail=state.motion.drift_detail,
        )
        drift = mass_drift_step(drift_input)
        final_motion = drift.after
    elif order == DRIFT_THEN_IMPULSE:
        drift = mass_drift_step(state.motion)
        final_motion = MassDriftState1D(
            position=drift.after.position,
            momentum=momentum_after,
            mass=drift.after.mass,
            drift_detail=drift.after.drift_detail,
        )
    else:
        raise ValueError("unknown impulse/drift tick order")

    after = ImpulseDriftTickState1D(
        motion=final_motion,
        impulse_detail=impulse.detail_after,
    )
    return ImpulseDriftTickOutcome1D(
        order=order,
        before=state,
        impulse=impulse,
        displacement=drift.displacement,
        after=after,
        contact_status_after=momentum_contact_status(
            final_motion.momentum,
            outward_normal,
        ),
    )


@dataclass(frozen=True)
class TickOrderComparison1D:
    impulse_then_drift: ImpulseDriftTickOutcome1D
    drift_then_impulse: ImpulseDriftTickOutcome1D
    displacement_difference: int
    drift_detail_difference: int
    impulse_quantum: int


def compare_impulse_drift_orders(
    state: ImpulseDriftTickState1D,
    outward_normal: int,
    response_sample: int,
    amplitude: int,
    impulse_scale_magnitude: int,
) -> TickOrderComparison1D:
    """Run both policies and verify the exact order-defect identity."""
    impulse_first = material_impulse_drift_tick(
        state,
        outward_normal,
        response_sample,
        amplitude,
        impulse_scale_magnitude,
        IMPULSE_THEN_DRIFT,
    )
    drift_first = material_impulse_drift_tick(
        state,
        outward_normal,
        response_sample,
        amplitude,
        impulse_scale_magnitude,
        DRIFT_THEN_IMPULSE,
    )
    if impulse_first.after.motion.momentum != drift_first.after.motion.momentum:
        raise AssertionError("tick order changed final momentum")
    if impulse_first.after.impulse_detail != drift_first.after.impulse_detail:
        raise AssertionError("tick order changed impulse detail")

    displacement_difference = (
        impulse_first.displacement - drift_first.displacement
    )
    drift_detail_difference = (
        impulse_first.after.motion.drift_detail
        - drift_first.after.motion.drift_detail
    )
    if (
        state.motion.mass * displacement_difference + drift_detail_difference
        != impulse_first.impulse.impulse_quanta
    ):
        raise AssertionError("tick-order displacement/detail identity failed")

    return TickOrderComparison1D(
        impulse_then_drift=impulse_first,
        drift_then_impulse=drift_first,
        displacement_difference=displacement_difference,
        drift_detail_difference=drift_detail_difference,
        impulse_quantum=impulse_first.impulse.impulse_quanta,
    )
