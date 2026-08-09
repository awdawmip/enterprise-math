"""Exact accumulation laws for the finite material-impulse world.

When the signed impulse scale is fixed, retaining the bounded impulse detail
makes sequential quantization exactly batch-invariant.  For response samples
``r_t`` on amplitude ``A`` and signed scale ``S``,

    A * sum(j_t) + delta_T = S * sum(r_t),

with initial detail zero.  Equivalently ``sum(j_t)`` and ``delta_T`` are exactly
the signed toward-zero quotient/remainder of the one-shot numerator
``S*sum(r_t)``.  No impulse information is lost merely because the response is
split across several ticks.

For a fixed positive response ``r``, positive outward impulse-scale magnitude
``J`` and an initially approaching normal momentum ``-m`` (m>0), retained
detail gives exact *momentum* event thresholds:

    N_nonnegative = ceil(A*m       / (J*r)),
    N_outward     = ceil(A*(m + 1) / (J*r)).

The first is when the delivered integer normal momentum becomes non-negative;
the second is when it becomes strictly outward.  Calling the latter a physical
``rebound`` additionally requires wall/contact history and no transmission, so
that richer event is intentionally left to the wall/world layer.  A zero
response has no finite threshold.

If detail is deliberately discarded after every event, each event contributes
only ``floor(J*r/A)`` outward quanta.  When ``J*r < A`` this is zero forever,
while retained detail still reaches the finite momentum thresholds above.  This
is an explicit precision-policy effect, not a constitutive or SI-unit claim.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_world_1d import accumulate_material_impulses
from .material_oscillator import signed_divmod_toward_zero


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_integer(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _ceil_div_positive(numerator: int, denominator: int) -> int:
    if numerator < 0 or denominator <= 0:
        raise ValueError("ceil-div arguments require numerator>=0 and denominator>0")
    return (numerator + denominator - 1) // denominator


@dataclass(frozen=True)
class RetainedImpulseTelescope:
    response_samples: tuple[int, ...]
    amplitude: int
    signed_impulse_scale: int
    response_sum: int
    scaled_response_sum: int
    sequential_impulse_quanta: int
    sequential_final_detail: int
    one_shot_impulse_quanta: int
    one_shot_detail: int


def retained_impulse_telescope(
    response_samples: tuple[int, ...] | list[int],
    amplitude: int,
    signed_impulse_scale: int,
) -> RetainedImpulseTelescope:
    """Verify exact sequential-versus-one-shot equivalence with retained detail."""
    _require_positive("amplitude", amplitude)
    _require_integer("signed_impulse_scale", signed_impulse_scale)
    samples = tuple(response_samples)
    for response in samples:
        _require_integer("response_sample", response)
        if not 0 <= response <= amplitude:
            raise ValueError("response samples must lie in 0..amplitude")

    sequential = accumulate_material_impulses(
        samples,
        amplitude,
        signed_impulse_scale,
        retain_detail=True,
    )
    response_sum = sum(samples)
    scaled = signed_impulse_scale * response_sum
    one_shot, detail = signed_divmod_toward_zero(scaled, amplitude)
    if sequential.total_impulse_quanta != one_shot:
        raise AssertionError("retained impulse detail lost batch invariance")
    if sequential.final_detail != detail:
        raise AssertionError("retained impulse detail disagrees with one-shot remainder")
    if amplitude * one_shot + detail != scaled:
        raise AssertionError("retained impulse telescope failed reconstruction")
    return RetainedImpulseTelescope(
        response_samples=samples,
        amplitude=amplitude,
        signed_impulse_scale=signed_impulse_scale,
        response_sum=response_sum,
        scaled_response_sum=scaled,
        sequential_impulse_quanta=sequential.total_impulse_quanta,
        sequential_final_detail=sequential.final_detail,
        one_shot_impulse_quanta=one_shot,
        one_shot_detail=detail,
    )


@dataclass(frozen=True)
class ConstantResponseMomentumThresholds:
    amplitude: int
    response_sample: int
    outward_impulse_scale_magnitude: int
    inward_normal_momentum_magnitude: int
    retained_first_nonnegative_event: int | None
    retained_first_outward_event: int | None
    dropped_impulse_per_event: int
    dropped_first_nonnegative_event: int | None
    dropped_first_outward_event: int | None


def constant_response_momentum_thresholds(
    amplitude: int,
    response_sample: int,
    outward_impulse_scale_magnitude: int,
    inward_normal_momentum_magnitude: int,
) -> ConstantResponseMomentumThresholds:
    """Return exact retained/dropped delivered-momentum thresholds.

    ``inward_normal_momentum_magnitude=m`` represents initial normal momentum
    ``-m`` with ``m>0``.  These thresholds say only when the delivered integer
    momentum reaches zero or becomes outward; rebound remains a world/history
    classification.
    """
    for name, value in (
        ("amplitude", amplitude),
        ("outward_impulse_scale_magnitude", outward_impulse_scale_magnitude),
        ("inward_normal_momentum_magnitude", inward_normal_momentum_magnitude),
    ):
        _require_positive(name, value)
    _require_integer("response_sample", response_sample)
    if not 0 <= response_sample <= amplitude:
        raise ValueError("response_sample must lie in 0..amplitude")

    per_event_numerator = outward_impulse_scale_magnitude * response_sample
    if per_event_numerator == 0:
        retained_nonnegative = None
        retained_outward = None
    else:
        retained_nonnegative = _ceil_div_positive(
            amplitude * inward_normal_momentum_magnitude,
            per_event_numerator,
        )
        retained_outward = _ceil_div_positive(
            amplitude * (inward_normal_momentum_magnitude + 1),
            per_event_numerator,
        )

    dropped_per_event = per_event_numerator // amplitude
    if dropped_per_event == 0:
        dropped_nonnegative = None
        dropped_outward = None
    else:
        dropped_nonnegative = _ceil_div_positive(
            inward_normal_momentum_magnitude,
            dropped_per_event,
        )
        dropped_outward = _ceil_div_positive(
            inward_normal_momentum_magnitude + 1,
            dropped_per_event,
        )

    return ConstantResponseMomentumThresholds(
        amplitude=amplitude,
        response_sample=response_sample,
        outward_impulse_scale_magnitude=outward_impulse_scale_magnitude,
        inward_normal_momentum_magnitude=inward_normal_momentum_magnitude,
        retained_first_nonnegative_event=retained_nonnegative,
        retained_first_outward_event=retained_outward,
        dropped_impulse_per_event=dropped_per_event,
        dropped_first_nonnegative_event=dropped_nonnegative,
        dropped_first_outward_event=dropped_outward,
    )
