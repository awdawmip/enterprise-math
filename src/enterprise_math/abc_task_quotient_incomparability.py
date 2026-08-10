"""Exact incomparability witnesses for two P025 task-relative coarse states.

For a primitive abc triple define

    q_pair = min(rad(a)rad(b), rad(a)rad(c), rad(b)rad(c))

and let ``sigma_proj`` be the explicit Projective Capacity observable.

These scalar quotients are useful for different future languages.  Neither is
a function of the other, already on tiny unit triples.  The examples are an
application-level pressure test for P023 query-generated precision, not a new
generic quotient theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_support import abc_support_state, radical


@dataclass(frozen=True)
class TaskCoarseState:
    abc: tuple[int, int, int]
    pair_radical_selector: int
    sigma_projective: Fraction


def abc_task_coarse_state(a: int, b: int, c: int) -> TaskCoarseState:
    abc_support_state(a, b, c)
    radicals = (radical(a), radical(b), radical(c))
    pair_selector = min(
        radicals[0] * radicals[1],
        radicals[0] * radicals[2],
        radicals[1] * radicals[2],
    )
    sigma = projective_capacity_condition_state(a, b, c).sigma_projective
    return TaskCoarseState(
        abc=(a, b, c),
        pair_radical_selector=pair_selector,
        sigma_projective=sigma,
    )


def same_pair_selector_different_projective_counterexample() -> dict[str, object]:
    """Same de-Bruijn pair selector, different projective-capacity value."""
    first = abc_task_coarse_state(1, 2, 3)
    second = abc_task_coarse_state(1, 3, 4)
    if first.pair_radical_selector != second.pair_radical_selector:
        raise AssertionError("counterexample lost pair-radical collision")
    if first.sigma_projective == second.sigma_projective:
        raise AssertionError("counterexample lost projective separation")
    return {
        "first": first,
        "second": second,
        "shared_pair_selector": first.pair_radical_selector,
        "projective_values": (first.sigma_projective, second.sigma_projective),
    }


def same_projective_different_pair_selector_counterexample() -> dict[str, object]:
    """Same projective-capacity value, different de-Bruijn pair selector."""
    first = abc_task_coarse_state(1, 2, 3)
    second = abc_task_coarse_state(1, 5, 6)
    if first.sigma_projective != second.sigma_projective:
        raise AssertionError("counterexample lost projective collision")
    if first.pair_radical_selector == second.pair_radical_selector:
        raise AssertionError("counterexample lost pair-radical separation")
    return {
        "first": first,
        "second": second,
        "shared_projective": first.sigma_projective,
        "pair_selectors": (
            first.pair_radical_selector,
            second.pair_radical_selector,
        ),
    }


def future_query_separation_examples() -> dict[str, bool]:
    """Return exact threshold-query separations induced by the two collisions.

    * Same pair selector 2, but PCC_(1/2) differs between 1+2=3 and 1+3=4.
    * Same sigma 1, but the query ``q_pair<=3`` differs between 1+2=3 and 1+5=6.
    """
    first = abc_task_coarse_state(1, 2, 3)
    second = abc_task_coarse_state(1, 3, 4)
    third = abc_task_coarse_state(1, 5, 6)

    pcc_first = first.sigma_projective**2 < 3
    pcc_second = second.sigma_projective**2 < 4
    pair_first = first.pair_radical_selector <= 3
    pair_third = third.pair_radical_selector <= 3
    if pcc_first == pcc_second or pair_first == pair_third:
        raise AssertionError("future-query separation example changed")
    return {
        "pcc_half_123": pcc_first,
        "pcc_half_134": pcc_second,
        "pair_le_3_123": pair_first,
        "pair_le_3_156": pair_third,
    }
