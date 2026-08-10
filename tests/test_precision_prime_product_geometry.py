import unittest

from enterprise_math.precision_prime_product_geometry import (
    prime_product_dimension_stable,
    prime_product_genesis_profiles,
    prime_product_geometry_profile,
)


class PrecisionPrimeProductGeometryTests(unittest.TestCase):
    def test_precision_one_is_zero_axis_one_state_pregeometry(self):
        profile = prime_product_geometry_profile(1)
        self.assertEqual(
            (profile.dimension, profile.axis_sizes, profile.vertex_count, profile.edge_count, profile.diameter),
            (0, (), 1, 0, 0),
        )

    def test_three_distinct_prime_axes_give_three_dimensional_candidate(self):
        profile = prime_product_geometry_profile(30)
        self.assertEqual(profile.dimension, 3)
        self.assertEqual(profile.axis_sizes, (2, 3, 5))
        self.assertEqual(profile.vertex_count, 30)
        self.assertEqual(profile.edge_count, 59)
        self.assertEqual(profile.diameter, 7)

    def test_precision_can_grow_while_candidate_dimension_stays_three(self):
        p30 = prime_product_geometry_profile(30)
        p60 = prime_product_geometry_profile(60)
        p180 = prime_product_geometry_profile(180)
        self.assertEqual((p30.dimension, p60.dimension, p180.dimension), (3, 3, 3))
        self.assertEqual((p30.vertex_count, p60.vertex_count, p180.vertex_count), (30, 60, 180))
        self.assertEqual((p30.axis_sizes, p60.axis_sizes, p180.axis_sizes), ((2, 3, 5), (4, 3, 5), (4, 9, 5)))
        self.assertEqual((p30.diameter, p60.diameter, p180.diameter), (7, 9, 15))
        self.assertTrue(prime_product_dimension_stable(30, 60))
        self.assertTrue(prime_product_dimension_stable(60, 180))

    def test_genesis_chain_has_zero_one_two_three_then_stable_rank(self):
        profiles = prime_product_genesis_profiles((1, 2, 6, 30, 60, 180))
        self.assertEqual(tuple(profile.dimension for profile in profiles), (0, 1, 2, 3, 3, 3))
        self.assertEqual(tuple(profile.vertex_count for profile in profiles), (1, 2, 6, 30, 60, 180))

    def test_new_prime_factor_is_candidate_dimension_increase(self):
        self.assertFalse(prime_product_dimension_stable(6, 30))

    def test_invalid_refinement_fails_closed(self):
        with self.assertRaises(ValueError):
            prime_product_dimension_stable(6, 20)
        with self.assertRaises(ValueError):
            prime_product_genesis_profiles((1, 6, 10))


if __name__ == "__main__":
    unittest.main()
