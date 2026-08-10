from itertools import product

from enterprise_math.p022_barlow_marker_affine_semigroup import (
    coefficient_geometry_certifies_nonzero,
    coefficient_sign_class,
    half_defect_crossing_coefficients,
    half_defect_semigroup_certificate,
    negative_crossing_load_profile,
    numerical_semigroup_contains,
    positive_depth_cancellation_possible,
    same_sign_cancellation_possible,
)


def test_numerical_semigroup_membership_is_exact() -> None:
    assert numerical_semigroup_contains(0, (2, 3))
    assert not numerical_semigroup_contains(1, (2, 3))
    assert numerical_semigroup_contains(5, (2, 3))
    assert not numerical_semigroup_contains(7, (4, 6))
    assert numerical_semigroup_contains(8, (4, 6))


def test_sign_classes_and_exact_one_sign_logic() -> None:
    assert coefficient_sign_class(()) == "NONE"
    assert coefficient_sign_class((2, 4)) == "POSITIVE"
    assert coefficient_sign_class((-2, -4)) == "NEGATIVE"
    assert coefficient_sign_class((-2, 4)) == "MIXED"

    assert same_sign_cancellation_possible(3, ()) is False
    assert same_sign_cancellation_possible(3, (2, 4)) is False
    assert same_sign_cancellation_possible(1, (-2,)) is False
    assert same_sign_cancellation_possible(2, (-2,)) is True
    assert same_sign_cancellation_possible(5, (-2, -3)) is True
    assert same_sign_cancellation_possible(6, (-2, -3)) is False
    assert same_sign_cancellation_possible(3, (-2, 4)) is None


def test_mixed_sign_classification_is_exact_gcd_condition() -> None:
    assert positive_depth_cancellation_possible(2, (-4, 6))
    assert not positive_depth_cancellation_possible(1, (-4, 6))
    assert positive_depth_cancellation_possible(6, (-4, 10, 14))
    assert not positive_depth_cancellation_possible(5, (-4, 10, 14))

    # Cross-check the existential statement by bounded brute force on small
    # mixed generators.  A solution, when it exists, can be shifted through
    # an opposite-sign zero relation, so a modest bound catches these examples.
    examples = [(-2, 3), (-4, 6), (-3, 5, 10), (-4, 10, 14)]
    for coefficients in examples:
        for midpoint_depth in range(1, 9):
            predicted = positive_depth_cancellation_possible(midpoint_depth, coefficients)
            brute = any(
                midpoint_depth + sum(depth * coefficient for depth, coefficient in zip(depths, coefficients)) == 0
                for depths in product(range(1, 25), repeat=len(coefficients))
            )
            assert predicted == brute


def test_target_negative_marker_is_certified_without_exact_correction() -> None:
    assert half_defect_crossing_coefficients(369_581) == (-2,)
    assert negative_crossing_load_profile(1, (-2,)) == (2, -1, False)
    assert half_defect_semigroup_certificate(369_581, 1)


def test_vanishing_control_is_exactly_permitted_by_positive_depths() -> None:
    assert half_defect_crossing_coefficients(157) == (-1,)
    assert negative_crossing_load_profile(1, (-1,)) == (1, 0, True)
    assert positive_depth_cancellation_possible(1, (-1,))
    assert not half_defect_semigroup_certificate(157, 1)


def test_positive_crossings_are_automatically_safe() -> None:
    assert not positive_depth_cancellation_possible(1, (1,))
    assert coefficient_geometry_certifies_nonzero(1, (1,))
    assert coefficient_geometry_certifies_nonzero(5, (1, 3, 7))


def test_no_crossing_remains_automatically_safe() -> None:
    for prime in (23, 29, 47, 53, 71, 101, 149, 173, 239):
        assert half_defect_crossing_coefficients(prime) == ()
        assert half_defect_semigroup_certificate(prime, 1)
