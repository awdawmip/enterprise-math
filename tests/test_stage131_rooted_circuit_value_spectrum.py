import unittest
from fractions import Fraction

from enterprise_math.stage131_rooted_circuit_table_explosion import (
    rooted_circuit_count,
)
from enterprise_math.stage131_rooted_circuit_value_spectrum import (
    availability_width_depth_spectrum,
    depth_cumulative_count_matches_closed,
    depth_width_support_matches_closed,
    exact_depth_width_interval_closed,
    materialization_round_saving,
    rooted_circuit_count_through_base_depth,
    rooted_circuit_depth_count_closed,
    rooted_circuit_depth_histogram,
    rooted_circuit_depth_opportunities,
    rooted_circuit_exact_base_depth_count,
    rooted_circuit_width_depth_spectrum,
    spectrum_marginals_match_parent_width_polynomial,
    spectrum_total_count,
    spectrum_width_histogram,
    widths_at_exact_base_depth,
)


class Stage131RootedCircuitValueSpectrumTests(unittest.TestCase):
    def test_small_exact_width_depth_spectra(self):
        self.assertEqual(rooted_circuit_width_depth_spectrum(1), {(2, 1): 1})
        self.assertEqual(
            rooted_circuit_width_depth_spectrum(2),
            {
                (2, 1): 1,
                (3, 2): 2,
                (4, 2): 1,
            },
        )
        self.assertEqual(
            rooted_circuit_width_depth_spectrum(3),
            {
                (2, 1): 1,
                (3, 2): 2,
                (4, 2): 1,
                (4, 3): 2,
                (5, 3): 4,
                (6, 3): 5,
                (7, 3): 6,
                (8, 3): 4,
            },
        )

    def test_width_marginal_matches_rooted_circuit_polynomial(self):
        for height in range(1, 9):
            self.assertTrue(spectrum_marginals_match_parent_width_polynomial(height))
            spectrum = rooted_circuit_width_depth_spectrum(height)
            self.assertEqual(spectrum_total_count(spectrum), rooted_circuit_count(height))

    def test_depth_cumulative_count_is_host_height_invariant(self):
        for host_height in range(1, 9):
            self.assertTrue(depth_cumulative_count_matches_closed(host_height))
            cumulative = 0
            histogram = rooted_circuit_depth_histogram(host_height)
            for depth in range(1, host_height + 1):
                cumulative += histogram[depth]
                self.assertEqual(
                    cumulative,
                    rooted_circuit_count(depth),
                )
                self.assertEqual(
                    rooted_circuit_count_through_base_depth(host_height, depth),
                    rooted_circuit_count(depth),
                )

    def test_exact_depth_counts_are_successive_circuit_count_differences(self):
        expected_h5 = {
            1: 1,
            2: 3,
            3: 21,
            4: 651,
            5: 457653,
        }
        self.assertEqual(rooted_circuit_depth_count_closed(5), expected_h5)
        for host_height in range(1, 9):
            histogram = rooted_circuit_depth_histogram(host_height)
            for depth in range(1, host_height + 1):
                self.assertEqual(
                    histogram[depth],
                    rooted_circuit_exact_base_depth_count(host_height, depth),
                )

    def test_every_exact_depth_has_dense_width_interval(self):
        for host_height in range(1, 8):
            self.assertTrue(depth_width_support_matches_closed(host_height))
            for depth in range(1, host_height + 1):
                lower, upper = exact_depth_width_interval_closed(depth)
                self.assertEqual(lower, depth + 1)
                self.assertEqual(upper, 1 << depth)
                self.assertEqual(
                    widths_at_exact_base_depth(host_height, depth),
                    tuple(range(depth + 1, (1 << depth) + 1)),
                )

    def test_height_five_opportunity_spectrum_is_dominated_by_deep_circuits(self):
        opportunities = rooted_circuit_depth_opportunities(5)
        self.assertEqual(tuple(item.depth for item in opportunities), (1, 2, 3, 4, 5))
        self.assertEqual(
            tuple(item.circuit_count for item in opportunities),
            (1, 3, 21, 651, 457653),
        )
        self.assertEqual(opportunities[-1].one_round_saving, 4)
        self.assertEqual(opportunities[-1].min_premise_width, 6)
        self.assertEqual(opportunities[-1].max_premise_width, 32)
        self.assertEqual(
            opportunities[-1].share_of_all_root_circuits,
            Fraction(457653, 458329),
        )
        self.assertGreater(opportunities[-1].share_of_all_root_circuits, Fraction(99, 100))

    def test_materialization_saving_is_depth_minus_one(self):
        for depth in range(1, 20):
            self.assertEqual(materialization_round_saving(depth), depth - 1)

    def test_availability_direct_seed_is_always_depth_zero(self):
        for height in range(0, 8):
            spectrum = availability_width_depth_spectrum(height)
            self.assertEqual(spectrum[(1, 0)], 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            rooted_circuit_width_depth_spectrum(0)
        with self.assertRaises(ValueError):
            rooted_circuit_exact_base_depth_count(4, 5)
        with self.assertRaises(ValueError):
            materialization_round_saving(0)


if __name__ == "__main__":
    unittest.main()
