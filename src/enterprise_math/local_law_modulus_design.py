"""Arithmetic design laws for finite local-law residue codebooks.

For a finite exact integer codebook S, reduction modulo M is injective exactly
when M divides no nonzero difference of two values in S.  With semantic side
information, apply this criterion independently to each contextual codebook.

This turns local precision design into a finite divisor-avoidance problem.  It
also exposes several exact consequences:

* bad moduli form a finite union of divisor down-sets;
* reflective moduli are upward closed under divisibility but have no least
  element in the divisibility poset;
* a single p-adic ladder has an exact first reflective depth determined by the
  largest p-adic valuation of a codebook difference;
* for repeated copies of one primitive weight w, mod-M capacity is
  M/gcd(M,w)-1;
* several modular sensors are jointly equivalent to their lcm modulus.

The module is coefficient-arithmetic only.  The parent bounded-local-law owner
supplies the machine semantics that consume these codebooks.
"""

from __future__ import annotations

from math import gcd, isqrt, lcm
from typing import Hashable, Mapping, Sequence


Context = Hashable


def _alphabet(values: Sequence[int] | frozenset[int]) -> tuple[int, ...]:
    result = tuple(sorted(set(values)))
    if not result:
        raise ValueError("codebook must be nonempty")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("codebook values must be integers")
    return result


def codebook_difference_spectrum(
    values: Sequence[int] | frozenset[int],
) -> frozenset[int]:
    alphabet = _alphabet(values)
    return frozenset(
        abs(right - left)
        for index, left in enumerate(alphabet)
        for right in alphabet[index + 1 :]
        if right != left
    )


def contextual_difference_spectra(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
) -> dict[Context, frozenset[int]]:
    if not codebooks:
        raise ValueError("at least one contextual codebook is required")
    return {
        context: codebook_difference_spectrum(values)
        for context, values in codebooks.items()
    }


def positive_divisors(value: int) -> frozenset[int]:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value <= 0:
        raise ValueError("value must be positive")
    result = set()
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        partner = value // divisor
        if divisor >= 2:
            result.add(divisor)
        if partner >= 2:
            result.add(partner)
    return frozenset(result)


def bad_moduli_for_codebooks(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
) -> frozenset[int]:
    bad = set()
    for spectrum in contextual_difference_spectra(codebooks).values():
        for difference in spectrum:
            bad.update(positive_divisors(difference))
    return frozenset(bad)


def modulus_reflects_codebooks(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
    modulus: int,
) -> bool:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    spectra = contextual_difference_spectra(codebooks)
    return all(
        difference % modulus != 0
        for spectrum in spectra.values()
        for difference in spectrum
    )


def codebook_cardinality_lower_bound(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
) -> int:
    if not codebooks:
        raise ValueError("at least one contextual codebook is required")
    return max(len(_alphabet(values)) for values in codebooks.values())


def codebook_width_upper_bound(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
) -> int:
    """A guaranteed reflective modulus, not generally the least one."""
    if not codebooks:
        raise ValueError("at least one contextual codebook is required")
    width = max(
        max(alphabet) - min(alphabet)
        for values in codebooks.values()
        for alphabet in (_alphabet(values),)
    )
    return max(2, width + 1)


def least_numeric_reflective_modulus(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
) -> int:
    upper = codebook_width_upper_bound(codebooks)
    lower = max(2, codebook_cardinality_lower_bound(codebooks))
    for modulus in range(lower, upper + 1):
        if modulus_reflects_codebooks(codebooks, modulus):
            return modulus
    raise AssertionError("finite width bound failed to contain a reflective modulus")


def reflective_moduli_upward_closed_sample(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
    limit: int,
) -> bool:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 2:
        raise ValueError("limit must be an integer at least two")
    good = {
        modulus
        for modulus in range(2, limit + 1)
        if modulus_reflects_codebooks(codebooks, modulus)
    }
    for modulus in good:
        for multiple in range(2 * modulus, limit + 1, modulus):
            if multiple not in good:
                raise AssertionError("reflective modulus set is not upward closed")
    return True


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def incomparable_reflective_prime_witnesses(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
) -> tuple[int, int]:
    """Two incomparable reflective primes, proving no divisibility-least modulus."""
    spectra = contextual_difference_spectra(codebooks)
    maximum_difference = max(
        (difference for spectrum in spectra.values() for difference in spectrum),
        default=1,
    )
    primes = []
    candidate = max(2, maximum_difference + 1)
    while len(primes) < 2:
        if _is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    left, right = primes
    if not modulus_reflects_codebooks(codebooks, left):
        raise AssertionError("large prime failed contextual reflection")
    if not modulus_reflects_codebooks(codebooks, right):
        raise AssertionError("large prime failed contextual reflection")
    return left, right


def p_adic_valuation(value: int, prime: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value == 0:
        raise ValueError("value must be a nonzero integer")
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    amount = abs(value)
    exponent = 0
    while amount % prime == 0:
        amount //= prime
        exponent += 1
    return exponent


def first_reflective_padic_exponent(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
    prime: int,
) -> int:
    """Least e>=1 such that mod p^e is injective in every contextual codebook."""
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    spectra = contextual_difference_spectra(codebooks)
    maximum_valuation = max(
        (
            p_adic_valuation(difference, prime)
            for spectrum in spectra.values()
            for difference in spectrum
        ),
        default=0,
    )
    return maximum_valuation + 1


def padic_reflection_matches_depth(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
    prime: int,
    exponent: int,
) -> bool:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 1:
        raise ValueError("exponent must be a positive integer")
    predicted = exponent >= first_reflective_padic_exponent(codebooks, prime)
    actual = modulus_reflects_codebooks(codebooks, prime**exponent)
    if predicted != actual:
        raise AssertionError("p-adic valuation-depth criterion disagreed with reflection")
    return predicted


def single_primitive_capacity(weight: int, modulus: int) -> int:
    """Largest d with injective code on {0,w,2w,...,dw}."""
    if isinstance(weight, bool) or not isinstance(weight, int) or weight == 0:
        raise ValueError("weight must be a nonzero integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1:
        raise ValueError("modulus must exceed one")
    return modulus // gcd(modulus, abs(weight)) - 1


def single_primitive_reflects(
    weight: int,
    max_terms: int,
    modulus: int,
) -> bool:
    if isinstance(max_terms, bool) or not isinstance(max_terms, int) or max_terms < 0:
        raise ValueError("max_terms must be a nonnegative integer")
    return max_terms <= single_primitive_capacity(weight, modulus)


def first_reflective_padic_exponent_for_single_primitive(
    weight: int,
    max_terms: int,
    prime: int,
) -> int:
    if isinstance(weight, bool) or not isinstance(weight, int) or weight == 0:
        raise ValueError("weight must be a nonzero integer")
    if isinstance(max_terms, bool) or not isinstance(max_terms, int) or max_terms < 1:
        raise ValueError("max_terms must be a positive integer")
    if not _is_prime(prime):
        raise ValueError("prime must be prime")

    primitive_valuation = p_adic_valuation(weight, prime)
    power = 1
    extra = 0
    while power <= max_terms:
        power *= prime
        extra += 1
    return primitive_valuation + extra


def scaling_by_unit_preserves_reflection(
    values: Sequence[int] | frozenset[int],
    scale: int,
    modulus: int,
) -> bool:
    if isinstance(scale, bool) or not isinstance(scale, int) or scale == 0:
        raise ValueError("scale must be a nonzero integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1:
        raise ValueError("modulus must exceed one")
    if gcd(abs(scale), modulus) != 1:
        raise ValueError("scale must be a unit modulo modulus")
    alphabet = _alphabet(values)
    original = {"original": frozenset(alphabet)}
    scaled = {"scaled": frozenset(scale * value for value in alphabet)}
    result = modulus_reflects_codebooks(original, modulus)
    if modulus_reflects_codebooks(scaled, modulus) != result:
        raise AssertionError("unit scaling changed modular reflection")
    return result


def joint_modulus(moduli: Sequence[int]) -> int:
    values = tuple(moduli)
    if not values:
        raise ValueError("at least one modulus is required")
    result = 1
    for modulus in values:
        if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1:
            raise ValueError("every modulus must exceed one")
        result = lcm(result, modulus)
    return result


def modular_sensor_family_reflects(
    codebooks: Mapping[Context, Sequence[int] | frozenset[int]],
    moduli: Sequence[int],
) -> bool:
    """Tuple residues are injective exactly when the lcm modulus is injective."""
    return modulus_reflects_codebooks(codebooks, joint_modulus(moduli))
