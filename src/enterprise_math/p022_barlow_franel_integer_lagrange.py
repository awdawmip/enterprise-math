"""Integral endpoint Lagrange coordinate for Franel transversality.

The derivative Wronskian module defines

    W_n = F_n F'_(n+1) - F_(n+1) F'_n

and proves

    (n+1)^3 W_n
      = -8 n^2 (n+1) W_(n-1)
        + F_n ((7n+3)F_n + 16n F_(n-1)).

It also proves that

    T_n = F_n ((7n+3)F_n + 16n F_(n-1)) / (n+1)

is an integer.  Therefore the ungauged Lagrange coordinate

    Z_n := (n+1)^2 W_n

is itself integral and satisfies the particularly simple affine recurrence

    Z_n = -8 Z_(n-1) + T_n,     Z_0 = 3.

This removes even the power-of-two denominator carried by the earlier
integrating-factor coordinate Y_n=(-8)^(-n) Z_n.

At an odd prime p>n with p|F_n, recurrence nonadjacency makes F_(n-1) a p-unit.
Hence

    Z_(n-1)
      = n^2 (F_(n-1) F'_n - F_n F'_(n-1))
      = n^2 F_(n-1) F'_n                  (mod p),

and consequently

    F'_n = 0 (mod p)  iff  Z_(n-1) = 0 (mod p).

Thus the first-digit multiple-root problem, and in particular the
``double-stationary`` copy obstruction p^2|F_n and p|F'_n, may be studied using
an ordinary integer sequence.  A sufficient arithmetic theorem would be that
``gcd(F_n,Z_(n-1))`` has no prime factor larger than n.

The Franel recurrence and Straub formal derivative are prior art.  The
Wronskian forcing identity is established in the neighboring P022 module; the
integral Z-coordinate and endpoint packaging here are P022-local consequences.
"""

from __future__ import annotations

from .p022_barlow_franel_derivative_wronskian import (
    derivative_wronskian,
    wronskian_integer_increment,
)
from .p022_barlow_franel_gessel_lucas_copy import (
    _fraction_mod,
    franel_formal_derivative,
)
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def integer_lagrange_coordinate(index: int) -> int:
    """Return Z_n=(n+1)^2 W_n and certify integrality."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be non-negative")
    value = (index + 1) ** 2 * derivative_wronskian(index)
    if value.denominator != 1:
        raise AssertionError("ungauged Franel Lagrange coordinate must be integral")
    return value.numerator


def integer_lagrange_recurrence(index: int) -> tuple[int, int]:
    """Certify Z_n=-8 Z_(n-1)+T_n for n>=1."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    actual = integer_lagrange_coordinate(index)
    predicted = -8 * integer_lagrange_coordinate(index - 1) + wronskian_integer_increment(index)
    if actual != predicted:
        raise AssertionError("integer Lagrange affine recurrence failed")
    return actual, predicted


def endpoint_derivative_lagrange_residues(index: int, prime: int) -> tuple[int, int, int]:
    """At p>n and p|F_n return (F'_n,Z_(n-1),unit_factor) modulo p.

    The exact relation is

        Z_(n-1) = n^2 F_(n-1) F'_n  (mod p),

    and ``unit_factor=n^2 F_(n-1)`` is certified nonzero.
    """
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= index
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be a prime strictly larger than index")
    current = triple_moment_factor(index)
    previous = triple_moment_factor(index - 1) if index > 1 else 2
    if current % prime:
        raise ValueError("prime must divide the Franel endpoint F_n")
    if previous % prime == 0:
        raise AssertionError("adjacent Franel zeros are forbidden in the single-digit range")

    derivative = _fraction_mod(franel_formal_derivative(index), prime)
    lagrange = integer_lagrange_coordinate(index - 1) % prime
    factor = index * index % prime * (previous % prime) % prime
    if factor == 0:
        raise AssertionError("endpoint Lagrange multiplier must be a p-unit")
    if lagrange != factor * derivative % prime:
        raise AssertionError("endpoint derivative/Lagrange residue identity failed")
    return derivative, lagrange, factor


def endpoint_multiple_root_iff_previous_lagrange_zero(index: int, prime: int) -> bool:
    """Certify F'_n=0 mod p iff Z_(n-1)=0 mod p at a Franel p-root."""
    derivative, lagrange, _ = endpoint_derivative_lagrange_residues(index, prime)
    if (derivative == 0) != (lagrange == 0):
        raise AssertionError("endpoint multiple root and Lagrange zero must coincide")
    return derivative == 0
