"""Universality of primitive positive coefficient rows in arithmetic blocks.

For an integer block ``n=prod p_i^e_i``, the normalized arithmetic-derivative
coefficient at prime ``p_i`` is

    e_i * rad(n) / p_i.

After division by the block content, this gives a primitive positive integer
row.  Conversely every primitive positive integer row occurs in this way:
choose distinct primes ``p_i`` and exponents ``e_i=p_i*b_i``.  Then every
normalized coefficient is ``rad(n)*b_i`` and their gcd is ``rad(n)``.

This elementary construction is used as a negative boundary: the coefficient
rows appearing in P025 block access are not a narrower combinatorial class than
arbitrary primitive positive integer rows.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_absorption_block import (
    block_derivative_content,
    normalized_block_derivative_coefficients,
)
from .abc_support import prime_factorization


@dataclass(frozen=True)
class BlockRowRealization:
    requested_row: tuple[int, ...]
    primes: tuple[int, ...]
    exponents: tuple[int, ...]
    integer_block: int
    normalized_coefficients: tuple[int, ...]
    block_content: int
    primitive_block_row: tuple[int, ...]


def _primitive_positive_row(row: tuple[int, ...]) -> tuple[int, ...]:
    if not row:
        raise ValueError("row must be nonempty")
    content = 0
    for value in row:
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError("row entries must be positive integers")
        content = gcd(content, value)
    if content != 1:
        raise ValueError("row must be primitive")
    return row


def _validate_distinct_primes(primes: tuple[int, ...], dimension: int) -> None:
    if len(primes) != dimension:
        raise ValueError("prime-label count must equal row dimension")
    if len(set(primes)) != dimension:
        raise ValueError("prime labels must be distinct")
    for prime in primes:
        if (
            isinstance(prime, bool)
            or not isinstance(prime, int)
            or prime <= 1
            or prime_factorization(prime) != ((prime, 1),)
        ):
            raise ValueError("prime labels must be distinct primes")


def primitive_block_row(n: int) -> tuple[int, ...]:
    """Return the primitive positive derivative coefficient row of ``n>1``."""
    coefficients = normalized_block_derivative_coefficients(n)
    if not coefficients:
        raise ValueError("n must have nonempty prime support")
    content = block_derivative_content(n)
    row = tuple(value // content for _prime, value in coefficients)
    if gcd(*row) != 1:
        raise AssertionError("block row normalization failed to be primitive")
    return row


def realize_primitive_block_row(
    row: tuple[int, ...], primes: tuple[int, ...]
) -> BlockRowRealization:
    """Construct an integer block whose primitive derivative row is ``row``.

    Given primitive ``b_i>0`` and distinct primes ``p_i``, set

        e_i = p_i*b_i,
        n = product p_i^e_i.

    Then ``rad(n)=R`` and the normalized derivative coefficient is

        e_i * R/p_i = R*b_i.

    Its content is ``R``, so the primitive row is exactly ``b``.
    """
    row = _primitive_positive_row(row)
    _validate_distinct_primes(primes, len(row))
    exponents = tuple(prime * value for prime, value in zip(primes, row, strict=True))
    n = 1
    for prime, exponent in zip(primes, exponents, strict=True):
        n *= prime**exponent

    coefficients = normalized_block_derivative_coefficients(n)
    observed_primes = tuple(prime for prime, _value in coefficients)
    if observed_primes != tuple(sorted(primes)):
        # prime_factorization orders the block coordinates.  Require caller labels
        # in that canonical order so row entries retain their intended labels.
        raise ValueError("prime labels must be supplied in increasing order")
    values = tuple(value for _prime, value in coefficients)
    content = block_derivative_content(n)
    primitive = tuple(value // content for value in values)
    if primitive != row:
        raise AssertionError("constructed integer block failed row realization")

    return BlockRowRealization(
        requested_row=row,
        primes=primes,
        exponents=exponents,
        integer_block=n,
        normalized_coefficients=values,
        block_content=content,
        primitive_block_row=primitive,
    )


def primitive_positive_rows_are_exact_block_row_class(
    row: tuple[int, ...], primes: tuple[int, ...]
) -> bool:
    """Executable witness for the converse direction of the row-class theorem."""
    realization = realize_primitive_block_row(row, primes)
    if primitive_block_row(realization.integer_block) != row:
        raise AssertionError("row-class converse witness failed")
    return True
