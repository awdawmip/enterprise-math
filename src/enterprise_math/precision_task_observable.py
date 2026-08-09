"""Task-relative precision for correlated diagonal vector actuation in E002.

This module isolates a deliberately small but exact counterpressure to the
Stage-4 full-vector product law.  Consider one rectangular precision cell with
equal odd width ``w`` on every axis, the deterministic diagonal unit action
``(1,...,1)``, and a finite horizon ``h < w``.  Each fine coordinate has one
future crossing bucket: the first sample at which its coarse quotient leaves the
current cell, or one terminal bucket meaning 'not within the declared horizon'.

The full vector quotient remembers the ordered tuple of crossing buckets and
therefore needs ``(h+1)^n`` classes.  Weaker future languages identify different
tuples:

* a two-coordinate linear observable ``alpha*q1 + beta*q2`` has a complete
  finite classification by coefficient symmetry;
* the symmetric coordinate sum depends only on the multiset of crossing
  buckets and needs ``binomial(h+n,n)`` classes;
* Boolean ANY/ALL crossing questions depend only on the earliest/latest bucket
  and need only ``h+1`` classes.

The purpose is not to propose these observables as universal physics.  It is to
make the P023 task-language principle numerically explicit inside one physical
E002 trajectory.
"""

from __future__ import annotations

from math import comb
from typing import Sequence


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_width_horizon(width: int, horizon: int) -> None:
    _require_int("width", width)
    _require_int("horizon", horizon)
    if width <= 0 or width % 2 == 0:
        raise ValueError("width must be a positive odd integer")
    if horizon < 0 or horizon >= width:
        raise ValueError("horizon must satisfy 0 <= horizon < width")


def crossing_bucket(detail: int, width: int, horizon: int) -> int:
    """First unit-diagonal crossing sample, or ``horizon+1`` if not observed.

    A detail ``r`` in ``0..w-1`` under repeated +1 translation has quotient
    carry at the first positive sample ``w-r``.  All crossings after the
    declared horizon are intentionally identified with the terminal bucket
    ``h+1``.
    """
    _require_width_horizon(width, horizon)
    _require_int("detail", detail)
    if detail < 0 or detail >= width:
        raise ValueError("detail must lie in 0..width-1")
    first = width - detail
    return first if first <= horizon else horizon + 1


def crossing_step_sequence(bucket: int, horizon: int) -> tuple[int, ...]:
    """Binary coarse-quotient sequence for one crossing bucket."""
    _require_int("bucket", bucket)
    _require_int("horizon", horizon)
    if horizon < 0 or bucket < 1 or bucket > horizon + 1:
        raise ValueError("bucket must lie in 1..horizon+1")
    return tuple(int(bucket <= sample) for sample in range(horizon + 1))


def full_vector_class_count(dimension: int, horizon: int) -> int:
    """Ordered crossing-bucket tuples for the complete vector quotient."""
    _require_int("dimension", dimension)
    _require_int("horizon", horizon)
    if dimension <= 0 or horizon < 0:
        raise ValueError("dimension must be positive and horizon nonnegative")
    return (horizon + 1) ** dimension


def linear_two_coordinate_class_count(alpha: int, beta: int, horizon: int) -> int:
    """Exact class count for ``alpha*q1 + beta*q2`` under diagonal unit action.

    The ``h+1`` possible crossing buckets form ordered pairs.  Generic nonzero
    unequal/nonopposite coefficients label the two coordinates and preserve the
    whole ordered pair.  Equal coefficients erase coordinate order; opposite
    coefficients collapse every diagonal pair to the zero sequence.  A zero
    coefficient discards one coordinate completely.
    """
    _require_int("alpha", alpha)
    _require_int("beta", beta)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    buckets = horizon + 1
    if alpha == 0 and beta == 0:
        return 1
    if alpha == 0 or beta == 0:
        return buckets
    if alpha == beta:
        return buckets * (buckets + 1) // 2
    if alpha == -beta:
        return buckets * (buckets - 1) + 1
    return buckets * buckets


def linear_two_coordinate_signature(
    detail_left: int,
    detail_right: int,
    width: int,
    horizon: int,
    alpha: int,
    beta: int,
) -> tuple[int, ...]:
    """Direct sampled scalar-linear future signature used for falsification."""
    _require_width_horizon(width, horizon)
    for name, value in (("left detail", detail_left), ("right detail", detail_right)):
        _require_int(name, value)
        if value < 0 or value >= width:
            raise ValueError(f"{name} must lie in 0..width-1")
    _require_int("alpha", alpha)
    _require_int("beta", beta)
    return tuple(
        alpha * ((detail_left + sample) // width)
        + beta * ((detail_right + sample) // width)
        for sample in range(horizon + 1)
    )


def symmetric_sum_class_count(dimension: int, horizon: int) -> int:
    """Exact classes for ``sum_i q_i``: multisets of crossing buckets."""
    _require_int("dimension", dimension)
    _require_int("horizon", horizon)
    if dimension <= 0 or horizon < 0:
        raise ValueError("dimension must be positive and horizon nonnegative")
    return comb(horizon + dimension, dimension)


def symmetric_sum_signature(
    details: Sequence[int],
    width: int,
    horizon: int,
) -> tuple[int, ...]:
    """Direct future signature of the symmetric coordinate sum."""
    _require_width_horizon(width, horizon)
    values = tuple(details)
    if not values:
        raise ValueError("at least one coordinate detail is required")
    for detail in values:
        _require_int("detail", detail)
        if detail < 0 or detail >= width:
            raise ValueError("detail must lie in 0..width-1")
    return tuple(
        sum((detail + sample) // width for detail in values)
        for sample in range(horizon + 1)
    )


def any_crossed_signature(
    details: Sequence[int],
    width: int,
    horizon: int,
) -> tuple[int, ...]:
    """Boolean future language: whether at least one coordinate has crossed."""
    _require_width_horizon(width, horizon)
    buckets = tuple(crossing_bucket(detail, width, horizon) for detail in details)
    if not buckets:
        raise ValueError("at least one coordinate detail is required")
    earliest = min(buckets)
    return tuple(int(earliest <= sample) for sample in range(horizon + 1))


def all_crossed_signature(
    details: Sequence[int],
    width: int,
    horizon: int,
) -> tuple[int, ...]:
    """Boolean future language: whether every coordinate has crossed."""
    _require_width_horizon(width, horizon)
    buckets = tuple(crossing_bucket(detail, width, horizon) for detail in details)
    if not buckets:
        raise ValueError("at least one coordinate detail is required")
    latest = max(buckets)
    return tuple(int(latest <= sample) for sample in range(horizon + 1))


def any_or_all_class_count(horizon: int) -> int:
    """Earliest/latest crossing bucket has exactly ``h+1`` possibilities."""
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    return horizon + 1


def two_coordinate_equality_class_count(horizon: int) -> int:
    """Exact classes for Boolean ``q1 == q2`` under diagonal unit action."""
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    buckets = horizon + 1
    return 1 + buckets * (buckets - 1) // 2


def two_coordinate_equality_signature(
    detail_left: int,
    detail_right: int,
    width: int,
    horizon: int,
) -> tuple[int, ...]:
    """Direct Boolean equality future signature."""
    _require_width_horizon(width, horizon)
    for detail in (detail_left, detail_right):
        _require_int("detail", detail)
        if detail < 0 or detail >= width:
            raise ValueError("detail must lie in 0..width-1")
    return tuple(
        int((detail_left + sample) // width == (detail_right + sample) // width)
        for sample in range(horizon + 1)
    )
