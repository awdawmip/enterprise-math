from fractions import Fraction
import unittest

from enterprise_math.brc_newton_quadratic_selector import (
    AffineQuadraticSelectorFamily,
    QuadraticSelectorState,
    evaluate_affine_quadratic_selector,
    quadratic_fixed_multiplicity,
    quadratic_selector_state,
    quadratic_smallest_real_selected,
)
from enterprise_math.brc_newton_schedule_strata import RationalAffineForm

Q = Fraction


def f(*coefficients):
    return RationalAffineForm(tuple(Q(value) for value in coefficients))


class NewtonQuadraticSelectorFoundationTests(unittest.TestCase):
    def test_one_parameter_witness_regimes(self):
        r = Q(-1)
        stable = quadratic_selector_state(Q(-3), Q(1), r)
        self.assertTrue(stable.fixed_multiplicity)
        self.assertGreater(stable.discriminant, 0)
        self.assertTrue(stable.smallest_real_selected)

        complex_case = quadratic_selector_state(Q(0), Q(1), r)
        self.assertLess(complex_case.discriminant, 0)
        self.assertTrue(complex_case.smallest_real_selected)

        collision = quadratic_selector_state(Q(2), Q(1), r)
        self.assertEqual(collision.root_value, 0)
        self.assertFalse(collision.fixed_multiplicity)
        self.assertFalse(collision.smallest_real_selected)

        unstable = quadratic_selector_state(Q(3), Q(1), r)
        self.assertGreater(unstable.discriminant, 0)
        self.assertFalse(unstable.smallest_real_selected)

    def test_discriminant_zero_not_sufficient(self):
        r = Q(-1)
        right = quadratic_selector_state(Q(-2), Q(1), r)  # (y-1)^2
        self.assertEqual(right.discriminant, 0)
        self.assertTrue(right.smallest_real_selected)
        left = quadratic_selector_state(Q(4), Q(4), r)  # (y+2)^2
        self.assertEqual(left.discriminant, 0)
        self.assertFalse(left.smallest_real_selected)

    def test_identity_and_chamber_signature(self):
        for a, b, r in ((-3, 1, -1), (0, 1, -1), (4, 4, -1), (1, 3, 2)):
            state = quadratic_selector_state(a, b, r)
            self.assertTrue(state.identity_holds)
            self.assertEqual(
                state.left_margin * state.left_margin - state.discriminant,
                4 * state.root_value,
            )
            self.assertEqual(len(state.chamber_signature), 3)

    def test_affine_family_evaluation(self):
        family = AffineQuadraticSelectorFamily(
            f(1, 2, -1),
            f(2, -1, 3),
            Q(-1),
        )
        self.assertEqual(family.parameter_count, 2)
        state = evaluate_affine_quadratic_selector(family, (Q(1), Q(2)))
        self.assertEqual(state.a, Q(1))
        self.assertEqual(state.b, Q(7))
        self.assertTrue(state.identity_holds)
        self.assertEqual(state, family.evaluate((Q(1), Q(2))))

    def test_function_facade(self):
        self.assertTrue(quadratic_fixed_multiplicity(-3, 1, -1))
        self.assertTrue(quadratic_smallest_real_selected(-3, 1, -1))
        self.assertFalse(quadratic_fixed_multiplicity(2, 1, -1))
        self.assertFalse(quadratic_smallest_real_selected(3, 1, -1))

    def test_type_and_dimension_guards(self):
        with self.assertRaises(TypeError):
            QuadraticSelectorState(True, Q(1), Q(-1))
        with self.assertRaises(ValueError):
            AffineQuadraticSelectorFamily(f(1, 2), f(1, 2, 3), Q(-1))
        family = AffineQuadraticSelectorFamily(f(1, 2), f(1, 3), Q(-1))
        with self.assertRaises(ValueError):
            family.evaluate((Q(1), Q(2)))
        with self.assertRaises(TypeError):
            evaluate_affine_quadratic_selector("bad", ())


if __name__ == "__main__":
    unittest.main()
