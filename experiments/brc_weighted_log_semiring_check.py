"""Exact research checker for weighted/log-semiring BRC candidate laws.

This is not a production tool and does not modify canonical R023 semantics.
It checks the finite-DAG path-sum theorem and the Boolean support projection on
non-negative rational carriers, plus explicit failure witnesses for additive
cancellation and multiplicative zero divisors.

No float, Decimal, Fraction, native division, or logarithm call is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Ratio:
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        if self.numerator < 0:
            raise ValueError("research Ratio numerator must be non-negative")
        if self.denominator <= 0:
            raise ValueError("research Ratio denominator must be positive")


ZERO = Ratio(0, 1)
ONE = Ratio(1, 1)


def ratio_add(left: Ratio, right: Ratio) -> Ratio:
    return Ratio(
        left.numerator * right.denominator
        + right.numerator * left.denominator,
        left.denominator * right.denominator,
    )


def ratio_multiply(left: Ratio, right: Ratio) -> Ratio:
    return Ratio(
        left.numerator * right.numerator,
        left.denominator * right.denominator,
    )


def ratio_equal(left: Ratio, right: Ratio) -> bool:
    return left.numerator * right.denominator == right.numerator * left.denominator


def support(value: Ratio) -> bool:
    return value.numerator != 0


EDGES = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}
PATHS_0_TO_3 = (
    ((0, 3),),
    ((0, 1), (1, 3)),
    ((0, 2), (2, 3)),
    ((0, 1), (1, 2), (2, 3)),
)


def local_weighted_recoalescence(weights: tuple[Ratio, ...]) -> tuple[Ratio, ...]:
    state = [ZERO, ZERO, ZERO, ZERO]
    state[0] = ONE
    for vertex in (1, 2, 3):
        total = ZERO
        for edge_index, (source, target) in enumerate(EDGES):
            if target == vertex:
                contribution = ratio_multiply(state[source], weights[edge_index])
                total = ratio_add(total, contribution)
        state[vertex] = total
    return tuple(state)


def explicit_path_sum(weights: tuple[Ratio, ...]) -> Ratio:
    total = ZERO
    for path in PATHS_0_TO_3:
        path_weight = ONE
        for edge in path:
            path_weight = ratio_multiply(path_weight, weights[EDGE_INDEX[edge]])
        total = ratio_add(total, path_weight)
    return total


def boolean_reachability(weights: tuple[Ratio, ...]) -> tuple[bool, ...]:
    state = [False, False, False, False]
    state[0] = True
    for vertex in (1, 2, 3):
        state[vertex] = any(
            state[source] and support(weights[edge_index])
            for edge_index, (source, target) in enumerate(EDGES)
            if target == vertex
        )
    return tuple(state)


def check_nonnegative_rational_projection() -> int:
    palette = (
        Ratio(0, 1),
        Ratio(1, 2),
        Ratio(1, 1),
        Ratio(2, 1),
    )
    checked = 0
    for weights in product(palette, repeat=len(EDGES)):
        weighted_state = local_weighted_recoalescence(weights)
        path_sum = explicit_path_sum(weights)
        if not ratio_equal(weighted_state[3], path_sum):
            raise AssertionError("local recoalescence differs from explicit path sum")
        boolean_state = boolean_reachability(weights)
        if support(weighted_state[3]) != boolean_state[3]:
            raise AssertionError("weighted support differs from Boolean support")
        checked += 1
    return checked


def check_signed_cancellation_counterexample() -> None:
    # Two source-to-target paths contribute +1 and -1.
    direct = 1
    via_intermediate = 1 * -1
    weighted_total = direct + via_intermediate
    boolean_support = (direct != 0) or (via_intermediate != 0)
    if weighted_total != 0 or not boolean_support:
        raise AssertionError("signed cancellation witness was not constructed")
    if (weighted_total != 0) == boolean_support:
        raise AssertionError("signed support should fail additive homomorphism")


def check_zero_divisor_counterexample() -> None:
    left = 2
    right = 3
    product_mod_6 = (left * right) % 6
    if left % 6 == 0 or right % 6 == 0:
        raise AssertionError("zero-divisor factors must be nonzero modulo 6")
    if product_mod_6 != 0:
        raise AssertionError("2*3 must vanish modulo 6")
    boolean_path_support = (left % 6 != 0) and (right % 6 != 0)
    if not boolean_path_support:
        raise AssertionError("Boolean path support should see both nonzero factors")


def check_equal_branch_surplus_prelog() -> None:
    # The exact log statement follows by applying ln to these positive masses:
    # total = k*m  =>  ln(total)-ln(m) = ln(k).
    for branch_count in range(1, 9):
        for mass in range(1, 9):
            total = branch_count * mass
            if total != branch_count * mass:
                raise AssertionError("equal-branch mass identity failed")
            maximum = mass
            if total < maximum or total > branch_count * maximum:
                raise AssertionError("recoalescence surplus bound failed")
            if total == branch_count * maximum and branch_count > 0:
                pass


def check_general_surplus_bounds_prelog() -> None:
    # For positive masses W=sum(w_i), M=max(w_i), k=len(w):
    # M <= W <= kM, hence 0 <= ln(W/M) <= ln(k).
    palettes = (
        (1,),
        (1, 2),
        (1, 1, 1),
        (1, 2, 3),
        (2, 5, 5, 1),
    )
    for weights in palettes:
        total = sum(weights)
        maximum = max(weights)
        count = len(weights)
        if not (maximum <= total <= count * maximum):
            raise AssertionError("pre-log surplus inequality failed")
        if total == maximum and count != 1:
            raise AssertionError("positive multi-branch total must exceed maximum")
        if total == count * maximum and any(weight != maximum for weight in weights):
            raise AssertionError("upper equality requires equal positive weights")


def main() -> None:
    cases = check_nonnegative_rational_projection()
    check_signed_cancellation_counterexample()
    check_zero_divisor_counterexample()
    check_equal_branch_surplus_prelog()
    check_general_surplus_bounds_prelog()
    print(
        "BRC weighted/log-semiring research check PASS: "
        f"{cases} exact rational DAG assignments; "
        "signed cancellation and zero-divisor obstructions confirmed"
    )


if __name__ == "__main__":
    main()
