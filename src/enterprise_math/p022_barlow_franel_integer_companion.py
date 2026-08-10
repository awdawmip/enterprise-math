"""Integer normalization of the P022 Franel midpoint-offset companion.

This is the same theorem family as ``p022_barlow_franel_midpoint_offset``.
It removes rational denominators from the universal companion by setting

    H_d = 8^(d-1) ((2d-1)!!)^2 G_d  (d>=1),  H_0=0.

Then

    H_0=0, H_1=1,
    H_(d+1)=-(28 d^2+1) H_d + 8(2d-1)^4 H_(d-1).

For a forced-midpoint prime p=5 or 7 (mod 8), m=(p-1)/2, and 0<d<m,
the scaling factor is a p-adic unit.  Hence

    p | F_(m-d)  iff  p | H_d.

Thus the full forced-midpoint Franel zero alphabet can be recovered from one
fixed integer recurrence, with no Fraction or modular division in the query.
"""

from __future__ import annotations

from functools import lru_cache

from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_franel_midpoint_offset import midpoint_companion_fraction
from .p022_barlow_franel_lucas_rank import franel_zero_digits
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_offset(offset: int) -> None:
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")


def _require_forced_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
        or not half_index_is_forced_zero(prime)
    ):
        raise ValueError("prime must be an odd prime in 5 or 7 modulo 8")


def odd_double_factorial(offset: int) -> int:
    """Return (2d-1)!!, with (-1)!!=1 at d=0 by convention."""
    _require_offset(offset)
    result = 1
    for value in range(1, 2 * offset, 2):
        result *= value
    return result


def integer_companion_scale(offset: int) -> int:
    """S_d = 8^(d-1)((2d-1)!!)^2 for d>=1; S_0=1."""
    _require_offset(offset)
    if offset == 0:
        return 1
    double_factorial = odd_double_factorial(offset)
    return 8 ** (offset - 1) * double_factorial * double_factorial


@lru_cache(maxsize=None)
def midpoint_integer_companion(offset: int) -> int:
    """Exact integer companion H_d."""
    _require_offset(offset)
    if offset == 0:
        return 0
    if offset == 1:
        return 1
    d = offset - 1
    return (
        -(28 * d * d + 1) * midpoint_integer_companion(d)
        + 8 * (2 * d - 1) ** 4 * midpoint_integer_companion(d - 1)
    )


def integer_companion_matches_rational(offset: int) -> bool:
    """Cross-check H_d/S_d = G_d exactly over Q."""
    _require_offset(offset)
    if offset == 0:
        return midpoint_companion_fraction(0) == 0
    scale = integer_companion_scale(offset)
    return midpoint_companion_fraction(offset).numerator * scale == (
        midpoint_integer_companion(offset)
        * midpoint_companion_fraction(offset).denominator
    )


def integer_companion_table_mod(prime: int, max_offset: int) -> tuple[int, ...]:
    """H_0,...,H_max modulo p using integer recurrence only."""
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")
    _require_offset(max_offset)
    if max_offset == 0:
        return (0,)
    values = [0, 1]
    for d in range(1, max_offset):
        values.append(
            (
                -(28 * d * d + 1) * values[d]
                + 8 * (2 * d - 1) ** 4 * values[d - 1]
            )
            % prime
        )
    return tuple(values)


def integer_companion_prime_hits(offset: int, prime: int) -> bool:
    """Whether p divides H_d in the p-unit scaling range p>2d-1."""
    _require_offset(offset)
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")
    if offset and prime <= 2 * offset - 1:
        raise ValueError("prime must exceed the companion scaling factors")
    return midpoint_integer_companion(offset) % prime == 0


def forced_zero_offsets_from_integer_companion(prime: int) -> tuple[int, ...]:
    """All left zero offsets 1<=d<m from the integer recurrence."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    if midpoint <= 1:
        return ()
    values = integer_companion_table_mod(prime, midpoint - 1)
    return tuple(offset for offset in range(1, midpoint) if values[offset] == 0)


def zero_digits_from_integer_companion(prime: int) -> tuple[int, ...]:
    """Reconstruct Z_p from integer companion hits plus reflection."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    offsets = forced_zero_offsets_from_integer_companion(prime)
    return tuple(
        sorted(
            [midpoint]
            + [midpoint - offset for offset in offsets]
            + [midpoint + offset for offset in offsets]
        )
    )


def integer_companion_reconstructs_zero_digits(prime: int) -> bool:
    predicted = zero_digits_from_integer_companion(prime)
    actual = franel_zero_digits(prime)
    if predicted != actual:
        raise AssertionError("integer companion must reconstruct the Franel zero alphabet")
    return True


def companion_transfer_determinant(step: int) -> int:
    """det [[-(28d^2+1), 8(2d-1)^4],[1,0]]."""
    if isinstance(step, bool) or not isinstance(step, int) or step <= 0:
        raise ValueError("step must be a positive integer")
    return -8 * (2 * step - 1) ** 4


def companion_casoratian(step: int) -> int:
    """W_d for H_0=0,H_1=1 and K_0=1,K_1=0.

    W_0=1 and W_d=(-8)^d((2d-1)!!)^4.
    """
    _require_offset(step)
    double_factorial = odd_double_factorial(step)
    return (-8) ** step * double_factorial ** 4
