from fractions import Fraction

from enterprise_math.p017_p018_iwaniec_root_level_bridge import (
    IWANIEC_LABORDE_LEVEL,
    IWANIEC_LABORDE_THETA,
    bilinear_level_exponent,
    iwaniec_root_level_ledger,
    root_sieve_parameter,
)


def test_1981_level_exponent_and_root_cutoffs_align_exactly() -> None:
    assert bilinear_level_exponent(IWANIEC_LABORDE_THETA) == IWANIEC_LABORDE_LEVEL == Fraction(19, 35)
    assert root_sieve_parameter(IWANIEC_LABORDE_THETA, Fraction(1, 4)) == Fraction(76, 35) > 2
    assert root_sieve_parameter(IWANIEC_LABORDE_THETA, Fraction(1, 3)) == Fraction(57, 35) < 2


def test_formal_square_endpoint_direct_p2_gap_is_one_over_42() -> None:
    data = iwaniec_root_level_ledger()
    assert data["formal_square_level_exponent"] == Fraction(9, 14)
    assert data["formal_square_p3_s"] == Fraction(18, 7) > 2
    assert data["formal_square_p2_s"] == Fraction(27, 14) < 2
    assert data["formal_square_direct_p2_level_deficit"] == Fraction(1, 42)
    assert data["status"] == "PRIOR_ART_LEVEL_TO_ROOT_CUTOFF_ALIGNMENT"
