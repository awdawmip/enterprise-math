"""Force a primitive twin-source escape beyond the six-rank scale.

Let q be a Franel prime primitive at a nontrivial twin center r, so 2r-1 and
2r+1 are prime and r is a multiple of three.  Suppose the first terminal row
D_(2r-1) cancels.  Earlier P022 work then supplies the terminal equal-depth
collision and the lower bound q>=3r-1.

The two source primes themselves have useful odd-multiple re-entry rows.
For the right source prime 2r+1 put

    N3+ = 3r+2,    2N3+-1 = 3(2r+1),
    N5+ = 5r+3,    2N5+-1 = 5(2r+1).

If N3+ is composite, its canonical A-relation has, at indices >=r, exactly

    A_r^(-1) A_(r+1) A_(3r+1).

If N3+ is prime then r is odd; switching to the left source prime gives the
always-even segment

    N3- = 3r-1,    2N3--1 = 3(2r-1),

whose high support is exactly A_r A_(3r-2).

At a primitive source F_(r+1) is a q-unit.  If the relevant threefold defect
also vanishes, p-Lucas nonadjacency below the two-digit horizon forces a new
q-zero near 3r.  Primitivity plus reflection then forces q beyond 4r; the only
small residual candidate q=4r+1 is already excluded by the universal midpoint
companion terminal-offset theorem.  Thus continued escape implies q>=4r+5.

The fivefold row is uniform for r>=9.  Since r=0 mod3,

    N5+ = 5r+3 = 3(5r/3+1).

The integer-basis support of N5+ is strictly below r, and the same holds for
all nonexplicit pieces of 5(2r+1).  Hence the high support is exactly

    A_r^(-1) A_(r+1) A_(5r+2).

If this defect also vanishes, the same p-Lucas/reflection argument forces
q>6r+3.  Therefore a terminally deferred primitive twin row is either captured
by one of these fixed source re-entry rows or its valuation prime lies beyond
the linear six-rank barrier.

The Franel p-Lucas/reflection/nonadjacency facts are prior art.  The exact
central-binomial re-entry supports and their Barlow escape coupling are P022.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import (
    base_p_digits,
    franel_zero_digits,
)
from .p022_barlow_franel_universal_companion import (
    first_large_terminal_offsets_are_excluded,
)
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center
from .p022_barlow_twin_defect_difference import (
    primitive_twin_terminal_cancellation_signature,
)


def _require_twin_source(rank: int, prime: int) -> None:
    if rank < 6 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a nontrivial twin-prime center")
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")


def right_threefold_segment(rank: int) -> int:
    return 3 * rank + 2


def left_threefold_segment(rank: int) -> int:
    return 3 * rank - 1


def right_fivefold_segment(rank: int) -> int:
    return 5 * rank + 3


def right_threefold_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    """High A-support at N=3r+2 when that integer is composite."""
    if rank < 6 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a nontrivial twin-prime center")
    segment = right_threefold_segment(rank)
    if _is_prime(segment):
        raise ValueError("prime N3+ uses the left threefold fallback")
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((rank, -1), (rank + 1, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("right threefold support escaped the clean form")
    return high


def left_threefold_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    """High A-support at N=3r-1 in the odd-rank fallback branch."""
    if rank < 6 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a nontrivial twin-prime center")
    if rank % 2 == 0:
        raise ValueError("left threefold fallback is only needed for odd rank")
    segment = left_threefold_segment(rank)
    if _is_prime(segment):
        raise AssertionError("3r-1 must be even and composite for odd r")
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((rank, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("left threefold support escaped the clean form")
    return high


def right_fivefold_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    """Uniform high A-support at N=5r+3 for every twin rank r>=9."""
    if rank < 9 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a twin-prime center at least nine")
    segment = right_fivefold_segment(rank)
    if segment % 3:
        raise AssertionError("r=0 mod3 must make 5r+3 divisible by three")
    if _is_prime(segment):
        raise AssertionError("right fivefold segment must be composite")
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((rank, -1), (rank + 1, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("right fivefold support escaped the clean form")
    return high


def _two_digit_adjacent_zeros_are_forbidden(
    prime: int,
    left: int,
    right: int,
) -> bool:
    """Certify adjacent q-zeros cannot occur when right<2q and q is a unit digit."""
    if right != left + 1 or not 0 <= left < right < 2 * prime:
        raise ValueError("indices must be adjacent and lie below 2q")
    zeros = set(franel_zero_digits(prime))
    for value in (left, right):
        digits = base_p_digits(value, prime)
        if len(digits) > 2:
            raise AssertionError("declared horizon must use at most two base-q digits")
        if len(digits) == 2 and digits[1] != 1:
            raise AssertionError("the only possible leading digit below 2q is one")
    left_zero = any(digit in zeros for digit in base_p_digits(left, prime))
    right_zero = any(digit in zeros for digit in base_p_digits(right, prime))
    if left_zero and right_zero:
        raise AssertionError("unit-leading adjacent copies inherit single-digit nonadjacency")
    return True


def _zero_index_forces_size_side(
    rank: int,
    prime: int,
    zero_index: int,
) -> str:
    """Use primitivity/p-Lucas/reflection to locate q around one forced zero.

    The caller guarantees rank<zero_index<2q and q|F_zero_index.
    Returns ``below`` when q<zero_index, and ``above`` when q>zero_index,
    after certifying the corresponding primitive size inequality.
    """
    if not rank < zero_index < 2 * prime:
        raise ValueError("zero index must lie between the source and 2q")
    zeros = set(franel_zero_digits(prime))
    if zero_index < prime:
        if zero_index not in zeros:
            raise AssertionError("single-digit forced zero is missing from Z_q")
        reflected = prime - 1 - zero_index
        if reflected < rank:
            raise AssertionError("reflection would create a zero below the primitive rank")
        return "above"
    remainder = zero_index - prime
    if remainder not in zeros:
        raise AssertionError("two-digit p-Lucas copy must have a zero remainder digit")
    if remainder < rank:
        raise AssertionError("p-Lucas copy would create a zero below the primitive rank")
    return "below"


def threefold_reentry_or_barrier(rank: int, prime: int) -> tuple[str, int, int]:
    """Return capture or certify that terminal escape has crossed the 4r scale.

    The terminal defect must already vanish.  The result is either
    ``("capture", segment, valuation)`` or ``("barrier", 4r+5, prime)``.
    """
    _require_twin_source(rank, prime)
    if primitive_twin_terminal_cancellation_signature(rank, prime) is None:
        raise ValueError("the twin terminal defect has not cancelled")

    right = right_threefold_segment(rank)
    if not _is_prime(right):
        right_threefold_high_support(rank)
        value = franel_defect_valuation(right, prime)
        if value:
            return "capture", right, value
        source_depth = p_adic_valuation(triple_moment_factor(rank), prime)
        previous_depth = p_adic_valuation(triple_moment_factor(right - 1), prime)
        current_depth = p_adic_valuation(triple_moment_factor(right), prime)
        if right >= 2 * prime:
            raise AssertionError("terminal cancellation already gives q>=3r-1, so N3+<2q")
        _two_digit_adjacent_zeros_are_forbidden(prime, right - 1, right)
        if current_depth != 0 or previous_depth != source_depth:
            raise AssertionError("vanishing right threefold defect must transport source depth backward")
        side = _zero_index_forces_size_side(rank, prime, right - 1)
        if side != "above" or prime < 4 * rank + 2:
            raise AssertionError("right threefold zero must force q beyond 4r+1")
    else:
        if rank % 2 == 0:
            raise AssertionError("3r+2 prime forces r odd")
        left = left_threefold_segment(rank)
        left_threefold_high_support(rank)
        value = franel_defect_valuation(left, prime)
        if value:
            return "capture", left, value
        source_depth = p_adic_valuation(triple_moment_factor(rank), prime)
        previous_depth = p_adic_valuation(triple_moment_factor(left - 1), prime)
        current_depth = p_adic_valuation(triple_moment_factor(left), prime)
        if current_depth != source_depth or previous_depth != 0:
            raise AssertionError("vanishing left threefold defect must transport source depth forward")
        if left >= prime:
            raise AssertionError("odd-rank left threefold zero must lie below q")
        reflected = prime - 1 - left
        if reflected < rank:
            raise AssertionError("left threefold reflection would violate primitivity")
        if prime < 4 * rank:
            raise AssertionError("left threefold zero must force q>=4r")
        if prime == 4 * rank + 1:
            first_large_terminal_offsets_are_excluded(rank, prime)
            raise AssertionError("q=4r+1 cannot support terminal cancellation")

    if prime < 4 * rank + 5:
        raise AssertionError("prime arithmetic leaves no terminally escaping q below 4r+5")
    return "barrier", 4 * rank + 5, prime


def fivefold_reentry_or_barrier(rank: int, prime: int) -> tuple[str, int, int]:
    """After the 4r barrier, capture or force q beyond 6r+3."""
    _require_twin_source(rank, prime)
    if rank < 9:
        raise ValueError("rank six is a finite exceptional case")
    if prime < 4 * rank + 5:
        raise ValueError("threefold barrier must be established first")
    right = right_fivefold_segment(rank)
    right_fivefold_high_support(rank)
    value = franel_defect_valuation(right, prime)
    if value:
        return "capture", right, value

    source_depth = p_adic_valuation(triple_moment_factor(rank), prime)
    previous_depth = p_adic_valuation(triple_moment_factor(right - 1), prime)
    current_depth = p_adic_valuation(triple_moment_factor(right), prime)
    if right >= 2 * prime:
        raise AssertionError("q>=4r+5 must place N5+ below the two-digit horizon")
    _two_digit_adjacent_zeros_are_forbidden(prime, right - 1, right)
    if current_depth != 0 or previous_depth != source_depth:
        raise AssertionError("vanishing fivefold defect must transport source depth backward")
    side = _zero_index_forces_size_side(rank, prime, right - 1)
    if side != "above" or prime < 6 * rank + 3:
        raise AssertionError("fivefold transported zero must force q beyond 6r+2")
    if prime == 6 * rank + 3:
        raise AssertionError("6r+3 is a nontrivial multiple of three")
    return "barrier", 6 * rank + 4, prime
