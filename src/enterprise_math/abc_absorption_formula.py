"""Closed prime-support formulas for P025 absorption redundancy.

This module removes witness-lattice enumeration from the exact minimum
Wronskian absorption redundancy introduced in P025 Supplement 04.  All
operations are finite integer arithmetic on prime supports and valuations.

The underlying determinantal-divisor calculation is standard integer linear
algebra.  The abc-specific closed formulas are research diagnostics; they do
not prove the abc conjecture and carry no historical-priority claim.
"""

from __future__ import annotations

from math import gcd

from .abc_support import abc_support_state, prime_factorization, radical
from .abc_witness_absorption import minimum_absorption_redundancy
from .abc_witness_precision import witness_coordinates


def _content(entries: tuple[int, ...]) -> int:
    result = 0
    for entry in entries:
        result = gcd(result, abs(entry))
    return result


def _valuation_map(n: int) -> dict[int, int]:
    return dict(prime_factorization(n))


def raw_additive_relation_vector(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the un-normalized integer row for ``d(a)+d(b)=d(c)``."""
    data = abc_support_state(a, b, c)
    coordinates = witness_coordinates(a, b, c)
    va = _valuation_map(a)
    vb = _valuation_map(b)
    vc = _valuation_map(c)
    row = []
    for prime in coordinates:
        if prime in va:
            row.append(a * va[prime] // prime)
        elif prime in vb:
            row.append(b * vb[prime] // prime)
        elif prime in vc:
            row.append(-c * vc[prime] // prime)
        else:  # pragma: no cover - coordinates are built from exactly these supports.
            raise AssertionError("prime coordinate escaped abc support partition")
    if not row or all(entry == 0 for entry in row):
        raise ValueError("abc support must give a non-zero additive relation row")
    # Touch data so malformed non-primitive triples are rejected by abc_support_state.
    if int(data["radical_product"]) != radical(a * b * c):
        raise AssertionError("abc support state returned inconsistent radical product")
    return tuple(row)


def additive_relation_content(a: int, b: int, c: int) -> int:
    """Return the gcd/content removed when the additive row is made primitive."""
    return _content(raw_additive_relation_vector(a, b, c))


def cross_block_absorption_terms(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the exact normalized cross-support minors.

    Let ``R=rad(abc)`` and ``g`` be the content of the raw additive relation
    row.  For primes ``p,q`` belonging to distinct support blocks among
    ``a,b,c``, the corresponding scaled Wronskian 2x2 minor divided by the
    compulsory multiplicity residual ``abc/R`` is

        R * v_p * v_q / (g * p * q).

    Same-block minors vanish and therefore do not affect the positive image
    step of the Wronskian on the additive witness lattice.
    """
    data = abc_support_state(a, b, c)
    supports = tuple(tuple(int(p) for p in support) for support in data["supports"])
    valuations = tuple(_valuation_map(n) for n in (a, b, c))
    R = int(data["radical_product"])
    g = additive_relation_content(a, b, c)
    terms: list[int] = []
    for left_block in range(3):
        for right_block in range(left_block + 1, 3):
            for p in supports[left_block]:
                for q in supports[right_block]:
                    numerator = R * valuations[left_block][p] * valuations[right_block][q]
                    denominator = g * p * q
                    if numerator % denominator != 0:
                        raise AssertionError("normalized cross-support minor must be integral")
                    terms.append(numerator // denominator)
    if not terms:
        raise ValueError("need primes in at least two abc support blocks for non-degenerate Wronskians")
    return tuple(terms)


def minimum_absorption_redundancy_support_formula(a: int, b: int, c: int) -> int:
    """Compute ``eta_min`` directly from support blocks and valuations."""
    result = _content(cross_block_absorption_terms(a, b, c))
    if result <= 0:
        raise AssertionError("absorption floor must be positive")
    return result


def support_formula_matches_determinantal_formula(a: int, b: int, c: int) -> bool:
    """Audit the closed support formula against the exterior-divisor formula."""
    support_value = minimum_absorption_redundancy_support_formula(a, b, c)
    determinant_value = minimum_absorption_redundancy(a, b, c)
    if support_value != determinant_value:
        raise AssertionError("support formula disagrees with determinantal formula")
    return True


def is_squarefree(n: int) -> bool:
    """Return whether the positive integer is squarefree; 1 is squarefree."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return all(exponent == 1 for _prime, exponent in prime_factorization(n))


def squarefree_perfect_absorption(a: int, b: int, c: int) -> bool:
    """Verify the squarefree sufficient family ``eta_min=1``.

    For a primitive abc triple with at least two non-unit terms, if every term
    is squarefree then every valuation is one, the raw additive row has content
    one, and the gcd of the cross terms ``rad(abc)/(pq)`` is one.
    """
    abc_support_state(a, b, c)
    if sum(value > 1 for value in (a, b, c)) < 2:
        raise ValueError("need at least two non-unit support blocks")
    if not all(is_squarefree(value) for value in (a, b, c)):
        raise ValueError("squarefree family requires all three terms squarefree")
    eta = minimum_absorption_redundancy_support_formula(a, b, c)
    if eta != 1:
        raise AssertionError("squarefree primitive abc triple lost perfect absorption")
    return True


def one_plus_squarefree_to_prime_power_absorption(
    b: int, prime: int, exponent: int
) -> int:
    """Return ``eta_min=exponent`` for ``1+b=prime^exponent`` with squarefree b.

    This is an exact family specialization of the support formula, not an
    existence claim about how often ``prime^exponent-1`` is squarefree.
    """
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
        raise ValueError("prime must be a prime integer > 1")
    if prime_factorization(prime) != ((prime, 1),):
        raise ValueError("prime must be prime")
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 1:
        raise ValueError("exponent must be a positive integer")
    if b <= 1 or not is_squarefree(b):
        raise ValueError("b must be squarefree and greater than 1")
    c = prime**exponent
    if 1 + b != c:
        raise ValueError("require 1+b=prime^exponent")
    eta = minimum_absorption_redundancy_support_formula(1, b, c)
    if eta != exponent:
        raise AssertionError("one-plus-squarefree prime-power formula failed")
    return eta


def two_prime_power_blocks_absorption(
    p: int, m: int, q: int, n: int
) -> dict[str, int | bool]:
    """Specialize to an actual primitive relation ``1+p^m=q^n``.

    The two support coordinates give the exact formula

        eta_min = m*n / gcd(m*p^(m-1), n*q^(n-1)).

    Perfect absorption is equivalent to the pair of divisibilities
    ``n | p^(m-1)`` and ``m | q^(n-1)``.
    """
    for name, prime in (("p", p), ("q", q)):
        if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
            raise ValueError(f"{name} must be a prime integer > 1")
        if prime_factorization(prime) != ((prime, 1),):
            raise ValueError(f"{name} must be prime")
    for name, exponent in (("m", m), ("n", n)):
        if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 1:
            raise ValueError(f"{name} must be a positive integer")
    if p == q:
        raise ValueError("the two prime support blocks must be distinct")
    a = 1
    b = p**m
    c = q**n
    if a + b != c:
        raise ValueError("require the actual relation 1+p^m=q^n")
    g = gcd(m * p ** (m - 1), n * q ** (n - 1))
    if (m * n) % g != 0:
        raise AssertionError("actual prime-power abc relation must make g divide mn")
    formula = (m * n) // g
    eta = minimum_absorption_redundancy_support_formula(a, b, c)
    if eta != formula:
        raise AssertionError("two-prime-power support formula failed")
    divisibility_test = p ** (m - 1) % n == 0 and q ** (n - 1) % m == 0
    if (eta == 1) != divisibility_test:
        raise AssertionError("perfect-absorption divisibility classification failed")
    return {
        "row_content": g,
        "eta_min": eta,
        "perfect_absorption": eta == 1,
    }
