"""Graded Franel p-adic basins from Delaygue's valuation theorem.

Delaygue proved, for the Franel sequence F_n=sum_k C(n,k)^3, that

    v_p(F_N) >= alpha_p(F,N),

where alpha_p(F,N) counts base-p digits d of N for which p|F_d.

This module does not re-prove that prior-art theorem.  It packages its exact
combinatorial consequences for the P022 zero-digit/precision route:
- the zero-digit multiplicity is a finite-state lower bound on p-adic depth;
- its distribution on 0..p^L-1 is exactly binomial;
- a forced midpoint digit repeated L times gives
      v_p(F_((p^L-1)/2)) >= L
  for p=5 or 7 (mod 8);
- for p=5 or 23 (mod 24), p>5, every odd level of that tower is again on the
  composite A-boundary because p^L-2 is divisible by three.
"""

from __future__ import annotations

from math import comb

from .p022_barlow_franel_half_index import (
    half_index,
    half_index_is_forced_zero,
)
from .p022_barlow_franel_lucas_rank import (
    base_p_digits,
    franel_zero_digit_count,
    franel_zero_digits,
)
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 1
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be prime")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def zero_digit_multiplicity(value: int, prime: int) -> int:
    """Delaygue's alpha_p(F,N): # base-p digits lying in the zero alphabet."""
    _require_prime(prime)
    _require_natural("value", value)
    zero_set = set(franel_zero_digits(prime))
    return sum(digit in zero_set for digit in base_p_digits(value, prime))


def delaygue_valuation_lower_bound(value: int, prime: int) -> int:
    """The prior-art guaranteed lower exponent v_p(F_N)>=alpha_p(F,N)."""
    return zero_digit_multiplicity(value, prime)


def alpha_profile_count(prime: int, digit_length: int, alpha: int) -> int:
    """Exact # of N in 0..p^L-1 having exactly alpha zero digits."""
    _require_prime(prime)
    _require_natural("digit_length", digit_length)
    _require_natural("alpha", alpha)
    if alpha > digit_length:
        return 0
    zero_count = franel_zero_digit_count(prime)
    nonzero_count = prime - zero_count
    return (
        comb(digit_length, alpha)
        * (zero_count**alpha)
        * (nonzero_count ** (digit_length - alpha))
    )


def alpha_profile(prime: int, digit_length: int) -> tuple[int, ...]:
    """Exact finite distribution of Delaygue lower-bound exponents."""
    return tuple(
        alpha_profile_count(prime, digit_length, alpha)
        for alpha in range(digit_length + 1)
    )


def guaranteed_valuation_tail_count(
    prime: int, digit_length: int, minimum_valuation: int
) -> int:
    """# indices whose digit state alone guarantees v_p(F_N)>=minimum_valuation."""
    _require_natural("minimum_valuation", minimum_valuation)
    if minimum_valuation > digit_length:
        return 0
    return sum(alpha_profile(prime, digit_length)[minimum_valuation:])


def total_alpha_load(prime: int, digit_length: int) -> int:
    """Exact sum of alpha_p(F,N) over the complete p^L block."""
    _require_prime(prime)
    _require_natural("digit_length", digit_length)
    zero_count = franel_zero_digit_count(prime)
    if digit_length == 0:
        return 0
    return digit_length * zero_count * (prime ** (digit_length - 1))


def average_valuation_lower_bound_fraction(
    prime: int, digit_length: int
) -> tuple[int, int]:
    """Block-average lower bound: mean v_p(F_N)>=L*z_p/p."""
    _require_prime(prime)
    _require_natural("digit_length", digit_length)
    return digit_length * franel_zero_digit_count(prime), prime


def repeated_midpoint_index(prime: int, digit_length: int) -> int:
    """Number with L repeated midpoint digits: (p^L-1)/2."""
    _require_prime(prime)
    _require_natural("digit_length", digit_length)
    if prime == 2:
        raise ValueError("midpoint requires an odd prime")
    if digit_length == 0:
        return 0
    midpoint = half_index(prime)
    value = midpoint * ((prime**digit_length - 1) // (prime - 1))
    expected = (prime**digit_length - 1) // 2
    if value != expected:
        raise AssertionError("repeated midpoint digits must equal (p^L-1)/2")
    if base_p_digits(value, prime) != (midpoint,) * digit_length:
        raise AssertionError("repeated midpoint base-p expansion failed")
    return value


def forced_midpoint_tower_lower_bound(prime: int, digit_length: int) -> tuple[int, int]:
    """Return (N_L,L) with the certified bound v_p(F_NL)>=L."""
    _require_prime(prime)
    _require_natural("digit_length", digit_length)
    if prime == 2 or not half_index_is_forced_zero(prime):
        raise ValueError("prime must lie in a forced midpoint residue class")
    value = repeated_midpoint_index(prime, digit_length)
    alpha = zero_digit_multiplicity(value, prime)
    if alpha != digit_length:
        raise AssertionError("every repeated midpoint digit must be a zero digit")
    return value, alpha


def odd_level_composite_boundary_tower(
    prime: int, digit_length: int
) -> tuple[int, int, int]:
    """Composite-boundary tower for p=5 or 23 mod 24 and odd L.

    Returns (N_L, boundary=2*N_L-1, valuation_lower_bound=L).
    """
    _require_prime(prime)
    _require_natural("digit_length", digit_length)
    if prime <= 5 or prime % 24 not in (5, 23):
        raise ValueError("prime must exceed five and lie in 5 or 23 mod 24")
    if digit_length == 0 or digit_length % 2 == 0:
        raise ValueError("digit_length must be positive and odd")
    value, lower = forced_midpoint_tower_lower_bound(prime, digit_length)
    boundary = 2 * value - 1
    if boundary != prime**digit_length - 2:
        raise AssertionError("tower boundary must equal p^L-2")
    if boundary <= 3 or boundary % 3:
        raise AssertionError("odd tower level must lie on a composite boundary")
    return value, boundary, lower
