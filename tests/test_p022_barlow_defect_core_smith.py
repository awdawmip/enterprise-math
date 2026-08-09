from math import gcd

from enterprise_math.p022_barlow_defect_core_smith import (
    CORE_EXCEPTIONAL_PRIMES,
    CORE_EXACT_DETERMINANT,
    CORE_MINOR_ONE,
    CORE_MINOR_TWO,
    CORE_SMITH_LAST_INVARIANT,
    exact_core_determinant_150,
    historical_modular_residue_from_exact_determinant,
    prime_factors_of_core_cokernel,
    smith_invariant_factors_150,
    smith_witness_minors_150,
)
from enterprise_math.p022_barlow_low_order_identifiability_150 import (
    CERTIFICATE_150_DETERMINANT_RESIDUE,
)


def test_exact_core_determinant_is_small_nonzero_integer() -> None:
    assert exact_core_determinant_150() == CORE_EXACT_DETERMINANT == -26_622
    assert abs(CORE_EXACT_DETERMINANT) == 2 * 3**3 * 17 * 29


def test_two_39x39_minors_are_coprime() -> None:
    first, second = smith_witness_minors_150()
    assert (first, second) == (CORE_MINOR_ONE, CORE_MINOR_TWO) == (-6, -797)
    assert gcd(abs(first), abs(second)) == 1


def test_smith_diagonal_has_only_one_nontrivial_invariant() -> None:
    invariants = smith_invariant_factors_150()
    assert len(invariants) == 40
    assert invariants[:39] == (1,) * 39
    assert invariants[-1] == CORE_SMITH_LAST_INVARIANT == 26_622


def test_only_four_prime_characteristics_make_the_core_singular() -> None:
    assert prime_factors_of_core_cokernel() == CORE_EXCEPTIONAL_PRIMES == (
        2,
        3,
        17,
        29,
    )


def test_old_modular_residue_is_just_exact_determinant_reduced_modulo_q() -> None:
    assert historical_modular_residue_from_exact_determinant() == 973_381
    assert historical_modular_residue_from_exact_determinant() == (
        CERTIFICATE_150_DETERMINANT_RESIDUE
    )
