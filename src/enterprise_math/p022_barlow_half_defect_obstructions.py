"""Exact obstruction split for the half-index Franel defect conjecture.

For primes p>5 with p=5 or 23 (mod 24), let m=(p-1)/2.  The half-index
theorem gives p|F_m and 2m-1=p-2 is composite, so the canonical pure Franel
defect D_m is defined.

The empirical one-unit statement v_p(D_m)=1 separates into two logically
independent issues:

1. support avoidance: none of the earlier Franel factors used by the canonical
   central-binomial elimination is zero modulo p;
2. simple midpoint lift: F_m is divisible by p but not by p^2.

If support avoidance holds, every eliminated earlier factor is a p-adic unit,
so v_p(D_m)=v_p(F_m) exactly.  This module provides integer-only mod-p and
mod-p^2 oracles for both obstructions without constructing huge Franel values.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
)


def _require_prime_modulus(prime: int) -> None:
    # composite_boundary_half_witness performs the full odd-prime/family check
    composite_boundary_half_witness(prime)


def franel_recurrence_table_mod(prime: int, modulus: int, stop: int) -> tuple[int, ...]:
    """Return F_0,...,F_stop modulo modulus by the exact Franel recurrence.

    Intended use has modulus p or p^2 and stop<p, so every (k+1)^2 denominator
    is a unit modulo the modulus.
    """
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 2:
        raise ValueError("prime must be an odd integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1:
        raise ValueError("modulus must exceed one")
    if isinstance(stop, bool) or not isinstance(stop, int) or not 0 <= stop < prime:
        raise ValueError("stop must lie in 0..p-1")
    if stop == 0:
        return (1 % modulus,)

    values = [1 % modulus, 2 % modulus]
    for k in range(1, stop):
        numerator = (
            (7 * k * k + 7 * k + 2) * values[k]
            + 8 * k * k * values[k - 1]
        ) % modulus
        denominator = ((k + 1) * (k + 1)) % modulus
        try:
            inverse = pow(denominator, -1, modulus)
        except ValueError as exc:  # pragma: no cover - guard for misuse
            raise ValueError("recurrence denominator must be invertible") from exc
        values.append(numerator * inverse % modulus)
    return tuple(values)


def half_defect_support(prime: int) -> tuple[int, ...]:
    """Indices of earlier Franel factors in the canonical A-elimination."""
    segment, _ = composite_boundary_half_witness(prime)
    exponents = composite_A_relation_exponents(segment)
    return tuple(index for index, _ in exponents)


def half_defect_support_zero_hits(prime: int) -> tuple[int, ...]:
    """Canonical A-elimination support indices j with p|F_j."""
    _require_prime_modulus(prime)
    support = half_defect_support(prime)
    if not support:
        return ()
    table = franel_recurrence_table_mod(prime, prime, max(support))
    return tuple(index for index in support if table[index] == 0)


def support_avoidance_holds(prime: int) -> bool:
    return not half_defect_support_zero_hits(prime)


def half_index_mod_prime_square(prime: int) -> int:
    """Return F_((p-1)/2) modulo p^2 by recurrence only."""
    segment, _ = composite_boundary_half_witness(prime)
    modulus = prime * prime
    return franel_recurrence_table_mod(prime, modulus, segment)[segment]


def half_index_lift_quotient(prime: int) -> int:
    """Return q_p^F = F_((p-1)/2)/p modulo p.

    The half-index theorem guarantees divisibility by p, so the canonical
    residue modulo p^2 is a multiple of p.
    """
    residue = half_index_mod_prime_square(prime)
    if residue % prime:
        raise AssertionError("half-index theorem must force p-divisibility")
    return (residue // prime) % prime


def simple_midpoint_lift_holds(prime: int) -> bool:
    """Whether v_p(F_((p-1)/2)) is exactly one."""
    return half_index_lift_quotient(prime) != 0


def canonical_defect_valuation_if_support_avoids(prime: int) -> int:
    """Return the exact v_p(D_m) when support avoidance is certified.

    Under avoidance, all earlier F_j in the rational defect denominator and
    numerator correction are p-units, so only F_m contributes.  Since this
    helper reads F_m modulo p^2, it distinguishes valuation one from valuation
    at least two; values >=2 are returned as 2 (a lower-bound marker), not as a
    claimed exact higher valuation.
    """
    if not support_avoidance_holds(prime):
        raise ValueError("canonical support meets an earlier Franel zero")
    return 1 if simple_midpoint_lift_holds(prime) else 2


def half_defect_obstruction_profile(prime: int) -> tuple[tuple[int, ...], int, bool]:
    """Return (support_zero_hits, lift_quotient_mod_p, one_unit_certified)."""
    hits = half_defect_support_zero_hits(prime)
    quotient = half_index_lift_quotient(prime)
    one_unit = not hits and quotient != 0
    return hits, quotient, one_unit
