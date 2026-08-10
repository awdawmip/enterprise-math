"""Localize all forced-copy defect pollution to the original q-digit alphabet.

For the forced composite copy N=a*q+r (a=1 or 2) of a primitive twin rank r,
put B=2N-1.  By construction 3 divides B.  Every odd prime factor of B is at
most B/3, and every index introduced by the recursive central-binomial integer
basis is at most half such a prime plus one.  Using q>=2r+1, this puts the whole
integer-basis support of B strictly below q.

The denominator integer basis of N is also harmless above q.  For a=1 all its
indices are below q.  For a=2 its possible indices above q are at most
(N+1)/2=q+(r+1)/2, so their base-q remainder is strictly below the primitive
rank r and cannot be a Franel zero digit.

Consequently every q-divisible Franel support term in the canonical defect at
N has index below q and is literally one of the original zero digits Z_q.  No
new higher-digit Lucas zero can pollute the forced copy.  The unresolved global
capture problem is therefore a finite signed coefficient problem on Z_q.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import base_p_digits, franel_zero_digits
from .p022_barlow_half_defect_support_tree import prime_halving_candidate_indices
from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
    integer_in_central_binomial_basis,
)
from .p022_barlow_lucas_copy_capture import forced_composite_copy_segment
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor


def forced_copy_numerator_support_bound(rank: int, prime: int) -> tuple[int, int]:
    """Return (max exact support, rigorous tree bound), both strictly below q."""
    _, segment = forced_composite_copy_segment(rank, prime)
    boundary = 2 * segment - 1
    if boundary % 3:
        raise AssertionError("forced boundary must be divisible by three")
    tree_bound = (boundary // 3 + 1) // 2
    exact = integer_in_central_binomial_basis(boundary)
    exact_max = max((index for index, _ in exact), default=0)
    if exact_max > tree_bound:
        raise AssertionError("integer-basis support exceeded the factor/halving bound")
    if tree_bound >= prime:
        raise AssertionError("forced-copy numerator tree must stay below q")
    candidates = prime_halving_candidate_indices(boundary)
    if exact and not {index for index, _ in exact} <= set(candidates):
        raise AssertionError("prime-halving candidates must contain exact support")
    return exact_max, tree_bound


def forced_copy_denominator_high_remainders_are_preprimitive(rank: int, prime: int) -> bool:
    """Any denominator-basis index >=q has base-q remainder below r."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    a, segment = forced_composite_copy_segment(rank, prime)
    exact = integer_in_central_binomial_basis(segment)
    if a == 1 and any(index >= prime for index, _ in exact):
        raise AssertionError("a=1 denominator support must stay below q")
    ceiling = (segment + 1) // 2
    for index, _ in exact:
        if index > ceiling:
            raise AssertionError("integer-basis index exceeded the direct half-prime ceiling")
        if index < prime:
            continue
        digits = base_p_digits(index, prime)
        if len(digits) != 2 or digits[0] >= rank:
            raise AssertionError("high denominator index must have preprimitive remainder")
    return True


def forced_copy_pollution_is_single_digit(rank: int, prime: int) -> tuple[tuple[int, int], ...]:
    """All q-divisible defect support is exactly on original zero digits <q."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    _, segment = forced_composite_copy_segment(rank, prime)
    forced_copy_numerator_support_bound(rank, prime)
    forced_copy_denominator_high_remainders_are_preprimitive(rank, prime)
    zeros = set(franel_zero_digits(prime))
    pollution = []
    for index, exponent in composite_A_relation_exponents(segment):
        digits = base_p_digits(index, prime)
        divisible = any(digit in zeros for digit in digits)
        if not divisible:
            continue
        if index >= prime:
            raise AssertionError("all q-divisible forced-copy support must collapse below q")
        if index not in zeros:
            raise AssertionError("sub-q pollution must be a literal zero digit")
        pollution.append((index, exponent))
    return tuple(pollution)


def forced_copy_positive_pollution(rank: int, prime: int) -> tuple[tuple[int, int], ...]:
    """Exact remaining obstruction to the nonpositive-support capture theorem."""
    return tuple(
        (index, exponent)
        for index, exponent in forced_copy_pollution_is_single_digit(rank, prime)
        if exponent > 0
    )
