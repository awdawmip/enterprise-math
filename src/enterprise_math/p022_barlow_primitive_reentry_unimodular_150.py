"""Twin-prime primitive re-entry and an actual-prime unimodular N=150 core.

The primitive-successor theorem leaves one genuine arithmetic deferral: a
primitive Franel event at rank r is not captured at r or r+1 when both
2r-1 and 2r+1 are prime.  The canonical central-binomial relation has a much
more rigid shape in this twin-prime case.

For every nontrivial twin-prime center r, the coefficient of A_r is zero in
every composite-boundary defect D_n with

    r+2 <= n < 2r-1,

and the first canonical A_r re-entry is

    D_(2r-1),  alpha_r = -1.

Indeed r is divisible by 3, so the odd boundary 4r-3 of D_(2r-1) is composite.
Before that point, the recursive A-basis expansions of n and 2n-1 only use
indices below r: n<2r-1, while an odd composite 2n-1<4r-3 has largest prime
factor at most (2n-1)/3.  At n=2r-1 the denominator itself is the prime 2r-1,
whose canonical expansion introduces A_r once; the defect relation subtracts
it, producing alpha_r=-1.  This is a structural blackout interval for the
A_r coefficient, not a claim that every primitive Franel prime has no other
Franel zero before the re-entry column.

For the historical N=150 Franel-defect core, two exact twin re-entries are
already genuine triangular unit rows:

    rank 21, prime 3019  -> D_41 with valuation +1,
    rank 30, prime 1361  -> D_59 with valuation +1.

A second finite simplification is stronger than the earlier Smith/Bézout
saturation certificate.  After the existing 18 primitive unit captures reduce
the core to its 22x22 residual R (det R=-13311), introduce only two new real
prime-valuation rows:

    q_41 = 1466657,                 primitive at F_41,
    q_63 = 1017335309243777987,     primitive at F_63.

After projection through the same 18 unit pivots, these are strict singleton
rows on the residual columns:

    v_(q_41) = e_(D_41),
    v_(q_63) = e_(D_63).

Replacing the historical residual rows v_31 and v_563 by these two actual prime
rows gives determinant -1.  Directly making the same substitutions in the
40x40 capture core gives determinant -1 as well.  Thus the N=150 core admits a
square unimodular certificate made entirely from genuine prime valuations; no
derived integer linear combination and no coprime-minor argument is required.

This is a finite structural certificate.  It does not prove that every future
Franel-defect column has a primitive divisor or a bounded-width capture rule.
"""

from __future__ import annotations

from .p022_barlow_defect_core_saturation import core_valuation_row_150
from .p022_barlow_defect_core_smith import exact_determinant_bareiss
from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
    composite_indices,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_primitive_core_reduction import (
    EXPECTED_CAPTURE_COUNT,
    EXPECTED_RESIDUAL_COLUMNS,
    capture_order_150,
    capture_square_core_150,
    primitive_residual_22_150,
    reordered_capture_core_150,
)
from .p022_barlow_primitive_defect_criterion import (
    is_primitive_franel_divisor,
    primitive_defect_pivot,
)
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center

TWIN_REENTRY_21 = (21, 3_019, 41, 1)
TWIN_REENTRY_30 = (30, 1_361, 59, 1)

NEW_PRIMITIVE_RANK_41 = 41
NEW_PRIMITIVE_PRIME_41 = 1_466_657
NEW_PRIMITIVE_RANK_63 = 63
NEW_PRIMITIVE_PRIME_63 = 1_017_335_309_243_777_987
REPLACED_RESIDUAL_ROW_PRIMES = (31, 563)
EXPECTED_TWO_ROW_RESIDUAL_DETERMINANT = -1
EXPECTED_TWO_ROW_CORE_DETERMINANT = -1


def _require_rank(rank: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("rank must be an integer at least three")


def _is_prime_u64(value: int) -> bool:
    """Deterministic Miller-Rabin primality test for 0 <= value < 2**64."""
    if isinstance(value, bool) or not isinstance(value, int):
        return False
    if value < 2 or value >= 1 << 64:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime

    odd_part = value - 1
    power = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        power += 1

    for witness in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        witness %= value
        if witness in (0, 1):
            continue
        residue = pow(witness, odd_part, value)
        if residue in (1, value - 1):
            continue
        for _ in range(power - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def twin_prime_blackout_profile(rank: int) -> tuple[tuple[int, ...], int]:
    """Return (blackout composite columns, first canonical A_r re-entry)."""
    _require_rank(rank)
    if not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be the center of an odd twin-prime pair")
    if rank % 3 != 0:
        raise AssertionError("every nontrivial odd twin-prime center is divisible by three")

    target = 2 * rank - 1
    if target not in composite_indices(target):
        raise AssertionError("4r-3 must be composite, so D_(2r-1) must exist")

    blackout = tuple(
        segment
        for segment in composite_indices(target - 1)
        if rank + 2 <= segment < target
    )
    for segment in blackout:
        coefficient = dict(composite_A_relation_exponents(segment)).get(rank, 0)
        if coefficient != 0:
            raise AssertionError("A_r escaped the twin-prime blackout interval")

    target_coefficient = dict(composite_A_relation_exponents(target)).get(rank, 0)
    if target_coefficient != -1:
        raise AssertionError("first canonical twin-prime re-entry must have alpha_r=-1")
    return blackout, target


def primitive_twin_reentry_certificate(rank: int, prime: int) -> tuple[int, int]:
    """Exact q-adic unit re-entry certificate when the declared prime has one."""
    _, target = twin_prime_blackout_profile(rank)
    if not _is_prime_u64(prime):
        raise ValueError("prime must be a certified unsigned-64-bit prime")
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")

    depth = p_adic_valuation(triple_moment_factor(rank), prime)
    if depth <= 0:
        raise AssertionError("primitive depth must be positive")
    earlier_support = tuple(
        segment
        for segment in composite_indices(target - 1)
        if franel_defect_valuation(segment, prime) != 0
    )
    if earlier_support:
        raise AssertionError("declared primitive row is not triangular up to re-entry")
    actual = franel_defect_valuation(target, prime)
    if actual != depth:
        raise AssertionError("twin-prime re-entry must recover the primitive depth")
    return target, actual


def _project_through_eighteen_capture_pivots(prime: int) -> tuple[int, ...]:
    """Project one genuine valuation row into the historical 22-column residual."""
    _, col_order = capture_order_150()
    row = [core_valuation_row_150(prime)[index] for index in col_order]
    pivot_matrix = reordered_capture_core_150()
    for pivot_index in range(EXPECTED_CAPTURE_COUNT):
        pivot = pivot_matrix[pivot_index][pivot_index]
        if abs(pivot) != 1:
            raise AssertionError("capture pivot must remain an integer unit")
        coefficient = row[pivot_index]
        if coefficient:
            multiplier = coefficient // pivot
            for col in range(pivot_index, len(row)):
                row[col] -= multiplier * pivot_matrix[pivot_index][col]
        if row[pivot_index] != 0:
            raise AssertionError("projection must clear every primitive capture column")
    return tuple(row[EXPECTED_CAPTURE_COUNT:])


def new_primitive_rows_are_certified_150() -> bool:
    """Certify primality, primitive rank, and unit direct pivots for q_41,q_63."""
    for rank, prime in (
        (NEW_PRIMITIVE_RANK_41, NEW_PRIMITIVE_PRIME_41),
        (NEW_PRIMITIVE_RANK_63, NEW_PRIMITIVE_PRIME_63),
    ):
        if not _is_prime_u64(prime):
            raise AssertionError("stored new valuation row must be genuinely prime")
        if not is_primitive_franel_divisor(rank, prime):
            raise AssertionError("stored new prime must be primitive at its declared rank")
        if primitive_defect_pivot(rank, prime) != 1:
            raise AssertionError("stored new primitive pivot must have unit depth")
    return True


def projected_new_primitive_supports_150() -> tuple[
    tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]
]:
    """The two new rows are strict singleton units on D_41 and D_63."""
    new_primitive_rows_are_certified_150()
    row_41 = _project_through_eighteen_capture_pivots(NEW_PRIMITIVE_PRIME_41)
    row_63 = _project_through_eighteen_capture_pivots(NEW_PRIMITIVE_PRIME_63)
    support_41 = tuple(
        (segment, value)
        for segment, value in zip(EXPECTED_RESIDUAL_COLUMNS, row_41, strict=True)
        if value
    )
    support_63 = tuple(
        (segment, value)
        for segment, value in zip(EXPECTED_RESIDUAL_COLUMNS, row_63, strict=True)
        if value
    )
    if support_41 != ((41, 1),):
        raise AssertionError("q_41 projected support changed")
    if support_63 != ((63, 1),):
        raise AssertionError("q_63 projected support changed")
    return support_41, support_63


def residual_row_primes_150() -> tuple[int, ...]:
    """Row labels of the historical 22x22 residual after the 18 captures."""
    _, row_primes, _ = capture_square_core_150()
    row_order, _ = capture_order_150()
    labels = tuple(row_primes[index] for index in row_order[EXPECTED_CAPTURE_COUNT:])
    if len(labels) != len(EXPECTED_RESIDUAL_COLUMNS):
        raise AssertionError("residual row/column dimensions diverged")
    return labels


def two_row_unimodular_residual_150() -> tuple[tuple[int, ...], ...]:
    """Replace v_31,v_563 by the projected q_41,q_63 rows."""
    projected_new_primitive_supports_150()
    matrix = [list(row) for row in primitive_residual_22_150()]
    labels = residual_row_primes_150()
    replacements = (
        (31, _project_through_eighteen_capture_pivots(NEW_PRIMITIVE_PRIME_41)),
        (563, _project_through_eighteen_capture_pivots(NEW_PRIMITIVE_PRIME_63)),
    )
    for old_prime, replacement in replacements:
        row_index = labels.index(old_prime)
        matrix[row_index] = list(replacement)
    return tuple(tuple(row) for row in matrix)


def two_row_unimodular_residual_determinant_150() -> int:
    value = exact_determinant_bareiss(two_row_unimodular_residual_150())
    if value != EXPECTED_TWO_ROW_RESIDUAL_DETERMINANT:
        raise AssertionError("two-row residual determinant changed")
    return value


def two_row_actual_prime_core_150() -> tuple[tuple[int, ...], ...]:
    """40x40 capture core after replacing v_31,v_563 by the two new prime rows."""
    square, row_primes, _ = capture_square_core_150()
    matrix = [list(row) for row in square]
    labels = list(row_primes)
    for old_prime, new_prime in (
        (31, NEW_PRIMITIVE_PRIME_41),
        (563, NEW_PRIMITIVE_PRIME_63),
    ):
        row_index = labels.index(old_prime)
        matrix[row_index] = list(core_valuation_row_150(new_prime))
        labels[row_index] = new_prime
    if not all(_is_prime_u64(prime) for prime in labels):
        raise AssertionError("every row of the final core must be an actual prime valuation")
    return tuple(tuple(row) for row in matrix)


def two_row_actual_prime_core_determinant_150() -> int:
    value = exact_determinant_bareiss(two_row_actual_prime_core_150())
    if value != EXPECTED_TWO_ROW_CORE_DETERMINANT:
        raise AssertionError("actual-prime 40x40 core determinant changed")
    return value


def verify_primitive_reentry_unimodular_150() -> bool:
    if primitive_twin_reentry_certificate(*TWIN_REENTRY_21[:2]) != TWIN_REENTRY_21[2:]:
        raise AssertionError("rank-21 twin re-entry certificate changed")
    if primitive_twin_reentry_certificate(*TWIN_REENTRY_30[:2]) != TWIN_REENTRY_30[2:]:
        raise AssertionError("rank-30 twin re-entry certificate changed")
    new_primitive_rows_are_certified_150()
    projected_new_primitive_supports_150()
    if two_row_unimodular_residual_determinant_150() != -1:
        raise AssertionError("22-residual is not unimodular after two real prime rows")
    if two_row_actual_prime_core_determinant_150() != -1:
        raise AssertionError("40-core is not unimodular after two real prime rows")
    return True
