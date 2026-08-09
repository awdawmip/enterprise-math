"""Higher collision moments for selected-layer Barlow observations.

For a length-ell ±1 segment, the r-th power sum of imbalance fiber sizes is

    F_r(ell) = sum_j C(ell,j)^r.

Selected-layer observations factor over independent segments. Therefore the
number of ordered r-tuples of microscopic words sharing one observation is

    M_r = 2^(r*tail) * product_j F_r(ell_j).

The P011 collision statistic

    J_k = sum_y C(|fiber_y|, k)

is recovered from the power moments by signed Stirling numbers of the first
kind because ``C(x,k)=(x)_k/k!``.
"""

from __future__ import annotations

from math import comb, factorial

from .p022_barlow_precision_fibers import selected_segment_lengths


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")


def generalized_binomial_power_sum(length: int, order: int) -> int:
    """Return ``sum_j C(length,j)^order``."""
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be a non-negative integer")
    _require_order(order)
    return sum(comb(length, count) ** order for count in range(length + 1))


def ordered_equal_observation_tuple_count(
    length: int, selected_layers: tuple[int, ...], order: int
) -> int:
    """Number of ordered r-tuples sharing the selected-layer observation."""
    _require_order(order)
    segments, tail = selected_segment_lengths(length, selected_layers)
    result = 2 ** (order * tail)
    for segment in segments:
        result *= generalized_binomial_power_sum(segment, order)
    return result


def signed_stirling_first_kind(order: int) -> tuple[int, ...]:
    """Coefficients s(order,j) in ``(x)_order=sum_j s(order,j)x^j``."""
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be a non-negative integer")
    coefficients = [1]
    for n in range(order):
        updated = [0] * (len(coefficients) + 1)
        for degree, value in enumerate(coefficients):
            updated[degree] -= n * value
            updated[degree + 1] += value
        coefficients = updated
    return tuple(coefficients)


def collision_count_from_power_moments(power_moments: tuple[int, ...], order: int) -> int:
    """Recover P011 ``J_order`` from ``M_r=sum fiber^r`` for r<=order.

    ``power_moments[r]`` must equal M_r. Index zero is ignored for positive
    collision order.
    """
    _require_order(order)
    if not isinstance(power_moments, tuple) or len(power_moments) <= order:
        raise ValueError("power_moments must contain indices through order")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in power_moments[1 : order + 1]
    ):
        raise ValueError("power moments must be non-negative integers")
    stirling = signed_stirling_first_kind(order)
    numerator = sum(
        stirling[power] * power_moments[power]
        for power in range(1, order + 1)
    )
    denominator = factorial(order)
    if numerator < 0 or numerator % denominator:
        raise AssertionError("fiber falling-factorial sum must be divisible by order factorial")
    return numerator // denominator


def selected_layer_collision_count(
    length: int, selected_layers: tuple[int, ...], order: int
) -> int:
    """Exact P011 order-k collision count of the selected-layer quotient."""
    _require_order(order)
    moments = [0]
    for power in range(1, order + 1):
        moments.append(
            ordered_equal_observation_tuple_count(
                length, selected_layers, power
            )
        )
    return collision_count_from_power_moments(tuple(moments), order)


def final_imbalance_power_moment(length: int, order: int) -> int:
    """Final-layer specialization: one segment and no hidden tail."""
    selected_layers = (length,) if length else ()
    return ordered_equal_observation_tuple_count(length, selected_layers, order)
