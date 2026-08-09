"""Exact impulse thresholds separating momentum reversal from saved-position reversal.

Orient the 1D coordinate so that motion *toward* the wall is positive.  Let

    P > 0   incoming oriented momentum,
    m > 0   integer mass,
    R       oriented drift remainder with |R| < m,
    J >= 0  wall-opposing integer impulse.

After the impulse,

    P' = P-J,
    q(J) = trunc_toward_zero((R+P-J)/m).

Momentum and saved-cell motion therefore have distinct exact thresholds:

* momentum still toward wall iff ``J<P``;
* momentum stalls iff ``J=P``;
* momentum reverses iff ``J>P``;
* saved center moves toward wall iff ``J<=R+P-m``;
* saved center holds iff ``R+P-m < J < R+P+m``;
* saved center moves away iff ``J>=R+P+m``.

Thus the first momentum-reversing impulse is ``P+1`` while the first impulse
that moves the saved center away is ``P+R+m``.  Their threshold gap is

    R+m-1 in {0,...,2m-2}.

Equivalently there are exactly ``R+m-1`` integer impulse levels for which
momentum is already reversed but the saved center has not yet moved away.

If sub-cell detail is deliberately dropped on impulse, use ``R=0`` and the band
has exactly ``m-1`` impulse levels.  Retaining a positive remainder delays
saved-position reversal by ``R`` further impulse quanta relative to that policy;
a negative remainder advances it by ``|R|``.

This is a finite arithmetic effect of mass drift and retained positional phase,
not dissipative physics.
"""

from __future__ import annotations

from dataclasses import dataclass

MOMENTUM_TOWARD = "MOMENTUM_TOWARD"
MOMENTUM_STALLED = "MOMENTUM_STALLED"
MOMENTUM_REVERSED = "MOMENTUM_REVERSED"
CELL_TOWARD = "CELL_TOWARD"
CELL_HOLD = "CELL_HOLD"
CELL_AWAY = "CELL_AWAY"


def _toward_zero_quotient(value: int, divisor: int) -> int:
    if value >= 0:
        return value // divisor
    return -((-value) // divisor)


@dataclass(frozen=True)
class ImpulseReversalThresholds:
    oriented_momentum: int
    mass: int
    oriented_remainder: int
    first_momentum_reversal_impulse: int
    first_cell_hold_or_away_impulse: int
    last_cell_hold_impulse: int
    first_cell_away_impulse: int
    reversed_momentum_without_away_cell_count: int
    dropped_detail_first_cell_away_impulse: int
    retained_minus_dropped_away_threshold: int


def impulse_reversal_thresholds(
    oriented_momentum: int,
    mass: int,
    oriented_remainder: int,
) -> ImpulseReversalThresholds:
    """Return all exact finite impulse thresholds for one oriented pre-tick phase."""
    if (
        isinstance(oriented_momentum, bool)
        or not isinstance(oriented_momentum, int)
        or oriented_momentum <= 0
    ):
        raise ValueError("oriented_momentum must be a positive integer")
    if isinstance(mass, bool) or not isinstance(mass, int) or mass <= 0:
        raise ValueError("mass must be a positive integer")
    if (
        isinstance(oriented_remainder, bool)
        or not isinstance(oriented_remainder, int)
        or abs(oriented_remainder) >= mass
    ):
        raise ValueError("oriented_remainder must satisfy |R| < mass")

    first_momentum_reversal = oriented_momentum + 1
    first_not_toward_cell = oriented_remainder + oriented_momentum - mass + 1
    # J is constrained to be nonnegative in the world; the arithmetic threshold
    # may be negative when the free saved-cell drift is already a hold.
    first_not_toward_cell = max(0, first_not_toward_cell)
    first_away = oriented_momentum + oriented_remainder + mass
    last_hold = first_away - 1
    band = first_away - first_momentum_reversal
    if not 0 <= band <= 2 * mass - 2:
        raise AssertionError("momentum/cell reversal band escaped exact finite bound")
    dropped_first_away = oriented_momentum + mass
    return ImpulseReversalThresholds(
        oriented_momentum=oriented_momentum,
        mass=mass,
        oriented_remainder=oriented_remainder,
        first_momentum_reversal_impulse=first_momentum_reversal,
        first_cell_hold_or_away_impulse=first_not_toward_cell,
        last_cell_hold_impulse=last_hold,
        first_cell_away_impulse=first_away,
        reversed_momentum_without_away_cell_count=band,
        dropped_detail_first_cell_away_impulse=dropped_first_away,
        retained_minus_dropped_away_threshold=oriented_remainder,
    )


def classify_impulse_motion(
    oriented_momentum: int,
    mass: int,
    oriented_remainder: int,
    impulse: int,
) -> tuple[str, str, int]:
    """Return (momentum class, saved-cell class, oriented cell displacement)."""
    thresholds = impulse_reversal_thresholds(
        oriented_momentum,
        mass,
        oriented_remainder,
    )
    if isinstance(impulse, bool) or not isinstance(impulse, int) or impulse < 0:
        raise ValueError("impulse must be a non-negative integer")
    post_momentum = oriented_momentum - impulse
    if post_momentum > 0:
        momentum_class = MOMENTUM_TOWARD
    elif post_momentum == 0:
        momentum_class = MOMENTUM_STALLED
    else:
        momentum_class = MOMENTUM_REVERSED

    displacement = _toward_zero_quotient(
        oriented_remainder + post_momentum,
        mass,
    )
    if displacement > 0:
        cell_class = CELL_TOWARD
    elif displacement == 0:
        cell_class = CELL_HOLD
    else:
        cell_class = CELL_AWAY

    # Audit threshold formulas against direct classification.
    if (impulse >= thresholds.first_cell_away_impulse) != (cell_class == CELL_AWAY):
        raise AssertionError("cell-away threshold disagrees with direct toward-zero drift")
    return momentum_class, cell_class, displacement
