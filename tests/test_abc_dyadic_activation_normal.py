import unittest
from fractions import Fraction

from enterprise_math.abc_dyadic_activation_normal import (
    dyadic_activation_normal_form,
    signed_seed_activation_bound,
    suffix_profile_from_first_depth,
)


class DyadicActivationNormalFormTests(unittest.TestCase):
    def test_reconstructs_every_suffix_profile_from_one_depth(self) -> None:
        self.assertEqual(
            suffix_profile_from_first_depth(3, None),
            (False, False, False, False),
        )
        self.assertEqual(
            suffix_profile_from_first_depth(3, 0),
            (True, True, True, True),
        )
        self.assertEqual(
            suffix_profile_from_first_depth(3, 2),
            (False, False, True, True),
        )
        self.assertEqual(
            suffix_profile_from_first_depth(3, 3),
            (False, False, False, True),
        )

    def test_exact_nontrivial_first_crossing_depth_two(self) -> None:
        state = dyadic_activation_normal_form(3, 41, 2, 3)
        self.assertEqual(state.exponents, (2, 4, 8, 16))
        self.assertEqual(
            state.pressures,
            (
                Fraction(1, 22),
                Fraction(13, 22),
                Fraction(221, 22),
                Fraction(221, 22),
            ),
        )
        self.assertEqual(
            state.activation_profile,
            (False, False, True, True),
        )
        self.assertEqual(state.first_activation_depth, 2)
        self.assertEqual(state.first_activation_exponent, 8)
        self.assertTrue(state.suffix_verified)

    def test_already_active_and_never_active_are_boundary_normal_forms(self) -> None:
        active = dyadic_activation_normal_form(23, 41, 2, 3)
        self.assertEqual(active.first_activation_depth, 0)
        self.assertEqual(active.activation_profile, (True, True, True, True))

        inactive = dyadic_activation_normal_form(3, 5, 2, 3)
        self.assertIsNone(inactive.first_activation_depth)
        self.assertEqual(inactive.activation_profile, (False, False, False, False))

    def test_threshold_is_future_relative(self) -> None:
        unit = dyadic_activation_normal_form(3, 41, 2, 3, Fraction(1, 1))
        ten = dyadic_activation_normal_form(3, 41, 2, 3, Fraction(10, 1))
        eleven = dyadic_activation_normal_form(3, 41, 2, 3, Fraction(11, 1))
        self.assertEqual(unit.first_activation_depth, 2)
        self.assertEqual(ten.first_activation_depth, 2)
        self.assertIsNone(eleven.first_activation_depth)

    def test_monotonicity_collapses_boolean_profile_state_space(self) -> None:
        state = dyadic_activation_normal_form(3, 41, 2, 8)
        self.assertEqual(state.profile_state_count, 10)
        self.assertEqual(state.unconstrained_boolean_state_count, 512)
        self.assertLess(state.profile_state_count, state.unconstrained_boolean_state_count)

    def test_active_sum_seed_forces_difference_activation_by_depth_one(self) -> None:
        data = signed_seed_activation_bound(5, 59, 3)
        self.assertFalse(data["lower_difference_active"])
        self.assertTrue(data["lower_sum_active"])
        self.assertTrue(data["doubled_difference_active"])
        self.assertEqual(data["first_difference_activation_depth_upper_bound"], 1)

    def test_active_difference_seed_has_depth_zero(self) -> None:
        data = signed_seed_activation_bound(23, 41, 2)
        self.assertTrue(data["lower_difference_active"])
        self.assertEqual(data["first_difference_activation_depth_upper_bound"], 0)


if __name__ == "__main__":
    unittest.main()
