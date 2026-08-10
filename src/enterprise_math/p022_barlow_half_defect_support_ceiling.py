"""Prime-factor ceiling for the canonical half-index A-elimination support.

For a positive integer x, the recursive central-binomial basis expansion uses
an odd prime q only through the adjacent indices

    h=(q+1)/2 and h-1,

then recurses into h.  Therefore every nontrivial index in the expansion is at
most (P_odd(x)+1)/2, where P_odd(x) is the largest odd prime factor of x.

For the P022 half-defect family p=5 or 23 (mod 24), m=(p-1)/2 and p-2 is
composite.  The canonical relation

    A_m = product_(j<m) A_j^alpha_j

has support contained in

    {m-1} union {1,...,B_p},

where

    B_p=max(ceil_A(m), ceil_A(p-2)).

The isolated point m-1 is always Franel-nonzero modulo a forced-midpoint prime
because F_m=0 and adjacent Franel zeros are impossible.  Hence if the Franel
rank of apparition r_p exceeds B_p, support avoidance follows automatically.

This is a sufficient rank certificate, not a characterization: r_p<=B_p may
still be support-safe because the actual A-support tree is sparse.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_franel_lucas_rank import franel_rank_of_apparition
from .p022_barlow_half_defect_obstructions import half_defect_support_zero_hits
from .p022_barlow_low_order_defect_reduction import (
    _factor_integer,
    composite_A_relation_exponents,
    integer_in_central_binomial_basis,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def largest_odd_prime_factor(value: int) -> int:
    """Largest odd prime factor, or 1 for a power of two / value 1."""
    _require_positive("value", value)
    odd_primes = [prime for prime, _ in _factor_integer(value) if prime % 2]
    return max(odd_primes, default=1)


def central_binomial_basis_support_ceiling(value: int) -> int:
    """A proved envelope for every index in the canonical A-basis expansion."""
    _require_positive("value", value)
    largest = largest_odd_prime_factor(value)
    ceiling = 1 if largest == 1 else (largest + 1) // 2
    expansion = integer_in_central_binomial_basis(value)
    if expansion and max(index for index, _ in expansion) > ceiling:
        raise AssertionError("recursive prime-halving support exceeded its ceiling")
    return ceiling


def half_defect_low_support_ceiling(prime: int) -> int:
    """B_p for the p=5,23 mod 24 composite-boundary midpoint family."""
    midpoint, _ = composite_boundary_half_witness(prime)
    return max(
        central_binomial_basis_support_ceiling(midpoint),
        central_binomial_basis_support_ceiling(prime - 2),
    )


def half_defect_support_respects_ceiling(prime: int) -> bool:
    """Every support index is either m-1 or at most B_p."""
    midpoint, _ = composite_boundary_half_witness(prime)
    ceiling = half_defect_low_support_ceiling(prime)
    support = tuple(index for index, _ in composite_A_relation_exponents(midpoint))
    if any(index != midpoint - 1 and index > ceiling for index in support):
        raise AssertionError("half-defect support escaped the prime-factor ceiling")
    return True


def rank_ceiling_is_automatic_safe(prime: int) -> bool:
    """Whether r_p>B_p, a sufficient certificate for support avoidance."""
    midpoint, _ = composite_boundary_half_witness(prime)
    rank = franel_rank_of_apparition(prime)
    if rank is None:
        raise AssertionError("forced midpoint prime must have a Franel zero")
    ceiling = half_defect_low_support_ceiling(prime)
    if rank <= ceiling:
        return False
    if rank >= midpoint:
        # Primitive midpoint is included: only m is zero on the left side.
        pass
    if half_defect_support_zero_hits(prime):
        raise AssertionError("rank above the support ceiling must force avoidance")
    return True


def support_ceiling_profile(prime: int) -> tuple[int, int, int, bool]:
    """Return (midpoint, rank, low-support ceiling, automatic-safe flag)."""
    midpoint, _ = composite_boundary_half_witness(prime)
    rank = franel_rank_of_apparition(prime)
    if rank is None:
        raise AssertionError("forced midpoint prime must have a rank")
    ceiling = half_defect_low_support_ceiling(prime)
    return midpoint, rank, ceiling, rank_ceiling_is_automatic_safe(prime)
