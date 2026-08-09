from fractions import Fraction

from enterprise_math.p022_barlow_low_order_defect_reduction import (
    A_certificate_rows_are_complete_prime_basis_150,
    DEFECT_66_DETERMINANT_RESIDUE,
    DEFECT_67_DETERMINANT_RESIDUE,
    DEFECT_150_DETERMINANT_RESIDUE,
    composite_A_relation_exponents,
    composite_indices,
    defect_certificate_66_residue,
    defect_certificate_67_residue,
    defect_certificate_150_residue,
    evaluate_A_exponents,
    franel_defect,
    franel_defect_valuation,
    integer_in_central_binomial_basis,
    primes_through,
    segment_67_A_relation,
    segment_67_row_337_defect_support,
)
from enterprise_math.p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    pair_moment_factor,
    triple_moment_factor,
)


def test_integer_basis_reconstructs_every_small_positive_integer() -> None:
    for value in range(1, 300):
        exponents = integer_in_central_binomial_basis(value)
        assert evaluate_A_exponents(exponents) == Fraction(value, 1)


def test_prime_odd_boundary_is_exactly_a_new_A_valuation_pivot() -> None:
    for segment in range(2, 151):
        boundary = 2 * segment - 1
        if boundary not in primes_through(boundary):
            continue
        assert p_adic_valuation(pair_moment_factor(segment), boundary) == 1
        assert all(
            p_adic_valuation(pair_moment_factor(previous), boundary) == 0
            for previous in range(1, segment)
        )


def test_every_composite_boundary_A_column_has_exact_triangular_relation() -> None:
    for segment in composite_indices(150):
        relation = composite_A_relation_exponents(segment)
        assert relation
        assert all(index < segment for index, _ in relation)
        assert evaluate_A_exponents(relation) == pair_moment_factor(segment)


def test_tail_plus_composite_relation_count_matches_A_kernel_dimension() -> None:
    for maximum in range(2, 151):
        a_rank = len(primes_through(2 * maximum - 1))
        total_joint_columns = maximum + 1  # segments 1..N plus hidden tail
        assert 1 + len(composite_indices(maximum)) == total_joint_columns - a_rank


def test_segment_67_canonical_A_relation_is_exact_and_small() -> None:
    relation = segment_67_A_relation()
    assert relation == (
        (1, 3),
        (2, -2),
        (4, 1),
        (8, 1),
        (9, -2),
        (10, 1),
        (33, 1),
        (34, -1),
        (66, 1),
    )
    assert evaluate_A_exponents(relation) == pair_moment_factor(67)


def test_franel_defect_valuation_matches_explicit_rational() -> None:
    for segment in composite_indices(35):
        defect = franel_defect(segment)
        for prime in primes_through(100):
            direct = p_adic_valuation(defect.numerator, prime) - p_adic_valuation(
                defect.denominator, prime
            )
            assert franel_defect_valuation(segment, prime) == direct


def test_reduced_defect_certificates_are_exactly_nonzero() -> None:
    assert defect_certificate_66_residue() == DEFECT_66_DETERMINANT_RESIDUE == 4
    assert (
        defect_certificate_67_residue()
        == DEFECT_67_DETERMINANT_RESIDUE
        == 999_999
    )
    assert (
        defect_certificate_150_residue()
        == DEFECT_150_DETERMINANT_RESIDUE
        == 26_622
    )


def test_current_150_A_rows_are_exactly_the_canonical_prime_basis() -> None:
    assert A_certificate_rows_are_complete_prime_basis_150()
    assert len(primes_through(299)) == 62
    assert len(composite_indices(150)) == 88


def test_row_337_explains_global_composite_extension_not_local_F67_factor() -> None:
    # 337 does not divide F_67 itself.  It detects the residual relation among
    # older pure Franel defects, which is why it can close the 66->67 extension.
    assert p_adic_valuation(triple_moment_factor(67), 337) == 0
    assert franel_defect_valuation(67, 337) == 0
    assert segment_67_row_337_defect_support() == (
        (11, 1),
        (23, -1),
        (35, 1),
        (46, -1),
        (58, 1),
    )
