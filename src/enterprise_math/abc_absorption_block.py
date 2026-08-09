"""Block-level compression of the P025 absorption floor.

For one integer ``n`` the normalized arithmetic derivative

    d_x(n) / (n/rad(n))

ranges over one principal ideal ``h(n) Z``.  The generator

    h(n) = gcd_{p|n} v_p(n) * rad(n)/p

compresses all within-block prime coordinates for the purpose of Wronskian
absorption-floor arithmetic.  For a primitive abc triple, ``eta_min`` then
depends only on the three block radicals, residuals, and derivative contents.

The gcd/Bezout facts are elementary integer algebra.  The module is a compact
reference implementation for the P025 certificate-language specialization.
"""

from __future__ import annotations

from math import gcd

from .abc_absorption_formula import (
    additive_relation_content,
    minimum_absorption_redundancy_support_formula,
)
from .abc_support import abc_support_state, multiplicity_residual, prime_factorization, radical


def _positive_gcd(values: tuple[int, ...]) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def normalized_block_derivative_coefficients(n: int) -> tuple[tuple[int, int], ...]:
    """Return coefficients of ``d_x(n)/(n/rad(n))`` by prime coordinate.

    If ``R=rad(n)``, the coefficient at prime ``p`` is
    ``v_p(n) * R/p``.  The unit ``n=1`` has no prime coordinates.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return ()
    R = radical(n)
    return tuple((p, exponent * (R // p)) for p, exponent in prime_factorization(n))


def block_derivative_content(n: int) -> int:
    """Return ``h(n)``; define ``h(1)=0`` for the empty support block."""
    coefficients = normalized_block_derivative_coefficients(n)
    if not coefficients:
        return 0
    result = _positive_gcd(tuple(value for _prime, value in coefficients))
    if result <= 0:
        raise AssertionError("nonempty derivative coefficient set must have positive content")
    return result


def normalized_block_derivative_value(n: int, coordinates: tuple[int, ...]) -> int:
    """Evaluate ``d_x(n)/(n/rad(n))`` on local prime-coordinate values."""
    coefficients = normalized_block_derivative_coefficients(n)
    if len(coordinates) != len(coefficients):
        raise ValueError("coordinate count must match the prime support of n")
    return sum(value * x for (_prime, value), x in zip(coefficients, coordinates, strict=True))


def block_raw_additive_content(n: int) -> int:
    """Return the gcd of the raw additive-row coefficients contributed by n."""
    if n == 1:
        return 0
    return multiplicity_residual(n) * block_derivative_content(n)


def triple_block_additive_content(a: int, b: int, c: int) -> int:
    """Return the raw additive-row content from the three compressed blocks."""
    abc_support_state(a, b, c)
    result = _positive_gcd(
        (
            block_raw_additive_content(a),
            block_raw_additive_content(b),
            block_raw_additive_content(c),
        )
    )
    if result <= 0:
        raise AssertionError("primitive abc triple must have a nonzero additive row")
    direct = additive_relation_content(a, b, c)
    if result != direct:
        raise AssertionError("block additive content disagrees with prime-coordinate row")
    return result


def block_absorption_terms(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return at most three positive block-pair generators for ``eta_min``.

    Let ``R_i=rad(n_i)`` and ``h_i=h(n_i)`` for blocks ``a,b,c``.  If blocks
    ``i,j`` are nonempty and ``k`` is the remaining block, the gcd of all
    normalized cross-prime minors between ``i`` and ``j`` is

        R_k * h_i * h_j / g,

    where ``g`` is the raw additive-row content.  Unit blocks have ``h=0`` and
    contribute no pair.
    """
    abc_support_state(a, b, c)
    values = (a, b, c)
    radicals = tuple(radical(n) for n in values)
    contents = tuple(block_derivative_content(n) for n in values)
    g = triple_block_additive_content(a, b, c)
    terms: list[int] = []
    for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        if contents[i] == 0 or contents[j] == 0:
            continue
        numerator = radicals[k] * contents[i] * contents[j]
        if numerator % g != 0:
            raise AssertionError("compressed block minor generator must be integral")
        terms.append(numerator // g)
    if not terms:
        raise ValueError("need at least two nonempty prime-support blocks")
    return tuple(terms)


def minimum_absorption_redundancy_block_formula(a: int, b: int, c: int) -> int:
    """Compute ``eta_min`` from at most three compressed block terms."""
    result = _positive_gcd(block_absorption_terms(a, b, c))
    if result <= 0:
        raise AssertionError("absorption floor must be positive")
    support_formula = minimum_absorption_redundancy_support_formula(a, b, c)
    if result != support_formula:
        raise AssertionError("block formula disagrees with cross-prime support formula")
    return result


def block_absorption_state(a: int, b: int, c: int) -> dict[str, object]:
    """Return the compact arithmetic state sufficient to compute ``eta_min``."""
    abc_support_state(a, b, c)
    radicals = tuple(radical(n) for n in (a, b, c))
    residuals = tuple(multiplicity_residual(n) for n in (a, b, c))
    contents = tuple(block_derivative_content(n) for n in (a, b, c))
    g = triple_block_additive_content(a, b, c)
    terms = block_absorption_terms(a, b, c)
    eta = _positive_gcd(terms)
    return {
        "radicals": radicals,
        "multiplicity_residuals": residuals,
        "block_derivative_contents": contents,
        "raw_additive_content": g,
        "block_absorption_terms": terms,
        "eta_min": eta,
    }
