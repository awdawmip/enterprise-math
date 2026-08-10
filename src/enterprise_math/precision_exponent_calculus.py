"""Fractionless exponent-coordinate tools for R004 precision research.

Positive integer scale factors are represented by their finite prime-exponent
words.  This is standard unique-factorization / valuation mathematics.  R004
uses it to linearize P005's multiplicative scale lattice without introducing
logarithms or normalized real coordinates.

No physical interpretation is attached automatically: rank, depth, and
exponent imbalance are arithmetic invariants of the scale word.  Calling them
spatial dimension, time, or isotropy requires an additional physical theorem.
"""
from __future__ import annotations

from itertools import combinations
from math import gcd, lcm
from collections.abc import Sequence

from enterprise_math.precision_prime_axes import prime_factorization

ExponentWord = tuple[tuple[int, int], ...]


def _pos(value: int, name: str = "value") -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def scale_exponent_word(scale: int) -> ExponentWord:
    """Canonical finite-support prime-exponent word for a positive integer."""
    _pos(scale, "scale")
    return prime_factorization(scale)


def exponent_word_to_integer(word: Sequence[tuple[int, int]]) -> int:
    """Decode a non-negative exponent word back to one positive integer."""
    items = tuple(word)
    last_prime = 1
    value = 1
    for prime, exponent in items:
        _pos(prime, "prime")
        if prime <= last_prime:
            raise ValueError("prime labels must be strictly increasing")
        if prime_factorization(prime) != ((prime, 1),):
            raise ValueError("word labels must be prime")
        if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent <= 0:
            raise ValueError("stored scale exponents must be positive")
        value *= prime**exponent
        last_prime = prime
    return value


def rational_exponent_word(numerator: int, denominator: int) -> ExponentWord:
    """Laurent prime-exponent word for one positive rational quantity.

    The result stores only integer exponents.  Negative exponents replace the
    denominator syntactically; no rational or floating-point object is created.
    """
    _pos(numerator, "numerator")
    _pos(denominator, "denominator")
    exponents: dict[int, int] = {}
    for prime, exponent in prime_factorization(numerator):
        exponents[prime] = exponents.get(prime, 0) + exponent
    for prime, exponent in prime_factorization(denominator):
        exponents[prime] = exponents.get(prime, 0) - exponent
    return tuple((prime, exponent) for prime, exponent in sorted(exponents.items()) if exponent)


def multiply_scale_words(left: int, right: int) -> ExponentWord:
    """Check that scale multiplication becomes coordinatewise exponent addition."""
    _pos(left, "left")
    _pos(right, "right")
    return scale_exponent_word(left * right)


def exponent_sum_word(left: int, right: int) -> ExponentWord:
    """Build the coordinatewise sum of two scale exponent words."""
    _pos(left, "left")
    _pos(right, "right")
    values: dict[int, int] = {}
    for prime, exponent in (*scale_exponent_word(left), *scale_exponent_word(right)):
        values[prime] = values.get(prime, 0) + exponent
    return tuple(sorted(values.items()))


def exponent_meet_word(left: int, right: int) -> ExponentWord:
    """Coordinatewise minimum, equal to the gcd exponent word."""
    _pos(left, "left")
    _pos(right, "right")
    a = dict(scale_exponent_word(left))
    b = dict(scale_exponent_word(right))
    return tuple(
        (prime, min(a.get(prime, 0), b.get(prime, 0)))
        for prime in sorted(set(a) | set(b))
        if min(a.get(prime, 0), b.get(prime, 0))
    )


def exponent_join_word(left: int, right: int) -> ExponentWord:
    """Coordinatewise maximum, equal to the lcm exponent word."""
    _pos(left, "left")
    _pos(right, "right")
    a = dict(scale_exponent_word(left))
    b = dict(scale_exponent_word(right))
    return tuple(
        (prime, max(a.get(prime, 0), b.get(prime, 0)))
        for prime in sorted(set(a) | set(b))
    )


def p005_exponent_linearization_holds(left: int, right: int) -> bool:
    """Executable specialization of the unique-factorization lattice isomorphism."""
    return (
        exponent_sum_word(left, right) == scale_exponent_word(left * right)
        and exponent_meet_word(left, right) == scale_exponent_word(gcd(left, right))
        and exponent_join_word(left, right) == scale_exponent_word(lcm(left, right))
    )


def scale_axis_rank(scale: int) -> int:
    """Number of active prime axes (little omega)."""
    return len(scale_exponent_word(scale))


def scale_total_depth(scale: int) -> int:
    """Total prime-exponent mass (big Omega), with Omega(1)=0."""
    return sum(exponent for _, exponent in scale_exponent_word(scale))


def scale_hasse_distance(left: int, right: int) -> int:
    """Graph distance in the prime-step divisibility Hasse graph.

    One edge multiplies or divides by one prime.  The exact distance is the L1
    difference of exponent vectors.
    """
    _pos(left, "left")
    _pos(right, "right")
    a = dict(scale_exponent_word(left))
    b = dict(scale_exponent_word(right))
    return sum(abs(a.get(prime, 0) - b.get(prime, 0)) for prime in set(a) | set(b))


def scale_hasse_distance_gcd_formula(left: int, right: int) -> int:
    """Equivalent scalar formula Omega(left/g)+Omega(right/g)."""
    _pos(left, "left")
    _pos(right, "right")
    common = gcd(left, right)
    return scale_total_depth(left // common) + scale_total_depth(right // common)


def exponent_imbalance_defect(scale: int) -> int:
    """Symmetric integer defect of unequal active-axis exponents.

    This is arithmetic anisotropy only.  Zero means all active prime exponents
    are equal; R004 already has a counterexample showing that this does not imply
    intrinsic graph/physical isotropy.
    """
    exponents = tuple(exponent for _, exponent in scale_exponent_word(scale))
    return sum(abs(left - right) for left, right in combinations(exponents, 2))


def equal_exponent_scale(scale: int) -> bool:
    return exponent_imbalance_defect(scale) == 0
