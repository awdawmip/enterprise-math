"""Franel p-Lucas structure and primitive-divisor rank consequences.

For prime p and base-p digits n_i, Lucas' binomial theorem gives

    F_n = sum_k C(n,k)^3 = prod_i F_(n_i)  (mod p).

Consequences:
- a primitive prime divisor p of F_n must satisfy p>n;
- the first index r_p with p|F_(r_p), when it exists, lies in 1..p-1;
- if p is primitive at n, then p also divides F_(n+p), so finite private
  markers never stay private forever;
- p divides no Franel term iff none of F_1,...,F_(p-1) vanish mod p.

These are standard Lucas-structure consequences; this module uses them to
sharpen the P022 primitive-defect criterion.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import primes_through
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
        raise ValueError("prime must exceed one")
    if prime not in primes_through(prime):
        raise ValueError("value must be prime")


def base_p_digits(value: int, prime: int) -> tuple[int, ...]:
    _require_prime(prime)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("value must be a non-negative integer")
    if value == 0:
        return (0,)
    digits = []
    remaining = value
    while remaining:
        digits.append(remaining % prime)
        remaining //= prime
    return tuple(digits)


def franel_lucas_residue(value: int, prime: int) -> int:
    """Product of digit Franel values modulo p."""
    digits = base_p_digits(value, prime)
    result = 1
    for digit in digits:
        result = result * (triple_moment_factor(digit) % prime) % prime
    return result


def franel_residue(value: int, prime: int) -> int:
    _require_prime(prime)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("value must be a non-negative integer")
    return triple_moment_factor(value) % prime


def lucas_factorization_holds(value: int, prime: int) -> bool:
    return franel_residue(value, prime) == franel_lucas_residue(value, prime)


def franel_zero_digits(prime: int) -> tuple[int, ...]:
    """Nonzero base-p digits d with F_d=0 mod p."""
    _require_prime(prime)
    return tuple(
        digit
        for digit in range(1, prime)
        if triple_moment_factor(digit) % prime == 0
    )


def franel_rank_of_apparition(prime: int) -> int | None:
    """First positive index divisible by p, or None for a Lucas-Type-I prime."""
    zeros = franel_zero_digits(prime)
    return zeros[0] if zeros else None


def primitive_divisor_requires_large_prime(segment: int, prime: int) -> bool:
    """If p is primitive at F_n, certify the necessary inequality p>n."""
    _require_prime(prime)
    if isinstance(segment, bool) or not isinstance(segment, int) or segment <= 0:
        raise ValueError("segment must be a positive integer")
    if triple_moment_factor(segment) % prime:
        raise ValueError("prime does not divide the declared Franel term")
    if any(triple_moment_factor(previous) % prime == 0 for previous in range(1, segment)):
        raise ValueError("prime is not primitive at the declared segment")
    if prime <= segment:
        raise AssertionError("p-Lucas forces a smaller zero digit when p<=n")
    return True


def primitive_marker_recurrence_index(segment: int, prime: int) -> int:
    """A primitive p at n necessarily reappears at n+p by p-Lucas."""
    if not primitive_divisor_requires_large_prime(segment, prime):
        raise AssertionError("primitive divisor prerequisite failed")
    later = segment + prime
    if franel_lucas_residue(later, prime) != 0:
        raise AssertionError("base-p digits (n,1) must force a later zero")
    return later


def lucas_divisibility_from_digits(value: int, prime: int) -> bool:
    """Divisibility iff at least one base-p digit is a zero digit."""
    _require_prime(prime)
    digits = base_p_digits(value, prime)
    zero_set = set(franel_zero_digits(prime))
    predicted = any(digit in zero_set for digit in digits)
    actual = franel_residue(value, prime) == 0
    if predicted != actual:
        raise AssertionError("Franel p-Lucas digit-zero criterion failed")
    return actual
