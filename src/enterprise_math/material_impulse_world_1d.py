"""Finite 1D material impulse and momentum-drift comparator.

This module explores the next E001 world-law layer without inserting a
``REBOUND -> reverse motion`` command.  A finite material response sample first
passes through one declared integer impulse calibration.  The resulting signed
impulse is added to momentum.  Rebound, stop, or continued approach are then
*observed* from the momentum sign relative to an explicit wall normal.

Two bounded details remain first-class precision choices:

1. impulse detail: for response ``r/A`` and signed impulse scale ``S``,

       raw = detail + S*r,
       raw = A*j + detail',

   where ``j`` is the signed integer impulse quantum;
2. drift detail: for signed momentum ``p`` and positive integer mass ``m``,

       raw = drift_detail + p,
       raw = m*dx + drift_detail'.

Both quotients use the canonical signed toward-zero division from the E001
oscillator, avoiding the negative-direction bias of floor division.  Retaining
these details gives exact telescoping ledgers; deliberately dropping them is an
explicit lower-precision policy.

The calibration scale, momentum and mass are integer model coordinates.  This
module does not claim SI-unit calibration, conservation for an external closed
physical system, or constitutive-law validity without separate empirical work.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import signed_divmod_toward_zero

APPROACHING = "APPROACHING"
STOPPED = "STOPPED"
REBOUND = "REBOUND"


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_integer(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


@dataclass(frozen=True)
class MaterialImpulseQuantization:
    response_sample: int
    amplitude: int
    signed_impulse_scale: int
    detail_before: int
    raw_signed_numerator: int
    impulse_quanta: int
    detail_after: int


def material_impulse_quantization(
    response_sample: int,
    amplitude: int,
    signed_impulse_scale: int,
    detail: int = 0,
) -> MaterialImpulseQuantization:
    """Quantize one signed calibrated material impulse with retained detail."""
    _require_positive("amplitude", amplitude)
    _require_integer("response_sample", response_sample)
    _require_integer("signed_impulse_scale", signed_impulse_scale)
    _require_integer("detail", detail)
    if not 0 <= response_sample <= amplitude:
        raise ValueError("response_sample must lie in 0..amplitude")
    if abs(detail) >= amplitude:
        raise ValueError("impulse detail must lie in the signed amplitude fiber")

    raw = detail + signed_impulse_scale * response_sample
    impulse, detail_after = signed_divmod_toward_zero(raw, amplitude)
    if amplitude * impulse + detail_after != raw:
        raise AssertionError("impulse quotient/detail failed exact reconstruction")
    return MaterialImpulseQuantization(
        response_sample=response_sample,
        amplitude=amplitude,
        signed_impulse_scale=signed_impulse_scale,
        detail_before=detail,
        raw_signed_numerator=raw,
        impulse_quanta=impulse,
        detail_after=detail_after,
    )


@dataclass(frozen=True)
class ImpulseSequenceReport:
    response_samples: tuple[int, ...]
    amplitude: int
    signed_impulse_scale: int
    retain_detail: bool
    impulse_quanta: tuple[int, ...]
    details_after: tuple[int, ...]
    total_impulse_quanta: int
    final_detail: int


def accumulate_material_impulses(
    response_samples: tuple[int, ...] | list[int],
    amplitude: int,
    signed_impulse_scale: int,
    retain_detail: bool = True,
) -> ImpulseSequenceReport:
    """Apply repeated response impulses with retained or deliberately dropped detail."""
    samples = tuple(response_samples)
    detail = 0
    impulses: list[int] = []
    details: list[int] = []
    for response in samples:
        report = material_impulse_quantization(
            response,
            amplitude,
            signed_impulse_scale,
            detail if retain_detail else 0,
        )
        impulses.append(report.impulse_quanta)
        details.append(report.detail_after)
        detail = report.detail_after if retain_detail else 0
    return ImpulseSequenceReport(
        response_samples=samples,
        amplitude=amplitude,
        signed_impulse_scale=signed_impulse_scale,
        retain_detail=retain_detail,
        impulse_quanta=tuple(impulses),
        details_after=tuple(details),
        total_impulse_quanta=sum(impulses),
        final_detail=detail,
    )


def momentum_contact_status(
    momentum: int,
    outward_normal: int,
) -> str:
    """Classify signed momentum relative to an explicit outward wall normal."""
    _require_integer("momentum", momentum)
    _require_integer("outward_normal", outward_normal)
    if outward_normal not in (-1, 1):
        raise ValueError("outward_normal must be -1 or +1")
    signed = outward_normal * momentum
    if signed < 0:
        return APPROACHING
    if signed == 0:
        return STOPPED
    return REBOUND


@dataclass(frozen=True)
class MomentumImpulseStep:
    momentum_before: int
    momentum_after: int
    outward_normal: int
    status_before: str
    status_after: str
    impulse: MaterialImpulseQuantization


def apply_material_impulse_to_momentum(
    momentum: int,
    outward_normal: int,
    response_sample: int,
    amplitude: int,
    impulse_scale_magnitude: int,
    impulse_detail: int = 0,
) -> MomentumImpulseStep:
    """Apply an outward material impulse; rebound is derived from the new sign."""
    _require_integer("momentum", momentum)
    _require_positive("impulse_scale_magnitude", impulse_scale_magnitude)
    if outward_normal not in (-1, 1):
        raise ValueError("outward_normal must be -1 or +1")
    impulse = material_impulse_quantization(
        response_sample,
        amplitude,
        outward_normal * impulse_scale_magnitude,
        impulse_detail,
    )
    after = momentum + impulse.impulse_quanta
    return MomentumImpulseStep(
        momentum_before=momentum,
        momentum_after=after,
        outward_normal=outward_normal,
        status_before=momentum_contact_status(momentum, outward_normal),
        status_after=momentum_contact_status(after, outward_normal),
        impulse=impulse,
    )


@dataclass(frozen=True)
class MassDriftState1D:
    position: int
    momentum: int
    mass: int
    drift_detail: int = 0

    def __post_init__(self) -> None:
        _require_integer("position", self.position)
        _require_integer("momentum", self.momentum)
        _require_positive("mass", self.mass)
        _require_integer("drift_detail", self.drift_detail)
        if abs(self.drift_detail) >= self.mass:
            raise ValueError("drift_detail must lie in the signed mass fiber")


@dataclass(frozen=True)
class MassDriftStep1D:
    before: MassDriftState1D
    displacement: int
    raw_drift_numerator: int
    after: MassDriftState1D


def mass_drift_step(state: MassDriftState1D) -> MassDriftStep1D:
    """Advance one tick using exact signed quotient/detail mass drift."""
    raw = state.drift_detail + state.momentum
    displacement, detail_after = signed_divmod_toward_zero(raw, state.mass)
    after = MassDriftState1D(
        position=state.position + displacement,
        momentum=state.momentum,
        mass=state.mass,
        drift_detail=detail_after,
    )
    if state.mass * displacement + detail_after != raw:
        raise AssertionError("mass drift failed exact quotient/detail identity")
    return MassDriftStep1D(
        before=state,
        displacement=displacement,
        raw_drift_numerator=raw,
        after=after,
    )


def trace_constant_momentum_drift(
    initial: MassDriftState1D,
    ticks: int,
) -> tuple[MassDriftStep1D, ...]:
    """Trace constant momentum and verify the exact cumulative drift telescope."""
    if isinstance(ticks, bool) or not isinstance(ticks, int) or ticks < 0:
        raise ValueError("ticks must be a non-negative integer")
    current = initial
    steps: list[MassDriftStep1D] = []
    for _ in range(ticks):
        step = mass_drift_step(current)
        steps.append(step)
        current = step.after
    left = initial.mass * (current.position - initial.position)
    left += current.drift_detail - initial.drift_detail
    right = ticks * initial.momentum
    if left != right:
        raise AssertionError("constant-momentum drift failed cumulative telescope")
    return tuple(steps)
