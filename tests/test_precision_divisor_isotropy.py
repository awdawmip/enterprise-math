import unittest

from enterprise_math.precision_divisor_isotropy import (
    intrinsic_radius_two_anisotropy_witness,
    strong_sphere_transitivity_fails,
)


class PrecisionDivisorIsotropyTests(unittest.TestCase):
    def test_equal_exponent_three_axis_grid_still_has_intrinsic_anisotropy(self):
        # 30^4 = 2^4 * 3^4 * 5^4 gives the symmetric 5x5x5 exponent cube.
        scale = 30**4
        witness = intrinsic_radius_two_anisotropy_witness(scale)
        self.assertEqual(witness.center, (2, 2, 2))
        self.assertEqual(witness.first_target, (4, 2, 2))
        self.assertEqual(witness.second_target, (3, 3, 2))
        self.assertEqual(witness.common_distance, 2)
        self.assertEqual(witness.first_geodesic_count, 1)
        self.assertEqual(witness.second_geodesic_count, 2)
        self.assertTrue(strong_sphere_transitivity_fails(scale))

    def test_prime_labels_do_not_change_the_same_anisotropy_witness(self):
        first = intrinsic_radius_two_anisotropy_witness(30**4)
        second = intrinsic_radius_two_anisotropy_witness(42**4)
        self.assertEqual(
            (first.common_distance, first.first_geodesic_count, first.second_geodesic_count),
            (second.common_distance, second.first_geodesic_count, second.second_geodesic_count),
        )

    def test_too_small_or_one_axis_grid_fails_closed(self):
        with self.assertRaises(ValueError):
            intrinsic_radius_two_anisotropy_witness(30**2)
        with self.assertRaises(ValueError):
            intrinsic_radius_two_anisotropy_witness(2**5)


if __name__ == "__main__":
    unittest.main()
