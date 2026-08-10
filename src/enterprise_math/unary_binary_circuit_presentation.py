"""Binary-power circuit presentation for repeated application of one exact action.

The literal unary d-macro table stores A,A^2,...,A^d and executes A^m using
roughly ceil(m/d) chunks.  A different presentation class stores only powers of
two:

    A, A^2, A^4, A^8, ...

through the declared horizon h.  Every exponent m<=h is then executed by the
binary expansion of m.  Storage is

    floor(log2 h)+1

stored matrices, while worst-case runtime composition count over 1<=m<=h is

    floor(log2(h+1)).

The latter is exact because ``2^t-1<=h`` for
`t=floor(log2(h+1))`, giving one exponent with t one-bits, while the smallest
integer with t+1 one-bits is ``2^(t+1)-1>h``.

Powers are precomputed by repeated squaring, so the table itself needs only one
new exact matrix multiplication per additional stored power after A.

This is a constructive circuit presentation, not a universal optimality theorem.
Addition chains, radix systems and task-specific algebra can yield other
frontiers.  Its purpose is to prove sharply that the literal contiguous-macro
Pareto is representation-class relative.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .presentation_storage_depth_pareto import (
    Matrix,
    Scalar,
    _validate_square_matrix,
    identity_matrix,
    matrix_multiply,
    macro_execution_blocks,
)


def _nonnegative_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _positive_int(value: int, *, name: str) -> int:
    result = _nonnegative_int(value, name=name)
    if result == 0:
        raise ValueError(f"{name} must be positive")
    return result


def binary_power_exponents(horizon: int) -> tuple[int, ...]:
    h = _positive_int(horizon, name="horizon")
    return tuple(1 << bit for bit in range(h.bit_length()))


def binary_power_rule_count(horizon: int) -> int:
    h = _positive_int(horizon, name="horizon")
    return h.bit_length()


def worst_case_binary_execution_blocks(horizon: int) -> int:
    h = _positive_int(horizon, name="horizon")
    return (h + 1).bit_length() - 1


def binary_execution_exponents(exponent: int) -> tuple[int, ...]:
    m = _nonnegative_int(exponent, name="exponent")
    return tuple(
        1 << bit
        for bit in range(m.bit_length())
        if (m >> bit) & 1
    )


def binary_execution_blocks(exponent: int) -> int:
    m = _nonnegative_int(exponent, name="exponent")
    return m.bit_count()


def precompute_binary_power_table(
    generator: Sequence[Sequence[Scalar]],
    horizon: int,
) -> dict[int, Matrix]:
    matrix = _validate_square_matrix(generator)
    exponents = binary_power_exponents(horizon)
    table: dict[int, Matrix] = {1: matrix}
    current = matrix
    exponent = 1
    for target_exponent in exponents[1:]:
        current = matrix_multiply(current, current)
        exponent *= 2
        if exponent != target_exponent:
            raise AssertionError("binary power exponent progression failed")
        table[target_exponent] = current
    return table


def binary_precompute_multiplications(horizon: int) -> int:
    return binary_power_rule_count(horizon) - 1


def execute_unary_power_from_binary_table(
    generator: Sequence[Sequence[Scalar]],
    exponent: int,
    horizon: int,
) -> Matrix:
    matrix = _validate_square_matrix(generator)
    m = _nonnegative_int(exponent, name="exponent")
    h = _positive_int(horizon, name="horizon")
    if m > h:
        raise ValueError("exponent exceeds declared horizon")
    if m == 0:
        return identity_matrix(len(matrix))
    table = precompute_binary_power_table(matrix, h)
    current = identity_matrix(len(matrix))
    for power in binary_execution_exponents(m):
        current = matrix_multiply(table[power], current)
    return current


def literal_unary_power(
    generator: Sequence[Sequence[Scalar]],
    exponent: int,
) -> Matrix:
    matrix = _validate_square_matrix(generator)
    m = _nonnegative_int(exponent, name="exponent")
    current = identity_matrix(len(matrix))
    for _ in range(m):
        current = matrix_multiply(matrix, current)
    return current


def binary_power_execution_matches_literal(
    generator: Sequence[Sequence[Scalar]],
    exponent: int,
    horizon: int,
) -> bool:
    literal = literal_unary_power(generator, exponent)
    binary = execute_unary_power_from_binary_table(generator, exponent, horizon)
    if literal != binary:
        raise AssertionError("binary-power circuit changed exact unary transition")
    return True


def literal_contiguous_execution_at_same_rule_count(horizon: int) -> int:
    h = _positive_int(horizon, name="horizon")
    rules = binary_power_rule_count(h)
    return macro_execution_blocks(h, min(rules, h))


@dataclass(frozen=True)
class UnaryPresentationComparison:
    horizon: int
    binary_stored_rules: int
    binary_precompute_multiplications: int
    binary_worst_execution_blocks: int
    contiguous_macro_depth_at_same_rule_count: int
    contiguous_worst_execution_blocks: int

    @property
    def binary_strictly_faster_at_same_rule_count(self) -> bool:
        return self.binary_worst_execution_blocks < self.contiguous_worst_execution_blocks

    @property
    def execution_blocks_saved(self) -> int:
        return self.contiguous_worst_execution_blocks - self.binary_worst_execution_blocks


def compare_binary_to_contiguous_same_storage(horizon: int) -> UnaryPresentationComparison:
    h = _positive_int(horizon, name="horizon")
    rules = binary_power_rule_count(h)
    contiguous_depth = min(rules, h)
    return UnaryPresentationComparison(
        horizon=h,
        binary_stored_rules=rules,
        binary_precompute_multiplications=binary_precompute_multiplications(h),
        binary_worst_execution_blocks=worst_case_binary_execution_blocks(h),
        contiguous_macro_depth_at_same_rule_count=contiguous_depth,
        contiguous_worst_execution_blocks=macro_execution_blocks(h, contiguous_depth),
    )


def first_horizon_binary_strictly_dominates_same_storage_contiguous(
    search_limit: int = 10000,
) -> int | None:
    limit = _positive_int(search_limit, name="search_limit")
    for horizon in range(1, limit + 1):
        if compare_binary_to_contiguous_same_storage(horizon).binary_strictly_faster_at_same_rule_count:
            return horizon
    return None
