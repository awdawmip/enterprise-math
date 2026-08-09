import unittest

from enterprise_math.p017_mirror_cross import aggregate_mirror_certificate
from enterprise_math.p017_mirror_directional import (
    directional_first_moments,
    directional_mirror_certificate,
    directional_precision_blocks,
    directional_prime_incidence_formula,
    dyadic_radius_block_index,
    minimum_directional_precision_level,
    terminal_radius_precision_level,
)


class P017MirrorDirectionalTests(unittest.TestCase):
    def test_directional_moments_sum_to_canonical_first_moment(self):
        for k in range(3, 120):
            directional = directional_first_moments(k)
            canonical = aggregate_mirror_certificate(k)
            self.assertEqual(directional["total_incidence"], canonical["first_incidence"])

    def test_per_prime_directional_counts_are_nonnegative(self):
        for k in (11, 31, 47, 83):
            center = k * (k + 1)
            for p in range(2, k + 1):
                try:
                    data = directional_prime_incidence_formula(k, p)
                except ValueError:
                    continue
                self.assertNotEqual(center % p, 0)
                self.assertGreaterEqual(data["lower"], 0)
                self.assertGreaterEqual(data["upper"], 0)

    def test_directional_certificate_subsumes_mc06_on_bounded_range(self):
        for k in range(3, 120):
            data = directional_mirror_certificate(k)
            if data["mc06_certificate"]:
                self.assertTrue(data["directional_certificate"], msg=f"k={k}")

    def test_fixed_directional_only_witnesses(self):
        witnesses = (137, 171, 233, 293, 336, 470, 570)
        for k in witnesses:
            data = directional_mirror_certificate(k)
            self.assertTrue(data["directional_certificate"], msg=f"k={k}")
            self.assertFalse(data["mc06_certificate"], msg=f"k={k}")

    def test_side_deficit_example(self):
        data = directional_mirror_certificate(137)
        self.assertEqual(data["surviving_radius_count"], 43)
        self.assertEqual((data["lower_incidence"], data["upper_incidence"]), (45, 41))
        self.assertTrue(data["upper_channel_certificate"])

    def test_product_only_example(self):
        data = directional_mirror_certificate(233)
        self.assertEqual((data["lower_slack"], data["upper_slack"]), (0, 4))
        self.assertEqual(data["simultaneous_excess_slack"], 1)
        self.assertTrue(data["product_violation_certificate"])
        self.assertFalse(data["mc06_certificate"])

    def test_non_witness_boundary(self):
        data = directional_mirror_certificate(31)
        self.assertEqual((data["lower_slack"], data["upper_slack"]), (0, 0))
        self.assertEqual(data["simultaneous_excess_slack"], 0)
        self.assertFalse(data["directional_certificate"])

    def test_mc08_level_zero_is_mc07(self):
        for k in (31, 137, 233):
            global_data = directional_mirror_certificate(k)
            precision = directional_precision_blocks(k, 0)
            self.assertEqual(
                precision["precision_certificate"],
                global_data["directional_certificate"],
            )
            self.assertEqual(len(precision["blocks"]), 1)
            block = precision["blocks"][0]
            self.assertEqual(block["lower_slack"], global_data["lower_slack"])
            self.assertEqual(block["upper_slack"], global_data["upper_slack"])
            self.assertEqual(
                block["simultaneous_excess_slack"],
                global_data["simultaneous_excess_slack"],
            )

    def test_dyadic_partition_is_nested(self):
        for k in range(3, 80):
            for level in range(0, 5):
                for radius in range(1, k):
                    parent = dyadic_radius_block_index(k, radius, level)
                    child = dyadic_radius_block_index(k, radius, level + 1)
                    self.assertEqual(child // 2, parent)

    def test_precision_certificate_persists_under_refinement(self):
        for k in range(3, 140):
            seen = False
            for level in range(0, min(6, terminal_radius_precision_level(k)) + 1):
                certified = directional_precision_blocks(k, level)["precision_certificate"]
                if seen:
                    self.assertTrue(certified, msg=f"k={k}, level={level}")
                seen |= certified

    def test_known_first_precision_levels(self):
        # These are fixed regression witnesses from the bounded pressure test.
        self.assertEqual(minimum_directional_precision_level(31, 3), 1)
        self.assertEqual(minimum_directional_precision_level(127, 4), 3)
        self.assertEqual(minimum_directional_precision_level(625, 5), 4)
        self.assertEqual(minimum_directional_precision_level(982, 5), 5)

    def test_terminal_level_has_singleton_nonempty_blocks(self):
        for k in range(3, 80):
            level = terminal_radius_precision_level(k)
            data = directional_precision_blocks(k, level)
            for block in data["blocks"]:
                self.assertEqual(block["surviving_radius_count"], 1)

    def test_fixed_low_precision_is_not_claimed_universal(self):
        # 32 blocks certify every k<=1000 in the research pressure test, but not
        # larger k uniformly.  k=2896 is a fixed counterexample to level 5.
        self.assertFalse(directional_precision_blocks(2896, 5)["precision_certificate"])
        self.assertTrue(directional_precision_blocks(2896, 6)["precision_certificate"])

    def test_validation(self):
        with self.assertRaises(ValueError):
            directional_mirror_certificate(1)
        with self.assertRaises(ValueError):
            directional_prime_incidence_formula(11, 4)
        with self.assertRaises(ValueError):
            directional_precision_blocks(11, -1)
        with self.assertRaises(ValueError):
            dyadic_radius_block_index(11, 0, 2)


if __name__ == "__main__":
    unittest.main()
