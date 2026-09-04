from fractions import Fraction
import unittest

from enterprise_math.brc_newton_quadratic_selector import (
    AffineQuadraticSelectorFamily,
    quadratic_positive_interval_root_count,
    quadratic_selector_state,
    quadratic_smallest_positive_compact_selected,
    quadratic_smallest_positive_selected,
    quadratic_sturm_variation,
)
from enterprise_math.brc_newton_schedule_strata import RationalAffineForm

Q = Fraction


def f(*coefficients):
    return RationalAffineForm(tuple(Q(value) for value in coefficients))


class NewtonQuadraticPositiveSelectorFoundationTests(unittest.TestCase):
    def test_one_parameter_mirror_witness(self):
        r = Q(1)
        unsafe = quadratic_selector_state(Q(-3), Q(1), r)
        self.assertEqual(unsafe.positive_interval_root_count, 1)
        self.assertFalse(unsafe.smallest_positive_selected)
        self.assertFalse(unsafe.smallest_positive_compact_selected)

        complex_case = quadratic_selector_state(Q(0), Q(1), r)
        self.assertEqual(complex_case.positive_interval_root_count, 0)
        self.assertTrue(complex_case.smallest_positive_selected)

        negative_competitors = quadratic_selector_state(Q(3), Q(1), r)
        self.assertEqual(negative_competitors.positive_interval_root_count, 0)
        self.assertTrue(negative_competitors.smallest_positive_selected)

        collision = quadratic_selector_state(Q(-2), Q(1), r)
        self.assertFalse(collision.fixed_multiplicity)
        self.assertFalse(collision.smallest_positive_selected)
        with self.assertRaises(ValueError):
            _ = collision.positive_interval_root_count

    def test_zero_root_endpoint_is_harmless(self):
        r = Q(1)
        right_or_nonpositive = quadratic_selector_state(Q(1), Q(0), r)  # roots 0,-1
        self.assertEqual(right_or_nonpositive.positive_interval_root_count, 0)
        self.assertTrue(right_or_nonpositive.smallest_positive_selected)

        interior = quadratic_selector_state(Q(-1, 2), Q(0), r)  # roots 0,1/2
        self.assertEqual(interior.positive_interval_root_count, 1)
        self.assertFalse(interior.smallest_positive_selected)

        beyond = quadratic_selector_state(Q(-2), Q(0), r)  # roots 0,2
        self.assertEqual(beyond.positive_interval_root_count, 0)
        self.assertTrue(beyond.smallest_positive_selected)

    def test_discriminant_zero_stable_and_unstable(self):
        r = Q(1)
        stable = quadratic_selector_state(Q(2), Q(1), r)  # (y+1)^2
        self.assertEqual(stable.discriminant, 0)
        self.assertEqual(stable.positive_interval_root_count, 0)
        self.assertTrue(stable.smallest_positive_selected)

        unstable = quadratic_selector_state(Q(-1), Q(1, 4), r)  # (y-1/2)^2
        self.assertEqual(unstable.discriminant, 0)
        self.assertEqual(unstable.positive_interval_root_count, 1)
        self.assertFalse(unstable.smallest_positive_selected)

    def test_sturm_variation_formula_and_compact_consistency(self):
        cases = (
            (-3, 1, 1),
            (0, 1, 1),
            (3, 1, 1),
            (-1, Q(1, 4), 1),
            (2, 1, 1),
            (-2, 0, 1),
            (1, 0, 1),
            (-3, -1, 2),
        )
        for a, b, r in cases:
            state = quadratic_selector_state(a, b, r)
            if state.fixed_multiplicity:
                expected = quadratic_sturm_variation((state.b, state.a, state.discriminant)) - quadratic_sturm_variation(
                    (state.root_value, 2 * state.declared_root + state.a, state.discriminant)
                )
                self.assertEqual(state.positive_interval_root_count, expected)
                self.assertTrue(state.positive_formula_consistent)
                self.assertEqual(
                    quadratic_smallest_positive_selected(a, b, r),
                    quadratic_smallest_positive_compact_selected(a, b, r),
                )

    def test_affine_family_positive_selector(self):
        family = AffineQuadraticSelectorFamily(f(0, 1), f(1, 0), Q(1))  # Q=y^2+t y+1
        self.assertFalse(family.evaluate((Q(-3),)).smallest_positive_selected)
        self.assertTrue(family.evaluate((Q(0),)).smallest_positive_selected)
        self.assertTrue(family.evaluate((Q(3),)).smallest_positive_selected)

    def test_smallest_positive_input_guards(self):
        nonpositive = quadratic_selector_state(Q(0), Q(1), Q(0))
        self.assertFalse(nonpositive.smallest_positive_selected)
        self.assertFalse(nonpositive.smallest_positive_compact_selected)
        with self.assertRaises(ValueError):
            _ = nonpositive.positive_interval_root_count
        with self.assertRaises(TypeError):
            quadratic_sturm_variation((Q(1), True, Q(-1)))
        with self.assertRaises(ValueError):
            quadratic_positive_interval_root_count(-2, 1, 1)  # Q(1)=0 collision


if __name__ == "__main__":
    unittest.main()
