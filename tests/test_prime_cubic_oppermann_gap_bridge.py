import unittest

from enterprise_math.prime_cubic_oppermann_gap_bridge import (
    KADIRI_LUMLEY_E59_DELTA,
    KADIRI_LUMLEY_E59_K_MAX,
    OLD_COMPLETE_PREFIX_MAX,
    OPPERMANN_INDEX_LIMIT,
    OPPERMANN_ONLY_K_MAX,
    PRIME_GAP_COVERAGE_LIMIT,
    ceil_sqrt_half_cube,
    cubic_root_horizon_pair,
    effective_relative_interval_fits,
    kadiri_lumley_e59_endpoint_arithmetic_holds,
    oppermann_endpoint_arithmetic_holds,
    oppermann_escape_forces_large_effective_scale,
    oppermann_index_covered,
    upper_closed_by_uniform_gap_cap,
    worst_q_gt_k_cofactor_floor,
)


class PrimeCubicOppermannGapBridgeTests(unittest.TestCase):
    def test_exact_oppermann_endpoint(self):
        self.assertEqual(
            ceil_sqrt_half_cube(OPPERMANN_ONLY_K_MAX),
            70_499_999_996_893,
        )
        self.assertEqual(
            ceil_sqrt_half_cube(OPPERMANN_ONLY_K_MAX + 1),
            70_500_000_046_075,
        )
        self.assertTrue(oppermann_endpoint_arithmetic_holds())

    def test_oppermann_coverage_has_exact_scale_complement(self):
        n2 = OPPERMANN_INDEX_LIMIT**2
        for k in range(3, 200):
            for q in range(2, k + 1):
                self.assertEqual(
                    oppermann_index_covered(k, q),
                    k**3 <= q * n2,
                )
                self.assertTrue(oppermann_escape_forces_large_effective_scale(k, q))

    def test_q_gt_k_cofactor_cutoff_is_exact(self):
        for k in range(2, 200):
            expected = max(k**3 // q for q in range(k + 1, 3 * k + 1))
            self.assertEqual(worst_q_gt_k_cofactor_floor(k), expected)
            self.assertEqual(worst_q_gt_k_cofactor_floor(k), k * k - k)

        self.assertEqual(
            worst_q_gt_k_cofactor_floor(OPPERMANN_ONLY_K_MAX),
            4_623_158_888_827_747_400,
        )
        self.assertEqual(
            worst_q_gt_k_cofactor_floor(KADIRI_LUMLEY_E59_K_MAX),
            34_092_151_333_005_523_140,
        )
        self.assertLess(
            worst_q_gt_k_cofactor_floor(KADIRI_LUMLEY_E59_K_MAX),
            PRIME_GAP_COVERAGE_LIMIT,
        )

    def test_exact_kadiri_lumley_e59_endpoint(self):
        k = KADIRI_LUMLEY_E59_K_MAX
        delta = KADIRI_LUMLEY_E59_DELTA
        self.assertTrue(effective_relative_interval_fits(k, delta))
        self.assertFalse(effective_relative_interval_fits(k + 1, delta))
        self.assertEqual(
            3 * (k + 1) * (delta - 1) - k * k,
            5_838_848_460,
        )
        self.assertEqual(
            3 * (k + 2) * (delta - 1) - (k + 1) * (k + 1),
            -1,
        )
        self.assertTrue(kadiri_lumley_e59_endpoint_arithmetic_holds())

    def test_uniform_1724_cap_closes_upper_after_old_prefix(self):
        first = OLD_COMPLETE_PREFIX_MAX + 1
        self.assertTrue(upper_closed_by_uniform_gap_cap(first))
        self.assertTrue(upper_closed_by_uniform_gap_cap(KADIRI_LUMLEY_E59_K_MAX))

        s0, f0, _ = cubic_root_horizon_pair(first)
        self.assertEqual(f0 - s0, 3628)

        s1, f1, _ = cubic_root_horizon_pair(KADIRI_LUMLEY_E59_K_MAX)
        self.assertEqual(f1 - s1, 114_619)


if __name__ == "__main__":
    unittest.main()
