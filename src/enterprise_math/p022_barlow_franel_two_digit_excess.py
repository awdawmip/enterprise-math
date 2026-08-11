"""Two-digit p-adic valuation calculus for Franel p-Lucas copies.

Let N=a*p+b with 0<=a,b<p.  Three different mechanisms control the first
p-adic layers.

1. High zero, low unit.  If p divides F_a exactly once and F_b is a p-unit,
   Straub's Gessel--Lucas congruence gives

       F_(a p+b) = F_b F_a                              (mod p^2),

   because the correction term already contains the factor p*F_a.  Therefore

       v_p(F_(a p+b))=1.

   This is an orientation-sensitive exact theorem: a simple zero in the high
   digit is copied with exact depth one across every unit low digit.

2. Low zero, high unit.  If p divides F_b exactly once, write

       u_b=F_b/p,  d_b=F'_b  (mod p).

   Then

       F_(a p+b)/p = F_a (u_b+a d_b)                   (mod p).

   Hence there is at most one high unit digit a modulo p for which the copied
   depth can rise above one.  This is Straub's first-jet phenomenon packaged
   by the existing P022 Gessel--Lucas module.

3. Two zero digits.  Delaygue's valuation theorem, as specialized by
   Gorodetsky to the sporadic Apéry-like sequences, gives

       v_p(F_(a p+b)) >= 2

   whenever both a and b lie in the Franel zero alphabet.  P022 records the
   difference between the actual valuation and this compulsory digit baseline
   as valuation excess.

The Gessel--Lucas and Delaygue--Gorodetsky results are prior art.  The purpose
of this module is to expose their asymmetric two-digit interaction as a typed
transport tool for the Barlow defect problem.
"""

from __future__ import annotations

from .p022_barlow_franel_gessel_lucas_copy import (
    franel_gessel_lucas_mod_square,
    simple_zero_copy_linear_residue,
)
from .p022_barlow_franel_lucas_rank import franel_residue
from .p022_barlow_franel_reflection_first_jet import simple_zero_exceptional_multiplier
from .p022_barlow_franel_zero_digit_depth import (
    excess_decomposition,
    franel_zero_digit_count,
)
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def _require_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def two_digit_index(high: int, low: int, prime: int) -> int:
    _require_prime(prime)
    for name, value in (("high", high), ("low", low)):
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < prime:
            raise ValueError(f"{name} digit must lie in 0..p-1")
    return high * prime + low


def simple_high_zero_unit_low_residue(
    high: int,
    low: int,
    prime: int,
) -> tuple[int, int, int]:
    """Return (N,actual quotient,predicted quotient) and prove exact depth one.

    Assumptions: v_p(F_high)=1 and F_low is a p-unit.  The predicted quotient is
    F_low*(F_high/p) modulo p.
    """
    index = two_digit_index(high, low, prime)
    if p_adic_valuation(triple_moment_factor(high), prime) != 1:
        raise ValueError("high digit must be a simple Franel p-zero")
    low_value = 1 if low == 0 else triple_moment_factor(low)
    if low_value % prime == 0:
        raise ValueError("low digit must be a Franel p-unit")

    actual_square, predicted_square = franel_gessel_lucas_mod_square(
        low,
        prime,
        high,
    )
    if actual_square != predicted_square or actual_square % prime:
        raise AssertionError("high-zero copy must remain p-divisible")
    actual = (actual_square // prime) % prime
    high_unit = (triple_moment_factor(high) // prime) % prime
    predicted = (low_value % prime) * high_unit % prime
    if actual != predicted or actual == 0:
        raise AssertionError("simple high zero with unit low digit must stay depth one")
    return index, actual, predicted


def simple_low_zero_unit_high_residue(
    low: int,
    high: int,
    prime: int,
) -> tuple[int, int, int | None]:
    """Return (N,quotient residue,exceptional high multiplier).

    Assumptions: v_p(F_low)=1 and F_high is a p-unit.  The quotient residue is
    nonzero except possibly at the unique exceptional multiplier returned by
    `simple_zero_exceptional_multiplier`.
    """
    index = two_digit_index(high, low, prime)
    if p_adic_valuation(triple_moment_factor(low), prime) != 1:
        raise ValueError("low digit must be a simple Franel p-zero")
    high_value = 1 if high == 0 else triple_moment_factor(high)
    if high_value % prime == 0:
        raise ValueError("high digit must be a Franel p-unit")
    if high == 0:
        # N=low itself, so the copied quotient is just the source unit.
        quotient = (triple_moment_factor(low) // prime) % prime
    else:
        quotient, predicted = simple_zero_copy_linear_residue(low, prime, high)
        if quotient != predicted:
            raise AssertionError("low-zero first-jet residue changed")
    exceptional = simple_zero_exceptional_multiplier(prime, low)
    if quotient == 0 and exceptional != high:
        raise AssertionError("only the exceptional multiplier can raise the low-zero copy depth")
    if quotient != 0 and exceptional == high:
        raise AssertionError("the exceptional multiplier must annihilate the first quotient")
    return index, quotient, exceptional


def two_zero_digit_baseline(high: int, low: int, prime: int) -> tuple[int, int]:
    """Return (N,alpha_p(N)) and certify the Delaygue baseline is at least two."""
    index = two_digit_index(high, low, prime)
    if franel_residue(high, prime) != 0 or franel_residue(low, prime) != 0:
        raise ValueError("both base-p digits must be Franel zero digits")
    baseline = franel_zero_digit_count(index, prime)
    if baseline != 2:
        raise AssertionError("a two-digit zero pair must contribute exactly two zero digits")
    return index, baseline


def two_zero_digit_excess(high: int, low: int, prime: int) -> tuple[int, int, int]:
    """Bounded exact oracle returning (valuation,baseline,excess) for two zero digits."""
    index, baseline = two_zero_digit_baseline(high, low, prime)
    valuation, checked_baseline, excess = excess_decomposition(index, prime)
    if checked_baseline != baseline or valuation < 2 or excess < 0:
        raise AssertionError("two-zero digit valuation lies below the Delaygue baseline")
    return valuation, baseline, excess
