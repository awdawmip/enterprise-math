"""Exact integer tooling for candidate primitive lattices from Gram matrices.

This module deliberately avoids floating-point geometry.  Given a symmetric
positive-definite integer Gram matrix G, it performs an exact Fraction-valued LDL
factorization and recursively enumerates all integer coefficient vectors x with

    x^T G x = target_norm.

The resulting minimal vectors can then be fed to the generic primitive causal
link profiler.  The implementation is intended as a research reference for
lattices supplied by exact Gram data (for example catalogue entries such as
Lambda_9/Lambda_10), not as a high-performance lattice-enumeration package.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt

Gram = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _validate_gram(gram: Gram) -> None:
    if not isinstance(gram, tuple) or not gram:
        raise ValueError("gram must be a non-empty tuple of rows")
    n = len(gram)
    if any(not isinstance(row, tuple) or len(row) != n for row in gram):
        raise ValueError("gram must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in gram
        for value in row
    ):
        raise ValueError("gram entries must be integers")
    for i in range(n):
        for j in range(n):
            if gram[i][j] != gram[j][i]:
                raise ValueError("gram must be symmetric")


def exact_ldl(gram: Gram) -> tuple[tuple[tuple[Fraction, ...], ...], tuple[Fraction, ...]]:
    """Return exact unit-lower L and positive diagonal D with G=L D L^T."""
    _validate_gram(gram)
    n = len(gram)
    lower = [[Fraction(int(i == j), 1) for j in range(n)] for i in range(n)]
    diagonal = [Fraction(0, 1) for _ in range(n)]

    for i in range(n):
        value = Fraction(gram[i][i], 1)
        for k in range(i):
            value -= lower[i][k] * lower[i][k] * diagonal[k]
        if value <= 0:
            raise ValueError("gram must be positive definite")
        diagonal[i] = value

        for j in range(i + 1, n):
            entry = Fraction(gram[j][i], 1)
            for k in range(i):
                entry -= lower[j][k] * lower[i][k] * diagonal[k]
            lower[j][i] = entry / diagonal[i]

    return tuple(tuple(row) for row in lower), tuple(diagonal)


def gram_norm(gram: Gram, vector: Vector) -> int:
    _validate_gram(gram)
    if len(vector) != len(gram) or any(
        isinstance(value, bool) or not isinstance(value, int) for value in vector
    ):
        raise ValueError("vector must be an integer coefficient tuple of matching dimension")
    return sum(
        vector[i] * gram[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def _floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def _ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def _ceil_sqrt_fraction(value: Fraction) -> int:
    if value < 0:
        raise ValueError("square-root bound must be non-negative")
    ceiling = (value.numerator + value.denominator - 1) // value.denominator
    root = isqrt(ceiling)
    return root if root * root == ceiling else root + 1


def vectors_of_norm(gram: Gram, target_norm: int) -> tuple[Vector, ...]:
    """Enumerate all nonzero integer coefficient vectors of exact Gram norm."""
    _validate_gram(gram)
    if (
        isinstance(target_norm, bool)
        or not isinstance(target_norm, int)
        or target_norm <= 0
    ):
        raise ValueError("target_norm must be a positive integer")

    lower, diagonal = exact_ldl(gram)
    n = len(gram)
    current = [0] * n
    result: list[Vector] = []

    def recurse(index: int, partial: Fraction) -> None:
        if index < 0:
            vector = tuple(current)
            if any(vector) and gram_norm(gram, vector) == target_norm:
                result.append(vector)
            return

        remaining = Fraction(target_norm, 1) - partial
        if remaining < 0:
            return

        tail = sum(
            lower[j][index] * current[j]
            for j in range(index + 1, n)
        )
        radius = _ceil_sqrt_fraction(remaining / diagonal[index]) + 1
        center = -tail
        low = _floor_fraction(center) - radius
        high = _ceil_fraction(center) + radius

        for value in range(low, high + 1):
            shifted = Fraction(value, 1) + tail
            contribution = diagonal[index] * shifted * shifted
            if contribution > remaining:
                continue
            current[index] = value
            recurse(index - 1, partial + contribution)
        current[index] = 0

    recurse(n - 1, Fraction(0, 1))
    return tuple(sorted(result))


def minimal_vectors(gram: Gram, minimal_norm: int) -> tuple[Vector, ...]:
    """Semantic alias used by the causal-link research code."""
    return vectors_of_norm(gram, minimal_norm)
