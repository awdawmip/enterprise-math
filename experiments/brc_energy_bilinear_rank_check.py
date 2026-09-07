"""Exact rank certificate for the BRC energy-jet bounded-product frontier.

The scaled-cross implementation computes two bilinear outputs from bounded
innovation variables y=(e,w,a) and N-sized state variables x=(J,q,s,t,u):

1. the N-sized bilinear part of nabla^3 E_new;
2. the N-sized bilinear part of C_new-C.

Flattening the output/innovation axes against x gives a 6-by-5 integer matrix.
Its rank is five.  Any algorithm in the declared linear-coordinate model that
builds these bilinear outputs from products of one innovation linear form and
one N-sized state linear form therefore needs at least five such products.
The current scaled-cross formulas use exactly five.
"""
from __future__ import annotations

from fractions import Fraction

# Row order: (E,e), (E,w), (E,a), (C,e), (C,w), (C,a).
# Column order: J, q, s, t, u.
BILINEAR_FLATTENING = (
    (2, 2, 0, 0, 0),
    (0, 2, 0, 0, 0),
    (0, 0, 0, 0, 0),
    (0, 0, 6, 6, 0),
    (0, 0, 6, 0, 0),
    (0, 0, 0, 0, 12),
)


def rational_rank(rows: tuple[tuple[int, ...], ...]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(pivot_row, row_count) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_value = matrix[pivot_row][column]
        matrix[pivot_row] = [value / pivot_value for value in matrix[pivot_row]]
        for index in range(row_count):
            if index == pivot_row or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                left - factor * right
                for left, right in zip(matrix[index], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def outer(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(a * b for b in right) for a in left)


def add_matrices(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def current_five_product_decomposition() -> tuple[tuple[int, ...], ...]:
    zero = tuple(tuple(0 for _ in range(5)) for _ in range(6))
    # Each term is one bounded-innovation linear form times one N-sized-state
    # linear form, followed by routing to one output.
    terms = (
        # 2*e*(J+q)
        ((2, 0, 0, 0, 0, 0), (1, 1, 0, 0, 0)),
        # 2*w*q
        ((0, 2, 0, 0, 0, 0), (0, 1, 0, 0, 0)),
        # 6*e*(s+t)
        ((0, 0, 0, 6, 0, 0), (0, 0, 1, 1, 0)),
        # 6*w*s
        ((0, 0, 0, 0, 6, 0), (0, 0, 1, 0, 0)),
        # 12*a*u
        ((0, 0, 0, 0, 0, 12), (0, 0, 0, 0, 1)),
    )
    result = zero
    for left, right in terms:
        result = add_matrices(result, outer(left, right))
    return result


def main() -> None:
    assert rational_rank(BILINEAR_FLATTENING) == 5
    assert rational_rank(BILINEAR_FLATTENING[:3]) == 2
    assert rational_rank(BILINEAR_FLATTENING[3:]) == 3
    assert current_five_product_decomposition() == BILINEAR_FLATTENING
    print("BRC energy bilinear rank: PASS (combined rank=5, achieved by 5 products)")


if __name__ == "__main__":
    main()
