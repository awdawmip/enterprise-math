"""Finite staged-composition effect for two material response layers.

This module studies a pure integer projection effect, not a physical laminate
constitutive law.  Two response layers are represented by finite ratios
``r1/A1`` and ``r2/A2`` acting on an incoming integer budget ``B``.

Direct one-shot composition is

    D = floor(B*r1*r2/(A1*A2)).

Sequential layer order 1->2 is

    S12 = floor(floor(B*r1/A1)*r2/A2),

and order 2->1 is defined symmetrically.  Because the first projection discards
less than one ``A1``-cell of numerator, exact Euclidean division gives

    D-S12 in {0,1},
    D-S21 in {0,1},
    |S12-S21| <= 1.

Thus noncommuting finite layer order can arise solely from intermediate
projection even though the undeformed rational product is commutative.  The
report retains exact remainders/carry bits so this effect is fully auditable.
"""

from __future__ import annotations

from dataclasses import dataclass


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_layer(response: int, amplitude: int, label: str) -> None:
    _require_nonnegative(f"{label}_response", response)
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude <= 0:
        raise ValueError(f"{label}_amplitude must be a positive integer")
    if response > amplitude:
        raise ValueError(f"{label}_response must not exceed amplitude")


@dataclass(frozen=True)
class StagedLayerOrder:
    first_response: int
    first_amplitude: int
    second_response: int
    second_amplitude: int
    first_stage_budget: int
    first_stage_remainder: int
    second_stage_remainder: int
    staged_budget: int
    direct_budget: int
    direct_minus_staged: int
    carry_bit: int


def staged_layer_order(
    incoming_budget: int,
    first_response: int,
    first_amplitude: int,
    second_response: int,
    second_amplitude: int,
) -> StagedLayerOrder:
    """Evaluate one ordered two-layer projection and its exact one-bit defect."""
    _require_nonnegative("incoming_budget", incoming_budget)
    _require_layer(first_response, first_amplitude, "first")
    _require_layer(second_response, second_amplitude, "second")

    first_num = incoming_budget * first_response
    first_budget, first_remainder = divmod(first_num, first_amplitude)
    second_num = first_budget * second_response
    staged_budget, second_remainder = divmod(second_num, second_amplitude)
    direct_budget = (
        incoming_budget * first_response * second_response
        // (first_amplitude * second_amplitude)
    )
    defect = direct_budget - staged_budget
    if defect not in (0, 1):
        raise AssertionError("two-layer staged projection defect escaped one-bit bound")

    carry_lhs = first_amplitude * second_remainder + first_remainder * second_response
    carry_rhs = first_amplitude * second_amplitude
    carry = int(carry_lhs >= carry_rhs)
    if defect != carry:
        raise AssertionError("two-layer projection defect disagrees with exact carry criterion")
    return StagedLayerOrder(
        first_response=first_response,
        first_amplitude=first_amplitude,
        second_response=second_response,
        second_amplitude=second_amplitude,
        first_stage_budget=first_budget,
        first_stage_remainder=first_remainder,
        second_stage_remainder=second_remainder,
        staged_budget=staged_budget,
        direct_budget=direct_budget,
        direct_minus_staged=defect,
        carry_bit=carry,
    )


@dataclass(frozen=True)
class TwoLayerOrderComparison:
    incoming_budget: int
    direct_budget: int
    order_12: StagedLayerOrder
    order_21: StagedLayerOrder
    signed_order_difference: int
    absolute_order_difference: int


def compare_two_layer_orders(
    incoming_budget: int,
    response_1: int,
    amplitude_1: int,
    response_2: int,
    amplitude_2: int,
) -> TwoLayerOrderComparison:
    """Compare both staged orders against their common direct product projection."""
    order_12 = staged_layer_order(
        incoming_budget,
        response_1,
        amplitude_1,
        response_2,
        amplitude_2,
    )
    order_21 = staged_layer_order(
        incoming_budget,
        response_2,
        amplitude_2,
        response_1,
        amplitude_1,
    )
    if order_12.direct_budget != order_21.direct_budget:
        raise AssertionError("commutative direct product changed under layer exchange")
    signed = order_12.staged_budget - order_21.staged_budget
    absolute = abs(signed)
    if absolute > 1:
        raise AssertionError("two-layer order effect exceeded one returned-budget quantum")
    return TwoLayerOrderComparison(
        incoming_budget=incoming_budget,
        direct_budget=order_12.direct_budget,
        order_12=order_12,
        order_21=order_21,
        signed_order_difference=signed,
        absolute_order_difference=absolute,
    )
