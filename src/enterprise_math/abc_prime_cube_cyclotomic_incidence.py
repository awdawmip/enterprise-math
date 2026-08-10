"""Finite incidence bounds for P025 cyclotomic congruence signatures.

If a repeated Phi_3/Phi_6 signature has modulus M and k repeated primes, then
p/q is restricted to exactly 2^k invertible CRT root classes modulo M.
For labelled integers 1<=p,q<=P this gives the elementary envelope

    2^k * P * (floor((P-1)/M)+1).

Primality, p>q, and the original cyclotomic equation can only reduce this count.
No prime-distribution theorem is used.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_prime_cube_cyclotomic_congruence import CyclotomicCongruenceSignature


@dataclass(frozen=True)
class CyclotomicIncidenceEnvelope:
    height: int
    repeated_modulus: int
    repeated_prime_count: int
    root_choice_count: int
    candidates_per_q_per_root: int
    ordered_integer_pair_bound: int
    ambient_ordered_pair_count: int


def cyclotomic_signature_incidence_envelope(
    signature: CyclotomicCongruenceSignature, height: int
) -> CyclotomicIncidenceEnvelope:
    """Return the exact elementary integer-pair envelope for one signature."""
    if isinstance(height, bool) or not isinstance(height, int) or height < 1:
        raise ValueError("height must be a positive integer")
    M = signature.repeated_modulus
    choices = signature.root_choice_count
    k = len(signature.constraints)
    if choices != 1 << k:
        raise AssertionError("root choice count must be two per repeated prime")
    per = (height - 1) // M + 1
    raw_bound = choices * height * per
    ambient = height * height
    bound = min(ambient, raw_bound)
    return CyclotomicIncidenceEnvelope(
        height=height,
        repeated_modulus=M,
        repeated_prime_count=k,
        root_choice_count=choices,
        candidates_per_q_per_root=per,
        ordered_integer_pair_bound=bound,
        ambient_ordered_pair_count=ambient,
    )


def repeated_modulus_minimum(repeated_prime_count: int) -> int:
    """Return the universal lower bound ``49^k`` for k repeated cyclotomic primes."""
    if (
        isinstance(repeated_prime_count, bool)
        or not isinstance(repeated_prime_count, int)
        or repeated_prime_count < 0
    ):
        raise ValueError("repeated_prime_count must be a non-negative integer")
    return 49**repeated_prime_count


def root_class_compression_ratio_lower_bound(repeated_prime_count: int) -> tuple[int, int]:
    """Return a universal denominator/numerator pair for modulus/choice compression.

    Since M>=49^k and there are 2^k classes, the ratio-space compression factor
    M/2^k is at least 49^k/2^k.  We store it as the exact integer pair
    ``(49^k,2^k)`` rather than floating point.
    """
    minimum = repeated_modulus_minimum(repeated_prime_count)
    choices = 1 << repeated_prime_count
    return minimum, choices
