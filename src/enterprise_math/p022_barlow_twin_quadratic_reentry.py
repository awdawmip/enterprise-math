"""Universal quadratic re-entry pair for a primitive twin Franel source.

Let r be a nontrivial twin-prime center, with source primes

    p_- = 2r-1,   p_+ = 2r+1.

Two neighboring-product identities give composite odd boundaries with smooth
denominators:

    2 N_- - 1 = (2r-1)(2r-3),   N_- = 2(r-1)^2,
    2 N_+ - 1 = (2r+1)(2r+3),   N_+ = 2(r+1)^2.

For N_- every factor other than p_- is below p_-, while N_- itself is built
from r-1.  Hence the canonical A-relation has high support exactly

    +e_r + e_(N_--1).

For N_+, the factor 2r+3 is a nontrivial multiple of three because every
nontrivial twin center has 3|r.  Its prime-halving support is below r, as is the
support of N_+=2(r+1)^2.  Thus the high support is exactly

    -e_r + e_(r+1) + e_(N_+-1).

For a q-adic row primitive at r, z_(r+1)=0.  Therefore complete defect escape
forces two additional Franel zeros:

    q | F_(K_-),  K_- = N_- = 2(r-1)^2,
    q | F_(K_+),  K_+ = N_+-1 = 2(r+1)^2-1.

Their separation is the linear quantity

    K_+ - K_- = 8r-1.

The clean relations hold without a size hypothesis.  The stronger digit-band
consequence is used only after the terminal-escape size bound q>=3r-1.  In that
range both transported indices satisfy K<rq<q^2.  Their base-q quotient digits
are therefore below r and are q-units.  Hence p-Lucas puts the zero in the
remainder digit, while Jarvis--Verrill reflection puts its mirror in the zero
alphabet as well.  Primitivity then forces the symmetric band

    r <= K mod q <= q-1-r.

The Franel p-Lucas/reflection facts are prior art.  The quadratic clean rows,
their paired transport, and the symmetric digit-band use are P022-local.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import (
    franel_lucas_residue,
    franel_residue,
)
from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center


def _require_twin(rank: int) -> None:
    if rank < 6 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a nontrivial twin-prime center")


def left_quadratic_segment(rank: int) -> int:
    _require_twin(rank)
    return 2 * (rank - 1) ** 2


def right_quadratic_segment(rank: int) -> int:
    _require_twin(rank)
    return 2 * (rank + 1) ** 2


def left_quadratic_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    segment = left_quadratic_segment(rank)
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((rank, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("left quadratic re-entry escaped the clean support")
    return high


def right_quadratic_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    segment = right_quadratic_segment(rank)
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((rank, -1), (rank + 1, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("right quadratic re-entry escaped the clean support")
    return high


def quadratic_transported_indices(rank: int) -> tuple[int, int]:
    """Return (K_-,K_+) forced by vanishing of the two clean defects."""
    left = left_quadratic_segment(rank)
    right = right_quadratic_segment(rank) - 1
    if right - left != 8 * rank - 1:
        raise AssertionError("quadratic transported-index separation changed")
    return left, right


def primitive_zero_digit_band(
    rank: int,
    prime: int,
    index: int,
) -> tuple[int, int, int]:
    """For a transported q-zero K<rq, return (quotient,remainder,mirror)."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared rank")
    if prime < 3 * rank - 1:
        raise ValueError("digit-band use requires the terminal-escape size horizon")
    if not rank <= index < rank * prime:
        raise ValueError("index must lie in the one-extra-digit horizon [r,rq)")
    if franel_lucas_residue(index, prime) != 0:
        raise ValueError("index must be a q-divisible Franel term")
    quotient, remainder = divmod(index, prime)
    if quotient >= rank:
        raise AssertionError("transported quotient digit must be preprimitive")
    if quotient and franel_residue(quotient, prime) == 0:
        raise AssertionError("preprimitive quotient digit must be a q-unit")
    if franel_residue(remainder, prime) != 0:
        raise AssertionError("p-Lucas zero must lie in the remainder digit")
    mirror = prime - 1 - remainder
    if remainder < rank or mirror < rank:
        raise AssertionError("primitivity plus reflection forces the symmetric band")
    return quotient, remainder, mirror


def quadratic_escape_outcomes(
    rank: int,
    prime: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return capture rows, or certify both quadratic transported zeros.

    This verifier is intended after terminal cancellation, so the size horizon
    q>=3r-1 is explicit.  A nonzero returned valuation is a capture; a zero
    valuation triggers the corresponding p-Lucas digit-band certificate.
    """
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared rank")
    _require_twin(rank)
    if prime < 3 * rank - 1:
        raise ValueError("quadratic escape verifier starts at the terminal horizon")
    left_segment = left_quadratic_segment(rank)
    right_segment = right_quadratic_segment(rank)
    left_value = franel_defect_valuation(left_segment, prime)
    right_value = franel_defect_valuation(right_segment, prime)
    left_index, right_index = quadratic_transported_indices(rank)
    if left_value == 0:
        primitive_zero_digit_band(rank, prime, left_index)
    if right_value == 0:
        primitive_zero_digit_band(rank, prime, right_index)
    return (left_segment, left_value), (right_segment, right_value)
