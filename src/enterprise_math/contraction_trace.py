"""Finite witness and trace kernels for P019 dimension contraction.

This module separates three layers:

1. balanced minimum values, which are associative under min-plus block merge;
2. full two-block fiber witness relations, which are integer intervals;
3. directed boundary representatives, whose repeated selection can depend on the
   ordered contraction history.

No floating point values or true division are used.
"""

from __future__ import annotations

from math import comb, factorial

from .dimension_contraction import balanced_power_energy


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def balanced_minimizer_count(block_size: int, power: int, total: int) -> int:
    """Number of labeled slot-level minimizers for Psi_(m,s)(total).

    For power > 1 the minimizer is balanced: if |total| = m*q+r, exactly r
    labeled slots carry magnitude q+1 and the remaining slots carry q.  For
    power = 1 every sign-consistent weak composition is minimizing.
    """
    _require_positive("block_size", block_size)
    _require_positive("power", power)
    _require_integer("total", total)
    magnitude = abs(total)
    if power == 1:
        if magnitude == 0:
            return 1
        return comb(magnitude + block_size - 1, block_size - 1)
    _, remainder = divmod(magnitude, block_size)
    return comb(block_size, remainder)


def two_block_argmin_profile(
    left_size: int, right_size: int, power: int, total: int
) -> tuple[tuple[int, int], ...]:
    """Return (left_total, labeled multiplicity) for every min-plus minimizer.

    For power > 1 the profile is the hypergeometric remainder allocation
    profile. For power = 1 it is the weak-composition profile.
    """
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_positive("power", power)
    _require_integer("total", total)

    if power == 1:
        if total >= 0:
            values = range(0, total + 1)
        else:
            values = range(total, 1)
        result = []
        for left_total in values:
            right_total = total - left_total
            left_count = balanced_minimizer_count(left_size, 1, left_total)
            right_count = balanced_minimizer_count(right_size, 1, right_total)
            result.append((left_total, left_count * right_count))
        return tuple(result)

    total_size = left_size + right_size
    magnitude = abs(total)
    q, remainder = divmod(magnitude, total_size)
    low = max(0, remainder - right_size)
    high = min(left_size, remainder)
    sign = 1 if total >= 0 else -1
    result = []
    for left_remainder in range(low, high + 1):
        left_magnitude = left_size * q + left_remainder
        right_remainder = remainder - left_remainder
        multiplicity = comb(left_size, left_remainder) * comb(
            right_size, right_remainder
        )
        result.append((sign * left_magnitude, multiplicity))
    return tuple(result)


def fiber_excess_energy(
    left_size: int, right_size: int, power: int, total: int, left_total: int
) -> int:
    """Energy above the merged fiber minimum for one two-block split."""
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_positive("power", power)
    _require_integer("total", total)
    _require_integer("left_total", left_total)
    split = balanced_power_energy(left_size, power, left_total) + balanced_power_energy(
        right_size, power, total - left_total
    )
    merged = balanced_power_energy(left_size + right_size, power, total)
    return split - merged


def fiber_witness_interval(
    left_size: int, right_size: int, power: int, total: int, slack: int
) -> tuple[int, int]:
    """Compressed full witness relation for one contraction fiber.

    Returns the integer interval [L,U] of left totals whose split energy is at
    most merged_minimum + slack. Discrete convexity guarantees that the full
    feasible set is exactly this interval.
    """
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_positive("power", power)
    _require_integer("total", total)
    _require_natural("slack", slack)

    profile = two_block_argmin_profile(left_size, right_size, power, total)
    left = min(value for value, _ in profile)
    right = max(value for value, _ in profile)

    while fiber_excess_energy(left_size, right_size, power, total, left - 1) <= slack:
        left -= 1
    while fiber_excess_energy(left_size, right_size, power, total, right + 1) <= slack:
        right += 1
    return left, right


def fiber_witness_multiplicity(
    left_size: int, right_size: int, power: int, total: int, slack: int
) -> int:
    """Number of feasible block-total witnesses in the compressed fiber relation."""
    left, right = fiber_witness_interval(left_size, right_size, power, total, slack)
    return right - left + 1


def directed_boundary_split(
    receiver_size: int, donor_size: int, power: int, total: int, slack: int
) -> tuple[int, int]:
    """Unique right-end boundary representative for donor -> receiver transfer."""
    _, receiver_total = fiber_witness_interval(
        receiver_size, donor_size, power, total, slack
    )
    return receiver_total, total - receiver_total


def unoriented_partition_chain_count(slot_count: int) -> int:
    """Number of maximal chains from singletons to one block in Pi_N."""
    _require_positive("slot_count", slot_count)
    if slot_count == 1:
        return 1
    return factorial(slot_count) * factorial(slot_count - 1) // (2 ** (slot_count - 1))


def oriented_contraction_history_count(slot_count: int) -> int:
    """Number of complete merge histories when each merge has receiver/donor order."""
    _require_positive("slot_count", slot_count)
    return factorial(slot_count) * factorial(slot_count - 1)
