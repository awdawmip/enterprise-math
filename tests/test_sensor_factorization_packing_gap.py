import unittest

from enterprise_math.sensor_factorization_pareto import (
    best_factorization_for_exact_channel_count,
    peak_width_lower_bound,
)


class SensorFactorizationPackingGapTests(unittest.TestCase):
    def test_7_11_13_two_channel_continuous_lower_bound_is_unattainable(self):
        primes = (7, 11, 13)
        lower = peak_width_lower_bound(primes, 2)
        best = best_factorization_for_exact_channel_count(primes, 2)

        self.assertEqual(lower, 5)
        self.assertEqual(best.peak_bit_width, 7)
        self.assertEqual(best.peak_width_optimality_gap, 2)
        self.assertEqual(set(best.channel_moduli), {13, 77})

    def test_packing_gap_disappears_after_three_way_split(self):
        primes = (7, 11, 13)
        best = best_factorization_for_exact_channel_count(primes, 3)
        self.assertEqual(best.peak_bit_width, 4)
        self.assertEqual(best.peak_width_lower_bound, 4)
        self.assertEqual(best.peak_width_optimality_gap, 0)

    def test_210_balanced_points_have_zero_packing_gap(self):
        primes = (2, 3, 5, 7)
        for channels in (1, 2, 3, 4):
            best = best_factorization_for_exact_channel_count(primes, channels)
            self.assertEqual(best.peak_width_optimality_gap, 0)


if __name__ == "__main__":
    unittest.main()
