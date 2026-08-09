"""Compile finite causal inventory operations into exact LEGO interaction laws.

An operation maps an input continuation-type inventory n to an output inventory.
For each output type upsilon, its integer count is expanded exactly in the
product-binomial LEGO interaction basis.  The compiled coefficients

    A[k, upsilon]

are the irreducible k-unit causal effects that create/destroy output type
upsilon.  Order-one-only operators are ordinary additive/matrix shadows;
higher orders are exact multi-witness interactions, not Taylor approximations.
"""

from __future__ import annotations

from itertools import product
from typing import Hashable

from .multitype_lego_interaction import (
    interaction_order,
    multitype_interaction_spectrum,
    reconstruct_multitype_response,
)

Type = Hashable
CountVector = tuple[int, ...]


def compile_inventory_operator(
    input_types: tuple[Type, ...],
    output_types: tuple[Type, ...],
    maxima: CountVector,
    operation_table: dict[CountVector, dict[Type, int]],
) -> dict[tuple[CountVector, Type], int]:
    """Compile a rectangular finite operation table into exact interaction coefficients."""
    if not isinstance(input_types, tuple) or not input_types:
        raise ValueError("input_types must be a non-empty tuple")
    if not isinstance(output_types, tuple) or not output_types:
        raise ValueError("output_types must be a non-empty tuple")
    if len(set(input_types)) != len(input_types) or len(set(output_types)) != len(output_types):
        raise ValueError("type labels must be unique")
    if not isinstance(maxima, tuple) or len(maxima) != len(input_types):
        raise ValueError("maxima must match input_types")
    expected_states = {
        tuple(state)
        for state in product(*(range(value + 1) for value in maxima))
    }
    if set(operation_table) != expected_states:
        raise ValueError("operation_table must cover the full rectangular input box")

    compiled: dict[tuple[CountVector, Type], int] = {}
    for output_type in output_types:
        response: dict[CountVector, int] = {}
        for state, inventory in operation_table.items():
            if not isinstance(inventory, dict):
                raise ValueError("each operation output must be an inventory dict")
            count = inventory.get(output_type, 0)
            if isinstance(count, bool) or not isinstance(count, int):
                raise ValueError("output counts must be integers")
            response[state] = count
        coefficients = multitype_interaction_spectrum(response, maxima)
        for order, coefficient in coefficients.items():
            if coefficient:
                compiled[(order, output_type)] = coefficient
    return compiled


def apply_compiled_inventory_operator(
    compiled: dict[tuple[CountVector, Type], int],
    output_types: tuple[Type, ...],
    state: CountVector,
) -> dict[Type, int]:
    """Reconstruct the exact output inventory at one input state."""
    result: dict[Type, int] = {}
    for output_type in output_types:
        coefficients = {
            order: coefficient
            for (order, target), coefficient in compiled.items()
            if target == output_type
        }
        # Missing coefficients inside the required lower box are zeros.
        full = {
            tuple(order): coefficients.get(tuple(order), 0)
            for order in product(*(range(value + 1) for value in state))
        }
        count = reconstruct_multitype_response(full, state)
        if count:
            result[output_type] = count
    return result


def operator_interaction_order(
    compiled: dict[tuple[CountVector, Type], int],
) -> int:
    """Maximum nonzero irreducible witness order in a compiled operator."""
    if not compiled:
        return 0
    return max(interaction_order(order) for order, _ in compiled)


def higher_operator_terms(
    compiled: dict[tuple[CountVector, Type], int],
    minimum_order: int = 2,
) -> dict[tuple[CountVector, Type], int]:
    if isinstance(minimum_order, bool) or not isinstance(minimum_order, int) or minimum_order < 0:
        raise ValueError("minimum_order must be a non-negative integer")
    return {
        key: coefficient
        for key, coefficient in compiled.items()
        if interaction_order(key[0]) >= minimum_order
    }
