"""Exact lifted-momentum accounting for retained finite material impulse detail.

When material impulse projection keeps its remainder, the pair

    (whole momentum p, detail eta),    |eta|<A,

has one exact lifted numerator

    Pi = A*p + eta.

A material response sample ``r`` under signed maximum impulse numerator ``s*J``
then updates this lifted state without loss:

    Pi' = Pi + s*J*r.

Therefore an arbitrary response history satisfies

    Pi_n = Pi_0 + s*J*sum(r_t),

independent of how often the intermediate whole/detail projection is exposed.
This is the impulse analogue of retaining quotient detail elsewhere in Enterprise
Math.

In an inward-positive oriented coordinate, let ``Pi0>0`` and let ``I>=0`` be the
cumulative outward impulse numerator.  The represented whole momentum is:

* inward positive iff ``Pi0-I >= A``;
* zero iff ``-A < Pi0-I < A``;
* outward negative iff ``Pi0-I <= -A``.

Thus finite momentum resolution creates an exact zero-momentum stall band between
slowing and true reversal.  This band is distinct from a zero material force and
from a spatial interaction dead zone.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_coupling import project_material_impulse

INWARD = "INWARD"
STALL = "STALL"
OUTWARD = "OUTWARD"


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def lifted_momentum_numerator(momentum_quanta: int, detail_numerator: int, amplitude: int) -> int:
    """Return exact ``A*p+eta`` after validating the finite detail cell."""
    if isinstance(momentum_quanta, bool) or not isinstance(momentum_quanta, int):
        raise ValueError("momentum_quanta must be an integer")
    if isinstance(detail_numerator, bool) or not isinstance(detail_numerator, int):
        raise ValueError("detail_numerator must be an integer")
    _require_positive("amplitude", amplitude)
    if abs(detail_numerator) >= amplitude:
        raise ValueError("detail_numerator must lie strictly inside one amplitude cell")
    return amplitude * momentum_quanta + detail_numerator


def oriented_momentum_phase(lifted_inward_numerator: int, amplitude: int) -> str:
    """Classify a lifted numerator by its represented whole inward momentum sign."""
    if isinstance(lifted_inward_numerator, bool) or not isinstance(lifted_inward_numerator, int):
        raise ValueError("lifted_inward_numerator must be an integer")
    _require_positive("amplitude", amplitude)
    if lifted_inward_numerator >= amplitude:
        return INWARD
    if lifted_inward_numerator <= -amplitude:
        return OUTWARD
    return STALL


@dataclass(frozen=True)
class ImpulseAccumulationThresholds:
    initial_lifted_inward_numerator: int
    amplitude: int
    minimum_impulse_numerator_to_stop: int
    minimum_impulse_numerator_to_reverse: int
    stall_impulse_numerator_range: tuple[int, int]


def impulse_accumulation_thresholds(
    initial_lifted_inward_numerator: int,
    amplitude: int,
) -> ImpulseAccumulationThresholds:
    """Return exact cumulative outward-impulse thresholds for stop/reversal."""
    _require_positive("initial_lifted_inward_numerator", initial_lifted_inward_numerator)
    _require_positive("amplitude", amplitude)
    stop = max(0, initial_lifted_inward_numerator - amplitude + 1)
    reverse = initial_lifted_inward_numerator + amplitude
    return ImpulseAccumulationThresholds(
        initial_lifted_inward_numerator=initial_lifted_inward_numerator,
        amplitude=amplitude,
        minimum_impulse_numerator_to_stop=stop,
        minimum_impulse_numerator_to_reverse=reverse,
        stall_impulse_numerator_range=(stop, reverse - 1),
    )


def minimum_ticks_for_cumulative_impulse(threshold: int, impulse_numerator_per_tick: int) -> int | None:
    """Ceiling threshold/tick, or None when a positive threshold can never be reached."""
    _require_nonnegative("threshold", threshold)
    _require_nonnegative("impulse_numerator_per_tick", impulse_numerator_per_tick)
    if threshold == 0:
        return 0
    if impulse_numerator_per_tick == 0:
        return None
    return (threshold + impulse_numerator_per_tick - 1) // impulse_numerator_per_tick


@dataclass(frozen=True)
class RetainedImpulseHistoryCertificate:
    amplitude: int
    max_impulse_per_tick: int
    outward_sign: int
    initial_momentum_quanta: int
    initial_detail_numerator: int
    response_sum: int
    final_momentum_quanta: int
    final_detail_numerator: int
    initial_lifted_numerator: int
    final_lifted_numerator: int
    expected_final_lifted_numerator: int


def retained_impulse_history_certificate(
    initial_momentum_quanta: int,
    initial_detail_numerator: int,
    response_samples: tuple[int, ...] | list[int],
    amplitude: int,
    max_impulse_per_tick: int,
    outward_sign: int,
) -> RetainedImpulseHistoryCertificate:
    """Project a response word and certify exact lifted additivity."""
    _require_positive("amplitude", amplitude)
    _require_nonnegative("max_impulse_per_tick", max_impulse_per_tick)
    if outward_sign not in (-1, 1):
        raise ValueError("outward_sign must be -1 or +1")
    samples = tuple(response_samples)
    for sample in samples:
        _require_nonnegative("response_sample", sample)
        if sample > amplitude:
            raise ValueError("response sample must not exceed amplitude")
    initial_lifted = lifted_momentum_numerator(
        initial_momentum_quanta, initial_detail_numerator, amplitude
    )
    momentum = initial_momentum_quanta
    detail = initial_detail_numerator
    for sample in samples:
        report = project_material_impulse(
            sample,
            amplitude,
            max_impulse_per_tick,
            outward_sign,
            detail,
            True,
        )
        momentum += report.impulse_quanta
        detail = report.next_detail_numerator
    response_sum = sum(samples)
    final_lifted = lifted_momentum_numerator(momentum, detail, amplitude)
    expected = initial_lifted + outward_sign * max_impulse_per_tick * response_sum
    if final_lifted != expected:
        raise AssertionError("retained impulse history failed lifted-momentum identity")
    return RetainedImpulseHistoryCertificate(
        amplitude=amplitude,
        max_impulse_per_tick=max_impulse_per_tick,
        outward_sign=outward_sign,
        initial_momentum_quanta=initial_momentum_quanta,
        initial_detail_numerator=initial_detail_numerator,
        response_sum=response_sum,
        final_momentum_quanta=momentum,
        final_detail_numerator=detail,
        initial_lifted_numerator=initial_lifted,
        final_lifted_numerator=final_lifted,
        expected_final_lifted_numerator=expected,
    )
