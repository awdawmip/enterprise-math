#!/usr/bin/env python3
"""Exact finite checks for quotient nilpotence and resolvent growth.

The checker uses only integers and ``Fraction``.  It verifies a finite operator
no-go; no prime-distribution asymptotic is assumed.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable

Matrix = list[list[Fraction]]


def nilpotence_depth(n: int) -> int:
    assert n >= 1
    k = 0
    power = 1
    while power <= n:
        power *= 2
        k += 1
    return k


def mat_zero(n: int) -> Matrix:
    return [[Fraction(0, 1) for _ in range(n)] for _ in range(n)]


def mat_identity(n: int) -> Matrix:
    out = mat_zero(n)
    for i in range(n):
        out[i][i] = Fraction(1, 1)
    return out


def mat_add(a: Matrix, b: Matrix, scale: Fraction = Fraction(1, 1)) -> Matrix:
    n = len(a)
    return [[a[i][j] + scale * b[i][j] for j in range(n)] for i in range(n)]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    out = mat_zero(n)
    for i in range(n):
        for k in range(n):
            if a[i][k] == 0:
                continue
            for j in range(n):
                out[i][j] += a[i][k] * b[k][j]
    return out


def mat_pow(a: Matrix, exponent: int) -> Matrix:
    assert exponent >= 0
    out = mat_identity(len(a))
    base = a
    e = exponent
    while e:
        if e & 1:
            out = mat_mul(out, base)
        base = mat_mul(base, base)
        e //= 2
    return out


def sup_operator_norm(a: Matrix) -> Fraction:
    return max((sum((abs(x) for x in row), Fraction(0, 1)) for row in a), default=Fraction(0, 1))


def quotient_matrix(n: int, action: int) -> Matrix:
    """Matrix on states 1,...,n; values at state 0 are fixed to zero."""
    assert n >= 1 and action >= 2
    out = mat_zero(n)
    for state in range(1, n + 1):
        endpoint = state // action
        if endpoint > 0:
            out[state - 1][endpoint - 1] = Fraction(1, 1)
    return out


def convex_quotient_matrix(n: int, actions: Iterable[int], raw_weights: Iterable[int]) -> Matrix:
    actions = list(actions)
    raw_weights = list(raw_weights)
    assert actions and len(actions) == len(raw_weights)
    assert all(a >= 2 for a in actions)
    assert all(w > 0 for w in raw_weights)
    total = sum(raw_weights)
    out = mat_zero(n)
    for action, raw in zip(actions, raw_weights, strict=True):
        out = mat_add(out, quotient_matrix(n, action), Fraction(raw, total))
    return out


def run_word(n: int, word: list[int]) -> int:
    state = n
    for action in word:
        state //= action
    return state


def check_word_geometry(limit: int = 120) -> None:
    words = [[], [2], [3], [2, 2], [2, 3, 5], [7, 2, 2, 3]]
    for n in range(limit + 1):
        for word in words:
            product = 1
            for action in word:
                product *= action
            assert run_word(n, word) == n // product
            assert run_word(n, word) <= n // (2 ** len(word))


def check_nilpotence_and_inverse(limit: int = 45) -> None:
    action_sets = [([2], [1]), ([2, 3], [2, 3]), ([2, 4, 9], [5, 2, 7])]
    for n in range(1, limit + 1):
        depth = nilpotence_depth(n)
        identity = mat_identity(n)
        for actions, weights in action_sets:
            p = convex_quotient_matrix(n, actions, weights)
            assert mat_pow(p, depth) == mat_zero(n), (n, actions, depth)

            inverse = mat_zero(n)
            power = identity
            sign = Fraction(1, 1)
            for _ in range(depth):
                inverse = mat_add(inverse, power, sign)
                power = mat_mul(power, p)
                sign = -sign

            assert mat_mul(mat_add(identity, p), inverse) == identity
            assert mat_mul(inverse, mat_add(identity, p)) == identity
            assert sup_operator_norm(p) <= 1
            assert sup_operator_norm(inverse) <= depth


def check_deterministic_sharpness(limit: int = 100) -> None:
    for n in range(1, limit + 1):
        depth = nilpotence_depth(n)
        q2 = quotient_matrix(n, 2)
        identity = mat_identity(n)
        inverse = mat_zero(n)
        power = identity
        sign = Fraction(1, 1)
        for _ in range(depth):
            inverse = mat_add(inverse, power, sign)
            power = mat_mul(power, q2)
            sign = -sign
        assert sup_operator_norm(inverse) == depth, (n, depth, sup_operator_norm(inverse))


def main() -> None:
    check_word_geometry()
    check_nilpotence_and_inverse()
    check_deterministic_sharpness()
    print("prime-winding nilpotent pseudospectral checks: PASS")


if __name__ == "__main__":
    main()
