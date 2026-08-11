import unittest

from enterprise_math.prime_cubic_oppermann_gap_bridge import (
    COMBINED_K_MAX,
    OLD_COMPLETE_PREFIX_MAX,
    OPPERMANN_INDEX_LIMIT,
    PRIME_GAP_COVERAGE_LIMIT,
    ceil_sqrt_half_cube,
    combined_endpoint_arithmetic_holds,
    cubic_root_horizon_pair,
    upper_closed_by_uniform_gap_cap,
    worst_q_gt_k_cofactor_floor,
)


class PrimeCubicOppermannGapBridgeTests(unittest.TestCase):
    def test_exact_oppermann_endpoint(self):
        self.assertEqual(
            ceil_sqrt_half_cube(COMBINED_K_MAX),
            70_499_999_996_893,
        )
        self.assertEqual(
            ceil_sqrt_half_cube(COMBINED_K_MAX + 1),
            70_500_000_046_075,
        )
        self.assertLessEqual(
            ceil_sqrt_half_cube(COMBINED_K_MAX),
            OPPERMANN_INDEX_LIMIT,
        )
        self.assertGreater(
            ceil_sqrt_half_cube(COMBINED_K_MAX + 1),
            OPPERMANN_INDEX_LIMIT,
        )

    def test_q_gt_k_cofactor_cutoff_is_exact(self):
        for k in range(2, 200):
            expected = max(k**3 // q for q in range(k + 1, 3 * k + 1))
            self.assertEqual(worst_q_gt_k_cofactor_floor(k), expected)
            self.assertEqual(worst_q_gt_k_cofactor_floor(k), k * k - k)

        self.assertEqual(
            worst_q_gt_k_cofactor_floor(COMBINED_K_MAX),
            4_623_158_888_827_747_400,
        )
        self.assertLess(
            worst_q_gt_k_cofactor_floor(COMBINED_K_MAX),
            PRIME_GAP_COVERAGE_LIMIT,
        )

    def test_uniform_1724_cap_closes_upper_after_old_prefix(self):
        first = OLD_COMPLETE_PREFIX_MAX + 1
        self.assertTrue(upper_closed_by_uniform_gap_cap(first))
        self.assertTrue(upper_closed_by_uniform_gap_cap(COMBINED_K_MAX))

        s0, f0, _ = cubic_root_horizon_pair(first)
        self.assertEqual(f0 - s0, 3628)

        s1, f1, _ = cubic_root_horizon_pair(COMBINED_K_MAX)
        self.assertEqual(f1 - s1, 69_555)

    def test_frozen_combined_endpoint_packet(self):
        self.assertTrue(combined_endpoint_arithmetic_holds())


if __name__ == "__main__":
    unittest.main()
