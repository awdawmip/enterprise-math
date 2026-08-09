"""Exact endpoint-pair and integer holonomy calculus for a 2x2 deterministic grid.

Semantically replayed from historical P018 research. The subtraction-free layer
keeps endpoint pairs and composes adjacent pairs by their shared endpoint. When
states are natural numbers, the same rectangle admits an exact signed-difference
coordinate whose two decompositions agree by finite response/telescoping
identities.

No limiting process, derivative, probability, or floating-point arithmetic is
used here.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

from .difference_response import admissible_difference, response

X = TypeVar("X")
Y = TypeVar("Y")
Z = TypeVar("Z")

NaturalOperation = Callable[[int], int]


def compose_adjacent_pairs(
    first: tuple[X, X], second: tuple[X, X]
) -> tuple[X, X]:
    """Compose ``(a,b)`` and ``(b,c)`` into the endpoint pair ``(a,c)``."""
    if first[1] != second[0]:
        raise ValueError("state pairs are not adjacent")
    return first[0], second[1]


def bifurcated_pair_map(
    first_operation: Callable[[X], Y],
    second_operation: Callable[[X], Y],
    pair: tuple[X, X],
) -> tuple[Y, Y]:
    """Apply possibly different deterministic maps to the two pair components."""
    return first_operation(pair[0]), second_operation(pair[1])


def rectangle_endpoint_pairs(
    first_left: Callable[[X], Y],
    first_right: Callable[[X], Y],
    second_left: Callable[[Y], Z],
    second_right: Callable[[Y], Z],
    state: X,
) -> tuple[tuple[Z, Z], tuple[Z, Z], tuple[Z, Z]]:
    """Return outer pair and the two exact 2x2 pair decompositions."""
    f0 = first_left(state)
    f1 = first_right(state)
    a = second_left(f0)
    b = second_left(f1)
    c = second_right(f0)
    d = second_right(f1)

    outer = (a, d)
    horizontal_then_vertical = compose_adjacent_pairs((a, b), (b, d))
    vertical_then_horizontal = compose_adjacent_pairs((a, c), (c, d))

    if outer != horizontal_then_vertical or outer != vertical_then_horizontal:
        raise AssertionError("critical-grid endpoint-pair interchange failed")
    return outer, horizontal_then_vertical, vertical_then_horizontal


def _require_natural_output(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")
    return value


def operation_family_difference(
    first_operation: NaturalOperation,
    second_operation: NaturalOperation,
    state: int,
) -> int:
    """Return the oriented pointwise difference ``G1(y)-G0(y)``."""
    _require_natural_output("state", state)
    first = _require_natural_output("first operation output", first_operation(state))
    second = _require_natural_output("second operation output", second_operation(state))
    return second - first


def rectangle_holonomy(
    first_left: NaturalOperation,
    first_right: NaturalOperation,
    second_left: NaturalOperation,
    second_right: NaturalOperation,
    state: int,
) -> int:
    """Return outer signed holonomy ``G1(F1(x)) - G0(F0(x))``."""
    _require_natural_output("state", state)
    f0 = _require_natural_output("F0 output", first_left(state))
    f1 = _require_natural_output("F1 output", first_right(state))
    a = _require_natural_output("G0(F0(x))", second_left(f0))
    d = _require_natural_output("G1(F1(x))", second_right(f1))
    return d - a


def rectangle_holonomy_decompositions(
    first_left: NaturalOperation,
    first_right: NaturalOperation,
    second_left: NaturalOperation,
    second_right: NaturalOperation,
    state: int,
) -> tuple[int, int, int]:
    """Return outer holonomy and its two exact finite decompositions."""
    _require_natural_output("state", state)
    f0 = _require_natural_output("F0 output", first_left(state))
    f1 = _require_natural_output("F1 output", first_right(state))
    displacement = f1 - f0
    if not admissible_difference(f0, displacement):
        raise AssertionError("first-stage displacement is not admissible")

    outer = rectangle_holonomy(
        first_left, first_right, second_left, second_right, state
    )
    first_route = response(second_left, f0, displacement) + operation_family_difference(
        second_left, second_right, f1
    )
    second_route = operation_family_difference(
        second_left, second_right, f0
    ) + response(second_right, f0, displacement)

    if outer != first_route or outer != second_route:
        raise AssertionError("numeric critical-grid interchange failed")
    return outer, first_route, second_route


def rectangle_variation_identity(
    first_left: NaturalOperation,
    first_right: NaturalOperation,
    second_left: NaturalOperation,
    second_right: NaturalOperation,
    state: int,
) -> tuple[int, int]:
    """Return the two sides of the exact finite rectangle-variation identity."""
    _require_natural_output("state", state)
    f0 = _require_natural_output("F0 output", first_left(state))
    f1 = _require_natural_output("F1 output", first_right(state))
    displacement = f1 - f0

    left = operation_family_difference(
        second_left, second_right, f1
    ) - operation_family_difference(second_left, second_right, f0)
    right = response(second_right, f0, displacement) - response(
        second_left, f0, displacement
    )
    if left != right:
        raise AssertionError("rectangle-variation identity failed")
    return left, right


def common_suffix_reduction(
    first_left: NaturalOperation,
    first_right: NaturalOperation,
    suffix: NaturalOperation,
    state: int,
) -> tuple[int, int]:
    """Reduce the rectangle identity to ordinary common-suffix response."""
    _require_natural_output("state", state)
    f0 = _require_natural_output("F0 output", first_left(state))
    f1 = _require_natural_output("F1 output", first_right(state))
    displacement = f1 - f0
    outer = rectangle_holonomy(first_left, first_right, suffix, suffix, state)
    propagated = response(suffix, f0, displacement)
    if outer != propagated:
        raise AssertionError("common-suffix reduction failed")
    return outer, propagated


def common_prefix_reduction(
    prefix: NaturalOperation,
    second_left: NaturalOperation,
    second_right: NaturalOperation,
    state: int,
) -> tuple[int, int]:
    """Reduce the rectangle identity when both first-stage paths are identical."""
    _require_natural_output("state", state)
    intermediate = _require_natural_output("prefix output", prefix(state))
    outer = rectangle_holonomy(prefix, prefix, second_left, second_right, state)
    pointwise = operation_family_difference(second_left, second_right, intermediate)
    if outer != pointwise:
        raise AssertionError("common-prefix reduction failed")
    return outer, pointwise


def cancellation_example(state: int = 1) -> dict[str, int]:
    """Concrete zero-outer-holonomy example with nonzero local edge defects."""
    _require_natural_output("state", state)
    if state < 1:
        raise ValueError("state must be at least 1 for this example")
    f0 = lambda value: value
    f1 = lambda value: value + 1
    g0 = lambda value: value
    g1 = lambda value: max(value - 1, 0)

    f0x = f0(state)
    f1x = f1(state)
    outer = rectangle_holonomy(f0, f1, g0, g1, state)
    first_displacement = f1x - f0x
    g_defect_at_f1 = operation_family_difference(g0, g1, f1x)
    if outer != 0 or first_displacement == 0 or g_defect_at_f1 == 0:
        raise AssertionError("cancellation counterexample was not realized")
    return {
        "outer": outer,
        "first_displacement": first_displacement,
        "g_defect_at_f1": g_defect_at_f1,
    }
