"""Anonymous occupancy growth: free relation dimension plus periodic residue structure.

Let A_m(c) be the number of anonymous occupancy histograms of total c on m slots.
Equivalently it is the number of integer partitions of c into at most m parts (or,
by conjugation, parts of size at most m).  A direct LEGO recurrence is

    A_m(c) = A_m(c-m) + A_(m-1)(c),

with the first term representing states using at least one size-m column/part.
Unlike the labeled weak-composition count H_m(c), A_m(c) is generally not a
single polynomial; finite permutation quotient leaves a periodic/quasi-polynomial
residue pattern.  The free relation rank m-1 therefore must be separated from the
finite period/torsion shadow.

For L=lcm(1,...,m), the standard restricted-partition quasi-polynomial theorem
implies that step-L finite differences remove polynomial degree without mixing
residue classes.  The executable reference checks the resulting exact identities
for bounded m/ranges; the general quasi-polynomial theorem is prior art.
"""

from __future__ import annotations

from math import gcd, factorial


def lcm(left: int, right: int) -> int:
    if left <= 0 or right <= 0:
        raise ValueError("lcm inputs must be positive")
    return left // gcd(left, right) * right


def anonymity_period(slot_count: int) -> int:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    result = 1
    for value in range(1, slot_count + 1):
        result = lcm(result, value)
    return result


def anonymous_occupancy_count(slot_count: int, total: int) -> int:
    """Restricted partition count via parts <= slot_count."""
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be non-negative")
    counts = [0] * (total + 1)
    counts[0] = 1
    for part in range(1, slot_count + 1):
        for amount in range(part, total + 1):
            counts[amount] += counts[amount - part]
    return counts[total]


def anonymous_growth_sequence(slot_count: int, maximum_total: int) -> tuple[int, ...]:
    return tuple(anonymous_occupancy_count(slot_count, total) for total in range(maximum_total + 1))


def anonymous_recurrence_identity(slot_count: int, total: int) -> bool:
    if slot_count == 1:
        return anonymous_occupancy_count(1, total) == 1
    left = anonymous_occupancy_count(slot_count, total)
    without_max = anonymous_occupancy_count(slot_count - 1, total)
    with_max = anonymous_occupancy_count(slot_count, total - slot_count) if total >= slot_count else 0
    return left == without_max + with_max


def step_difference(values: tuple[int, ...], step: int) -> tuple[int, ...]:
    if isinstance(step, bool) or not isinstance(step, int) or step <= 0:
        raise ValueError("step must be positive")
    if len(values) <= step:
        return ()
    return tuple(values[index + step] - values[index] for index in range(len(values) - step))


def repeated_step_difference(values: tuple[int, ...], step: int, order: int) -> tuple[int, ...]:
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be non-negative")
    current = values
    for _ in range(order):
        current = step_difference(current, step)
    return current


def expected_top_step_difference(slot_count: int) -> int:
    """For L=lcm(1..m), Delta_L^(m-1) A_m = L^(m-1)/m! under the quasi-polynomial theorem."""
    L = anonymity_period(slot_count)
    numerator = L ** max(0, slot_count - 1)
    denominator = factorial(slot_count)
    if numerator % denominator != 0:
        raise AssertionError("expected restricted-partition top difference should be integral")
    return numerator // denominator


def period_aware_dimension_check(slot_count: int, starting_total: int = 0) -> bool:
    """Finite executable audit with enough samples for m period-sized differences."""
    if starting_total < 0:
        raise ValueError("starting_total must be non-negative")
    L = anonymity_period(slot_count)
    order = slot_count - 1
    # Need at least order+2 step-L positions to expose the top constant and one zero difference.
    maximum_total = starting_total + L * (slot_count + 2)
    values = tuple(
        anonymous_occupancy_count(slot_count, total)
        for total in range(starting_total, maximum_total + 1)
    )
    top = repeated_step_difference(values, L, order)
    next_level = repeated_step_difference(values, L, order + 1)
    return (
        bool(top)
        and len(set(top)) == 1
        and top[0] == expected_top_step_difference(slot_count)
        and all(value == 0 for value in next_level)
    )


def unit_difference_fails_for_two_slot_anonymous_growth(maximum_total: int = 20) -> bool:
    values = anonymous_growth_sequence(2, maximum_total)
    first = step_difference(values, 1)
    return len(set(first)) > 1 and period_aware_dimension_check(2)
