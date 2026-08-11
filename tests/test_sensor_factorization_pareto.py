import math
import unittest

from enterprise_math.sensor_factorization_pareto import (
    all_factorization_points,
    best_factorization_by_channel_budget,
    best_factorization_for_exact_channel_count,
    factorization_pareto_frontier,
    grouped_code_equivalent_to_fused_modulus,
    grouping_is_crt_exact,
    residue_bit_width,
    set_partitions,
)


class SensorFactorizationParetoTests(unittest.TestCase):
    def test_four_prime_set_has_bell_four_groupings(self):
        partitions = set_partitions((2, 3, 5, 7))
        self.assertEqual(len(partitions), 15)

    def test_every_grouping_has_same_crt_equality_code_as_mod_210(self):
        primes = (2, 3, 5, 7)
        for grouping in set_partitions(primes):
            self.assertTrue(grouping_is_crt_exact(primes, grouping))
            for left in range(-50, 261, 17):
                for right in range(-20, 281, 23):
                    self.assertEqual(
                        grouped_code_equivalent_to_fused_modulus(
                            primes,
                            grouping,
                            left,
                            right,
                        ),
                        left % 210 == right % 210,
                    )

    def test_exact_channel_count_optima_for_210(self):
        primes = (2, 3, 5, 7)

        one = best_factorization_for_exact_channel_count(primes, 1)
        self.assertEqual(one.channel_moduli, (210,))
        self.assertEqual(one.peak_bit_width, 8)
        self.assertEqual(one.total_rounded_bit_width, 8)

        two = best_factorization_for_exact_channel_count(primes, 2)
        self.assertEqual(set(two.channel_moduli), {14, 15})
        self.assertEqual(two.peak_bit_width, 4)
        self.assertEqual(two.total_rounded_bit_width, 8)

        three = best_factorization_for_exact_channel_count(primes, 3)
        self.assertEqual(set(three.channel_moduli), {5, 6, 7})
        self.assertEqual(three.peak_bit_width, 3)
        self.assertEqual(three.total_rounded_bit_width, 9)

        four = best_factorization_for_exact_channel_count(primes, 4)
        self.assertEqual(set(four.channel_moduli), {2, 3, 5, 7})
        self.assertEqual(four.peak_bit_width, 3)
        self.assertEqual(four.total_rounded_bit_width, 9)

    def test_pareto_frontier_drops_fully_split_point_when_peak_width_saturates(self):
        frontier = factorization_pareto_frontier((2, 3, 5, 7))
        resource_pairs = {(point.channel_count, point.peak_bit_width) for point in frontier}
        self.assertEqual(resource_pairs, {(1, 8), (2, 4), (3, 3)})
        self.assertNotIn((4, 3), resource_pairs)

    def test_channel_budget_four_prefers_three_channels_after_saturation(self):
        best = best_factorization_by_channel_budget((2, 3, 5, 7), 4)
        self.assertEqual(best.channel_count, 3)
        self.assertEqual(best.peak_bit_width, 3)
        self.assertEqual(set(best.channel_moduli), {5, 6, 7})

    def test_fusion_reduces_channels_and_cannot_reduce_peak_modulus(self):
        # Check the elementary monotonicity on every refinement pair obtained by
        # fusing the fully split 2,3,5,7 channels all the way to one channel.
        split_peak = max((2, 3, 5, 7))
        two_group_peak = max(14, 15)
        fused_peak = 210
        self.assertLess(split_peak, two_group_peak)
        self.assertLess(two_group_peak, fused_peak)
        self.assertLessEqual(residue_bit_width(split_peak), residue_bit_width(two_group_peak))
        self.assertLessEqual(residue_bit_width(two_group_peak), residue_bit_width(fused_peak))

    def test_product_and_information_content_are_grouping_invariant(self):
        points = all_factorization_points((2, 3, 5, 7))
        for point in points:
            self.assertEqual(math.prod(point.channel_moduli), 210)
            self.assertEqual(point.fused_modulus, 210)
            # Rounded machine storage can exceed the fused width due to per-channel
            # ceiling overhead, but never falls below it.
            self.assertGreaterEqual(point.total_rounded_bit_width, residue_bit_width(210))

    def test_validation(self):
        with self.assertRaises(ValueError):
            all_factorization_points(())
        with self.assertRaises(ValueError):
            all_factorization_points((2, 2))
        with self.assertRaises(ValueError):
            all_factorization_points((2, 4))
        with self.assertRaises(ValueError):
            best_factorization_for_exact_channel_count((2, 3), 3)


if __name__ == "__main__":
    unittest.main()
