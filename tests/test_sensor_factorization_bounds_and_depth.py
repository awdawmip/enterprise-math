import unittest

from enterprise_math.sensor_factorization_execution_depth import (
    parallel_crt_reconstruction_depth,
    scalar_reconstruction_resource_pair,
    sensor_execution_point,
    sequential_crt_reconstruction_depth,
)
from enterprise_math.sensor_factorization_pareto import (
    best_factorization_for_exact_channel_count,
    information_peak_width_lower_bound,
    peak_width_lower_bound,
)


class SensorFactorizationBoundsAndDepthTests(unittest.TestCase):
    def test_210_optima_meet_information_plus_atomic_lower_bound(self):
        primes = (2, 3, 5, 7)
        expected_widths = {1: 8, 2: 4, 3: 3, 4: 3}
        for channels, expected in expected_widths.items():
            self.assertEqual(peak_width_lower_bound(primes, channels), expected)
            point = best_factorization_for_exact_channel_count(primes, channels)
            self.assertEqual(point.peak_bit_width, expected)
            self.assertTrue(point.meets_peak_width_lower_bound)
            self.assertEqual(point.peak_width_optimality_gap, 0)

    def test_information_lower_bound_alone_does_not_explain_full_split_saturation(self):
        # For four channels, information balance alone only says >=2 bits, but
        # the atomic prime7 already needs3 bits and forces the true lower bound3.
        self.assertEqual(information_peak_width_lower_bound(210, 4), 2)
        self.assertEqual(peak_width_lower_bound((2, 3, 5, 7), 4), 3)

    def test_crt_reconstruction_depths(self):
        expected_parallel = {1: 0, 2: 1, 3: 2, 4: 2, 5: 3, 8: 3, 9: 4}
        for channels, depth in expected_parallel.items():
            self.assertEqual(parallel_crt_reconstruction_depth(channels), depth)
            self.assertEqual(sequential_crt_reconstruction_depth(channels), channels - 1)

    def test_same_210_precision_trades_peak_width_for_scalar_reconstruction_depth(self):
        fused = sensor_execution_point((2, 3, 5, 7), ((2, 3, 5, 7),))
        two = sensor_execution_point((2, 3, 5, 7), ((2, 7), (3, 5)))
        three = sensor_execution_point((2, 3, 5, 7), ((2, 3), (5,), (7,)))
        split = sensor_execution_point((2, 3, 5, 7), ((2,), (3,), (5,), (7,)))

        self.assertEqual(scalar_reconstruction_resource_pair(fused), (8, 0))
        self.assertEqual(scalar_reconstruction_resource_pair(two), (4, 1))
        self.assertEqual(scalar_reconstruction_resource_pair(three), (3, 2))
        self.assertEqual(scalar_reconstruction_resource_pair(split), (3, 2))

        # Fully split is dominated by the three-channel grouping even under
        # scalar-reconstruction resources: same peak width/depth, more channels.
        self.assertEqual(split.peak_bit_width, three.peak_bit_width)
        self.assertEqual(
            split.parallel_scalar_reconstruction_depth,
            three.parallel_scalar_reconstruction_depth,
        )
        self.assertGreater(split.channel_count, three.channel_count)

    def test_tuple_native_interface_has_zero_reconstruction_depth_for_every_grouping(self):
        for grouping in (
            ((2, 3, 5, 7),),
            ((2, 7), (3, 5)),
            ((2, 3), (5,), (7,)),
            ((2,), (3,), (5,), (7,)),
        ):
            point = sensor_execution_point((2, 3, 5, 7), grouping)
            self.assertEqual(point.tuple_native_depth, 0)

    def test_validation(self):
        with self.assertRaises(ValueError):
            parallel_crt_reconstruction_depth(0)
        with self.assertRaises(ValueError):
            sequential_crt_reconstruction_depth(False)


if __name__ == "__main__":
    unittest.main()
