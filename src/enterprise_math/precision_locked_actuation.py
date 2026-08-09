"""Centered precision quotients and precision-locked actuation for E002.

This module extends the E002 threshold-control pressure test without changing the
project's foundational core.  The target-centered deadband of half-width ``d``
has odd cardinality ``w = 2*d - 1``.  Treating ``w`` as the actual cell width
turns the three-way threshold observation into the sign of an exact Euclidean
quotient.

The main engineering question is then arithmetic: when does a physical integer
translation preserve those quotient fibers?  The answer is exact divisibility.
If an actuation increment is a multiple of ``w``, the quotient evolves without
reading hidden within-cell detail.  Otherwise a bounded Euclidean carry is
unavoidable.  For a finite action family, ``gcd`` identifies the coarsest
centered refinement closed under every action.

The general quotient/future-sufficiency theorem belongs to P023.  This file is
an E002 arithmetic specialization and executable engineering probe.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm
from typing import Iterable, Sequence

from .precision_hysteresis import ThresholdObservation


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def precision_cell_width(precision: int) -> int:
    """Return the target-centered E002 cell width ``w = 2*d - 1``."""
    _require_positive("precision", precision)
    return 2 * precision - 1


def precision_from_cell_width(width: int) -> int:
    """Convert a positive odd centered-cell width back to E002 half-width ``d``."""
    _require_positive("width", width)
    if width % 2 == 0:
        raise ValueError("centered cell width must be odd")
    return (width + 1) // 2


@dataclass(frozen=True)
class CenteredPrecisionState:
    """Exact target-centered Euclidean precision chart."""

    quotient: int
    detail: int
    width: int

    def reconstruct_error(self) -> int:
        """Recover the represented integer error exactly."""
        return self.width * self.quotient + self.detail - (self.width - 1) // 2


def centered_precision_state(error: int, precision: int) -> CenteredPrecisionState:
    """Write ``e = w*q + r - (w-1)/2`` with ``0 <= r < w``."""
    _require_int("error", error)
    width = precision_cell_width(precision)
    shifted = error + (width - 1) // 2
    quotient, detail = divmod(shifted, width)
    return CenteredPrecisionState(quotient, detail, width)


def threshold_observation_from_quotient(quotient: int) -> ThresholdObservation:
    """Three-way E002 threshold observation as the sign of the centered quotient."""
    _require_int("quotient", quotient)
    if quotient < 0:
        return ThresholdObservation.BELOW
    if quotient > 0:
        return ThresholdObservation.ABOVE
    return ThresholdObservation.COLLAPSED


@dataclass(frozen=True)
class TranslationCertificate:
    """Exact quotient/detail transport under one integer actuation increment."""

    quotient_before: int
    detail_before: int
    quotient_bulk: int
    increment_detail: int
    carry: int
    quotient_after: int
    detail_after: int
    width: int


def translation_certificate(
    error: int,
    precision: int,
    increment: int,
) -> TranslationCertificate:
    """Return exact Euclidean transport data for ``error -> error + increment``.

    If ``increment = k*w + s`` with ``0 <= s < w``, then

    ``q' = q + k + 1[r+s >= w]`` and ``r' = (r+s) mod w``.
    """
    _require_int("increment", increment)
    state = centered_precision_state(error, precision)
    quotient_bulk, increment_detail = divmod(increment, state.width)
    carry = int(state.detail + increment_detail >= state.width)
    quotient_after = state.quotient + quotient_bulk + carry
    detail_after = (state.detail + increment_detail) % state.width
    direct = centered_precision_state(error + increment, precision)
    if (quotient_after, detail_after) != (direct.quotient, direct.detail):
        raise AssertionError("translation certificate failed exact reconstruction")
    return TranslationCertificate(
        quotient_before=state.quotient,
        detail_before=state.detail,
        quotient_bulk=quotient_bulk,
        increment_detail=increment_detail,
        carry=carry,
        quotient_after=quotient_after,
        detail_after=detail_after,
        width=state.width,
    )


def translation_descends(precision: int, increment: int) -> bool:
    """Whether translation by ``increment`` is deterministic on centered quotient cells."""
    _require_int("increment", increment)
    width = precision_cell_width(precision)
    return increment % width == 0


def translation_carry_bit(error: int, precision: int, increment: int) -> int:
    """Canonical one-step repair bit when a translation is not fiber-constant."""
    return translation_certificate(error, precision, increment).carry


def _normalized_actions(increments: Iterable[int]) -> tuple[int, ...]:
    actions = tuple(increments)
    if not actions:
        raise ValueError("at least one actuation increment is required")
    for increment in actions:
        _require_int("increment", increment)
    return actions


def stable_action_cell_width(precision: int, increments: Iterable[int]) -> int:
    """Coarsest centered refinement width closed under every supplied translation.

    For starting width ``w`` and action family ``A``, this is
    ``g = gcd(w, |a| for a in A)``.  Because ``w`` is odd, ``g`` is positive
    and odd even when every action is zero.
    """
    actions = _normalized_actions(increments)
    width = precision_cell_width(precision)
    common = width
    for increment in actions:
        common = gcd(common, abs(increment))
    return common


def stable_action_precision(precision: int, increments: Iterable[int]) -> int:
    """E002 half-width corresponding to :func:`stable_action_cell_width`."""
    return precision_from_cell_width(stable_action_cell_width(precision, increments))


def stable_action_state(
    error: int,
    precision: int,
    increments: Iterable[int],
) -> CenteredPrecisionState:
    """Return the coarsest centered refinement that supports the full action family."""
    refined = stable_action_precision(precision, increments)
    return centered_precision_state(error, refined)


def exact_action_quotient_step(
    quotient: int,
    cell_width: int,
    increment: int,
) -> int:
    """Apply a translation directly to a compatible centered quotient."""
    _require_int("quotient", quotient)
    _require_positive("cell_width", cell_width)
    if cell_width % 2 == 0:
        raise ValueError("centered cell width must be odd")
    _require_int("increment", increment)
    if increment % cell_width != 0:
        raise ValueError("increment is not compatible with this centered quotient")
    return quotient + increment // cell_width


def _positive_divisors(value: int) -> tuple[int, ...]:
    _require_positive("value", value)
    small: list[int] = []
    large: list[int] = []
    candidate = 1
    while candidate * candidate <= value:
        if value % candidate == 0:
            small.append(candidate)
            paired = value // candidate
            if paired != candidate:
                large.append(paired)
        candidate += 1
    return tuple(small + list(reversed(large)))


def action_family_grain(increments: Iterable[int]) -> int:
    """Return ``gcd(|a|)`` for a nontrivial physical action family.

    An all-zero family has no finite maximum compatible cell width, so this
    helper rejects that degenerate case rather than inventing a bound.
    """
    actions = _normalized_actions(increments)
    common = 0
    for increment in actions:
        common = gcd(common, abs(increment))
    if common == 0:
        raise ValueError("all-zero action family has unbounded compatible precision widths")
    return common


def admissible_precision_widths(increments: Iterable[int]) -> tuple[int, ...]:
    """All target-centered widths exactly preserved by every action.

    E002 centered widths are odd, so these are exactly the odd divisors of the
    action-family grain.
    """
    grain = action_family_grain(increments)
    return tuple(divisor for divisor in _positive_divisors(grain) if divisor % 2 == 1)


def admissible_precisions(increments: Iterable[int]) -> tuple[int, ...]:
    """All E002 half-widths whose centered quotients are exact for every action."""
    return tuple(precision_from_cell_width(width) for width in admissible_precision_widths(increments))


def shared_exact_action_unit(precisions: Iterable[int]) -> int:
    """Smallest positive actuation magnitude compatible with every supplied precision."""
    values = tuple(precisions)
    if not values:
        raise ValueError("at least one precision is required")
    unit = 1
    for precision in values:
        unit = lcm(unit, precision_cell_width(precision))
    return unit


def centered_coarse_projection(
    fine_quotient: int,
    fine_precision: int,
    coarse_precision: int,
) -> int:
    """Project nested centered quotient labels along odd-width divisibility.

    If fine width ``w`` divides coarse width ``W=m*w``, then ``m`` is odd and

    ``Q_W(e) = floor((Q_w(e) + (m-1)/2) / m)``.
    """
    _require_int("fine_quotient", fine_quotient)
    fine_width = precision_cell_width(fine_precision)
    coarse_width = precision_cell_width(coarse_precision)
    if coarse_width % fine_width != 0:
        raise ValueError("fine centered-cell width must divide coarse width")
    ratio = coarse_width // fine_width
    if ratio % 2 == 0:
        raise AssertionError("ratio of positive odd centered widths must be odd")
    return (fine_quotient + (ratio - 1) // 2) // ratio


def odd_power_precision_ladder(base: int, levels: int) -> tuple[int, ...]:
    """Return a nested centered-precision ladder with widths ``1,b,b^2,...``."""
    _require_positive("base", base)
    _require_positive("levels", levels)
    if base % 2 == 0:
        raise ValueError("base must be odd")
    widths = [base**level for level in range(levels)]
    return tuple(precision_from_cell_width(width) for width in widths)


@dataclass(frozen=True)
class DelayedActuationSample:
    """One sample of an exact delayed precision-locked plant trajectory."""

    error: int
    quotient: int
    detail: int
    applied_increment: int
    queue: tuple[int, ...]


def delayed_precision_locked_trace(
    initial_error: int,
    precision: int,
    initial_queue: Sequence[int],
    issued_increments: Sequence[int],
) -> tuple[DelayedActuationSample, ...]:
    """Run a delayed translation plant and audit exact quotient closure.

    ``initial_queue`` is the finite delay line.  At each sample its first action
    is applied, then the next issued action is appended.  Every queued/issued
    action must be a multiple of the centered cell width.  The returned samples
    store the pre-update physical state and the action applied at that sample,
    followed by one terminal sample whose ``applied_increment`` is zero.
    """
    _require_int("initial_error", initial_error)
    width = precision_cell_width(precision)
    queue = tuple(initial_queue)
    if not queue:
        raise ValueError("delay queue must be nonempty")
    for increment in (*queue, *issued_increments):
        _require_int("increment", increment)
        if increment % width != 0:
            raise ValueError("all delayed actions must be multiples of the precision cell width")

    error = initial_error
    samples: list[DelayedActuationSample] = []
    pending = list(queue)
    for issued in issued_increments:
        state = centered_precision_state(error, precision)
        applied = pending.pop(0)
        samples.append(
            DelayedActuationSample(
                error=error,
                quotient=state.quotient,
                detail=state.detail,
                applied_increment=applied,
                queue=tuple(pending + [issued]),
            )
        )
        error += applied
        pending.append(issued)

    state = centered_precision_state(error, precision)
    samples.append(
        DelayedActuationSample(
            error=error,
            quotient=state.quotient,
            detail=state.detail,
            applied_increment=0,
            queue=tuple(pending),
        )
    )
    return tuple(samples)
