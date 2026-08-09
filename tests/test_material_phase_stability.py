import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_phase_stability import (
    exact_first_nonpositive_x_step,
    phase_sign_stability_profile,
    projected_first_nonpositive_x_step,
    x_sign_certificate_holds,
    x_sign_itinerary_amplitude_bound,
)


class MaterialPhaseStabilityTests(unittest.TestCase):
    def setUp(self):
        self.rotation = PythagoreanRotation(399, 40, 401)

    def test_reference_exact_quarter_x_crossing_is_step_16(self):
        self.assertEqual(exact_first_nonpositive_x_step(self.rotation, 100), 16)

    def test_conservative_reference_sign_bound_is_finite_and_sufficient(self):
        bound = x_sign_itinerary_amplitude_bound(self.rotation, 16)
        self.assertEqual(bound, 2461)
        self.assertTrue(x_sign_certificate_holds(bound, self.rotation, 16))
        self.assertEqual(
            projected_first_nonpositive_x_step(bound, self.rotation, 100),
            16,
        )

    def test_bound_profile_starts_exactly_at_zero_discrepancy(self):
        profile = phase_sign_stability_profile(self.rotation, 3)
        self.assertEqual(profile[0].unit_exact, (1, 0))
        self.assertEqual(profile[0].scale, 1)
        self.assertEqual(profile[0].l1_discrepancy_bound, 0)
        self.assertEqual(profile[0].minimum_amplitude_for_x_sign, 1)
        self.assertIsNone(profile[0].minimum_amplitude_for_y_sign)
        for left, right in zip(profile, profile[1:]):
            self.assertEqual(right.scale, left.scale * self.rotation.c)
            self.assertGreaterEqual(
                right.l1_discrepancy_bound,
                left.l1_discrepancy_bound,
            )

    def test_observed_reference_crossing_stabilizes_much_below_worst_case_bound(self):
        # This is a bounded regression, not the theorem.  A direct scan found
        # all amplitudes 61..2000 cross at the same exact lifted step 16.
        for amplitude in range(61, 2001):
            self.assertEqual(
                projected_first_nonpositive_x_step(amplitude, self.rotation, 30),
                16,
            )

    def test_low_amplitude_phase_collapse_can_cross_at_other_steps(self):
        observed = {
            projected_first_nonpositive_x_step(amplitude, self.rotation, 30)
            for amplitude in range(1, 61)
        }
        self.assertGreater(len(observed), 1)
        self.assertIn(15, observed)
        self.assertIn(16, observed)
        self.assertIn(17, observed)

    def test_other_small_rotation_has_finite_sign_bound(self):
        rotation = PythagoreanRotation(3, 4, 5)
        crossing = exact_first_nonpositive_x_step(rotation, 20)
        self.assertIsNotNone(crossing)
        bound = x_sign_itinerary_amplitude_bound(rotation, crossing)
        self.assertGreater(bound, 0)
        self.assertTrue(x_sign_certificate_holds(bound, rotation, crossing))


if __name__ == "__main__":
    unittest.main()
