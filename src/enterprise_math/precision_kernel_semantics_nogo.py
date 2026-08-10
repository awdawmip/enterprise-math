"""Kernel-only semantic reconstruction no-go for the representation compiler.

An equivalence relation determines the quotient set but not the operations that a
typed future language requires on that quotient.  The smallest exact example uses
parity q:Z/4Z -> Z/2Z.  The same kernel supports both addition and multiplication,
but the descended quotient operations are different: XOR versus AND.

Therefore a representation compiler that must emit descended operations,
relations or witness semantics cannot take only a bare future kernel as input.
It needs the typed future language.  The kernel remains a useful intermediate
representation for equality/minimal-class computation, not a complete semantic
specification.
"""
from __future__ import annotations

from collections.abc import Callable

State = int
BinaryOperation = Callable[[int, int], int]
Table = tuple[tuple[int, int], tuple[int, int]]


def parity_observation(state: int) -> int:
    if isinstance(state, bool) or not isinstance(state, int):
        raise ValueError("state must be integer")
    return state % 2


def parity_partition() -> frozenset[frozenset[int]]:
    return frozenset((frozenset((0, 2)), frozenset((1, 3))))


def add_mod_four(left: int, right: int) -> int:
    return (left + right) % 4


def multiply_mod_four(left: int, right: int) -> int:
    return (left * right) % 4


def operation_descends_through_parity(operation: BinaryOperation) -> bool:
    for left_a in range(4):
        for left_b in range(4):
            if parity_observation(left_a) != parity_observation(left_b):
                continue
            for right_a in range(4):
                for right_b in range(4):
                    if parity_observation(right_a) != parity_observation(right_b):
                        continue
                    if parity_observation(operation(left_a, right_a)) != parity_observation(
                        operation(left_b, right_b)
                    ):
                        return False
    return True


def descended_parity_operation_table(operation: BinaryOperation) -> Table:
    if not operation_descends_through_parity(operation):
        raise ValueError("operation does not descend through parity quotient")
    representatives = (0, 1)
    return tuple(
        tuple(parity_observation(operation(left, right)) for right in representatives)
        for left in representatives
    )  # type: ignore[return-value]


def parity_addition_table() -> Table:
    return descended_parity_operation_table(add_mod_four)


def parity_multiplication_table() -> Table:
    return descended_parity_operation_table(multiply_mod_four)


def kernel_semantics_nogo_holds() -> bool:
    """Same quotient partition, distinct required descended operation semantics."""
    return (
        operation_descends_through_parity(add_mod_four)
        and operation_descends_through_parity(multiply_mod_four)
        and parity_addition_table() == ((0, 1), (1, 0))
        and parity_multiplication_table() == ((0, 0), (0, 1))
        and parity_addition_table() != parity_multiplication_table()
    )
