"""Capped p-adic valuation carry and exact addition-repair tools for R004.

The p-adic valuation itself is established number theory.  This module uses it
as a pressure test of an exponent-first precision language:

* multiplication/gcd/lcm are naturally valuation-compatible;
* addition is exactly predictable from valuation levels when the levels differ;
* equal-level addition can create arbitrarily deep extra divisibility;
* at a finite cap K, level + normalized unit residue modulo p^(K-level)
  is sufficient, and those unit residues are pairwise future-distinguishable;
* if every translation modulo p^K belongs to the future language, the coarsest
  safe repair is the full residue modulo p^K, so universal addition removes all
  valuation-only compression.

The last point is an R004 specialization/consumer of P023/P024 future-safe
quotient logic, not a new generic partition-refinement theorem.
"""
from __future__ import annotations

from collections.abc import Sequence

ValuationSignature = tuple[int, int]


def _prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be a prime integer")
    divisor = 2
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            raise ValueError("prime must be a prime integer")
        divisor += 1


def _cap(cap: int) -> None:
    if isinstance(cap, bool) or not isinstance(cap, int) or cap <= 0:
        raise ValueError("cap must be a positive integer")


def p_valuation(value: int, prime: int) -> int:
    """Ordinary v_p(value) for a nonzero integer."""
    _prime(prime)
    if isinstance(value, bool) or not isinstance(value, int) or value == 0:
        raise ValueError("value must be a nonzero integer")
    remaining = abs(value)
    level = 0
    while remaining % prime == 0:
        remaining //= prime
        level += 1
    return level


def capped_p_valuation(value: int, prime: int, cap: int) -> int:
    """Finite valuation level, with zero and multiples of p^cap mapped to cap."""
    _prime(prime)
    _cap(cap)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("value must be a non-negative integer")
    if value == 0:
        return cap
    return min(p_valuation(value, prime), cap)


def valuation_carry(value: int, other: int, prime: int) -> int:
    """Extra valuation depth in a sum beyond the smaller input level."""
    if value <= 0 or other <= 0:
        raise ValueError("valuation carry uses positive integer summands")
    left = p_valuation(value, prime)
    right = p_valuation(other, prime)
    return p_valuation(value + other, prime) - min(left, right)


def valuation_only_sum_level(
    value: int, other: int, prime: int, cap: int
) -> int | None:
    """Return the capped sum level when input levels alone force it.

    Unequal levels force the minimum.  Two already-capped values force the cap.
    Equal uncapped levels return ``None`` because unit cancellation data matters.
    """
    left = capped_p_valuation(value, prime, cap)
    right = capped_p_valuation(other, prime, cap)
    if left == cap and right == cap:
        return cap
    if left != right:
        return min(left, right)
    return None


def equal_level_unbounded_carry_witness(
    prime: int, level: int, extra_depth: int
) -> tuple[int, int]:
    """Witness equal input valuations with arbitrarily large addition carry."""
    _prime(prime)
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")
    if isinstance(extra_depth, bool) or not isinstance(extra_depth, int) or extra_depth <= 0:
        raise ValueError("extra_depth must be a positive integer")
    left = prime**level
    right = prime**level * (prime**extra_depth - 1)
    if p_valuation(left, prime) != level or p_valuation(right, prime) != level:
        raise AssertionError("witness inputs must have the declared equal level")
    if p_valuation(left + right, prime) != level + extra_depth:
        raise AssertionError("witness sum must realize the requested carry depth")
    return left, right


def capped_unit_signature(value: int, prime: int, cap: int) -> ValuationSignature:
    """Canonical capped level plus normalized unit residue.

    If level ``a<cap``, write ``value=p^a*u`` with p not dividing u and retain
    ``u mod p^(cap-a)``.  Level ``cap`` uses residue marker zero.
    """
    level = capped_p_valuation(value, prime, cap)
    if level == cap:
        return cap, 0
    modulus = prime ** (cap - level)
    unit = (value // (prime**level)) % modulus
    if unit % prime == 0:
        raise AssertionError("normalized unit residue must be a p-adic unit")
    return level, unit


def signature_residue_mod_power(
    signature: ValuationSignature, prime: int, cap: int
) -> int:
    """Recover the represented residue modulo p^cap."""
    _prime(prime)
    _cap(cap)
    if len(signature) != 2:
        raise ValueError("signature must be (level, unit_residue)")
    level, unit = signature
    if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= cap:
        raise ValueError("signature level outside cap")
    modulus = prime**cap
    if level == cap:
        if unit != 0:
            raise ValueError("capped level uses zero residue marker")
        return 0
    unit_modulus = prime ** (cap - level)
    if (
        isinstance(unit, bool)
        or not isinstance(unit, int)
        or not 0 <= unit < unit_modulus
        or unit % prime == 0
    ):
        raise ValueError("invalid normalized unit residue")
    return (prime**level * unit) % modulus


def add_capped_unit_signatures(
    left: ValuationSignature,
    right: ValuationSignature,
    prime: int,
    cap: int,
) -> ValuationSignature:
    """Composition-safe addition at finite p-adic precision."""
    modulus = prime**cap
    total_residue = (
        signature_residue_mod_power(left, prime, cap)
        + signature_residue_mod_power(right, prime, cap)
    ) % modulus
    return capped_unit_signature(total_residue, prime, cap)


def unit_residue_class_count(prime: int, cap: int, level: int) -> int:
    """Number phi(p^(cap-level)) of sharp same-level repair classes."""
    _prime(prime)
    _cap(cap)
    if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= cap:
        raise ValueError("level outside cap")
    if level == cap:
        return 1
    height = cap - level
    return (prime - 1) * prime ** (height - 1)


def separate_distinct_unit_residues(
    left_unit: int,
    right_unit: int,
    prime: int,
    height: int,
) -> int:
    """Return one unit partner distinguishing two different unit residues.

    The partner is ``-left_unit mod p^height``.  The first sum reaches the cap;
    the second cannot because the two unit residues were distinct.
    """
    _prime(prime)
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be positive")
    modulus = prime**height
    for unit, name in ((left_unit, "left_unit"), (right_unit, "right_unit")):
        if (
            isinstance(unit, bool)
            or not isinstance(unit, int)
            or not 0 < unit < modulus
            or unit % prime == 0
        ):
            raise ValueError(f"{name} must be a nonzero unit residue")
    if left_unit == right_unit:
        raise ValueError("unit residues must be distinct")
    partner = (-left_unit) % modulus
    if partner == 0 or partner % prime == 0:
        raise AssertionError("negative of a unit must remain a nonzero unit")
    return partner


def universal_translation_signature(residue: int, prime: int, cap: int) -> tuple[int, ...]:
    """All capped-valuation observations under translations modulo p^cap."""
    _prime(prime)
    _cap(cap)
    modulus = prime**cap
    if isinstance(residue, bool) or not isinstance(residue, int) or not 0 <= residue < modulus:
        raise ValueError("residue outside Z/p^cap Z")
    return tuple(
        capped_p_valuation((residue + translation) % modulus, prime, cap)
        for translation in range(modulus)
    )


def universal_translation_closure_is_exact(prime: int, cap: int) -> bool:
    """Check that full translation language separates every residue mod p^cap."""
    _prime(prime)
    _cap(cap)
    modulus = prime**cap
    signatures = {
        universal_translation_signature(residue, prime, cap)
        for residue in range(modulus)
    }
    return len(signatures) == modulus


def repaired_class_count(prime: int, cap: int) -> int:
    """Total classes in level+unit repair, exactly p^cap."""
    _prime(prime)
    _cap(cap)
    return sum(unit_residue_class_count(prime, cap, level) for level in range(cap + 1))
