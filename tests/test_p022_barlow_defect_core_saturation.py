from math import gcd

from enterprise_math.p022_barlow_defect_core_saturation import (
    BEZOUT_ONE,
    BEZOUT_TWO,
    PAIRING_ONE,
    PAIRING_TWO,
    SATURATION_PRIME_ONE,
    SATURATION_PRIME_TWO,
    derived_unimodular_row_150,
    obstruction_pairing_150,
    saturation_pairings_150,
    unimodular_core_determinant_150,
    verify_core_saturation_150,
)
from enterprise_math.p022_barlow_defect_core_obstruction import (
    primitive_obstruction_vector_150,
)


def test_two_new_prime_rows_have_coprime_obstruction_pairings() -> None:
    assert obstruction_pairing_150(SATURATION_PRIME_ONE) == PAIRING_ONE == -13_311
    assert obstruction_pairing_150(SATURATION_PRIME_TWO) == PAIRING_TWO == 2_518
    first, second = saturation_pairings_150()
    assert gcd(abs(first), abs(second)) == 1


def test_stored_bezout_combination_pairs_with_obstruction_by_one() -> None:
    first, second = saturation_pairings_150()
    assert BEZOUT_ONE * first + BEZOUT_TWO * second == 1
    row = derived_unimodular_row_150()
    vector = primitive_obstruction_vector_150()
    assert sum(value * coefficient for value, coefficient in zip(row, vector, strict=True)) == 1


def test_replacing_v269_by_derived_row_makes_core_unimodular() -> None:
    assert unimodular_core_determinant_150() == 1


def test_full_saturation_verifier_passes() -> None:
    assert verify_core_saturation_150()
