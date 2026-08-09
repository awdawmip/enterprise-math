"""Finite linear codes as shadows of residue conservation checks.

A causal conservation law can be specified by a matrix H over Z/qZ.  The
syndrome of an integer/residue event x is Hx mod q; allowed residue patterns are
the kernel.  When q is a field modulus this kernel is the traditional linear
code defined by a parity-check matrix.

The project ordering is therefore:

    conservation checks -> residue kernel/code -> local alphabet lift -> geometry.

Minimum Hamming weight is the minimum support of a nonzero residue-conserving
pattern.  Weight enumerators count support layers but are weaker than the exact
accepted event family.

This is standard coding-theory algebra.  The code is used here as a finite
coordinate shadow of a causal conservation kernel, not claimed as a new object.
"""

from __future__ import annotations

from itertools import product

Word = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _validate_matrix(checks: Matrix, modulus: int) -> int:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 2:
        raise ValueError("modulus must be at least two")
    if not checks or not checks[0]:
        raise ValueError("check matrix must be non-empty")
    width = len(checks[0])
    if any(len(row) != width for row in checks):
        raise ValueError("all check rows must have equal width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in checks for value in row
    ):
        raise ValueError("check entries must be integers")
    return width


def residue_syndrome(word: Word, checks: Matrix, modulus: int) -> tuple[int, ...]:
    width = _validate_matrix(checks, modulus)
    if len(word) != width:
        raise ValueError("word length must match check width")
    return tuple(
        sum(coefficient * value for coefficient, value in zip(row, word)) % modulus
        for row in checks
    )


def satisfies_residue_conservation(word: Word, checks: Matrix, modulus: int) -> bool:
    return all(value == 0 for value in residue_syndrome(word, checks, modulus))


def residue_kernel(checks: Matrix, modulus: int) -> tuple[Word, ...]:
    width = _validate_matrix(checks, modulus)
    return tuple(
        tuple(word)
        for word in product(range(modulus), repeat=width)
        if satisfies_residue_conservation(tuple(word), checks, modulus)
    )


def hamming_weight(word: Word) -> int:
    return sum(value != 0 for value in word)


def minimum_nonzero_support(codewords: tuple[Word, ...]) -> int | None:
    weights = [hamming_weight(word) for word in codewords if any(word)]
    return min(weights) if weights else None


def support_histogram(codewords: tuple[Word, ...]) -> dict[int, int]:
    histogram: dict[int, int] = {}
    for word in codewords:
        weight = hamming_weight(word)
        histogram[weight] = histogram.get(weight, 0) + 1
    return dict(sorted(histogram.items()))


def binary_single_parity_check(length: int) -> Matrix:
    if length < 2:
        raise ValueError("length must be at least two")
    return (tuple(1 for _ in range(length)),)


def ternary_repetition_checks() -> Matrix:
    # x0=x1=x2 mod 3.
    return (
        (1, -1, 0),
        (0, 1, -1),
    )


def ternary_hamming_4_checks() -> Matrix:
    # Parity-check matrix dual to G=[I_2 | [[1,1],[1,2]]].
    return (
        (2, 2, 1, 0),
        (2, 1, 0, 1),
    )
