"""Franel p-Lucas structure, rank consequences, and divisibility basins.

For prime p and base-p digits n_i, Lucas' binomial theorem gives

    F_n = sum_k C(n,k)^3 = prod_i F_(n_i)  (mod p).

The p-Lucas property is prior art; the reflection congruence

    F_d = (-8)^d F_(p-1-d)  (mod p),  0 <= d < p,

for odd primes is also prior art (Jarvis--Verrill, Lemma 2.6).
The module packages consequences needed by the P022 defect/precision route:

- p|F_n iff a base-p digit of n is a zero digit modulo p;
- if a first zero r_p exists, then it is the least zero digit;
- the zero-digit set is reflection-symmetric, hence r_p <= (p-1)/2;
- therefore every odd primitive prime divisor p of F_n satisfies p >= 2n+1;
- if p is primitive at n, every later index whose base-p expansion contains
  digit n is also divisible by p, so a primitive marker is never permanently
  private;
- if z_p digit values are zero modulo p, then exactly (p-z_p)^L indices in
  0..p^L-1 remain nonzero.  Thus any nonempty zero-digit set generates a
  density-one divisibility basin along p-power blocks.

No priority claim is made for the Lucas or reflection congruences themselves.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import primes_through
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
        raise ValueError("prime must exceed one")
    if prime not in primes_through(prime):
        raise ValueError("value must be prime")


def _require_odd_prime(prime: int) -> None:
    _require_prime(prime)
    if prime == 2:
        raise ValueError("odd prime required")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _franel_factor(value: int) -> int:
    """Franel factor including the Lucas unit F_0=1."""
    _require_natural("value", value)
    return 1 if value == 0 else triple_moment_factor(value)


def base_p_digits(value: int, prime: int) -> tuple[int, ...]:
    _require_prime(prime)
    _require_natural("value", value)
    if value == 0:
        return (0,)
    digits = []
    remaining = value
    while remaining:
        digits.append(remaining % prime)
        remaining //= prime
    return tuple(digits)


def franel_lucas_residue(value: int, prime: int) -> int:
    """Product of digit Franel values modulo p, with F_0=1."""
    digits = base_p_digits(value, prime)
    result = 1
    for digit in digits:
        result = result * (_franel_factor(digit) % prime) % prime
    return result


def franel_residue(value: int, prime: int) -> int:
    _require_prime(prime)
    _require_natural("value", value)
    return _franel_factor(value) % prime


def lucas_factorization_holds(value: int, prime: int) -> bool:
    return franel_residue(value, prime) == franel_lucas_residue(value, prime)


def franel_zero_digits(prime: int) -> tuple[int, ...]:
    """Nonzero base-p digits d with F_d=0 mod p."""
    _require_prime(prime)
    return tuple(
        digit
        for digit in range(1, prime)
        if _franel_factor(digit) % prime == 0
    )


def franel_zero_digit_count(prime: int) -> int:
    return len(franel_zero_digits(prime))


def franel_rank_of_apparition(prime: int) -> int | None:
    """First positive index divisible by p, or None if no zero digit exists."""
    zeros = franel_zero_digits(prime)
    return zeros[0] if zeros else None


def franel_reflection_residue_holds(digit: int, prime: int) -> bool:
    """Jarvis--Verrill reflection F_d=(-8)^d F_(p-1-d) mod p."""
    _require_odd_prime(prime)
    _require_natural("digit", digit)
    if digit >= prime:
        raise ValueError("digit must be smaller than prime")
    left = _franel_factor(digit) % prime
    right = (
        pow(-8, digit, prime) * (_franel_factor(prime - 1 - digit) % prime)
    ) % prime
    return left == right


def franel_zero_digit_reflection_holds(prime: int) -> bool:
    """Certify d is a zero digit iff p-1-d is a zero digit."""
    _require_odd_prime(prime)
    zeros = set(franel_zero_digits(prime))
    for digit in range(0, prime):
        reflected_zero = prime - 1 - digit in zeros
        digit_zero = digit in zeros
        if digit_zero != reflected_zero:
            raise AssertionError("Franel zero-digit reflection symmetry failed")
        if not franel_reflection_residue_holds(digit, prime):
            raise AssertionError("Franel reflection congruence failed")
    return True


def franel_rank_reflection_bound(prime: int) -> tuple[int, int] | None:
    """Return (r_p,(p-1)/2) and certify r_p <= (p-1)/2 when r_p exists."""
    _require_odd_prime(prime)
    rank = franel_rank_of_apparition(prime)
    if rank is None:
        return None
    reflected = prime - 1 - rank
    if _franel_factor(reflected) % prime != 0:
        raise AssertionError("reflection of the first zero must also be a zero")
    bound = (prime - 1) // 2
    if rank > bound:
        raise AssertionError("reflection symmetry forces r_p <= (p-1)/2")
    return rank, bound


def franel_midpoint_zero_criterion(prime: int) -> bool:
    """Certify the prior-art midpoint criterion p|F_((p-1)/2) iff p=5,7 mod 8."""
    _require_odd_prime(prime)
    midpoint = (prime - 1) // 2
    actual = franel_residue(midpoint, prime) == 0
    predicted = prime % 8 in (5, 7)
    if actual != predicted:
        raise AssertionError("Franel midpoint congruence criterion failed")
    return actual


def primitive_divisor_requires_large_prime(segment: int, prime: int) -> bool:
    """Certify the strengthened necessary size bound for a primitive divisor.

    The p-Lucas digit argument first gives p>n.  For odd p, the
    Jarvis--Verrill reflection of the first zero then gives p>=2n+1.
    The sole even primitive case is p=2 at F_1.
    """
    _require_prime(prime)
    if isinstance(segment, bool) or not isinstance(segment, int) or segment <= 0:
        raise ValueError("segment must be a positive integer")
    if _franel_factor(segment) % prime:
        raise ValueError("prime does not divide the declared Franel term")
    if any(_franel_factor(previous) % prime == 0 for previous in range(1, segment)):
        raise ValueError("prime is not primitive at the declared segment")
    if prime <= segment:
        raise AssertionError("p-Lucas forces a smaller zero digit when p<=n")
    if prime == 2:
        if segment != 1:
            raise AssertionError("2 is primitive only at F_1")
        return True
    if prime < 2 * segment + 1:
        raise AssertionError(
            "Franel reflection symmetry forces an odd primitive p>=2n+1"
        )
    return True


def primitive_marker_recurrence_index(segment: int, prime: int) -> int:
    """Return the first simple repeated marker n+p forced by p-Lucas."""
    if not primitive_divisor_requires_large_prime(segment, prime):
        raise AssertionError("primitive divisor prerequisite failed")
    later = segment + prime
    if franel_lucas_residue(later, prime) != 0:
        raise AssertionError("base-p digits containing n must force a later zero")
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


def lucas_block_nonzero_count(prime: int, digit_length: int) -> int:
    """Exact # of N in 0..p^L-1 with F_N nonzero modulo p."""
    _require_prime(prime)
    _require_natural("digit_length", digit_length)
    allowed_digits = prime - franel_zero_digit_count(prime)
    return allowed_digits**digit_length


def lucas_block_divisible_count(prime: int, digit_length: int) -> int:
    """Exact # of N in 0..p^L-1 with p|F_N."""
    _require_prime(prime)
    _require_natural("digit_length", digit_length)
    domain = prime**digit_length
    return domain - lucas_block_nonzero_count(prime, digit_length)


def lucas_block_counts(prime: int, digit_length: int) -> tuple[int, int, int]:
    """Return (domain, nonzero, divisible) and certify the partition."""
    domain = prime**digit_length
    nonzero = lucas_block_nonzero_count(prime, digit_length)
    divisible = lucas_block_divisible_count(prime, digit_length)
    if nonzero + divisible != domain:
        raise AssertionError("p-Lucas block counts must partition the domain")
    return domain, nonzero, divisible


def nonzero_block_ratio_upper_pair(prime: int, digit_length: int) -> tuple[int, int]:
    """Exact fraction numerator/denominator for nonzero density on a p^L block."""
    domain, nonzero, _ = lucas_block_counts(prime, digit_length)
    return nonzero, domain
