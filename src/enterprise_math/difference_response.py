"""Exact state-dependent difference response for deterministic integer operations.

The base state remains a non-negative integer.  An oriented comparison is stored
as an integer ``difference`` subject to ``base + difference >= 0``.  Every
operation ``F : N -> N`` then induces the exact response

    R_F(base, difference) = F(base + difference) - F(base).

This module is an executable specification for P018 Supplement 11.  The
finite-difference identities are elementary/established mathematics; the code
exists to pressure-test their use inside the Enterprise Math precision and
irreversibility framework.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable

from .core import collapse, integer_nth_root
from .precision_signed_holonomy import signed_defect_transport

NaturalOperation = Callable[[int], int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def admissible_difference(base_state: int, difference: int) -> bool:
    """Return whether ``difference`` belongs to the fiber D_base."""
    _require_natural("base_state", base_state)
    _require_integer("difference", difference)
    return base_state + difference >= 0


def _checked_output(operation: NaturalOperation, state: int) -> int:
    output = operation(state)
    _require_natural("operation output", output)
    return output


def response(operation: NaturalOperation, base_state: int, difference: int) -> int:
    """Return the exact finite response ``F(x+h)-F(x)`` of a natural operation."""
    _require_natural("base_state", base_state)
    _require_integer("difference", difference)
    if not admissible_difference(base_state, difference):
        raise ValueError("difference is not admissible from base_state")
    base_output = _checked_output(operation, base_state)
    perturbed_output = _checked_output(operation, base_state + difference)
    result = perturbed_output - base_output
    if base_output + result < 0:
        raise AssertionError("response left the target difference fiber")
    return result


def identity_response(base_state: int, difference: int) -> int:
    """P018-T100 identity response."""
    return response(lambda value: value, base_state, difference)


def composed_response(
    first: NaturalOperation,
    second: NaturalOperation,
    base_state: int,
    difference: int,
) -> tuple[int, int]:
    """Return direct and staged responses for ``second ∘ first``.

    The two entries must agree by P018-T100.
    """
    first_response = response(first, base_state, difference)
    first_base = _checked_output(first, base_state)
    staged = response(second, first_base, first_response)
    direct = response(
        lambda value: _checked_output(second, _checked_output(first, value)),
        base_state,
        difference,
    )
    return direct, staged


def path_holonomy(
    first_path: NaturalOperation,
    second_path: NaturalOperation,
    base_state: int,
) -> int:
    """Return the oriented parallel-path difference ``second(x)-first(x)``."""
    _require_natural("base_state", base_state)
    first_output = _checked_output(first_path, base_state)
    second_output = _checked_output(second_path, base_state)
    holonomy = second_output - first_output
    if not admissible_difference(first_output, holonomy):
        raise AssertionError("parallel-path holonomy is not target-admissible")
    return holonomy


def suffix_holonomy(
    first_path: NaturalOperation,
    second_path: NaturalOperation,
    suffix: NaturalOperation,
    base_state: int,
) -> tuple[int, int]:
    """Return direct and response-propagated common-suffix holonomy (P018-T102)."""
    _require_natural("base_state", base_state)
    first_output = _checked_output(first_path, base_state)
    holonomy = path_holonomy(first_path, second_path, base_state)
    propagated = response(suffix, first_output, holonomy)
    direct = path_holonomy(
        lambda value: _checked_output(suffix, _checked_output(first_path, value)),
        lambda value: _checked_output(suffix, _checked_output(second_path, value)),
        base_state,
    )
    return direct, propagated


def quotient_response(base_state: int, difference: int, modulus: int) -> int:
    """P018-T101: quotient response, equal to signed precision transport."""
    _require_positive("modulus", modulus)
    quotient = lambda value: value // modulus
    direct = response(quotient, base_state, difference)
    transported = signed_defect_transport(modulus, base_state, difference)
    if direct != transported:
        raise AssertionError("quotient response disagrees with signed transport")
    return direct


def critical_square_defect(
    fine_operation: NaturalOperation,
    coarse_operation: NaturalOperation,
    base_state: int,
    ratio: int,
) -> int:
    """Return ``F_coarse(Q(x)) - Q(F_fine(x))`` for one precision square."""
    _require_natural("base_state", base_state)
    _require_positive("ratio", ratio)
    projected = base_state // ratio
    lower_then = _checked_output(coarse_operation, projected)
    upper_then = _checked_output(fine_operation, base_state) // ratio
    return lower_then - upper_then


def collapse_projection_defect(state: int, power: int, ratio: int) -> int:
    """P009/P018 collapse-versus-projection critical-square holonomy."""
    _require_natural("state", state)
    _require_positive("power", power)
    _require_positive("ratio", ratio)
    operation = lambda value: collapse(value, power)
    return critical_square_defect(operation, operation, state, ratio)


def collapse_commutator_holonomy(state: int, first_power: int, second_power: int) -> int:
    """Return ``C_p(C_q(n)) - C_q(C_p(n))`` from P018-T109/P003."""
    _require_natural("state", state)
    _require_positive("first_power", first_power)
    _require_positive("second_power", second_power)
    first_after_second = collapse(collapse(state, second_power), first_power)
    second_after_first = collapse(collapse(state, first_power), second_power)
    return first_after_second - second_after_first


def response_is_zero_collision(
    operation: NaturalOperation,
    base_state: int,
    difference: int,
) -> bool:
    """Check P018-T106 at one state/difference pair."""
    if not admissible_difference(base_state, difference):
        raise ValueError("difference is not admissible from base_state")
    zero_response = response(operation, base_state, difference) == 0
    same_output = _checked_output(operation, base_state + difference) == _checked_output(
        operation, base_state
    )
    if zero_response != same_output:
        raise AssertionError("zero response/collision equivalence failed")
    return zero_response


def compose_operations(operations: Iterable[NaturalOperation]) -> NaturalOperation:
    """Compose operations in iteration order: first item acts first."""
    operation_list = list(operations)

    def cumulative(value: int) -> int:
        _require_natural("state", value)
        current = value
        for operation in operation_list:
            current = _checked_output(operation, current)
        return current

    return cumulative


def zero_response_matches_endpoint_equality(
    operations: Iterable[NaturalOperation],
    base_state: int,
    difference: int,
) -> bool:
    """Executable form of P018-T107 for one cumulative deterministic path."""
    cumulative = compose_operations(operations)
    zero_response = response(cumulative, base_state, difference) == 0
    endpoint_equal = _checked_output(
        cumulative, base_state + difference
    ) == _checked_output(cumulative, base_state)
    if zero_response != endpoint_equal:
        raise AssertionError("cumulative zero-response relation mismatch")
    return zero_response


def collapse_response_is_same_basin(
    base_state: int,
    difference: int,
    power: int,
) -> bool:
    """P018-T108: zero collapse response iff both states have the same integer root."""
    _require_natural("base_state", base_state)
    _require_integer("difference", difference)
    _require_positive("power", power)
    if not admissible_difference(base_state, difference):
        raise ValueError("difference is not admissible from base_state")
    operation = lambda value: collapse(value, power)
    zero_response = response(operation, base_state, difference) == 0
    same_basin = integer_nth_root(base_state, power) == integer_nth_root(
        base_state + difference, power
    )
    if zero_response != same_basin:
        raise AssertionError("collapse zero-response/basin equivalence failed")
    return zero_response
