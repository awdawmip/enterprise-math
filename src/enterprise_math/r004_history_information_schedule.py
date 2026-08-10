"""History-support resource schedules in canonical integer-information levels.

Enterprise Math already uses the integer information level

    L_B(m) = min { ell in N_0 : m <= B^ell }.

For a nondecreasing visible-history support profile R_0,...,R_H, define the
required level lambda_t=L_B(R_t).  If initial/runtime support budgets are powers
B^e_0,...,B^e_H, causal transcript capacity is sufficient at every prefix iff

    sum_{j=0}^t e_j >= lambda_t.

The minimum final exponent is lambda_H.  The just-in-time schedule is the
successive increase of lambda.  All other minimum-total schedules move some of
that information capacity earlier in time.  A dynamic program counts the
minimum schedules above an arbitrary integer demand boundary; the full
B-ary profile lambda_t=t specializes to the Catalan frontier.

This is a derived resource layer on the declared history observation language,
not a primitive entropy or physical law.
"""

from __future__ import annotations

from collections.abc import Sequence


def _base(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        raise ValueError("information base must be an integer at least two")
    return value


def _support_profile(values: Sequence[int]) -> tuple[int, ...]:
    row = tuple(values)
    if not row:
        raise ValueError("history support profile must be nonempty")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in row
    ):
        raise ValueError("history support counts must be positive integers")
    if any(left > right for left, right in zip(row[:-1], row[1:], strict=True)):
        raise ValueError("history prefix support counts must be nondecreasing")
    return row


def integer_information_level(base: int, mass: int) -> int:
    """Exact L_B(m)=min{ell:m<=B^ell}, using integer multiplication only."""
    B = _base(base)
    if isinstance(mass, bool) or not isinstance(mass, int) or mass <= 0:
        raise ValueError("mass must be a positive integer")
    level = 0
    capacity = 1
    while capacity < mass:
        capacity *= B
        level += 1
    return level


def history_support_information_levels(
    base: int, support_counts: Sequence[int]
) -> tuple[int, ...]:
    """Map a valid history-support profile to its integer information demand."""
    B = _base(base)
    row = _support_profile(support_counts)
    return tuple(integer_information_level(B, value) for value in row)


def r_adic_exponent_schedule_fits_history_profile(
    base: int,
    support_counts: Sequence[int],
    exponents: Sequence[int],
) -> bool:
    """Check cumulative B-adic exponent capacity against every history prefix."""
    levels = history_support_information_levels(base, support_counts)
    row = tuple(exponents)
    if len(row) != len(levels):
        raise ValueError("one exponent is required for the initial stage and every history step")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in row
    ):
        raise ValueError("resource exponents must be non-negative integers")
    cumulative = 0
    for exponent, required in zip(row, levels, strict=True):
        cumulative += exponent
        if cumulative < required:
            return False
    return True


def minimum_total_r_adic_exponent(
    base: int, support_counts: Sequence[int]
) -> int:
    """Minimum final B-adic transcript exponent for a valid history profile."""
    levels = history_support_information_levels(base, support_counts)
    return levels[-1]


def just_in_time_r_adic_exponents(
    base: int, support_counts: Sequence[int]
) -> tuple[int, ...]:
    """Minimum-total schedule that introduces capacity only when demand rises."""
    levels = history_support_information_levels(base, support_counts)
    previous = 0
    result = []
    for required in levels:
        if required < previous:
            raise AssertionError("valid history information demand must be nondecreasing")
        result.append(required - previous)
        previous = required
    schedule = tuple(result)
    if not r_adic_exponent_schedule_fits_history_profile(base, support_counts, schedule):
        raise AssertionError("just-in-time schedule must satisfy every demand prefix")
    return schedule


def minimum_r_adic_schedule_count(
    base: int, support_counts: Sequence[int]
) -> int:
    """Count minimum-total B-adic schedules above the information-demand boundary.

    Dynamic state is the cumulative exponent E_t.  The final cumulative exponent
    is fixed at L_B(R_H); at each stage E_t must be at least lambda_t and cannot
    decrease.  Each nondecreasing cumulative path corresponds uniquely to one
    exponent schedule by taking successive differences.
    """
    levels = history_support_information_levels(base, support_counts)
    final_level = levels[-1]
    dp = [0] * (final_level + 1)
    for cumulative in range(levels[0], final_level + 1):
        dp[cumulative] = 1

    for required in levels[1:]:
        next_dp = [0] * (final_level + 1)
        running = 0
        for cumulative in range(final_level + 1):
            running += dp[cumulative]
            if cumulative >= required:
                next_dp[cumulative] = running
        dp = next_dp
    return dp[final_level]


def minimum_schedule_storage_advance_area(
    base: int,
    support_counts: Sequence[int],
    exponents: Sequence[int],
) -> int:
    """Cumulative exponent slack above the target information demand.

    The schedule must have minimum final exponent L_B(R_H).  Area is summed
    through the penultimate stage; final slack is zero on the minimum-total
    frontier.
    """
    levels = history_support_information_levels(base, support_counts)
    row = tuple(exponents)
    if len(row) != len(levels):
        raise ValueError("schedule width must match the history profile")
    if not r_adic_exponent_schedule_fits_history_profile(base, support_counts, row):
        raise ValueError("schedule does not meet the declared history information demand")
    if sum(row) != levels[-1]:
        raise ValueError("storage-advance area here is restricted to minimum-total schedules")

    cumulative = 0
    area = 0
    for time in range(len(row) - 1):
        cumulative += row[time]
        area += cumulative - levels[time]
    return area
