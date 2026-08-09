"""Exact integer midpoint identities for finite impulse time integration.

This module isolates an integrator-level effect from material hysteresis and from
projection loss.  Let ``Pi`` be any signed lifted momentum numerator and let a
constant signed momentum-rate numerator ``H`` act over integer duration quanta.
For an explicit duration partition ``dt_i``:

    Pi_i = Pi_{i-1} + H*dt_i.

Use doubled displacement numerators so no half-integer is introduced:

    midpoint = sum_i dt_i*(Pi_{i-1}+Pi_i),
    postkick = 2*sum_i dt_i*Pi_i,
    prekick  = 2*sum_i dt_i*Pi_{i-1}.

For total duration ``T=sum_i dt_i`` the midpoint sum telescopes exactly:

    midpoint = T*(Pi_0+Pi_final),

independent of how ``T`` was partitioned.  The one-sided schedules have exact
quadratic defects

    postkick-midpoint = H*sum_i dt_i^2,
    midpoint-prekick  = H*sum_i dt_i^2.

Thus constant-rate time refinement is exactly neutral at the lifted numerator
level under midpoint pairing, while pre/post kick schedules retain a cadence
defect even before any integer spatial projection is applied.

The same pairing is selected by the exact square identity for one impulse
``j=Pi_1-Pi_0``:

    Pi_1^2-Pi_0^2 = j*(Pi_0+Pi_1).

So midpoint impulse-work pairing matches the lifted kinetic-square change exactly;
post-pairing differs by ``j^2`` and pre-pairing by ``-j^2``.

Trapezoidal/midpoint integration is established numerical analysis.  E001 uses
these identities only as an integer accounting/comparator layer; no novelty claim
is made for the integration rule itself.
"""

from __future__ import annotations

from dataclasses import dataclass


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _duration_schedule(durations: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    schedule = tuple(durations)
    if not schedule:
        raise ValueError("duration schedule must be nonempty")
    for duration in schedule:
        _require_integer("duration", duration)
        if duration < 0:
            raise ValueError("duration quanta must be non-negative")
    if sum(schedule) <= 0:
        raise ValueError("total duration must be positive")
    return schedule


@dataclass(frozen=True)
class ConstantRateIntegratorReport:
    initial_lifted_momentum: int
    momentum_rate_per_time_quantum: int
    durations: tuple[int, ...]
    total_duration: int
    final_lifted_momentum: int
    midpoint_doubled_displacement_numerator: int
    coarse_midpoint_doubled_displacement_numerator: int
    postkick_doubled_displacement_numerator: int
    prekick_doubled_displacement_numerator: int
    squared_duration_sum: int
    postkick_midpoint_defect: int
    midpoint_prekick_defect: int

    @property
    def midpoint_partition_exact(self) -> bool:
        return (
            self.midpoint_doubled_displacement_numerator
            == self.coarse_midpoint_doubled_displacement_numerator
        )


def constant_rate_integrator_report(
    initial_lifted_momentum: int,
    momentum_rate_per_time_quantum: int,
    durations: tuple[int, ...] | list[int],
) -> ConstantRateIntegratorReport:
    """Return exact pre/mid/post displacement numerators for one time partition."""
    _require_integer("initial_lifted_momentum", initial_lifted_momentum)
    _require_integer("momentum_rate_per_time_quantum", momentum_rate_per_time_quantum)
    schedule = _duration_schedule(durations)

    current = initial_lifted_momentum
    midpoint = 0
    postkick = 0
    prekick = 0
    for duration in schedule:
        before = current
        after = before + momentum_rate_per_time_quantum * duration
        midpoint += duration * (before + after)
        postkick += 2 * duration * after
        prekick += 2 * duration * before
        current = after

    total = sum(schedule)
    coarse_midpoint = total * (initial_lifted_momentum + current)
    square_sum = sum(duration * duration for duration in schedule)
    expected_defect = momentum_rate_per_time_quantum * square_sum
    if midpoint != coarse_midpoint:
        raise AssertionError("midpoint constant-rate partition identity failed")
    if postkick - midpoint != expected_defect:
        raise AssertionError("postkick midpoint defect identity failed")
    if midpoint - prekick != expected_defect:
        raise AssertionError("midpoint prekick defect identity failed")

    return ConstantRateIntegratorReport(
        initial_lifted_momentum=initial_lifted_momentum,
        momentum_rate_per_time_quantum=momentum_rate_per_time_quantum,
        durations=schedule,
        total_duration=total,
        final_lifted_momentum=current,
        midpoint_doubled_displacement_numerator=midpoint,
        coarse_midpoint_doubled_displacement_numerator=coarse_midpoint,
        postkick_doubled_displacement_numerator=postkick,
        prekick_doubled_displacement_numerator=prekick,
        squared_duration_sum=square_sum,
        postkick_midpoint_defect=postkick - midpoint,
        midpoint_prekick_defect=midpoint - prekick,
    )


@dataclass(frozen=True)
class ImpulseWorkPairingReport:
    before_lifted_momentum: int
    impulse_numerator: int
    after_lifted_momentum: int
    kinetic_square_change: int
    midpoint_work_numerator: int
    post_work_numerator: int
    pre_work_numerator: int
    post_defect: int
    pre_defect: int


def impulse_work_pairing_report(
    before_lifted_momentum: int,
    impulse_numerator: int,
) -> ImpulseWorkPairingReport:
    """Expose the exact pre/mid/post work pairing defects for one impulse."""
    _require_integer("before_lifted_momentum", before_lifted_momentum)
    _require_integer("impulse_numerator", impulse_numerator)
    after = before_lifted_momentum + impulse_numerator
    kinetic_change = after * after - before_lifted_momentum * before_lifted_momentum
    midpoint = impulse_numerator * (before_lifted_momentum + after)
    post = 2 * impulse_numerator * after
    pre = 2 * impulse_numerator * before_lifted_momentum
    if midpoint != kinetic_change:
        raise AssertionError("midpoint work pairing failed square-difference identity")
    if post - kinetic_change != impulse_numerator * impulse_numerator:
        raise AssertionError("post work defect is not +j^2")
    if pre - kinetic_change != -(impulse_numerator * impulse_numerator):
        raise AssertionError("pre work defect is not -j^2")
    return ImpulseWorkPairingReport(
        before_lifted_momentum=before_lifted_momentum,
        impulse_numerator=impulse_numerator,
        after_lifted_momentum=after,
        kinetic_square_change=kinetic_change,
        midpoint_work_numerator=midpoint,
        post_work_numerator=post,
        pre_work_numerator=pre,
        post_defect=post - kinetic_change,
        pre_defect=pre - kinetic_change,
    )
