"""Zero-digit p-adic depth and valuation excess for the Franel sequence.

Delaygue proved p-adic valuation lower bounds for a large class of Apéry-like
factorial-ratio sequences.  Gorodetsky specialized those results to the
sporadic Apéry-like sequences: if

    Z_p={0<=d<p : p divides F_d}

and alpha_p(n) counts the base-p digits of n which belong to Z_p, then the
Franel sequence satisfies

    v_p(F_n) >= alpha_p(n)

for every n>=1 and every prime p.  This is prior art (Delaygue; Gorodetsky,
Corollary 2.5), not a P022 theorem.

P022 packages the nonnegative remainder

    epsilon_p(n)=v_p(F_n)-alpha_p(n) >= 0

as the ``valuation excess``.  Transport identities can therefore be split into
an unavoidable digit-depth baseline plus an excess term.  In particular a
hypothetical defect escape can be analyzed by asking not merely which base-p
digits are Franel zeros, but whether every transported term saturates the
Delaygue lower bound or acquires positive excess.

The exact valuation helper below is intended for bounded research
verification.  The nonnegativity theorem itself is imported as prior art and is
not reproved by finite computation here.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import base_p_digits, franel_zero_digits
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def _require_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be prime")


def franel_zero_digit_count(index: int, prime: int) -> int:
    """Return alpha_p(n), the number of base-p digits lying in Z_p."""
    _require_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    zeros = set(franel_zero_digits(prime))
    return sum(digit in zeros for digit in base_p_digits(index, prime))


def franel_valuation_excess(index: int, prime: int) -> int:
    """Return epsilon_p(n)=v_p(F_n)-alpha_p(n) for bounded exact verification."""
    _require_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    valuation = p_adic_valuation(triple_moment_factor(index), prime)
    baseline = franel_zero_digit_count(index, prime)
    excess = valuation - baseline
    if excess < 0:
        raise AssertionError("Delaygue--Gorodetsky zero-digit lower bound failed")
    return excess


def franel_delaygue_lower_bound_holds(index: int, prime: int) -> bool:
    """Bounded oracle for v_p(F_n)>=alpha_p(n); theorem status is prior art."""
    return franel_valuation_excess(index, prime) >= 0


def two_digit_zero_pattern(index: int, prime: int) -> tuple[int, int, bool, bool]:
    """For n<q^2 return (high,low,high_zero,low_zero)."""
    _require_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime * prime:
        raise ValueError("index must lie in 0..p^2-1")
    high, low = divmod(index, prime)
    zeros = set(franel_zero_digits(prime))
    return high, low, high in zeros, low in zeros


def excess_decomposition(index: int, prime: int) -> tuple[int, int, int]:
    """Return (valuation,zero-digit baseline,nonnegative excess)."""
    _require_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    valuation = p_adic_valuation(triple_moment_factor(index), prime)
    baseline = franel_zero_digit_count(index, prime)
    excess = valuation - baseline
    if excess < 0:
        raise AssertionError("valuation cannot lie below the zero-digit baseline")
    return valuation, baseline, excess
