import unittest

from enterprise_math.sensor_factorization_pareto import all_factorization_points
from enterprise_math.sensor_factorization_storage_law import (
    fused_residue_bit_width,
    rounded_storage_overhead,
    rounded_storage_overhead_bound,
    verify_rounded_storage_law,
)


class SensorFactorizationStorageLawTests(unittest.TestCase):
    def test_every_2_3_5_7_factorization_obeys_g_minus_one_overhead(self):
        for point in all_factorization_points((2, 3, 5, 7)):
            self.assertTrue(verify_rounded_storage_law(point))
            self.assertGreaterEqual(rounded_storage_overhead(point), 0)
            self.assertLessEqual(
                rounded_storage_overhead(point),
                rounded_storage_overhead_bound(point),
            )

    def test_210_reference_storage_points(self):
        by_moduli = {
            frozenset(point.channel_moduli): point
            for point in all_factorization_points((2, 3, 5, 7))
        }
        fused = by_moduli[frozenset({210})]
        balanced_two = by_moduli[frozenset({14, 15})]
        balanced_three = by_moduli[frozenset({5, 6, 7})]
        split = by_moduli[frozenset({2, 3, 5, 7})]

        self.assertEqual(fused_residue_bit_width(fused), 8)
        self.assertEqual(rounded_storage_overhead(fused), 0)
        self.assertEqual(rounded_storage_overhead(balanced_two), 0)
        self.assertEqual(rounded_storage_overhead(balanced_three), 1)
        self.assertEqual(rounded_storage_overhead(split), 1)

    def test_storage_overhead_bound_on_several_prime_sets(self):
        for primes in (
            (2, 3),
            (2, 3, 5),
            (3, 5, 7, 11),
            (7, 11, 13),
        ):
            for point in all_factorization_points(primes):
                self.assertTrue(verify_rounded_storage_law(point))


if __name__ == "__main__":
    unittest.main()
