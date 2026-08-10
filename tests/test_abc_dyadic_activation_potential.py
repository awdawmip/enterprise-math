import unittest
from fractions import Fraction

from enterprise_math.abc_dyadic_activation_potential import (
    biaxial_activation_potential,
)
from enterprise_math.abc_dyadic_threshold_staircase import dyadic_threshold_staircase


class DyadicActivationPotentialTests(unittest.TestCase):
    def setUp(self) -> None:
        self.old = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (
                Fraction(1, 22),
                Fraction(1, 2),
                Fraction(1),
                Fraction(11),
            ),
        )

    def test_threshold_area_derivative_is_crossing_span(self) -> None:
        potential = biaxial_activation_potential(self.old, Fraction(10))
        self.assertEqual(potential.old_area, 9)
        self.assertEqual(potential.new_threshold_crossing_depth, 2)
        self.assertEqual(potential.new_threshold_old_active_span, 2)
        self.assertEqual(potential.threshold_first_difference, 2)

    def test_orbit_area_derivative_is_new_node_rank(self) -> None:
        potential = biaxial_activation_potential(self.old, Fraction(10))
        self.assertEqual(
            potential.orbit_first_difference,
            potential.new_node_old_threshold_rank,
        )
        self.assertGreaterEqual(potential.new_node_old_threshold_rank, 3)

    def test_mixed_second_difference_is_active_corner_bit(self) -> None:
        potential = biaxial_activation_potential(self.old, Fraction(10))
        # The old final pressure is already >10 and the orbit is monotone, so
        # the appended node certainly lies above the new threshold.
        self.assertTrue(potential.new_corner_active)
        self.assertEqual(potential.mixed_difference_threshold_then_orbit, 1)
        self.assertEqual(potential.mixed_difference_orbit_then_threshold, 1)
        self.assertTrue(potential.corner_law_verified)

    def test_inactive_new_corner_gives_zero_mixed_difference(self) -> None:
        potential = biaxial_activation_potential(self.old, Fraction(10**100))
        self.assertFalse(potential.new_corner_active)
        self.assertEqual(potential.threshold_first_difference, 0)
        self.assertEqual(potential.mixed_difference_threshold_then_orbit, 0)
        self.assertEqual(potential.mixed_difference_orbit_then_threshold, 0)

    def test_area_reconstructs_from_first_differences_and_corner(self) -> None:
        potential = biaxial_activation_potential(self.old, Fraction(10))
        self.assertEqual(
            potential.biaxially_extended_area,
            potential.old_area
            + potential.threshold_first_difference
            + potential.orbit_first_difference
            + int(potential.new_corner_active),
        )

    def test_multi_threshold_jump_has_large_orbit_derivative_but_one_corner_bit(self) -> None:
        old = dyadic_threshold_staircase(
            7,
            17,
            2,
            0,
            (Fraction(1, 2), Fraction(1), Fraction(2)),
        )
        potential = biaxial_activation_potential(old, Fraction(3))
        self.assertEqual(potential.old_area, 0)
        # Appended rho_{4,-}=13/6 reaches all three old thresholds but not T=3.
        self.assertEqual(potential.orbit_first_difference, 3)
        self.assertFalse(potential.new_corner_active)
        self.assertEqual(potential.mixed_difference_threshold_then_orbit, 0)


if __name__ == "__main__":
    unittest.main()
