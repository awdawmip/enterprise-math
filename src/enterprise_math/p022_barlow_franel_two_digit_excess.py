"""Two-digit p-adic valuation calculus for Franel p-Lucas copies.

Let N=a*p+b with 0<=a,b<p.  Three different mechanisms control the first
p-adic layers.

1. High zero, low unit.  If p divides F_a exactly once and F_b is a p-unit,
   Straub's Gessel--Lucas congruence gives

       F_(a p+b) = F_b F_a                              (mod p^2),

   because the correction term already contains the factor p*F_a.  Therefore

       v_p(F_(a p+b))=1.

2. Low zero, high unit.  If p divides F_b exactly once, write

       u_b=F_b/p,  d_b=F'_b  (mod p).

   Then

       F_(a p+b)/p = F_a (u_b+a d_b)                   (mod p).

   Hence there is at most one high unit digit a modulo p for which the copied
   depth can rise above one.

3. Two zero digits.  Delaygue's valuation theorem, as specialized by
   Gorodetsky to the sporadic Apéry-like sequences, gives

       v_p(F_(a p+b)) >= 2

   whenever both a and b lie in the Franel zero alphabet.  P022 records the
   difference between the actual valuation and this compulsory digit baseline
   as valuation excess.

A particularly useful transport residual follows when the high digit a is a
simple zero and 1<=b<p.  Put

    R(a,b)=v_p(F_(ap+b))-1-v_p(F_(ap+b-1)).

If b is a unit, Gessel--Lucas gives the first valuation as one while the
predecessor still contains the high zero digit, so Delaygue gives R<=-1.
If b is also a zero, then b-1 is a unit by single-digit nonadjacency;
Gessel--Lucas makes the predecessor depth exactly one and Delaygue gives

    R(a,b)=epsilon_p(ap+b)>=0.

Consequently

    R(a,b)=0

is possible exactly in the two-zero-digit branch with zero valuation excess.
This is the local calculus needed by the secondary quadratic Barlow transport.

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
    """Return (N,actual quotient,predicted quotient) and prove exact depth one."""
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
    """Return (N,quotient residue,exceptional high multiplier)."""
    index = two_digit_index(high, low, prime)
    if p_adic_valuation(triple_moment_factor(low), prime) != 1:
        raise ValueError("low digit must be a simple Franel p-zero")
    high_value = 1 if high == 0 else triple_moment_factor(high)
    if high_value % prime == 0:
        raise ValueError("high digit must be a Franel p-unit")
    if high == 0:
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
    """Return (N,alpha_p(N)) and certify the Delaygue baseline is exactly two."""
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


def simple_high_zero_transport_residual(
    high: int,
    low: int,
    prime: int,
) -> tuple[str, int, int]:
    """Classify R=v_p(F_(ap+b))-1-v_p(F_(ap+b-1)) for 1<=b<p.

    Returns `(branch,residual,excess)`.  For a unit low digit, `branch` is
    ``unit-low``, the excess field is -1 (not used), and residual is strictly
    negative.  For a zero low digit, `branch` is ``two-zero``, residual equals
    the nonnegative Delaygue valuation excess of F_(ap+b).
    """
    _require_prime(prime)
    if not 1 <= low < prime:
        raise ValueError("low digit must lie in 1..p-1 so the high digit persists in N-1")
    if p_adic_valuation(triple_moment_factor(high), prime) != 1:
        raise ValueError("high digit must be a simple Franel p-zero")

    index = two_digit_index(high, low, prime)
    previous = index - 1
    low_zero = franel_residue(low, prime) == 0
    if not low_zero:
        simple_high_zero_unit_low_residue(high, low, prime)
        valuation = p_adic_valuation(triple_moment_factor(index), prime)
        previous_valuation, previous_baseline, _ = excess_decomposition(previous, prime)
        if valuation != 1 or previous_baseline < 1 or previous_valuation < 1:
            raise AssertionError("unit-low branch must keep the high zero in both adjacent copies")
        residual = valuation - 1 - previous_valuation
        if residual >= 0:
            raise AssertionError("unit-low simple-high residual must be strictly negative")
        return "unit-low", residual, -1

    if franel_residue(low - 1, prime) == 0:
        raise AssertionError("single-digit Franel zero digits cannot be adjacent")
    # N-1 has the same simple high zero and a unit low digit, hence exact depth one.
    simple_high_zero_unit_low_residue(high, low - 1, prime)
    previous_valuation = p_adic_valuation(triple_moment_factor(previous), prime)
    if previous_valuation != 1:
        raise AssertionError("predecessor in the two-zero branch must have exact depth one")
    valuation, baseline, excess = two_zero_digit_excess(high, low, prime)
    if baseline != 2:
        raise AssertionError("two-zero branch must have digit baseline two")
    residual = valuation - 1 - previous_valuation
    if residual != excess:
        raise AssertionError("transport residual must equal the two-zero valuation excess")
    return "two-zero", residual, excess
