"""Lift primitive twin terminal cancellation to the fixed transfer depth.

Let t=2r-2.  Linearity of the Franel recurrence gives an exact decomposition
from the state at r-1,r to the terminal coordinate t:

    F_t = C_r F_(r-1) + E_r F_r,

where C_r is the direct terminal transfer from initial state (1,0), and E_r is
the companion transfer from initial state (0,1).

For a primitive Franel prime q at rank r all recurrence denominators between r
and t are q-units, and F_(r-1) is a q-unit.  If the primitive twin terminal row
cancels, P022 already proves

    v_q(F_t)=v_q(F_r)=h>0.

The exact linear decomposition then forces

    v_q(C_r)>=h.

Indeed both F_t and E_r F_r vanish modulo q^h, so C_r F_(r-1) does as well.
Thus a deep primitive source h>=2 which still cancels at the terminal row
requires q^2 to divide the numerator of the fixed transfer C_r.  This depth
lift does not require formal-derivative stationarity and is therefore an
independent compression of the deep escape branch.

Finite exact pressure tests currently find no large common square divisor of
F_r and num(C_r) in the tested range.  That squarefreeness pattern is evidence,
not a theorem.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p022_barlow_franel_terminal_transfer import terminal_transfer
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center
from .p022_barlow_twin_defect_difference import primitive_twin_terminal_cancellation_signature


def terminal_companion_transfer(rank: int) -> Fraction:
    """E_r: terminal value from state (y_(r-1),y_r)=(0,1)."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 2:
        raise ValueError("rank must be an integer at least two")
    previous = Fraction(0, 1)
    current = Fraction(1, 1)
    for n in range(rank, 2 * rank - 2):
        following = Fraction(
            (7 * n * n + 7 * n + 2) * current + 8 * n * n * previous,
            (n + 1) ** 2,
        )
        previous, current = current, following
    return current


def terminal_linear_decomposition(rank: int) -> tuple[Fraction, Fraction, int]:
    """Certify F_(2r-2)=C_r F_(r-1)+E_r F_r exactly."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 2:
        raise ValueError("rank must be an integer at least two")
    c = terminal_transfer(rank)
    e = terminal_companion_transfer(rank)
    previous = triple_moment_factor(rank - 1)
    current = triple_moment_factor(rank)
    terminal = triple_moment_factor(2 * rank - 2)
    predicted = c * previous + e * current
    if predicted.denominator != 1 or predicted.numerator != terminal:
        raise AssertionError("terminal transfer decomposition failed")
    return c, e, terminal


def rational_p_adic_valuation(value: Fraction, prime: int) -> int:
    """p-adic valuation of a nonzero rational."""
    if value == 0:
        raise ValueError("zero has infinite p-adic valuation")
    return p_adic_valuation(abs(value.numerator), prime) - p_adic_valuation(
        value.denominator, prime
    )


def primitive_terminal_cancellation_lifts_transfer_depth(rank: int, prime: int) -> tuple[int, int]:
    """Return (source_depth,transfer_depth) and certify transfer_depth>=source_depth."""
    if rank < 6 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a nontrivial twin-prime center")
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared rank")
    signature = primitive_twin_terminal_cancellation_signature(rank, prime)
    if signature is None:
        raise ValueError("the first twin terminal defect has not cancelled")
    source_depth, terminal_depth, next_depth = signature
    if next_depth != 0 or terminal_depth != source_depth:
        raise AssertionError("terminal cancellation signature changed")

    c, e, terminal = terminal_linear_decomposition(rank)
    _ = e
    if c.denominator % prime == 0:
        raise AssertionError("primitive q must be a unit on the terminal transfer denominator")
    if terminal % (prime**source_depth):
        raise AssertionError("terminal value must carry the source depth")
    if triple_moment_factor(rank) % (prime**source_depth):
        raise AssertionError("source value must carry its declared depth")
    if triple_moment_factor(rank - 1) % prime == 0:
        raise AssertionError("primitivity makes F_(r-1) a q-unit")

    transfer_depth = rational_p_adic_valuation(c, prime)
    if transfer_depth < source_depth:
        raise AssertionError("terminal cancellation must lift the full source depth into C_r")
    return source_depth, transfer_depth


def terminal_source_transfer_gcd(rank: int) -> int:
    """gcd(F_r,num(C_r)), the fixed terminal common-zero integer."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 2:
        raise ValueError("rank must be an integer at least two")
    return gcd(triple_moment_factor(rank), abs(terminal_transfer(rank).numerator))


def large_common_square_primes(rank: int) -> tuple[int, ...]:
    """Finite diagnostic: primes q>r with q^2 dividing both F_r and num(C_r)."""
    value = terminal_source_transfer_gcd(rank)
    result = []
    remaining = value
    candidate = 2
    while candidate * candidate <= remaining:
        exponent = 0
        while remaining % candidate == 0:
            remaining //= candidate
            exponent += 1
        if candidate > rank and exponent >= 2:
            result.append(candidate)
        candidate = 3 if candidate == 2 else candidate + 2
    return tuple(result)
