"""Composition-safety hierarchy for P008-style collapse quotients.

Let q(n) be the complete-level/root index induced by a strictly increasing growth
law V.  There are two distinct composition questions:

1. representative coherence: compose only exact complete representatives V(k),
   collapse again, and ask whether the induced level operation is associative;
2. fiber congruence: ask whether all fine amounts in one q-fiber behave the same
   under the exact future operation.

Fiber congruence is the true P023 future-safety requirement for discarding basin
detail.  Representative coherence is strictly weaker.

Linear fixed-block growth passes representative associativity but fails addition
congruence on basin members (e.g. 0~4 mod floor(/5), yet +1 separates them).
Square growth can fail even representative associativity.  Retaining exact basin
detail restores the original associative addition in both cases.
"""

from __future__ import annotations

from .causal_basin_state import complete_level_join_is_associative_on_sample
from .causal_completion_collapse import completion_root_index


def collapse_class_map(growth: tuple[int, ...], maximum_amount: int) -> dict[int, int]:
    if not isinstance(growth, tuple) or not growth:
        raise ValueError("growth must be a non-empty tuple")
    if isinstance(maximum_amount, bool) or not isinstance(maximum_amount, int) or maximum_amount < 0:
        raise ValueError("maximum_amount must be a non-negative integer")
    result = {}
    for amount in range(maximum_amount + 1):
        level = completion_root_index(growth, amount)
        if level is not None:
            result[amount] = level
    return result


def addition_congruence_defects(
    growth: tuple[int, ...],
    maximum_amount: int,
) -> tuple[tuple[int, int, int, int], ...]:
    """Witnesses `(x,x_prime,y,qsum_difference)` showing q is not + congruence.

    We only need one common added amount y: if q(x)=q(x') but q(x+y)!=q(x'+y),
    the collapse cannot define an exact future-safe addition quotient.
    """
    classes = collapse_class_map(growth, maximum_amount * 2)
    values = tuple(range(maximum_amount + 1))
    defects = []
    for x in values:
        for x_prime in range(x + 1, maximum_amount + 1):
            if classes[x] != classes[x_prime]:
                continue
            for y in values:
                left_sum = x + y
                right_sum = x_prime + y
                if left_sum not in classes or right_sum not in classes:
                    continue
                if classes[left_sum] != classes[right_sum]:
                    defects.append((x, x_prime, y, classes[right_sum] - classes[left_sum]))
    return tuple(defects)


def collapse_is_addition_congruence_on_sample(
    growth: tuple[int, ...],
    maximum_amount: int,
) -> bool:
    return not addition_congruence_defects(growth, maximum_amount)


def representative_level_operation_is_associative(
    growth: tuple[int, ...],
    levels: tuple[int, ...],
) -> bool:
    return complete_level_join_is_associative_on_sample(growth, levels)


def safety_profile(
    growth: tuple[int, ...],
    levels: tuple[int, ...],
    maximum_amount: int,
) -> tuple[bool, bool]:
    """Return `(representative_associativity, full_fiber_addition_congruence)`."""
    return (
        representative_level_operation_is_associative(growth, levels),
        collapse_is_addition_congruence_on_sample(growth, maximum_amount),
    )
